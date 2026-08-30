#!/usr/bin/env python3
"""Validate OMENWARD current v4.8 documentation and historical compatibility boundaries."""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

CURRENT_CONTRACT = "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8"
HISTORICAL_PLANNING_GATE = "IMPLEMENTATION_AUTHORITY_REQUIRED"
CURRENT_REACTIVATION_GATE = "PHASE2_STORYBOOK_REMAINING_UNIT_RUNTIME_ASSETS__ISSUE_256__SOURCE_SHEETS_GENERATED__TRUE_ALPHA_CELL_EXPORT_PENDING_REVIEW"
CURRENT_ACTIVITY = "FIRST5_FTUE_CORE_LOOP_RECONCILIATION__TERRAIN_AND_SHIELD_GUARD_PAIR_IMPLEMENTED__REMAINING_SOURCE_CELLS_PENDING_REVIEW"
CURRENT_IMAGE_POLICY = "USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES"
FORWARD_DEFENSE_SPEC = "docs/design/APPROVED_OMENWARD_FORWARD_DEFENSE_AND_OCCUPATION_NODE_CONTRACT_2026-08-28.md"
FORWARD_DEFENSE_DECISION_ID = "OMW-PLAN-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01"
GLOBAL_BUILDING_ROSTER_SPEC = "docs/design/APPROVED_OMENWARD_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOTS_2026-08-30.md"
GLOBAL_BUILDING_ROSTER_DECISION_ID = "OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01"
CURRENT_DECISION_COUNT = 28
BASE_FORWARD_LAYOUT_SPEC = "docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md"
BASE_FORWARD_LAYOUT_DECISION_ID = "OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01"
BASE_FORWARD_LAYOUT_REVIEW = "docs/reviews/ADVERSARIAL_OPEN_BATTLEFIELD_TOWER_ONLY_LAYOUT_REVIEW_2026-08-28.md"
REPOSITORY_ONLY_POLICY = "docs/process/APPROVED_OMENWARD_REPOSITORY_ONLY_CANON_AND_NOTION_RETIREMENT_2026-08-28.md"
REPOSITORY_ONLY_POLICY_ID = "OMW-OPS-20260828-REPOSITORY-ONLY-CANON-NOTION-RETIREMENT-01"
PROJECT_HOME = "docs/PROJECT_HOME.md"
NOTION_MIGRATION_REPORT = "docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md"
NOTION_MIGRATION_ID = "OMW-OPS-20260828-NOTION-CURRENT-CONTENT-TO-REPOSITORY-01"
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
CURRENT_VISUAL_DECISION_ID = "OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01"
CURRENT_MAP_TOPOLOGY = "MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT"
CURRENT_FRONT_STRUCTURE = "FRONT_STRUCTURE = ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT"
CURRENT_ROUTE_STATE_GRAMMAR = "ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE"
CURRENT_MAP_ONLY_BOARD_SCOPE = "PROJECT_CORE_SCENE_VISUAL_BOARD_SCOPE = STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED"
CURRENT_VISUAL_SPEC = "docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md"
CURRENT_VISUAL_BOARD = "docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md"
CURRENT_VISUAL_LOCK_PACKET = "docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md"
CURRENT_VISUAL_LOCK_REVIEW = "docs/reviews/ADVERSARIAL_OPEN_BATTLEFIELD_V6_VISUAL_LOCK_REVIEW_2026-08-29.md"
LEGACY_RUNTIME_VISUAL_ASSET = "docs/images/approved/OMENWARD_BATTLEFIELD_BACKDROP_V1.md"
# Compatibility export for mutation tests that validate the legacy runtime evidence.
CURRENT_VISUAL_ASSET = LEGACY_RUNTIME_VISUAL_ASSET
CURRENT_STORYBOOK_SHIELD_GUARD_PAIR = "docs/images/approved/OMENWARD_STORYBOOK_SD_SHIELD_GUARD_TRUE_ALPHA_PAIR_V1.md"
CURRENT_VISUAL_HANDOFF = "docs/HANDOFF_CONTEXT.md"
CURRENT_RESTART_HANDOFF = "docs/handoffs/2026-08-29-open-battlefield-v6-visual-lock-handoff.md"
CURRENT_UNIT_ANIMATION_CONTRACT = "docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md"
IMPLEMENTATION_PACKET = "docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md"
IMPLEMENTATION_PLAN = "docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md"
MACHINE_QA_RECORD = "docs/qa/OMENWARD_RUN_COMMAND_MACHINE_QA_2026-08-27.md"
STALE_NORTH_STAR_GATE = "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST"
STALE_FINAL_REVIEW_GATE = "CURRENT_NEXT = FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK"
DYNAMIC_CURRENT_REF = "RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH"

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    PROJECT_HOME,
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    LIFECYCLE_REGISTRY,
    CURRENT_SPEC,
    CURRENT_GDD,
    CURRENT_VISUAL_SPEC,
    CURRENT_VISUAL_BOARD,
    CURRENT_VISUAL_LOCK_PACKET,
    CURRENT_VISUAL_LOCK_REVIEW,
    CURRENT_VISUAL_ASSET,
    CURRENT_STORYBOOK_SHIELD_GUARD_PAIR,
    CURRENT_VISUAL_HANDOFF,
    CURRENT_RESTART_HANDOFF,
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
    MACHINE_QA_RECORD,
    HISTORICAL_VERTICAL_SLICE,
    CURRENT_REVIEW,
    EVIDENCE_PILOT,
    LEDGER,
    LEGENDARY_DEPLOYMENT_POLICY,
    ROULETTE_RULES,
    FORWARD_DEFENSE_SPEC,
    BASE_FORWARD_LAYOUT_SPEC,
    BASE_FORWARD_LAYOUT_REVIEW,
    REPOSITORY_ONLY_POLICY,
    NOTION_MIGRATION_REPORT,
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
    registered = set(re.findall(r"\| `(OMW-(?:PLAN|VISUAL)-[^`]+)` \|", decisions))
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
            CURRENT_VISUAL_BOARD,
            LEGACY_RUNTIME_VISUAL_ASSET,
            f"CURRENT_APPROVED_REPLAN_DECISIONS = {CURRENT_DECISION_COUNT}",
            FORWARD_DEFENSE_DECISION_ID,
            GLOBAL_BUILDING_ROSTER_SPEC,
            GLOBAL_BUILDING_ROSTER_DECISION_ID,
            GLOBAL_BUILDING_ROSTER_SPEC,
            BASE_FORWARD_LAYOUT_DECISION_ID,
            BASE_FORWARD_LAYOUT_SPEC,
            NOTION_MIGRATION_REPORT,
            "FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY",
            "FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL",
            "FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN",
            "OCCUPATION_SLOT_ACTIVATION = STABLE_PLAYER_HELD_FORWARD_BASE_OR_CLASH_ZONE_ONLY",
            "OMW-PLAN-20260826-UNIT-ANIMATION-PRODUCTION-CONTRACT-01",
            CURRENT_UNIT_ANIMATION_CONTRACT,
            "OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01",
            "OMW-PLAN-20260820-CONTENT-BOSS-ARC-01",
            "OMW-PLAN-20260820-BALANCE-BUDGET-01",
            "OMW-PLAN-20260820-TEXT-UX-STATE-01",
            "OMW-PLAN-20260820-ROULETTE-DDD-FEEDBACK-01",
            "OMW-PLAN-20260820-TOPDOWN-BATTLEFIELD-LAYOUT-01",
            "OMW-PLAN-20260820-TOPDOWN-UNIT-SILHOUETTE-01",
            "VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION",
            "BATTLEFIELD_PRESENTATION = ONE_SIMULTANEOUS_THREE_FRONT_STRATEGIC_MAP",
            CURRENT_MAP_TOPOLOGY,
            CURRENT_FRONT_STRUCTURE,
            CURRENT_ROUTE_STATE_GRAMMAR,
            CURRENT_MAP_ONLY_BOARD_SCOPE,
            "PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP",
            "CURRENT_TARGET_RUNTIME_ASSET = OMW-IMG-20260830-WIDE-CONNECTED-STRATEGIC-FRONT-TERRAIN-V1",
            "LEGACY_RUNTIME_BACKDROP = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1",
            "PROJECT_CORE_SCENE_VISUAL_BOARD = USER_CONFIRMED_PLANNING_LOCK__V6_OPEN_BATTLEFIELD_NO_BARRICADE__NOT_RUNTIME_ASSET",
            CURRENT_VISUAL_LOCK_PACKET,
            CURRENT_STORYBOOK_SHIELD_GUARD_PAIR,
            f"CURRENT_NEXT = {CURRENT_REACTIVATION_GATE}",
            f"IMPLEMENTATION_AUTHORITY = {CURRENT_IMPLEMENTATION_AUTHORITY}",
            IMPLEMENTATION_PACKET,
            IMPLEMENTATION_PLAN,
            "RUNTIME_EVIDENCE = PARTIAL__HEADLESS_CONTRACTS_AND_HERA_TECHNICAL_SMOKE_PLUS_THREE_RESOLUTION_CAPTURE",
            "HUMAN_EVIDENCE = NOT_RUN",
            f"IMAGE_GENERATION = {CURRENT_IMAGE_POLICY}",
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
            CURRENT_MAP_TOPOLOGY,
            CURRENT_FRONT_STRUCTURE,
            CURRENT_ROUTE_STATE_GRAMMAR,
            CURRENT_MAP_ONLY_BOARD_SCOPE,
            "PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP",
            f"VISUAL_GENERATION = {CURRENT_IMAGE_POLICY}",
        ),
        "AGENTS",
    )

    active = read(root, "docs/ACTIVE_CONTEXT.md")
    require(
        errors,
        active,
        (
            CURRENT_CONTRACT,
            f"status: {CURRENT_ACTIVITY}",
            f"CURRENT_APPROVED_REPLAN_DECISIONS = {CURRENT_DECISION_COUNT}",
            GLOBAL_BUILDING_ROSTER_DECISION_ID,
            GLOBAL_BUILDING_ROSTER_SPEC,
            BASE_FORWARD_LAYOUT_DECISION_ID,
            BASE_FORWARD_LAYOUT_SPEC,
            "FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY",
            "FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL",
            "OCCUPATION_SLOT_CAPACITY = 6_PLUS_STABLE_PLAYER_HELD_FORWARD_BASE_AND_CLASH_ZONE",
            "BUILDING_MAP_PLACEMENT = FORBIDDEN",
            "FIXED_TOWER_COUNT_PER_SHARED_FRONT = 1",
            CURRENT_VISUAL_DECISION_ID,
            CURRENT_VISUAL_LOCK_PACKET,
            CURRENT_MAP_TOPOLOGY,
            CURRENT_FRONT_STRUCTURE,
            CURRENT_ROUTE_STATE_GRAMMAR,
            CURRENT_MAP_ONLY_BOARD_SCOPE,
            "APPROVED_VISUAL_BATTLEFIELD_BACKDROP_V1 = LEGACY_RUNTIME_ASSET__CURRENT_BUILD_ONLY",
            "current_visual_asset: OMW-IMG-20260830-WIDE-CONNECTED-STRATEGIC-FRONT-TERRAIN-V1",
            "NOTION_CURRENT_VISUAL_IMAGE = HISTORICAL_SERVER_READBACK_ONLY__NO_FUTURE_WRITES",
            REPOSITORY_ONLY_POLICY,
            NOTION_MIGRATION_REPORT,
            "implementation_authorized: true",
            "implementation_scope: RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE",
            "implementation_execution: IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN",
            f"current_handoff: {CURRENT_RESTART_HANDOFF}",
            f"current_storybook_shield_guard_pair: {CURRENT_STORYBOOK_SHIELD_GUARD_PAIR}",
            f"CURRENT_NEXT = {CURRENT_REACTIVATION_GATE}",
            "CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED",
            "CURRENT_GUT_RED = NOT_RUN",
            "CURRENT_GUT_GREEN = NOT_RUN",
            "CURRENT_HERA_LIVE_QA = PARTIAL__RUN_COMMAND_PREPARE_TO_BATTLE_MOUSE_AND_UI_ACCEPT_KEYBOARD__DIAGNOSTICS_CLEAN",
            "CURRENT_MINIMAP_READABILITY = PARTIAL__THREE_RESOLUTION_TECHNICAL_CAPTURED__HUMAN_NOT_RUN",
            "CURRENT_SD_UNIT_RUNTIME_READABILITY = PARTIAL__ALL18_UNIT_GALLERY_NO_CLIPPING_SIGNAL",
            "CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN",
            "CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN",
            f"IMAGE_GENERATION = {CURRENT_IMAGE_POLICY}",
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

    machine_qa = read(root, MACHINE_QA_RECORD)
    require(
        errors,
        machine_qa,
        (
            "OMENWARD Run Command Machine QA · 2026-08-27",
            "d0f1742e8b65781ba6513c2cfe0e3f1f55da447e",
            "CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN",
            "CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN",
        ),
        "Run Command machine QA record",
    )

    visual_spec = read(root, CURRENT_VISUAL_SPEC)
    require(
        errors,
        visual_spec,
        (
            CURRENT_VISUAL_DECISION_ID,
            "status: USER_CONFIRMED_CURRENT",
            "VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION",
            "BATTLEFIELD_PRESENTATION = ONE_SIMULTANEOUS_THREE_FRONT_STRATEGIC_MAP",
            CURRENT_MAP_TOPOLOGY,
            CURRENT_FRONT_STRUCTURE,
            CURRENT_ROUTE_STATE_GRAMMAR,
            CURRENT_MAP_ONLY_BOARD_SCOPE,
            "PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP",
            "runtime_target_asset: NOT_CREATED",
            "PROJECT_CORE_SCENE_VISUAL_BOARD = GENERATED_EXPLORATION",
            "!= RUNTIME_ASSET",
            "Phase 2 entry criteria",
        ),
        "current visual spec",
    )

    visual_board = read(root, CURRENT_VISUAL_BOARD)
    require(
        errors,
        visual_board,
        (
            "board_id: OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01",
            CURRENT_VISUAL_DECISION_ID,
            "revision: v6__OPEN_BATTLEFIELD_NO_BARRICADE",
            "map_topology: ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT",
            "front_structure: ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT",
            "route_state_grammar: WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE",
            "board_scope: STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED",
            "roulette_system: RETAINED__NOT_VISUALIZED_IN_CURRENT_MAP_ONLY_BOARD",
            "OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v6_OPEN_BATTLEFIELD_NO_BARRICADE.png",
            "92A0922212ED62AAE30723FDFD97E13D61D37168F950A236104A2A1EB6F8D94D",
            "status: USER_CONFIRMED_PLANNING_LOCK__NOT_RUNTIME_ASSET",
            CURRENT_VISUAL_LOCK_PACKET,
            "rights_status: PLANNING_REFERENCE_ONLY__NOT_RUNTIME_ASSET__NOT_RELEASE_RIGHTS_PASS",
            "!= runtime asset batch",
            "no pseudo-text used as structured truth",
        ),
        "current visual planning board",
    )

    visual_asset = read(root, LEGACY_RUNTIME_VISUAL_ASSET)
    require(
        errors,
        visual_asset,
        (
            "asset_id: OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1",
            "status: LEGACY_RUNTIME_ASSET__CURRENT_BUILD_CONSUMER_ACTIVE",
            "dimensions: 1672x941",
            "sha256: DB80778C1EA0A7905EA938B902F94C06DC472EB00740C93E07A38CE6E4C86525",
            "runtime_readability: PARTIAL_TECHNICAL_HERA_CAPTURE__HUMAN_NOT_RUN",
            "human_evidence: NOT_RUN",
            "Generation runtime: OpenAI image generation",
        ),
        "legacy runtime visual asset record",
    )

    visual_handoff = read(root, CURRENT_VISUAL_HANDOFF)
    require(
        errors,
        visual_handoff,
        (
            f"current_gate: {CURRENT_REACTIVATION_GATE}",
            "current_image_package_status: P0_REMAINDER_SOURCES_AND_CLEANUP_MASTERS_STORED",
            f"image_generation: {CURRENT_IMAGE_POLICY}",
            "codex_godot_execution: IMPLEMENTED__WIDE_CONNECTED_TERRAIN_BOUND__MACHINE_QA__RUNTIME_NOT_RUN",
        ),
        "current visual closeout handoff",
    )

    restart_handoff = read(root, CURRENT_RESTART_HANDOFF)
    require(
        errors,
        restart_handoff,
        (
            "status: CURRENT_RESTART_ROUTER",
            CURRENT_CONTRACT,
            "notion_current_authority: RETIRED__NO_FUTURE_READ_OR_WRITE",
            BASE_FORWARD_LAYOUT_SPEC,
            CURRENT_VISUAL_BOARD,
            CURRENT_VISUAL_LOCK_PACKET,
            f"current_gate: {CURRENT_REACTIVATION_GATE}",
            "runtime: NOT_RUN",
            "human_usability: NOT_RUN",
        ),
        "base/forward restart handoff",
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
            "NORTH_STAR_V2_1 = HISTORICAL_REFERENCE_ONLY",
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "NOTION_CURRENT_VISUAL_IMAGE = HISTORICAL_SERVER_READBACK_ONLY__NO_FUTURE_WRITES",
            REPOSITORY_ONLY_POLICY,
            CURRENT_IMAGE_POLICY,
            "CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED",
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
            f"CURRENT_CONFIRMED_REPLAN_DECISIONS = {CURRENT_DECISION_COUNT}",
            "NORTH_STAR_V2_1 = HISTORICAL_REFERENCE_ONLY",
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "NOTION_CURRENT_VISUAL_IMAGE = HISTORICAL_SERVER_READBACK_ONLY__NO_FUTURE_WRITES",
            REPOSITORY_ONLY_POLICY,
            "CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED",
            GLOBAL_BUILDING_ROSTER_SPEC,
            "FORWARD_BASE_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY",
            "FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL",
            "GLOBAL_BUILDING_ROSTER = 6_PLUS_STABLE_PLAYER_HELD_FORWARD_BASE_AND_CLASH_ZONE",
            "BUILDING_MAP_PLACEMENT = FORBIDDEN",
            "FIXED_TOWER_COUNT_PER_SHARED_FRONT = 1",
            "CURRENT_WINDOWS_RUNTIME = PARTIAL__STANDALONE_TECHNICAL_CAPTURED_960_1280_1920",
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
            "NORTH_STAR_V2_1 = HISTORICAL_REFERENCE_ONLY",
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "NOTION_CURRENT_VISUAL_IMAGE = HISTORICAL_SERVER_READBACK_ONLY__NO_FUTURE_WRITES",
            REPOSITORY_ONLY_POLICY,
            CURRENT_IMAGE_POLICY,
            "CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED",
            GLOBAL_BUILDING_ROSTER_SPEC,
            "FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY",
            "FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL",
            "GLOBAL_BUILDING_ROSTER = 6_PLUS_STABLE_PLAYER_HELD_FORWARD_BASE_AND_CLASH_ZONE",
            "BUILDING_MAP_PLACEMENT = FORBIDDEN",
            "FIXED_TOWER_COUNT_PER_SHARED_FRONT = 1",
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

    forward_defense = read(root, FORWARD_DEFENSE_SPEC)
    require(
        errors,
        forward_defense,
        (
            FORWARD_DEFENSE_DECISION_ID,
            "status: PARTIALLY_SUPERSEDED__FIXED_FORWARD_BARRICADE_REMOVED__TOWER_AND_OCCUPATION_NODE_RETAINED",
            "FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY",
            "FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL",
            "TACTICAL_COMMAND_BARRICADE = OUT_OF_SCOPE__RETAINED",
            "OCCUPATION_NODE_ACTIVATION = STABLE_PLAYER_OWNED_OUTPOST_ONLY",
            "CONSTRUCTION_NODE_DURING_CAPTURE = LOCKED",
            "PLAYER_BUILT_EFFECTS_AFTER_HOSTILE_CAPTURE = RUINED",
            "FIXED_DEFENSE_SOLO_CLEAR = FORBIDDEN",
            "FORWARD_DEFENSE_RUNTIME = NOT_IMPLEMENTED",
            "NO_BASE_PROMOTION = PROJECT_SPECIFIC_MAPRUN_FRONT_AND_OUTPOST_RULES",
        ),
        "forward-defense / occupation-node contract",
    )

    base_forward_layout = read(root, BASE_FORWARD_LAYOUT_SPEC)
    require(
        errors,
        base_forward_layout,
        (
            BASE_FORWARD_LAYOUT_DECISION_ID,
            "status: CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED",
            "HOME_BASE_PREBUILT_PRODUCTION_BUILDINGS = NONE",
            "HOME_BASE_CONSTRUCTION_NODE_COUNT_PER_FACTION = 4",
            "HOME_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_FACTION = 2",
            "FORWARD_BASE_CONSTRUCTION_NODE_COUNT_PER_BASE = 2",
            "FORWARD_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_BASE = 1",
            "FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY",
            "FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL",
            "FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN",
            "BUILD_PLACEMENT_FREEDOM = DISCOVERABLE_FIXED_PADS_IN_OPEN_TERRAIN__NOT_FREEFORM_TERRAIN_GRID",
            "TOTAL_CONSTRUCTION_NODE_CAPACITY_PER_FACTION = 10",
            "PHASE_2_PRODUCT_CODE_AUTHORITY = NONE",
        ),
        "open-battlefield tower-only layout contract",
    )

    base_forward_layout_review = read(root, BASE_FORWARD_LAYOUT_REVIEW)
    require(
        errors,
        base_forward_layout_review,
        (
            "review_id: OMW-REV-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01",
            "result: PASS_5_OF_5__PLANNING_SCOPE_ONLY",
            BASE_FORWARD_LAYOUT_DECISION_ID,
            "runtime: NOT_RUN",
            "human_usability: NOT_RUN",
            "player_experience: NOT_RUN",
            "visual_lock: USER_CONFIRM_PENDING",
            "NO_BASE_PROMOTION = PROJECT_SPECIFIC_THREE_FRONT_OCCUPATION_AND_FIXED_PAD_LAYOUT",
        ),
        "open-battlefield tower-only layout adversarial review",
    )

    visual_lock_packet = read(root, CURRENT_VISUAL_LOCK_PACKET)
    require(
        errors,
        visual_lock_packet,
        (
            "packet_id: OMW-VISUAL-LOCK-20260829-OPEN-BATTLEFIELD-V6-01",
            CURRENT_VISUAL_DECISION_ID,
            BASE_FORWARD_LAYOUT_DECISION_ID,
            "status: USER_CONFIRMED_CURRENT__PLANNING_LOCKED__NOT_RUNTIME_IMPLEMENTED",
            "USER_CONFIRMED_IN_CHAT",
            "FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL",
            "FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN",
            "runtime: NOT_RUN",
            "human_usability: NOT_RUN",
            "player_experience: NOT_RUN",
            f"NEXT_GATE = {CURRENT_REACTIVATION_GATE}",
        ),
        "open-battlefield v6 visual direction lock packet",
    )

    visual_lock_review = read(root, CURRENT_VISUAL_LOCK_REVIEW)
    require(
        errors,
        visual_lock_review,
        (
            "review_id: OMW-REV-20260829-OPEN-BATTLEFIELD-V6-VISUAL-LOCK-01",
            "result: PASS_5_OF_5__PLANNING_LOCK_SCOPE_ONLY",
            "runtime: NOT_RUN",
            "human_usability: NOT_RUN",
            "player_experience: NOT_RUN",
            "rights_review: NOT_RUN",
        ),
        "open-battlefield v6 visual lock adversarial review",
    )

    repository_only = read(root, REPOSITORY_ONLY_POLICY)
    require(
        errors,
        repository_only,
        (
            REPOSITORY_ONLY_POLICY_ID,
            "REPOSITORY_HUMAN_FACING_CANON = Markdown owners under docs/ + README.md",
            "NOTION_CURRENT_AUTHORITY = RETIRED",
            "NOTION_FUTURE_READ_OR_WRITE = FORBIDDEN_UNTIL_USER_REENABLES",
            "NOTION_DESTINATION_READBACK = NOT_REQUIRED",
            "NOTION_MIGRATION_READ = COMPLETE__USER_APPROVED_READ_ONLY",
            NOTION_MIGRATION_REPORT,
        ),
        "repository-only canon policy",
    )

    project_home = read(root, PROJECT_HOME)
    require(
        errors,
        project_home,
        (
            "status: CURRENT_REPOSITORY_PROJECT_HOME",
            NOTION_MIGRATION_REPORT,
            "FORWARD_DEFENSE_OCCUPATION_NODES = SUPERSEDED_IN_SCOPE__GLOBAL_ROSTER_IMPLEMENTED__MACHINE_VERIFIED",
            "HUMAN_USABILITY_AND_PLAYER_EXPERIENCE = NOT_RUN",
        ),
        "repository Project Home",
    )

    notion_migration = read(root, NOTION_MIGRATION_REPORT)
    require(
        errors,
        notion_migration,
        (
            NOTION_MIGRATION_ID,
            "authority_after_migration: REPOSITORY_ONLY",
            "notion_access: USER_APPROVED_READ_ONLY__NO_WRITE_OR_DELETE",
            "NOTION_WRITE_OR_DELETE = NOT_PERFORMED",
            "MIGRATED_AND_CORRECTED",
            "HISTORICAL_OR_SUPERSEDED__NOT_COPIED_AS_CURRENT",
        ),
        "Notion current-content migration report",
    )

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
            CURRENT_IMAGE_POLICY,
            GLOBAL_BUILDING_ROSTER_SPEC,
            REPOSITORY_ONLY_POLICY,
            PROJECT_HOME,
            NOTION_MIGRATION_REPORT,
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
            CURRENT_IMAGE_POLICY,
            GLOBAL_BUILDING_ROSTER_SPEC,
            REPOSITORY_ONLY_POLICY,
            "[증거/호환] docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md",
            f"[증거] {MACHINE_QA_RECORD}",
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
            CURRENT_IMAGE_POLICY,
            GLOBAL_BUILDING_ROSTER_SPEC,
            REPOSITORY_ONLY_POLICY,
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
            f"current_gate: {CURRENT_REACTIVATION_GATE}",
            f"image_generation: {CURRENT_IMAGE_POLICY}",
            "runtime_validation: PARTIAL__RUN_COMMAND_PREPARE_TO_BATTLE_LIVE_CAPTURED",
            "human_player_evidence: NOT_RUN",
            "codex_godot_execution: IMPLEMENTED__WIDE_CONNECTED_TERRAIN_BOUND__MACHINE_QA__RUNTIME_NOT_RUN",
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
            CURRENT_IMAGE_POLICY,
            REPOSITORY_ONLY_POLICY,
        ),
        "onboarding authority",
    )

    ledger_current = read(root, "docs/PROJECT_CANON_DECISION_LEDGER.md")
    require(
        errors,
        ledger_current,
        (
            CURRENT_CONTRACT,
            f"CURRENT_APPROVED_REPLAN_DECISIONS = {CURRENT_DECISION_COUNT}",
            GLOBAL_BUILDING_ROSTER_DECISION_ID,
            GLOBAL_BUILDING_ROSTER_SPEC,
            BASE_FORWARD_LAYOUT_DECISION_ID,
            BASE_FORWARD_LAYOUT_SPEC,
            pathlib.PurePosixPath(NORTH_STAR_AUDIT).name,
            pathlib.PurePosixPath(FINAL_REVIEW).name,
            "NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY",
            "FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
            CURRENT_IMAGE_POLICY,
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
