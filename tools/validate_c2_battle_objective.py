#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re

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
        "the top enemy gate collapses from same-lane siege unit attacks",
        "other lane gates remain standing",
        "both teams on one clash freeze it as contested",
        "an empty stable clash clears its contested marker",
        "farm food cap is removed when the outpost becomes neutral",
        "enemy base destruction from unit attacks produces a natural battle victory",
        "player base destruction produces a natural battle defeat",
        "enemy base destruction closes StageRun as victory",
        "W15 legendary boss defeat produces standard victory",
    ):
        if phrase not in contract_test:
            errors.append(f"C2 regression test missing: {phrase}")
    required_doc_states = {
        "README.md": ("C2 전투 목적 루프 구현 후보", "사람 플레이 미완결"),
        "docs/ACTIVE_CONTEXT.md": ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING"),
        "docs/HANDOFF_CONTEXT.md": ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING"),
        "docs/CURRENT_IMPLEMENTATION_STATUS.md": ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING"),
        "docs/OMENWARD_GAME_DESIGN.md": ("문서 버전: **v0.22**", "C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE"),
        "docs/OMENWARD_ROADMAP.md": ("C2 전투 목적 구현 후보·공통 원격 검증",),
        "docs/DECISIONS_PENDING.md": ("C2 전투 목적 루프 구현 후보", "본진 독립 HP"),
        "docs/DOCUMENTATION_MAP.md": ("C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md",),
    }
    for relative, phrases in required_doc_states.items():
        body = (root / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in body:
                errors.append(f"{relative} missing C2 candidate state: {phrase}")

    stale_active = (
        "PR #49 사용자 검토 대기",
        "PR #49 C1 원격 검증 결과 검토",
        "PR #49 병합",
        "[현재] 승인 룰렛 핵심 계약 복구",
        "현재 C1 시작 문서",
        "전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종은 닫히지 않았다",
    )
    excluded_parts = {"archive", "issues", "goals", "work_orders", "proposals"}
    active_docs = [root / "README.md", root / "AGENTS.md"]
    for path in (root / "docs").rglob("*.md"):
        if not any(part in excluded_parts for part in path.relative_to(root / "docs").parts):
            active_docs.append(path)
    for path in active_docs:
        body = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        for stale in stale_active:
            if stale in body:
                errors.append(f"active document retains stale C1/C2 state: {relative} -> {stale}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            clean = target.split("#", 1)[0].strip()
            if not clean or "://" in clean or clean.startswith(("#", "mailto:")):
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"broken active Markdown link: {relative} -> {clean}")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        name = path.name.lower()
        relative = path.relative_to(root).as_posix()
        if path.name.startswith("_C2_") or "_apply_c2_" in name or "_sync_c2_" in name or "apply-c2" in name or "sync-c2" in name:
            errors.append(f"temporary C2 artifact remains: {relative}")
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
