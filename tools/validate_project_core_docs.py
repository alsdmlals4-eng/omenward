#!/usr/bin/env python3
"""Validate OMENWARD current v4.7 documentation and historical compatibility boundaries."""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

CURRENT_SPEC = "docs/CURRENT_CONFIRMED_DECISIONS.md"
CURRENT_REVIEW = "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"
CURRENT_GDD = "docs/OMENWARD_GDD_CURRENT_CANON.md"
LIFECYCLE_REGISTRY = "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
EVIDENCE_PILOT = "docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md"
LEDGER = "docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md"
LEGENDARY_DEPLOYMENT_POLICY = "docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md"
ROULETTE_RULES = "docs/design/APPROVED_ROULETTE_CORE_RULES.md"
HISTORICAL_VERTICAL_SLICE = "docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md"
TOPDOWN_LAYOUT = "docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md"
TOPDOWN_SILHOUETTE = "docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md"
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
    CURRENT_SPEC,
    CURRENT_GDD,
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    TOPDOWN_LAYOUT,
    TOPDOWN_SILHOUETTE,
    HISTORICAL_VERTICAL_SLICE,
    CURRENT_REVIEW,
    EVIDENCE_PILOT,
    LEDGER,
    LEGENDARY_DEPLOYMENT_POLICY,
    ROULETTE_RULES,
)

CURRENT_ROUTE_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    LIFECYCLE_REGISTRY,
    CURRENT_SPEC,
    CURRENT_GDD,
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
)

FORBIDDEN_CURRENT_MARKERS = (
    "PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY",
    "PAUSED_PENDING_USER_REFERENCE_FILES",
    "current_next_gate: WORLD_CONFLICT_AND_CORE_STORY",
    "current_next_gate: ROULETTE_DDD_FEEDBACK_SPEC",
)


def read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def require(errors: list[str], body: str, markers: tuple[str, ...], label: str) -> None:
    for marker in markers:
        if marker not in body:
            errors.append(f"{label} missing current contract marker: {marker}")


def validate_links(errors: list[str], root: pathlib.Path, relative: str, body: str) -> None:
    source = root / relative
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0].strip()
        if not clean:
            continue
        candidates = ((source.parent / clean).resolve(), (root / clean).resolve())
        if not any(candidate.exists() for candidate in candidates):
            errors.append(f"broken local link: {relative} -> {clean}")


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if errors:
        return errors

    decisions = read(root, CURRENT_SPEC)
    require(
        errors,
        decisions,
        (
            "status: CURRENT_DECISION_RECOVERY_INDEX",
            "CURRENT_APPROVED_REPLAN_DECISIONS = 18",
            "OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01",
            "OMW-PLAN-20260820-CONTENT-BOSS-ARC-01",
            "OMW-PLAN-20260820-BALANCE-BUDGET-01",
            "OMW-PLAN-20260820-TEXT-UX-STATE-01",
            "OMW-PLAN-20260820-ROULETTE-DDD-FEEDBACK-01",
            "OMW-PLAN-20260820-TOPDOWN-BATTLEFIELD-LAYOUT-01",
            "OMW-PLAN-20260820-TOPDOWN-UNIT-SILHOUETTE-01",
            "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST",
            "USER_REQUEST_ONLY",
        ),
        "current decision index",
    )

    core = read(root, "docs/PROJECT_CORE.md")
    require(
        errors,
        core,
        (
            "current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md",
            "VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상",
            "RUN_HISTORY_RESET = FALSE",
            "PREPARE -> COMMIT -> BATTLE -> REVIEW",
            "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST",
            "USER_REQUEST_ONLY",
            "CURRENT_GODOT_RUNTIME = NOT_RUN",
            "LEGACY_C1_C2_C3_PROVEN",
        ),
        "Project Core",
    )
    for marker in ("storage_selling_food", "구형 전술 자원: 마석"):
        if marker in core:
            errors.append(f"Project Core contains legacy core marker: {marker}")

    status = read(root, "docs/CURRENT_IMPLEMENTATION_STATUS.md")
    require(
        errors,
        status,
        (
            "CURRENT_CONFIRMED_REPLAN_DECISIONS = 18",
            "CURRENT_GODOT_RUNTIME = NOT_RUN",
            "CURRENT_WINDOWS_RUNTIME = NOT_RUN",
            "CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN",
            "LEGACY_C1_C2_C3_PROVEN",
        ),
        "current implementation status",
    )
    for exact_history in ("C1 구현 검증 head:", "C1 최종 검증 run:", "C2 최종 검증 run:"):
        if exact_history in status:
            errors.append(f"current implementation status embeds exact historical proof: {exact_history}")

    gdd = read(root, CURRENT_GDD)
    require(
        errors,
        gdd,
        (
            "status: CURRENT_GDD_CANON",
            "VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상",
            "RUN_HISTORY_RESET = FALSE",
            "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST",
            "USER_REQUEST_ONLY",
            "CURRENT_GODOT_RUNTIME = NOT_RUN",
        ),
        "current GDD",
    )
    for stale in (
        "CAUSE_OF_OMEN_CYCLE = USER_DECISION_REQUIRED",
        "HIGH_LEVEL_ENEMY_OR_VEIL_IDENTITY = USER_DECISION_REQUIRED",
        "STAGE_20_NARRATIVE_RESOLUTION = USER_DECISION_REQUIRED",
    ):
        if stale in gdd:
            errors.append(f"current GDD retains superseded world decision: {stale}")

    active = read(root, "docs/ACTIVE_CONTEXT.md")
    require(errors, active, ("CURRENT_APPROVED_REPLAN_DECISIONS = 18", "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST", "USER_REQUEST_ONLY"), "Active Context")
    if "current_branch_and_commit:" in active:
        errors.append("Active Context contains self-referential current_branch_and_commit")
    for field in ("current_main", "context_baseline_commit"):
        match = re.search(rf"(?m)^{field}:\s*([^\n]+)$", active)
        if match and re.fullmatch(r"[0-9a-f]{40}", match.group(1).strip(" `")):
            errors.append(f"{field} must resolve dynamically")

    doc_map = read(root, "docs/DOCUMENTATION_MAP.md")
    require(
        errors,
        doc_map,
        (
            "docs/CURRENT_CONFIRMED_DECISIONS.md",
            "APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md",
            "APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md",
            "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST",
            "USER_REQUEST_ONLY",
            "Google Sheet는 current human authority가 아니다",
        ),
        "Documentation Map",
    )

    lifecycle = read(root, LIFECYCLE_REGISTRY)
    require(
        errors,
        lifecycle,
        (
            "APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md",
            "APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md",
            "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST",
            "USER_REQUEST_ONLY",
            "[증거/호환] docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md",
        ),
        "lifecycle registry",
    )

    roadmap = read(root, "docs/OMENWARD_ROADMAP.md")
    require(errors, roadmap, ("REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST", "USER_REQUEST_ONLY", "TOPDOWN_BATTLEFIELD_LAYOUT", "TOPDOWN_UNIT_SILHOUETTE"), "roadmap")

    pending = read(root, "docs/DECISIONS_PENDING.md")
    require(errors, pending, ("ECONOMY_BASELINE_DRIFT", "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST", "IMPLEMENTATION_AUTHORITY_REQUIRED"), "pending decisions")
    for stale in ("WORLD_CONFLICT_AND_CORE_STORY", "20_STAGE_CONTENT_AND_BOSS_STRUCTURE", "TEXT_UX_AND_STATE_TRANSITION_SPEC"):
        if f"NEXT_PRODUCT_DECISION = {stale}" in pending:
            errors.append(f"pending decisions routes a completed planning gate as next: {stale}")

    handoff = read(root, "docs/HANDOFF_CONTEXT.md")
    require(errors, handoff, ("PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7", "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST", "USER_REQUEST_ONLY", "CURRENT_GODOT_RUNTIME = NOT_RUN"), "handoff")
    for stale in ("PHASE_C_ISSUE176_PROJECT_BOOT_SIGNAL11_ISOLATION", "DISPOSABLE_AUTOLOAD_AB_ISOLATION", "PR175 = OPEN_DRAFT"):
        if stale in handoff:
            errors.append(f"current handoff retains historical runtime routing: {stale}")

    for relative in CURRENT_ROUTE_FILES:
        body = read(root, relative)
        for marker in FORBIDDEN_CURRENT_MARKERS:
            if marker in body:
                errors.append(f"current route contains stale marker: {relative} -> {marker}")
        validate_links(errors, root, relative, body)

    legacy_gdd = read(root, "docs/OMENWARD_GAME_DESIGN.md")
    if "[대체됨]" not in legacy_gdd:
        errors.append("legacy GDD lacks superseded marker")

    pilot = read(root, EVIDENCE_PILOT)
    if "implementation_authority: NONE" not in pilot:
        errors.append("Evidence Pilot lost non-implementation boundary")

    # Historical files remain verifiable but are not current routing authority.
    historical_spec = read(root, HISTORICAL_VERTICAL_SLICE)
    if "USER_APPROVED_PLAN" not in historical_spec:
        errors.append("historical Vertical Slice contract lost provenance")
    if pathlib.PurePosixPath(HISTORICAL_VERTICAL_SLICE).name in core and "[증거/호환]" not in lifecycle:
        errors.append("historical Vertical Slice is exposed without compatibility classification")

    legendary = read(root, LEGENDARY_DEPLOYMENT_POLICY)
    if "COMMIT_TIME_REVALIDATION: REQUIRED" not in legendary:
        errors.append("legendary deployment contract lost commit-time revalidation")
    roulette = read(root, ROULETTE_RULES)
    if "노출 인덱스" not in roulette:
        errors.append("roulette horizontal movement contract lost exposure index")
    lineage = read(root, LEDGER)
    if "AUTHORED_PRIORITY_LIST" not in lineage:
        errors.append("V2 decision lineage lost AUTHORED_PRIORITY_LIST")

    for relative in ("README.md", "AGENTS.md", "docs/PROJECT_CORE.md", CURRENT_GDD):
        if "VERTICAL_SLICE_PROVEN" in read(root, relative):
            errors.append(f"premature completion claim in {relative}")

    validate_links(errors, root, EVIDENCE_PILOT, pilot)
    return errors


def main() -> int:
    errors = validate(ROOT)
    if errors:
        print("Project Core documentation validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Project Core documentation validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
