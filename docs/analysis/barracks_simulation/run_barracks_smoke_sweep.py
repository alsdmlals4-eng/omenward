#!/usr/bin/env python3
"""Run the deterministic 2,000-seed OMENWARD barracks screening model."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from smoke_analysis import aggregate_vector, general_support_sensitivity
from smoke_common import DECISION_ID, rounded, sha256, write_outputs
from smoke_simulator import SmokeSimulator


def run_smoke_sweep(root: Path, seed_count: int = 2000, output_dir: Path | None = None) -> tuple[Path, Path]:
    root = Path(root).resolve()
    analysis_dir = root / "docs/analysis/barracks_simulation"
    baseline_path = analysis_dir / "current_maprun_economy_pressure_baseline.v1.json"
    model_path = analysis_dir / "smoke_model_assumptions.v1.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    model = json.loads(model_path.read_text(encoding="utf-8"))
    if model["decision_id"] != DECISION_ID:
        raise ValueError("smoke model Decision ID mismatch")
    if baseline["run_gate"]["simulation_runnable"] != "TRUE_FOR_SMOKE_ONLY":
        raise ValueError("3/10 baseline does not authorize smoke execution")
    if seed_count <= 0:
        raise ValueError("seed_count must be positive")

    simulator = SmokeSimulator(baseline, model, seed_count)
    vectors_input = model["parameter_vectors"]
    baseline_vector = next(v for v in vectors_input if v["vector_id"] == "V00_BASELINE")
    general_cache: dict[tuple[str, str, str], dict[str, Any]] = {}
    for path in model["scenario_matrix"]["stage2_paths"]:
        for gold_scenario in model["scenario_matrix"]["gold_scenarios"]:
            for policy in model["scenario_matrix"]["spin_policies"]:
                general_cache[(path, gold_scenario, policy)] = simulator.simulate_batch_numpy(
                    baseline_vector, path, gold_scenario, policy, "general_only", support_label="MID"
                )
    vectors = [aggregate_vector(simulator, vector, general_cache) for vector in vectors_input]
    baseline_result = next(row for row in vectors if row["vector_id"] == "V00_BASELINE")
    sensitivity = general_support_sensitivity(simulator, baseline_vector)
    baseline_result["support_sensitivity"] = sensitivity
    threshold = float(model["thresholds"]["GENERAL_PATH_VALIDITY_RATE_MIN"])
    states = {label: value >= threshold for label, value in sensitivity.items()}
    delta = max(sensitivity.values()) - min(sensitivity.values())
    identifiability_fail = delta > float(model["gate_rules"]["support_sensitivity_delta_max"]) or len(set(states.values())) > 1
    failed = ["MODEL_IDENTIFIABILITY_FAIL"] if identifiability_fail else []
    failed.extend(name for name, passed in baseline_result["threshold_pass"].items() if not passed)
    result = {
        "schema_version": "1.0",
        "decision_id": DECISION_ID,
        "parent_decision_id": model["parent_decision_id"],
        "status": "SMOKE_COMPLETED_CONDITIONAL_FAIL" if failed else "SMOKE_PASS",
        "seed_count": seed_count,
        "common_random_numbers": True,
        "parameter_vector_count": len(vectors),
        "input_hashes": {"baseline_sha256": sha256(baseline_path), "model_sha256": sha256(model_path)},
        "model_boundaries": model["model_boundaries"],
        "parameter_vectors": vectors,
        "baseline_vector": baseline_result,
        "identifiability": {
            "status": "FAIL" if identifiability_fail else "PASS",
            "support_sensitivity_delta": rounded(delta),
            "general_validity_threshold_states": states,
            "reason": "NON_BARRACKS_SUPPORT_NUMERICS_NOT_CANONICAL" if identifiability_fail else "ROBUST_ACROSS_SUPPORT_ENVELOPES",
        },
        "failed_gates": failed,
        "selected_parameter_vector": None,
        "gate": {
            "smoke_sweep": "COMPLETED",
            "decision_sweep": "BLOCKED" if failed else "READY_FOR_USER_REVIEW",
            "confirmation_sweep": "BLOCKED",
            "product_implementation": "NOT_AUTHORIZED",
            "next_gate": "PLAYER_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION" if failed else "DECISION_SWEEP_USER_REVIEW",
        },
    }
    return write_outputs(output_dir or analysis_dir, result)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--seeds", type=int, default=2000)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    json_path, csv_path = run_smoke_sweep(args.root, args.seeds, args.output_dir)
    print(json_path)
    print(csv_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
