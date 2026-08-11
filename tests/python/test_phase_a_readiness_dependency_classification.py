from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]

REVIEW = ROOT / "docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md"
PHASE_B = ROOT / "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"
WORKFLOW = ROOT / ".github/workflows/validate-canon-freshness-v4-5.yml"

ACTIVATION_DECISION = "OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1"
TAXONOMY = (
    "IMPLEMENTATION_COMPLETENESS",
    "PROVISIONAL_IMPLEMENTATION_INPUT_APPROVED",
    "POST_RUNTIME_EVIDENCE_TUNING",
    "FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER",
    "LEVEL_OR_IMPLEMENTATION_DETAIL_DEFERRED",
    "RELEASE_PHASE_DEFERRED",
    "HISTORICAL_OR_SUPERSEDED",
)


class PhaseAReadinessDependencyClassificationTest(unittest.TestCase):
    def test_v45_workflow_executes_historical_phase_a_contract(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("tests/python/test_phase_a_readiness_dependency_classification.py", text)
        self.assertIn("python -m unittest tests.python.test_phase_a_readiness_dependency_classification -v", text)

    def test_historical_review_preserves_phase_a_taxonomy_and_closed_gate_at_that_time(self) -> None:
        self.assertTrue(REVIEW.is_file())
        text = REVIEW.read_text(encoding="utf-8")
        self.assertIn(ACTIVATION_DECISION, text)
        for marker in TAXONOMY:
            self.assertIn(marker, text)
        for historical_gate in (
            "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED",
            "PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN",
            "PHASE_C_BLOCKED",
        ):
            self.assertIn(historical_gate, text)

    def test_historical_review_preserves_runtime_dependency_direction(self) -> None:
        text = REVIEW.read_text(encoding="utf-8")
        for marker in (
            "ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS",
            "ROLE_OUTPUT_RUNTIME -> DETERMINISTIC_MEASUREMENT -> FUNCTIONAL_VALUE_COMPARISON -> FINAL_TUNING",
            "SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING",
            "PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175",
            "T3_CONTENT_AND_FINAL_NAMES = FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER",
        ):
            self.assertIn(marker, text)

    def test_phase_b_owner_records_the_later_transition_without_rewriting_phase_a_history(self) -> None:
        current = PHASE_B.read_text(encoding="utf-8")
        for marker in (
            "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED",
            "PHASE_B_FINAL_PLANNING_REVIEW = PASS",
            "IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED",
            "PHASE_C_GATE = OPEN",
            "ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS",
            "FINAL_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING",
        ):
            self.assertIn(marker, current)
        historical = REVIEW.read_text(encoding="utf-8")
        self.assertIn("PHASE_C_BLOCKED", historical)
        self.assertNotIn("PHASE_C_GATE = OPEN", historical)


if __name__ == "__main__":
    unittest.main()
