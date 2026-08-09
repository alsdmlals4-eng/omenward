from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project.godot"
GODOT_AI = ROOT / "addons/godot_ai/plugin.cfg"
GUT = ROOT / "addons/gut/plugin.cfg"
HERA = ROOT / "addons/hera_agent_godot/plugin.cfg"
HERA_README = ROOT / "addons/hera_agent_godot/README.md"
HERA_LICENSE = ROOT / "addons/hera_agent_godot/LICENSE"
AUTHORITY = ROOT / "docs/process/APPROVED_OMENWARD_GODOT_AI_3_1_3_HERA_GUT_USER_APPROVAL_AND_REMOTE_SYNC_RECONCILIATION_2026-08-09.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"

DECISION = "OMW-DEC-20260809-TOOLS-GODOT-AI-3-1-3-HERA-GUT-USER-APPROVAL-REMOTE-SYNC-RECONCILIATION-V1"
SYNC_MAIN = "f1bf8939208a864bce1f99eea0555f05369dc9d6"


class ToolStateUserApprovalRemoteSyncTest(unittest.TestCase):
    def test_remote_main_evidence_matches_user_approved_state(self) -> None:
        project = PROJECT.read_text(encoding="utf-8")
        self.assertIn('res://addons/godot_ai/plugin.cfg', project)
        self.assertIn('res://addons/gut/plugin.cfg', project)
        self.assertIn('res://addons/hera_agent_godot/plugin.cfg', project)
        self.assertIn('HeraGameInspector=', project)
        self.assertIn('version="3.1.3"', GODOT_AI.read_text(encoding="utf-8"))
        self.assertIn('version="9.7.1"', GUT.read_text(encoding="utf-8"))
        self.assertIn('version="1.0.0"', HERA.read_text(encoding="utf-8"))

    def test_hera_bundled_provenance_and_metadata_drift_are_visible(self) -> None:
        readme = HERA_README.read_text(encoding="utf-8")
        license_text = HERA_LICENSE.read_text(encoding="utf-8")
        self.assertIn("https://github.com/NotNull92/hera-agent-godot", readme)
        self.assertIn("v0.9.0", readme)
        self.assertIn("MIT License", license_text)
        self.assertIn('version="1.0.0"', HERA.read_text(encoding="utf-8"))

    def test_authority_records_user_approval_and_verified_remote_sync(self) -> None:
        self.assertTrue(AUTHORITY.is_file(), f"missing authority: {AUTHORITY.relative_to(ROOT)}")
        text = AUTHORITY.read_text(encoding="utf-8")
        for marker in (
            DECISION,
            SYNC_MAIN,
            "GODOT_AI_USER_APPROVED_VERSION = 3.1.3",
            "GODOT_AI_UPSTREAM_RELEASE = v3.1.3",
            "GUT_USER_APPROVAL = APPROVED",
            "GUT_USER_REPORTED_LOCAL_ENABLEMENT = ENABLED_NOT_HOST_VERIFIED",
            "HERA_USER_APPROVAL = APPROVED",
            "HERA_USER_REPORTED_LOCAL_ENABLEMENT = ENABLED_NOT_HOST_VERIFIED",
            "REMOTE_PROJECT_GODOT_GUT_ENABLED = TRUE",
            "REMOTE_PROJECT_GODOT_HERA_ENABLED = TRUE",
            "REMOTE_GODOT_AI_VERSION = 3.1.3",
            "REMOTE_SYNC_COMPLETION = VERIFIED",
            "HERA_EXISTING_SOLUTION_DISPOSITION = REUSE_APPROVED_BY_USER",
            "HERA_BUNDLED_README_VERSION = 0.9.0_STALE_METADATA",
        ):
            self.assertIn(marker, text)

    def test_durable_state_closes_approval_and_remote_sync_blockers(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["last_gate_update_decision"], DECISION)
        self.assertEqual(state["source_repository_main_sha"], SYNC_MAIN)
        gate = state["entry_gate"]
        blockers = set(gate["blocking_reasons"])
        for closed in (
            "GUT_ADOPTION_SPEC_PR155_NOT_MERGED",
            "HIGODOT_EXACT_SOURCE_OR_VERSION_UNVERIFIED",
            "HERA_PRESENT_BUT_ADOPTION_NOT_VERIFIED",
            "DIRECT_MAIN_HERA_IMPORT_NOT_YET_DISPOSITIONED",
            "GODOT_AI_3_1_3_REMOTE_SYNC_REQUIRED",
            "GUT_REMOTE_ENABLEMENT_SYNC_REQUIRED",
            "HERA_REMOTE_ENABLEMENT_SYNC_REQUIRED",
        ):
            self.assertNotIn(closed, blockers)
        self.assertIn("BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED", blockers)
        self.assertEqual(gate["decision"], "BLOCK")

    def test_tool_roles_remain_non_overlapping_and_user_approved(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        tools = state["tool_authority"]
        self.assertEqual(tools["higodot"]["approved_version"], "3.1.3")
        self.assertEqual(tools["higodot"]["user_approval"], "APPROVED")
        self.assertEqual(tools["higodot"]["remote_version_observed"], "3.1.3")
        self.assertTrue(tools["higodot"]["remote_editor_plugin_enabled"])
        self.assertEqual(tools["higodot"]["remote_sync_status"], "VERIFIED")
        self.assertEqual(tools["gut"]["version"], "9.7.1")
        self.assertEqual(tools["gut"]["user_approval"], "APPROVED")
        self.assertEqual(tools["gut"]["user_reported_local_enablement"], "ENABLED_NOT_HOST_VERIFIED")
        self.assertTrue(tools["gut"]["remote_editor_plugin_enabled"])
        self.assertEqual(tools["gut"]["remote_sync_status"], "VERIFIED")
        self.assertEqual(tools["hera"]["approved_version"], "1.0.0")
        self.assertEqual(tools["hera"]["user_approval"], "APPROVED")
        self.assertEqual(tools["hera"]["existing_solution_disposition"], "REUSE_APPROVED_BY_USER")
        self.assertEqual(tools["hera"]["user_reported_local_enablement"], "ENABLED_NOT_HOST_VERIFIED")
        self.assertTrue(tools["hera"]["remote_editor_plugin_enabled"])
        self.assertEqual(tools["hera"]["remote_sync_status"], "VERIFIED")
        self.assertEqual(tools["hera"]["persistent_source_mutation"], "FORBIDDEN")
        self.assertEqual(tools["role_overlap"], "FORBIDDEN")


if __name__ == "__main__":
    unittest.main()
