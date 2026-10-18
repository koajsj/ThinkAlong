from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("thinkalong_validator", ROOT / "scripts" / "validate_skill.py")
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(
            ROOT,
            self.root,
            ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc"),
        )

    def tearDown(self):
        self.temp.cleanup()

    def errors(self):
        return validator.validate(self.root)

    def test_current_repo_passes(self):
        self.assertEqual(self.errors(), [])

    def test_invalid_frontmatter_fails(self):
        path = self.root / "skills/think-along/SKILL.md"
        path.write_text(path.read_text().replace("name: think-along", "name: [broken", 1), encoding="utf-8")
        self.assertTrue(any("invalid SKILL.md" in e for e in self.errors()))

    def test_unknown_frontmatter_key_fails(self):
        path = self.root / "skills/think-along/SKILL.md"
        path.write_text(path.read_text().replace("license: MIT", "license: MIT\nunknown-field: true", 1), encoding="utf-8")
        self.assertTrue(any("unsupported SKILL.md frontmatter key" in e for e in self.errors()))

    def test_missing_task_case_fails(self):
        path = self.root / "evals/task-cases.md"
        path.write_text("\n".join(line for line in path.read_text().splitlines() if not line.startswith("| E30 |")), encoding="utf-8")
        self.assertTrue(any("exactly 30 unique cases" in e for e in self.errors()))

    def test_duplicate_task_case_fails(self):
        path = self.root / "evals/task-cases.md"
        text = path.read_text()
        row = next(line for line in text.splitlines() if line.startswith("| E29 |"))
        path.write_text(text + "\n" + row + "\n", encoding="utf-8")
        self.assertTrue(any("exactly 30 unique cases" in e for e in self.errors()))

    def test_missing_trigger_case_fails(self):
        path = self.root / "evals/trigger-cases.md"
        path.write_text("\n".join(line for line in path.read_text().splitlines() if not line.startswith("| T30 |")), encoding="utf-8")
        self.assertTrue(any("exactly 30 unique cases" in e for e in self.errors()))

    def test_bad_default_prompt_fails(self):
        path = self.root / "skills/think-along/agents/openai.yaml"
        path.write_text(path.read_text().replace("$think-along", "ThinkAlong"), encoding="utf-8")
        self.assertTrue(any("default_prompt must explicitly invoke" in e for e in self.errors()))

    def test_short_description_fails(self):
        path = self.root / "skills/think-along/agents/openai.yaml"
        path.write_text(path.read_text().replace("Turn fuzzy requests into useful, checked results", "Short"), encoding="utf-8")
        self.assertTrue(any("short_description must be 25-64" in e for e in self.errors()))

    def test_broken_local_link_fails(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n[broken](missing.md)\n", encoding="utf-8")
        self.assertTrue(any("broken local link" in e for e in self.errors()))

    def test_description_over_limit_fails(self):
        path = self.root / "skills/think-along/SKILL.md"
        text = path.read_text()
        start = text.index("description: ") + len("description: ")
        end = text.index("\n", start)
        text = text[:start] + ("x" * 1025) + text[end:]
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("description must be 1-1024" in e for e in self.errors()))

    def test_package_contains_only_runtime_files(self):
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts" / "package_skill.py")],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        archive = self.root / "dist" / "think-along.zip"
        self.assertTrue(archive.is_file())
        expected = {
            "think-along/SKILL.md",
            "think-along/LICENSE",
            "think-along/agents/openai.yaml",
            "think-along/references/workflow.md",
            "think-along/references/acceptance-checks.md",
            "think-along/references/examples.md",
        }
        with zipfile.ZipFile(archive) as zf:
            self.assertIsNone(zf.testzip())
            self.assertEqual(set(zf.namelist()), expected)


if __name__ == "__main__":
    unittest.main()
