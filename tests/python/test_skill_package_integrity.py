from __future__ import annotations

import copy
import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "tools" / "validate_skill_system.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(validator)


class SkillPackageIntegrityTests(unittest.TestCase):
    def test_full_contract_passes(self) -> None:
        self.assertEqual([], validator.validate(ROOT / "docs/base/SKILL_REGISTRY.json"))

    def test_optimized_package_count_and_disciplines(self) -> None:
        registry = json.loads((ROOT / "docs/base/SKILL_REGISTRY.json").read_text(encoding="utf-8"))
        self.assertEqual(23, len(registry["skills"]))
        self.assertEqual(11, len(registry["selected_disciplines"]))
        self.assertEqual({"foundation", "disciplines"}, {s["category"] for s in registry["skills"]})

    def test_no_specialist_packages_remain(self) -> None:
        self.assertFalse((ROOT / "skills/specialists").exists())

    def test_duplicate_id_is_rejected(self) -> None:
        registry_path = ROOT / "docs/base/SKILL_REGISTRY.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["skills"][1]["id"] = registry["skills"][0]["id"]
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as handle:
            json.dump(registry, handle, ensure_ascii=False)
            path = pathlib.Path(handle.name)
        try:
            errors = validator.validate(path)
        finally:
            path.unlink(missing_ok=True)
        self.assertTrue(any("duplicate Skill IDs" in error for error in errors))

    def test_review_stack_is_mandatory(self) -> None:
        registry_path = ROOT / "docs/base/SKILL_REGISTRY.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["routing"]["review_stack"].remove("foundation.adversarial-review")
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as handle:
            json.dump(registry, handle, ensure_ascii=False)
            path = pathlib.Path(handle.name)
        try:
            errors = validator.validate(path)
        finally:
            path.unlink(missing_ok=True)
        self.assertTrue(any("mandatory adversarial review stack" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
