# OMENWARD Run Command Vertical Slice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement one playable OMENWARD vertical slice that proves `PREPARE -> Roulette STOPPED/MANIPULATE -> CONFIRM -> COMMIT pending plan -> atomic deployment -> BATTLE -> REVIEW` without replacing the existing battle/economy foundation.

**Architecture:** Use the approved orchestration-first design. `StageRun` remains the owner of existing economy, buildings, roulette, deployment, wave director, battle, and Core UX services; new focused state/transaction objects own Run Command phase, roulette manipulation session, and pending deployment plan. Player UI consumes a view model/snapshot and sends commands only; it does not calculate game rules. Preserve the current technical `StageHud` as a debug/evidence surface while introducing a separate player-facing Focus Mode surface.

**Tech Stack:** Godot 4.7.x, GDScript, GUT 9.7.1, existing headless SceneTree tests, HiGodot/godot-ai as sole persistent Godot authoring authority, Hera as read-only live QA.

**Spec:**
- `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md`

## Global Constraints

- `RUN_COMMAND_SCREEN = PREPARE -> COMMIT -> BATTLE -> REVIEW`.
- `ROULETTE_EXPOSURE = 3×3`.
- Player-facing roulette has 12 direct arrows: column up/down × 3 and row left/right × 3.
- `THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN`.
- `IRREVERSIBLE_LANE_COMMITMENT = REQUIRED`, but actual deployment occurs only after the COMMIT primary CTA; pending plans are editable and are not deployed truth.
- `ONE_ACTIVE_WORK_SURFACE_AT_A_TIME = TRUE`.
- `DUPLICATE_TOP_RESOURCES = FORBIDDEN`.
- Debug Token Ledger, raw target IDs, internal cause codes, and exact diagnostic counters remain off the player-facing default surface.
- Existing `RouletteService.resolve_board_snapshot()` central-row judging and 8-line outcome behavior must remain regression-protected.
- Existing battle, economy, building, wave, and role-output workstreams must not be rewritten as part of this slice.
- Persistent `.gd`, `.tscn`, `.tres`, project-setting, or other Godot-source mutations must be performed through HiGodot/godot-ai only.
- GUT is the deterministic GDScript test authority; Hera is `LIVE_QA_AND_OBSERVABILITY_ONLY` and must produce tracked-source delta `NONE`.
- Runtime, device, accessibility, controller, and human evidence remain `NOT_RUN` until actually executed.
- No new paid dependency, SDK, or service.

---

## File Structure

### Create
- `scripts/run_command/run_command_state.gd` — authoritative PREPARE/COMMIT/BATTLE/REVIEW phase state.
- `scripts/roulette/roulette_manipulation_session.gd` — immutable stopped board + row/column manipulation transaction before confirm.
- `scripts/units/pending_deployment_plan.gd` — editable COMMIT plan and atomic preflight/apply boundary.
- `scripts/ui/run_command_view_model.gd` — player-safe snapshot; strips debug-only internals.
- `scripts/ui/run_command_screen.gd` — player input/controller for Focus Mode surface; delegates to run/view model.
- `scenes/ui/run_command_screen.tscn` — player-facing top HUD + battlefield-preserving compact lower deck shell.
- `tests/gut/test_run_command_state.gd` — phase state GUT contract.
- `tests/gut/test_roulette_manipulation_session.gd` — 3×3 manipulation/GUT contract.
- `tests/gut/test_pending_deployment_plan.gd` — staged/atomic COMMIT contract.
- `tests/gut/test_run_command_vertical_slice.gd` — cross-system vertical slice contract.

### Modify
- `scripts/core/stage_run.gd` — compose the new state/session/plan and gate active simulation by phase.
- `scripts/presentation/scene_binder.gd` — bind the player-facing Run Command screen without removing the technical HUD.
- `scenes/main/main.tscn` — instance the Run Command player UI while retaining debug/evidence access.
- `tests/headless/stage_run_test.gd` — replace the obsolete immediate-deploy expectation with staged COMMIT expectations while preserving all unrelated regressions.
- `docs/ACTIVE_CONTEXT.md` — only after implementation/evidence, record actual executed state; do not pre-promote PASS.
- `docs/CURRENT_IMPLEMENTATION_STATUS.md` — only after implementation/evidence, record exact implementation/evidence ceiling.

---

### Task 1: Run Command phase state

**Files:**
- Create: `scripts/run_command/run_command_state.gd`
- Test: `tests/gut/test_run_command_state.gd`

**Interfaces:**
- Produces:
  - `class_name RunCommandState`
  - constants `PREPARE`, `COMMIT`, `BATTLE`, `REVIEW`
  - `func phase() -> StringName`
  - `func enter_prepare() -> void`
  - `func enter_commit() -> bool`
  - `func enter_battle() -> bool`
  - `func enter_review() -> bool`
  - `func can_mutate_preparation() -> bool`
  - `func can_edit_commit_plan() -> bool`
  - `func can_advance_combat() -> bool`

- [ ] **Step 1: Write the failing GUT test**

```gdscript
extends GutTest

const RunCommandState = preload("res://scripts/run_command/run_command_state.gd")

func test_phase_order_and_capabilities() -> void:
    var state := RunCommandState.new()
    assert_eq(state.phase(), &"prepare")
    assert_true(state.can_mutate_preparation())
    assert_false(state.can_advance_combat())

    assert_true(state.enter_commit())
    assert_true(state.can_edit_commit_plan())
    assert_false(state.can_mutate_preparation())

    assert_true(state.enter_battle())
    assert_true(state.can_advance_combat())
    assert_false(state.can_edit_commit_plan())

    assert_true(state.enter_review())
    assert_false(state.can_advance_combat())
    state.enter_prepare()
    assert_eq(state.phase(), &"prepare")
```

- [ ] **Step 2: Run RED**

Run:
```text
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_run_command_state.gd -gexit
```
Expected: >0 tests discovered and FAIL because `run_command_state.gd` does not exist.

- [ ] **Step 3: Implement the minimal state machine**

```gdscript
class_name RunCommandState
extends RefCounted

const PREPARE := &"prepare"
const COMMIT := &"commit"
const BATTLE := &"battle"
const REVIEW := &"review"

var _phase: StringName = PREPARE

func phase() -> StringName:
    return _phase

func enter_prepare() -> void:
    _phase = PREPARE

func enter_commit() -> bool:
    if _phase != PREPARE:
        return false
    _phase = COMMIT
    return true

func enter_battle() -> bool:
    if _phase != COMMIT:
        return false
    _phase = BATTLE
    return true

func enter_review() -> bool:
    if _phase != BATTLE:
        return false
    _phase = REVIEW
    return true

func can_mutate_preparation() -> bool:
    return _phase == PREPARE

func can_edit_commit_plan() -> bool:
    return _phase == COMMIT

func can_advance_combat() -> bool:
    return _phase == BATTLE
```

- [ ] **Step 4: Run GREEN** — same command, expected PASS with >0 tests.
- [ ] **Step 5: Commit**

```text
git add scripts/run_command/run_command_state.gd tests/gut/test_run_command_state.gd
git commit -m "feat: add Run Command phase state"
```

---

### Task 2: 3×3 roulette manipulation session

**Files:**
- Create: `scripts/roulette/roulette_manipulation_session.gd`
- Test: `tests/gut/test_roulette_manipulation_session.gd`
- Read-only dependency: `scripts/roulette/roulette_service.gd`

**Interfaces:**
- Produces:
  - `class_name RouletteManipulationSession`
  - `func begin(board: Array[StringName], available_moves: int) -> bool`
  - `func board_snapshot() -> Array[StringName]`
  - `func preview_row_shift(row: int, direction: int) -> Array[StringName]`
  - `func preview_column_shift(column: int, direction: int) -> Array[StringName]`
  - `func apply_row_shift(row: int, direction: int) -> bool`
  - `func apply_column_shift(column: int, direction: int) -> bool`
  - `func remaining_moves() -> int`
  - `func confirm() -> Array[StringName]`
  - `func is_confirmed() -> bool`

- [ ] **Step 1: Write failing GUT cases** for: exact 9-cell requirement, preview purity, row wrap, column wrap, move consumption, no mutation with zero moves, no mutation after confirm, and returned board copies not aliases.

Representative contract:
```gdscript
func test_preview_is_pure_and_apply_consumes_one_move() -> void:
    var session := RouletteManipulationSession.new()
    assert_true(session.begin([&"a",&"b",&"c",&"d",&"e",&"f",&"g",&"h",&"i"], 1))
    var preview := session.preview_row_shift(1, 1)
    assert_eq(preview, [&"a",&"b",&"c",&"f",&"d",&"e",&"g",&"h",&"i"])
    assert_eq(session.board_snapshot(), [&"a",&"b",&"c",&"d",&"e",&"f",&"g",&"h",&"i"])
    assert_true(session.apply_row_shift(1, 1))
    assert_eq(session.remaining_moves(), 0)
```

- [ ] **Step 2: Run RED** with the focused GUT file; require >0 discovered tests.
- [ ] **Step 3: Implement minimal immutable-preview/copy-on-read session.** Use only 3×3 projection semantics; do not invent economy, rewards, or final V2 physical reel persistence in this file.
- [ ] **Step 4: Run GREEN.**
- [ ] **Step 5: Run existing roulette headless contract** to prove central-row and 8-line resolver behavior is unchanged.
- [ ] **Step 6: Commit**

```text
git add scripts/roulette/roulette_manipulation_session.gd tests/gut/test_roulette_manipulation_session.gd
git commit -m "feat: add deterministic roulette manipulation session"
```

---

### Task 3: Staged and atomic deployment plan

**Files:**
- Create: `scripts/units/pending_deployment_plan.gd`
- Test: `tests/gut/test_pending_deployment_plan.gd`
- Read-only dependency: `scripts/units/deployment_service.gd`

**Interfaces:**
- Produces:
  - `class_name PendingDeploymentPlan`
  - `func assign(reward_index: int, lane_id: StringName) -> bool`
  - `func unassign(reward_index: int) -> bool`
  - `func assignments() -> Dictionary`
  - `func preflight(rewards: Array, food_available: int) -> Dictionary`
  - `func apply(rewards: Array, deploy_callable: Callable) -> Dictionary`
  - result shape: `{ "accepted": bool, "reason": StringName, "applied_count": int }`

- [ ] **Step 1: Write failing GUT tests** proving pending edits do not call deployment, lane reassignment is editable, invalid lanes fail, insufficient aggregate food produces `accepted=false` with `applied_count=0`, and a successful apply calls the deploy callable exactly once per assigned reward.
- [ ] **Step 2: Run RED.**
- [ ] **Step 3: Implement preflight-before-apply.** Never partially apply when the plan itself is invalid. The plan does not own food; it reads the aggregate requirement and delegates actual deployment to the existing service only after preflight.
- [ ] **Step 4: Run GREEN.**
- [ ] **Step 5: Commit.**

```text
git add scripts/units/pending_deployment_plan.gd tests/gut/test_pending_deployment_plan.gd
git commit -m "feat: add atomic pending deployment plan"
```

---

### Task 4: Integrate state/session/plan into StageRun

**Files:**
- Modify: `scripts/core/stage_run.gd`
- Modify: `tests/headless/stage_run_test.gd`
- Test: `tests/gut/test_run_command_vertical_slice.gd`

**Interfaces:**
- `StageRun` produces:
  - `var run_command_state: RunCommandState`
  - `var roulette_session: RouletteManipulationSession`
  - `var pending_deployment_plan: PendingDeploymentPlan`
  - `func begin_roulette_manipulation(seed_input: Dictionary) -> Dictionary`
  - `func shift_roulette_row(row: int, direction: int) -> bool`
  - `func shift_roulette_column(column: int, direction: int) -> bool`
  - `func confirm_roulette_result() -> bool`
  - `func assign_pending_reward(reward_index: int, lane_id: StringName) -> bool`
  - `func unassign_pending_reward(reward_index: int) -> bool`
  - `func confirm_deployment_and_start_battle() -> Dictionary`

- [ ] **Step 1: Change the old immediate-deployment headless expectation to RED.** The test must assert that assignment in COMMIT does not change `deployment.deployed_cards`, `battle.snapshot().units`, or `economy.food_used` until final confirm.
- [ ] **Step 2: Add a focused vertical-slice GUT test** that starts a run, enters PREPARE, resolves/manipulates a deterministic board, confirms reward, enters COMMIT, assigns a lane, confirms atomically, reaches BATTLE, advances combat, and eventually reaches REVIEW through a deterministic test result path.
- [ ] **Step 3: Run RED with >0 tests.**
- [ ] **Step 4: Integrate the three new domain objects into `StageRun`.** Preserve existing `RouletteService` as the authoritative resolver and reward builder. Do not duplicate line-count/reward logic in the session or UI.
- [ ] **Step 5: Gate `advance(delta)` by phase.** PREPARE/COMMIT/REVIEW must not advance wave, battle, or economy active time. BATTLE uses the existing wave/battle/economy sequence.
- [ ] **Step 6: Transition to REVIEW only from actual battle result resolution.** Debug `stage_victory/stage_defeat` remains test/debug capability but must not be the player-facing completion path.
- [ ] **Step 7: Run focused GREEN and the complete existing headless regression set used by CI.**
- [ ] **Step 8: Commit.**

```text
git add scripts/core/stage_run.gd tests/headless/stage_run_test.gd tests/gut/test_run_command_vertical_slice.gd
git commit -m "feat: orchestrate Run Command vertical slice"
```

---

### Task 5: Player-safe Run Command view model

**Files:**
- Create: `scripts/ui/run_command_view_model.gd`
- Test: `tests/gut/test_run_command_view_model.gd`
- Read-only dependency: `scripts/core/core_ux_service.gd`

**Interfaces:**
- Produces `func snapshot(run: Variant) -> Dictionary` with keys:
  - `phase`
  - `top_hud`: `gold`, `mana`, `food_used`, `food_cap`, `wave`, `forecast_summary`
  - `prepare`: current active work-surface state only
  - `commit`: stored rewards, pending assignments, irreversible warning, primary CTA state
  - `battle`: lane status + tactical summary only
  - `review`: five causal blocks only
  - `block_reason_copy`

- [ ] **Step 1: Write RED tests** that fail if `source_building_ids`, `reward_archetype_ids`, raw unit IDs, raw target IDs, raw cause codes, or exact diagnostic counters leak into the default player snapshot.
- [ ] **Step 2: Implement a read-only adapter.** It may consume existing debug/Core UX snapshots but must project them into player-safe semantics; it must not mutate run state or calculate combat/roulette outcomes.
- [ ] **Step 3: GREEN + regression.**
- [ ] **Step 4: Commit.**

```text
git add scripts/ui/run_command_view_model.gd tests/gut/test_run_command_view_model.gd
git commit -m "feat: add player-safe Run Command view model"
```

---

### Task 6: Focus-adaptive Run Command player UI

**Files:**
- Create: `scripts/ui/run_command_screen.gd`
- Create: `scenes/ui/run_command_screen.tscn`
- Modify: `scripts/presentation/scene_binder.gd`
- Modify: `scenes/main/main.tscn`
- Preserve: `scripts/ui/stage_hud.gd`, `scenes/ui/stage_hud.tscn`

**Interfaces:**
- Consumes `RunCommandViewModel.snapshot(run)` and the `StageRun` command methods from Task 4.
- Player controls invoke domain commands only.

- [ ] **Step 1: Add a GUT/scene contract that loads the new scene and verifies required named nodes exist:** `TopHud`, `BattlefieldContext`, `LowerDeck`, `RouletteSurface`, `CommitSurface`, `BattleSurface`, `ReviewSurface`, `PrimaryAction`.
- [ ] **Step 2: RED.**
- [ ] **Step 3: Build the shell at the existing 960×540 reference.** Lower deck target is 25–32% of screen height; battlefield remains visible. Do not copy the mockup's multi-surface lower dashboard.
- [ ] **Step 4: Implement Focus visibility:** only one lower work surface visible at once.
- [ ] **Step 5: Implement Roulette surface:** 3×3 board, 12 direct arrows, move count, Spin/Confirm CTA separation, preview on hover/focus without spending.
- [ ] **Step 6: Implement COMMIT surface:** stored/new rewards, editable lane assignment, irreversible warning, exactly one primary CTA.
- [ ] **Step 7: Implement BATTLE/REVIEW surfaces:** hide Build/Spin/Commit mutation during battle; review shows causal summary rather than raw debug report.
- [ ] **Step 8: Keep the technical StageHud reachable only as debug/evidence surface; do not make both dashboards simultaneously player-visible by default.**
- [ ] **Step 9: GREEN scene-load and focused UI contract tests.**
- [ ] **Step 10: Commit.**

```text
git add scripts/ui/run_command_screen.gd scenes/ui/run_command_screen.tscn scripts/presentation/scene_binder.gd scenes/main/main.tscn
git commit -m "feat: add Focus Mode Run Command player UI"
```

---

### Task 7: Parse/import, complete regression, deterministic evidence

**Files:**
- No product change unless a failing test reveals a bounded defect.
- Evidence output should go only to the repository's existing evidence/test artifact locations; do not invent a second evidence authority.

- [ ] **Step 1: Godot 4.7.x headless import/parse.** Require no script/resource errors.
- [ ] **Step 2: Run all new GUT tests.** Require >0 tests and 100% pass.
- [ ] **Step 3: Run existing headless suite**, including roulette, stage run, battle, application/session, bootstrap and any CI-routed project contracts affected by changed files.
- [ ] **Step 4: Run Python contract/regression suite used by `.github/workflows/validate-omenward-core.yml`.** Zero-test discovery or skipped required checks is failure.
- [ ] **Step 5: Determinism replay:** execute the focused vertical slice twice with identical seeds/actions and compare the resulting command/input log and final state. Require exact semantic identity for deterministic fields.
- [ ] **Step 6: Confirm no unrelated role-output, balance, platform, adapter, or historical-evidence files changed.**
- [ ] **Step 7: Commit only if verification required a bounded correction; otherwise no commit.**

---

### Task 8: Hera live QA and Implementation Reality Gate

**Files:**
- No persistent authoring through Hera.

- [ ] **Step 1: Record tracked-source fingerprint immediately before Hera QA.**
- [ ] **Step 2: Launch the game and complete one real player-path smoke:** PREPARE -> Spin -> manipulate -> Confirm -> COMMIT assignment -> atomic confirm -> BATTLE -> REVIEW.
- [ ] **Step 3: Verify at 960×540, 1280×720, and 1920×1080:** all three lanes remain visible; lower deck is secondary; exactly one active work surface; 12 arrows remain legible; no duplicated Gold/Mana/Troop totals.
- [ ] **Step 4: Verify mouse and keyboard focus.** Controller remains `NOT_RUN` unless a real controller/input path is executed.
- [ ] **Step 5: Capture post-Hera tracked-source fingerprint and require delta `NONE` attributable to Hera.**
- [ ] **Step 6: Mark evidence precisely:** runtime PASS only for paths actually executed; device/accessibility/human/player-experience remain NOT_RUN unless separately performed.

---

### Task 9: Five full adversarial review loops and PR integration

**Files:**
- Entire exact-head diff + relevant current owners + test/evidence outputs.

- [ ] **Loop 1 — authority/architecture attack:** check UI/domain leakage, duplicate state owners, stale v4.7 assumptions, unrelated open-workstream mutation. Fix and rerun affected tests.
- [ ] **Loop 2 — transaction attack:** force invalid lane, insufficient aggregate food, empty rewards, duplicate assignment, zero move tickets, post-confirm manipulation, phase-skipping. Fix and rerun.
- [ ] **Loop 3 — regression attack:** central judging line, 8-line reward count, existing battle/economy/wave behavior in BATTLE, historical evidence ownership, debug HUD preservation. Fix and rerun.
- [ ] **Loop 4 — UX/state attack:** multiple primary CTAs, multiple lower surfaces visible, resource duplication, raw debug leakage, hidden irreversible boundary, three reels mistaken for three lanes. Fix and rerun.
- [ ] **Loop 5 — Implementation Reality Gate:** re-read exact HEAD, fresh main, all changed files, all test outputs, Hera evidence, and remaining work. Exit only with zero blocking findings.

- [ ] **Create one implementation PR from latest completed `main`.** Do not modify pre-existing/open unrelated branches or PRs.
- [ ] **Require exact-head CI, unresolved thread 0, no ruleset bypass, no admin bypass.**
- [ ] **Merge only if the Base current-task continuation rules are satisfied.** Otherwise leave the PR open with the exact blocker.
- [ ] **Postmerge readback:** fetch merged main and verify changed files/evidence are present; do not call runtime/human verification complete beyond executed evidence.

---

## Self-Review

**Spec coverage:** The plan covers Run Command phase ownership, 3×3 direct-arrow manipulation, staged atomic commit, battle-only active time, player-safe information projection, one-surface lower deck, technical HUD preservation, runtime/deterministic evidence, and 5-loop adversarial review. Platform release, balance finalization, controller/device/human usability, full 20-stage MapRun progression, merchant/maintenance depth, and production art are intentionally outside this first vertical slice.

**Placeholder scan:** No `TBD`, generic "add tests", or undefined follow-up placeholder remains. Every product mutation task has a concrete test cycle and interface.

**Type consistency:** `StageRun` owns orchestration; `RouletteManipulationSession` never resolves rewards; `PendingDeploymentPlan` never owns food/economy; `RunCommandViewModel` is read-only; `RunCommandScreen` sends commands but does not calculate rules.

**Execution route:** Use `superpowers:subagent-driven-development` when an executor with HiGodot access is available; otherwise `superpowers:executing-plans` in a HiGodot-enabled session. Persistent Godot mutation through GitHub text-file APIs is not an allowed substitute.