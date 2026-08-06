"""KPI aggregation and support-envelope identifiability checks."""
from __future__ import annotations

from typing import Any

import numpy as np

from smoke_common import SPECIAL_TYPES, rounded, threshold_pass


def aggregate_vector(simulator, vector: dict[str, Any], general_mid_cache: dict[tuple[str, str, str], dict[str, Any]]) -> dict[str, Any]:
    if np is None:
        raise RuntimeError("NumPy is required for accelerated smoke execution")
    special_dominance = 0
    multi_dominance = 0
    comparison_count = 0
    general_valid = 0
    token_share_sum = 0.0
    token_burst_max = 0.0
    ratio_chunks: list[Any] = []
    dominance = simulator.model["dominance_rules"]

    for path in simulator.model["scenario_matrix"]["stage2_paths"]:
        for gold_scenario in simulator.gold_scenarios:
            for policy in simulator.model["scenario_matrix"]["spin_policies"]:
                key = (path, gold_scenario, policy)
                general = general_mid_cache[key]
                special = simulator.simulate_batch_numpy(vector, path, gold_scenario, policy, "special_only")
                general_special = simulator.simulate_batch_numpy(vector, path, gold_scenario, policy, "general_and_special")
                multi = simulator.simulate_batch_numpy(vector, path, gold_scenario, policy, "multi_special")
                general_valid += int(general["valid"].sum())
                comparison_count += simulator.seed_count

                special_dom = special["valid"] & (
                    (~general["valid"])
                    | (
                        (special["mean_margin"] - general["mean_margin"] >= dominance["mean_margin_advantage"])
                        & (special["unit_equivalent_10_min"] >= dominance["unit_equivalent_advantage"] * general["unit_equivalent_10_min"])
                    )
                )
                special_dominance += int(special_dom.sum())

                best_valid = general["valid"] | special["valid"] | general_special["valid"]
                best_margin = np.maximum.reduce([general["mean_margin"], special["mean_margin"], general_special["mean_margin"]])
                best_equivalent = np.maximum.reduce([
                    general["unit_equivalent_10_min"],
                    special["unit_equivalent_10_min"],
                    general_special["unit_equivalent_10_min"],
                ])
                multi_dom = multi["valid"] & (
                    (~best_valid)
                    | (
                        (multi["mean_margin"] - best_margin >= dominance["mean_margin_advantage"])
                        & (multi["unit_equivalent_10_min"] >= dominance["unit_equivalent_advantage"] * best_equivalent)
                    )
                )
                multi_dominance += int(multi_dom.sum())

                first_gain = special["unit_equivalent_10_min"] - general["unit_equivalent_10_min"]
                second_gain = multi["unit_equivalent_10_min"] - special["unit_equivalent_10_min"]
                positive = first_gain > 1e-9
                if positive.any():
                    ratio_chunks.append(second_gain[positive] / first_gain[positive])
                token_share_sum += float(special["token_share_10_min"].sum())
                token_burst_max = max(token_burst_max, float(multi["token_share_burst_max"].max()))

    outcome_valid_counts = {name: 0 for name in SPECIAL_TYPES}
    outcome_total = 0
    regret_count = 0
    for path in simulator.model["scenario_matrix"]["stage2_paths"]:
        scores = []
        for special_name in SPECIAL_TYPES:
            result = simulator.simulate_batch_numpy(
                vector,
                path,
                "standard",
                "reserve",
                "special_only",
                fixed_special=special_name,
            )
            outcome_valid_counts[special_name] += int(result["valid"].sum())
            scores.append(result["mean_margin"] + 0.02 * result["unit_equivalent_10_min"])
        score_matrix = np.stack(scores, axis=1)
        middle = np.median(score_matrix, axis=1)
        worst = score_matrix.min(axis=1)
        regret = np.maximum(0.0, (middle - worst) / np.maximum(np.abs(middle), 1e-9))
        regret_count += int((regret > float(dominance["regret_threshold"])).sum())
        outcome_total += simulator.seed_count

    ratio_values = np.concatenate(ratio_chunks) if ratio_chunks else np.array([], dtype=np.float64)
    kpis: dict[str, Any] = {
        "SPECIAL_OPTION_DOMINANCE_RATE": rounded(special_dominance / comparison_count),
        "GENERAL_PATH_VALIDITY_RATE": rounded(general_valid / comparison_count),
        "EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE": {
            name: rounded(outcome_valid_counts[name] / outcome_total) for name in SPECIAL_TYPES
        },
        "WORST_SPECIAL_REGRET_RATE": rounded(regret_count / outcome_total),
        "SPECIAL_TOKEN_SHARE_10_MIN": rounded(token_share_sum / comparison_count),
        "SPECIAL_TOKEN_SHARE_BURST_MAX": rounded(token_burst_max),
        "MULTI_SPECIAL_DOMINANCE_RATE": rounded(multi_dominance / comparison_count),
        "SECOND_SPECIAL_MARGINAL_VALUE_RATIO": rounded(float(np.median(ratio_values)) if ratio_values.size else 0.0),
        "REROLL_EXPECTED_VALUE_GAIN": 0.0,
    }
    passed = threshold_pass(kpis, simulator.model["thresholds"])
    return {
        "vector_id": vector["vector_id"],
        "special_cost_multiplier": vector["special_cost_multiplier"],
        "special_interval_multiplier": vector["special_interval_multiplier"],
        "special_functional_value_index": vector["special_functional_value_index"],
        "primary_kpis": kpis,
        "threshold_pass": passed,
        "failed_thresholds": [name for name, is_pass in passed.items() if not is_pass],
        "passed_threshold_count": sum(1 for is_pass in passed.values() if is_pass),
    }


def general_support_sensitivity(simulator, baseline_vector: dict[str, Any]) -> dict[str, float]:
    result: dict[str, float] = {}
    denominator = (
        len(simulator.model["scenario_matrix"]["stage2_paths"])
        * len(simulator.gold_scenarios)
        * len(simulator.model["scenario_matrix"]["spin_policies"])
        * simulator.seed_count
    )
    for support_label in ("LOW", "MID", "HIGH"):
        valid = 0
        for path in simulator.model["scenario_matrix"]["stage2_paths"]:
            for gold_scenario in simulator.gold_scenarios:
                for policy in simulator.model["scenario_matrix"]["spin_policies"]:
                    run = simulator.simulate_batch_numpy(
                        baseline_vector,
                        path,
                        gold_scenario,
                        policy,
                        "general_only",
                        support_label=support_label,
                    )
                    valid += int(run["valid"].sum())
        result[support_label] = rounded(valid / denominator)
    return result
