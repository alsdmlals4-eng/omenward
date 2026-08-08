from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
ADAPTER = ROOT / "skills" / "PROJECT_BASE_ADAPTER.json"
ACTIVE_STATE = ROOT / "docs" / "operations" / "ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"

DECISION_ID = "OMW-DEC-20260808-PROCESS-PROJECT-BASE-ADAPTER-FRESHNESS-RECONCILIATION-V1"
BASELINE_MAIN = "1f23981fdfc3e965ff46c8866e978c4701eb3d4e"
BASE_RELEASE_VERSION = "9.4.3"
BASE_RELEASE_COMMIT = "7dd1a4f80388bc5faca767ff74a3eb32dc9d0ac8"
PROTECTED_POLICY_SHA = "1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"


class ProjectBaseAdapterFreshnessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
        cls.state = json.loads(ACTIVE_STATE.read_text(encoding="utf-8"))

    def test_release_pin_is_preserved_without_automatic_base_main_migration(self) -> None:
        release = self.adapter["base_release"]
        self.assertEqual(release["version"], BASE_RELEASE_VERSION)
        self.assertEqual(release["release_commit"], BASE_RELEASE_COMMIT)

    def test_gdd_sheet_matches_current_reconciled_workspace(self) -> None:
        sheet = self.adapter["gdd_sheet"]
        self.assertEqual(sheet["id"], SHEET_ID)
        self.assertEqual(sheet["role"], "USER_FACING_GDD_WORKSPACE")
        self.assertEqual(sheet["sync_status"], "CURRENT")
        self.assertEqual(sheet["declared_sync_status"], "SHEET_GITHUB_SYNCED")
        self.assertEqual(sheet["write_policy"], "NO_AUTOMATIC_OVERWRITE")

    def test_protected_baseline_uses_current_main_canonical_adapter_source(self) -> None:
        baseline = self.adapter["protected_baseline"]
        self.assertEqual(baseline["commit"], BASELINE_MAIN)
        self.assertEqual(baseline["authority_kind"], "REMOTE_TRACKING_REF")
        self.assertEqual(baseline["authority_ref"], "refs/remotes/origin/main")
        self.assertEqual(baseline["policy_source_type"], "CANONICAL_ADAPTER_SOURCE")
        self.assertEqual(baseline["policy_source_path"], "skills/PROJECT_BASE_ADAPTER.json")
        self.assertEqual(baseline["protected_paths_pointer"], "/protected_paths")
        baseline_adapter = json.loads(subprocess.check_output(["git", "show", f"{BASELINE_MAIN}:skills/PROJECT_BASE_ADAPTER.json"], text=True))
        protected_policy = (json.dumps(baseline_adapter["protected_paths"], ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(protected_policy).hexdigest(), PROTECTED_POLICY_SHA)
        self.assertEqual(baseline["policy_sha256"], PROTECTED_POLICY_SHA)

    def test_adapter_freshness_remains_closed_across_later_planning_gates(self) -> None:
        gate = self.state["entry_gate"]
        blockers = set(gate["blocking_reasons"])
        self.assertNotIn("PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED", blockers)
        self.assertNotIn("PR154_CONDITIONAL_FAIL_UNMERGED", blockers)
        self.assertIn("GUT_ADOPTION_SPEC_PR155_NOT_MERGED", blockers)
        self.assertEqual(gate["decision"], "BLOCK")
        self.assertNotIn("PROJECT_BASE_ADAPTER_FRESHNESS_RECONCILIATION", gate["allowed_next_actions"])
        adapter_state = self.state["project_base_adapter"]
        self.assertEqual(adapter_state["decision_id"], DECISION_ID)
        self.assertEqual(adapter_state["protected_baseline_commit"], BASELINE_MAIN)
        self.assertEqual(adapter_state["protected_policy_sha256"], PROTECTED_POLICY_SHA)
        self.assertEqual(adapter_state["gdd_sheet_sync_status"], "CURRENT")
        self.assertEqual(adapter_state["status"], "FRESHNESS_RECONCILED")
        self.assertTrue(adapter_state["blocker_cleared"])


if __name__ == "__main__":
    unittest.main()
