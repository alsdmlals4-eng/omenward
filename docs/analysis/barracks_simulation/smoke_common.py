"""Shared constants, threshold rules, hashes, and output serialization."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any

DECISION_ID = "OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1"
MASK64 = (1 << 64) - 1
UNIT_TYPES = ["basic_infantry", "shield", "archer", "assassin", "priest", "mage", "flying_unit", "giant"]
UNIT_INDEX = {name: index for index, name in enumerate(UNIT_TYPES)}
SPECIAL_TYPES = ["assassin", "priest", "mage", "flying_unit", "giant"]
WINDOWS = (300, 600, 900)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_code(text: str) -> int:
    return int.from_bytes(hashlib.sha256(text.encode("utf-8")).digest()[:8], "little")


def rounded(value: float) -> float:
    return round(float(value), 6)


def threshold_pass(kpis: dict[str, Any], thresholds: dict[str, float]) -> dict[str, bool]:
    outcome = kpis["EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE"]
    return {
        "SPECIAL_OPTION_DOMINANCE_RATE": kpis["SPECIAL_OPTION_DOMINANCE_RATE"] <= thresholds["SPECIAL_OPTION_DOMINANCE_RATE_MAX"],
        "GENERAL_PATH_VALIDITY_RATE": kpis["GENERAL_PATH_VALIDITY_RATE"] >= thresholds["GENERAL_PATH_VALIDITY_RATE_MIN"],
        "EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE": min(outcome.values()) >= thresholds["EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE_MIN"],
        "WORST_SPECIAL_REGRET_RATE": kpis["WORST_SPECIAL_REGRET_RATE"] <= thresholds["WORST_SPECIAL_REGRET_RATE_MAX"],
        "SPECIAL_TOKEN_SHARE_10_MIN": kpis["SPECIAL_TOKEN_SHARE_10_MIN"] <= thresholds["SPECIAL_TOKEN_SHARE_10_MIN_MAX"],
        "SPECIAL_TOKEN_SHARE_BURST_MAX": kpis["SPECIAL_TOKEN_SHARE_BURST_MAX"] <= thresholds["SPECIAL_TOKEN_SHARE_BURST_MAX_MAX"],
        "MULTI_SPECIAL_DOMINANCE_RATE": kpis["MULTI_SPECIAL_DOMINANCE_RATE"] <= thresholds["MULTI_SPECIAL_DOMINANCE_RATE_MAX"],
        "SECOND_SPECIAL_MARGINAL_VALUE_RATIO": kpis["SECOND_SPECIAL_MARGINAL_VALUE_RATIO"] <= thresholds["SECOND_SPECIAL_MARGINAL_VALUE_RATIO_MAX"],
        "REROLL_EXPECTED_VALUE_GAIN": kpis["REROLL_EXPECTED_VALUE_GAIN"] == thresholds["REROLL_EXPECTED_VALUE_GAIN"],
    }


def write_outputs(output_dir: Path, result: dict[str, Any]) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "smoke_sweep_2000.v1.json"
    csv_path = output_dir / "smoke_sweep_2000.v1.csv"
    json_path.write_text(json.dumps(result, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")
    fields = [
        "vector_id", "special_cost_multiplier", "special_interval_multiplier",
        "special_functional_value_index", "passed_threshold_count", "failed_thresholds",
        "special_option_dominance_rate", "general_path_validity_rate",
        "worst_special_regret_rate", "special_token_share_10_min",
        "special_token_share_burst_max", "multi_special_dominance_rate",
        "second_special_marginal_value_ratio", "minimum_special_outcome_validity_rate",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in result["parameter_vectors"]:
            k = row["primary_kpis"]
            writer.writerow({
                "vector_id": row["vector_id"],
                "special_cost_multiplier": row["special_cost_multiplier"],
                "special_interval_multiplier": row["special_interval_multiplier"],
                "special_functional_value_index": row["special_functional_value_index"],
                "passed_threshold_count": row["passed_threshold_count"],
                "failed_thresholds": "|".join(row["failed_thresholds"]),
                "special_option_dominance_rate": k["SPECIAL_OPTION_DOMINANCE_RATE"],
                "general_path_validity_rate": k["GENERAL_PATH_VALIDITY_RATE"],
                "worst_special_regret_rate": k["WORST_SPECIAL_REGRET_RATE"],
                "special_token_share_10_min": k["SPECIAL_TOKEN_SHARE_10_MIN"],
                "special_token_share_burst_max": k["SPECIAL_TOKEN_SHARE_BURST_MAX"],
                "multi_special_dominance_rate": k["MULTI_SPECIAL_DOMINANCE_RATE"],
                "second_special_marginal_value_ratio": k["SECOND_SPECIAL_MARGINAL_VALUE_RATIO"],
                "minimum_special_outcome_validity_rate": min(k["EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE"].values()),
            })
    return json_path, csv_path
