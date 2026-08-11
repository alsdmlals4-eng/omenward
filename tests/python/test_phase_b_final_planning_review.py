from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


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

    def test_current_stage_consumers_use_elite_boss_cadence_not_legacy_danger(self) -> None:
        current_paths = [
            "README.md",
            "docs/PROJECT_CORE.md",
            "docs/OMENWARD_GDD_CURRENT_CANON.md",
        ]
        for path in current_paths:
            text = read(path)
            with self.subTest(path=path):
                self.assertIn("DANGER_STAGE_TYPE = REMOVED", text)
                self.assertIn("ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE", text)
                self.assertIn("BOSS_STAGES = 5 / 10 / 15 / 20", text)
                self.assertNotIn("Danger = 4 / 9 / 14 / 19", text)
                self.assertNotIn("FIRST_DANGER_INTEGRATION", text)

    def test_lifecycle_and_documentation_map_route_latest_product_owners(self) -> None:
        lifecycle = read("docs/DOCUMENT_LIFECYCLE_REGISTRY.md")
        docmap = read("docs/DOCUMENTATION_MAP.md")
        for text in (lifecycle, docmap):
            self.assertIn("APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md", text)
            self.assertIn("APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md", text)
            self.assertIn("APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md", text)
            self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md", text)
        self.assertIn("LEGACY_DANGER_CADENCE_AUTHORITY = NONE", lifecycle)

    def test_current_phase_consumers_record_received_gate_and_phase_b_pass(self) -> None:
        current_paths = [
            "AGENTS.md",
            "docs/ACTIVE_CONTEXT.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/DECISIONS_PENDING.md",
            "docs/DOCUMENTATION_MAP.md",
            "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
            "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
            "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
        ]
        for path in current_paths:
            text = read(path)
            with self.subTest(path=path):
                self.assertIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED", text)
                self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW = PASS", text)
                self.assertIn("PHASE_C_GATE = OPEN", text)

    def test_machine_state_opens_phase_c_only_after_phase_b_pass(self) -> None:
        state = json.loads(read("docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"))
        phase = state["planning_phase"]
        self.assertIs(phase["completion_declared"], True)
        self.assertEqual(phase["phase_b_status"], "PASS")
        self.assertEqual(phase["phase_c_status"], "READY_TO_ENTER")
        self.assertEqual(state["phase_c_gate"], "OPEN")
        self.assertNotIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED", state["blocking_reasons"])
        self.assertNotIn("PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN", state["blocking_reasons"])
        self.assertIn("ISSUE176_7_RUNTIME_GAPS_OPEN", state["blocking_reasons"])

    def test_phase_b_does_not_fake_runtime_or_numeric_completion(self) -> None:
        status = read("docs/CURRENT_IMPLEMENTATION_STATUS.md")
        pending = read("docs/DECISIONS_PENDING.md")
        for text in (status, pending):
            self.assertIn("PR175 = OPEN_DRAFT", text)
            self.assertIn("ISSUE176_APPROVED_RUNTIME_GAPS = 7", text)
            self.assertIn("FINAL_PARAMETER_VECTOR = NOT_SELECTED", text)
            self.assertIn("FINAL_PRODUCT_NUMERICS = NOT_APPROVED", text)
            self.assertIn("USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4", text)
            self.assertIn("GODOT_AI_3_1_4", text)


if __name__ == "__main__":
    unittest.main()
