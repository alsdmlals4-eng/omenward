#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "scripts/data/roulette_spin_result.gd",
    "scripts/roulette/roulette_service.gd",
    "scripts/buildings/building_service.gd",
    "tests/headless/roulette_contract_test.gd",
    "docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md",
)
FORBIDDEN_ACTIVE_REFERENCES = (
    "docs/work_orders/0001-phase-0-codex-plan-mode.md",
    "work_orders/0001-phase-0-codex-plan-mode.md",
    "docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md",
    "work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md",
    "docs/design/proposals/0001-phase-0-godot-bootstrap.md",
    "design/proposals/0001-phase-0-godot-bootstrap.md",
    "docs/goals/0001-engine-selection-and-bootstrap.md",
    "goals/0001-engine-selection-and-bootstrap.md",
    "docs/goals/0002-core-vertical-slice.md",
    "goals/0002-core-vertical-slice.md",
)
EXCLUDED_DOC_PARTS = {"archive", "work_orders", "proposals", "issues", "goals"}


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def active_markdown_files(root: pathlib.Path = ROOT) -> list[pathlib.Path]:
    result: list[pathlib.Path] = []
    for path in (root / "docs").rglob("*.md"):
        relative_parts = path.relative_to(root / "docs").parts
        if any(part in EXCLUDED_DOC_PARTS for part in relative_parts):
            continue
        result.append(path)
    result.append(root / "README.md")
    result.append(root / "AGENTS.md")
    return sorted(set(result))


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing C1 file: {relative}")
    if errors:
        return errors

    roulette = (root / "scripts/roulette/roulette_service.gd").read_text(encoding="utf-8")
    buildings = (root / "scripts/buildings/building_service.gd").read_text(encoding="utf-8")
    stage_run = (root / "scripts/core/stage_run.gd").read_text(encoding="utf-8")
    economy_test = (root / "tests/headless/economy_roulette_test.gd").read_text(encoding="utf-8")
    contract_test = (root / "tests/headless/roulette_contract_test.gd").read_text(encoding="utf-8")

    roulette_terms = (
        "LINE_INDEXES",
        "resolve_board_snapshot",
        "_completed_line_count",
        "_rank_for_lines",
        "legendary_generated",
        "_gold_reward",
        "source_archetype_rank_fallback",
    )
    for term in roulette_terms:
        if term not in roulette:
            errors.append(f"roulette service missing contract term: {term}")
    if "return cards" in roulette or "Array[UnitSpawnDefinition]" in re.search(r"func spin.*", roulette).group(0):
        errors.append("roulette service still exposes the direct nine-card placeholder API")
    if "roulette_archetype_ids" in buildings or "roulette_archetype_ids" in economy_test:
        errors.append("legacy roulette_archetype_ids consumer remains")
    if "first_result.size() == 9" in economy_test:
        errors.append("placeholder nine-card assertion remains")
    if '&"barracks"' not in buildings or '&"warrior"' not in buildings:
        errors.append("approved barracks warrior token source is missing")
    if 'pending_roulette_rewards' not in stage_run or 'pending_reward' not in stage_run:
        errors.append("stage-owned reward storage contract is missing")
    for phrase in (
        "middle judgment line fails",
        "one matching line produces one common reward",
        "two matching lines produce elite",
        "three matching lines produce hero",
        "first all-nine board produces one legendary",
        "later all-nine boards convert to two heroes",
    ):
        if phrase not in contract_test:
            errors.append(f"roulette regression test missing: {phrase}")

    for path in active_markdown_files(root):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        for forbidden in FORBIDDEN_ACTIVE_REFERENCES:
            if forbidden in text:
                errors.append(f"active document references retired execution input: {relative} -> {forbidden}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
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
        if path.is_file() and path.name.startswith("_C1_"):
            errors.append(f"temporary C1 audit file remains: {path.relative_to(root).as_posix()}")
    for path in root.rglob("*"):
        if path.is_file() and ("_apply_c1_" in path.name or "-once" in path.name and "c1" in path.name.lower()):
            errors.append(f"temporary C1 bootstrap remains: {path.relative_to(root).as_posix()}")

    gdd = (root / "docs/OMENWARD_GAME_DESIGN.md").read_text(encoding="utf-8")
    if "문서 버전: **v0.21**" not in gdd:
        errors.append("GDD was not advanced to v0.21")
    for stale in ("### 구현 전 미확정", "Issue #1 Phase 0 Codex Plan Mode", "현재 실제 Godot 코드, Scene, Resource, 테스트는 생성·수정하지 않는다"):
        if stale in gdd:
            errors.append(f"GDD retains stale implementation state: {stale}")
    baseline = (root / "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md").read_text(encoding="utf-8")
    if "Phase 0 Plan Mode 대기 / 구현 전" in baseline:
        errors.append("active preproduction baseline still claims implementation has not started")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("C1 roulette validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C1 roulette validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
