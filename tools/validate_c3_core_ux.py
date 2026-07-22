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
    ".github/workflows/validate-core-contracts.yml",
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

TEMPORARY_C3_PATHS = (
    ".github/workflows/diagnose-c3-headless.yml",
    "docs/_C3_HEADLESS_DIAGNOSTIC.log",
    "tools/_repair_c3_stage_run_types.py",
)


def read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def require_terms(errors: list[str], body: str, terms: tuple[str, ...], label: str) -> None:
    for term in terms:
        if term not in body:
            errors.append(f"{label} missing contract term: {term}")


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing C3 file: {relative}")
    if errors:
        return errors

    workflow = read(root, ".github/workflows/validate-core-contracts.yml")
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

    require_terms(
        errors,
        service,
        (
            '"token_ledger"',
            '"construction_comparison"',
            '"omen"',
            '"tactical_overlay"',
            '"latest_wave_report"',
            "var before_probability: float",
            "var preview_sources: Array[Dictionary]",
            "var after_probability: float",
            "var role: String",
            "probability_before",
            "probability_after",
            "gate_under_pressure",
            "clean_defense",
        ),
        "core UX service",
    )

    require_terms(
        errors,
        stage_run,
        (
            'const RouletteSpinResult = preload("res://scripts/data/roulette_spin_result.gd")',
            'const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")',
            "CoreUxServiceScript",
            "core_ux_snapshot",
            "register_wave",
            "observe_unit_delta",
            "consume_battle_events",
            "update_wave_reports",
        ),
        "StageRun C3 integration",
    )

    require_terms(
        errors,
        roulette,
        ("func token_ledger", "func probability_for_symbol", "X_WEIGHT", "GOLD_WEIGHT"),
        "roulette authoritative preview",
    )

    require_terms(
        errors,
        wave_director,
        (
            "OMEN_T30_SECONDS",
            "OMEN_T15_SECONDS",
            "OMEN_T5_SECONDS",
            "func seconds_until_next_wave",
            "func omen_phase",
        ),
        "wave director staged omen",
    )

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

    require_terms(
        errors,
        hud_script,
        (
            "run.core_ux_snapshot()",
            'entry.get("source_building_ids"',
            'entry.get("reward_archetype_ids"',
            'entry.get("target_priority_tags"',
            'lane.get("gate_damage_dealt"',
            'lane.get("gate_damage_taken"',
            'lane.get("base_damage_dealt"',
            'lane.get("base_damage_taken"',
        ),
        "HUD C3 evidence rendering",
    )
    for forbidden in (
        "X_WEIGHT",
        "GOLD_WEIGHT",
        "WAVE_INTERVAL_SECONDS",
        "gate_damage_taken +",
        "probability_after =",
    ):
        if forbidden in hud_script:
            errors.append(f"HUD improperly owns domain calculation: {forbidden}")

    require_terms(
        errors,
        headless,
        (
            "_test_script_instantiation",
            "C3 dependency script cannot instantiate",
            "initial token ledger does not invent an inactive building source",
            "token ledger exposes the authoritative source building ID",
            "construction comparison exposes insufficient gold without mutating state",
            "construction comparison safely blocks a contested capture state",
            "tactical overlay safely exposes a unit with no current target",
            "wave report remains empty while a registered wave is unresolved",
            "barracks preview increases the warrior probability before construction",
            "T-30 reveals lane and role without exact unit details",
            "T-15 reveals exact shared archetype and counter hints",
            "T-5 highlights the highest-count danger lane",
            "tactical overlay exposes the approved anti-air hint",
            "tactical overlay exposes the approved target-priority hint",
            "wave report counts the actual defeated enemy in its lane",
            "identical stage state produces an identical core UX snapshot",
        ),
        "C3 headless regression",
    )

    require_terms(
        errors,
        workflow,
        (
            "Validate C3 core UX contract",
            "python tools/validate_c3_core_ux.py",
            "timeout 120s",
            "timeout 60s",
            "Reject temporary C3 repair artifacts",
            "test ! -e docs/_C3_HEADLESS_DIAGNOSTIC.log",
            "test ! -e tools/_repair_c3_stage_run_types.py",
            "test ! -e .github/workflows/diagnose-c3-headless.yml",
        ),
        "permanent core contract workflow",
    )

    require_terms(
        errors,
        audit,
        (
            "C3_IMPLEMENTED",
            "REMOTE_VALIDATION_PENDING",
            "HUMAN_QA_PENDING",
            "C1U_PENDING_USER_DECISION",
            "var preview_sources: Array[Dictionary]",
            "각 Godot headless 파일에 60초 상한",
            "CORE_LOOP_PROVEN",
            "CORE_VERTICAL_SLICE_COMPLETE",
        ),
        "C3 audit",
    )
    for stale in (
        "C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING",
        "현재 누락:",
        "건설 전후 확률 차이와 비용·효과 비교가 없다.",
    ):
        if stale in audit:
            errors.append(f"C3 audit regressed to a pre-implementation state: {stale}")

    code_files = tuple((root / "scripts").rglob("*.gd"))
    forbidden_c1u_terms = (
        "grant_move_token",
        "apply_lucky_replace",
        "shift_roulette_row",
        "shift_roulette_column",
        "roulette_storage_capacity = 3",
    )
    for path in code_files:
        body = path.read_text(encoding="utf-8")
        for term in forbidden_c1u_terms:
            if term in body:
                errors.append(
                    f"C1U implementation leaked into C3: {path.relative_to(root).as_posix()} -> {term}"
                )

    for relative in TEMPORARY_C3_PATHS:
        if (root / relative).exists():
            errors.append(f"temporary C3 artifact remains: {relative}")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        name = path.name.lower()
        relative = path.relative_to(root).as_posix()
        if (
            "_apply_c3_" in name
            or "_repair_c3_" in name
            or "_diagnose_c3_" in name
            or "diagnose-c3" in name
            or path.name.startswith("_C3_")
        ):
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
