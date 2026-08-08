#!/usr/bin/env python3
"""Run the approved deterministic V00-only 10,000-seed barracks robustness sweep."""
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
from smoke_common import sha256, write_outputs
from smoke_simulator import SmokeSimulator

DECISION_ID = "OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1"
PARENT_DECISION_ID = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1"
SEED_COUNT = 10000
OUTPUT_STEM = "robustness_sweep_10000.v1"
ROBUSTNESS_ENVELOPE = "V00_BASELINE_COST_INTERVAL_ONLY"
ROBUSTNESS_SPECIAL_BARRACKS_COST_GOLD = 60.0
ROBUSTNESS_SPECIAL_INTERVAL_MULTIPLIER = 1.70
SOURCE_2K_JSON_SHA256 = "a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2"
SOURCE_2K_CSV_SHA256 = "3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560"
ROBUSTNESS_GATE_METRICS = (
    "SPECIAL_TOKEN_SHARE_10_MIN",
    "SPECIAL_TOKEN_SHARE_BURST_MAX",
    "REROLL_EXPECTED_VALUE_GAIN",
)


def output_paths(output_dir: Path) -> tuple[Path, Path]:
    output_dir = Path(output_dir)
    return output_dir / f"{OUTPUT_STEM}.json", output_dir / f"{OUTPUT_STEM}.csv"


def _load_inputs(root: Path) -> tuple[Path, Path, Path, Path, Path, dict[str, Any], dict[str, Any], dict[str, Any]]:
    analysis_dir = root / "docs/analysis/barracks_simulation"
    baseline_path = analysis_dir / "current_maprun_economy_pressure_baseline.v1.json"
    model_path = analysis_dir / "smoke_model_assumptions.v1.json"
    remediation_path = analysis_dir / "remediation_model.v1.json"
    source_json = analysis_dir / "smoke_sweep_2000.v2.json"
    source_csv = analysis_dir / "smoke_sweep_2000.v2.csv"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    model = json.loads(model_path.read_text(encoding="utf-8"))
    remediation = json.loads(remediation_path.read_text(encoding="utf-8"))
    return baseline_path, model_path, remediation_path, source_json, source_csv, baseline, model, remediation


def _validate_contract(
    baseline: dict[str, Any],
    model: dict[str, Any],
    remediation: dict[str, Any],
    source_json: Path,
    source_csv: Path,
) -> dict[str, Any]:
    if sha256(source_json) != SOURCE_2K_JSON_SHA256 or sha256(source_csv) != SOURCE_2K_CSV_SHA256:
        raise ValueError("canonical 2k evidence hash mismatch")
    if baseline["run_gate"]["simulation_runnable"] != "TRUE_FOR_SMOKE_ONLY":
        raise ValueError("approved analysis baseline does not permit simulator execution")
    if remediation["player_capability_proxy"]["combat_power_scalar"] != "FORBIDDEN":
        raise ValueError("combat-power scalar injection is forbidden")
    if float(remediation["player_capability_proxy"]["numeric_simulation_support_contribution"]) != 0.0:
        raise ValueError("numeric support contribution must remain zero")
    if int(remediation["multi_special_token_source"]["second_special_min_non_special_active_sources"]) != 3:
        raise ValueError("second-special physical TokenSource guard mismatch")

    vector = next((row for row in model["parameter_vectors"] if row["vector_id"] == "V00_BASELINE"), None)
    if vector is None:
        raise ValueError("V00 baseline vector missing")
    if float(vector["special_interval_multiplier"]) != ROBUSTNESS_SPECIAL_INTERVAL_MULTIPLIER:
        raise ValueError("V00 interval envelope mismatch")
    general_barracks = float(baseline["economy"]["required_stage1_t1_costs_gold"]["general_barracks"])
    derived_special_cost = general_barracks * float(vector["special_cost_multiplier"])
    baseline_special_cost = float(baseline["economy"]["special_barracks_t1_cost_gold"])
    if derived_special_cost != ROBUSTNESS_SPECIAL_BARRACKS_COST_GOLD or baseline_special_cost != ROBUSTNESS_SPECIAL_BARRACKS_COST_GOLD:
        raise ValueError("V00 cost envelope mismatch")

    intervals = baseline["production_intervals_active_combat_seconds"]
    general_max = max(float(intervals[name]) for name in ("basic_infantry", "shield", "archer"))
    scale = float(vector["special_interval_multiplier"]) / 1.70
    special_min = min(float(intervals[name]) * scale for name in ("assassin", "priest", "mage", "flying_unit", "giant"))
    if special_min <= general_max:
        raise ValueError("V00 interval violates longer-than-general canon gate")
    return vector


def run_robustness_10000(root: Path, output_dir: Path | None = None) -> tuple[Path, Path]:
    root = Path(root).resolve()
    (
        baseline_path,
        model_path,
        remediation_path,
        source_json,
        source_csv,
        baseline,
        model,
        remediation,
    ) = _load_inputs(root)
    vector = _validate_contract(baseline, model, remediation, source_json, source_csv)

    simulator = SmokeSimulator(baseline, model, remediation, SEED_COUNT)
    general_cache: dict[tuple[str, str, str], dict[str, Any]] = {}
    for path in model["scenario_matrix"]["stage2_paths"]:
        for gold_scenario in model["scenario_matrix"]["gold_scenarios"]:
            for policy in model["scenario_matrix"]["spin_policies"]:
                general_cache[(path, gold_scenario, policy)] = simulator.simulate_batch_numpy(
                    vector,
                    path,
                    gold_scenario,
                    policy,
                    "general_only",
                    support_label="REMEDIATION_ZERO",
                )

    baseline_result = aggregate_vector(simulator, vector, general_cache)
    raw_pass = baseline_result["raw_threshold_pass"]
    robustness_failed = [name for name in ROBUSTNESS_GATE_METRICS if not raw_pass[name]]
    status = "ROBUSTNESS_PASS" if not robustness_failed else "ROBUSTNESS_CONDITIONAL_FAIL"
    deferred_observations = int(baseline_result["deferred_second_special_token_source_observations"])

    result = {
        "schema_version": "1.0",
        "decision_id": DECISION_ID,
        "parent_decision_id": PARENT_DECISION_ID,
        "status": status,
        "seed_count": SEED_COUNT,
        "common_random_numbers": True,
        "parameter_vector_count": 1,
        "input_hashes": {
            "baseline_sha256": sha256(baseline_path),
            "historical_smoke_model_sha256": sha256(model_path),
            "remediation_model_sha256": sha256(remediation_path),
        },
        "source_2k_evidence": {
            "json": str(source_json.relative_to(root)).replace("\\", "/"),
            "json_sha256": SOURCE_2K_JSON_SHA256,
            "csv": str(source_csv.relative_to(root)).replace("\\", "/"),
            "csv_sha256": SOURCE_2K_CSV_SHA256,
            "seed_count": 2000,
            "preservation": "UNCHANGED_REQUIRED",
        },
        "robustness_envelope": {
            "name": ROBUSTNESS_ENVELOPE,
            "special_barracks_cost_gold": ROBUSTNESS_SPECIAL_BARRACKS_COST_GOLD,
            "special_interval_multiplier": ROBUSTNESS_SPECIAL_INTERVAL_MULTIPLIER,
            "special_functional_value_index": "DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS",
            "simulator_historical_functional_value_input": float(vector["special_functional_value_index"]),
            "simulator_historical_functional_value_policy": "NON_DECISION_LEGACY_INPUT_ONLY",
        },
        "robustness_gate_metrics": list(ROBUSTNESS_GATE_METRICS),
        "robustness_failed_gates": robustness_failed,
        "identifiability": {
            "status": "DIAGNOSTIC_NON_IDENTIFIABLE",
            "combat_power_scalar": "FORBIDDEN",
            "numeric_support_contribution": 0.0,
            "balance_gate": "EXCLUDED_UNTIL_PRODUCT_COMBAT_NUMERICS_EXIST",
            "second_special_marginal_value_ratio": "DIAGNOSTIC_NON_SELECTION_FOR_THIS_ROBUSTNESS_RUN",
        },
        "second_special_token_source_guard": {
            "minimum_non_special_active_sources": 3,
            "deferred_observations": deferred_observations,
            "status": "PRESERVED_AND_OBSERVED" if deferred_observations > 0 else "PRESERVED_NOT_TRIGGERED",
        },
        "parameter_vectors": [baseline_result],
        "baseline_vector": baseline_result,
        "failed_gates": robustness_failed,
        "selected_parameter_vector": None,
        "gate": {
            "robustness_10000": "COMPLETED",
            "parameter_selection_10000": "NOT_AUTHORIZED",
            "confirmation_sweep_50000": "BLOCKED",
            "functional_value_selection": "BLOCKED_UNTIL_PRODUCT_COMBAT_NUMERICS",
            "final_parameter_vector": "NOT_SELECTED",
            "final_product_numerics": "NOT_APPROVED",
            "product_implementation": "NOT_AUTHORIZED",
            "godot_authoring": "NOT_AUTHORIZED",
        },
    }
    destination = Path(output_dir).resolve() if output_dir else root / "docs/analysis/barracks_simulation"
    json_path, csv_path = output_paths(destination)
    if json_path == source_json or csv_path == source_csv:
        raise ValueError("10k output path aliases canonical 2k evidence")
    return write_outputs(destination, result, stem=OUTPUT_STEM)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    json_path, csv_path = run_robustness_10000(args.root, args.output_dir)
    result = json.loads(json_path.read_text(encoding="utf-8"))
    print(json_path)
    print(csv_path)
    print(f"status={result['status']} failed_gates={result['failed_gates']}")
    return 0 if result["status"] == "ROBUSTNESS_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
