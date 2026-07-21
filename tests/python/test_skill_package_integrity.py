from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "docs" / "base" / "SKILL_REGISTRY.json"


class SkillPackageIntegrityTests(unittest.TestCase):
    def test_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "tools/validate_skill_system.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_registry_ids_and_paths_are_unique(self) -> None:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        ids = [skill["id"] for skill in data["skills"]]
        paths = [skill["path"] for skill in data["skills"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(paths), len(set(paths)))

    def test_validator_rejects_duplicate_id_mutation(self) -> None:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        data["skills"][1]["id"] = data["skills"][0]["id"]
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "registry.json"
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "tools/validate_skill_system.py", "--registry", str(path)],
                cwd=ROOT, text=True, capture_output=True, check=False,
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate Skill IDs", result.stdout)

    def test_expected_category_counts(self) -> None:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        counts: dict[str, int] = {}
        for skill in data["skills"]:
            counts[skill["category"]] = counts.get(skill["category"], 0) + 1
        self.assertEqual(counts, {"foundation": 7, "disciplines": 11, "specialists": 6})


if __name__ == "__main__":
    unittest.main()
