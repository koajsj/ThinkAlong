#!/usr/bin/env python3
"""Validate and package only runtime Skill files."""
from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "think-along"
DIST = ROOT / "dist"
FILES = [
    ("SKILL.md", SOURCE / "SKILL.md"),
    ("LICENSE", ROOT / "LICENSE"),
    ("agents/openai.yaml", SOURCE / "agents" / "openai.yaml"),
    ("references/workflow.md", SOURCE / "references" / "workflow.md"),
]


def main() -> int:
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skill.py")], cwd=ROOT)
    if result.returncode:
        print("Refusing to package: validation failed.", file=sys.stderr)
        return result.returncode
    missing = [name for name, path in FILES if not path.is_file()]
    if missing:
        print(f"Missing package files: {missing}", file=sys.stderr)
        return 1
    DIST.mkdir(exist_ok=True)
    archive = DIST / "think-along.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for name, path in FILES:
            zf.write(path, Path("think-along") / name)
    with zipfile.ZipFile(archive) as zf:
        expected = {str(Path("think-along") / name) for name, _ in FILES}
        if zf.testzip() is not None or set(zf.namelist()) != expected:
            print("Package integrity or contents check failed.", file=sys.stderr)
            return 1
    print(f"Created {archive.relative_to(ROOT)} ({archive.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
