#!/usr/bin/env python3
"""Validate ThinkAlong repository metadata, case sets, links, and package inputs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
TASK_IDS = {f"E{i:02d}" for i in range(1, 21)}
TRIGGER_IDS = {f"T{i:02d}" for i in range(1, 21)}


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
    errors: list[str] = []
    required = [
        "README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
        "SECURITY.md", "skills/think-along/SKILL.md", "skills/think-along/agents/openai.yaml",
        "skills/think-along/references/workflow.md", "adapters/portable-instructions.md",
        "docs/platform-compatibility.md", "docs/audit-summary.md", "docs/release-checklist.md",
        "evals/task-cases.md", "evals/trigger-cases.md", "requirements-dev.txt",
        "scripts/package_skill.py", "tests/test_validate_skill.py", ".github/workflows/validate.yml",
    ]
    for item in required:
        if not (root / item).is_file():
            errors.append(f"missing required file: {item}")

    try:
        skill, body = frontmatter((root / "skills/think-along/SKILL.md").read_text(encoding="utf-8"))
        if skill.get("name") != "think-along":
            errors.append("skill name must be think-along")
        desc = skill.get("description")
        if not isinstance(desc, str) or not desc.strip() or len(desc) > 200:
            errors.append("skill description must be 1-200 characters")
        if skill.get("license") != "MIT":
            errors.append("skill license must be MIT")
        if len(body.splitlines()) > 500:
            errors.append("skill body exceeds 500 lines")
        if "references/workflow.md" not in body:
            errors.append("skill must link to references/workflow.md")
    except Exception as exc:
        errors.append(f"invalid SKILL.md: {exc}")

    try:
        metadata = yaml.safe_load((root / "skills/think-along/agents/openai.yaml").read_text(encoding="utf-8"))
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
        try:
            ids = case_ids((root / relative).read_text(encoding="utf-8"), prefix)
            if len(ids) != len(set(ids)) or set(ids) != expected or len(ids) != len(expected):
                errors.append(f"{relative} must contain exactly {len(expected)} unique cases")
        except Exception as exc:
            errors.append(f"cannot validate {relative}: {exc}")

    # Validate local Markdown links and reject links escaping the repository.
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in root.rglob("*.md"):
        if ".git" in md.parts or "dist" in md.parts:
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"invalid UTF-8: {md.relative_to(root)}")
            continue
        for target in link_re.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {md.relative_to(root)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {md.relative_to(root)} -> {target}")

    return errors


def main() -> int:
    errors = validate()
    print(f"ThinkAlong validation: {0 if errors else 1} overall result; {len(errors)} errors.")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if not errors:
        print("PASS: required files, YAML metadata, exact case sets, and local Markdown links.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
