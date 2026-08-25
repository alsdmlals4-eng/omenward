from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURRENT_CONTRACT = "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8"
STALE_GATE = "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST"
FINAL_REVIEW = "docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class PhaseBFinalPlanningReviewTests(unittest.TestCase):
    def test_phase_b_review_owner_closes_planning_without_new_product_decision(self) -> None:
        review = read("docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md")
        self.assertIn("OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1", review)
        self.assertIn("review_result: PASS", review)
        self.assertIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED", review)
        self.assertIn("NEW_PRODUCT_DECISION_REQUIRED = FALSE", review)
        self.assertIn("IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED", review)
        self.assertIn("PHASE_C_GATE = OPEN", review)
        self.assertIn("ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS", review)
        self.assertIn("FINAL_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING", review)

    def test_current_stage_authorities_use_elite_boss_cadence_not_legacy_danger(self) -> None:
        current_authorities = [
            "docs/PROJECT_CORE.md",
            "docs/OMENWARD_GDD_CURRENT_CANON.md",
        ]
        for path in current_authorities:
            text = read(path)
            with self.subTest(path=path):
                self.assertIn("DANGER_STAGE_TYPE = REMOVED", text)
                self.assertIn("ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE", text)
                self.assertIn("BOSS_STAGES = 5 / 10 / 15 / 20", text)
                self.assertNotIn("Danger = 4 / 9 / 14 / 19", text)
                self.assertNotIn("FIRST_DANGER_INTEGRATION", text)

        readme = read("README.md")
        self.assertIn("current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md", readme)
        self.assertIn("current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md", readme)

    def test_lifecycle_and_documentation_map_separate_current_owners_from_phase_b_history(self) -> None:
        lifecycle = read("docs/DOCUMENT_LIFECYCLE_REGISTRY.md")
        docmap = read("docs/DOCUMENTATION_MAP.md")
        for text in (lifecycle, docmap):
            self.assertIn("APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md", text)
            self.assertIn("APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md", text)
            self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md", text)
        self.assertIn("[증거/호환] docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md", lifecycle)
        self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW = HISTORICAL_PASS", lifecycle)
        self.assertIn("LEGACY_DANGER_CADENCE_AUTHORITY = NONE", lifecycle)
        self.assertIn("FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md", lifecycle)

    def test_current_phase_consumers_preserve_v48_history_while_current_route_is_paused(self) -> None:
        current_paths = [
            "AGENTS.md",
            "docs/ACTIVE_CONTEXT.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/DECISIONS_PENDING.md",
            "docs/DOCUMENTATION_MAP.md",
            "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
            "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
        ]
        for path in current_paths:
            text = read(path)
            with self.subTest(path=path):
                self.assertIn(CURRENT_CONTRACT, text)
                self.assertNotIn("PHASE_C_GATE = OPEN", text)
                self.assertNotIn(STALE_GATE, text)

        active = read("docs/ACTIVE_CONTEXT.md")
        pending = read("docs/DECISIONS_PENDING.md")
        self.assertIn("HISTORICAL_PRE_APPROVAL_GATE = IMPLEMENTATION_AUTHORITY_REQUIRED", active)
        self.assertIn("FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5", active)
        self.assertIn("FINAL_PLANNING_REVIEW_SCOPE = RETAINED_PRE_20260825_VISUAL_OVERRIDE_EVIDENCE", active)
        self.assertIn("PROJECT_ACTIVITY = PAUSED_QUEUED", active)
        self.assertIn("CURRENT_NEXT = USER_EXPLICIT_REACTIVATION", active)
        self.assertIn("CURRENT_CANON_RECONCILIATION = REQUIRED_UNTIL_EXACT_HEAD_GREEN_AND_MERGED_MAIN_READBACK", pending)
        self.assertIn("CURRENT_IMPLEMENTATION_AUTHORITY = NONE", pending)

    def test_current_final_review_closes_planning_without_runtime_promotion(self) -> None:
        review = read(FINAL_REVIEW)
        for marker in (
            "status: PASS_5_OF_5",
            "ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
            "NEW_PRODUCT_DECISION_REQUIRED = FALSE",
            "CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED",
            "IMPLEMENTATION_AUTHORITY = NONE",
            "CURRENT_GODOT_RUNTIME = NOT_RUN",
            "CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN",
        ):
            self.assertIn(marker, review)

    def test_machine_state_preserves_historical_phase_b_transition(self) -> None:
        state = json.loads(read("docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"))
        phase = state["planning_phase"]
        self.assertIs(phase["completion_declared"], True)
        self.assertEqual(phase["phase_b_status"], "PASS")
        self.assertEqual(phase["phase_c_status"], "READY_TO_ENTER")
        self.assertEqual(state["phase_c_gate"], "OPEN")
        self.assertNotIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED", state["blocking_reasons"])
        self.assertNotIn("PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN", state["blocking_reasons"])
        self.assertIn("ISSUE176_7_RUNTIME_GAPS_OPEN", state["blocking_reasons"])

    def test_phase_b_history_and_current_runtime_boundary_do_not_cross(self) -> None:
        review = read("docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md")
        self.assertIn("PR175 = OPEN_DRAFT", review)
        self.assertIn("ISSUE176_APPROVED_RUNTIME_GAPS = 7", review)
        self.assertIn("USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4", review)
        self.assertIn("GODOT_AI_3_1_4_CANON_AUTHORITY_RECONCILIATION = DEFER_TO_PHASE_C_FRESH_VERIFY", review)

        status = read("docs/CURRENT_IMPLEMENTATION_STATUS.md")
        pending = read("docs/DECISIONS_PENDING.md")
        for text in (status, pending):
            self.assertIn("FINAL_PARAMETER_VECTOR = NOT_SELECTED", text)
            self.assertIn("FINAL_PRODUCT_NUMERICS = NOT_APPROVED", text)
        self.assertNotIn("PR175 = OPEN_DRAFT", status)
        self.assertIn("CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED", status)
        self.assertIn("CURRENT_GODOT_RUNTIME = NOT_RUN", status)
        self.assertIn("CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN", status)


if __name__ == "__main__":
    unittest.main()
