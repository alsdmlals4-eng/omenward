#!/usr/bin/env python3
"""Validate Omenward Core V2 canonical documentation contracts."""
from __future__ import annotations

import pathlib
import re
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CORE.md",
    "docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md",
    "docs/design/APPROVED_ROULETTE_CORE_RULES.md",
    "docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    "docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md",
)

REFERENCE_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
)

BASELINE_FILES = (
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md",
    "docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md",
)

CORE_STATUS = (
    "V2_SPEC_APPROVED",
    "V2_CANON_CANDIDATE",
    "V2_IMPLEMENTATION_NOT_STARTED",
    "LEGACY_C1_C2_C3_PROVEN",
    "CORE_LOCK_V2_PENDING",
)

STATUS_BOUNDARY = (
    "V2_SPEC_APPROVED",
    "V2_CANON_CANDIDATE",
    "V2_IMPLEMENTATION_NOT_STARTED",
    "LEGACY_C1_C2_C3_PROVEN",
    "HUMAN_QA_NOT_RUN",
)

REQUIRED_DECISIONS = (
    "TokenInstance",
    "가장 낮은 안정",
    "SpinSnapshot",
    "15/25/35/45/55/100",
    "전술 아이템 룰렛 심벌은 보류",
    "TokenSource",
    "mid-run save",
)

PREMATURE_EXACT_STATES = (
    "V2_IMPLEMENTED",
    "V2_VERTICAL_SLICE_PROVEN",
    "MVP_COMPLETE",
    "CORE_LOCK_V2",
)

ACTIVE_COMPLETION_FILES = (
    "README.md",
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/OMENWARD_GAME_DESIGN.md",
)


def read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def missing(text: str, values: Iterable[str]) -> list[str]:
    return [value for value in values if value not in text]


def baseline_main(text: str) -> str | None:
    match = re.search(r"(?m)^- 기준 main: `([0-9a-f]{40})`$", text)
    return match.group(1) if match else None


def link_exists(root: pathlib.Path, source_relative: str, target: str) -> bool:
    clean = target.split("#", 1)[0].strip()
    if not clean:
        return True
    source = root / source_relative
    candidates = ((source.parent / clean).resolve(), (root / clean).resolve())
    repository_root = root.resolve()
    for candidate in candidates:
        try:
            candidate.relative_to(repository_root)
        except ValueError:
            continue
        if candidate.exists():
            return True
    return False


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if errors:
        return errors

    core = read(root, "docs/PROJECT_CORE.md")
    integrated = read(root, "docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md")
    roulette = read(root, "docs/design/APPROVED_ROULETTE_CORE_RULES.md")
    maprun = read(root, "docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md")
    status = read(root, "docs/CURRENT_IMPLEMENTATION_STATUS.md")

    for value in CORE_STATUS:
        if value not in core:
            errors.append(f"PROJECT_CORE missing V2 contract: {value}")
        if value not in integrated:
            errors.append(f"integrated spec missing V2 contract: {value}")

    for value in STATUS_BOUNDARY:
        if value not in status:
            errors.append(f"implementation status missing V2 contract: {value}")

    decision_text = "\n".join((integrated, roulette, maprun))
    for value in REQUIRED_DECISIONS:
        if value not in decision_text:
            errors.append(f"missing approved V2 decision: {value}")

    if "노출 인덱스" not in roulette or "cursor" not in roulette:
        errors.append("roulette horizontal movement contract incomplete")
    if "길이는 변하지 않는다" not in roulette or "insert" not in roulette or "remove" not in roulette:
        errors.append("roulette horizontal movement must preserve array length without insert/remove")
    if "V2_IMPLEMENTATION_NOT_STARTED" not in status or "LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN" not in status:
        errors.append("implementation status does not separate V2 from legacy evidence")

    baselines: dict[str, str] = {}
    for relative in BASELINE_FILES:
        value = baseline_main(read(root, relative))
        if value is None:
            errors.append(f"{relative} missing baseline main commit")
        else:
            baselines[relative] = value
    if len(set(baselines.values())) > 1:
        detail = ", ".join(f"{relative}={value}" for relative, value in sorted(baselines.items()))
        errors.append(f"baseline main mismatch: {detail}")

    for relative in REFERENCE_FILES:
        text = read(root, relative)
        if "PROJECT_CORE.md" not in text:
            errors.append(f"{relative} does not reference PROJECT_CORE.md")
        if "CURRENT_IMPLEMENTATION_STATUS.md" not in text:
            errors.append(f"{relative} does not reference CURRENT_IMPLEMENTATION_STATUS.md")

    for relative in ACTIVE_COMPLETION_FILES:
        text = read(root, relative)
        for state in PREMATURE_EXACT_STATES:
            if re.search(rf"(?m)^\s*{re.escape(state)}\s*$", text):
                errors.append(f"{relative} claims premature completion: {state}")

    docmap = read(root, "docs/DOCUMENTATION_MAP.md")
    for owner in (
        "APPROVED_CORE_V2_INTEGRATED_SPEC.md",
        "APPROVED_ROULETTE_CORE_RULES.md",
        "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md",
    ):
        if owner not in docmap:
            errors.append(f"documentation map missing V2 owner: {owner}")

    if "APPROVED_ROULETTE_CORE_RULES.md" not in integrated:
        errors.append("integrated spec does not route detailed roulette ownership")
    if "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md" not in integrated:
        errors.append("integrated spec does not route detailed MapRun ownership")

    for relative in REQUIRED_FILES:
        text = read(root, relative)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            if not link_exists(root, relative, target):
                errors.append(f"broken local link in {relative}: {target}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Project core V2 documentation validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Project core V2 documentation validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
