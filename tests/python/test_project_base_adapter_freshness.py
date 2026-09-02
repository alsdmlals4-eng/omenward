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
HISTORICAL_BASELINE_MAIN = "1f23981fdfc3e965ff46c8866e978c4701eb3d4e"
APPROVED_PROTECTED_BASELINE = "9a67a267a69c80fba6f25d5a37e360a15dcc2419"
BASE_RELEASE_VERSION = "9.4.4"
BASE_RELEASE_COMMIT = "210ec78292fa12ed7563ba743b322dd36103ae4a"
PROTECTED_POLICY_SHA = "1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52"
CURRENT_ADAPTER_SHA = "996f19cf5aba6f91dceab8d0961a8fb39567a796237862aa7f096fd600600212"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"
GENERATED_OPERATING_ARTIFACTS = (
    ".agents/skills/omenward-workflow-router/SKILL.md",
    "docs/PROJECT_OPERATING_DASHBOARD.html",
    "skills/BASE_V9_ADAPTER.json",
    "skills/PROJECT_BASE_SKILL_ADAPTER.json",
    "skills/PROJECT_SKILL_SNAPSHOT.json",
)


class ProjectBaseAdapterFreshnessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
        cls.state = json.loads(ACTIVE_STATE.read_text(encoding="utf-8"))

    def test_release_pin_is_preserved_without_automatic_base_main_migration(self) -> None:
        release = self.adapter["base_release"]
        self.assertEqual(2, self.adapter["schema_version"])
        self.assertEqual("omenward", self.adapter["project"]["project_id"])
        self.assertEqual(release["version"], BASE_RELEASE_VERSION)
        self.assertEqual(release["release_commit"], BASE_RELEASE_COMMIT)

    def test_gdd_sheet_is_historical_compatibility_not_current_workspace(self) -> None:
        sheet = self.adapter["gdd_sheet"]
        self.assertEqual(sheet["id"], SHEET_ID)
        self.assertEqual(sheet["role"], "GOOGLE_SHEETS_LEGACY_MIGRATION_SOURCE")
        self.assertEqual(sheet["sync_status"], "STALE")
        self.assertEqual(sheet["workspace_status"], "MIGRATION_COMPATIBILITY_SURFACE")
        self.assertEqual(sheet["declared_sync_status"], "HISTORICAL_RECONCILIATION_ONLY")
        self.assertEqual(sheet["write_policy"], "NO_CURRENT_READ_OR_WRITE")
        self.assertEqual(sheet["current_authority"], "REPOSITORY_ONLY")

    def test_protected_baseline_preserves_the_existing_approved_change_origin(self) -> None:
        baseline = self.adapter["protected_baseline"]
        self.assertEqual(baseline["commit"], APPROVED_PROTECTED_BASELINE)
        self.assertEqual(baseline["authority_kind"], "REMOTE_TRACKING_REF")
        self.assertEqual(baseline["authority_ref"], "refs/remotes/origin/main")
        self.assertEqual(baseline["policy_source_type"], "CANONICAL_ADAPTER_SOURCE")
        self.assertEqual(baseline["policy_source_path"], "skills/PROJECT_BASE_ADAPTER.json")
        self.assertEqual(baseline["protected_paths_pointer"], "/protected_paths")
        baseline_adapter = json.loads(
            subprocess.check_output(
                ["git", "show", f"{APPROVED_PROTECTED_BASELINE}:skills/PROJECT_BASE_ADAPTER.json"]
            ).decode("utf-8")
        )
        protected_policy = (json.dumps(baseline_adapter["protected_paths"], ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(protected_policy).hexdigest(), PROTECTED_POLICY_SHA)
        self.assertEqual(baseline["policy_sha256"], PROTECTED_POLICY_SHA)
        self.assertEqual(hashlib.sha256(ADAPTER.read_bytes()).hexdigest(), CURRENT_ADAPTER_SHA)

    def test_historical_state_block_remains_point_in_time_while_current_adapter_advances(self) -> None:
        gate = self.state["entry_gate"]
        blockers = set(gate["blocking_reasons"])
        self.assertNotIn("PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED", blockers)
        self.assertNotIn("PR154_CONDITIONAL_FAIL_UNMERGED", blockers)
        self.assertNotIn("GUT_ADOPTION_SPEC_PR155_NOT_MERGED", blockers)
        self.assertEqual(gate["decision"], "BLOCK")
        self.assertNotIn("PROJECT_BASE_ADAPTER_FRESHNESS_RECONCILIATION", gate["allowed_next_actions"])
        adapter_state = self.state["project_base_adapter"]
        self.assertEqual(adapter_state["decision_id"], DECISION_ID)
        self.assertEqual(adapter_state["protected_baseline_commit"], HISTORICAL_BASELINE_MAIN)
        self.assertEqual(adapter_state["canonical_adapter_sha256"], "799b20aa009c3a90dcf433f965a1f8280de30a7dfdc36bfc7518e4f19ea6677c")
        self.assertEqual(adapter_state["protected_policy_sha256"], PROTECTED_POLICY_SHA)
        self.assertEqual(adapter_state["gdd_sheet_sync_status"], "CURRENT")
        self.assertEqual(adapter_state["status"], "FRESHNESS_RECONCILED")
        self.assertTrue(adapter_state["blocker_cleared"])

    def test_generated_operating_artifacts_are_checked_out_with_lf(self) -> None:
        for relative_path in GENERATED_OPERATING_ARTIFACTS:
            with self.subTest(relative_path=relative_path):
                attribute = subprocess.check_output(
                    ["git", "check-attr", "eol", "--", relative_path],
                    cwd=ROOT,
                    text=True,
                )
                self.assertEqual(f"{relative_path}: eol: lf\n", attribute)


if __name__ == "__main__":
    unittest.main()
