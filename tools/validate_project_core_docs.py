#!/usr/bin/env python3
"""Validate Omenward Core V2 canonical documentation contracts."""
from __future__ import annotations

import pathlib
import re
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]

LEDGER = "docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md"
CURRENT_R1_R2_PLAN = "docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md"
PLANNING_REVIEW = "docs/reviews/2026-07-26-v2-r1-r2-planning-review.md"
BENCHMARK_REFRESH = "docs/benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md"

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CORE.md",
    "docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md",
    LEDGER,
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
    CURRENT_R1_R2_PLAN,
    PLANNING_REVIEW,
    BENCHMARK_REFRESH,
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
    PLANNING_REVIEW,
    BENCHMARK_REFRESH,
)

# Only active current-state owners must agree on the current integration baseline.
# Historical plans retain their original baseline and are validated by authority markers instead.
PRODUCT_BASELINE_FILES = (
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
)

CORE_STATUS = (
    "V2_SPEC_APPROVED",
    "V2_CANON_CURRENT_BY_PR_57_MERGE",
    "V2_IMPLEMENTATION_NOT_STARTED",
    "LEGACY_C1_C2_C3_PROVEN",
    "CORE_LOCK_V2_PENDING",
)

STATUS_BOUNDARY = (
    "V2_SPEC_APPROVED",
    "V2_CANON_CURRENT_BY_PR_57_MERGE",
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

LEDGER_REQUIRED_CONTRACTS = (
    "GM-01",
    "GM-16",
    "GM-32",
    "SOURCE_BOUND_X",
    "GM-42",
    "GM-59",
    "GM-68",
    "GM-77",
    "GM-89R",
    "GM-99",
    "GM-100D",
    "GM-104R",
    "영웅 철벽병",
    "GM-105R",
    "GM-106",
    "AUTHORED_PRIORITY_LIST",
    "V2_IMPLEMENTATION_NOT_STARTED",
)

SUPERSEDED_CONTRACTS = (
    "계열별 고정 상위 등급 템플릿",
    "주기적 3기 묶음",
    "적 존재 시 성문 재건을 정지",
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
    LEDGER,
    PLANNING_REVIEW,
    BENCHMARK_REFRESH,
)

HISTORICAL_PLAN = "docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md"
HISTORICAL_PLAN_MARKERS = (
    "HISTORICAL_IMPLEMENTATION_PLAN_DRAFT",
    "REVALIDATION_REQUIRED",
    "PRODUCT_CODE_NOT_AUTHORIZED",
    "APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md",
)

CURRENT_PLAN_MARKERS = (
    "Governing Issue: `#69`",
    "Keep `RouletteService.spin()` on the Legacy independent nine-cell generator",
    "Token instance IDs are injected by the caller",
    "New runtime state classes use `RefCounted`",
    "Build remains blocked by the project Plan Mode gate",
)

PLANNING_REVIEW_MARKERS = (
    "PLANNING_PHASE: COMPLETE",
    "R1_R2_SCOPE: APPROVED_AND_UNCHANGED",
    "PRODUCT_CODE_AUTHORIZED: NO",
    "FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND",
    "Codex의 기준선은 실행 시작 시점의 최신 `origin/main`",
)

BENCHMARK_REFRESH_MARKERS = (
    "CURRENT_V2_STRUCTURE: RETAIN",
    "R1_R2_SCOPE: UNCHANGED",
    "설계 청사진",
    "전선 대응 브리핑",
    "전투 인과 사슬",
    "지형·경로 편집",
)

CURRENT_ROUTING_FILES = (
    PLANNING_REVIEW,
    BENCHMARK_REFRESH,
    CURRENT_R1_R2_PLAN,
)


def read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def missing(text: str, values: Iterable[str]) -> list[str]:
    return [value for value in values if value not in text]


def baseline_main(text: str) -> str | None:
    match = re.search(
        r"(?m)^- (?:기준 main|현재 main|현재 main 기준): `([0-9a-f]{40})`$",
        text,
    )
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
    ledger = read(root, LEDGER)
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

    decision_text = "\n".join((integrated, ledger, roulette, maprun))
    for value in REQUIRED_DECISIONS:
        if value not in decision_text:
            errors.append(f"missing approved V2 decision: {value}")

    for value in LEDGER_REQUIRED_CONTRACTS:
        if value not in ledger:
            errors.append(f"integrated decision ledger missing contract: {value}")

    for value in SUPERSEDED_CONTRACTS:
        if value not in ledger:
            errors.append(f"integrated decision ledger missing supersession marker: {value}")

    if "노출 인덱스" not in roulette or "cursor" not in roulette:
        errors.append("roulette horizontal movement contract incomplete")
    if "길이는 변하지 않는다" not in roulette or "insert" not in roulette or "remove" not in roulette:
        errors.append("roulette horizontal movement must preserve array length without insert/remove")
    if "V2_IMPLEMENTATION_NOT_STARTED" not in status or "LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN" not in status:
        errors.append("implementation status does not separate V2 from legacy evidence")

    baselines: dict[str, str] = {}
    for relative in PRODUCT_BASELINE_FILES:
        value = baseline_main(read(root, relative))
        if value is None:
            errors.append(f"{relative} missing baseline main commit")
        else:
            baselines[relative] = value
    if len(set(baselines.values())) > 1:
        detail = ", ".join(f"{relative}={value}" for relative, value in sorted(baselines.items()))
        errors.append(f"baseline main mismatch: {detail}")

    historical_plan = read(root, HISTORICAL_PLAN)
    for marker in HISTORICAL_PLAN_MARKERS:
        if marker not in historical_plan:
            errors.append(f"historical implementation plan missing authority marker: {marker}")

    current_plan = read(root, CURRENT_R1_R2_PLAN)
    for marker in CURRENT_PLAN_MARKERS:
        if marker not in current_plan:
            errors.append(f"current R1+R2 plan missing authority marker: {marker}")

    planning_review = read(root, PLANNING_REVIEW)
    for marker in PLANNING_REVIEW_MARKERS:
        if marker not in planning_review:
            errors.append(f"planning review missing authority marker: {marker}")

    benchmark_refresh = read(root, BENCHMARK_REFRESH)
    for marker in BENCHMARK_REFRESH_MARKERS:
        if marker not in benchmark_refresh:
            errors.append(f"V2 benchmark refresh missing scope marker: {marker}")

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
    for relative in CURRENT_ROUTING_FILES:
        if pathlib.PurePosixPath(relative).name not in docmap:
            errors.append(f"documentation map missing current planning input: {relative}")

    if "APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md" not in integrated:
        errors.append("integrated spec does not route the latest decision ledger")
    if "충돌할 경우 해당 결정 원장이 우선" not in integrated:
        errors.append("integrated spec does not establish decision-ledger precedence")
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
