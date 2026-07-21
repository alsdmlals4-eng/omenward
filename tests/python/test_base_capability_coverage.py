from __future__ import annotations

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


class BaseCapabilityCoverageTests(unittest.TestCase):
    def test_all_25_base_skills_are_mapped(self) -> None:
        coverage = json.loads((ROOT / "docs/base/BASE_CAPABILITY_COVERAGE.json").read_text(encoding="utf-8"))
        self.assertEqual(25, len(coverage["mappings"]))
        self.assertEqual(validator.EXPECTED_BASE_SKILLS, {m["base_skill_id"] for m in coverage["mappings"]})

    def test_every_target_mode_exists(self) -> None:
        registry = json.loads((ROOT / "docs/base/SKILL_REGISTRY.json").read_text(encoding="utf-8"))
        known = {skill["id"]: set(skill["modes"]) for skill in registry["skills"]}
        coverage = json.loads((ROOT / "docs/base/BASE_CAPABILITY_COVERAGE.json").read_text(encoding="utf-8"))
        for mapping in coverage["mappings"]:
            for target in mapping["local_targets"]:
                self.assertIn(target["id"], known)
                self.assertTrue(set(target["modes"]).issubset(known[target["id"]]))

    def test_removed_specialists_have_compatibility_aliases(self) -> None:
        aliases = json.loads((ROOT / "skills/LEGACY_SKILL_ALIASES.json").read_text(encoding="utf-8"))["aliases"]
        self.assertTrue(validator.REQUIRED_OLD_ALIASES.issubset(aliases))

    def test_missing_base_mapping_is_detected(self) -> None:
        coverage_path = ROOT / "docs/base/BASE_CAPABILITY_COVERAGE.json"
        data = json.loads(coverage_path.read_text(encoding="utf-8"))
        removed = data["mappings"].pop()
        original = coverage_path.read_text(encoding="utf-8")
        try:
            coverage_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            errors = validator.validate(ROOT / "docs/base/SKILL_REGISTRY.json")
        finally:
            coverage_path.write_text(original, encoding="utf-8")
        self.assertTrue(any("Base capability coverage mismatch" in error for error in errors), removed)

    def test_unknown_coverage_mode_is_detected(self) -> None:
        coverage_path = ROOT / "docs/base/BASE_CAPABILITY_COVERAGE.json"
        data = json.loads(coverage_path.read_text(encoding="utf-8"))
        data["mappings"][0]["local_targets"][0]["modes"].append("missing-mode")
        original = coverage_path.read_text(encoding="utf-8")
        try:
            coverage_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            errors = validator.validate(ROOT / "docs/base/SKILL_REGISTRY.json")
        finally:
            coverage_path.write_text(original, encoding="utf-8")
        self.assertTrue(any("coverage target modes missing" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
