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
WORKFLOW = ROOT / ".github/workflows/validate-canon-freshness-v4-5.yml"

CURRENT_CONSUMERS = (AGENTS, GDD, ONBOARDING, WORKBOOK)

ACTIVATION_DECISION = "OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1"
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
        self.assertIn('"tests/python/test_phase_a_readiness_dependency_classification.py"', text)
        self.assertIn("tests/python/test_phase_a_readiness_dependency_classification.py", text)
        self.assertIn(
            "python -m unittest tests.python.test_phase_a_readiness_dependency_classification -v",
            text,
        )

    def test_review_artifact_exists_and_uses_same_activation_decision(self) -> None:
        self.assertTrue(REVIEW.is_file(), f"missing readiness review: {REVIEW.relative_to(ROOT)}")
        text = REVIEW.read_text(encoding="utf-8")
        self.assertIn(ACTIVATION_DECISION, text)
        for marker in TAXONOMY:
            self.assertIn(marker, text)

    def test_physical_token_count_is_not_republished_as_pending(self) -> None:
        for path in CURRENT_CONSUMERS:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn(
                "TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION",
                text,
                f"{path.relative_to(ROOT)} republishes an ambiguous superseded physical-token pending marker",
            )
            for marker in PHYSICAL_TOKEN_MARKERS:
                self.assertIn(marker, text, f"{path.relative_to(ROOT)} missing {marker}")

    def test_special_selection_distribution_stays_tuning_not_fake_final(self) -> None:
        for path in (AGENTS, PENDING, GDD, ONBOARDING, REVIEW):
            text = path.read_text(encoding="utf-8")
            self.assertIn("SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING", text)
            self.assertNotIn("SPECIAL_T1_SELECTION_DISTRIBUTION = FINAL", text)

    def test_runtime_dependency_direction_is_preserved(self) -> None:
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn(
            "ROLE_OUTPUT_RUNTIME -> DETERMINISTIC_MEASUREMENT -> FUNCTIONAL_VALUE_COMPARISON -> FINAL_TUNING",
            review,
        )
        self.assertIn("ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS", review)
        self.assertIn("FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING", review)
        self.assertIn("FINAL_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING", review)

    def test_platform_save_export_store_are_not_pr175_prebuild_blockers(self) -> None:
        for path in (PENDING, REVIEW):
            text = path.read_text(encoding="utf-8")
            self.assertIn("PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175", text)
            self.assertIn("SHARED_SAVE_SCHEMA = NOT_STARTED", text)
            self.assertIn("EXPORT_PRESETS = ABSENT", text)
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("RELEASE_PHASE_DEFERRED", review)
        self.assertNotIn("PLATFORM_SAVE_EXPORT_STORE = COMPLETE", review)

    def test_open_full_product_content_is_not_silently_resolved(self) -> None:
        for path in (PENDING, REVIEW):
            text = path.read_text(encoding="utf-8")
            self.assertIn("T3_CONTENT_AND_FINAL_NAMES = FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER", text)
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("ARCHER_T3_LATER_APPROVED_DETAIL = CROSSBOW_ARCHER / RAPID_FIRE_ARCHER", review)
        self.assertIn("DEFENSE_TOWER_T3_DETAILS = FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER", review)

    def test_phase_gate_remains_closed(self) -> None:
        for path in (AGENTS, PENDING, GDD, ONBOARDING, WORKBOOK, REVIEW):
            text = path.read_text(encoding="utf-8")
            self.assertIn("PHASE_C_BLOCKED", text)
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED", review)
        self.assertIn("PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN", review)
        self.assertNotIn("PHASE_C_OPEN", review)

    def test_workbook_no_longer_routes_to_closed_pr178(self) -> None:
        text = WORKBOOK.read_text(encoding="utf-8")
        self.assertNotIn("current_working_pr: 178", text)
        self.assertIn("current_phase_a_focus: PR175_PHASE_A_READINESS_REVIEW", text)
        self.assertIn("sheet_sync_status: MERGED_CANON_BOUNDED_REREAD_PASS", text)


if __name__ == "__main__":
    unittest.main()
