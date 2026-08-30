# OMENWARD · 열린 전장 v6 Visual Lock Handoff

```yaml
handoff_id: OMW-HANDOFF-20260829-OPEN-BATTLEFIELD-V6-VISUAL-LOCK-01
updated_at: 2026-08-29
status: CURRENT_RESTART_ROUTER
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
notion_current_authority: RETIRED__NO_FUTURE_READ_OR_WRITE
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
layout_owner: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
visual_lock_packet: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md
planning_board_owner: docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md
adversarial_review: docs/reviews/ADVERSARIAL_OPEN_BATTLEFIELD_V6_VISUAL_LOCK_REVIEW_2026-08-29.md
current_gate: PHASE2_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOT_MIGRATION__ISSUE_255__MACHINE_VERIFIED__RUNTIME_TARGET_RESOLUTION_REQUIRED
product_code_authority: OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01__SCOPED_IMPLEMENTED__MACHINE_VERIFIED
runtime: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
```

## Locked planning state

```text
PLANNING_BOARD = OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01__V6_OPEN_BATTLEFIELD_NO_BARRICADE
PLANNING_BOARD_STATUS = USER_CONFIRMED_PLANNING_LOCK__NOT_RUNTIME_ASSET
HOME_BASE = 4_DISCOVERABLE_FIXED_CONSTRUCTION_PADS + 2_FIXED_AUTO_ATTACK_TOWERS
FORWARD_BASE = 2_DISCOVERABLE_FIXED_CONSTRUCTION_PADS + 1_FIXED_AUTO_ATTACK_TOWER
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN
BUILD_PLACEMENT_FREEDOM = DISCOVERABLE_FIXED_PADS_IN_OPEN_TERRAIN__NOT_FREEFORM_TERRAIN_GRID
TACTICAL_COMMAND_BARRICADE = OUT_OF_SCOPE__RETAINED
```

## Resume exactly here

1. Fresh-read Base/main/open PR/Issue and the current Decision index, Active Context, this handoff, visual lock packet, layout contract, and board record.
2. Run the Phase 2 readiness review: create or confirm one implementation Issue, define RED tests for exact pad/tower/no-fixed-barricade semantics, prepare an implementation packet, and review runtime-asset provenance.
3. Only after that gate, create a separately authorized Godot implementation branch. Target-resolution runtime QA and human usability/player evidence remain separate and `NOT_RUN` until executed.

The preceding 2026-08-28 open-battlefield handoff is superseded as a restart router; it remains historical evidence for the v6 generation and its pre-lock review.
