#!/usr/bin/env python3
"""Statically validate ThinkAlong's Skill, repository metadata and local links."""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FRONTMATTER = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}
PACKAGE_FILES = (
    ("SKILL.md", "skills/think-along/SKILL.md"),
    ("LICENSE", "LICENSE"),
    ("agents/openai.yaml", "skills/think-along/agents/openai.yaml"),
    ("references/workflow.md", "skills/think-along/references/workflow.md"),
    ("references/acceptance-checks.md", "skills/think-along/references/acceptance-checks.md"),
    ("references/examples.md", "skills/think-along/references/examples.md"),
)


def load_yaml(text: str):
    """Use safe YAML parsing without silently accepting overwritten keys."""
    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node)
            if key in result:
                raise ValueError(f"duplicate YAML key: {key}")
            result[key] = loader.construct_object(value_node)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    return yaml.load(text, Loader=UniqueLoader)


def frontmatter(text: str):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    data = load_yaml(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data, text[match.end():]


def validate(root: Path = ROOT) -> list[str]:
    if yaml is None:
        raise RuntimeError("PyYAML missing; install requirements-dev.txt")
    root = root.resolve()
    errors: list[str] = []
    required = [
        "AGENTS.md", "README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
        "SECURITY.md", "skills/think-along/SKILL.md", "skills/think-along/agents/openai.yaml",
        "skills/think-along/references/workflow.md",
        "skills/think-along/references/acceptance-checks.md",
        "skills/think-along/references/examples.md",
        "adapters/portable-instructions.md", "docs/platform-compatibility.md",
        "docs/audit-summary.md", "docs/release-checklist.md", "docs/github-metadata.md",
        "docs/research-summary.md", "evals/protocol.md", "evals/scoring-rubric.md",
        "requirements-dev.txt", "scripts/package_skill.py",
        ".github/workflows/validate.yml",
    ]
    for item in required:
        if not (root / item).is_file():
            errors.append(f"missing required file: {item}")

    source = root / "skills/think-along"
    package_sources = {root / relative for _, relative in PACKAGE_FILES}
    for path in sorted(package_sources):
        if any(part.is_symlink() for part in (path, *path.parents) if part != root and root in part.parents):
            errors.append(f"package input must not be a symlink: {path.relative_to(root)}")

    for script in sorted((root / "scripts").glob("*.py")):
        try:
            ast.parse(script.read_text(encoding="utf-8"), filename=str(script.relative_to(root)))
        except (SyntaxError, UnicodeError, OSError) as exc:
            errors.append(f"invalid Python source {script.relative_to(root)}: {exc}")

    skill_path = root / "skills/think-along/SKILL.md"
    if skill_path.is_file():
        try:
            skill, body = frontmatter(skill_path.read_text(encoding="utf-8"))
            unknown = set(skill) - ALLOWED_FRONTMATTER
            if unknown:
                errors.append(f"unsupported SKILL.md frontmatter key(s): {', '.join(sorted(unknown))}")
            name = skill.get("name")
            if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                errors.append("skill name must be lowercase hyphen-case, 1-64 characters")
            elif name != "think-along":
                errors.append("skill name must match the canonical name think-along")
            desc = skill.get("description")
            if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024 or "<" in desc or ">" in desc:
                errors.append("skill description must be 1-1024 characters and contain no angle brackets")
            if skill.get("license") != "MIT":
                errors.append("skill license must be MIT")
            if "compatibility" in skill and (not isinstance(skill["compatibility"], str)
                                             or not skill["compatibility"].strip()
                                             or not 1 <= len(skill["compatibility"]) <= 500):
                errors.append("compatibility must be a string of 1-500 characters when present")
            if "allowed-tools" in skill and not isinstance(skill["allowed-tools"], str):
                errors.append("allowed-tools must be a space-separated string when present")
            if "metadata" in skill and not isinstance(skill["metadata"], dict):
                errors.append("metadata must be a YAML mapping when present")
            elif isinstance(skill.get("metadata"), dict):
                if any(not isinstance(k, str) or not isinstance(v, str) for k, v in skill["metadata"].items()):
                    errors.append("metadata keys and values must be strings")
                version = skill["metadata"].get("version")
                if version != "0.4.0":
                    errors.append("skill metadata version must match 0.4.0")
            if len(body.splitlines()) > 500:
                errors.append("skill body exceeds 500 lines")
            for phrase in ("outcome contract", "repair loop", "acceptance-checks.md", "examples.md"):
                if phrase.lower() not in body.lower():
                    errors.append(f"SKILL.md is missing core mechanism/reference: {phrase}")
        except Exception as exc:
            errors.append(f"invalid SKILL.md: {exc}")
    else:
        errors.append("cannot validate SKILL.md because it is missing")

    metadata_path = root / "skills/think-along/agents/openai.yaml"
    if metadata_path.is_file():
        try:
            metadata = load_yaml(metadata_path.read_text(encoding="utf-8"))
            interface = metadata.get("interface") if isinstance(metadata, dict) else None
            if not isinstance(interface, dict):
                errors.append("agents/openai.yaml requires interface mapping")
            else:
                short = interface.get("short_description")
                prompt = interface.get("default_prompt")
                if interface.get("display_name") != "ThinkAlong":
                    errors.append("display_name must be ThinkAlong")
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    errors.append("short_description must be 25-64 characters")
                if not isinstance(prompt, str) or "$think-along" not in prompt:
                    errors.append("default_prompt must explicitly invoke $think-along")
            policy = metadata.get("policy") if isinstance(metadata, dict) else None
            if not isinstance(policy, dict) or policy.get("allow_implicit_invocation") is not True:
                errors.append("agents/openai.yaml requires policy.allow_implicit_invocation: true")
        except Exception as exc:
            errors.append(f"invalid agents/openai.yaml: {exc}")

    # Validate local Markdown links and reject links escaping the repository.
    link_re = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
    for md in root.rglob("*.md"):
        if any(part in {".git", "dist", "__pycache__"} for part in md.parts):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as exc:
            errors.append(f"cannot read Markdown {md.relative_to(root)}: {exc}")
            continue
        for target in link_re.findall(text):
            target = target.split("#", 1)[0].strip().strip("<>")
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"link escapes repository: {md.relative_to(root)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {md.relative_to(root)} -> {target}")
            if source in md.parents:
                if resolved not in package_sources:
                    errors.append(f"link escapes Skill package or targets an unbundled file: {md.relative_to(root)} -> {target}")

    workflow_path = root / ".github/workflows/validate.yml"
    if workflow_path.is_file():
        try:
            workflow = load_yaml(workflow_path.read_text(encoding="utf-8"))
            job = workflow["jobs"]["validate"]
            if "if" in job or job.get("continue-on-error", False) is not False:
                errors.append("CI validate job must be unconditional and must not allow failure")
            steps = job["steps"]
            if not isinstance(steps, list) or any(not isinstance(step, dict) for step in steps):
                raise ValueError("validate job requires a list of step mappings")
            # Conservative repository contract, not a GitHub expression/shell evaluator.
            # Required checks use standalone commands, no conditions or tolerated failures.
            required_steps = [
                step for step in steps
                if "if" not in step and step.get("continue-on-error", False) is False
            ]
            actions = {step["uses"] for step in required_steps if isinstance(step.get("uses"), str)}
            commands = {
                step["run"].strip()
                for step in required_steps if isinstance(step.get("run"), str)
            }
            for action in ("actions/checkout@v7", "actions/setup-python@v7"):
                if action not in actions:
                    errors.append(f"CI requires an unconditional, failure-propagating action step: {action}")
            for command in ("python scripts/validate_skill.py", "python scripts/package_skill.py"):
                if command not in commands:
                    errors.append(f"CI requires an unconditional, failure-propagating standalone command: {command}")
        except (KeyError, TypeError, ValueError, yaml.YAMLError, OSError) as exc:
            errors.append(f"invalid CI workflow: {exc}")

    return errors


def main() -> int:
    try:
        errors = validate()
    except Exception as exc:
        print(f"ThinkAlong validation could not run: {exc}", file=sys.stderr)
        return 2
    print(f"ThinkAlong validation: {len(errors)} error(s).")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if not errors:
        print("PASS: required files, Python syntax, Skill frontmatter, metadata/invocation policy, package references, local links, and CI steps.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
