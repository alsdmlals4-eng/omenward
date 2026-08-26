# OMENWARD Run Command Vertical Slice · Execution Packet

```yaml
packet_id: OMW-EXEC-20260824-RUN-COMMAND-VERTICAL-SLICE-01
status: APPROVED_FOR_EXECUTION_RECONCILED_2026_08_26
approved_by_user: true
approved_at: 2026-08-24
reactivated_by_user: true
reactivated_at: 2026-08-26
architecture: ORCHESTRATION_FIRST_VERTICAL_SLICE
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8-r5.4
implementation_plan: docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md
historical_base_main_at_packet_creation: fb11c50d594c03d49f4d675e01340148f889cdbc
execution_baseline: LATEST_COMPLETED_MAIN_AT_EXECUTOR_FRESH_READ
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
codex_route: CODEX_GODOT_PRODUCT_IMPLEMENTATION_HANDOFF
implementation_authority: HIGODOT_SINGLE_PERSISTENT_AUTHORING_AUTHORITY
persistent_godot_authoring: RESOLVE_FROM_CURRENT_PROJECT_ADOPTION_AND_EXACT_SESSION
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

The player-facing battlefield for this slice must consume the current visual/battlefield Decision rather than the superseded long-road/no-minimap layout.

```text
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
```

## Required current owners

- `docs/CURRENT_CONFIRMED_DECISIONS.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md`
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`
- Project Notion Home + relevant Run Command/UI/Visual human-facing pages.

## Execution baseline and ownership

The historical `runtime/run-command-vertical-slice-20260824` branch and its 2026-08-24 start SHA are provenance only. They are not the execution baseline after reactivation.

```text
latest completed `main`
→ fresh open-PR/Issue inventory
→ current Decision / Active Context / implementation packet
→ Project Notion Home + current visual surfaces
→ actual code/test/toolchain state
→ new implementation branch/worktree owned by the Codex execution work item
```

Actual Godot product implementation is not performed by GPT through a PowerShell-launched local Codex. GPT owns this planning/reconciliation and final review. Codex receives `CODEX_GODOT_PRODUCT_IMPLEMENTATION_HANDOFF`, independently fresh-reads OMENWARD GitHub + Notion, and performs product implementation in its own execution environment.

## Execution invariants

- Preserve `StageRun`, `RouletteService`, `DeploymentService`, `BattleSimulator`, `StageEconomy`, and `WaveDirector` as reusable foundation unless a RED test proves a bounded change is required.
- Add orchestration seams rather than a second game-state authority.
- PREPARE/COMMIT/REVIEW do not advance active battle/wave/economy time.
- COMMIT assignments are editable pending state; no food reservation, spawn, or deployed truth before final confirm.
- Final COMMIT applies only after aggregate preflight and must not knowingly partially apply an invalid plan.
- Player-facing roulette uses 3×3 + 12 direct arrows; preview does not spend; executed moves are irreversible inside the session; Spin and Result Confirm are separate actions.
- Player UI does not recompute combat, roulette outcome, probability authority, or causal truth.
- All three current Front-State views remain simultaneously readable.
- Each front owns one contextual minimap for progress/stronghold/route and relevant infiltration/air/Boss/Siege context.
- The minimap does not replicate every unit, combat animation, or VFX; it is not a second battlefield.
- Technical `StageHud` is preserved as debug/evidence surface; it is not the default player-facing North Star.
- No three-reels-to-three-lanes fixed mapping.
- No gambling/jackpot presentation.
- No final balance authority promotion.
- No image generation in this implementation work item.

## Toolchain freshness before product mutation

The executor must not reuse old PID/session/port or historical tool pins as current readiness evidence.

```text
current repository/worktree identity
→ current project.godot compatibility
→ official/current adopted toolchain check
→ exact installed Godot + authoring/test/live-QA identities
→ exact Editor/session routing
→ rollback/canary requirements when an update is actually needed
→ product mutation
```

Current OMENWARD adoption retains HiGodot as the persistent authoring authority, GUT as deterministic test authority, and Hera as read-only live QA; their exact versions and live session identity must still be fresh-read. A tool being installed does not prove its current session is the OMENWARD session.

## Evidence sequence

```text
GUT or current adopted deterministic test RED (>0 discovered tests)
→ project-adopted persistent Godot authoring
→ current project-approved Godot parse/import
→ focused GREEN
→ existing headless/Python regressions
→ deterministic replay comparison
→ project-adopted read-only live QA with tracked-source delta NONE
→ 960×540 / 1280×720 / 1920×1080 front/minimap readability evidence
→ five full adversarial review loops
→ exact-head CI/review/ruleset gate
→ safe merge if eligible
→ postmerge GitHub readback
→ applicable Project Notion human-facing reflection/readback
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
- unrelated adapter/governance backlog after this reconciliation is merged
- takeover/merge/rebase of PR #205 or PR #209

## Stop conditions

Stop as `BLOCKED_UNVERIFIED` rather than broadening scope if any of these occur:

- exact project/editor/session or project-adopted authoring authority cannot be proven for persistent Godot mutation.
- latest `main` changes invalidate the implementation plan or create overlapping current-task ownership.
- a required test cannot discover >0 tests.
- the current visual Decision cannot be represented without changing protected product meaning or expanding the first-slice scope.
- exact-head regression/CI failure cannot be resolved inside the approved slice.
- a needed fix would change protected product identity, game economy/balance authority, or unrelated workstreams.

## Current execution readiness

```yaml
PLANNING: PASS
USER_ARCHITECTURE_APPROVAL: PASS
USER_REACTIVATION_2026_08_26: PASS
IMPLEMENTATION_PLAN: RECONCILED_WITH_CURRENT_VISUAL_DECISION
EXECUTION_PACKET: RECONCILED_WITH_R5_4
EXECUTION_BASELINE: MUST_FRESH_READ_LATEST_COMPLETED_MAIN
CODEX_HANDOFF: READY_AFTER_THIS_RECONCILIATION_MERGES
PRODUCT_RUNTIME_IMPLEMENTATION: NOT_RUN
DETERMINISTIC_RED: NOT_RUN
DETERMINISTIC_GREEN: NOT_RUN
LIVE_QA: NOT_RUN
GUT_RED: NOT_RUN
GUT_GREEN: NOT_RUN
HERA_LIVE_QA: NOT_RUN
MINIMAP_RUNTIME_READABILITY: NOT_RUN
SD_UNIT_RUNTIME_READABILITY: NOT_RUN
HUMAN_VALIDATION: NOT_RUN
PLAYER_EXPERIENCE_VALIDATION: NOT_RUN
```

The next valid product executor is Codex after this reconciliation reaches current `main`. Codex must fresh-read current OMENWARD GitHub + Project Notion, create/own a fresh implementation workstream from latest completed `main`, follow the reconciled plan, and report actual tests/runtime evidence back for GPT review.
