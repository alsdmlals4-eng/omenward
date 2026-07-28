#!/usr/bin/env python3
"""Validate OMENWARD current Vertical Slice documentation contracts.

The active authority moved from the earlier V2 minimum-slice package to the
2026-07-27 full-system Vertical Slice contract. Historical V2 documents remain
required as lineage and detailed-rule evidence, but they no longer own current
product status.
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]

CURRENT_SPEC = "docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md"
CURRENT_REVIEW = "docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md"
EVIDENCE_PILOT = "docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md"
LEDGER = "docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md"
LEGENDARY_DEPLOYMENT_POLICY = "docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md"
ROULETTE_RULES = "docs/design/APPROVED_ROULETTE_CORE_RULES.md"
MAPRUN_RULES = "docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    CURRENT_SPEC,
    CURRENT_REVIEW,
    EVIDENCE_PILOT,
    "docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md",
    LEDGER,
    LEGENDARY_DEPLOYMENT_POLICY,
    ROULETTE_RULES,
    MAPRUN_RULES,
)

CURRENT_ROUTE_FILES = (
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
)

CORE_MARKERS = (
    "APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md",
    "PLANNING_ONLY_PROFILE",
    "제품 코드: `NOT_AUTHORIZED`",
    "VERTICAL_SLICE_NOT_IMPLEMENTED",
    "LEGACY_C1_C2_C3_PROVEN",
    "HUMAN_QA_NOT_RUN",
)

STATUS_MARKERS = (
    "APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md",
    "최신 버티컬 슬라이스 구현: `NOT_STARTED`",
    "LEGACY_C1_C2_C3_PROVEN",
    "VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED",
    "LATEST_AUTOMATED_CONTRACTS_NOT_RUN",
    "HUMAN_QA_NOT_RUN",
    "CORE_LOCK_NOT_ALLOWED",
)

SPEC_MARKERS = (
    "USER_APPROVED_PLAN",
    "PLANNING_ONLY_PROFILE",
    "PRODUCT_CODE_NOT_AUTHORIZED",
    "FULL_SYSTEM_VERTICAL_SLICE",
    "MINIMUM_CONTENT_BREADTH",
    "SKIPPED_BY_USER_DECISION",
    "NOT_IMPLEMENTED",
    "NOT_PROVEN",
    "HUMAN_QA_NOT_RUN",
    "SpinSnapshot",
    "SpinSession",
    "TokenSource",
    "20스테이지",
)

PILOT_MARKERS = (
    "status: PILOT_RECOMMENDATION",
    "implementation_authority: NONE",
    "human_validation: NOT_RUN",
    "별도 CORE_POC",
    "Vertical Slice",
    "ADAPT",
    "running-adversarial-review-and-refinement",
)

LEDGER_MARKERS = (
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
    "GM-105R",
    "GM-106",
    "AUTHORED_PRIORITY_LIST",
)

LEGENDARY_POLICY_MARKERS = (
    "LEGENDARY_ACQUISITION_CAP: REMOVED",
    "LEGENDARY_PENDING_REWARD: ALWAYS_LEGENDARY",
    "PLAYER_ALIVE_LEGENDARY_BATTLEFIELD_CAP: 1",
    "COMMIT_TIME_REVALIDATION: REQUIRED",
    "AUTO_DOWNGRADE_WITHOUT_CONSENT: FORBIDDEN",
)

PREMATURE_EXACT_STATES = (
    "VERTICAL_SLICE_PROVEN",
    "MVP_COMPLETE",
    "CORE_LOCK",
)


def read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def missing(text: str, values: Iterable[str]) -> list[str]:
    return [value for value in values if value not in text]


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
    status = read(root, "docs/CURRENT_IMPLEMENTATION_STATUS.md")
    spec = read(root, CURRENT_SPEC)
    review = read(root, CURRENT_REVIEW)
    pilot = read(root, EVIDENCE_PILOT)
    ledger = read(root, LEDGER)
    legendary = read(root, LEGENDARY_DEPLOYMENT_POLICY)
    roulette = read(root, ROULETTE_RULES)
    active_context = read(root, "docs/ACTIVE_CONTEXT.md")
    docmap = read(root, "docs/DOCUMENTATION_MAP.md")

    for value in missing(core, CORE_MARKERS):
        errors.append(f"PROJECT_CORE missing current Vertical Slice contract: {value}")
    for value in missing(status, STATUS_MARKERS):
        errors.append(f"implementation status missing current boundary: {value}")
    for value in missing(spec, SPEC_MARKERS):
        errors.append(f"current Vertical Slice spec missing contract: {value}")
    for value in missing(pilot, PILOT_MARKERS):
        errors.append(f"Evidence Pilot missing boundary: {value}")
    for value in missing(ledger, LEDGER_MARKERS):
        errors.append(f"V2 decision lineage missing contract: {value}")
    for value in missing(legendary, LEGENDARY_POLICY_MARKERS):
        errors.append(f"legendary deployment policy missing contract: {value}")

    if "BLOCKER" not in review or "제품 코드" not in review:
        errors.append("current adversarial review missing blocker or product-code boundary")

    for relative in CURRENT_ROUTE_FILES:
        if pathlib.PurePosixPath(CURRENT_SPEC).name not in read(root, relative):
            errors.append(f"{relative} does not route current Vertical Slice authority")

    if pathlib.PurePosixPath(CURRENT_REVIEW).name not in docmap:
        errors.append("documentation map does not route current adversarial review")
    if pathlib.PurePosixPath(EVIDENCE_PILOT).name not in docmap:
        errors.append("documentation map does not route Evidence Pilot")
    if "PILOT_RECOMMENDATION / NOT_CANON" not in docmap:
        errors.append("documentation map does not preserve Pilot non-canon boundary")

    if "current_branch: main" not in active_context:
        errors.append("ACTIVE_CONTEXT missing current_branch: main")
    if "context_baseline_commit" not in active_context:
        errors.append("ACTIVE_CONTEXT missing context_baseline_commit")
    if "current_branch_and_commit" in active_context:
        errors.append("ACTIVE_CONTEXT restored forbidden self-referential branch/commit field")

    if "노출 인덱스" not in roulette or "cursor" not in roulette:
        errors.append("roulette horizontal movement contract incomplete")
    if "길이는 변하지 않는다" not in roulette or "insert" not in roulette or "remove" not in roulette:
        errors.append("roulette movement must preserve array length without insert/remove")

    if "VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED" not in status:
        errors.append("implementation status does not identify latest implementation boundary")
    if "LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN" not in status:
        errors.append("implementation status does not preserve Legacy C1 evidence")

    for relative in (
        "README.md",
        "docs/PROJECT_CORE.md",
        "docs/CURRENT_IMPLEMENTATION_STATUS.md",
        "docs/ACTIVE_CONTEXT.md",
        "docs/HANDOFF_CONTEXT.md",
        "docs/OMENWARD_GAME_DESIGN.md",
        CURRENT_SPEC,
        CURRENT_REVIEW,
    ):
        text = read(root, relative)
        for state in PREMATURE_EXACT_STATES:
            if re.search(rf"(?m)^\s*{re.escape(state)}\s*$", text):
                errors.append(f"{relative} claims premature completion: {state}")

    for relative in REQUIRED_FILES:
        if not relative.endswith(".md"):
            continue
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
        print("OMENWARD current Vertical Slice documentation validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("OMENWARD current Vertical Slice documentation validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
