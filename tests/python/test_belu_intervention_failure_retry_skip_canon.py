from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-BELU-INTERVENTION-FAILURE-RETRY-SKIP-RULES-V1"
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BELU_INTERVENTION_FAILURE_RETRY_SKIP_RULES_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BELU_INTERVENTION_FAILURE_RETRY_SKIP_RULES_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-belu-intervention-failure-retry-skip-rules-design.md"


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class BeluInterventionFailureRetrySkipCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (AUTHORITY, REVIEW, SPEC):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_decision_and_checkpoint_are_explicit(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            DECISION_ID,
            "DECISION_STATUS = PARTIAL_APPROVAL_9_OF_10",
            "APPROVAL_CHECKPOINT = BELU_INTERVENTION_FAILURE_RETRY_SKIP_RULES",
        ):
            self.assertIn(marker, text)

    def test_belu_never_replaces_player_choice(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "BELU_AUTO_SELECT = FORBIDDEN",
            "BELU_AUTO_BUILD = FORBIDDEN",
            "BELU_AUTO_DEPLOY = FORBIDDEN",
            "BELU_HINT_DEFAULT = SHORT_CONTEXT_ONLY",
            "BELU_FIRST_FAILURE_HINT = ONE_CAUSE_PLUS_ONE_DIRECTION",
        ):
            self.assertIn(marker, text)

    def test_retry_restores_same_stage_start_state(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "FIRST_CLEAR_FAILURE_RETRY_POINT = SAME_STAGE_START_CHECKPOINT",
            "RETRY_RUN_SEED = PRESERVED",
            "RETRY_OMEN_FORECAST = PRESERVED",
            "RETRY_SPECIAL_T1_RESULTS = PRESERVED",
            "RETRY_PLAYER_CONFIRMED_CHOICES = PRESERVED",
        ):
            self.assertIn(marker, text)

    def test_failure_farming_is_forbidden(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "FAILED_ATTEMPT_REWARD_COMMIT = FORBIDDEN",
            "FAILED_ATTEMPT_GOLD_COMMIT = FORBIDDEN",
            "FAILED_ATTEMPT_REROLL_ADVANTAGE = FORBIDDEN",
            "RETRY_DUPLICATE_REWARD = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_skip_rules_distinguish_before_and_after_first_clear(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "PRE_FIRST_CLEAR_DIALOGUE_SHORTENING = ALLOWED",
            "PRE_FIRST_CLEAR_REQUIRED_ACTION_SKIP = FORBIDDEN",
            "POST_FIRST_CLEAR_FULL_ONBOARDING_SKIP = ALLOWED",
            "POST_FIRST_CLEAR_SKIP_REWARD_REGRANT = FORBIDDEN",
            "POST_FIRST_CLEAR_TUTORIAL_REPLAY = ALLOWED_FROM_SETTINGS",
        ):
            self.assertIn(marker, text)

    def test_retry_does_not_become_a_fake_run_rule(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "FIRST_CLEAR_RETRY_SAFETY_SCOPE = ONBOARDING_ONLY",
            "POST_FIRST_CLEAR_STANDARD_RUN_FAILURE_RULES = REQUIRED",
            "TUTORIAL_RETRY_EXCEPTION_MUST_BE_DISCLOSED = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_adversarial_review_covers_core_failure_modes(self) -> None:
        text = read(REVIEW)
        for marker in (
            "BELU_OVERCOACHING",
            "RETRY_FARMING",
            "SEED_REROLL_EXPLOIT",
            "MANDATORY_ACTION_SKIP",
            "FAKE_RULE_PARITY",
            "LEARNED_HELPLESSNESS",
        ):
            self.assertIn(marker, text)

    def test_product_and_validation_boundaries_remain_closed(self) -> None:
        text = read(AUTHORITY)
        for marker in (
            "PRODUCT_CODE = UNCHANGED",
            "SCENE_RESOURCE_DATA = UNCHANGED",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
            "EXACT_HINT_WORDING_AND_ESCALATION = PENDING_HUMAN_QA",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
