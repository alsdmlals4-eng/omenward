from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BaseV9AdoptionTests(unittest.TestCase):
    def test_current_adapter_preserves_implementation_boundary(self) -> None:
        data = json.loads((ROOT / "skills/PROJECT_BASE_ADAPTER.json").read_text(encoding="utf-8"))
        health = json.loads((ROOT / "docs/PROJECT_OPERATING_HEALTH.json").read_text(encoding="utf-8"))
        release = data["base_release"]
        self.assertEqual("9.4.3", release["version"])
        self.assertEqual("7dd1a4f80388bc5faca767ff74a3eb32dc9d0ac8", release["release_commit"])
        self.assertEqual("da33a350d61b8adc52df97fccc7001708a933370", release["release_evidence_commit"])
        self.assertEqual("0b7c94f38d959efc0fc9442274c60b2e268a3c97", release["finalization_commit"])
        intake = data["shared_overrides"]["managing-project-intake-and-work-contract"]
        self.assertEqual(10, intake["planning_first_governance"]["max_approved_decisions_per_batch"])
        self.assertEqual("GRILL_ME_REQUIRED", intake["planning_first_governance"]["planning_conflict_state"])
        self.assertEqual("NOTION_DEFAULT_PROJECT_WORKSPACE", intake["planning_first_governance"]["current_human_workspace"])
        self.assertEqual("GITHUB_REPOSITORY_AND_ACTUAL_RUNTIME", intake["planning_first_governance"]["runtime_structured_authority"])
        self.assertEqual("AWAITING_USER_CONFIRMATION", intake["first_prompt_governance"]["unconfirmed_state"])
        sheet = data["gdd_sheet"]
        self.assertEqual("GOOGLE_SHEETS_LEGACY_MIGRATION_SOURCE", sheet["role"])
        self.assertEqual("MIGRATION_COMPATIBILITY_SURFACE", sheet["workspace_status"])
        self.assertEqual("NOT_CONFIGURED", sheet["sync_status"])
        self.assertEqual("HISTORICAL_SYNCED", sheet["declared_sync_status"])
        self.assertFalse(sheet["new_input_allowed"])
        self.assertFalse(sheet["read_for_normal_work"])
        self.assertEqual("OM-L0", health["operating_maturity"])
        self.assertEqual("PE-0", health["product_evidence_maturity"])
        self.assertEqual("NOT_RUN", health["critical_gates"]["runtime"])

    def test_v9_compatibility_view_is_generated(self) -> None:
        data = json.loads((ROOT / "skills/BASE_V9_ADAPTER.json").read_text(encoding="utf-8"))
        self.assertEqual("GENERATED_COMPATIBILITY_VIEW", data["artifact_role"])
        self.assertTrue(data["generated"])
        self.assertEqual("skills/PROJECT_BASE_ADAPTER.json", data["canonical_source"])

    def test_adoption_contract_and_gates_exist(self) -> None:
        audit = (ROOT / "docs/BASE_V9_ADOPTION_AUDIT.md").read_text(encoding="utf-8")
        workflow = (ROOT / ".github/workflows/validate-base-v9-adoption.yml").read_text(encoding="utf-8")
        for token in ("OPERATING_SYSTEM_ONLY", "VERTICAL_SLICE_CONTRACT", "PRODUCT_IMPLEMENTATION_NOT_STARTED", "NOT_RUN"):
            self.assertIn(token, audit)
        self.assertIn("ci-gate", workflow)
        self.assertIn("adversarial-gate", workflow)

    def test_candidate_draft_reuse_is_isolated_outside_product_paths(self) -> None:
        manifest = json.loads((ROOT / "docs/base-reuse-adoption.json").read_text(encoding="utf-8"))
        self.assertEqual("8553678f70e22f193a2336b591f677dcfa5a8965", manifest["base_source_commit"])
        self.assertEqual("enabled", manifest["modules"]["RM-SYS-003"]["state"])
        destination = manifest["modules"]["RM-SYS-003"]["destination"]
        self.assertEqual("vendor/base-reuse/candidate_draft_weight_engine.gd", destination)
        self.assertTrue((ROOT / destination).is_file())
        self.assertTrue((ROOT / "vendor/base-reuse/omenward_candidate_draft_adapter.gd").is_file())

        workflow = (ROOT / ".github/workflows/validate-base-v9-adoption.yml").read_text(encoding="utf-8")
        for protected_prefix in ("scripts/", "scenes/", "data/", "assets/", "addons/", "project\\.godot"):
            self.assertIn(protected_prefix, workflow)
        self.assertNotIn("vendor/base-reuse", workflow)


if __name__ == "__main__": unittest.main()
