"""Vectorized seeded economy, production, physical-reel, and pressure simulation."""
from __future__ import annotations

import math
from typing import Any

import numpy as np

from smoke_common import MASK64, SPECIAL_TYPES, UNIT_INDEX, UNIT_TYPES, WINDOWS, stable_code


def enabled_special_token_sources(
    non_special_active_sources: Any,
    special_building_active: Any,
    second_special_min_non_special_active_sources: int,
) -> tuple[Any, Any]:
    """Return active special TokenSource mask and deferred-second mask.

    Auto-production state is deliberately separate from this TokenSource mask.
    """
    active = np.asarray(special_building_active, dtype=bool)
    non_special = np.asarray(non_special_active_sources)
    token_active = np.zeros_like(active, dtype=bool)
    token_active[:, 0] = active[:, 0]
    token_active[:, 1] = active[:, 1] & (non_special >= second_special_min_non_special_active_sources)
    deferred_second = active[:, 1] & ~token_active[:, 1]
    return token_active, deferred_second


class SmokeSimulator:
    def __init__(
        self,
        baseline: dict[str, Any],
        model: dict[str, Any],
        remediation: dict[str, Any],
        seed_count: int,
    ) -> None:
        self.baseline = baseline
        self.model = model
        self.remediation = remediation
        self.seed_count = seed_count
        self.food = [float(model["unit_proxy"]["food_cost"][name]) for name in UNIT_TYPES]
        self.affinity = {
            pressure: [float(values[name]) for name in UNIT_TYPES]
            for pressure, values in model["unit_proxy"]["pressure_affinity"].items()
        }
        self.stages = baseline["stage_1_to_5_pressure_baseline"]
        self.gold_scenarios = model["scenario_matrix"]["gold_scenarios"]
        self.noise_min = float(model["battle_noise"]["minimum"])
        self.noise_max = float(model["battle_noise"]["maximum"])
        token_rule = remediation["multi_special_token_source"]
        self.second_special_min_non_special = int(token_rule["second_special_min_non_special_active_sources"])

    def _scenario_code(self, path: str, gold_scenario: str, policy: str) -> int:
        return stable_code(f"{path}|{gold_scenario}|{policy}")

    def _uniform_array(self, seeds: Any, scenario_code: int, stream: int) -> Any:
        seeds_u = np.asarray(seeds, dtype=np.uint64)
        with np.errstate(over="ignore"):
            value = ((seeds_u + np.uint64(1)) * np.uint64(0xD1342543DE82EF95))
            value ^= np.uint64(scenario_code)
            value ^= np.uint64((stream * 0x9E3779B97F4A7C15) & MASK64)
            value = value + np.uint64(0x9E3779B97F4A7C15)
            value = ((value ^ (value >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9))
            value = ((value ^ (value >> np.uint64(27))) * np.uint64(0x94D049BB133111EB))
            value = value ^ (value >> np.uint64(31))
        mantissa = (value >> np.uint64(11)) & np.uint64((1 << 53) - 1)
        return mantissa.astype(np.float64) / float(1 << 53)

    def simulate_batch_numpy(
        self,
        vector: dict[str, Any],
        path: str,
        gold_scenario: str,
        policy: str,
        plan: str,
        support_label: str = "REMEDIATION_ZERO",
        fixed_special: str | None = None,
    ) -> dict[str, Any]:
        economy = self.baseline["economy"]
        seeds = np.arange(self.seed_count, dtype=np.uint64)
        n = self.seed_count
        scenario_code = self._scenario_code(path, gold_scenario, policy)
        control_points = int(self.gold_scenarios[gold_scenario])
        special_cost = 40.0 * float(vector["special_cost_multiplier"])
        interval_scale = float(vector["special_interval_multiplier"]) / 1.70
        special_interval_vector = np.array(
            [float(self.baseline["production_intervals_active_combat_seconds"][name]) * interval_scale for name in SPECIAL_TYPES],
            dtype=np.float64,
        )
        base_power = np.array([2.5, 3.0, 3.0] + [3.0 * float(vector["special_functional_value_index"])] * 5)
        if support_label == "REMEDIATION_ZERO":
            support = {pressure: 0.0 for pressure in self.affinity}
        else:
            support = self.model["support_envelopes_tu"][support_label]
        plan_items = {
            "general_only": [],
            "special_only": ["special"],
            "general_and_special": ["general", "special"],
            "multi_special": ["special", "special"],
        }[plan]

        counts = np.zeros((n, len(UNIT_TYPES)), dtype=np.float64)
        gold = np.full(n, 20.0, dtype=np.float64)
        active_time = 0.0
        wall = 50.0
        main_progress = 0.0
        extra_progress = np.zeros(n, dtype=np.float64)
        special_progress = np.zeros((n, 2), dtype=np.float64)
        extra_active = np.zeros(n, dtype=bool)
        special_active = np.zeros((n, 2), dtype=bool)
        special_type = np.full((n, 2), -1, dtype=np.int16)
        plan_position = np.zeros(n, dtype=np.int8)
        main_symbol = "basic_infantry"
        valid = np.ones(n, dtype=bool)
        min_margin = np.full(n, np.inf, dtype=np.float64)
        margin_sum = np.zeros(n, dtype=np.float64)
        wave_index = 0
        token_share_max = np.zeros(n, dtype=np.float64)
        spin_count = np.zeros(n, dtype=np.int16)
        snapshots: dict[int, dict[str, Any]] = {}

        def reserve_vector() -> Any:
            reserve = np.zeros(n, dtype=np.float64)
            for position, item in enumerate(plan_items):
                reserve[plan_position == position] = 40.0 if item == "general" else special_cost
            return reserve

        def token_state() -> tuple[Any, Any, Any, Any]:
            symbol_counts = np.zeros((n, len(UNIT_TYPES) + 1), dtype=np.float64)
            symbol_counts[:, 0] = 1.0
            symbol_counts[:, 1 + UNIT_INDEX[main_symbol]] += 1.0
            symbol_counts[extra_active, 1 + UNIT_INDEX["basic_infantry"]] += 1.0
            non_special_sources = 2 + extra_active.astype(np.int16)
            token_active, deferred_second = enabled_special_token_sources(
                non_special_sources,
                special_active,
                self.second_special_min_non_special,
            )
            for slot in range(2):
                active_rows = np.flatnonzero(token_active[:, slot])
                if active_rows.size:
                    columns = 1 + np.array(
                        [UNIT_INDEX[SPECIAL_TYPES[index]] for index in special_type[active_rows, slot]],
                        dtype=np.int16,
                    )
                    np.add.at(symbol_counts, (active_rows, columns), 1.0)
            source_count = symbol_counts.sum(axis=1)
            reel_length = np.maximum(3.0, source_count)
            special_sources = token_active.sum(axis=1).astype(np.float64)
            return symbol_counts, reel_length, special_sources / reel_length, deferred_second

        def update_token_share() -> Any:
            nonlocal token_share_max
            _, _, share, _ = token_state()
            token_share_max = np.maximum(token_share_max, share)
            return share

        def spin(period: int, index: int, active_mask: Any) -> None:
            active_rows = np.flatnonzero(active_mask)
            if not active_rows.size:
                return
            gold[active_rows] -= float(economy["base_spin_cost_gold"])
            spin_count[active_rows] += 1
            symbol_counts, reel_length, _, _ = token_state()
            local_counts = symbol_counts[active_rows]
            probabilities = (local_counts / reel_length[active_rows, None]) ** 3
            cumulative = np.cumsum(probabilities, axis=1)
            rolls = self._uniform_array(seeds[active_rows], scenario_code, 1000 + period * 32 + index)
            hits = rolls[:, None] < cumulative
            any_hit = hits.any(axis=1)
            results = np.full(active_rows.size, -1, dtype=np.int16)
            results[any_hit] = hits[any_hit].argmax(axis=1)
            gold_rows = active_rows[results == 0]
            gold[gold_rows] += math.floor(float(economy["base_spin_cost_gold"]) * 0.75)
            reward_mask = results > 0
            if reward_mask.any():
                np.add.at(counts, (active_rows[reward_mask], results[reward_mask] - 1), 1.0)
            update_token_share()

        def spin_batch(period: int) -> None:
            if policy == "maintenance":
                spin(period, 0, gold >= float(economy["base_spin_cost_gold"]))
                return
            for spin_index in range(20):
                reserve = reserve_vector() if policy == "reserve" else 0.0
                active_mask = gold >= float(economy["base_spin_cost_gold"]) + reserve
                if not active_mask.any():
                    return
                spin(period, spin_index, active_mask)

        def buy_planned() -> None:
            for position, item in enumerate(plan_items):
                cost = 40.0 if item == "general" else special_cost
                mask = (plan_position == position) & (gold >= cost)
                if not mask.any():
                    continue
                gold[mask] -= cost
                if item == "general":
                    extra_active[mask] = True
                else:
                    target_rows = np.flatnonzero(mask)
                    slot_for_row = np.where(~special_active[target_rows, 0], 0, 1)
                    for slot in (0, 1):
                        slot_rows = target_rows[slot_for_row == slot]
                        if not slot_rows.size:
                            continue
                        special_active[slot_rows, slot] = True
                        if fixed_special is not None and slot == 0:
                            special_type[slot_rows, slot] = SPECIAL_TYPES.index(fixed_special)
                        else:
                            rolls = self._uniform_array(seeds[slot_rows], scenario_code, 2000 + slot)
                            special_type[slot_rows, slot] = np.minimum(
                                (rolls * len(SPECIAL_TYPES)).astype(np.int16), len(SPECIAL_TYPES) - 1
                            )
                plan_position[mask] += 1

        def advance_active(delta: float) -> None:
            nonlocal active_time, main_progress
            old_active = active_time
            new_active = active_time + delta
            gold[:] += (math.floor(new_active / 20.0) - math.floor(old_active / 20.0)) * 6.0
            gold[:] += (math.floor(new_active / 60.0) - math.floor(old_active / 60.0)) * 4.0 * control_points

            main_interval = 50.0 if main_symbol == "basic_infantry" else 65.0
            main_progress += delta
            produced_main = math.floor(main_progress / main_interval)
            main_progress -= produced_main * main_interval
            counts[:, UNIT_INDEX[main_symbol]] += produced_main

            extra_progress[extra_active] += delta
            produced_extra = np.floor(extra_progress / 50.0).astype(np.int16)
            extra_progress[:] -= produced_extra * 50.0
            counts[:, UNIT_INDEX["basic_infantry"]] += produced_extra

            for slot in range(2):
                active_rows = np.flatnonzero(special_active[:, slot])
                if not active_rows.size:
                    continue
                special_progress[active_rows, slot] += delta
                intervals = special_interval_vector[special_type[active_rows, slot]]
                produced = np.floor(special_progress[active_rows, slot] / intervals).astype(np.int16)
                special_progress[active_rows, slot] -= produced * intervals
                np.add.at(counts, (active_rows, 3 + special_type[active_rows, slot]), produced)
            active_time = new_active

        def snapshot() -> dict[str, Any]:
            total_food = counts @ np.asarray(self.food)
            food_factor = np.minimum(1.0, 18.0 / np.maximum(total_food, 1e-9))
            unit_equivalent = (counts @ base_power) * food_factor
            _, _, share, deferred_second = token_state()
            update_token_share()
            return {
                "gold": gold.copy(),
                "unit_equivalent": unit_equivalent,
                "token_share": share.copy(),
                "second_special_deferred": deferred_second.copy(),
                "special_buildings": special_active.sum(axis=1).astype(np.float64),
                "spin_count": spin_count.astype(np.float64).copy(),
            }

        def battle(pressure: str, threat: float) -> None:
            nonlocal valid, min_margin, margin_sum, wave_index
            total_food = counts @ np.asarray(self.food)
            food_factor = np.minimum(1.0, 18.0 / np.maximum(total_food, 1e-9))
            affinity = np.asarray(self.affinity[pressure])
            unit_power = ((counts * base_power * affinity).sum(axis=1)) * food_factor
            noise_roll = self._uniform_array(seeds, scenario_code, 3000 + wave_index)
            noise = self.noise_min + (self.noise_max - self.noise_min) * noise_roll
            capacity = (float(support[pressure]) + unit_power) * noise
            margin = (capacity - threat) / threat
            valid &= capacity >= threat
            min_margin = np.minimum(min_margin, margin)
            margin_sum += margin
            wave_index += 1

        spin(0, 0, np.ones(n, dtype=bool))

        for stage_index, stage in enumerate(self.stages):
            stage_start = wall
            elapsed = 0.0
            events: list[tuple[float, str, float]] = []
            for offset, threat in zip(stage["wave_target_offsets_seconds"], stage["wave_threat_budgets_tu"]):
                events.append((float(offset), "wave", float(threat)))
            for window in WINDOWS:
                if stage_start < window <= stage_start + float(stage["expected_active_combat_seconds"]):
                    events.append((float(window) - stage_start, "window", float(window)))
            events.append((float(stage["expected_active_combat_seconds"]), "end", 0.0))
            events.sort(key=lambda item: (item[0], 0 if item[1] == "window" else 1))

            for offset, event_type, value in events:
                delta = offset - elapsed
                if delta > 0:
                    advance_active(delta)
                    wall += delta
                    elapsed = offset
                if event_type == "wave":
                    battle(stage["pressure"], value)
                elif event_type == "window":
                    snapshots[int(value)] = snapshot()

            if stage_index < 4:
                if stage_index == 0:
                    main_symbol = path
                    main_progress = 0.0
                buy_planned()
                wall += 30.0
                spin_batch(stage_index + 1)

        snapshots[900] = snapshot()
        return {
            "valid": valid,
            "min_margin": min_margin,
            "mean_margin": margin_sum / 15.0,
            "unit_equivalent_10_min": snapshots[600]["unit_equivalent"],
            "unit_equivalent_15_min": snapshots[900]["unit_equivalent"],
            "token_share_10_min": snapshots[600]["token_share"],
            "token_share_burst_max": token_share_max,
            "second_special_token_source_deferred_10_min": snapshots[600]["second_special_deferred"],
            "gold_10_min": snapshots[600]["gold"],
            "spins_10_min": snapshots[600]["spin_count"],
        }
