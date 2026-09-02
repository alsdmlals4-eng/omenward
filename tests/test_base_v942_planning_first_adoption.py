from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "skills/PROJECT_BASE_ADAPTER.json"


def load() -> dict:
    return json.loads(ADAPTER.read_text(encoding="utf-8"))


class PlanningFirstCompatibilityTests(unittest.TestCase):
    def test_v944_preserves_planning_first_contract(self) -> None:
        data = load(); release = data["base_release"]
        self.assertEqual("9.4.4", release["version"])
        self.assertEqual("210ec78292fa12ed7563ba743b322dd36103ae4a", release["release_commit"])
        self.assertEqual("bb61e68dc3028421b60c11b87ba2abd297ee6f78", release["release_evidence_commit"])
        self.assertEqual("5adc196c0185951f50e49ab5e51586eff8d60886", release["finalization_commit"])
        self.assertEqual("08f882d0c77339e8f7ff187c35b79501e0a2958ab1ff1c7aaa1c0ef8dbee45d6", data["skill_registry"]["base"]["sha256"])

    def test_planning_first_contract(self) -> None:
        data = load(); active = {r if isinstance(r, str) else r["skill_id"] for r in data["routing"]["base_routes"] if isinstance(r, str) or r.get("status") == "ACTIVE"}
        self.assertIn("managing-project-intake-and-work-contract", active)
        policy = data["shared_overrides"]["managing-project-intake-and-work-contract"]["planning_first_governance"]
        self.assertEqual("docs/PLANNING_FIRST_GRILL_ME_BATCH_POLICY.md", policy["base_contract_source"])
        self.assertEqual("templates/project-operations/GRILL_ME_BATCH_CHECKPOINT.md", policy["checkpoint_template"])
        self.assertEqual("base-v9.4.4.lock.json", policy["base_release_lock"])
        self.assertEqual(10, policy["max_approved_decisions_per_batch"])
        self.assertEqual("RECOMMENDED_DEFAULT", policy["numeric_default_state"])
        self.assertEqual("GRILL_ME_REQUIRED", policy["planning_conflict_state"])
        self.assertEqual("APPROVED_PENDING_MERGE", policy["pre_merge_repository_state"])
        self.assertEqual("SYNCED_TO_MAIN", policy["post_merge_repository_state"])
        self.assertEqual("HISTORICAL_RECONCILIATION_ONLY", policy["legacy_sheet_compatibility_state"])
        self.assertEqual("NOT_RUN", policy["actual_project_batch_execution"])

    def test_project_boundaries_remain_unchanged(self) -> None:
        data = load()
        self.assertEqual("STALE", data["gdd_sheet"]["sync_status"])
        self.assertEqual("HISTORICAL_RECONCILIATION_ONLY", data["gdd_sheet"]["declared_sync_status"])
        self.assertEqual(["data/", "scripts/", "scenes/", "assets/", "addons/", "project.godot"], data["protected_paths"])
        self.assertEqual("NOT_RUN", data["shared_overrides"]["orchestrating-deepseek-worktrees"]["actual_external_ai_worktree_execution"])


if __name__ == "__main__": unittest.main()
