#!/usr/bin/env python3
"""Validate ThinkAlong's Agent Skill, repository metadata, eval cases, and local links."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
TASK_IDS = {f"E{i:02d}" for i in range(1, 31)}
TRIGGER_IDS = {f"T{i:02d}" for i in range(1, 31)}
ALLOWED_FRONTMATTER = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}


def frontmatter(text: str):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data, text[match.end():]


def case_ids(text: str, prefix: str) -> list[str]:
    return re.findall(rf"(?m)^\|\s*({prefix}\d{{2}})\s*\|", text)


def validate(root: Path = ROOT) -> list[str]:
    if yaml is None:
        raise RuntimeError("PyYAML missing; install requirements-dev.txt")
    root = root.resolve()
    errors: list[str] = []
    required = [
        "README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
        "SECURITY.md", "skills/think-along/SKILL.md", "skills/think-along/agents/openai.yaml",
        "skills/think-along/references/workflow.md",
        "skills/think-along/references/acceptance-checks.md",
        "skills/think-along/references/examples.md",
        "adapters/portable-instructions.md", "docs/platform-compatibility.md",
        "docs/audit-summary.md", "docs/release-checklist.md", "docs/github-metadata.md",
        "evals/task-cases.md", "evals/trigger-cases.md", "evals/scoring-rubric.md",
        "requirements-dev.txt", "scripts/package_skill.py", "tests/test_validate_skill.py",
        ".github/workflows/validate.yml",
    ]
    for item in required:
        if not (root / item).is_file():
            errors.append(f"missing required file: {item}")

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
            if "compatibility" in skill and not isinstance(skill["compatibility"], str):
                errors.append("compatibility must be a string when present")
            if "allowed-tools" in skill and not isinstance(skill["allowed-tools"], (str, list)):
                errors.append("allowed-tools must be a string or list when present")
            if "metadata" in skill and not isinstance(skill["metadata"], dict):
                errors.append("metadata must be a YAML mapping when present")
            elif isinstance(skill.get("metadata"), dict):
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
            metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
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
        except Exception as exc:
            errors.append(f"invalid agents/openai.yaml: {exc}")

    for relative, prefix, expected in [
        ("evals/task-cases.md", "E", TASK_IDS),
        ("evals/trigger-cases.md", "T", TRIGGER_IDS),
    ]:
        path = root / relative
        if not path.is_file():
            continue
        try:
            ids = case_ids(path.read_text(encoding="utf-8"), prefix)
            if len(ids) != len(set(ids)) or set(ids) != expected or len(ids) != len(expected):
                errors.append(f"{relative} must contain exactly {len(expected)} unique cases")
        except Exception as exc:
            errors.append(f"cannot validate {relative}: {exc}")

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

    workflow_path = root / ".github/workflows/validate.yml"
    if workflow_path.is_file():
        workflow_text = workflow_path.read_text(encoding="utf-8")
        if "actions/checkout@v7" not in workflow_text:
            errors.append("CI should use actions/checkout@v7 or a reviewed newer version")
        if "actions/setup-python@v7" not in workflow_text:
            errors.append("CI should use actions/setup-python@v7 or a reviewed newer version")
        for command in (
            "python scripts/validate_skill.py",
            "python -m unittest discover -s tests -v",
            "python scripts/package_skill.py",
        ):
            if command not in workflow_text:
                errors.append(f"CI workflow is missing command: {command}")

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
        print("PASS: required files, Skill frontmatter, metadata, exact eval sets, local links, and CI commands.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
