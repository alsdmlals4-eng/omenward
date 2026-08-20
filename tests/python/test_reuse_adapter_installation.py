from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class ReuseAdapterInstallationTests(unittest.TestCase):
    def test_manifest_and_vendored_files_match_the_approved_module(self) -> None:
        manifest = json.loads((ROOT / "docs/base-reuse-adoption.json").read_text(encoding="utf-8"))
        draft = manifest["modules"]["RM-SYS-003"]

        self.assertEqual("8553678f70e22f193a2336b591f677dcfa5a8965", manifest["base_source_commit"])
        self.assertEqual("enabled", draft["state"])
        self.assertEqual(
            "templates/reuse-modules/godot/candidate_draft_weight_engine.gd",
            draft["source"],
        )
        self.assertEqual(
            "vendor/base-reuse/candidate_draft_weight_engine.gd",
            draft["destination"],
        )
        self.assertTrue((ROOT / draft["destination"]).is_file())
        self.assertTrue((ROOT / "vendor/base-reuse/omenward_candidate_draft_adapter.gd").is_file())
        self.assertTrue((ROOT / "tests/headless/p0_candidate_draft_reuse_test.gd").is_file())

    def test_adapter_preserves_omenward_candidate_boundaries(self) -> None:
        adapter = (ROOT / "vendor/base-reuse/omenward_candidate_draft_adapter.gd").read_text(encoding="utf-8")
        for token in (
            "TOKEN_SOURCE_CANDIDATE_COUNT := 3",
            "OMENWARD_REQUIRES_THREE_TOKEN_SOURCE_CANDIDATES",
            "DUPLICATE_CANDIDATE_ID",
            "FRACTIONAL_WEIGHT_FORBIDDEN",
            "NON_POSITIVE_WEIGHT",
            "INSUFFICIENT_UNIQUE_CANDIDATES",
            "DUPLICATE_FORBID",
        ):
            self.assertIn(token, adapter)

    def test_core_workflow_watches_vendor_changes_and_runs_headless_suite(self) -> None:
        workflow = (ROOT / ".github/workflows/validate-omenward-core.yml").read_text(encoding="utf-8")
        self.assertGreaterEqual(workflow.count('"vendor/base-reuse/**"'), 2)
        self.assertIn("for test_file in tests/headless/*_test.gd", workflow)
        self.assertIn("Install Godot 4.7.1 Standard", workflow)
        self.assertIn("Runtime smoke", workflow)


if __name__ == "__main__":
    unittest.main()
