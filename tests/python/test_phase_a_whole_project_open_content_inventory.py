from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/validate-canon-freshness-v4-5.yml"
REVIEW = ROOT / "docs/reviews/PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_INVENTORY_2026-08-11.md"

CURRENT_ROUTERS = (
    ROOT / "AGENTS.md",
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    ROOT / "docs/DECISIONS_PENDING.md",
    ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md",
    ROOT / "docs/PROJECT_CORE.md",
    ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
)

STATE_MARKERS = (
    "ONBOARDING_PLANNING_STATUS = MAIN_CANONICAL_APPROVED_10_OF_10",
    "ONBOARDING_10_OF_10_SCOPE = ONBOARDING_BATCH_ONLY",
    "WHOLE_PROJECT_PHASE_A_STATUS = OPEN_CONTENT_REMAINING",
    "WHOLE_PROJECT_PLANNING_COMPLETE = FALSE",
    "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED",
    "PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN",
    "PHASE_C_BLOCKED",
)

OPEN_GROUPS = (
    "OPEN_GROUP_1 = BUILDING_T3_DETAILS_AND_FINAL_BRANCH_NAMING",
    "OPEN_GROUP_2 = HERO_LEGENDARY_FAMILY_REVALIDATION",
    "OPEN_GROUP_3 = META_HUB_REVALIDATION",
)


class PhaseAWholeProjectOpenContentInventoryTest(unittest.TestCase):
    def test_v45_workflow_executes_inventory_contract(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("tests/python/test_phase_a_whole_project_open_content_inventory.py", text)
        self.assertIn(
            "python -m unittest tests.python.test_phase_a_whole_project_open_content_inventory -v",
            text,
        )

    def test_review_artifact_exists_and_has_additive_phase_model(self) -> None:
        self.assertTrue(REVIEW.is_file(), f"missing inventory review: {REVIEW.relative_to(ROOT)}")
        text = REVIEW.read_text(encoding="utf-8")
        for marker in STATE_MARKERS + OPEN_GROUPS:
            self.assertIn(marker, text)

    def test_current_routers_do_not_equate_onboarding_10_of_10_with_whole_project_completion(self) -> None:
        for path in CURRENT_ROUTERS:
            text = path.read_text(encoding="utf-8")
            for marker in STATE_MARKERS:
                self.assertIn(marker, text, f"{path.relative_to(ROOT)} missing {marker}")
            self.assertNotIn("WHOLE_PROJECT_PLANNING_COMPLETE = TRUE", text)

    def test_only_three_genuine_new_product_decision_groups_are_identified(self) -> None:
        review = REVIEW.read_text(encoding="utf-8")
        for marker in OPEN_GROUPS:
            self.assertIn(marker, review)
        self.assertIn("Genuine new product Decision groups = 3", review)

    def test_held_hero_and_meta_are_not_current_implementation_input(self) -> None:
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("HERO_LEGENDARY_CURRENT_STATUS = HELD_REVALIDATION_REQUIRED", review)
        self.assertIn("HERO_LEGENDARY_IMPLEMENTATION_AUTHORITY = NONE", review)
        self.assertIn("META_HUB_CURRENT_STATUS = HELD_REVALIDATION_REQUIRED", review)
        self.assertIn("META_HUB_IMPLEMENTATION_AUTHORITY = NONE", review)

    def test_building_t3_is_partial_open_but_troop_t3_structure_is_not_reset(self) -> None:
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("BUILDING_T3_DETAILS = GENUINE_OPEN_PRODUCT_DECISION", review)
        self.assertIn("DEFENSE_BRANCH_FINAL_DISPLAY_NAME = GENUINE_OPEN_PRODUCT_DECISION", review)
        self.assertIn("TROOP_T3_ROLE_GRADE_STRUCTURE = APPROVED_POC_STRUCTURE", review)
        self.assertIn("ARCHER_T3_CURRENT = CROSSBOW_ARCHER / RAPID_FIRE_ARCHER", review)
        self.assertIn("TROOP_T3_EXACT_NUMERICS = POST_RUNTIME_OR_LATER_BALANCE_TUNING", review)

    def test_prior_non_blocker_classification_is_preserved(self) -> None:
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS", review)
        self.assertIn("FINAL_FV_AND_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING", review)
        self.assertIn("PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175", review)

    def test_next_step_is_user_grill_me_not_automatic_product_approval(self) -> None:
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("NEXT_PRODUCT_GATE = USER_GRILL_ME_APPROVAL_REQUIRED", review)
        self.assertIn("AUTO_APPROVE_NEW_PRODUCT_CHOICES = FORBIDDEN", review)
        self.assertIn("MAX_GRILL_ME_DECISIONS = 10", review)


if __name__ == "__main__":
    unittest.main()
