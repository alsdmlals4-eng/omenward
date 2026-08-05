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
            "DECISION_STATUS = PARTIAL_APPROVAL_5_OF_10",
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

    def test_checkpoint_five_placement_and_gold_safety_contract(self) -> None:
        text = read(CANON)
        for marker in (
            "T1_PLACEMENT_POLICY = CATEGORY_COMPATIBLE_SAFE_NODES",
            "T1_BUILD_ORDER = PLAYER_SELECTED",
            "FOUNDATION_SETUP_RELOCATION = FREE_BEFORE_CONFIRMATION",
            "FOUNDATION_SETUP_CONFIRMATION = REQUIRED",
            "POST_CONFIRMATION_PLACEMENT_RULES = STANDARD_RUN_RULES",
            "FREE_RELOCATION_AFTER_CONFIRMATION = FORBIDDEN",
            "STAGE_1_REQUIRED_COST_RESERVE = SUM_OF_UNBUILT_REQUIRED_T1_COSTS",
            "STAGE_1_NON_T1_SPENDING_BEFORE_REQUIRED_SET_COMPLETE = BLOCKED",
            "STAGE_1_LEFTOVER_GOLD_POLICY = NORMAL_WALLET_AFTER_REQUIRED_SET_COMPLETE",
            "FOUNDATION_GRANT_SURPLUS = FORBIDDEN",
            "T1_INVALID_PLACEMENT_TRANSACTION = ATOMIC_ROLLBACK_FULL_REFUND",
            "FIRST_ROULETTE_UNLOCK = AFTER_ALL_SIX_T1_AND_SETUP_CONFIRMATION",
            "EXACT_T1_COSTS = PENDING_SIMULATION",
        ):
            self.assertIn(marker, text)

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
            "FOUNDATION_SETUP_CONFIRMATION",
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
            "T1_EXACT_NODE_COORDINATES = PENDING_LEVEL_LAYOUT",
            "FIRST_T2_UPGRADE_CANDIDATE_IDENTITIES = PENDING_GRILLME",
            "STAGE_2_LEFTOVER_GOLD_POLICY = PENDING_GRILLME",
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
            self.assertIn("PARTIAL_APPROVAL_5_OF_10", text, str(path.relative_to(ROOT)))
            self.assertIn("STAGE_1_T1_BUILDINGS", text, str(path.relative_to(ROOT)))
            self.assertIn("T1_PLACEMENT_POLICY", text, str(path.relative_to(ROOT)))
            self.assertIn("STAGE_1_REQUIRED_COST_RESERVE", text, str(path.relative_to(ROOT)))
            self.assertIn("FIRST_MEANINGFUL_BUILD_CHOICE", text, str(path.relative_to(ROOT)))

    def test_platform_authority_survives_onboarding_updates(self) -> None:
        agents = read(ROOT / "AGENTS.md")
        for marker in (
            "OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1",
            "APPROVED_DUAL_PLATFORM",
            "COMMON_PLATFORM_GATE",
            "PC_RELEASE_GATE",
            "MOBILE_RELEASE_GATE",
            "RELEASE_BLOCKED_UNVERIFIED",
        ):
            self.assertIn(marker, agents)

    def test_post_merge_operational_drift_is_closed(self) -> None:
        active = read(ACTIVE_CONTEXT)
        ledger = read(LEDGER)
        self.assertNotIn("current_status: PR_CANON_TARGET / NOT_IMPLEMENTED", active)
        self.assertIn("last_merged_planning_pr: 141", ledger)
        self.assertIn("last_merged_planning_commit: 6b23ca2bb627827651a42ba6db01829e44ee8a14", ledger)

    def test_lifecycle_blocks_superseded_inputs(self) -> None:
        text = read(LIFECYCLE)
        for marker in (
            DECISION_ID,
            "LEGACY_SEPARATE_TUTORIAL",
            "LEGACY_STAGE1_FULL_SYSTEM_DUMP",
            "LEGACY_SCRIPTED_TUTORIAL_VICTORY",
            "SUPERSEDED_PREBUILT_T1_START",
            "LEGACY_LONG_T1_BUILDING_EXPLANATION",
            "UNSAFE_UNRESERVED_STAGE1_SPENDING",
            "FREE_RELOCATION_AFTER_CONFIRMATION",
            "IMPLEMENTATION_INPUT_FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_adversarial_review_preserves_product_boundary(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-492",
            "TUTORIAL_MAIN_RULE_DRIFT",
            "T1_BUILD_CHECKLIST_FATIGUE",
            "TUTORIAL_GOLD_ECONOMY_DRIFT",
            "FOUNDATION_SETUP_SOFTLOCK",
            "RESERVED_GOLD_ESCAPE",
            "FREE_RELOCATION_RULE_LEAK",
            "INVALID_PLACEMENT_PARTIAL_COMMIT",
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
