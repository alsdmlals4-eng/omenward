from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = ROOT / "docs/analysis/barracks_simulation"
RUNNER = ANALYSIS / "run_barracks_remediation_smoke.py"
SIMULATOR = ANALYSIS / "smoke_simulator.py"
DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1"


def load_module(name: str, path: Path):
    if str(ANALYSIS) not in sys.path:
        sys.path.insert(0, str(ANALYSIS))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BarracksRemediationSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.runner = load_module("barracks_remediation_runner", RUNNER)
        cls.simulator = load_module("barracks_remediation_simulator", SIMULATOR)

    def test_physical_guard_keeps_second_special_deferred_until_three_non_special_sources(self) -> None:
        buildings = np.array([[True, True], [True, True], [True, False]], dtype=bool)
        non_special = np.array([2, 3, 3])
        token_active, deferred = self.simulator.enabled_special_token_sources(non_special, buildings, 3)
        self.assertEqual(token_active.tolist(), [[True, False], [True, True], [True, False]])
        self.assertEqual(deferred.tolist(), [True, False, False])
        active_share = token_active[1].sum() / (non_special[1] + token_active[1].sum())
        self.assertAlmostEqual(active_share, 0.40)

    def test_small_seed_rerun_is_deterministic_and_clears_original_two_gate_failures(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_json, first_csv = self.runner.run_remediation_smoke(ROOT, seed_count=32, output_dir=Path(first))
            second_json, second_csv = self.runner.run_remediation_smoke(ROOT, seed_count=32, output_dir=Path(second))
            self.assertEqual(first_json.read_bytes(), second_json.read_bytes())
            self.assertEqual(first_csv.read_bytes(), second_csv.read_bytes())
            result = json.loads(first_json.read_text(encoding="utf-8"))
        self.assertEqual(result["decision_id"], DECISION)
        self.assertEqual(result["identifiability"]["status"], "DIAGNOSTIC_NON_IDENTIFIABLE")
        self.assertNotIn("MODEL_IDENTIFIABILITY_FAIL", result["failed_gates"])
        self.assertLessEqual(result["baseline_vector"]["primary_kpis"]["SPECIAL_TOKEN_SHARE_BURST_MAX"], 0.45)
        self.assertNotIn("SPECIAL_TOKEN_SHARE_BURST_MAX", result["failed_gates"])
        self.assertEqual(result["gate"]["product_implementation"], "NOT_AUTHORIZED")


if __name__ == "__main__":
    unittest.main()
