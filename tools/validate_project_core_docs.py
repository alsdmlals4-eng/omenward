#!/usr/bin/env python3
"""Validate OMENWARD current v4.8 documentation and historical compatibility boundaries."""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

CURRENT_CONTRACT = "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8"
HISTORICAL_PLANNING_GATE = "IMPLEMENTATION_AUTHORITY_REQUIRED"
CURRENT_REACTIVATION_GATE = "USER_EXPLICIT_NEXT_P0_ASSET_SCOPE_APPROVAL"
CURRENT_IMPLEMENTATION_AUTHORITY = "SCOPED_APPROVED"
CURRENT_SPEC = "docs/CURRENT_CONFIRMED_DECISIONS.md"
CURRENT_REVIEW = "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"
FINAL_REVIEW = "docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md"
FINAL_REVIEW_ID = "OMW-REV-20260824-FINAL-PLANNING-ADVERSARIAL-DRIFT-01"
CURRENT_GDD = "docs/OMENWARD_GDD_CURRENT_CANON.md"
LIFECYCLE_REGISTRY = "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
EVIDENCE_PILOT = "docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md"
LEDGER = "docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md"
LEGENDARY_DEPLOYMENT_POLICY = "docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md"
ROULETTE_RULES = "docs/design/APPROVED_ROULETTE_CORE_RULES.md"
HISTORICAL_VERTICAL_SLICE = "docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md"
TOPDOWN_LAYOUT = "docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md"
TOPDOWN_SILHOUETTE = "docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md"
NORTH_STAR_AUDIT = "docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md"
NORTH_STAR_AUDIT_ID = "OMW-PLAN-20260824-NORTH-STAR-V2-1-AUDIT-01"
CURRENT_VISUAL_DECISION_ID = "OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01"
CURRENT_VISUAL_SPEC = "docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md"
CURRENT_VISUAL_ASSET = "docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md"
CURRENT_VISUAL_HANDOFF = "docs/handoffs/2026-08-26-gpt-work-image-production-handoff.md"
CURRENT_UNIT_ANIMATION_CONTRACT = "docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md"
IMPLEMENTATION_PACKET = "docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md"
IMPLEMENTATION_PLAN = "docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md"
STALE_NORTH_STAR_GATE = "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST"
STALE_FINAL_REVIEW_GATE = "CURRENT_NEXT = FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK"
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
    CURRENT_VISUAL_SPEC,
    CURRENT_VISUAL_ASSET,
    CURRENT_VISUAL_HANDOFF,
    CURRENT_UNIT_ANIMATION_CONTRACT,
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/DECISIONS_PENDING.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    TOPDOWN_LAYOUT,
    TOPDOWN_SILHOUETTE,
    NORTH_STAR_AUDIT,
    FINAL_REVIEW,
    IMPLEMENTATION_PACKET,
    IMPLEMENTATION_PLAN,
    HISTORICAL_VERTICAL_SLICE,
    CURRENT_REVIEW,
    EVIDENCE_PILOT,
    LEDGER,
    LEGENDARY_DEPLOYMENT_POLICY,
    ROULETTE_RULES,
)

# Volatile current state is owned by CURRENT_SPEC + ACTIVE_CONTEXT + HANDOFF.
# Older detailed documents remain required as durable/history inputs, but their
# superseded visual literals cannot override the 2026-08-25 current Decision.
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
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/DECISIONS_PENDING.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
)

FORBIDDEN_CURRENT_MARKERS = (
    "PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY",
    "PAUSED_PENDING_USER_REFERENCE_FILES",
    "current_next_gate: WORLD_CONFLICT_AND_CORE_STORY",
    "current_next_gate: ROULETTE_DDD_FEEDBACK_SPEC",
    STALE_NORTH_STAR_GATE,
    STALE_FINAL_REVIEW_GATE,
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


def validate_decision_count(errors: list[str], decisions: str) -> None:
    declared_match = re.search(r"CURRENT_APPROVED_REPLAN_DECISIONS\s*=\s*(\d+)", decisions)
    if not declared_match:
        errors.append("current decision index missing declared decision count")
        return
    registered = set(re.findall(r"\| `(OMW-PLAN-[^`]+)` \|", decisions))
    declared = int(declared_match.group(1))
    if declared != len(registered):
        errors.append(f"decision count mismatch: declared {declared}, registered {len(registered)}")


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
            CURRENT_CONTRACT,
            NORTH_STAR_AUDIT_ID,
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            CURRENT_VISUAL_DECISION_ID,
            CURRENT_VISUAL_SPEC,
            CURRENT_VISUAL_ASSET,
            "CURRENT_APPROVED_REPLAN_DECISIONS = 21",
            "OMW-PLAN-20260826-UNIT-ANIMATION-PRODUCTION-CONTRACT-01",
            CURRENT_UNIT_ANIMATION_CONTRACT,
            "OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01",
            "OMW-PLAN-20260820-CONTENT-BOSS-ARC-01",
            "OMW-PLAN-20260820-BALANCE-BUDGET-01",
            "OMW-PLAN-20260820-TEXT-UX-STATE-01",
            "OMW-PLAN-20260820-ROULETTE-DDD-FEEDBACK-01",
            "OMW-PLAN-20260820-TOPDOWN-BATTLEFIELD-LAYOUT-01",
            "OMW-PLAN-20260820-TOPDOWN-UNIT-SILHOUETTE-01",
            "VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION",
            "PER_FRONT_MINIMAP = REQUIRED",
            "APPROVED_VISUAL = OM-IMG-023",
            "PROJECT_STATE = PAUSED_AT_P0_ASSET_COVERAGE_DECISION_GATE",
            f"CURRENT_NEXT = {CURRENT_REACTIVATION_GATE}",
            f"IMPLEMENTATION_AUTHORITY = {CURRENT_IMPLEMENTATION_AUTHORITY}",
            IMPLEMENTATION_PACKET,
            IMPLEMENTATION_PLAN,
            "RUNTIME_EVIDENCE = NOT_RUN",
            "HUMAN_EVIDENCE = NOT_RUN",
            "IMAGE_GENERATION = USER_REQUEST_ONLY",
        ),
        "current decision index",
    )
    validate_decision_count(errors, decisions)

    agents = read(root, "AGENTS.md")
    require(
        errors,
        agents,
        (
            CURRENT_CONTRACT,
            "implementation_authorized: RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT",
            "IMPLEMENTATION_START = RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT",
            "CURRENT_ROUTE = RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT",
            CURRENT_VISUAL_DECISION_ID,
            "PER_FRONT_MINIMAP = REQUIRED",
            "VISUAL_GENERATION = USER_REQUEST_ONLY",
        ),
        "AGENTS",
    )

    active = read(root, "docs/ACTIVE_CONTEXT.md")
    require(
        errors,
        active,
        (
            CURRENT_CONTRACT,
            "status: PAUSED_AT_P0_ASSET_COVERAGE_DECISION_GATE",
            "CURRENT_APPROVED_REPLAN_DECISIONS = 21",
            CURRENT_VISUAL_DECISION_ID,
            "APPROVED_VISUAL_OM_IMG_023 = USER_APPROVED_CURRENT",
            "NOTION_CURRENT_VISUAL_IMAGE = SERVER_READBACK_PASS",
            "implementation_authorized: true",
            "implementation_scope: RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE_ONLY",
            "implementation_execution: NOT_RESUMED_IN_VISUAL_CLOSEOUT",
            f"CURRENT_NEXT = {CURRENT_REACTIVATION_GATE}",
            "CURRENT_GODOT_RUNTIME = NOT_RUN",
            "CURRENT_GUT_RED = NOT_RUN",
            "CURRENT_GUT_GREEN = NOT_RUN",
            "CURRENT_HERA_LIVE_QA = NOT_RUN",
            "CURRENT_MINIMAP_READABILITY = NOT_RUN",
            "CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN",
            "CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN",
            "CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN",
            "IMAGE_GENERATION = USER_REQUEST_ONLY",
        ),
        "Active Context",
    )
    if "current_branch_and_commit:" in active:
        errors.append("Active Context contains self-referential current_branch_and_commit")
    for field in ("current_main", "context_baseline_commit"):
        match = re.search(rf"(?m)^{field}:\s*([^\n]+)$", active)
        if match and re.fullmatch(r"[0-9a-f]{40}", match.group(1).strip(" `")):
            errors.append(f"{field} must resolve dynamically")

    packet = read(root, IMPLEMENTATION_PACKET)
    require(
        errors,
        packet,
        (
            "packet_id: OMW-EXEC-20260824-RUN-COMMAND-VERTICAL-SLICE-01",
            "status: APPROVED_FOR_EXECUTION",
            "approved_by_user: true",
            "architecture: ORCHESTRATION_FIRST_VERTICAL_SLICE",
            "implementation_authority: HIGODOT_SINGLE_PERSISTENT_AUTHORING_AUTHORITY",
            "PRODUCT_RUNTIME_IMPLEMENTATION: NOT_RUN",
            "GUT_RED: NOT_RUN",
            "GUT_GREEN: NOT_RUN",
            "HERA_LIVE_QA: NOT_RUN",
            "HUMAN_VALIDATION: NOT_RUN",
        ),
        "implementation packet",
    )
    plan = read(root, IMPLEMENTATION_PLAN)
    require(
        errors,
        plan,
        (
            "OMENWARD Run Command Vertical Slice Implementation Plan",
            "orchestration-first",
            "HiGodot",
            "GUT",
            "PREPARE",
            "COMMIT",
            "BATTLE",
            "REVIEW",
        ),
        "implementation plan",
    )

    visual_spec = read(root, CURRENT_VISUAL_SPEC)
    require(
        errors,
        visual_spec,
        (
            CURRENT_VISUAL_DECISION_ID,
            "status: USER_APPROVED_CURRENT",
            "BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS",
            "PER_FRONT_MINIMAP = REQUIRED",
            "VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION",
            "COMMANDER_SILHOUETTE = LONG_COMMAND_FLAG",
            "ADVERSARIAL_FULL_LOOP_COUNT = 5",
            "RUNTIME_AND_HUMAN_EVIDENCE = NOT_RUN",
        ),
        "current visual spec",
    )

    visual_asset = read(root, CURRENT_VISUAL_ASSET)
    require(
        errors,
        visual_asset,
        (
            "asset_id: OM-IMG-023",
            f"decision_id: {CURRENT_VISUAL_DECISION_ID}",
            "status: USER_APPROVED_CURRENT",
            "source_dimensions: 1536x1024",
            "source_sha256: 0326b012d1fbefba85b545086b84992051591edff6f3b7e159cf3e083f204224",
            "runtime_readability: NOT_RUN",
            "human_usability: NOT_RUN",
            "rights_review: NOT_RUN",
        ),
        "current visual asset record",
    )

    visual_handoff = read(root, CURRENT_VISUAL_HANDOFF)
    require(
        errors,
        visual_handoff,
        (
            "current_gate: NEXT_P0_ASSET_SCOPE_APPROVAL",
            "current_image_package_status: P0_UNITS_BUILDINGS_CLEANUP_MASTERS_EXPORTED",
            "image_generation: USER_REQUEST_ONLY",
            "codex_godot_execution: BLOCKED_UNTIL_ALL_B_SCOPE_ASSETS_USER_APPROVED_CLEANED_EXPORTED_AND_IMPLEMENTATION_READY",
        ),
        "current visual closeout handoff",
    )

    # Current summary documents moved to the 2026-08-25 visual authority. Older
    # detailed documents below remain required as durable/history inputs, but their
    # superseded visual literals cannot override these current summaries.
    core = read(root, "docs/PROJECT_CORE.md")
    require(
        errors,
        core,
        (
            CURRENT_CONTRACT,
            "current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md",
            "VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상",
            "RUN_HISTORY_RESET = FALSE",
            "PREPARE -> COMMIT -> BATTLE -> REVIEW",
            "NORTH_STAR_V2_1 = REFERENCE_ONLY_AFTER_2026_08_25",
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "NOTION_CURRENT_VISUAL_IMAGE = SERVER_READBACK_PASS",
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
            CURRENT_CONTRACT,
            "CURRENT_CONFIRMED_REPLAN_DECISIONS = 21",
            "NORTH_STAR_V2_1 = REFERENCE_ONLY_AFTER_2026_08_25",
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "NOTION_CURRENT_VISUAL_IMAGE = SERVER_READBACK_PASS",
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
            CURRENT_CONTRACT,
            "VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상",
            "RUN_HISTORY_RESET = FALSE",
            "NORTH_STAR_V2_1 = REFERENCE_ONLY_AFTER_2026_08_25",
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "NOTION_CURRENT_VISUAL_IMAGE = SERVER_READBACK_PASS",
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

    doc_map = read(root, "docs/DOCUMENTATION_MAP.md")
    require(
        errors,
        doc_map,
        (
            CURRENT_CONTRACT,
            "docs/CURRENT_CONFIRMED_DECISIONS.md",
            "APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md",
            "APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md",
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY",
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
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
            CURRENT_CONTRACT,
            "APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md",
            "APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md",
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY",
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
            "USER_REQUEST_ONLY",
            "[증거/호환] docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md",
        ),
        "lifecycle registry",
    )

    roadmap = read(root, "docs/OMENWARD_ROADMAP.md")
    require(
        errors,
        roadmap,
        (
            CURRENT_CONTRACT,
            "NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY",
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
            "USER_REQUEST_ONLY",
            "TOPDOWN_BATTLEFIELD_LAYOUT",
            "TOPDOWN_UNIT_SILHOUETTE",
        ),
        "roadmap",
    )

    pending = read(root, "docs/DECISIONS_PENDING.md")
    require(
        errors,
        pending,
        (
            CURRENT_CONTRACT,
            "ECONOMY_BASELINE_DRIFT",
            "NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY",
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
        ),
        "pending decisions",
    )
    for stale in ("WORLD_CONFLICT_AND_CORE_STORY", "20_STAGE_CONTENT_AND_BOSS_STRUCTURE", "TEXT_UX_AND_STATE_TRANSITION_SPEC"):
        if f"NEXT_PRODUCT_DECISION = {stale}" in pending:
            errors.append(f"pending decisions routes a completed planning gate as next: {stale}")

    handoff = read(root, "docs/HANDOFF_CONTEXT.md")
    require(
        errors,
        handoff,
        (
            CURRENT_CONTRACT,
            "current_gate: NEXT_P0_ASSET_SCOPE_APPROVAL",
            "current_image_package_status: P0_UNITS_BUILDINGS_CLEANUP_MASTERS_EXPORTED",
            "image_generation: USER_REQUEST_ONLY",
            "runtime_validation: NOT_RUN",
            "human_player_evidence: NOT_RUN",
            "codex_godot_execution: BLOCKED_UNTIL_ALL_B_SCOPE_ASSETS_USER_APPROVED_CLEANED_EXPORTED_AND_IMPLEMENTATION_READY",
        ),
        "handoff",
    )
    for stale in ("PHASE_C_ISSUE176_PROJECT_BOOT_SIGNAL11_ISOLATION", "DISPOSABLE_AUTOLOAD_AB_ISOLATION", "PR175 = OPEN_DRAFT"):
        if stale in handoff:
            errors.append(f"current handoff retains historical runtime routing: {stale}")

    onboarding = read(root, "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md")
    require(
        errors,
        onboarding,
        (
            "status: CURRENT_ONBOARDING_AUTHORITY",
            CURRENT_CONTRACT,
            "current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md",
            "USER_REQUEST_ONLY",
        ),
        "onboarding authority",
    )

    ledger_current = read(root, "docs/PROJECT_CANON_DECISION_LEDGER.md")
    require(
        errors,
        ledger_current,
        (
            CURRENT_CONTRACT,
            "CURRENT_APPROVED_REPLAN_DECISIONS = 19",
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY",
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
            "USER_REQUEST_ONLY",
        ),
        "current decision ledger",
    )

    # The North Star audit and final planning review are historical records of
    # the state before later visual/implementation approvals. Their authority
    # markers remain unchanged rather than being rewritten as current state.
    audit = read(root, NORTH_STAR_AUDIT)
    require(
        errors,
        audit,
        (
            NORTH_STAR_AUDIT_ID,
            "status: APPROVED_CURRENT",
            CURRENT_CONTRACT,
            "BATTLEFIELD_COMPOSITION = APPROVED_DIRECTION",
            "LOWER_CONTROL_DECK_LAYOUT = NEEDS_CORRECTION",
            "ROULETTE_INTERACTION_SURFACE = NEEDS_CORRECTION",
            "EXACT_TEXT_VALUES_MICROLAYOUT = NON_CANON_REFERENCE",
            "IMPLEMENTATION_AUTHORIZED = FALSE",
        ),
        "North Star audit",
    )

    final_review = read(root, FINAL_REVIEW)
    require(
        errors,
        final_review,
        (
            FINAL_REVIEW_ID,
            "status: PASS_5_OF_5",
            CURRENT_CONTRACT,
            "ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
            "NEW_PRODUCT_DECISION_REQUIRED = FALSE",
            "PLANNING_BLOCKER = NONE",
            f"CURRENT_NEXT = {HISTORICAL_PLANNING_GATE}",
            "IMPLEMENTATION_AUTHORITY = NONE",
            "CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY",
            "CURRENT_GODOT_RUNTIME = NOT_RUN",
            "CURRENT_WINDOWS_RUNTIME = NOT_RUN",
            "CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN",
            "CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN",
        ),
        "final planning review",
    )

    for relative in CURRENT_ROUTE_FILES:
        body = read(root, relative)
        if CURRENT_CONTRACT not in body:
            errors.append(f"current route missing v4.8 planning contract: {relative}")
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
