# [현행] OMENWARD Handoff Context

```yaml
updated_at: 2026-08-31
status: MODULAR_CLOSE_SINGLE_FRONT_BATTLEFIELD__IMPLEMENTED__MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_visual_decision: OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
current_visual_asset: OMW-IMG-20260831-CLOSE-FRONT-BATTLEFIELD-MODULAR-V1__CANON_REGISTERED__IMPLEMENTED
current_battle_focus_owner: scripts/ui/battle_focus_view.gd
current_march_minimap_owner: scripts/ui/march_minimap_view.gd
current_gate: HUMAN_USABILITY_AND_MULTI_UNIT_COMBAT_READABILITY_CHECK
implementation_authorized: true
implementation_authority: SCOPED_APPROVED
implementation_execution: IMPLEMENTED__FULL_HEADLESS_GODOT_SUITE_PASS__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
runtime_validation: FULL_HEADLESS_SUITE_PASS__HERA_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
human_player_evidence: NOT_RUN
visual_generation: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
visual_confirmation: GENERATE_THEN_USER_CONFIRM_LOCK
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_open_work_items: FRESH_GITHUB_QUERY_REQUIRED
```

## Current product state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 30
MAP_TOPOLOGY = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL
FRONT_STRUCTURE = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE

PLAYER_WORK_SURFACES = DOMESTIC + ROULETTE + FRONT
BUILDING_MAP_PLACEMENT = FORBIDDEN
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
GLOBAL_BUILDING_ROSTER = 6_PLUS_EACH_STABLE_PLAYER_HELD_CAPTURE_POINT__MAX_9_SINGLE_FRONT
FIXED_TOWER_COUNT_PER_ACTIVE_FRONT = 1
TOWER_OWNERSHIP = STABLE_WARD_FORWARD_OBJECTIVE_ONLY
THREE_FRONT_TOPOLOGY = SUPERSEDED

BATTLE_PRIMARY_MARCH_MINIMAP = IMPLEMENTED__MODULAR_CLOSE_BATTLEFIELD__FULL_HEADLESS_SUITE_PASS__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
MARCH_MINIMAP_LAYOUT = TOP_SINGLE_ROW_STRIP
CURRENT_TARGET_RUNTIME_ASSET = OMW-IMG-20260831-CLOSE-FRONT-BATTLEFIELD-MODULAR-V1__CANON_REGISTERED__IMPLEMENTED
LEGACY_RUNTIME_BACKDROP = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1__RETAINED__NOT_CONSUMED_BY_BATTLEFOCUSVIEW
CURRENT_NEXT = HUMAN_USABILITY_AND_MULTI_UNIT_COMBAT_READABILITY_CHECK
```

## Current owners

- `docs/design/APPROVED_OMENWARD_BATTLE_PRIMARY_MARCH_MINIMAP_2026-08-30.md` — current battle-primary / read-only minimap presentation owner.
- `docs/design/APPROVED_OMENWARD_SINGLE_MARCH_FRONT_AND_THREE_TAB_COMMAND_2026-08-30.md` — retained topology and player workflow.
- `docs/superpowers/plans/2026-08-30-battle-primary-march-minimap.md` — implementation plan and test order.
- `docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_MODULAR_V1.md` — current exact user-locked foundation and territory-prop bundle.
- `docs/qa/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_RUNTIME_SMOKE_2026-08-31.md` — technical live BATTLE evidence.
- `scripts/core/stage_run.gd`, `scripts/battle/battle_simulator.gd`, `scripts/ui/run_command_screen.gd`, `scripts/ui/battle_focus_view.gd`, and `scripts/ui/march_minimap_view.gd` — implemented domain and presentation consumers.

## Verification boundary

The battle-primary implementation passed the full repository headless Godot
suite and a live technical render/input smoke. This establishes machine and
technical runtime coverage only; player readability, human UX, multi-unit
combat readability, release rights, and balance completion remain unestablished.

The engine may still report existing headless teardown resource/RID warnings
after successful tests. Those warnings are not being represented as a clean
engine teardown or a human runtime pass.

## Historical compatibility only

- `OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01` and the
  wide connected three-front terrain are historical art/topology references;
  they are not current runtime inputs.
- `OM-IMG-023` and its Notion/Drive records are historical reference evidence
  only. Repository authority is current; Notion has no future-read/write role.
- `docs/handoffs/2026-08-29-open-battlefield-v6-visual-lock-handoff.md` is a
  preserved pre-single-front record, not the current execution route.
- `docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md`
  remains historical planning evidence, not a current runtime or UX PASS.

## Resume order

1. Fresh Base and repository/default-branch + open-work-item read.
2. `AGENTS.md`, `docs/CURRENT_CONFIRMED_DECISIONS.md`, and
   `docs/ACTIVE_CONTEXT.md`.
3. This handoff, then the current GDD/Project Core and relevant current owner.
4. Run a human readability review with multiple allied and Veil units visible
   in `BattleFocusViewport` and the read-only `MarchMinimap` in BATTLE.
5. Keep the exact approved modular asset bundle immutable unless the user locks
   a replacement candidate set.
