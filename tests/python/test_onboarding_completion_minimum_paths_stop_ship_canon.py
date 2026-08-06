from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_ONBOARDING_COMPLETION_MINIMUM_VALID_PATHS_AND_HUMAN_STOP_SHIP_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_ONBOARDING_COMPLETION_MINIMUM_VALID_PATHS_AND_HUMAN_STOP_SHIP_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-onboarding-completion-minimum-valid-paths-human-stop-ship-design.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class OnboardingCompletionCanonTest(unittest.TestCase):
    def test_authority_files_exist(self):
        self.assertTrue(AUTHORITY.exists())
        self.assertTrue(REVIEW.exists())
        self.assertTrue(SPEC.exists())

    def test_final_approval_and_parent_completion(self):
        text = read(AUTHORITY)
        self.assertIn("OMW-DEC-20260806-PLANNING-ONBOARDING-COMPLETION-MINIMUM-VALID-PATHS-HUMAN-STOP-SHIP-V1", text)
        self.assertIn("DECISION_STATUS = APPROVED_10_OF_10", text)
        self.assertIn("PARENT_FIRST_10_15_MINUTES_FLOW = PLANNING_COMPLETE", text)

    def test_completion_is_not_boss_only(self):
        text = read(AUTHORITY)
        self.assertIn("ONBOARDING_COMPLETE_TRIGGER = ALL_REQUIRED_MILESTONES_PLUS_FIRST_BOSS_CLEAR_PLUS_SUMMARY_ACK", text)
        self.assertIn("ONBOARDING_FIRST_CLEAR_FLAG_COMMIT = ATOMIC_AFTER_COMPLETION_TRIGGER", text)
        self.assertIn("EARLY_COMPLETION_FLAG_COMMIT = FORBIDDEN", text)
        self.assertIn("FIRST_CLEAR_REWARD_COMMIT = EXACTLY_ONCE", text)

    def test_required_milestones_cover_all_five_stages(self):
        text = read(AUTHORITY)
        for marker in (
            "STAGE1_REQUIRED_MILESTONE = FOUNDATION_ROULETTE_DEPLOYMENT_COMBAT_REVIEW_MERCHANT",
            "STAGE2_REQUIRED_MILESTONE = SHIELD_OR_ARCHER_T2_TOKEN_CHANGE_ROULETTE_CONTROL_DEPLOYMENT",
            "STAGE3_REQUIRED_MILESTONE = MANA_RESEARCH_AND_VALID_MANUAL_TACTIC_CAST",
            "STAGE4_REQUIRED_MILESTONE = DANGER_FORECAST_AND_PLAYER_MITIGATION_DECISION",
            "STAGE5_REQUIRED_MILESTONE = UNSCRIPTED_FIRST_BOSS_CLEAR",
        ):
            self.assertIn(marker, text)

    def test_minimum_player_paths_and_optional_special_barracks(self):
        text = read(AUTHORITY)
        self.assertIn("MINIMUM_VALID_PLAYER_PATH_COUNT = TWO", text)
        self.assertIn("MINIMUM_VALID_PLAYER_PATHS = SHIELD_WITHOUT_SPECIAL / ARCHER_WITHOUT_SPECIAL", text)
        self.assertIn("SPECIAL_BARRACKS_REQUIRED_FOR_ONBOARDING_COMPLETION = FALSE", text)
        self.assertIn("ONE_PATH_HARD_COUNTER = FORBIDDEN", text)

    def test_internal_qa_matrix_covers_random_special_results(self):
        text = read(AUTHORITY)
        self.assertIn("INTERNAL_QA_REQUIRED_SCENARIO_COUNT = TWELVE", text)
        self.assertIn("INTERNAL_QA_BASELINE_SCENARIOS = TWO_NO_SPECIAL_PATHS", text)
        self.assertIn("INTERNAL_QA_SPECIAL_MATRIX = TWO_T2_PATHS_X_FIVE_SPECIAL_RESULTS", text)
        self.assertIn("ALL_TWELVE_SCENARIOS_PROGRESSABLE_WITHOUT_DEBUG = REQUIRED", text)

    def test_human_validation_thresholds_are_explicit(self):
        text = read(AUTHORITY)
        for marker in (
            "FIRST_TIME_HUMAN_SAMPLE_MINIMUM = TWENTY",
            "PER_T2_PATH_SAMPLE_MINIMUM = TEN",
            "OVERALL_UNASSISTED_COMPLETION_RATE_MINIMUM = 0.85",
            "PER_PATH_UNASSISTED_COMPLETION_RATE_MINIMUM = 0.80",
            "PATH_COMPLETION_RATE_GAP_MAXIMUM = 0.20",
            "TARGET_MEDIAN_DURATION_MINUTES = 10_TO_15",
            "DURATION_P90_MAXIMUM_MINUTES = 20",
            "CORE_CAUSAL_UNDERSTANDING_RATE_MINIMUM = 0.80",
        ):
            self.assertIn(marker, text)

    def test_stop_ship_guards_cover_integrity_autonomy_and_parity(self):
        text = read(AUTHORITY) + read(REVIEW)
        for marker in (
            "STOP_SHIP_PROGRESSION_BLOCKER = TRUE",
            "STOP_SHIP_SAVE_OR_CHECKPOINT_CORRUPTION = TRUE",
            "STOP_SHIP_REWARD_DUPLICATION_OR_EARLY_FLAG = TRUE",
            "STOP_SHIP_RETRY_REROLL_OR_RESOURCE_GAIN = TRUE",
            "STOP_SHIP_REQUIRED_ACTION_BYPASS = TRUE",
            "STOP_SHIP_BELU_AUTO_RESOLUTION = TRUE",
            "STOP_SHIP_ANY_T2_OR_SPECIAL_RESULT_DEAD_PATH = TRUE",
            "STOP_SHIP_SCRIPTED_BOSS_VICTORY = TRUE",
            "STOP_SHIP_TUTORIAL_RETRY_LEAKS_TO_STANDARD_RUN = TRUE",
        ):
            self.assertIn(marker, text)

    def test_product_and_local_project_boundaries_remain_closed(self):
        text = read(AUTHORITY) + read(SPEC)
        self.assertIn("PRODUCT_CODE = UNCHANGED", text)
        self.assertIn("SCENE_RESOURCE_DATA = UNCHANGED", text)
        self.assertIn("LOCAL_GODOT_PROJECT = UNCHANGED", text)
        self.assertIn("RUNTIME = NOT_RUN", text)
        self.assertIn("HUMAN_QA = NOT_RUN", text)


if __name__ == "__main__":
    unittest.main()
