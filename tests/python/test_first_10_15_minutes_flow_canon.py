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
            "DECISION_STATUS = PARTIAL_APPROVAL_3_OF_10",
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
            "SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST",
            "STAGE_1 = PREBUILT_T1_TO_T2_AND_DEPLOYMENT_CAUSAL_CHAIN",
            "STAGE_2 = ROULETTE_CONTROL_AND_MULTI_FRONT",
            "STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC",
            "STAGE_4 = FIRST_DANGER_INTEGRATION",
            "STAGE_5 = FIRST_BOSS_MASTERY_CHECK",
            "MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE",
            "MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST",
        ):
            self.assertIn(marker, text)

    def test_prebuilt_t1_and_first_meaningful_choice_boundary(self) -> None:
        text = read(CANON)
        for marker in (
            "INITIAL_T1_BUILDINGS = PREBUILT",
            "T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS",
            "T1_BUILDING_CONSTRUCTION_TUTORIAL = FORBIDDEN",
            "LONG_T1_BUILDING_EXPLANATION = FORBIDDEN",
            "FIRST_MEANINGFUL_RULER_CHOICE = T2_UPGRADE_AND_IRREVERSIBLE_DEPLOYMENT",
            "T2_UPGRADE_PREVIEW = REQUIRED",
            "IRREVERSIBLE_DEPLOYMENT = REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_stage_one_teaches_the_revised_causal_chain(self) -> None:
        text = read(CANON)
        for marker in (
            "OMEN_FORECAST",
            "PREBUILT_T1_QUICK_READ",
            "T2_UPGRADE_PREVIEW_AND_CHOICE",
            "FIRST_ROULETTE",
            "TROOP_RESULT",
            "IRREVERSIBLE_DEPLOYMENT",
            "REAL_COMBAT",
            "CAUSAL_REVIEW",
            "FIRST_MERCHANT",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("FIRST_BUILD_CHOICE = REQUIRED", text)
        self.assertNotIn("BUILD_PREVIEW_AND_CHOICE", text)

    def test_unapproved_details_remain_pending(self) -> None:
        text = read(CANON)
        for marker in (
            "INITIAL_T1_INSTANCE_COUNT = PENDING_GRILLME",
            "FIRST_T2_UPGRADE_CANDIDATES = PENDING_GRILLME",
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
            self.assertIn("PARTIAL_APPROVAL_3_OF_10", text, str(path.relative_to(ROOT)))
            self.assertIn("INITIAL_T1_BUILDINGS", text, str(path.relative_to(ROOT)))
            self.assertIn("FIRST_MEANINGFUL_RULER_CHOICE", text, str(path.relative_to(ROOT)))

    def test_post_merge_operational_drift_is_closed(self) -> None:
        active = read(ACTIVE_CONTEXT)
        ledger = read(LEDGER)
        self.assertNotIn("current_status: PR_CANON_TARGET / NOT_IMPLEMENTED", active)
        self.assertIn("last_merged_planning_pr: 141", ledger)
        self.assertIn("last_merged_planning_commit: 6b23ca2bb627827651a42ba6db01829e44ee8a14", ledger)

    def test_lifecycle_blocks_old_tutorial_inputs(self) -> None:
        text = read(LIFECYCLE)
        for marker in (
            DECISION_ID,
            "LEGACY_SEPARATE_TUTORIAL",
            "LEGACY_STAGE1_FULL_SYSTEM_DUMP",
            "LEGACY_SCRIPTED_TUTORIAL_VICTORY",
            "LEGACY_T1_CONSTRUCTION_TUTORIAL",
            "LEGACY_LONG_T1_BUILDING_EXPLANATION",
            "IMPLEMENTATION_INPUT_FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_adversarial_review_preserves_product_boundary(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-492",
            "OMW-AUD-512",
            "TUTORIAL_MAIN_RULE_DRIFT",
            "MODAL_OVERLOAD",
            "ANSWER_FOLLOWING_ONBOARDING",
            "SCRIPTED_VICTORY_MASKING",
            "PREMATURE_SYSTEM_EXPOSURE",
            "STAGE_ONE_OVERLOAD",
            "T1_EXPLANATION_OVERLOAD",
            "T1_CONSTRUCTION_FALSE_PRIORITY",
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
