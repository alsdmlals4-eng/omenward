from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION = "OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1"
ACTIVATION_DECISION = "OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1"
PHASE_B_DECISION = "OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1"
C0_LOCAL_DECISION = "OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1"
BASE_MAIN = "069f0c9654a6cde7cea6f3343dd2fa81c6248d5d"
PROJECT_BASELINE = "87339f87949c8faea0dfe1482c5d0887a04d94f4"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"

BINDING = ROOT / "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"
CANONICAL_V45_R2 = ROOT / "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md"
GDD = ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md"
WORKBOOK = ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md"
ACTIVE_CONTEXT = ROOT / "docs/ACTIVE_CONTEXT.md"
CURRENT_STATUS = ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
AGENTS = ROOT / "AGENTS.md"
README = ROOT / "README.md"
PROJECT_CORE = ROOT / "docs/PROJECT_CORE.md"
ROADMAP = ROOT / "docs/OMENWARD_ROADMAP.md"
DOCUMENTATION_MAP = ROOT / "docs/DOCUMENTATION_MAP.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
PHASE_B_REVIEW = ROOT / "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"


class CanonFreshnessV45RoutingTest(unittest.TestCase):
    def test_v45_authority_files_exist(self) -> None:
        for path in (BINDING, STATE, CANONICAL_V45_R2, PHASE_B_REVIEW):
            self.assertTrue(path.is_file(), f"missing authority artifact: {path.relative_to(ROOT)}")

    def test_v45_r2_full_instruction_remains_repo_canonical_source(self) -> None:
        text = CANONICAL_V45_R2.read_text(encoding="utf-8")
        for marker in (
            "contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION",
            "contract_version: '4.5'",
            "revision: '2026-08-11-r2'",
            "adapter_policy: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON",
            'project_local_path: "C:/Users/user/Documents/GitHub/Ninza/omenward"',
            'godot_project_path: "C:/Users/user/Documents/GitHub/Ninza/omenward"',
        ):
            self.assertIn(marker, text)
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["active_contract"]["source"], str(CANONICAL_V45_R2.relative_to(ROOT)).replace("\\", "/"))
        self.assertEqual(state["active_contract"]["activation_decision_id"], ACTIVATION_DECISION)

    def test_machine_state_records_phase_b_transition_without_runtime_completion(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], "3.0")
        self.assertEqual(state["decision_id"], DECISION)
        self.assertEqual(state["phase_b_decision_id"], PHASE_B_DECISION)
        self.assertEqual(state["activation_baseline_main_sha"], PROJECT_BASELINE)
        self.assertEqual(state["base_current_main_observed"], BASE_MAIN)
        self.assertEqual(state["planning_phase"]["status"], "PHASE_B_FINAL_PLANNING_REVIEW_PASS")
        self.assertIs(state["planning_phase"]["completion_declared"], True)
        self.assertEqual(state["planning_phase"]["phase_b_status"], "PASS")
        self.assertEqual(state["planning_phase"]["phase_c_status"], "READY_TO_ENTER")
        self.assertEqual(state["phase_c_gate"], "OPEN")
        self.assertEqual(state["blocking_reasons"], ["ISSUE176_7_RUNTIME_GAPS_OPEN"])
        self.assertEqual(state["runtime_pr"]["number"], 175)
        self.assertEqual(state["runtime_pr"]["head_sha"], "bde85549560fca90f7aa25fc4842bc0a3afb92e7")
        self.assertEqual(state["runtime_pr"]["approved_runtime_gap_count"], 7)
        self.assertEqual(state["runtime_pr"]["merge"], "FORBIDDEN_UNTIL_RUNTIME_ACCEPTANCE")
        self.assertEqual(state["handoff_pr"]["number"], 177)
        self.assertEqual(state["handoff_pr"]["disposition"], "REFERENCE_ONLY_DO_NOT_MERGE")
        self.assertIsNone(state["product_boundary"]["final_parameter_vector"])
        self.assertEqual(state["product_boundary"]["final_product_numerics"], "NOT_APPROVED")

    def test_active_gdd_routes_special_t1_token_source_and_new_cadence(self) -> None:
        text = GDD.read_text(encoding="utf-8")
        special = text.split("### 특수병 병영", 1)[1].split("### 방어탑", 1)[0]
        for marker in (
            "SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT",
            "SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT",
            "SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT",
            "SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS",
            "TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1",
            "TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3",
            "FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN",
        ):
            self.assertIn(marker, special)
        for marker in (
            "DANGER_STAGE_TYPE = REMOVED",
            "ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE",
            "BOSS_STAGES = 5 / 10 / 15 / 20",
            "PHASE_B_FINAL_PLANNING_REVIEW = PASS",
            "PHASE_C_GATE = OPEN",
        ):
            self.assertIn(marker, text)

    def test_active_workbook_routes_current_token_and_phase_b_decision(self) -> None:
        text = WORKBOOK.read_text(encoding="utf-8")
        self.assertIn("SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT", text)
        self.assertIn(DECISION, text)
        self.assertIn(PHASE_B_DECISION, text)
        self.assertIn(SHEET_ID, text)
        self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW = PASS", text)

    def test_entry_documents_route_to_phase_b_pass(self) -> None:
        expected = {
            AGENTS: ("contract_version: 4.5", "MAIN_CANONICAL_APPROVED_10_OF_10", "PHASE_B_FINAL_PLANNING_REVIEW = PASS", "PHASE_C_GATE = OPEN"),
            PROJECT_CORE: ("MAIN_CANONICAL_APPROVED_10_OF_10", "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE", "PHASE_B_FINAL_PLANNING_REVIEW = PASS"),
            DOCUMENTATION_MAP: ("MAIN_CANONICAL_APPROVED_10_OF_10", "ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md", "ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"),
            ACTIVE_CONTEXT: (PHASE_B_DECISION, "PR175_DRAFT_7_RUNTIME_GAPS_OPEN", "PHASE_C_GATE = OPEN"),
            CURRENT_STATUS: (PHASE_B_DECISION, "PR175_DRAFT_7_RUNTIME_GAPS_OPEN", "PHASE_C_GATE = OPEN"),
            PENDING: (PHASE_B_DECISION, "ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS", "PHASE_C_GATE = OPEN"),
        }
        for path, markers in expected.items():
            text = path.read_text(encoding="utf-8")
            for marker in markers:
                self.assertIn(marker, text, f"{path.relative_to(ROOT)} missing {marker}")

    def test_current_execution_routers_advance_through_c0_local_pass(self) -> None:
        current_routers = (AGENTS, README, PROJECT_CORE, PENDING, ROADMAP)
        for path in current_routers:
            text = path.read_text(encoding="utf-8")
            self.assertIn(C0_LOCAL_DECISION, text, f"{path.relative_to(ROOT)} missing current C0 Decision")
            self.assertIn("PHASE_C_C0_OVERALL = PASS", text, f"{path.relative_to(ROOT)} missing C0 PASS")
            self.assertIn("PR175_CURRENT_MAIN_REVALIDATION_NEXT", text, f"{path.relative_to(ROOT)} missing current next gate")
            self.assertNotIn(
                "GODOT_AI_3_1_4_CANON_AUTHORITY_RECONCILIATION = DEFER_TO_PHASE_C_FRESH_VERIFY",
                text,
                f"{path.relative_to(ROOT)} still defers already-verified Godot AI authority",
            )

    def test_lifecycle_routes_v45_current_phase_b_and_v44_history(self) -> None:
        text = LIFECYCLE.read_text(encoding="utf-8")
        self.assertIn("ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md", text)
        self.assertIn("ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", text)
        self.assertIn("ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md", text)
        self.assertIn("HISTORICAL_V4_4_BINDING", text)
        self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md", text)
        self.assertIn("LEGACY_DANGER_CADENCE_AUTHORITY = NONE", text)


if __name__ == "__main__":
    unittest.main()
