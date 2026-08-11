from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]

AGENTS = ROOT / "AGENTS.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
GDD = ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md"
ONBOARDING = ROOT / "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md"
WORKBOOK = ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md"
REVIEW = ROOT / "docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md"
PHASE_B = ROOT / "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"
PRODUCT_CLOSURE = ROOT / "docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md"
WORKFLOW = ROOT / ".github/workflows/validate-canon-freshness-v4-5.yml"

CURRENT_CONSUMERS = (AGENTS, GDD, ONBOARDING, WORKBOOK)
ACTIVATION_DECISION = "OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1"
PRODUCT_CLOSURE_DECISION = "OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1"
PHYSICAL_TOKEN_MARKERS = (
    "TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1",
    "TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3",
    "FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN",
)
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
    def test_v45_workflow_executes_readiness_contract(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("tests/python/test_phase_a_readiness_dependency_classification.py", text)
        self.assertIn("python -m unittest tests.python.test_phase_a_readiness_dependency_classification -v", text)

    def test_historical_review_artifact_still_preserves_phase_a_taxonomy(self) -> None:
        self.assertTrue(REVIEW.is_file())
        text = REVIEW.read_text(encoding="utf-8")
        self.assertIn(ACTIVATION_DECISION, text)
        for marker in TAXONOMY:
            self.assertIn(marker, text)
        self.assertIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED", text)
        self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN", text)
        self.assertIn("PHASE_C_BLOCKED", text)

    def test_current_consumers_keep_physical_token_truth(self) -> None:
        for path in CURRENT_CONSUMERS:
            text = path.read_text(encoding="utf-8")
            for marker in PHYSICAL_TOKEN_MARKERS:
                self.assertIn(marker, text, f"{path.relative_to(ROOT)} missing {marker}")
            self.assertNotIn("TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION", text)

    def test_special_selection_distribution_stays_tuning(self) -> None:
        for path in (AGENTS, PENDING, GDD, ONBOARDING, REVIEW, PHASE_B):
            text = path.read_text(encoding="utf-8")
            self.assertIn("SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING", text)

    def test_runtime_dependency_direction_is_preserved(self) -> None:
        for path in (REVIEW, PHASE_B, PENDING, GDD):
            text = path.read_text(encoding="utf-8")
            self.assertIn("ROLE_OUTPUT_RUNTIME -> DETERMINISTIC_MEASUREMENT -> FUNCTIONAL_VALUE_COMPARISON -> FINAL_TUNING", text)
        self.assertIn("ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS", PHASE_B.read_text(encoding="utf-8"))
        self.assertIn("FINAL_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING", PHASE_B.read_text(encoding="utf-8"))

    def test_platform_save_export_store_remains_release_deferred(self) -> None:
        for path in (PENDING, PHASE_B):
            text = path.read_text(encoding="utf-8")
            self.assertIn("PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175", text)
            self.assertIn("SHARED_SAVE_SCHEMA = NOT_STARTED", text)
            self.assertIn("EXPORT_PRESETS = ABSENT", text)

    def test_product_closure_remains_closed_without_fake_final_numerics(self) -> None:
        pending = PENDING.read_text(encoding="utf-8")
        product = PRODUCT_CLOSURE.read_text(encoding="utf-8")
        self.assertIn(PRODUCT_CLOSURE_DECISION, pending)
        self.assertIn(PRODUCT_CLOSURE_DECISION, product)
        self.assertIn("T3_CONTENT_AND_FINAL_NAMES = RESOLVED_AT_PRODUCT_GRAMMAR_LEVEL", pending)
        self.assertIn("WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0", pending)
        self.assertIn("FINAL_PARAMETER_VECTOR = NOT_SELECTED", pending)
        self.assertIn("FINAL_PRODUCT_NUMERICS = NOT_APPROVED", pending)
        self.assertIn("정확 수치와 일부 역할별 세부 scalar는 runtime/balance evidence에서 확정한다.", product)

    def test_current_phase_gate_is_open_only_after_phase_b_pass(self) -> None:
        for path in (AGENTS, PENDING, GDD, ONBOARDING, WORKBOOK, PHASE_B):
            text = path.read_text(encoding="utf-8")
            self.assertIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED", text)
            self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW = PASS", text)
            self.assertIn("PHASE_C_GATE = OPEN", text)
        self.assertIn("IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED", PHASE_B.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
