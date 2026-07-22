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
    *CANONICAL_FILES,
    *UNIT_FILES,
)

TEMPORARY_C3_PATHS = (
    ".github/workflows/diagnose-c3-headless.yml",
    ".github/workflows/sync-c3-canonical-docs.yml",
    "docs/_C3_HEADLESS_DIAGNOSTIC.log",
    "tools/_repair_c3_stage_run_types.py",
    "tools/sync_c3_canonical_docs.py",
)

STALE_CANONICAL_TERMS = (
    "C3 코어 UX 다음 구현",
    "→ [다음 구현] C3 승인 코어 UX 6종",
    "PR #50 C2 검증 결과 병합",
    "PR #50 병합 및 C3 코어 UX 착수",
    "C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING",
    "문서 버전: **v0.22**",
    "현재 C3 시작점은",
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
    canonical = {relative: read(root, relative) for relative in CANONICAL_FILES}
    audit = canonical["docs/C3_CORE_UX_AUDIT_2026-07-23.md"]

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
    reject_terms(
        errors,
        audit,
        (
            "C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING",
            "현재 누락:",
            "건설 전후 확률 차이와 비용·효과 비교가 없다.",
        ),
        "C3 audit",
    )

    canonical_requirements = {
        "README.md": (
            "C3 코어 UX IMPLEMENTED·원격 검증 대기",
            "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
            "[다음 실행] 10~15분 사람 플레이",
            "C1U 이동권·럭키·100,000시드",
        ),
        "docs/CURRENT_IMPLEMENTATION_STATUS.md": (
            "C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING",
            "건설 전 룰렛 확률 미리보기",
            "라인별 웨이브 원인 보고",
            "C1U 이동권·럭키·결과 보관함 3칸",
            "PR #51",
        ),
        "docs/ACTIVE_CONTEXT.md": (
            "C3_IMPLEMENTED",
            "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
            "PR #51",
            "[다음 실행] 사람 플레이·1080p·720p 가독성 검증",
        ),
        "docs/HANDOFF_CONTEXT.md": (
            "C3_IMPLEMENTED",
            "StageRun.core_ux_snapshot()",
            "PR #51 병합",
            "C1U 사용자 결정 게이트",
        ),
        "docs/OMENWARD_GAME_DESIGN.md": (
            "문서 버전: **v0.23**",
            "C3_IMPLEMENTED",
            "C3 코어 UX 6종",
            "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
            "사람 QA 전 `CORE_LOOP_PROVEN`",
        ),
        "docs/OMENWARD_ROADMAP.md": (
            "C3 IMPLEMENTED·원격 검증 대기",
            "IMPLEMENTED / REMOTE_VALIDATION_PENDING",
            "C3 승인 코어 UX 6종 최신 영구 CI 검증과 PR #51 병합",
            "C1U는 사용자 결정 전 보류",
        ),
        "docs/DECISIONS_PENDING.md": (
            "PR #50 병합 완료",
            "B.3 C3 코어 UX 6종",
            "PR #51 병합",
            "이동권 심벌 완성선의 정확한 지급량",
            "본진 독립 HP·방어·저항 최종값",
        ),
        "docs/DOCUMENTATION_MAP.md": (
            "현재 사람 QA 시작점",
            "C3_CORE_UX_AUDIT_2026-07-23.md",
            "C3 코어 UX 구현·검증 계약",
        ),
        "docs/GODOT_PROJECT_STRUCTURE.md": (
            "C3 코어 UX IMPLEMENTED·원격 검증 대기",
            "StageRun.core_ux_snapshot()",
            "counter_tags",
            "target_priority_tags",
        ),
        "docs/VERTICAL_SLICE_VALIDATION.md": (
            "python tools/validate_c3_core_ux.py",
            "C1·C2·C3·프로젝트 코어·Skill Validator",
            "파일별 60초 상한",
            "임시 C3 수리·진단 파일의 재유입 거부",
        ),
    }
    for relative, terms in canonical_requirements.items():
        require_terms(errors, canonical[relative], terms, f"canonical document {relative}")

    for relative, body in canonical.items():
        reject_terms(errors, body, STALE_CANONICAL_TERMS, f"canonical document {relative}")

    gdd = canonical["docs/OMENWARD_GAME_DESIGN.md"]
    if len(gdd) < 16000:
        errors.append("GDD appears truncated below the protected C3 summary floor")
    require_terms(
        errors,
        gdd,
        (
            "중립화 10초 + 점령 10초",
            "최대 유효 점령력 2.0",
            "복귀 속도 초당 10%",
            "HP 5000",
            "공성 태그 피해 200%",
            "우회 이동 9초",
            "도착 2.5초 전",
            "시작 금화 160",
            "기본 수입 20초마다 +5",
            "중앙 접전지 60초마다 소유 지점당 +4",
            "중간거점 30초마다 소유 지점당 +2",
            "중앙 가로줄의 동일 비-X 심벌 3개",
            "전설은 스테이지당 1회",
            "방패병",
            "대검전사",
            "암살자",
            "창병",
            "궁병",
            "기병",
            "사제",
            "마법사",
            "비행병",
            "거인",
            "W15",
            "W20",
            "EnemyUnitProfile",
            "미니맵 없음",
        ),
        "GDD no-loss contract",
    )

    roadmap = canonical["docs/OMENWARD_ROADMAP.md"]
    if len(roadmap) < 9000:
        errors.append("roadmap appears truncated below the protected C3 summary floor")
    for section in range(1, 16):
        if f"## {section}." not in roadmap:
            errors.append(f"roadmap lost required section {section}")
    require_terms(
        errors,
        roadmap,
        (
            "P0 프리프로덕션",
            "P1 기술 기준선",
            "C0 정본·코어 복구",
            "C1 룰렛 핵심 계약",
            "C1U 룰렛 유틸리티",
            "C2 전투 목적 루프",
            "C3 코어 UX",
            "C4 코어 플레이테스트",
            "P3 시스템 안정화",
            "P4 콘텐츠·아트 확장",
            "P5 캠페인·데모",
            "P6 출시 준비",
        ),
        "roadmap no-loss contract",
    )

    decisions = canonical["docs/DECISIONS_PENDING.md"]
    require_terms(
        errors,
        decisions,
        (
            "Godot 4.7.1에서 치명적 회귀",
            "4.6.3 대안",
            "Mobile·Forward+",
            "640×360 논리 화면 대안",
            "AutoLoad 승격 재검토",
            "JSON Schema 파일과 GDScript validator",
            "AnimationContract 10개",
            "allied/veil Visual Profile 20개",
            "중앙 접전지 전용 점령·안정화 시간",
            "정규화 0~100 시뮬레이션 좌표",
        ),
        "decisions no-loss contract",
    )

    validation = canonical["docs/VERTICAL_SLICE_VALIDATION.md"]
    if validation.count("python tools/validate_c2_battle_objective.py") != 1:
        errors.append("vertical-slice validation must contain the C2 validator exactly once")
    if validation.count("python tools/validate_c3_core_ux.py") != 1:
        errors.append("vertical-slice validation must contain the C3 validator exactly once")

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
            or "sync_c3_canonical" in name
            or "diagnose-c3" in name
            or "sync-c3-canonical" in name
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
