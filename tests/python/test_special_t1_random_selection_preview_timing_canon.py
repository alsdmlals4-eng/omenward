from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-SPECIAL-T1-RANDOM-SELECTION-AND-PREVIEW-TIMING-V1"
PARENT_DECISION_ID = "OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1"
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_SPECIAL_T1_RANDOM_SELECTION_AND_PREVIEW_TIMING_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_SPECIAL_T1_RANDOM_SELECTION_AND_PREVIEW_TIMING_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-special-t1-random-selection-preview-timing-design.md"
ONBOARDING = ROOT / "docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md"


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class SpecialT1RandomSelectionPreviewTimingCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (AUTHORITY, REVIEW, SPEC, ONBOARDING):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_decision_and_checkpoint_are_explicit(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            DECISION_ID,
            PARENT_DECISION_ID,
            "DECISION_STATUS = PARTIAL_APPROVAL_8_OF_10",
            "APPROVAL_CHECKPOINT = SPECIAL_T1_RANDOM_SELECTION_AND_PREVIEW_TIMING",
        ):
            self.assertIn(marker, text)

    def test_selection_occurs_once_per_building_after_successful_commit(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT",
            "SPECIAL_T1_SELECTION_POOL = MAGE / PRIEST / ASSASSIN / FLYING_UNIT / GIANT",
            "SPECIAL_T1_SELECTION_COUNT = ONE",
            "SPECIAL_T1_SELECTION_SCOPE = PER_BUILDING_INDEPENDENT",
            "SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1",
            "SPECIAL_T1_REPEATED_PRODUCTION = SELECTED_UNIT_ONLY",
        ):
            self.assertIn(marker, text)

    def test_result_is_revealed_before_production_timer_starts(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "SPECIAL_T1_RESULT_REVEAL = IMMEDIATELY_AFTER_CONSTRUCTION_COMMIT",
            "SPECIAL_T1_PRECOMMIT_RESULT_PREVIEW = FORBIDDEN",
            "SPECIAL_T1_PRODUCTION_TIMER_START = AFTER_RESULT_REVEAL",
            "REVEAL_NAME_ICON_ROLE = REQUIRED",
            "REVEAL_FIRST_PRODUCTION_COUNTDOWN = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_no_t1_token_source_and_t2_overrides_random_identity(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "SPECIAL_T1_TOKEN_SOURCE = NONE",
            "SPECIAL_T2_SPECIALIZATION_OVERRIDES_T1_SELECTION = TRUE",
            "SPECIAL_T2_SELECTED_UNIT_TOKEN_SOURCE = ENABLED",
        ):
            self.assertIn(marker, text)

    def test_free_reroll_and_save_scumming_are_forbidden(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN",
            "SPECIAL_T1_FREE_REROLL = FORBIDDEN",
            "SPECIAL_T1_REVEAL_THEN_FREE_CANCEL = FORBIDDEN",
            "SPECIAL_T1_FAILED_CONSTRUCTION_SELECTION = NOT_COMMITTED",
            "SPECIAL_T1_SELECTION_SAVE_PERSISTENCE = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_adversarial_review_covers_randomness_failure_modes(self) -> None:
        text = read(REVIEW)
        for marker in (
            "SAVE_SCUM_REROLL",
            "REVEAL_CANCEL_REROLL",
            "DEAD_ROLL_BY_UPCOMING_PRESSURE",
            "RANDOM_VALUE_ASYMMETRY",
            "T2_OVERRIDE_CONFUSION",
            "PRODUCT_CODE = UNCHANGED",
        ):
            self.assertIn(marker, text)

    def test_onboarding_parent_is_promoted_to_checkpoint_eight(self) -> None:
        text = read(ONBOARDING)
        for marker in (
            DECISION_ID,
            "DECISION_STATUS = PARTIAL_APPROVAL_8_OF_10",
            "SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT",
            "SPECIAL_T1_RESULT_REVEAL = IMMEDIATELY_AFTER_CONSTRUCTION_COMMIT",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("SPECIAL_T1_RANDOM_SELECTION_TIMING = PENDING_GRILLME", text)
        self.assertNotIn("SPECIAL_T1_RESULT_PREVIEW = PENDING_GRILLME", text)

    def test_numeric_and_product_boundaries_remain_closed(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "SPECIAL_T1_SELECTION_WEIGHTS = PENDING_SIMULATION",
            "SPECIAL_T1_PRODUCTION_INTERVAL = PENDING_SIMULATION",
            "PRODUCT_CODE = UNCHANGED",
            "SCENE_RESOURCE_DATA = UNCHANGED",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
