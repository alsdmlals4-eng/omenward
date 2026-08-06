from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
AMENDMENT = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_REVIEW_2026-08-06.md"
BUILDING = ROOT / "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md"
SPECIAL = ROOT / "docs/design/APPROVED_OMENWARD_SPECIAL_T1_RANDOM_SELECTION_AND_PREVIEW_TIMING_2026-08-06.md"
ONBOARDING = ROOT / "docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md"
CURRENT = ROOT / "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md"


class BarracksAutoProductionTokenSourceAmendmentCanonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.amendment = AMENDMENT.read_text(encoding="utf-8")
        cls.review = REVIEW.read_text(encoding="utf-8")
        cls.building = BUILDING.read_text(encoding="utf-8")
        cls.special = SPECIAL.read_text(encoding="utf-8")
        cls.onboarding = ONBOARDING.read_text(encoding="utf-8")
        cls.current = CURRENT.read_text(encoding="utf-8")

    def test_amendment_decision_and_precedence_are_explicit(self) -> None:
        self.assertIn(
            "decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-AUTO-PRODUCTION-AND-TOKEN-SOURCE-AMENDMENT-V1",
            self.amendment,
        )
        self.assertIn("SUPERSEDES_SPECIAL_T1_NO_TOKEN_SOURCE_CLAUSES = TRUE", self.amendment)
        self.assertIn("SPECIAL_T1_TOKEN_SOURCE_NONE = SUPERSEDED", self.amendment)

    def test_both_barracks_tiers_produce_and_supply_token_sources(self) -> None:
        for marker in (
            "GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY",
            "GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY",
            "GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT",
            "GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT",
            "SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT",
            "SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT",
            "SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT",
            "SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.amendment)

    def test_special_t1_uses_one_fixed_selected_unit_for_both_paths(self) -> None:
        for marker in (
            "SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT",
            "SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1",
            "SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS",
            "SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN",
            "SPECIAL_T1_FREE_REROLL = FORBIDDEN",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.amendment)

    def test_exact_token_weights_remain_unfixed(self) -> None:
        self.assertIn("TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION", self.amendment)
        self.assertIn("SPECIAL_T1_TOKEN_WEIGHT = PENDING_SIMULATION", self.amendment)
        self.assertIn("SPECIAL_AUTO_PRODUCTION_INTERVAL = LONGER_THAN_GENERAL_UNIT", self.amendment)

    def test_current_authorities_no_longer_require_no_token_source(self) -> None:
        for text in (self.building, self.special, self.onboarding, self.current):
            self.assertNotIn("SPECIAL_T1_TOKEN_SOURCE = NONE", text)
            self.assertIn("SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT", text)

    def test_adversarial_review_covers_double_value_and_pool_dilution(self) -> None:
        for marker in (
            "SPECIAL_T1_DOUBLE_VALUE_RISK",
            "RANDOM_SOURCE_LOCK_IN",
            "TOKEN_POOL_DILUTION",
            "AUTO_PRODUCTION_TOKEN_SOURCE_CONFLATION",
            "PRODUCT_CODE = UNCHANGED",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.review)


if __name__ == "__main__":
    unittest.main()
