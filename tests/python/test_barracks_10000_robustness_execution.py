from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

from tools.git_canonical_evidence import git_blob_sha256

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = ROOT / "docs" / "analysis" / "barracks_simulation"
RUNNER = ANALYSIS / "run_barracks_robustness_10000.py"
RESULT_JSON = ANALYSIS / "robustness_sweep_10000.v1.json"
RESULT_CSV = ANALYSIS / "robustness_sweep_10000.v1.csv"
SOURCE_JSON = ANALYSIS / "smoke_sweep_2000.v2.json"
SOURCE_CSV = ANALYSIS / "smoke_sweep_2000.v2.csv"

DECISION_ID = "OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1"
PARENT_DECISION_ID = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1"
SOURCE_JSON_SHA = "a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2"
SOURCE_CSV_SHA = "3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560"
RESULT_JSON_SHA = "1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3"
RESULT_CSV_SHA = "e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b"


def file_sha256(path: Path) -> str:
    return git_blob_sha256(ROOT, path)


def load_runner():
    if not RUNNER.is_file():
        raise AssertionError(f"missing dedicated 10k runner: {RUNNER.relative_to(ROOT)}")
    spec = importlib.util.spec_from_file_location("barracks_robustness_10000", RUNNER)
    if spec is None or spec.loader is None:
        raise AssertionError("dedicated 10k runner import unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Barracks10000RobustnessExecutionTest(unittest.TestCase):
    def test_source_2k_evidence_hashes_are_unchanged(self) -> None:
        self.assertEqual(file_sha256(SOURCE_JSON), SOURCE_JSON_SHA)
        self.assertEqual(file_sha256(SOURCE_CSV), SOURCE_CSV_SHA)

    def test_dedicated_runner_has_fixed_unique_execution_identity(self) -> None:
        runner = load_runner()
        self.assertEqual(runner.DECISION_ID, DECISION_ID)
        self.assertEqual(runner.PARENT_DECISION_ID, PARENT_DECISION_ID)
        self.assertEqual(runner.SEED_COUNT, 10000)
        self.assertEqual(runner.OUTPUT_STEM, "robustness_sweep_10000.v1")
        self.assertEqual(runner.ROBUSTNESS_ENVELOPE, "V00_BASELINE_COST_INTERVAL_ONLY")
        self.assertEqual(float(runner.ROBUSTNESS_SPECIAL_BARRACKS_COST_GOLD), 60.0)
        self.assertEqual(float(runner.ROBUSTNESS_SPECIAL_INTERVAL_MULTIPLIER), 1.70)

    def test_dedicated_output_identity_cannot_alias_canonical_2k(self) -> None:
        runner = load_runner()
        json_path, csv_path = runner.output_paths(ANALYSIS)
        self.assertEqual(json_path, RESULT_JSON)
        self.assertEqual(csv_path, RESULT_CSV)
        self.assertNotEqual(json_path, SOURCE_JSON)
        self.assertNotEqual(csv_path, SOURCE_CSV)

    def test_committed_10k_result_hashes_and_metrics_are_exact(self) -> None:
        self.assertEqual(file_sha256(RESULT_JSON), RESULT_JSON_SHA)
        self.assertEqual(file_sha256(RESULT_CSV), RESULT_CSV_SHA)
        result = json.loads(RESULT_JSON.read_text(encoding="utf-8"))
        self.assertEqual(result["decision_id"], DECISION_ID)
        self.assertEqual(result["parent_decision_id"], PARENT_DECISION_ID)
        self.assertEqual(result["status"], "ROBUSTNESS_PASS")
        self.assertEqual(result["failed_gates"], [])
        self.assertEqual(result["seed_count"], 10000)
        self.assertTrue(result["common_random_numbers"])
        self.assertEqual(result["parameter_vector_count"], 1)
        self.assertEqual(result["baseline_vector"]["vector_id"], "V00_BASELINE")
        self.assertAlmostEqual(result["baseline_vector"]["primary_kpis"]["SPECIAL_TOKEN_SHARE_10_MIN"], 0.296265)
        self.assertAlmostEqual(result["baseline_vector"]["primary_kpis"]["SPECIAL_TOKEN_SHARE_BURST_MAX"], 0.333333)
        self.assertEqual(result["second_special_token_source_guard"]["deferred_observations"], 82181)
        self.assertEqual(result["robustness_envelope"]["name"], "V00_BASELINE_COST_INTERVAL_ONLY")
        self.assertEqual(float(result["robustness_envelope"]["special_barracks_cost_gold"]), 60.0)
        self.assertEqual(float(result["robustness_envelope"]["special_interval_multiplier"]), 1.70)
        self.assertEqual(result["robustness_envelope"]["special_functional_value_index"], "DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS")
        self.assertIsNone(result["selected_parameter_vector"])
        self.assertEqual(result["gate"]["parameter_selection_10000"], "NOT_AUTHORIZED")
        self.assertEqual(result["gate"]["confirmation_sweep_50000"], "BLOCKED")
        self.assertEqual(result["gate"]["product_implementation"], "NOT_AUTHORIZED")

    def test_combat_diagnostics_remain_non_gate_and_inputs_are_bound(self) -> None:
        result = json.loads(RESULT_JSON.read_text(encoding="utf-8"))
        diagnostic = set(result["baseline_vector"]["diagnostic_only_thresholds"])
        decision_failed = set(result["baseline_vector"]["decision_failed_thresholds"])
        self.assertTrue(diagnostic)
        self.assertTrue(diagnostic.isdisjoint(decision_failed))
        self.assertEqual(result["baseline_vector"]["primary_kpis"]["GENERAL_PATH_VALIDITY_RATE"], 0.0)
        self.assertEqual(result["baseline_vector"]["primary_kpis"]["WORST_SPECIAL_REGRET_RATE"], 1.0)
        self.assertEqual(result["identifiability"]["status"], "DIAGNOSTIC_NON_IDENTIFIABLE")
        self.assertEqual(result["identifiability"]["balance_gate"], "EXCLUDED_UNTIL_PRODUCT_COMBAT_NUMERICS_EXIST")
        self.assertEqual(result["source_2k_evidence"]["json_sha256"], SOURCE_JSON_SHA)
        self.assertEqual(result["source_2k_evidence"]["csv_sha256"], SOURCE_CSV_SHA)
        for key in ("baseline_sha256", "historical_smoke_model_sha256", "remediation_model_sha256"):
            self.assertRegex(result["input_hashes"][key], r"^[0-9a-f]{64}$")


if __name__ == "__main__":
    unittest.main()
