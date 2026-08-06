from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validate_gut_vendor_manifest.py"
MANIFEST_PATH = ROOT / "docs/operations/GUT_9_7_1_VENDOR_MANIFEST.v1.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("gut_vendor_validator", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("validator import unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GutVendorManifestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_truthful_blocked_manifest_passes(self) -> None:
        self.assertEqual(self.validator.validate_manifest(self.manifest), [])

    def test_exact_changed_path_set_is_pinned(self) -> None:
        paths = {row["path"] for row in self.manifest["changed_paths"]}
        self.assertEqual(paths, self.validator.EXPECTED_CHANGED_PATHS)
        self.assertEqual(len(paths), 18)

    def test_gdscript_delta_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.manifest)
        mutated["changed_paths"][0]["path"] = "gut.gd"
        errors = self.validator.validate_manifest(mutated)
        self.assertTrue(any("code/config/license delta forbidden" in item for item in errors))

    def test_missing_or_extra_paths_are_rejected(self) -> None:
        for field in ("missing_paths", "extra_paths"):
            mutated = copy.deepcopy(self.manifest)
            mutated["path_set"][field] = ["unexpected.txt"]
            errors = self.validator.validate_manifest(mutated)
            self.assertTrue(any("must not hide" in item for item in errors))

    def test_binary_resource_cannot_be_promoted_to_normalized(self) -> None:
        mutated = copy.deepcopy(self.manifest)
        row = next(item for item in mutated["changed_paths"] if item["path"] == "source_code_pro.fnt")
        row["classification"] = "HEADER_LOAD_STEPS_NORMALIZATION_CANDIDATE"
        errors = self.validator.validate_manifest(mutated)
        self.assertIn("source_code_pro.fnt must remain unclassified until decoded", errors)

    def test_activation_cannot_be_ready_while_blockers_remain(self) -> None:
        mutated = copy.deepcopy(self.manifest)
        mutated["activation"]["status"] = "READY"
        errors = self.validator.validate_manifest(mutated)
        self.assertIn("activation must remain BLOCKED", errors)

    def test_text_candidates_preserve_minus_thirteen_byte_evidence(self) -> None:
        mutated = copy.deepcopy(self.manifest)
        row = next(item for item in mutated["changed_paths"] if item["path"] != "source_code_pro.fnt")
        row["size_delta"] = -12
        errors = self.validator.validate_manifest(mutated)
        self.assertTrue(any("size delta must be -13" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
