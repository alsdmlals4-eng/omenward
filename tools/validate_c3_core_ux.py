#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROOF_HEAD = "1976c5355124b2ce7d7ef77b8835df0c95710038"
PROOF_RUN = "29965348284"
FINAL_WORKFLOW = ".github/workflows/validate-omenward-core.yml"

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
CANONICAL_FILES = (
    "README.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
)
REQUIRED_FILES = (
    FINAL_WORKFLOW,
    "scripts/core/core_ux_service.gd",
    "scripts/core/stage_run.gd",
    "scripts/buildings/building_service.gd",
    "scripts/roulette/roulette_service.gd",
    "scripts/waves/wave_director.gd",
    "scripts/battle/unit_instance.gd",
    "scripts/data/unit_archetype_profile.gd",
    "scripts/ui/stage_hud.gd",
    "scenes/ui/stage_hud.tscn",
    "tests/headless/c3_core_ux_test.gd",
    *CANONICAL_FILES,
    *UNIT_FILES,
)
TEMPORARY_C3_PATHS = (
    ".github/workflows/core-contracts.yml",
    ".github/workflows/validate-core-contracts.yml",
    ".github/workflows/finalize-c3-proof.yml",
    ".github/workflows/diagnose-c3-headless.yml",
    ".github/workflows/sync-c3-canonical-docs.yml",
    "docs/_C3_HEADLESS_DIAGNOSTIC.log",
    "tools/_repair_c3_stage_run_types.py",
    "tools/sync_c3_canonical_docs.py",
    "tools/finalize_c3_proof.py",
)
STALE_CANONICAL_TERMS = (
    "C3 코어 UX 다음 구현",
    "→ [다음 구현] C3 승인 코어 UX 6종",
    "PR #50 C2 검증 결과 병합",
    "PR #50 병합 및 C3 코어 UX 착수",
    "C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING",
    "문서 버전: **v0.22**",
    "현재 C3 시작점은",
    "C3 코어 UX IMPLEMENTED·원격 검증 대기",
    "C3 IMPLEMENTED·원격 검증 대기",
    "REMOTE_VALIDATION_PENDING",
    "C3 승인 코어 UX 6종 최신 영구 CI 검증과 PR #51 병합",
    ".github/workflows/core-contracts.yml",
    ".github/workflows/validate-core-contracts.yml",
    ".github/workflows/finalize-c3-proof.yml",
    "tools/finalize_c3_proof.py",
)


def read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def require_terms(errors: list[str], body: str, terms: tuple[str, ...], label: str) -> None:
    for term in terms:
        if term not in body:
            errors.append(f"{label} missing contract term: {term}")


def reject_terms(errors: list[str], body: str, terms: tuple[str, ...], label: str) -> None:
    for term in terms:
        if term in body:
            errors.append(f"{label} contains stale or forbidden term: {term}")


def missing_numbered_sections(body: str, first: int, last: int) -> list[int]:
    return [number for number in range(first, last + 1) if re.search(rf"^## {number}(?:\.|\s)", body, flags=re.MULTILINE) is None]


def validate_links(errors: list[str], root: pathlib.Path, relative: str, body: str) -> None:
    source = root / relative
    repository_root = root.resolve()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_text = target.split("#", 1)[0]
        if not path_text:
            continue
        candidates = ((source.parent / path_text).resolve(), (root / path_text).resolve())
        valid = False
        for candidate in candidates:
            try:
                candidate.relative_to(repository_root)
            except ValueError:
                continue
            if candidate.exists():
                valid = True
                break
        if not valid:
            errors.append(f"{relative} has broken local link: {target}")


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing C3 file: {relative}")
    for relative in TEMPORARY_C3_PATHS:
        if (root / relative).exists():
            errors.append(f"temporary C3 artifact remains: {relative}")
    if errors:
        return errors

    workflow = read(root, FINAL_WORKFLOW)
    service = read(root, "scripts/core/core_ux_service.gd")
    stage_run = read(root, "scripts/core/stage_run.gd")
    buildings = read(root, "scripts/buildings/building_service.gd")
    roulette = read(root, "scripts/roulette/roulette_service.gd")
    wave_director = read(root, "scripts/waves/wave_director.gd")
    unit_instance = read(root, "scripts/battle/unit_instance.gd")
    unit_profile = read(root, "scripts/data/unit_archetype_profile.gd")
    hud_script = read(root, "scripts/ui/stage_hud.gd")
    hud_scene = read(root, "scenes/ui/stage_hud.tscn")
    headless = read(root, "tests/headless/c3_core_ux_test.gd")
    canonical = {relative: read(root, relative) for relative in CANONICAL_FILES}

    require_terms(
        errors,
        workflow,
        (
            "name: Validate Omenward Core",
            "python tools/validate_c3_core_ux.py",
            "python -m unittest discover -s tests/python -v",
            "timeout 120s",
            "timeout 60s ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . -s",
            "Reject temporary C3 artifacts",
            "test ! -e tools/finalize_c3_proof.py",
            "test ! -e .github/workflows/core-contracts.yml",
            "test ! -e .github/workflows/validate-core-contracts.yml",
            "test ! -e .github/workflows/finalize-c3-proof.yml",
        ),
        "permanent Omenward workflow",
    )
    require_terms(
        errors,
        service,
        (
            '"token_ledger"',
            '"construction_comparison"',
            '"omen"',
            '"tactical_overlay"',
            '"latest_wave_report"',
            "roulette_token_sources_snapshot",
            "token_ledger_from_sources",
            "available_definitions_snapshot",
            "probability_for_symbol_from_sources",
            "var preview_sources: Array[Dictionary]",
            "var before_probability: float",
            "var after_probability: float",
            "gate_under_pressure",
            "clean_defense",
        ),
        "core UX service",
    )
    for forbidden in (
        "run.buildings.roulette_token_sources()",
        "run.buildings.building_state(HOME_OUTPOST_ID",
        "run.roulette.probability_for_symbol(symbol_id",
    ):
        if forbidden in service:
            errors.append(f"core UX snapshot uses mutating query path: {forbidden}")
    require_terms(
        errors,
        buildings,
        ("func roulette_token_sources_snapshot()", "func roster_snapshot()", "func available_definitions_snapshot()", "return roulette_token_sources_snapshot()"),
        "building read-only snapshot API",
    )
    require_terms(errors, roulette, ("func token_ledger_from_sources(", "func probability_for_symbol_from_sources(", "X_WEIGHT", "GOLD_WEIGHT"), "roulette authoritative preview")
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
        wave_director,
        ("const OMEN_T30_SECONDS", "const OMEN_T15_SECONDS", "const OMEN_T5_SECONDS", "func seconds_until_next_wave", "func omen_phase"),
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
    if 'target_priority_tags = PackedStringArray("flying", "nearest")' not in read(root, "data/units/archer.tres"):
        errors.append("archer target-priority vocabulary is not normalized to flying")

    for node_name in ("OmenDetailLabel", "TokenLedgerLabel", "ConstructionComparisonLabel", "TacticalOverlayLabel", "WaveReportLabel"):
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
            'front.get("gate_damage_dealt"',
            'front.get("gate_damage_taken"',
            'front.get("base_damage_dealt"',
            'front.get("base_damage_taken"',
        ),
        "HUD C3 evidence rendering",
    )
    for forbidden in ("X_WEIGHT", "GOLD_WEIGHT", "WAVE_INTERVAL_SECONDS", "gate_damage_taken +", "probability_after ="):
        if forbidden in hud_script:
            errors.append(f"HUD improperly owns domain calculation: {forbidden}")

    require_terms(
        errors,
        headless,
        (
            "func _test_script_instantiation",
            "C3 dependency script cannot instantiate",
            "_test_snapshot_is_read_only",
            "repeated C3 reads return the same snapshot without a gameplay tick",
            "C3 snapshot does not spend or grant gold",
            "C3 snapshot does not change food capacity",
            "C3 snapshot does not change global roster activation",
            "C3 snapshot does not append gameplay input-log events",
            "initial token ledger does not invent an inactive building source",
            "token ledger exposes the authoritative global roster source ID",
            "construction comparison exposes insufficient gold without mutating state",
            "an unstable Ward forward base leaves only the six base roster slots",
            "tactical overlay safely exposes a unit with no current target",
            "wave report remains empty while a registered wave is unresolved",
            "T-30 reveals the one front and role without exact unit details",
            "T-15 reveals exact shared archetype and counter hints",
            "T-5 highlights the one danger front",
            "tactical overlay exposes the approved anti-air hint",
            "tactical overlay exposes the approved target-priority hint",
            "wave report counts the actual defeated enemy on its front",
            "identical stage state produces an identical core UX snapshot",
        ),
        "C3 headless regression",
    )

    code_body = "\n".join((stage_run, service, roulette, hud_script))
    for forbidden in ("grant_move_token", "lucky_failure_counter", "result_storage_slots", "fixed_legendary_template"):
        if forbidden in code_body:
            errors.append(f"C1U implementation leaked into C3: {forbidden}")

    audit = canonical["docs/C3_CORE_UX_AUDIT_2026-07-23.md"]
    require_terms(
        errors,
        audit,
        (
            "C3_AUTOMATED_CONTRACTS_PROVEN",
            "HUMAN_QA_PENDING",
            "C1U_PENDING_USER_DECISION",
            PROOF_HEAD,
            PROOF_RUN,
            "var preview_sources: Array[Dictionary]",
            "각 Godot headless 파일에 60초 상한",
            "CORE_LOOP_PROVEN",
            "CORE_VERTICAL_SLICE_COMPLETE",
        ),
        "C3 audit",
    )

    gdd_body = canonical["docs/OMENWARD_GAME_DESIGN.md"]
    version_match = re.search(r"문서 버전:\s*\*\*v(\d+)\.(\d+)", gdd_body)
    current_v2 = version_match is not None and tuple(map(int, version_match.groups())) >= (0, 26)
    if current_v2:
        current_requirements = {
            "README.md": ("LEGACY_C1_C2_C3_PROVEN", "HUMAN_QA_NOT_RUN"),
            "docs/CURRENT_IMPLEMENTATION_STATUS.md": (
                "LEGACY_C1_C2_C3_PROVEN",
                "CURRENT_GODOT_RUNTIME = PARTIAL__BATTLE_PRIMARY_MACHINE_VERIFIED__MODULAR_CLOSE_BATTLEFIELD_RUNTIME_TECHNICAL_SMOKE_PASS",
                "CURRENT_WINDOWS_RUNTIME = HERA_TECHNICAL_SMOKE_PASS__ONE_LIVE_BATTLE_CAPTURE__HUMAN_NOT_RUN",
                "HUMAN_QA_NOT_RUN",
            ),
            "docs/OMENWARD_GAME_DESIGN.md": (
                "문서 버전: **v0.26",
                "LATEST_USER_DESIGN_INTEGRATED",
                "PRODUCT_CODE_NOT_AUTHORIZED",
            ),
            "docs/C3_CORE_UX_AUDIT_2026-07-23.md": (
                "C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING",
                PROOF_HEAD,
                PROOF_RUN,
            ),
        }
        for relative, terms in current_requirements.items():
            body = canonical[relative]
            require_terms(errors, body, terms, relative)
            validate_links(errors, root, relative, body)
        return errors

    canonical_requirements = {
        "README.md": ("C3 코어 UX AUTOMATED_CONTRACTS_PROVEN", PROOF_RUN, "[다음 실행] 10~15분 사람 플레이", "C1U 이동권·럭키·100,000시드"),
        "docs/CURRENT_IMPLEMENTATION_STATUS.md": ("C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING", PROOF_HEAD, PROOF_RUN, "라인별 웨이브 원인 보고", "C1U 이동권·럭키·결과 보관함 3칸"),
        "docs/ACTIVE_CONTEXT.md": ("C3_AUTOMATED_CONTRACTS_PROVEN", PROOF_RUN, "[다음 실행] 사람 플레이·1080p·720p 가독성 검증"),
        "docs/HANDOFF_CONTEXT.md": ("C3_AUTOMATED_CONTRACTS_PROVEN", "StageRun.core_ux_snapshot()", PROOF_RUN, "C1U 사용자 결정 게이트"),
        "docs/OMENWARD_GAME_DESIGN.md": ("문서 버전: **v0.23**", "C3_AUTOMATED_CONTRACTS_PROVEN", PROOF_RUN, "C3 코어 UX 6종", "사람 QA 전 `CORE_LOOP_PROVEN`"),
        "docs/OMENWARD_ROADMAP.md": ("C3 AUTOMATED_CONTRACTS_PROVEN", "AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING", "10~15분 사람 플레이·1080p·720p 가독성 QA", PROOF_RUN, "C1U는 사용자 결정 전 보류"),
        "docs/DECISIONS_PENDING.md": ("C3 자동 계약 검증 완료·사람 QA 준비", "B.3 C3 코어 UX 6종", PROOF_RUN, "이동권 심벌 완성선의 정확한 지급량", "본진 독립 HP·방어·저항 최종값"),
        "docs/DOCUMENTATION_MAP.md": ("현재 사람 QA 시작점", "C3_CORE_UX_AUDIT_2026-07-23.md", "C3 코어 UX 구현·검증 계약"),
        "docs/GODOT_PROJECT_STRUCTURE.md": ("C3 코어 UX AUTOMATED_CONTRACTS_PROVEN", "## C3 코어 UX 런타임", "core_ux_snapshot()", PROOF_RUN),
        "docs/VERTICAL_SLICE_VALIDATION.md": ("## C3 automated evidence", PROOF_HEAD, PROOF_RUN, "Validate Omenward Core", "사람 플레이·1080p·720p 가독성은 아직 실행하지 않았다"),
        "docs/C3_CORE_UX_AUDIT_2026-07-23.md": ("C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING", PROOF_HEAD, PROOF_RUN),
    }
    for relative, terms in canonical_requirements.items():
        require_terms(errors, canonical[relative], terms, relative)
        reject_terms(errors, canonical[relative], STALE_CANONICAL_TERMS, relative)
        validate_links(errors, root, relative, canonical[relative])

    gdd = canonical["docs/OMENWARD_GAME_DESIGN.md"]
    missing_gdd = missing_numbered_sections(gdd, 1, 20)
    if missing_gdd:
        errors.append("GDD appears truncated")
        for number in missing_gdd:
            errors.append(f"GDD lost required section {number}")
    require_terms(
        errors,
        gdd,
        (
            "중립화 10초 + 점령 10초",
            "HP 5000",
            "공성 태그 피해 200%",
            "진입 준비 1초",
            "우회 이동 9초",
            "시작 금화 160",
            "기본 수입 20초마다 +5",
            "중앙 가로줄의 동일 비-X 심벌 3개",
            "8·9칸 동일",
            "튜토리얼 1개 + 정규 9개",
            "지상 유닛 | 120 | 180",
            "W15: 직선 돌파",
            "W20: 끝나지 않는 진군",
        ),
        "GDD no-loss contract",
    )

    roadmap = canonical["docs/OMENWARD_ROADMAP.md"]
    for number in missing_numbered_sections(roadmap, 1, 15):
        errors.append(f"roadmap lost required section {number}")
    require_terms(errors, roadmap, ("## 4. G1", "## 5. G2", "## 7. P1", "## 9. P2", "## 10. P3", "## 11. P4", "## 12. P5", "## 13. P6", "## 14. 단계 변경 시 문서 동기화", "## 15. 지금 실행할 단 하나의 작업"), "roadmap no-loss contract")

    decisions = canonical["docs/DECISIONS_PENDING.md"]
    for number in missing_numbered_sections(decisions, 1, 12):
        errors.append(f"decisions lost required section {number}")
    require_terms(errors, decisions, ("Godot 4.7.1에서 치명적 회귀", "Mobile·Forward+ 재검토", "640×360 논리 화면 대안", "AutoLoad 승격 재검토", "JSON Schema 파일과 GDScript validator", "AnimationContract 10개", "allied/veil Visual Profile 20개", "결과 보관함 3칸"), "decisions no-loss contract")

    handoff = canonical["docs/HANDOFF_CONTEXT.md"]
    for number in missing_numbered_sections(handoff, 1, 12):
        errors.append(f"handoff lost required section {number}")

    structure = canonical["docs/GODOT_PROJECT_STRUCTURE.md"]
    for number in missing_numbered_sections(structure, 1, 16):
        errors.append(f"Godot structure lost required section {number}")
    require_terms(errors, structure, ("## C2 전투 목적 런타임", "## C3 코어 UX 런타임", "GameSession", "UnitArchetypeProfile", "AnimationContract", "FactionVisualProfile"), "Godot structure no-loss contract")

    validation = canonical["docs/VERTICAL_SLICE_VALIDATION.md"]
    if validation.count("python tools/validate_c2_battle_objective.py") != 1:
        errors.append("vertical validation must contain the C2 validator exactly once")
    if validation.count("python tools/validate_c3_core_ux.py") != 1:
        errors.append("vertical validation must contain the C3 validator exactly once")
    return errors


def main() -> int:
    errors = validate(ROOT)
    if errors:
        print("C3 core UX validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C3 core UX validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
