#!/usr/bin/env python3
"""Validate OMENWARD current documentation contracts and lifecycle boundaries."""
from __future__ import annotations

import pathlib
import re
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]

CURRENT_SPEC = "docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md"
CURRENT_REVIEW = "docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md"
CURRENT_CORE_REVIEW = "docs/reviews/ADVERSARIAL_CORE_FUN_CANON_AND_LEGACY_CONFLICT_REVIEW_2026-08-04.md"
CURRENT_CORE_FUN = "docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md"
CURRENT_GDD = "docs/OMENWARD_GDD_CURRENT_CANON.md"
LIFECYCLE_REGISTRY = "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
LIFECYCLE_POLICY = "docs/process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md"
EVIDENCE_PILOT = "docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md"
LEDGER = "docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md"
LEGENDARY_DEPLOYMENT_POLICY = "docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md"
ROULETTE_RULES = "docs/design/APPROVED_ROULETTE_CORE_RULES.md"
MAPRUN_RULES = "docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"
DYNAMIC_CURRENT_REF = "RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH"

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    LIFECYCLE_REGISTRY,
    LIFECYCLE_POLICY,
    CURRENT_GDD,
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    CURRENT_CORE_FUN,
    CURRENT_CORE_REVIEW,
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
    CURRENT_GDD,
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
    "골드 / 마력 / 배치 병력·병력 한도 / 이동권",
    "금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑",
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

LIFECYCLE_MARKERS = (
    "[현행]",
    "[대체됨]",
    "[보류]",
    "[폐기]",
    "[증거]",
    "OMENWARD_GDD_CURRENT_CANON.md",
)

CORE_FUN_MARKERS = (
    "예고된 압력",
    "제작한 확률",
    "비가역 전선 커밋",
    "설명 가능한 결과",
    "MASS",
    "ARMORED",
    "FLYING",
    "INFILTRATION",
    "SIEGE",
)

PREMATURE_EXACT_STATES = (
    "VERTICAL_SLICE_PROVEN",
    "MVP_COMPLETE",
    "CORE_LOCK",
)

LEGACY_CORE_MARKERS = (
    "storage_selling_food",
    "마석",
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


def has_fixed_sha_field(text: str, field: str) -> bool:
    return bool(re.search(rf"(?m)^{re.escape(field)}:\s*[0-9a-f]{{40}}\s*$", text))


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            if relative == LIFECYCLE_REGISTRY:
                errors.append(f"missing lifecycle registry: {relative}")
            else:
                errors.append(f"missing required file: {relative}")
    if errors:
        return errors

    core = read(root, "docs/PROJECT_CORE.md")
    status = read(root, "docs/CURRENT_IMPLEMENTATION_STATUS.md")
    spec = read(root, CURRENT_SPEC)
    review = read(root, CURRENT_REVIEW)
    core_review = read(root, CURRENT_CORE_REVIEW)
    core_fun = read(root, CURRENT_CORE_FUN)
    current_gdd = read(root, CURRENT_GDD)
    legacy_gdd = read(root, "docs/OMENWARD_GAME_DESIGN.md")
    lifecycle = read(root, LIFECYCLE_REGISTRY)
    policy = read(root, LIFECYCLE_POLICY)
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
    for value in missing(lifecycle, LIFECYCLE_MARKERS):
        errors.append(f"document lifecycle registry missing marker: {value}")
    for value in missing(core_fun, CORE_FUN_MARKERS):
        errors.append(f"core fun guardrails missing marker: {value}")

    if "BLOCKER" not in review or "제품 코드" not in review:
        errors.append("current adversarial review missing blocker or product-code boundary")
    if "BLOCKER" not in core_review or "PRODUCT_CODE" not in core_review:
        errors.append("current core adversarial review missing blocker or product-code boundary")

    for relative in CURRENT_ROUTE_FILES:
        if pathlib.PurePosixPath(CURRENT_SPEC).name not in read(root, relative):
            errors.append(f"{relative} does not route current Vertical Slice authority")

    if pathlib.PurePosixPath(CURRENT_REVIEW).name not in docmap:
        errors.append("documentation map does not route current adversarial review")
    if pathlib.PurePosixPath(CURRENT_CORE_REVIEW).name not in docmap:
        errors.append("documentation map does not route current core adversarial review")
    if pathlib.PurePosixPath(EVIDENCE_PILOT).name not in docmap:
        errors.append("documentation map does not route Evidence Pilot")
    if "PILOT_RECOMMENDATION / NOT_CANON" not in docmap:
        errors.append("documentation map does not preserve Pilot non-canon boundary")
    if pathlib.PurePosixPath(LIFECYCLE_REGISTRY).name not in docmap:
        errors.append("documentation map does not route lifecycle registry")
    if pathlib.PurePosixPath(CURRENT_GDD).name not in docmap:
        errors.append("documentation map does not route current GDD")

    if "current_branch: main" not in active_context:
        errors.append("ACTIVE_CONTEXT missing current_branch: main")
    if f"current_main: {DYNAMIC_CURRENT_REF}" not in active_context or has_fixed_sha_field(
        active_context, "current_main"
    ):
        errors.append("ACTIVE_CONTEXT current_main must resolve dynamically")
    if f"context_baseline_commit: {DYNAMIC_CURRENT_REF}" not in active_context or has_fixed_sha_field(
        active_context, "context_baseline_commit"
    ):
        errors.append("ACTIVE_CONTEXT context_baseline_commit must resolve dynamically")
    if "current_branch_and_commit" in active_context:
        errors.append("ACTIVE_CONTEXT restored forbidden self-referential branch/commit field")
    if DYNAMIC_CURRENT_REF not in policy:
        errors.append("dynamic current-main policy missing repository-default resolution")

    if "[대체됨]" not in legacy_gdd:
        errors.append("legacy GDD missing [대체됨] lifecycle marker")
    if "CURRENT_GDD_CANON" not in current_gdd:
        errors.append("current GDD missing current authority marker")

    for marker in LEGACY_CORE_MARKERS:
        if marker in core:
            errors.append(f"PROJECT_CORE contains forbidden legacy core marker: {marker}")

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
        CURRENT_GDD,
        CURRENT_SPEC,
        CURRENT_REVIEW,
        CURRENT_CORE_REVIEW,
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
        print("OMENWARD current documentation validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("OMENWARD current documentation validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
