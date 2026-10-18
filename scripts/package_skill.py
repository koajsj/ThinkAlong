#!/usr/bin/env python3
"""Validate and package only the runtime ThinkAlong Skill files."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from validate_skill import PACKAGE_FILES

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
FILES = [(name, ROOT / relative) for name, relative in PACKAGE_FILES]


def main() -> int:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_skill.py")],
        cwd=ROOT,
        check=False,
    )
    if result.returncode:
        print("Refusing to package: validation failed.", file=sys.stderr)
        return result.returncode
    missing = [name for name, path in FILES if not path.is_file()]
    if missing:
        print(f"Missing package files: {missing}", file=sys.stderr)
        return 1
    if DIST.is_symlink():
        print("Refusing to package: dist must not be a symlink.", file=sys.stderr)
        return 1
    DIST.mkdir(exist_ok=True)
    archive = DIST / "think-along.zip"
    if archive.is_symlink():
        print("Refusing to package: archive must not be a symlink.", file=sys.stderr)
        return 1
    # Read a single source snapshot; publish only a fully verified archive.
    contents = {f"think-along/{name}": path.read_bytes() for name, path in FILES}
    with tempfile.TemporaryDirectory(prefix=".think-along-", dir=DIST) as temporary:
        staged = Path(temporary) / "think-along.zip"
        with zipfile.ZipFile(staged, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for name, content in contents.items():
                entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                zf.writestr(entry, content, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        with zipfile.ZipFile(staged) as zf:
            if (zf.testzip() is not None or len(zf.namelist()) != len(contents)
                    or set(zf.namelist()) != set(contents)
                    or any(zf.read(name) != content for name, content in contents.items())):
                print("Package integrity or contents check failed.", file=sys.stderr)
                return 1
        staged.replace(archive)
    print(f"Created {archive.relative_to(ROOT)} ({archive.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
