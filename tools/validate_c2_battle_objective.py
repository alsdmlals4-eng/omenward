#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
C2_VALIDATION_RUN = "29938742864"
C2_VALIDATION_HEAD = "bf92195ee31b5d69b92c33f3b5321ed525c8b5c9"
C2_AUDIT_HEAD = "496157d0b87ab71ea2c9f25780f21df9f68b67f3"
C2_AUDIT_RUN = "29936497790"
CURRENT_WORKFLOW = ".github/workflows/validate-omenward-core.yml"
HISTORICAL_STATUS = "docs/archive/2026-07/pre-v2-canon/CURRENT_IMPLEMENTATION_STATUS_PRE_V2.md"

REQUIRED_FILES = (
    CURRENT_WORKFLOW,
    "scripts/battle/base_state.gd",
    "scripts/battle/battle_simulator.gd",
    "scripts/battle/outpost_state.gd",
    "scripts/core/stage_run.gd",
    "scripts/buildings/building_service.gd",
    "tests/headless/c2_battle_objective_test.gd",
    "docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md",
    HISTORICAL_STATUS,
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
    economy = (root / "scripts/core/stage_economy.gd").read_text(encoding="utf-8")
    unit_profile = (root / "scripts/data/unit_archetype_profile.gd").read_text(encoding="utf-8")
    contract_test = (root / "tests/headless/c2_battle_objective_test.gd").read_text(encoding="utf-8")
    workflow = (root / CURRENT_WORKFLOW).read_text(encoding="utf-8")

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
    for term in (
        "legendary_boss_unit_id",
        "_resolve_natural_result",
        "enemy_base_destroyed",
        "wave_15_legendary_boss_defeated",
    ):
        if term not in stage_run:
            errors.append(f"stage run missing natural result contract: {term}")
    for term in ("set_contested", "clear_capture_presence", "clampf(power, 0.0, MAX_CAPTURE_POWER)"):
        if term not in outpost:
            errors.append(f"outpost state missing approved capture contract: {term}")
    for term in ("sync_occupation_capacity", "roster_snapshot", "INACTIVE_LOCKED", "remove_food_cap"):
        if term not in building and term not in economy:
            errors.append(f"building lifecycle missing contract term: {term}")
    for term in ("capture_power", "structure_damage_tags"):
        if term not in unit_profile:
            errors.append(f"shared archetype schema missing objective field: {term}")

    for phrase in (
        "battle exposes one advancing front",
        "Ward forward stabilization grants the single tower",
        "the same force next stabilizes the clash zone",
        "the one enemy gate collapses from same-front siege attacks",
        "both teams on the one clash freeze it as contested",
        "an empty stable clash clears its contested marker",
        "loss of objectives locks the building below the new capacity",
        "a locked global farm loses its passive without deletion",
        "returning occupation capacity restores the owned roster entry",
        "enemy base destruction from one-front unit attacks produces a natural battle victory",
        "player base destruction produces a natural battle defeat",
        "enemy base destruction closes StageRun as victory",
        "W15 legendary boss defeat produces standard victory",
    ):
        if phrase not in contract_test:
            errors.append(f"C2 regression test missing: {phrase}")

    for term in (
        "name: Validate Omenward Core",
        "contracts_pr:",
        "contracts_full:",
        "tools/validate_c1_roulette.py",
        "tools/validate_c2_battle_objective.py",
        'os: [ubuntu-latest, windows-latest]',
        "Run all headless contract tests",
        "Runtime smoke",
    ):
        if term not in workflow:
            errors.append(f"unified core workflow missing contract term: {term}")

    gdd_body = (root / "docs/OMENWARD_GAME_DESIGN.md").read_text(encoding="utf-8")
    version_match = re.search(r"문서 버전:\s*\*\*v(\d+)\.(\d+)", gdd_body)
    current_v2 = version_match is not None and tuple(map(int, version_match.groups())) >= (0, 26)

    if current_v2:
        current_requirements = {
            "README.md": ("LEGACY_C1_C2_C3_PROVEN", "HUMAN_QA_NOT_RUN"),
            "docs/CURRENT_IMPLEMENTATION_STATUS.md": (
                "LEGACY_C1_C2_C3_PROVEN",
                "CURRENT_GODOT_RUNTIME = PARTIAL__BATTLE_PRIMARY_MACHINE_VERIFIED__MODULAR_CLOSE_BATTLEFIELD_RUNTIME_TECHNICAL_SMOKE_PASS",
                "CURRENT_WINDOWS_RUNTIME = HERA_TECHNICAL_SMOKE_PASS__ONE_LIVE_BATTLE_CAPTURE__HUMAN_NOT_RUN",
            ),
            "docs/OMENWARD_GAME_DESIGN.md": (
                "문서 버전: **v0.26",
                "LATEST_USER_DESIGN_INTEGRATED",
                "PRODUCT_CODE_NOT_AUTHORIZED",
            ),
        }
        for relative, phrases in current_requirements.items():
            body = (root / relative).read_text(encoding="utf-8")
            for phrase in phrases:
                if phrase not in body:
                    errors.append(f"{relative} missing current C2 evidence boundary: {phrase}")
    else:
        required_doc_states = {
            "README.md": ("C2 전투 목적 루프 REMOTE_PROVEN", "사람 플레이 미완결"),
            "docs/ACTIVE_CONTEXT.md": ("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN", "C3_AUTOMATED_CONTRACTS_PROVEN"),
            "docs/HANDOFF_CONTEXT.md": ("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN", "C3_AUTOMATED_CONTRACTS_PROVEN"),
            "docs/CURRENT_IMPLEMENTATION_STATUS.md": (
                "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN",
                f"C2 최종 검증 run: `{C2_VALIDATION_RUN}`",
            ),
            "docs/OMENWARD_GAME_DESIGN.md": ("문서 버전: **v0.23**", "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN"),
            "docs/OMENWARD_ROADMAP.md": ("C2 전투 목적 루프 원격 검증·병합 완료",),
            "docs/DECISIONS_PENDING.md": ("C2 전투 목적 루프 원격 검증 완료", "본진 독립 HP"),
            "docs/DOCUMENTATION_MAP.md": ("C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md",),
        }
        for relative, phrases in required_doc_states.items():
            body = (root / relative).read_text(encoding="utf-8")
            for phrase in phrases:
                if phrase not in body:
                    errors.append(f"{relative} missing proven C2 state: {phrase}")

    stale_active = (
        "C2 검증 구현는",
        "C2 전투 목적 구현 후보",
        "PR #49 사용자 검토 대기",
        "PR #49 C1 원격 검증 결과 검토",
        "C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE",
        "C2_REMOTE_VALIDATION_PENDING",
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

    audit = (root / "docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md").read_text(encoding="utf-8")
    for evidence in ("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN", C2_AUDIT_HEAD, C2_AUDIT_RUN, "`Validate Core Contracts`"):
        if evidence not in audit:
            errors.append(f"C2 audit missing historical proof: {evidence}")

    historical_status = (root / HISTORICAL_STATUS).read_text(encoding="utf-8")
    for evidence in (
        "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN",
        C2_VALIDATION_HEAD,
        C2_VALIDATION_RUN,
        "HUMAN_QA_NOT_RUN",
    ):
        if evidence not in historical_status:
            errors.append(f"historical C2 exact proof missing: {evidence}")

    if (root / ".github/workflows/validate-c1-roulette.yml").exists():
        errors.append("legacy C1-only workflow remains")
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        name = path.name.lower()
        relative = path.relative_to(root).as_posix()
        if path.name.startswith("_C2_") or any(
            token in name
            for token in (
                "_apply_c2_",
                "_sync_c2_",
                "_finalize_c2_",
                "_repair_c2_",
                "apply-c2",
                "sync-c2",
                "finalize-c2",
            )
        ):
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
