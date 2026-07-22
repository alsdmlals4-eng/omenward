#!/usr/bin/env python3
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "scripts/battle/base_state.gd",
    "scripts/battle/battle_simulator.gd",
    "scripts/battle/outpost_state.gd",
    "scripts/core/stage_run.gd",
    "scripts/buildings/building_service.gd",
    "tests/headless/c2_battle_objective_test.gd",
    "docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md",
)


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing C2 file: {relative}")
    if errors:
        return errors
    simulator = (root / "scripts/battle/battle_simulator.gd").read_text(encoding="utf-8")
    stage_run = (root / "scripts/core/stage_run.gd").read_text(encoding="utf-8")
    outpost = (root / "scripts/battle/outpost_state.gd").read_text(encoding="utf-8")
    building = (root / "scripts/buildings/building_service.gd").read_text(encoding="utf-8")
    unit_profile = (root / "scripts/data/unit_archetype_profile.gd").read_text(encoding="utf-8")
    contract_test = (root / "tests/headless/c2_battle_objective_test.gd").read_text(encoding="utf-8")
    for term in (
        "controlled_clash_count",
        "stable_owned_outpost_count",
        "_advance_capture_objectives",
        "_next_objective",
        "LUMERN_VICTORY",
        "VEIL_VICTORY",
        "BaseStateScript",
    ):
        if term not in simulator:
            errors.append(f"battle simulator missing C2 contract term: {term}")
    for term in ("legendary_boss_unit_id", "_resolve_natural_result", "enemy_base_destroyed", "wave_15_legendary_boss_defeated"):
        if term not in stage_run:
            errors.append(f"stage run missing natural result contract: {term}")
    for term in ("set_contested", "clear_capture_presence", "clampf(power, 0.0, MAX_CAPTURE_POWER)"):
        if term not in outpost:
            errors.append(f"outpost state missing approved capture contract: {term}")
    for term in ("sync_outpost_states", "remove_food_cap", "RUINED"):
        if term not in building and term not in (root / "scripts/core/stage_economy.gd").read_text(encoding="utf-8"):
            errors.append(f"building lifecycle missing contract term: {term}")
    for term in ("capture_power", "structure_damage_tags"):
        if term not in unit_profile:
            errors.append(f"shared archetype schema missing objective field: {term}")
    for phrase in (
        "an uncontested giant squad captures the top clash",
        "other lane gates remain standing",
        "both teams on one clash freeze it as contested",
        "farm food cap is removed when the outpost becomes neutral",
        "enemy base destruction produces a natural battle victory",
        "player base destruction produces a natural battle defeat",
        "enemy base destruction closes StageRun as victory",
        "W15 legendary boss defeat produces standard victory",
    ):
        if phrase not in contract_test:
            errors.append(f"C2 regression test missing: {phrase}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("C2 battle objective validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2 battle objective validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
