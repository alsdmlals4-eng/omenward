# [현행] OMENWARD Handoff Context

```yaml
updated_at: 2026-08-30
status: FIRST5_FTUE_CORE_LOOP_RECONCILIATION__TERRAIN_IMPLEMENTED__UNIT_SOURCE_SHEETS_GENERATED
handoff_packet_state: PACKET_READY
receiver_state: TRANSFER_ACCEPTED
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_visual_decision: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
current_visual_asset: OMW-IMG-20260830-WIDE-CONNECTED-STRATEGIC-FRONT-TERRAIN-V1
current_strategic_map_owner: scripts/ui/strategic_map_view.gd
current_strategic_map_issue: 235
current_wide_connected_terrain_asset: docs/images/approved/OMENWARD_WIDE_CONNECTED_STRATEGIC_FRONT_TERRAIN_V1.md
current_wide_connected_terrain_status: USER_APPROVED__CANON_REGISTERED__IMPLEMENTED__RUNTIME_NOT_RUN
legacy_runtime_visual_asset: OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
current_build_runtime_unit_asset_set: STORYBOOK_SD_SOURCE_SHEETS_GENERATED__TRUE_ALPHA_CELL_EXPORT_PENDING_REVIEW
current_storybook_unit_source_sheets: docs/images/planning/OMENWARD_STORYBOOK_SD_UNIT_RUNTIME_SOURCE_SHEETS_2026-08-30.md
current_storybook_shield_guard_pair_candidate: docs/images/planning/OMENWARD_STORYBOOK_SD_SHIELD_GUARD_TRUE_ALPHA_PAIR_CANDIDATE_2026-08-30.md
current_storybook_unit_asset_issue: 256
current_unit_animation_production_contract: docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md
current_image_package_status: P0_REMAINDER_SOURCES_AND_CLEANUP_MASTERS_STORED
current_gate: PHASE2_STORYBOOK_UNIT_RUNTIME_ASSETS__ISSUE_256__SOURCE_SHEETS_GENERATED__TRUE_ALPHA_CELL_EXPORT_PENDING_REVIEW
current_forward_defense_spec: docs/design/APPROVED_OMENWARD_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOTS_2026-08-30.md
current_base_forward_layout_spec: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
codex_godot_execution: IMPLEMENTED__WIDE_CONNECTED_TERRAIN_BOUND__MACHINE_QA__RUNTIME_NOT_RUN
sender_handoff: docs/handoffs/2026-08-29-open-battlefield-v6-visual-lock-handoff.md
receiver_ack: docs/handoffs/2026-08-25-front-state-visual-receiver-ack.md
implementation_execution: IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN
visual_generation_policy: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
visual_generation: PAUSED_PENDING_CORE_LOOP_RECONCILIATION
image_generation: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
runtime_validation: PARTIAL__RUN_COMMAND_PREPARE_TO_BATTLE_LIVE_CAPTURED
human_player_evidence: NOT_RUN
historical_premerge_main_sha: 4e10ea441ecf537e4bef5af9d1991ddf99be217d
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
historical_postmerge_main_sha: fd4e377c5a5203fb01c0d971e8ead474d618747f
current_closeout_state: PR_210_MERGED_ON_MAIN_HISTORICAL
receiver_base_main_sha: 1416907e6c62b00ef22dc568afa70cd86015846f
canon_freshness: CURRENT_MAIN_READBACK
```

This file is the short restart router. The sender packet was fresh-read by a new receiver and the transfer is now `TRANSFER_ACCEPTED`. Detailed evidence remains in the sender handoff and receiver ACK; this file does not duplicate them.

## Current state

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 28
FORWARD_DEFENSE_OCCUPATION_NODES = SUPERSEDED_IN_SCOPE__GLOBAL_ROSTER_IMPLEMENTED__MACHINE_VERIFIED
OPEN_BATTLEFIELD_TOWER_ONLY_LAYOUT = CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
FORWARD_BASE_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
GLOBAL_BUILDING_ROSTER = 6_PLUS_STABLE_PLAYER_HELD_FORWARD_BASE_AND_CLASH_ZONE
BUILDING_MAP_PLACEMENT = FORBIDDEN
FIXED_TOWER_COUNT_PER_SHARED_FRONT = 1
HOME_BASE_PREBUILT_PRODUCTION_BUILDINGS = NONE
HOME_BASE_CONSTRUCTION_NODE_COUNT_PER_FACTION = SUPERSEDED__GLOBAL_ROSTER_ONLY
HOME_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_FACTION = SUPERSEDED__ONE_FIXED_TOWER_PER_SHARED_FRONT
FORWARD_BASE_CONSTRUCTION_NODE_COUNT_PER_BASE = SUPERSEDED__GLOBAL_ROSTER_ONLY
FORWARD_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_BASE = SUPERSEDED__ONE_FIXED_TOWER_PER_SHARED_FRONT
CURRENT_VISUAL_DECISION = OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
CURRENT_MAIN = RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
PR_210_MERGED_MAIN_BASE = fd4e377c5a5203fb01c0d971e8ead474d618747f
PR_210_CLOSEOUT = MERGED_ON_MAIN_HISTORICAL
PLAYER_ROLE = Omen Warden / 징조수호관
PLAYER_FANTASY = 전조를 읽고 수호성을 준비하며 병력을 세 전선에 보내는 지휘관
DIRECT_HERO_MELEE_FANTASY = FORBIDDEN_AS_PRIMARY
COMMANDER_ROLE_ANCHOR = WARD_STANDARD_AND_STRATEGIC_MAP_EMBLEM

BATTLEFIELD_PRESENTATION = ONE_SIMULTANEOUS_THREE_FRONT_STRATEGIC_MAP
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
FRONT_STRUCTURE = ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
PROJECT_CORE_SCENE_VISUAL_BOARD_SCOPE = STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED
PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
CURRENT_TARGET_RUNTIME_ASSET = OMW-IMG-20260830-WIDE-CONNECTED-STRATEGIC-FRONT-TERRAIN-V1
LEGACY_RUNTIME_BACKDROP = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
PROJECT_CORE_SCENE_VISUAL_BOARD = USER_CONFIRMED_PLANNING_LOCK__V6_OPEN_BATTLEFIELD_NO_BARRICADE__NOT_RUNTIME_ASSET

IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED__PHASE2_GLOBAL_ROSTER_IMPLEMENTED__MACHINE_VERIFIED
IMPLEMENTATION_SCOPE = RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE_ONLY
IMPLEMENTATION_EXECUTION = IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN
PROJECT_ACTIVITY = FIRST5_FTUE_CORE_LOOP_RECONCILIATION__TERRAIN_IMPLEMENTED__UNIT_SOURCE_SHEETS_GENERATED
UNIT_ANIMATION_PRODUCTION_CONTRACT = RETAINED_GEOMETRY_ONLY__STORYBOOK_SD_SOURCE_SHEETS_PENDING_TRUE_ALPHA_CELL_EXPORT
SHIELD_GUARD_CLEANUP_MASTER_PAIR = LEGACY_STYLE_FIT_REVIEW_REQUIRED__NOT_CURRENT_RUNTIME_TARGET
CURRENT_NEXT = PHASE2_STORYBOOK_UNIT_RUNTIME_ASSETS__ISSUE_256__SOURCE_SHEETS_GENERATED__TRUE_ALPHA_CELL_EXPORT_PENDING_REVIEW
IMAGE_GENERATION = USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
VISUAL_GENERATION = USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
```

The 2026-08-28 Storybook Strategic Map Decision supersedes the close-backdrop target and previous detailed rendering language. It retains three-front simultaneous responsibility, battlefield-primary hierarchy, compact lower Control Deck, allied-vs-Veil contrast, 3×3 roulette/direct arrows, irreversible front commitment, `PREPARE -> COMMIT -> BATTLE -> REVIEW`, and silhouette-first troops.

## Receiver correction applied

Fresh receiver rehydration found that several current routers still exposed the pre-closeout 2026-08-24 state despite being marked current. PR #210 reconciled those current owners to the same 2026-08-25 visual Decision and retained-scoped-but-paused implementation state, then merged into current main.

This correction is documentation/canon routing only. It does not reactivate product/runtime work.

## Current visual direction / legacy runtime asset

```text
CURRENT_VISUAL_DECISION = OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
FRONT_STRUCTURE = ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
PROJECT_CORE_SCENE_VISUAL_BOARD_SCOPE = STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED
TARGET_RUNTIME_ASSET = NOT_CREATED
LEGACY_RUNTIME_ASSET = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
PLANNING_BOARD = OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01__V6_OPEN_BATTLEFIELD_NO_BARRICADE
PLANNING_BOARD_FILE = docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v6_OPEN_BATTLEFIELD_NO_BARRICADE.png
PLANNING_BOARD_STATUS = USER_CONFIRMED_PLANNING_LOCK__NOT_RUNTIME_ASSET
VISUAL_DIRECTION_LOCK_PACKET = docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md
```

Historical Notion surfaces (read-only provenance; no longer current):
- Project Home: https://app.notion.com/p/3c41b237eb1c816fbbc8e2dddc18b6eb
- Visual Bible: https://app.notion.com/p/3c01b237eb1c81c38be5e3ee9f64b59d
- Visual Components: https://app.notion.com/p/3c21b237eb1c81e29be2d6ce397c9c85

Server readback proves durable attachment/readback, not actual browser/device human-visible rendering.

## Evidence ceiling

```text
CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED
CURRENT_UI_RUNTIME = PARTIAL__RUN_COMMAND_PREPARE_TO_BATTLE_LIVE_CAPTURED
CURRENT_MINIMAP_READABILITY = PARTIAL__THREE_RESOLUTION_TECHNICAL_CAPTURED__HUMAN_NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = PARTIAL__ALL18_UNIT_GALLERY_NO_CLIPPING_SIGNAL
CURRENT_HUMAN_USABILITY = NOT_RUN
CURRENT_PLAYER_EXPERIENCE = NOT_RUN
RIGHTS_REVIEW = NOT_RUN
NOTION_SERVER_READBACK = PASS
NOTION_HUMAN_VISIBLE_CLIENT = NOT_RUN
```

## Compatibility conflict report

Google Sheet is migration/compatibility evidence only.

- `00_프로젝트_허브` is stale and still reflects an older PR175/Issue176/runtime period.
- `02_현재_확정결정` did not return the 2026-08-25 Front-State Decision in receiver search.
- `71_이미지기획_생성목록` and `72_이미지검수_승인로그` do contain `OM-IMG-023` with the current Decision ID.

Do not use the stale Sheet hub/decision list to overwrite GitHub/Notion current state. No new Sheet migration write is part of this closeout.

## Side effects already applied

```yaml
side_effects_already_applied:
  - OM-IMG-023 generated and user-approved
  - full-resolution PNG stored in Drive file 1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5
  - Notion Home current approved original attached and server-read back
  - Notion Visual Bible current approved original attached and server-read back
  - Sheet 71/72 OM-IMG-023 records written
  - OMENWARD PR #210 merged into current main fd4e377c5a5203fb01c0d971e8ead474d618747f
  - Base PR #693 carries BCP-2026-033-visual-canon-approval-and-handoff-integrity proposal/evidence
  - accidental placeholder main write already reverted by 4e10ea4
idempotency:
  retry_safe: false
  verify_before_retry:
    - verify Drive file before image re-upload
    - verify Notion image block before attachment retry
    - verify PR #210 before duplicate visual closeout PR
    - verify Base PR #693 before duplicate BCP-2026-033 submission
```

## Protected workstreams

- PR #210 is MERGED / historical visual-handoff closeout; no current task may mutate or re-run its closeout.
- PR #209 and PR #205 remain other-workstream read-only.
- Base PR #693 is the independent proposal-only `BCP-2026-033-visual-canon-approval-and-handoff-integrity` workstream and remains read-only here.
- Do not resume Issue #208 Run Command/Godot execution merely because handoff transfer is accepted.
- Required images may be produced automatically under the current autonomous-image policy; existing Omenward visual language and dual storage remain mandatory.

## Read next

A fresh future session should read only the current authorities needed for its requested scope:

1. latest Base main + root `AGENTS.md` and triggered owner;
2. fresh OMENWARD main/open PR/Issue + root `AGENTS.md`;
3. `docs/CURRENT_CONFIRMED_DECISIONS.md`;
4. `docs/ACTIVE_CONTEXT.md` + this file;
5. `docs/OMENWARD_GDD_CURRENT_CANON.md` / `docs/PROJECT_CORE.md` and the relevant detailed owner;
6. repository current visual spec / planning board / asset provenance and `OM-IMG-023` historical reference when visual scope is relevant;
7. implementation packet/actual runtime only after explicit product/runtime reactivation.

The full previous conversation is not required.

## Transfer state

```yaml
transfer_observed_postmerge_main_sha: fd4e377c5a5203fb01c0d971e8ead474d618747f
canon_freshness: CURRENT_MAIN_READBACK
receiver_ack:
  current_state_readback: PASS
  next_safe_action_readback: PASS
  protected_scope_readback: PASS
  pending_decisions_readback: []
  side_effects_readback: PASS
  status: TRANSFER_ACCEPTED
```

PR #210 closeout is merged historical evidence; resolve current main from the repository default branch before any new task. Prior exact-head verification/merge/readback steps are historical. Future product/runtime work requires a separate explicit user reactivation and fresh execution bootstrap.
