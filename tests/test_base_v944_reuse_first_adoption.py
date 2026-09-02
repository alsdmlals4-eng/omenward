from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "skills" / "PROJECT_BASE_ADAPTER.json"

V944_RELEASE = {
    "repository": "alsdmlals4-eng/Base",
    "version": "9.4.4",
    "release_commit": "210ec78292fa12ed7563ba743b322dd36103ae4a",
    "release_evidence_commit": "bb61e68dc3028421b60c11b87ba2abd297ee6f78",
    "finalization_commit": "5adc196c0185951f50e49ab5e51586eff8d60886",
}
V944_REGISTRY_SHA256 = "08f882d0c77339e8f7ff187c35b79501e0a2958ab1ff1c7aaa1c0ef8dbee45d6"


def load_adapter() -> dict:
    return json.loads(ADAPTER.read_text(encoding="utf-8"))


class BaseV944ReuseFirstAdoptionTests(unittest.TestCase):
    def test_released_v944_pin_and_reuse_first_gate_are_installed(self) -> None:
        adapter = load_adapter()

        self.assertEqual(V944_RELEASE, adapter["base_release"])
        self.assertEqual(2, adapter["schema_version"])
        self.assertEqual("omenward", adapter["project"]["project_id"])
        self.assertEqual(V944_REGISTRY_SHA256, adapter["skill_registry"]["base"]["sha256"])

        intake = adapter["shared_overrides"]["managing-project-intake-and-work-contract"]
        reuse_first = intake["reuse_first_governance"]
        self.assertEqual(
            "docs/knowledge/game-development/reuse/adoption/PROJECT_WORK_REUSE_HANDOFF.json",
            reuse_first["handoff_source"],
        )
        self.assertEqual(
            ["REUSE_FIRST_PREFLIGHT_REQUIRED", "REUSE_LEARNING_HANDOFF_REQUIRED"],
            reuse_first["required_gates"],
        )
        self.assertEqual("NOT_RUN", reuse_first["actual_project_execution"])
        self.assertTrue(reuse_first["project_only_learning_default"])

    def test_repository_only_policy_keeps_sheet_as_historical_compatibility(self) -> None:
        sheet = load_adapter()["gdd_sheet"]

        self.assertEqual("GOOGLE_SHEETS_LEGACY_MIGRATION_SOURCE", sheet["role"])
        self.assertEqual("STALE", sheet["sync_status"])
        self.assertEqual("MIGRATION_COMPATIBILITY_SURFACE", sheet["workspace_status"])
        self.assertEqual("HISTORICAL_RECONCILIATION_ONLY", sheet["declared_sync_status"])
        self.assertEqual("NO_CURRENT_READ_OR_WRITE", sheet["write_policy"])
        self.assertEqual("REPOSITORY_ONLY", sheet["current_authority"])


if __name__ == "__main__":
    unittest.main()
