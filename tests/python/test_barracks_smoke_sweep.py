from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1"
BASELINE = ROOT / "docs/analysis/barracks_simulation/current_maprun_economy_pressure_baseline.v1.json"
MODEL = ROOT / "docs/analysis/barracks_simulation/smoke_model_assumptions.v1.json"
RUNNER = ROOT / "docs/analysis/barracks_simulation/run_barracks_smoke_sweep.py"
RESULT_JSON = ROOT / "docs/analysis/barracks_simulation/smoke_sweep_2000.v1.json"
RESULT_CSV = ROOT / "docs/analysis/barracks_simulation/smoke_sweep_2000.v1.csv"
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_SMOKE_SWEEP_RESULTS_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BARRACKS_SMOKE_SWEEP_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-barracks-smoke-sweep-design.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-06-barracks-smoke-sweep.md"
ROUTERS = [
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    ROOT / "docs/DECISIONS_PENDING.md",
    ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md",
    ROOT / "docs/DOCUMENTATION_MAP.md",
    ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class BarracksSmokeSweepTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        cls.model = json.loads(MODEL.read_text(encoding="utf-8"))
        cls.result = json.loads(RESULT_JSON.read_text(encoding="utf-8"))
        cls.authority = AUTHORITY.read_text(encoding="utf-8")
        cls.review = REVIEW.read_text(encoding="utf-8")

    def test_inputs_and_output_are_exactly_scoped(self) -> None:
        self.assertEqual(self.model["decision_id"], DECISION_ID)
        self.assertEqual(self.model["seed_count"], 2000)
        self.assertEqual(len(self.model["parameter_vectors"]), 9)
        self.assertEqual(self.result["decision_id"], DECISION_ID)
        self.assertEqual(self.result["seed_count"], 2000)
        self.assertEqual(self.result["parameter_vector_count"], 9)
        self.assertEqual(self.result["input_hashes"]["baseline_sha256"], sha256(BASELINE))
        self.assertEqual(self.result["input_hashes"]["model_sha256"], sha256(MODEL))

    def test_result_is_conditional_fail_not_balance_approval(self) -> None:
        self.assertEqual(self.result["status"], "SMOKE_COMPLETED_CONDITIONAL_FAIL")
        self.assertEqual(self.result["gate"]["decision_sweep"], "BLOCKED")
        self.assertEqual(self.result["gate"]["product_implementation"], "NOT_AUTHORIZED")
        self.assertIn("MODEL_IDENTIFIABILITY_FAIL", self.result["failed_gates"])
        self.assertIn("SPECIAL_TOKEN_SHARE_BURST_MAX", self.result["failed_gates"])
        self.assertIsNone(self.result["selected_parameter_vector"])

    def test_baseline_reports_all_primary_kpis_and_thresholds(self) -> None:
        baseline = self.result["baseline_vector"]
        expected = {
            "SPECIAL_OPTION_DOMINANCE_RATE",
            "GENERAL_PATH_VALIDITY_RATE",
            "EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE",
            "WORST_SPECIAL_REGRET_RATE",
            "SPECIAL_TOKEN_SHARE_10_MIN",
            "SPECIAL_TOKEN_SHARE_BURST_MAX",
            "MULTI_SPECIAL_DOMINANCE_RATE",
            "SECOND_SPECIAL_MARGINAL_VALUE_RATIO",
            "REROLL_EXPECTED_VALUE_GAIN",
        }
        self.assertEqual(set(baseline["primary_kpis"]), expected)
        self.assertEqual(set(baseline["threshold_pass"]), expected)
        self.assertFalse(baseline["threshold_pass"]["GENERAL_PATH_VALIDITY_RATE"])
        self.assertFalse(baseline["threshold_pass"]["SPECIAL_TOKEN_SHARE_BURST_MAX"])
        self.assertLessEqual(baseline["primary_kpis"]["SPECIAL_TOKEN_SHARE_10_MIN"], 0.35)
        self.assertGreater(baseline["primary_kpis"]["SPECIAL_TOKEN_SHARE_BURST_MAX"], 0.45)

    def test_support_sensitivity_proves_identifiability_failure(self) -> None:
        sensitivity = self.result["baseline_vector"]["support_sensitivity"]
        self.assertLess(sensitivity["LOW"], 0.95)
        self.assertLess(sensitivity["MID"], 0.95)
        self.assertGreaterEqual(sensitivity["HIGH"], 0.95)
        self.assertGreater(sensitivity["HIGH"] - sensitivity["LOW"], 0.20)
        self.assertEqual(self.result["identifiability"]["status"], "FAIL")

    def test_model_limitations_are_not_hidden(self) -> None:
        omissions = set(self.model["model_boundaries"]["not_modeled"])
        self.assertIn("LUCKY_AND_MOVE_OPTIMIZATION", omissions)
        self.assertIn("CASUALTY_AND_DEATH", omissions)
        self.assertIn("IRREVERSIBLE_LANE_ASSIGNMENT", omissions)
        self.assertEqual(self.model["model_boundaries"]["fifteen_minute_window"], "CENSORED_AT_STAGE5_END_830_SECONDS")
        for marker in (
            "PROXY_MONTE_CARLO_WITH_IDENTIFIABILITY_ENVELOPE",
            "SMOKE_PASS_ESCALATION_WITHOUT_REVIEW = FORBIDDEN",
            "PRODUCT_CODE = UNCHANGED",
        ):
            self.assertIn(marker, self.authority + self.review + SPEC.read_text(encoding="utf-8"))

    def test_csv_matches_json_vector_count(self) -> None:
        with RESULT_CSV.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), self.result["parameter_vector_count"])
        self.assertEqual({row["vector_id"] for row in rows}, {row["vector_id"] for row in self.result["parameter_vectors"]})

    def test_small_seed_rerun_is_deterministic(self) -> None:
        spec = importlib.util.spec_from_file_location("barracks_smoke_runner", RUNNER)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_json, first_csv = module.run_smoke_sweep(ROOT, seed_count=32, output_dir=Path(first))
            second_json, second_csv = module.run_smoke_sweep(ROOT, seed_count=32, output_dir=Path(second))
            self.assertEqual(first_json.read_bytes(), second_json.read_bytes())
            self.assertEqual(first_csv.read_bytes(), second_csv.read_bytes())

    def test_authority_review_and_routers_use_fourth_gate(self) -> None:
        self.assertIn(f"decision_id: {DECISION_ID}", self.authority)
        self.assertIn("approval_count: 4_OF_10", self.authority)
        self.assertIn("SMOKE_COMPLETED_CONDITIONAL_FAIL", self.authority)
        self.assertIn("MODEL_IDENTIFIABILITY_FAIL", self.review)
        self.assertIn("SPECIAL_TOKEN_SHARE_BURST_MAX", self.review)
        for path in ROUTERS:
            text = path.read_text(encoding="utf-8")
            self.assertIn(DECISION_ID, text, path.as_posix())
        self.assertIn("NEXT_GATE = PLAYER_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION", ROUTERS[0].read_text(encoding="utf-8"))

    def test_plan_and_product_boundary_are_explicit(self) -> None:
        plan = PLAN.read_text(encoding="utf-8")
        self.assertIn("tests/python/test_barracks_smoke_sweep.py", plan)
        self.assertIn("Do not modify GDScript, Scene, Resource, project.godot, or gameplay data", plan)
        for text in (self.authority, self.review):
            self.assertIn("PRODUCT_CODE = UNCHANGED", text)
            self.assertIn("LOCAL_GODOT_PROJECT = UNCHANGED", text)


if __name__ == "__main__":
    unittest.main()
