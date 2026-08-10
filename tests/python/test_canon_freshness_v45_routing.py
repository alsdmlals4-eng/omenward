from __future__ import annotations

import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION = "OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1"
ACTIVATION_DECISION = "OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1"
BASE_MAIN = "315c66eea9614c284b9c11c4d522141065dfa4b0"
PROJECT_BASELINE = "87339f87949c8faea0dfe1482c5d0887a04d94f4"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"

BINDING = ROOT / "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"
DECISION_DOC = ROOT / "docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md"
CANONICAL_V45_R2 = ROOT / "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md"
SHEET_EVIDENCE = ROOT / "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json"
GDD = ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md"
WORKBOOK = ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md"
ACTIVE_CONTEXT = ROOT / "docs/ACTIVE_CONTEXT.md"
CURRENT_STATUS = ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
LEDGER = ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md"
AGENTS = ROOT / "AGENTS.md"
PROJECT_CORE = ROOT / "docs/PROJECT_CORE.md"
DOCUMENTATION_MAP = ROOT / "docs/DOCUMENTATION_MAP.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"


class CanonFreshnessV45RoutingTest(unittest.TestCase):
    def test_v45_authority_files_exist(self) -> None:
        for path in (BINDING, STATE, DECISION_DOC, SHEET_EVIDENCE):
            self.assertTrue(path.is_file(), f"missing current v4.5 authority artifact: {path.relative_to(ROOT)}")

    def test_v45_r2_full_instruction_is_repo_canonical_source(self) -> None:
        self.assertTrue(CANONICAL_V45_R2.is_file(), f"missing repo canonical instruction: {CANONICAL_V45_R2.relative_to(ROOT)}")
        text = CANONICAL_V45_R2.read_text(encoding="utf-8")
        for marker in (
            "contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION",
            "contract_version: '4.5'",
            "status: ACTIVE_BASE_CURRENT_MAIN_THIN_ADAPTER_GODOT_DELIVERY_CONTRACT",
            "revision: '2026-08-11-r2'",
            "adapter_policy: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON",
            'project_local_path: "C:/Users/user/Documents/GitHub/Ninza/omenward"',
            'canonical_local_checkout: "C:/Users/user/Documents/GitHub/Ninza/omenward"',
            'godot_project_path: "C:/Users/user/Documents/GitHub/Ninza/omenward"',
        ):
            self.assertIn(marker, text)
        self.assertNotIn("Switchy-Express-Cargo-Puzzle", text)

        binding = BINDING.read_text(encoding="utf-8")
        self.assertIn(ACTIVATION_DECISION, binding)
        self.assertIn(str(CANONICAL_V45_R2.relative_to(ROOT)).replace("\\", "/"), binding)

        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["active_contract"]["source"], str(CANONICAL_V45_R2.relative_to(ROOT)).replace("\\", "/"))
        self.assertEqual(state["active_contract"]["activation_decision_id"], ACTIVATION_DECISION)

    def test_v45_binding_is_thin_adapter_and_phase_c_is_blocked(self) -> None:
        text = BINDING.read_text(encoding="utf-8")
        for marker in (
            DECISION,
            'contract_version: "4.5"',
            "THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON",
            "project_local_path: C:/Users/user/Documents/GitHub/Ninza/omenward",
            "godot_project_path: C:/Users/user/Documents/GitHub/Ninza/omenward",
            "PHASE_A_GPT_CHAT_PLANNING",
            "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED",
            "PHASE_C_BLOCKED",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("Switchy-Express-Cargo-Puzzle", text)

    def test_v45_machine_state_tracks_fresh_base_and_current_gate(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], "3.0")
        self.assertEqual(state["decision_id"], DECISION)
        self.assertEqual(state["activation_baseline_main_sha"], PROJECT_BASELINE)
        self.assertEqual(state["base_current_main_observed"], BASE_MAIN)
        self.assertEqual(state["active_contract"]["version"], "4.5")
        self.assertEqual(state["active_contract"]["adapter_policy"], "THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON")
        self.assertEqual(state["planning_phase"]["status"], "PHASE_A_GPT_CHAT_PLANNING")
        self.assertEqual(state["planning_phase"]["completion_trigger"], "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION")
        self.assertEqual(state["phase_c_gate"], "BLOCK")
        self.assertIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED", state["blocking_reasons"])
        self.assertEqual(state["runtime_pr"]["number"], 175)
        self.assertEqual(state["runtime_pr"]["head_sha"], "bde85549560fca90f7aa25fc4842bc0a3afb92e7")
        self.assertEqual(state["runtime_pr"]["issue"], 176)
        self.assertEqual(state["runtime_pr"]["approved_runtime_gap_count"], 7)
        self.assertEqual(state["handoff_pr"]["number"], 177)
        self.assertEqual(state["handoff_pr"]["disposition"], "REFERENCE_ONLY_DO_NOT_MERGE")

    def test_active_gdd_no_longer_exposes_superseded_special_t1_token_source(self) -> None:
        text = GDD.read_text(encoding="utf-8")
        special = text.split("### 특수병 병영", 1)[1].split("### 방어탑", 1)[0]
        self.assertIn("SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT", special)
        self.assertIn("SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT", special)
        self.assertIn("SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT", special)
        self.assertIn("SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS", special)
        self.assertNotRegex(special, r"(?m)^SPECIAL_T1_TOKEN_SOURCE = NONE$")
        self.assertNotIn("룰렛 TokenSource를 제공하지 않는다", special)

    def test_active_workbook_does_not_republish_superseded_none_assignment(self) -> None:
        text = WORKBOOK.read_text(encoding="utf-8")
        self.assertNotRegex(text, r"(?m)^SPECIAL_T1_TOKEN_SOURCE = NONE$")
        self.assertIn("SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT", text)
        self.assertIn(DECISION, text)

    def test_entry_documents_route_to_current_10_of_10_v45_phase_a(self) -> None:
        expected = {
            AGENTS: ("contract_version: 4.5", "planning_status: MAIN_CANONICAL_APPROVED_10_OF_10", "PHASE_A_GPT_CHAT_PLANNING"),
            PROJECT_CORE: ("MAIN_CANONICAL_APPROVED_10_OF_10", "PHASE_A_GPT_CHAT_PLANNING", "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE"),
            DOCUMENTATION_MAP: ("MAIN_CANONICAL_APPROVED_10_OF_10", "ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md", "ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"),
            ACTIVE_CONTEXT: (DECISION, "PHASE_A_GPT_CHAT_PLANNING", "PR175_DRAFT_7_RUNTIME_GAPS_OPEN"),
            CURRENT_STATUS: (DECISION, "PHASE_A_GPT_CHAT_PLANNING", "PR175_DRAFT_7_RUNTIME_GAPS_OPEN"),
            LEDGER: (DECISION, "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5", BASE_MAIN),
        }
        for path, markers in expected.items():
            text = path.read_text(encoding="utf-8")
            for marker in markers:
                self.assertIn(marker, text, f"{path.relative_to(ROOT)} missing {marker}")

    def test_lifecycle_routes_v45_as_current_and_v44_as_history(self) -> None:
        text = LIFECYCLE.read_text(encoding="utf-8")
        self.assertIn("ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md", text)
        self.assertIn("ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", text)
        self.assertIn("ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md", text)
        self.assertIn("HISTORICAL_V4_4_BINDING", text)

    def test_sheet_sync_evidence_uses_same_decision_id_and_bounded_readback(self) -> None:
        evidence = json.loads(SHEET_EVIDENCE.read_text(encoding="utf-8"))
        self.assertEqual(evidence["decision_id"], DECISION)
        self.assertEqual(evidence["spreadsheet_id"], SHEET_ID)
        self.assertEqual(evidence["sync_result"], "PASS")
        self.assertEqual(evidence["reread_result"], "PASS")
        self.assertEqual(evidence["base_main_observed"], BASE_MAIN)
        self.assertIn("00_프로젝트_허브!A2:L2", evidence["ranges"])
        self.assertIn("02_현재_확정결정", " ".join(evidence["ranges"]))
        self.assertIn("04_누락_충돌_감사", " ".join(evidence["ranges"]))
        self.assertIn("15_조작_게임규칙", " ".join(evidence["ranges"]))
        self.assertIn("99_변경이력", " ".join(evidence["ranges"]))


if __name__ == "__main__":
    unittest.main()
