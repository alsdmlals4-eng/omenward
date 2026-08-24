# OMENWARD Run Command Vertical Slice · Execution Packet

```yaml
packet_id: OMW-EXEC-20260824-RUN-COMMAND-VERTICAL-SLICE-01
status: APPROVED_FOR_EXECUTION
approved_by_user: true
approved_at: 2026-08-24
architecture: ORCHESTRATION_FIRST_VERTICAL_SLICE
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
implementation_plan: docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md
base_main_at_packet_creation: fb11c50d594c03d49f4d675e01340148f889cdbc
implementation_authority: HIGODOT_SINGLE_PERSISTENT_AUTHORING_AUTHORITY
```

## Goal

Implement the first playable player-facing slice of the current OMENWARD Run Command design without replacing the existing battle/economy foundation.

```text
PREPARE
→ Roulette Spin
→ STOPPED 3×3
→ limited row/column manipulation
→ Result Confirm
→ reward storage
→ COMMIT pending lane assignment
→ atomic deployment confirm
→ BATTLE
→ REVIEW
```

## Required existing owners

- `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md`

## Execution invariants

- Preserve `StageRun`, `RouletteService`, `DeploymentService`, `BattleSimulator`, `StageEconomy`, and `WaveDirector` as reusable foundation unless a RED test proves a bounded change is required.
- Add orchestration seams rather than a second game-state authority.
- PREPARE/COMMIT/REVIEW do not advance active battle/wave/economy time.
- COMMIT assignments are editable pending state; no food reservation, spawn, or deployed truth before final confirm.
- Final COMMIT applies only after aggregate preflight and must not knowingly partially apply an invalid plan.
- Player-facing roulette uses 3×3 + 12 direct arrows; preview does not spend; executed moves are irreversible inside the session; Spin and Result Confirm are separate actions.
- Player UI does not recompute combat, roulette outcome, probability authority, or causal truth.
- Technical `StageHud` is preserved as debug/evidence surface; it is not the default player-facing North Star.
- No three-reels-to-three-lanes fixed mapping.
- No gambling/jackpot presentation.
- No final balance authority promotion.

## Evidence sequence

```text
GUT RED (>0 discovered tests)
→ HiGodot persistent implementation
→ Godot 4.7.x parse/import
→ focused GUT GREEN
→ existing headless/Python regressions
→ deterministic replay comparison
→ Hera read-only live QA with tracked-source delta NONE
→ five full adversarial review loops
→ exact-head CI/review/ruleset gate
→ safe merge if eligible
→ postmerge readback
```

## Explicit non-goals for this first slice

- full 20-stage MapRun production conversion
- merchant/maintenance depth
- final art production or new generated images
- final balance selection
- Android/device certification
- accessibility certification
- controller PASS without actual controller execution
- human/player-experience PASS without real user testing
- unrelated role-output Issue #176 work
- adapter/governance backlog

## Stop conditions

Stop as `BLOCKED_UNVERIFIED` rather than broadening scope if any of these occur:

- HiGodot authoring access is unavailable for persistent Godot mutation.
- latest `main` changes invalidate the implementation plan or create overlapping current-task ownership.
- a required test cannot discover >0 tests.
- exact-head regression/CI failure cannot be resolved inside the approved slice.
- a needed fix would change protected product identity, game economy/balance authority, or unrelated workstreams.

## Current execution readiness

```yaml
PLANNING: PASS
USER_ARCHITECTURE_APPROVAL: PASS
IMPLEMENTATION_PLAN: PREPARED
OPEN_PR_COLLISION_AT_APPROVAL_CHECK: NONE_FOUND
HIGODOT_PERSISTENT_AUTHORING_IN_THIS_CHAT: UNAVAILABLE
PRODUCT_RUNTIME_IMPLEMENTATION: NOT_RUN
GUT_RED: NOT_RUN
GUT_GREEN: NOT_RUN
HERA_LIVE_QA: NOT_RUN
HUMAN_VALIDATION: NOT_RUN
```

The next valid executor must start from fresh `main`, re-check open PRs/issues, invoke the implementation plan, and use HiGodot for every persistent Godot-source mutation.