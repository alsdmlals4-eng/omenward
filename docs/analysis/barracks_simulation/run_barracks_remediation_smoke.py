#!/usr/bin/env python3
"""Run the deterministic 2,000-seed barracks remediation smoke sweep."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from smoke_analysis import aggregate_vector
from smoke_common import rounded, sha256, write_outputs
from smoke_simulator import SmokeSimulator

DECISION_ID = "OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1"
PARENT_DECISION_ID = "OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1"


def run_remediation_smoke(root: Path, seed_count: int = 2000, output_dir: Path | None = None) -> tuple[Path, Path]:
    root = Path(root).resolve()
    analysis_dir = root / "docs/analysis/barracks_simulation"
    baseline_path = analysis_dir / "current_maprun_economy_pressure_baseline.v1.json"
    model_path = analysis_dir / "smoke_model_assumptions.v1.json"
    remediation_path = analysis_dir / "remediation_model.v1.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    model = json.loads(model_path.read_text(encoding="utf-8"))
    remediation = json.loads(remediation_path.read_text(encoding="utf-8"))

    if remediation["decision_id"] != DECISION_ID:
        raise ValueError("remediation Decision ID mismatch")
    if remediation["parent_decision_id"] != PARENT_DECISION_ID:
        raise ValueError("remediation parent Decision mismatch")
    if baseline["run_gate"]["simulation_runnable"] != "TRUE_FOR_SMOKE_ONLY":
        raise ValueError("3/10 baseline does not authorize smoke execution")
    if remediation["player_capability_proxy"]["combat_power_scalar"] != "FORBIDDEN":
        raise ValueError("combat-power scalar injection is forbidden")
    if float(remediation["player_capability_proxy"]["numeric_simulation_support_contribution"]) != 0.0:
        raise ValueError("numeric support contribution must remain zero for remediation smoke")
    if seed_count <= 0:
        raise ValueError("seed_count must be positive")

    simulator = SmokeSimulator(baseline, model, remediation, seed_count)
    vectors_input = model["parameter_vectors"]
    baseline_vector = next(v for v in vectors_input if v["vector_id"] == "V00_BASELINE")
    general_cache: dict[tuple[str, str, str], dict[str, Any]] = {}
    for path in model["scenario_matrix"]["stage2_paths"]:
        for gold_scenario in model["scenario_matrix"]["gold_scenarios"]:
            for policy in model["scenario_matrix"]["spin_policies"]:
                general_cache[(path, gold_scenario, policy)] = simulator.simulate_batch_numpy(
                    baseline_vector,
                    path,
                    gold_scenario,
                    policy,
                    "general_only",
                    support_label="REMEDIATION_ZERO",
                )

    vectors = [aggregate_vector(simulator, vector, general_cache) for vector in vectors_input]
    baseline_result = next(row for row in vectors if row["vector_id"] == "V00_BASELINE")
    failed = list(baseline_result["decision_failed_thresholds"])
    token_cap = float(remediation["multi_special_token_source"]["max_approved_burst_share"])
    observed_burst = float(baseline_result["primary_kpis"]["SPECIAL_TOKEN_SHARE_BURST_MAX"])
    if observed_burst > token_cap and "SPECIAL_TOKEN_SHARE_BURST_MAX" not in failed:
        failed.append("SPECIAL_TOKEN_SHARE_BURST_MAX")

    status = "SMOKE_RERUN_PASS" if not failed else "SMOKE_RERUN_CONDITIONAL_FAIL"
    result = {
        "schema_version": "2.0",
        "decision_id": DECISION_ID,
        "parent_decision_id": PARENT_DECISION_ID,
        "status": status,
        "seed_count": seed_count,
        "common_random_numbers": True,
        "parameter_vector_count": len(vectors),
        "input_hashes": {
            "baseline_sha256": sha256(baseline_path),
            "historical_smoke_model_sha256": sha256(model_path),
            "remediation_model_sha256": sha256(remediation_path),
        },
        "capability_proxy": remediation["player_capability_proxy"],
        "identifiability": {
            "status": "DIAGNOSTIC_NON_IDENTIFIABLE",
            "combat_power_scalar": "FORBIDDEN",
            "numeric_support_contribution": 0.0,
            "balance_gate": "EXCLUDED_UNTIL_PRODUCT_COMBAT_NUMERICS_EXIST",
        },
        "token_source_remediation": {
            **remediation["multi_special_token_source"],
            "observed_baseline_special_token_share_burst_max": rounded(observed_burst),
            "observed_baseline_burst_pass": observed_burst <= token_cap,
        },
        "parameter_vectors": vectors,
        "baseline_vector": baseline_result,
        "failed_gates": failed,
        "selected_parameter_vector": None,
        "gate": {
            "smoke_rerun": "COMPLETED",
            "decision_sweep_10000": "READY_FOR_USER_REVIEW" if not failed else "BLOCKED",
            "confirmation_sweep_50000": "BLOCKED",
            "product_implementation": "NOT_AUTHORIZED",
            "godot_authoring": "NOT_AUTHORIZED",
            "next_gate": "BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW" if not failed else "REMEDIATION_REVIEW",
        },
    }
    return write_outputs(output_dir or analysis_dir, result, stem="smoke_sweep_2000.v2")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--seeds", type=int, default=2000)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    json_path, csv_path = run_remediation_smoke(args.root, args.seeds, args.output_dir)
    print(json_path)
    print(csv_path)
    result = json.loads(json_path.read_text(encoding="utf-8"))
    print(f"status={result['status']} failed_gates={result['failed_gates']}")
    return 0 if result["status"] == "SMOKE_RERUN_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
