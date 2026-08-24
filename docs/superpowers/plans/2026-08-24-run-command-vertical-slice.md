# OMENWARD Run Command Vertical Slice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement one playable OMENWARD vertical slice that proves `PREPARE -> Roulette STOPPED/MANIPULATE -> CONFIRM -> COMMIT pending plan -> atomic deployment -> BATTLE -> REVIEW` without replacing the existing battle/economy foundation.

**Architecture:** Use the approved orchestration-first design. `StageRun` stays the coordinator for existing economy/building/roulette/deployment/wave/battle services. New focused state/transaction objects own Run Command phase, roulette manipulation, and pending deployment planning. The existing `RouletteService` is split only enough to support `paid spin snapshot -> manipulation -> confirmed resolution` without duplicating the central-row/8-line resolver. Deployment uses aggregate preflight plus one batch food reservation and prevalidated battle spawns so invalid COMMIT plans produce zero applied units.

**Tech Stack:** Godot 4.7.x, GDScript, GUT 9.7.1, existing SceneTree headless tests, HiGodot/godot-ai as sole persistent Godot authoring authority, Hera as read-only live QA.

**Spec:**
- `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md`

## Global Constraints

- `RUN_COMMAND_SCREEN = PREPARE -> COMMIT -> BATTLE -> REVIEW`.
- `ROULETTE_EXPOSURE = 3×3`; 12 direct arrows: 3 column up + 3 column down + 3 row left + 3 row right.
- `THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN`.
- `IRREVERSIBLE_LANE_COMMITMENT = REQUIRED`, but pending COMMIT assignments are editable and are not deployed truth.
- `ONE_ACTIVE_WORK_SURFACE_AT_A_TIME = TRUE`; duplicated top resource totals in the lower deck are forbidden.
- Existing `RouletteService.resolve_board_snapshot()` central-row judging, 8-line counting, rank and gold behavior remain the only reward-resolution authority.
- `RouletteService.spin()` legacy behavior remains regression-protected; the new player path must not charge twice or resolve before manipulation.
- PREPARE/COMMIT/REVIEW must not advance WaveDirector, BattleSimulator, or StageEconomy active time.
- Existing battle, economy, building, role-output and historical-evidence workstreams are not rewritten.
- Persistent `.gd`, `.tscn`, `.tres`, `project.godot`, Scene/Node/Resource mutations are HiGodot-only.
- GUT RED requires **>0 tests discovered**. A missing implementation file must not cause the test script itself to fail parsing before discovery: initial RED tests use dynamic `load()` or a behavior-level RED after a minimal loadable shell exists.
- Hera is `LIVE_QA_AND_OBSERVABILITY_ONLY`; tracked-source delta attributable to Hera must be `NONE`.
- Runtime/device/accessibility/controller/human evidence remain `NOT_RUN` until actually executed.
- No new paid dependency or service.

---

## File Structure

**Create**
- `scripts/run_command/run_command_state.gd` — PREPARE/COMMIT/BATTLE/REVIEW state authority.
- `scripts/roulette/roulette_manipulation_session.gd` — stopped 3×3 board, preview/apply/confirm and move budget.
- `scripts/units/pending_deployment_plan.gd` — editable reward-index → lane assignments and aggregate validation.
- `scripts/ui/run_command_view_model.gd` — read-only player-safe projection.
- `scripts/ui/run_command_screen.gd` — player input/controller; delegates commands.
- `scenes/ui/run_command_screen.tscn` — player-facing Focus Mode UI.
- focused GUT tests under `tests/gut/` for every new owner plus one vertical-slice integration test.

**Modify**
- `scripts/roulette/roulette_service.gd` — add paid stopped-snapshot transaction seam; keep `resolve_board_snapshot()` as outcome authority.
- `scripts/core/stage_economy.gd` — add non-mutating food-capacity preflight helper.
- `scripts/units/deployment_service.gd` — add batch deployment transaction with one aggregate food reservation.
- `scripts/battle/battle_simulator.gd` — add non-mutating spawn-definition preflight helper.
- `scripts/core/stage_run.gd` — compose new owners, phase-gate simulation, orchestrate confirmed roulette and COMMIT transaction.
- `scripts/presentation/scene_binder.gd`, `scenes/main/main.tscn` — bind player surface while preserving technical HUD as debug/evidence.
- `tests/headless/stage_run_test.gd` — replace obsolete immediate deployment expectation with staged COMMIT behavior; preserve unrelated regressions.
- `docs/ACTIVE_CONTEXT.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md` only after actual implementation/evidence; do not pre-promote PASS.

---

### Task 1: Run Command phase authority

**Files**
- Create: `scripts/run_command/run_command_state.gd`
- Test: `tests/gut/test_run_command_state.gd`

**Produces**
```gdscript
class_name RunCommandState
func phase() -> StringName
func enter_prepare() -> void
func enter_commit() -> bool
func enter_battle() -> bool
func enter_review() -> bool
func can_mutate_preparation() -> bool
func can_edit_commit_plan() -> bool
func can_advance_combat() -> bool
```

- [ ] **Step 1: RED test that is discoverable before the implementation exists.**

```gdscript
extends GutTest

func test_run_command_state_script_exists() -> void:
    var script := load("res://scripts/run_command/run_command_state.gd")
    assert_not_null(script)
```

Run:
```text
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_run_command_state.gd -gexit
```
Expected: 1+ test discovered, FAIL because load returns null.

- [ ] **Step 2: Create the minimal loadable `RunCommandState` shell**, rerun, then replace/add behavior RED assertions for legal phase order and capability flags.
- [ ] **Step 3: Implement minimal behavior:** initial PREPARE; only PREPARE→COMMIT→BATTLE→REVIEW; REVIEW→PREPARE explicit reset; phase capability helpers as specified.
- [ ] **Step 4: GREEN with >0 tests.**
- [ ] **Step 5: Commit.**

```text
git add scripts/run_command/run_command_state.gd tests/gut/test_run_command_state.gd
git commit -m "feat: add Run Command phase authority"
```

---

### Task 2: Split paid roulette spin from confirmed resolution

**Files**
- Modify: `scripts/roulette/roulette_service.gd`
- Create: `tests/gut/test_roulette_spin_transaction.gd`
- Preserve existing roulette headless tests.

**Produces**
```gdscript
func begin_paid_spin(seed_input: Dictionary) -> Dictionary
func resolve_confirmed_spin(transaction: Dictionary, confirmed_board: Array[StringName]) -> RouletteSpinResult
```

`begin_paid_spin()` result shape:
```gdscript
{
    "accepted": bool,
    "failure_reason": StringName,
    "spin_seed": int,
    "resolution_seed": int,
    "paid_cost": int,
    "board": Array[StringName],
    "sources": Array[Dictionary],
}
```

- [ ] **Step 1: RED tests** proving: one accepted begin deducts exactly one `SPIN_COST`; begin returns a 9-cell stopped board but no reward/gold resolution; insufficient gold mutates nothing; confirmed resolution uses `resolve_board_snapshot()` semantics and does not charge again; resolving the same transaction twice is rejected/idempotently blocked by transaction state owned by the caller/session rather than paying twice.
- [ ] **Step 2: Run RED (>0 discovered).**
- [ ] **Step 3: Refactor existing `spin()` to call the new seam internally** so legacy callers keep the same observable result: begin paid spin → immediately resolve its natural board. Do not duplicate `_completed_line_count`, rank or gold logic.
- [ ] **Step 4: GREEN focused tests + existing roulette contract.**
- [ ] **Step 5: Commit.**

```text
git add scripts/roulette/roulette_service.gd tests/gut/test_roulette_spin_transaction.gd
git commit -m "refactor: split roulette spin and confirmed resolution"
```

---

### Task 3: 3×3 manipulation session

**Files**
- Create: `scripts/roulette/roulette_manipulation_session.gd`
- Test: `tests/gut/test_roulette_manipulation_session.gd`

**Produces**
```gdscript
class_name RouletteManipulationSession
func begin(transaction: Dictionary, available_moves: int) -> bool
func board_snapshot() -> Array[StringName]
func preview_row_shift(row: int, direction: int) -> Array[StringName]
func preview_column_shift(column: int, direction: int) -> Array[StringName]
func apply_row_shift(row: int, direction: int) -> bool
func apply_column_shift(column: int, direction: int) -> bool
func remaining_moves() -> int
func confirm() -> Dictionary
func is_confirmed() -> bool
```

- [ ] **Step 1: Discoverable RED for missing script; create loadable shell; then behavior RED.**
- [ ] **Step 2: Behavior tests:** exact 9 cells; preview purity; row wrap; column wrap; move decrements only on successful apply; zero moves blocks apply; directions accept only `-1` or `1`; row/column index accepts only `0..2`; returned arrays/dictionaries are deep enough copies that caller mutation cannot alter session truth; after confirm all manipulation is blocked; confirm returns original transaction fields plus the confirmed board exactly once.
- [ ] **Step 3: Implement minimal copy-on-read session.** Do not resolve rewards, mutate economy, or infer three-lane mapping.
- [ ] **Step 4: GREEN + existing roulette regression.**
- [ ] **Step 5: Commit.**

```text
git add scripts/roulette/roulette_manipulation_session.gd tests/gut/test_roulette_manipulation_session.gd
git commit -m "feat: add deterministic roulette manipulation session"
```

---

### Task 4: Staged COMMIT and atomic batch deployment

**Files**
- Create: `scripts/units/pending_deployment_plan.gd`
- Modify: `scripts/core/stage_economy.gd`
- Modify: `scripts/units/deployment_service.gd`
- Modify: `scripts/battle/battle_simulator.gd`
- Test: `tests/gut/test_pending_deployment_plan.gd`
- Test: `tests/gut/test_atomic_deployment_batch.gd`

**Produces**
```gdscript
# StageEconomy
func can_reserve_food(amount: int) -> bool

# BattleSimulator
func can_spawn_definition(spawn: UnitSpawnDefinition) -> bool

# DeploymentService
func deploy_batch(cards: Array[UnitSpawnDefinition], lane_ids: Array[StringName], position: float) -> Dictionary
# result {"accepted": bool, "reason": StringName, "deployed": Array[UnitSpawnDefinition]}

# PendingDeploymentPlan
class_name PendingDeploymentPlan
func assign(reward_index: int, lane_id: StringName) -> bool
func unassign(reward_index: int) -> bool
func assignments() -> Dictionary
func build_ordered_batch(rewards: Array[UnitSpawnDefinition]) -> Dictionary
```

- [ ] **Step 1: RED tests for pending state:** assignment/reassignment/unassign never changes food/deployment/battle; invalid lane and invalid reward index fail; duplicate reward index has one current assignment.
- [ ] **Step 2: RED tests for aggregate transaction:** insufficient total food returns zero deployed; any invalid spawn definition/lane detected by preflight returns zero deployed; accepted batch reserves aggregate food **once**, records all deployment entries deterministically, and returns deployed definitions in reward-index order.
- [ ] **Step 3: Implement `StageEconomy.can_reserve_food()` as non-mutating mirror of capacity logic.**
- [ ] **Step 4: Implement `BattleSimulator.can_spawn_definition()` using exactly the existing `spawn_unit()` validity boundary: non-null, archetype exists, lane exists.** Do not add a new combat rule.
- [ ] **Step 5: Implement `DeploymentService.deploy_batch()`: validate array sizes/lanes/cards; sum food; call `can_reserve_food(total)`; only then call `try_reserve_food(total)` once; append/log all deployed cards. Existing single `deploy()` remains for compatibility and may delegate to batch-of-one.
- [ ] **Step 6: GREEN + deployment/battle/economy regressions.**
- [ ] **Step 7: Commit.**

```text
git add scripts/units/pending_deployment_plan.gd scripts/core/stage_economy.gd scripts/units/deployment_service.gd scripts/battle/battle_simulator.gd tests/gut/test_pending_deployment_plan.gd tests/gut/test_atomic_deployment_batch.gd
git commit -m "feat: add staged atomic deployment transaction"
```

---

### Task 5: Orchestrate the playable slice in StageRun

**Files**
- Modify: `scripts/core/stage_run.gd`
- Modify: `tests/headless/stage_run_test.gd`
- Create: `tests/gut/test_run_command_vertical_slice.gd`

**Produces**
```gdscript
var run_command_state: RunCommandState
var roulette_session: RouletteManipulationSession
var pending_deployment_plan: PendingDeploymentPlan

func begin_roulette_manipulation(seed_input: Dictionary, available_moves: int) -> Dictionary
func shift_roulette_row(row: int, direction: int) -> bool
func shift_roulette_column(column: int, direction: int) -> bool
func confirm_roulette_result() -> RouletteSpinResult
func enter_commit() -> bool
func assign_pending_reward(reward_index: int, lane_id: StringName) -> bool
func unassign_pending_reward(reward_index: int) -> bool
func confirm_deployment_and_start_battle() -> Dictionary
```

- [ ] **Step 1: RED:** revise the old immediate `deploy_next_roulette_reward()` expectation. In the new player path, lane assignment during COMMIT changes neither `economy.food_used`, `deployment.deployed_cards`, nor `battle.snapshot().units`.
- [ ] **Step 2: RED vertical-slice test:** PREPARE begin paid spin → stopped board → at least one legal manipulation → confirm once → reward storage → COMMIT assignment → final confirm → BATTLE; verify food/deployed/battle unit changes happen only at final COMMIT.
- [ ] **Step 3: Integrate roulette transaction:** `begin_roulette_manipulation()` only in PREPARE and only with no unresolved session/reward conflict. `confirm_roulette_result()` passes the session's confirmed transaction/board to `RouletteService.resolve_confirmed_spin()`, then stores reward using the existing stage storage path.
- [ ] **Step 4: Integrate COMMIT transaction:** before calling `deployment.deploy_batch()`, build all spawn definitions with assigned lanes and call `battle.can_spawn_definition()` for every definition. If any fail, return with zero deployment mutation. After accepted `deploy_batch`, spawn exactly the returned deployed definitions; the prior preflight makes `spawn_unit()` valid under current battle rules.
- [ ] **Step 5: Phase-gate `advance(delta)`:** PREPARE/COMMIT/REVIEW may update only non-active UI/planning clocks if needed; WaveDirector, BattleSimulator and StageEconomy active advancement occurs only in BATTLE.
- [ ] **Step 6: On natural battle result, enter REVIEW before exposing next-run transition.** Debug `stage_victory/stage_defeat` remains debug/test-only and must not become the player CTA.
- [ ] **Step 7: GREEN focused GUT + complete affected headless suite.**
- [ ] **Step 8: Commit.**

```text
git add scripts/core/stage_run.gd tests/headless/stage_run_test.gd tests/gut/test_run_command_vertical_slice.gd
git commit -m "feat: orchestrate Run Command vertical slice"
```

---

### Task 6: Player-safe view model and Focus Mode UI

**Files**
- Create: `scripts/ui/run_command_view_model.gd`
- Create: `scripts/ui/run_command_screen.gd`
- Create: `scenes/ui/run_command_screen.tscn`
- Modify: `scripts/presentation/scene_binder.gd`
- Modify: `scenes/main/main.tscn`
- Create tests: `tests/gut/test_run_command_view_model.gd`, `tests/gut/test_run_command_screen.gd`
- Preserve: `scripts/ui/stage_hud.gd`, `scenes/ui/stage_hud.tscn` as technical/debug evidence surface.

**View-model default snapshot**
```gdscript
{
  "phase": StringName,
  "top_hud": {"gold": int, "food_used": int, "food_cap": int, "wave": int, "forecast_summary": Variant},
  "prepare": Dictionary,
  "commit": Dictionary,
  "battle": Dictionary,
  "review": Dictionary,
  "primary_action": Dictionary,
}
```

- [ ] **Step 1: RED view-model tests:** fail if default player snapshot leaks `source_building_ids`, `reward_archetype_ids`, raw unit IDs, raw target IDs, raw internal cause codes, or exact diagnostic counters. View model must be read-only.
- [ ] **Step 2: Implement projection only; do not calculate roulette/combat outcomes or probabilities.**
- [ ] **Step 3: Discoverable RED scene test using dynamic `load()`** before the scene exists; then behavior tests for required nodes `TopHud`, `LowerDeck`, `RouletteSurface`, `CommitSurface`, `BattleSurface`, `ReviewSurface`, `PrimaryAction`.
- [ ] **Step 4: Build 960×540 reference shell.** Lower deck 25–32% exploration target; battlefield stays primary. Only one lower work surface visible at once.
- [ ] **Step 5: Roulette surface:** 3×3 center, all 12 arrows, preview on hover/focus without spending, Spin and Result Confirm separate, movement resources local only.
- [ ] **Step 6: COMMIT surface:** stored/new units, editable pending lanes, irreversible warning, one primary CTA. Do not present three abstract lane buttons as the only spatial cue if battlefield lane selection can be bound safely.
- [ ] **Step 7: BATTLE/REVIEW:** Build/Spin/Commit mutation hidden in BATTLE; REVIEW shows five causal blocks, not raw `WAVE CAUSE REPORT` text.
- [ ] **Step 8: SceneBinder binds both the battlefield and new Run Command player surface. Technical StageHud is not simultaneously shown as the normal player dashboard.**
- [ ] **Step 9: GREEN scene/view tests.**
- [ ] **Step 10: Commit.**

```text
git add scripts/ui/run_command_view_model.gd scripts/ui/run_command_screen.gd scenes/ui/run_command_screen.tscn scripts/presentation/scene_binder.gd scenes/main/main.tscn tests/gut/test_run_command_view_model.gd tests/gut/test_run_command_screen.gd
git commit -m "feat: add Focus Mode Run Command player UI"
```

---

### Task 7: Verification, runtime evidence, adversarial review and integration

- [ ] **Godot parse/import:** Godot 4.7.x, no script/resource errors.
- [ ] **GUT:** all new suites >0 tests, 100% pass.
- [ ] **Existing regressions:** roulette, stage run, battle, economy, deployment, application/session/bootstrap and every CI-routed affected contract.
- [ ] **Python contracts:** run the exact suite routed by `.github/workflows/validate-omenward-core.yml`; zero required tests/checks is failure.
- [ ] **Determinism replay:** same seed + same action list twice; compare confirmed board, deployed reward order/lane, input log deterministic fields and final slice state.
- [ ] **Unrelated-diff gate:** no role-output #176, balance pilot, platform/release, adapter/governance or historical-evidence mutation unless an independently approved work item owns it.
- [ ] **Hera pre-fingerprint → live player-path smoke → post-fingerprint.** Complete PREPARE→Spin→manipulate→Confirm→COMMIT→BATTLE→REVIEW. Hera source delta must be `NONE`.
- [ ] **Resolution/readability:** 960×540, 1280×720, 1920×1080; all three lanes visible, lower deck secondary, one active work surface, 12 arrows legible, top resource totals not duplicated. Mouse+keyboard executed. Controller remains NOT_RUN unless actually executed.

**Five full adversarial loops**
- [ ] **Loop 1 — authority/architecture:** duplicate state owners, UI rule calculation, premature resolution/charge, stale planning authority, unrelated open-work mutation.
- [ ] **Loop 2 — transaction:** insufficient gold, invalid board, zero moves, post-confirm mutation, invalid reward index/lane, insufficient aggregate food, invalid spawn preflight, double confirm, phase skip. Require zero mutation on rejected COMMIT.
- [ ] **Loop 3 — regressions:** legacy `spin()`, central-row judging, 8-line outcomes, battle/economy/wave behavior in BATTLE, debug HUD availability, historical evidence ownership.
- [ ] **Loop 4 — UX/state:** more than one primary CTA, more than one lower surface, resource duplication, raw debug leakage, hidden irreversible boundary, three-reels/three-lanes confusion, battlefield crop.
- [ ] **Loop 5 — Implementation Reality Gate:** fresh latest main + exact implementation HEAD + all changed files + tests + runtime/Hera evidence + remaining work. Exit only with zero blocking findings.

**Integration**
- [ ] Create one implementation PR from latest completed `main`; no takeover of existing/open unrelated branches.
- [ ] Require exact-head CI, unresolved threads 0, repository rules/checks, no force push/admin bypass.
- [ ] Merge only if current-task continuation rules are satisfied; otherwise leave the exact blocker.
- [ ] Postmerge readback exact main. Update `docs/ACTIVE_CONTEXT.md`/`docs/CURRENT_IMPLEMENTATION_STATUS.md` only to evidence actually executed; human/player experience remains NOT_RUN without real users.

---

## Self-Review

**Spec coverage:** Covers Run Command phase, paid stopped-spin transaction, 3×3/12-arrow manipulation, staged atomic COMMIT, battle-only active simulation, player-safe projection, Focus-adaptive lower deck, technical HUD preservation, deterministic/runtime evidence and 5-loop adversarial review.

**Adversarial corrections already incorporated:**
1. The first draft incorrectly assumed current `RouletteService.spin()` could precede manipulation; corrected by adding a paid stopped-snapshot seam and preserving `spin()` as legacy wrapper.
2. The first draft's preflight + per-unit deploy callable could still partially mutate if a later apply failed; corrected to aggregate food reservation + battle spawn preflight + deterministic batch deployment.
3. A missing-file `preload()` RED could prevent GUT discovery; corrected to discoverable dynamic-load RED before behavior RED.

**Intentionally outside first slice:** full 20-stage production MapRun, merchant/maintenance depth, production art generation, final balance authority, Android certification, accessibility certification, controller PASS without actual execution, human/player-experience PASS without real users.

**Execution route:** Persistent product implementation starts only in a HiGodot-enabled executor/session. GitHub text-file APIs are not a substitute for HiGodot persistent Godot authoring.