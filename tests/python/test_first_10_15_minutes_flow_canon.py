from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-05-first-10-15-minutes-flow-checkpoint-1.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-05-first-10-15-minutes-flow-checkpoint-1.md"
CANON = ROOT / "docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_FIRST_10_15_MINUTES_FLOW_FORMAT_REVIEW_2026-08-05.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
ACTIVE_CONTEXT = ROOT / "docs/ACTIVE_CONTEXT.md"
LEDGER = ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md"

CENTRAL_FILES = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "docs/PROJECT_CORE.md",
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/DOCUMENTATION_MAP.md",
    ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md",
    ROOT / "docs/DECISIONS_PENDING.md",
    ROOT / "docs/OMENWARD_ROADMAP.md",
    ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    ROOT / "docs/HANDOFF_CONTEXT.md",
    ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md",
    ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
)


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class FirstTenFifteenMinutesFlowCanonTests(unittest.TestCase):
    def test_checkpoint_authority_files_exist(self) -> None:
        for path in (SPEC, PLAN, CANON, REVIEW):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_approved_onboarding_format_is_explicit(self) -> None:
        text = read(CANON)
        for marker in (
            DECISION_ID,
            "DECISION_STATUS = PARTIAL_APPROVAL_4_OF_10",
            "ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE",
            "FIRST_SESSION = REAL_MAPRUN",
            "SEPARATE_TUTORIAL = FORBIDDEN",
            "FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN",
            "RULE_PARITY_WITH_MAIN_RUN = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_core_fun_is_taught_through_real_choices_not_scripted_outcomes(self) -> None:
        text = read(CANON)
        for marker in (
            "SCRIPTED_VICTORY = FORBIDDEN",
            "BELU_REPLACES_PLAYER_CHOICE = FORBIDDEN",
            "REAL_ECONOMY_RULES = REQUIRED",
            "REAL_COMBAT_RESULT_RULES = REQUIRED",
            "CORE_FUN_FIRST = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_approved_system_exposure_order_is_explicit(self) -> None:
        text = read(CANON)
        for marker in (
            "SYSTEM_EXPOSURE_ORDER = APPROVED_FOUNDATION_THEN_BRANCH_CHOICE",
            "STAGE_1 = BUILD_ONE_EACH_T1_AND_FIRST_DEPLOYMENT",
            "STAGE_2 = FIRST_T2_UPGRADE_CHOICE_AND_ROULETTE_CONTROL",
            "STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC",
            "STAGE_4 = FIRST_DANGER_INTEGRATION",
            "STAGE_5 = FIRST_BOSS_MASTERY_CHECK",
            "MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE",
            "MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST",
        ):
            self.assertIn(marker, text)

    def test_stage_one_builds_one_each_t1_with_real_gold(self) -> None:
        text = read(CANON)
        for marker in (
            "STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX",
            "STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET",
            "STAGE_1_BUILD_CURRENCY = REAL_GOLD",
            "T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS",
            "T1_BUILDING_PLACEMENT = PLAYER_EXECUTED",
            "T1_BUILDING_BRANCH_CHOICE = NONE",
            "LONG_T1_BUILDING_EXPLANATION = FORBIDDEN",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("INITIAL_T1_BUILDINGS = PREBUILT", text)

    def test_first_combat_and_build_choices_are_separated(self) -> None:
        text = read(CANON)
        for marker in (
            "FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT",
            "FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE",
            "STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE",
            "T2_UPGRADE_PREVIEW = REQUIRED",
            "IRREVERSIBLE_DEPLOYMENT = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_stage_one_and_two_teach_revised_causal_chain(self) -> None:
        text = read(CANON)
        for marker in (
            "OMEN_FORECAST",
            "STAGE_1_REAL_GOLD_GRANT",
            "BUILD_ONE_EACH_ALL_T1",
            "FIRST_ROULETTE",
            "TROOP_RESULT",
            "IRREVERSIBLE_DEPLOYMENT",
            "REAL_COMBAT",
            "CAUSAL_REVIEW",
            "FIRST_MERCHANT",
            "STAGE_2_T2_GOLD_GRANT",
            "T2_CANDIDATE_PREVIEW_AND_CHOICE",
        ):
            self.assertIn(marker, text)

    def test_mana_tower_construction_does_not_dump_research_early(self) -> None:
        text = read(CANON)
        for marker in (
            "MANA_TOWER_T1_INCLUDED_IN_STAGE_1_SET = REQUIRED",
            "MANA_TOWER_STAGE_1_EXPLANATION = BRIEF_RESOURCE_ROLE_ONLY",
            "TACTICAL_RESEARCH_EXPLANATION_BEFORE_STAGE_3 = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_unapproved_details_remain_pending(self) -> None:
        text = read(CANON)
        for marker in (
            "T1_PLACEMENT_LAYOUT = PENDING_GRILLME",
            "FIRST_T2_UPGRADE_CANDIDATES = PENDING_GRILLME",
            "STAGE_1_LEFTOVER_GOLD_POLICY = PENDING_GRILLME",
            "MINIMUM_VALID_PATHS = PENDING_GRILLME",
            "BELU_INTERVENTION_LEVEL = PENDING_GRILLME",
            "DANGER_EXACT_PRESSURE = PENDING_GRILLME",
            "BOSS_EXACT_PATTERN = PENDING_GRILLME",
            "FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME",
            "EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA",
        ):
            self.assertIn(marker, text)

    def test_central_authority_routes_in_progress_decision(self) -> None:
        for path in CENTRAL_FILES:
            text = read(path)
            self.assertIn(DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("7_OF_10_IN_PROGRESS", text, str(path.relative_to(ROOT)))
            self.assertIn("PARTIAL_APPROVAL_4_OF_10", text, str(path.relative_to(ROOT)))
            self.assertIn("STAGE_1_T1_BUILDINGS", text, str(path.relative_to(ROOT)))
            self.assertIn("FIRST_MEANINGFUL_BUILD_CHOICE", text, str(path.relative_to(ROOT)))

    def test_post_merge_operational_drift_is_closed(self) -> None:
        active = read(ACTIVE_CONTEXT)
        ledger = read(LEDGER)
        self.assertNotIn("current_status: PR_CANON_TARGET / NOT_IMPLEMENTED", active)
        self.assertIn("last_merged_planning_pr: 141", ledger)
        self.assertIn("last_merged_planning_commit: 6b23ca2bb627827651a42ba6db01829e44ee8a14", ledger)

    def test_lifecycle_blocks_superseded_prebuilt_and_long_explanation_inputs(self) -> None:
        text = read(LIFECYCLE)
        for marker in (
            DECISION_ID,
            "LEGACY_SEPARATE_TUTORIAL",
            "LEGACY_STAGE1_FULL_SYSTEM_DUMP",
            "LEGACY_SCRIPTED_TUTORIAL_VICTORY",
            "SUPERSEDED_PREBUILT_T1_START",
            "LEGACY_LONG_T1_BUILDING_EXPLANATION",
            "IMPLEMENTATION_INPUT_FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_adversarial_review_preserves_product_boundary(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-492",
            "OMW-AUD-516",
            "TUTORIAL_MAIN_RULE_DRIFT",
            "MODAL_OVERLOAD",
            "ANSWER_FOLLOWING_ONBOARDING",
            "SCRIPTED_VICTORY_MASKING",
            "PREMATURE_SYSTEM_EXPOSURE",
            "STAGE_ONE_OVERLOAD",
            "T1_BUILD_CHECKLIST_FATIGUE",
            "MANA_TOWER_EARLY_RESEARCH_DUMP",
            "TUTORIAL_GOLD_ECONOMY_DRIFT",
            "PRODUCT_CODE = UNCHANGED",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)

    def test_product_and_art_boundaries_remain_closed(self) -> None:
        text = read(CANON)
        for marker in (
            "PRODUCT_CODE = UNCHANGED",
            "DATA_MIGRATION = NOT_AUTHORIZED",
            "IMAGE_GENERATION = NOT_AUTHORIZED",
            "ANIMATION_HX = NOT_AUTHORIZED",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
