from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-STAGE2-FIRST-T2-CANDIDATES-AND-GOLD-RULES-V1"
PARENT_DECISION_ID = "OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1"
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_STAGE2_FIRST_T2_CANDIDATES_AND_GOLD_RULES_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_STAGE2_FIRST_T2_CANDIDATES_AND_GOLD_RULES_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-stage2-first-t2-candidates-gold-rules-design.md"
ONBOARDING = ROOT / "docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md"


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class Stage2FirstT2CandidatesGoldRulesCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (AUTHORITY, REVIEW, SPEC, ONBOARDING):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_decision_and_checkpoint_are_explicit(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            DECISION_ID,
            PARENT_DECISION_ID,
            "DECISION_STATUS = PARTIAL_APPROVAL_7_OF_10",
            "APPROVAL_CHECKPOINT = FIRST_STAGE2_T2_CANDIDATES_AND_GOLD_RULES",
        ):
            self.assertIn(marker, text)

    def test_first_candidates_are_fixed_same_building_branches(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "FIRST_STAGE2_T2_CANDIDATES = GENERAL_BARRACKS_T2_SHIELD / GENERAL_BARRACKS_T2_ARCHER",
            "FIRST_STAGE2_CANDIDATE_BUILDING = STAGE1_GENERAL_BARRACKS",
            "FIRST_STAGE2_CHOICE_SCOPE = SAME_BUILDING_TWO_BRANCHES",
            "SHIELD_ROLE = FRONTLINE_DURABILITY_AND_STALL",
            "ARCHER_ROLE = SUSTAINED_RANGED_DAMAGE_AND_FLYING_PRIORITY",
        ):
            self.assertIn(marker, text)

    def test_gold_contract_guarantees_one_without_surplus(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "FIRST_STAGE2_PAIR_COST_CLASS = SAME",
            "STAGE_2_REAL_GOLD_GRANT = EXACTLY_ONE_CANDIDATE_EFFECTIVE_COST",
            "STAGE_2_REQUIRED_COST_RESERVE = ONE_FIRST_T2_UPGRADE",
            "STAGE_2_NON_CANDIDATE_SPENDING_BEFORE_CHOICE = BLOCKED",
            "STAGE_2_GRANT_SURPLUS = FORBIDDEN",
            "STAGE_2_PREEXISTING_GOLD = PRESERVED",
            "STAGE_2_LEFTOVER_GOLD_AFTER_CHOICE = NORMAL_WALLET",
        ):
            self.assertIn(marker, text)

    def test_choice_is_local_irreversible_not_global_lock(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "FIRST_STAGE2_CHOICE_CONFIRMATION = REQUIRED",
            "FIRST_STAGE2_BRANCH_CHANGE_AFTER_CONFIRMATION = FORBIDDEN",
            "UNCHOSEN_BRANCH_GLOBAL_LOCK = FALSE",
            "OTHER_GENERAL_BARRACKS_CAN_SELECT_UNCHOSEN_BRANCH = TRUE",
        ):
            self.assertIn(marker, text)

    def test_next_pressure_keeps_both_paths_valid(self) -> None:
        text = read(AUTHORITY)
        review = read(REVIEW)
        for marker in (
            "FIRST_STAGE2_NEXT_PRESSURE = MIXED_SOFT_COUNTER",
            "FIRST_STAGE2_HARD_COUNTER_REQUIREMENT = FORBIDDEN",
            "SCRIPTED_OUTCOME = FORBIDDEN",
        ):
            self.assertIn(marker, text)
        for marker in (
            "FALSE_CHOICE_BY_OMEN",
            "SHIELD_ARCHER_VALUE_ASYMMETRY",
            "TUTORIAL_ONLY_PRICE_DRIFT",
            "GLOBAL_LOCK_MISREAD",
            "PRODUCT_CODE = UNCHANGED",
        ):
            self.assertIn(marker, review)

    def test_onboarding_parent_is_promoted_to_checkpoint_seven(self) -> None:
        text = read(ONBOARDING)
        for marker in (
            DECISION_ID,
            "DECISION_STATUS = PARTIAL_APPROVAL_7_OF_10",
            "FIRST_STAGE2_T2_CANDIDATES = GENERAL_BARRACKS_T2_SHIELD / GENERAL_BARRACKS_T2_ARCHER",
            "STAGE_2_LEFTOVER_GOLD_AFTER_CHOICE = NORMAL_WALLET",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("FIRST_STAGE2_T2_CANDIDATES = PENDING_GRILLME", text)
        self.assertNotIn("STAGE_2_LEFTOVER_GOLD_POLICY = PENDING_GRILLME", text)

    def test_numeric_and_product_boundaries_remain_closed(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "T2_EXACT_COST = PENDING_SIMULATION",
            "TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION",
            "PRODUCT_CODE = UNCHANGED",
            "SCENE_RESOURCE_DATA = UNCHANGED",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
