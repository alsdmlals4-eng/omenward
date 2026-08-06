from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-BARRACKS-SIMULATION-INPUT-PROVENANCE-AND-ROULETTE-AXIS-CORRECTION-V1"

AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_SIMULATION_INPUT_PROVENANCE_MANIFEST_2026-08-06.md"
MANIFEST = ROOT / "docs/analysis/barracks_simulation/input_provenance_manifest.v1.json"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BARRACKS_SIMULATION_INPUT_PROVENANCE_REVIEW_2026-08-06.md"
CONTRACT = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_CONTRACT_2026-08-06.md"
ACTIVE = ROOT / "docs/ACTIVE_CONTEXT.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
LEDGER = ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md"
MAP = ROOT / "docs/DOCUMENTATION_MAP.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"


class BarracksSimulationInputProvenanceManifestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.authority = AUTHORITY.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.review = REVIEW.read_text(encoding="utf-8")
        cls.contract = CONTRACT.read_text(encoding="utf-8")
        cls.active = ACTIVE.read_text(encoding="utf-8")
        cls.pending = PENDING.read_text(encoding="utf-8")
        cls.ledger = LEDGER.read_text(encoding="utf-8")
        cls.map = MAP.read_text(encoding="utf-8")
        cls.lifecycle = LIFECYCLE.read_text(encoding="utf-8")

    def test_authority_is_approved_second_gate_only(self) -> None:
        self.assertIn(f"decision_id: {DECISION_ID}", self.authority)
        self.assertIn("status: APPROVED_INPUT_PROVENANCE_MANIFEST", self.authority)
        self.assertIn("approval_count: 2_OF_10", self.authority)
        self.assertIn("PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED", self.authority)
        self.assertIn("SIMULATION_RUNNABLE = FALSE", self.authority)

    def test_manifest_schema_and_source_snapshot_are_explicit(self) -> None:
        self.assertEqual(self.manifest["decision_id"], DECISION_ID)
        self.assertEqual(self.manifest["schema_version"], "1.0")
        self.assertEqual(self.manifest["approval_count"], "2_OF_10")
        self.assertEqual(self.manifest["source_snapshot"]["git_parent_head"], "90e058ac0b9dc31d484af66da122741cc8a483cf")
        self.assertEqual(self.manifest["source_snapshot"]["sheet_revision_id"], "386")
        self.assertGreaterEqual(len(self.manifest["sources"]), 8)
        for source in self.manifest["sources"]:
            for key in ("source_id", "location", "version", "classification", "authority_use"):
                self.assertIn(key, source)

    def test_physical_reel_axis_correction_supersedes_fractional_weight(self) -> None:
        for marker in (
            "TOKEN_SOURCE_PROBABILITY_AXIS = PHYSICAL_TOKEN_INSTANCES_PER_REEL",
            "TOKEN_SOURCE_BUILDING_CONTRIBUTION = 1_TOKEN_PER_REEL",
            "SPECIAL_TOKEN_SOURCE_WEIGHT_MULTIPLIER_0_35_TO_0_80 = SUPERSEDED",
            "SAME_SYMBOL_SOURCE_WEIGHT = REWARD_SOURCE_SELECTION_ONLY",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.authority)
        self.assertIn("SPECIAL_TOKEN_SOURCE_WEIGHT_MULTIPLIER = 0.35 / 0.50 / 0.65 / 0.80", self.contract)
        self.assertIn("[부분 대체됨]", self.lifecycle)
        self.assertIn("물리 릴 TokenInstance 축으로 대체", self.lifecycle)
        self.assertIn("SPECIAL_TOKEN_SOURCE_WEIGHT_MULTIPLIER_0_35_TO_0_80 = SUPERSEDED", self.ledger)

    def test_legacy_sources_are_never_current_v2_authority(self) -> None:
        classifications = {s["source_id"]: s["classification"] for s in self.manifest["sources"]}
        self.assertEqual(classifications["legacy_stage_economy_baseline"], "LEGACY_POC_CANDIDATE")
        self.assertEqual(classifications["legacy_special_corps_v5"], "PARTIALLY_SUPERSEDED_CANDIDATE")
        self.assertEqual(classifications["legacy_weighted_board_code"], "IMPLEMENTED_LEGACY_CONFLICT")
        self.assertIn("LEGACY_WEIGHTED_BOARD_CODE = NOT_V2_SIMULATION_AUTHORITY", self.review)

    def test_dimensionless_axes_remain_ready(self) -> None:
        inputs = {i["input_id"]: i for i in self.manifest["inputs"]}
        self.assertEqual(inputs["GENERAL_BARRACKS_COST_INDEX"]["status"], "READY_DIMENSIONLESS")
        self.assertEqual(inputs["SPECIAL_BARRACKS_COST_MULTIPLIER"]["status"], "READY_DIMENSIONLESS")
        self.assertEqual(inputs["GENERAL_PRODUCTION_INTERVAL_INDEX"]["status"], "READY_DIMENSIONLESS")
        self.assertEqual(inputs["SPECIAL_PRODUCTION_INTERVAL_MULTIPLIER"]["status"], "READY_DIMENSIONLESS")
        self.assertEqual(inputs["TOKEN_INSTANCES_PER_REEL_PER_SOURCE"]["value"], 1)

    def test_blocking_inputs_keep_all_sweeps_closed(self) -> None:
        inputs = {i["input_id"]: i for i in self.manifest["inputs"]}
        for input_id in (
            "GENERAL_PRODUCTION_INTERVAL_SECONDS",
            "ASSASSIN_PRODUCTION_INTERVAL_SECONDS",
            "CURRENT_MAPRUN_GOLD_TIMELINE",
            "ENEMY_THREAT_BUDGET_AND_TIMELINE",
            "MAINTENANCE_CLOCK_MATRIX",
        ):
            with self.subTest(input_id=input_id):
                self.assertEqual(inputs[input_id]["status"], "MISSING_BLOCKER")
        self.assertFalse(self.manifest["run_gate"]["simulation_runnable"])
        self.assertEqual(self.manifest["run_gate"]["smoke_sweep"], "BLOCKED")
        self.assertEqual(self.manifest["run_gate"]["decision_sweep"], "BLOCKED")
        self.assertEqual(self.manifest["run_gate"]["confirmation_sweep"], "BLOCKED")

    def test_draw_cadence_is_a_policy_scenario_not_fake_clock(self) -> None:
        inputs = {i["input_id"]: i for i in self.manifest["inputs"]}
        cadence = inputs["ROULETTE_DRAW_POLICY"]
        self.assertEqual(cadence["status"], "READY_SCENARIO_POLICY")
        self.assertEqual(cadence["candidates"], [
            "AGGRESSIVE_WHEN_AFFORDABLE",
            "RESERVE_ESSENTIAL_OBLIGATIONS",
            "MAINTENANCE_ONLY",
        ])
        self.assertIn("ROULETTE_DRAW_CADENCE = POLICY_SCENARIO_NOT_FIXED_CLOCK", self.authority)

    def test_router_documents_point_to_second_gate_and_next_blocker(self) -> None:
        for text in (self.active, self.pending, self.ledger, self.map, self.lifecycle):
            self.assertIn(DECISION_ID, text)
        self.assertIn("current_grill_me_count: 2_OF_10", self.active)
        self.assertIn("NEXT_GATE = CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE", self.active)
        self.assertIn("[승인]", self.lifecycle)

    def test_product_and_local_project_remain_unchanged(self) -> None:
        for text in (self.authority, self.review):
            self.assertIn("PRODUCT_CODE = UNCHANGED", text)
            self.assertIn("LOCAL_GODOT_PROJECT = UNCHANGED", text)
        self.assertEqual(self.manifest["scope"]["product_code"], "UNCHANGED")
        self.assertEqual(self.manifest["scope"]["local_godot_project"], "UNCHANGED")


if __name__ == "__main__":
    unittest.main()
