# [현행] OMENWARD Handoff Context

```yaml
updated_at: 2026-08-30
status: SINGLE_MARCH_FRONT_THREE_TAB_COMMAND__IMPLEMENTED__RUNTIME_TECHNICAL_SMOKE_PASS
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_visual_decision: OMW-PLAN-20260830-SINGLE-MARCH-FRONT-THREE-TAB-01
current_visual_asset: OMW-IMG-20260830-SINGLE-MARCH-FRONT-TERRAIN-V1__GENERATED_CANDIDATE__USER_REVIEW_PENDING
current_strategic_map_owner: scripts/ui/strategic_map_view.gd
current_strategic_map_status: SINGLE_FRONT_IMPLEMENTED__RUNTIME_TECHNICAL_SMOKE_PASS
current_gate: REVIEW_TERRAIN_CANDIDATE_AND_RUN_HUMAN_USABILITY_CHECK
implementation_authorized: true
implementation_authority: SCOPED_APPROVED
implementation_execution: IMPLEMENTED__28_HEADLESS_GODOT_CONTRACTS_PASS__RUNTIME_TECHNICAL_SMOKE_PASS
runtime_validation: RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
human_player_evidence: NOT_RUN
visual_generation: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
visual_confirmation: GENERATE_THEN_USER_CONFIRM_LOCK
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_open_work_items: FRESH_GITHUB_QUERY_REQUIRED
```

## Current product state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 29
MAP_TOPOLOGY = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL
FRONT_STRUCTURE = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE

PLAYER_WORK_SURFACES = DOMESTIC + ROULETTE + FRONT
BUILDING_MAP_PLACEMENT = FORBIDDEN
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
GLOBAL_BUILDING_ROSTER = 6_PLUS_STABLE_PLAYER_HELD_FORWARD_BASE_AND_CLASH_ZONE
FIXED_TOWER_COUNT_PER_ACTIVE_FRONT = 1
TOWER_OWNERSHIP = STABLE_WARD_FORWARD_OBJECTIVE_ONLY
THREE_FRONT_TOPOLOGY = SUPERSEDED

SINGLE_MARCH_FRONT_THREE_TAB_COMMAND = IMPLEMENTED__28_HEADLESS_GODOT_CONTRACTS_PASS__RUNTIME_TECHNICAL_SMOKE_PASS
CURRENT_TARGET_RUNTIME_ASSET = OMW-IMG-20260830-SINGLE-MARCH-FRONT-TERRAIN-V1__GENERATED_CANDIDATE__NOT_BOUND
LEGACY_RUNTIME_BACKDROP = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
CURRENT_NEXT = REVIEW_TERRAIN_CANDIDATE_AND_RUN_HUMAN_USABILITY_CHECK
```

## Current owners

- `docs/design/APPROVED_OMENWARD_SINGLE_MARCH_FRONT_AND_THREE_TAB_COMMAND_2026-08-30.md` — approved topology and player workflow.
- `docs/superpowers/plans/2026-08-30-single-march-front-and-three-tab-command.md` — detailed implementation plan and test order.
- `docs/images/candidates/OMENWARD_SINGLE_MARCH_FRONT_TERRAIN_CANDIDATE_2026-08-30.md` — preview candidate only; there is no `assets/` copy or scene binding.
- `scripts/core/stage_run.gd`, `scripts/battle/battle_simulator.gd`, `scripts/ui/run_command_screen.gd`, and `scripts/ui/strategic_map_view.gd` — implemented domain and presentation consumers.

## Verification boundary

The single-front implementation passed all 28 repository headless Godot
contracts and a technical runtime smoke. This establishes automated contract
coverage plus a bounded live render/input observation. It does not establish
player readability, human UX, release rights, or balance completion.

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
4. Review the generated terrain candidate against the captured single-front path.
5. Ask for exact user lock only if promoting the generated terrain candidate;
   otherwise leave it unbound.
