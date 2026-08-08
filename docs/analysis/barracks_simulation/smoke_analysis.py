"""KPI aggregation for deterministic barracks smoke screening."""
from __future__ import annotations

from typing import Any

import numpy as np

from smoke_common import SPECIAL_TYPES, rounded, threshold_pass


def aggregate_vector(simulator, vector: dict[str, Any], general_cache: dict[tuple[str, str, str], dict[str, Any]]) -> dict[str, Any]:
    special_dominance = 0
    multi_dominance = 0
    comparison_count = 0
    general_valid = 0
    token_share_sum = 0.0
    token_burst_max = 0.0
    deferred_second_source_count = 0
    ratio_chunks: list[Any] = []
    dominance = simulator.model["dominance_rules"]

    for path in simulator.model["scenario_matrix"]["stage2_paths"]:
        for gold_scenario in simulator.gold_scenarios:
            for policy in simulator.model["scenario_matrix"]["spin_policies"]:
                key = (path, gold_scenario, policy)
                general = general_cache[key]
                special = simulator.simulate_batch_numpy(vector, path, gold_scenario, policy, "special_only", support_label="REMEDIATION_ZERO")
                general_special = simulator.simulate_batch_numpy(vector, path, gold_scenario, policy, "general_and_special", support_label="REMEDIATION_ZERO")
                multi = simulator.simulate_batch_numpy(vector, path, gold_scenario, policy, "multi_special", support_label="REMEDIATION_ZERO")
                general_valid += int(general["valid"].sum())
                comparison_count += simulator.seed_count

                # These legacy combat-success comparisons are retained as raw diagnostics only.
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
                deferred_second_source_count += int(multi["second_special_token_source_deferred_10_min"].sum())

    outcome_valid_counts = {name: 0 for name in SPECIAL_TYPES}
    outcome_total = 0
    regret_count = 0
    for path in simulator.model["scenario_matrix"]["stage2_paths"]:
        production_scores = []
        for special_name in SPECIAL_TYPES:
            result = simulator.simulate_batch_numpy(
                vector,
                path,
                "standard",
                "reserve",
                "special_only",
                support_label="REMEDIATION_ZERO",
                fixed_special=special_name,
            )
            outcome_valid_counts[special_name] += int(result["valid"].sum())
            # Remediation: outcome regret must not depend on the removed combat-support scalar.
            # Use the already-approved dimensionless 10-minute unit-equivalent screening axis only.
            production_scores.append(result["unit_equivalent_10_min"])
        score_matrix = np.stack(production_scores, axis=1)
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
    diagnostic_only = {"GENERAL_PATH_VALIDITY_RATE", "EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE"}
    decision_failed = [name for name, is_pass in passed.items() if (name not in diagnostic_only and not is_pass)]
    return {
        "vector_id": vector["vector_id"],
        "special_cost_multiplier": vector["special_cost_multiplier"],
        "special_interval_multiplier": vector["special_interval_multiplier"],
        "special_functional_value_index": vector["special_functional_value_index"],
        "primary_kpis": kpis,
        "raw_threshold_pass": passed,
        "diagnostic_only_thresholds": sorted(diagnostic_only),
        "decision_failed_thresholds": decision_failed,
        "decision_threshold_pass": not decision_failed,
        "outcome_regret_basis": "UNIT_EQUIVALENT_10_MIN_NO_COMBAT_SUPPORT_SCALAR",
        "deferred_second_special_token_source_observations": deferred_second_source_count,
    }
