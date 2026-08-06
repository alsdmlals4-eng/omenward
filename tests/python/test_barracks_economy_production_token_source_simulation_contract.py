from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-BARRACKS-ECONOMY-PRODUCTION-TOKEN-SOURCE-SIMULATION-CONTRACT-V1"
CONTRACT = ROOT / "docs/design/PROPOSED_OMENWARD_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_CONTRACT_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-barracks-economy-production-token-source-simulation-contract-design.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-06-barracks-economy-production-token-source-simulation-contract.md"
ACTIVE = ROOT / "docs/ACTIVE_CONTEXT.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
LEDGER = ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md"
MAP = ROOT / "docs/DOCUMENTATION_MAP.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"


class BarracksEconomyProductionTokenSourceSimulationContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = CONTRACT.read_text(encoding="utf-8")
        cls.review = REVIEW.read_text(encoding="utf-8")
        cls.spec = SPEC.read_text(encoding="utf-8")
        cls.plan = PLAN.read_text(encoding="utf-8")
        cls.active = ACTIVE.read_text(encoding="utf-8")
        cls.pending = PENDING.read_text(encoding="utf-8")
        cls.ledger = LEDGER.read_text(encoding="utf-8")
        cls.map = MAP.read_text(encoding="utf-8")
        cls.lifecycle = LIFECYCLE.read_text(encoding="utf-8")

    def test_contract_is_proposed_not_approved_or_implemented(self) -> None:
        self.assertIn(f"decision_id: {DECISION_ID}", self.contract)
        self.assertIn("status: PROPOSED_SIMULATION_CONTRACT", self.contract)
        self.assertIn("approval: USER_REVIEW_PENDING", self.contract)
        self.assertIn("PRODUCT_CODE = UNCHANGED", self.contract)
        self.assertIn("SIMULATION_RESULTS = NOT_RUN", self.contract)
        self.assertNotIn("status: APPROVED", self.contract)

    def test_current_barracks_identity_contract_is_preserved(self) -> None:
        for marker in (
            "GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY",
            "GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY",
            "SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT",
            "SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT",
            "SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS",
            "SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN",
            "SPECIAL_T1_FREE_REROLL = FORBIDDEN",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.contract)

    def test_simulation_inputs_cover_all_tunable_economic_axes(self) -> None:
        for marker in (
            "GENERAL_BARRACKS_COST_INDEX",
            "SPECIAL_BARRACKS_COST_MULTIPLIER",
            "GENERAL_PRODUCTION_INTERVAL_INDEX",
            "SPECIAL_PRODUCTION_INTERVAL_MULTIPLIER",
            "GENERAL_TOKEN_SOURCE_WEIGHT_INDEX",
            "SPECIAL_TOKEN_SOURCE_WEIGHT_MULTIPLIER",
            "TOKEN_SOURCE_COUNT_PER_EVENT",
            "ROULETTE_DRAW_CADENCE",
            "UNIT_FUNCTIONAL_VALUE_INDEX",
            "ENEMY_PRESSURE_TIMELINE",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.contract)

    def test_scenario_matrix_covers_path_rng_and_pressure_risks(self) -> None:
        for marker in (
            "GENERAL_ONLY",
            "SPECIAL_ONLY",
            "GENERAL_AND_SPECIAL",
            "MULTI_SPECIAL",
            "SHIELD_PATH",
            "ARCHER_PATH",
            "NO_SPECIAL_PATH",
            "FIXED_EACH_OF_FIVE_SPECIAL_RESULTS",
            "MASS / ARMORED / FLYING / INFILTRATION / SIEGE",
            "LOW / STANDARD / HIGH_SURPLUS",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.contract)

    def test_kpis_have_direction_owner_and_proposed_thresholds(self) -> None:
        for marker in (
            "SPECIAL_OPTION_DOMINANCE_RATE <= 0.60",
            "GENERAL_PATH_VALIDITY_RATE >= 0.95",
            "EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE >= 0.85",
            "WORST_SPECIAL_REGRET_RATE <= 0.15",
            "SPECIAL_TOKEN_SHARE_10_MIN <= 0.35",
            "SPECIAL_TOKEN_SHARE_BURST_MAX <= 0.45",
            "MULTI_SPECIAL_DOMINANCE_RATE <= 0.55",
            "SECOND_SPECIAL_MARGINAL_VALUE_RATIO <= 0.80",
            "REROLL_EXPECTED_VALUE_GAIN = 0",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.contract)
        self.assertIn("THRESHOLDS = POC_HYPOTHESES_REQUIRING_USER_APPROVAL", self.contract)

    def test_contract_defines_sample_sizes_and_no_false_green(self) -> None:
        for marker in (
            "SMOKE_SEEDS = 2000",
            "DECISION_SEEDS = 10000",
            "CONFIRMATION_SEEDS = 50000",
            "WINDOWS_MINUTES = 5 / 10 / 15",
            "MISSING_REQUIRED_INPUT = BLOCK_SIMULATION",
            "NO_BALANCE_APPROVAL_FROM_STATIC_MARKER_TESTS",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.contract)

    def test_adversarial_review_requires_joint_tuning_and_stops_exploits(self) -> None:
        for marker in (
            "SPECIAL_T1_DOUBLE_VALUE_RISK",
            "TOKEN_POOL_MONOPOLY_RISK",
            "MULTI_SPECIAL_COMPOUNDING_RISK",
            "LOW_ROLL_DEAD_PATH_RISK",
            "FREE_REROLL_REINTRODUCTION = FORBIDDEN",
            "COST_INTERVAL_TOKEN_WEIGHT_MUST_BE_TUNED_JOINTLY",
            "SIMULATION_GREEN_WITHOUT_INPUT_PROVENANCE = FORBIDDEN",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.review)

    def test_router_documents_mark_proposal_and_remove_stale_no_token_authority(self) -> None:
        for text in (self.active, self.pending, self.ledger, self.map, self.lifecycle):
            self.assertIn(DECISION_ID, text)
        self.assertIn("PROPOSED / USER_REVIEW_PENDING", self.active)
        self.assertIn("SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT", self.ledger)
        self.assertNotIn("SPECIAL_T1_TOKEN_SOURCE = NONE", self.ledger)
        self.assertIn("[제안]", self.lifecycle)

    def test_spec_and_plan_keep_simulation_separate_from_product_implementation(self) -> None:
        self.assertIn("SIMULATION_ARTIFACT_ONLY", self.spec)
        self.assertIn("PRODUCT_IMPLEMENTATION = OUT_OF_SCOPE", self.spec)
        self.assertIn("tests/python/test_barracks_economy_production_token_source_simulation_contract.py", self.plan)
        self.assertIn("Do not modify GDScript, Scene, Resource, project.godot, or gameplay data", self.plan)


if __name__ == "__main__":
    unittest.main()
