#!/usr/bin/env python3
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

UNIT_FILES = (
    "data/units/shield_guard.tres",
    "data/units/greatsword_warrior.tres",
    "data/units/assassin.tres",
    "data/units/spear_guard.tres",
    "data/units/archer.tres",
    "data/units/cavalry.tres",
    "data/units/priest.tres",
    "data/units/mage.tres",
    "data/units/flier.tres",
    "data/units/giant.tres",
)

REQUIRED_FILES = (
    "scripts/core/core_ux_service.gd",
    "scripts/core/stage_run.gd",
    "scripts/roulette/roulette_service.gd",
    "scripts/waves/wave_director.gd",
    "scripts/battle/unit_instance.gd",
    "scripts/data/unit_archetype_profile.gd",
    "scripts/ui/stage_hud.gd",
    "scenes/ui/stage_hud.tscn",
    "tests/headless/c3_core_ux_test.gd",
    "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
    *UNIT_FILES,
)


def read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing C3 file: {relative}")
    if errors:
        return errors

    service = read(root, "scripts/core/core_ux_service.gd")
    stage_run = read(root, "scripts/core/stage_run.gd")
    roulette = read(root, "scripts/roulette/roulette_service.gd")
    wave_director = read(root, "scripts/waves/wave_director.gd")
    unit_instance = read(root, "scripts/battle/unit_instance.gd")
    unit_profile = read(root, "scripts/data/unit_archetype_profile.gd")
    hud_script = read(root, "scripts/ui/stage_hud.gd")
    hud_scene = read(root, "scenes/ui/stage_hud.tscn")
    headless = read(root, "tests/headless/c3_core_ux_test.gd")
    audit = read(root, "docs/C3_CORE_UX_AUDIT_2026-07-23.md")

    for term in (
        '"token_ledger"',
        '"construction_comparison"',
        '"omen"',
        '"tactical_overlay"',
        '"latest_wave_report"',
        "probability_before",
        "probability_after",
        "gate_under_pressure",
        "clean_defense",
    ):
        if term not in service:
            errors.append(f"core UX service missing contract term: {term}")

    for term in ("CoreUxServiceScript", "core_ux_snapshot", "register_wave", "observe_unit_delta", "consume_battle_events", "update_wave_reports"):
        if term not in stage_run:
            errors.append(f"StageRun missing C3 integration term: {term}")

    for term in ("func token_ledger", "func probability_for_symbol", "X_WEIGHT", "GOLD_WEIGHT"):
        if term not in roulette:
            errors.append(f"roulette service missing authoritative preview term: {term}")

    for term in ("OMEN_T30_SECONDS", "OMEN_T15_SECONDS", "OMEN_T5_SECONDS", "func seconds_until_next_wave", "func omen_phase"):
        if term not in wave_director:
            errors.append(f"wave director missing staged omen term: {term}")

    for term in ("counter_tags", "target_priority_tags"):
        if term not in unit_profile or term not in unit_instance:
            errors.append(f"shared tactical metadata missing: {term}")

    required_unit_hints = {
        "data/units/shield_guard.tres": "ranged_defense",
        "data/units/spear_guard.tres": "anti_large",
        "data/units/archer.tres": "anti_air",
        "data/units/assassin.tres": "backline",
        "data/units/cavalry.tres": "backline",
        "data/units/giant.tres": "siege",
    }
    for relative, hint in required_unit_hints.items():
        if hint not in read(root, relative):
            errors.append(f"shared unit tactical hint missing: {relative} -> {hint}")

    for node_name in (
        "OmenDetailLabel",
        "TokenLedgerLabel",
        "ConstructionComparisonLabel",
        "TacticalOverlayLabel",
        "WaveReportLabel",
    ):
        if f'name="{node_name}"' not in hud_scene:
            errors.append(f"HUD scene missing C3 surface: {node_name}")
        if f"${node_name}" not in hud_script:
            errors.append(f"HUD script does not bind C3 surface: {node_name}")

    if "run.core_ux_snapshot()" not in hud_script:
        errors.append("HUD does not consume the read-only StageRun core UX snapshot")
    for forbidden in ("X_WEIGHT", "GOLD_WEIGHT", "WAVE_INTERVAL_SECONDS", "gate_damage_taken +", "probability_after ="):
        if forbidden in hud_script:
            errors.append(f"HUD improperly owns domain calculation: {forbidden}")

    for phrase in (
        "barracks preview increases the warrior probability before construction",
        "T-30 reveals lane and role without exact unit details",
        "T-15 reveals exact shared archetype and counter hints",
        "T-5 highlights the highest-count danger lane",
        "tactical overlay exposes the approved anti-air hint",
        "wave report counts the actual defeated enemy in its lane",
        "identical stage state produces an identical core UX snapshot",
    ):
        if phrase not in headless:
            errors.append(f"C3 headless regression missing: {phrase}")

    for heading in (
        "건설 전 룰렛 확률 미리보기",
        "현재 룰렛 토큰 장부",
        "T-30/T-15/T-5 베일의 징조",
        "상성·사거리·현재 타기팅 오버레이",
        "웨이브 종료 후 라인별 원인 보고",
        "건설 선택 비교 UI",
        "C1U_PENDING_USER_DECISION",
    ):
        if heading not in audit:
            errors.append(f"C3 audit missing approved boundary: {heading}")

    code_files = tuple((root / "scripts").rglob("*.gd"))
    forbidden_c1u_terms = ("grant_move_token", "apply_lucky_replace", "shift_roulette_row", "shift_roulette_column", "roulette_storage_capacity = 3")
    for path in code_files:
        body = path.read_text(encoding="utf-8")
        for term in forbidden_c1u_terms:
            if term in body:
                errors.append(f"C1U implementation leaked into C3: {path.relative_to(root).as_posix()} -> {term}")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        name = path.name.lower()
        relative = path.relative_to(root).as_posix()
        if "_apply_c3_" in name or "_repair_c3_" in name or "_diagnose_c3_" in name or path.name.startswith("_C3_"):
            errors.append(f"temporary C3 artifact remains: {relative}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("C3 core UX validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C3 core UX validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
