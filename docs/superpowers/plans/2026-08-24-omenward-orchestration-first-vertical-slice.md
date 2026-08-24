# OMENWARD Orchestration-first Vertical Slice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the smallest current-v4.8 playable orchestration slice that enforces `PREPARE → COMMIT → BATTLE → REVIEW`, uses a real three-reel `SpinSession` with row/column manipulation, stages deployment before one atomic irreversible confirm, and presents the result through a Focus-adaptive player UI without deleting the existing debug HUD.

**Architecture:** Keep `GameApplication → StageRun → existing services` as the composition spine. Add pure transient `RefCounted` domain state for Run Command phase, physical roulette state/session, and pending deployment planning; integrate those through `StageRun`, then bind a new player-facing Run Command presentation. Existing `RouletteService.resolve_board_snapshot()` remains the judgment/reward compatibility seam; existing battle/economy/building services remain authoritative for their current behavior.

**Tech Stack:** Godot 4.7.1 Standard, typed GDScript, Compatibility renderer, GUT 9.7.1, existing Python/headless repository contracts, HiGodot/Godot AI for all persistent Godot authoring, Hera for read-only live QA.

**Spec:** `docs/design/APPROVED_OMENWARD_ORCHESTRATION_FIRST_VERTICAL_SLICE_IMPLEMENTATION_ARCHITECTURE_2026-08-24.md`

## Global Constraints

- Base authority: fresh `alsdmlals4-eng/Base` current `main` and `AGENTS.md` at execution start.
- Project authority: fresh OMENWARD `main`, `AGENTS.md`, `docs/CURRENT_CONFIRMED_DECISIONS.md`, `docs/ACTIVE_CONTEXT.md`, current GDD/Project Core and this plan's Spec.
- Current product identity remains `건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다`.
- Run Command order is `PREPARE → COMMIT → BATTLE → REVIEW`.
- Roulette is a player-constructed probability engine, not gambling fantasy; scripted fake near-miss remains forbidden.
- Three reels are not mapped 1:1 to three lanes.
- Physical reel core follows `docs/design/APPROVED_ROULETTE_CORE_RULES.md`: each reel starts with three X; one active TokenSource contributes one source-bound token to each reel; vertical move rotates one reel cursor; horizontal move circularly swaps the three visible tokens in one row and persists in live reel state.
- Board resolution preserves the current center-row gate and 8-line count through the existing resolver/service compatibility seam.
- COMMIT is staged; actual deployment does not happen until one final confirm.
- After actual commit: recall, sell-deployed and cross-lane move remain forbidden.
- `ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION`: do not select final economy numerics in this implementation package.
- Existing current runtime numerics remain implementation inputs only; do not promote them to final product balance.
- Persistent Godot Script/Scene/Resource/project mutation must be performed only through HiGodot/Godot AI. GitHub text tooling may carry the plan/review packet but must not substitute for HiGodot persistent Godot authoring.
- GUT is the deterministic GDScript test authority for new behavior. A zero-test run is failure.
- Hera is `LIVE_QA_AND_OBSERVABILITY_ONLY`; tracked-source delta attributable to Hera must be `NONE`.
- Do not delete or repurpose `scripts/ui/stage_hud.gd` / `scenes/ui/stage_hud.tscn` in this slice. They remain technical/debug evidence surfaces.
- No new AutoLoad, generic ability framework, paid service, new external addon, or second Godot mutation authority.
- Image generation is not part of this plan.
- Device/human/accessibility checks not actually run remain `NOT_RUN`.

---

## File Responsibility Map

### Create

- `scripts/run_command/run_command_state.gd`
  - Pure legal phase transition state; no economy/battle/UI dependencies.
- `scripts/roulette/roulette_token_instance.gd`
  - One physical token instance with stable identity/source/reward payload.
- `scripts/roulette/roulette_reel_state.gd`
  - One circular reel, cursor, visibility, vertical shift, source-token insertion and horizontal-row slot replacement primitive.
- `scripts/roulette/roulette_run_state.gd`
  - Exactly three reels, cross-reel token-ID uniqueness, stopped-copy creation and horizontal row rotation.
- `scripts/roulette/roulette_spin_snapshot.gd`
  - Deep immutable stopped snapshot and row-major 3×3 projection.
- `scripts/roulette/roulette_spin_session.gd`
  - READY/STOPPED/CONFIRMED transaction state, working live-reel copy, move preview, move resource consumption and final board.
- `scripts/units/pending_deployment_plan.gd`
  - Editable reward-index → lane assignments for COMMIT; no actual deployment mutation.
- `scripts/ui/run_command_view_model.gd`
  - Player-safe snapshot projection; strips raw debug IDs and exposes one focus/CTA state.
- `scripts/ui/run_command_screen.gd`
  - Presentation event forwarding and rendering only.
- `scenes/ui/run_command_screen.tscn`
  - New player-facing top HUD + focus-adaptive lower deck shell.
- `tests/gut/test_run_command_state.gd`
- `tests/gut/test_roulette_physical_domain.gd`
- `tests/gut/test_roulette_spin_session.gd`
- `tests/gut/test_pending_deployment_plan.gd`
- `tests/gut/test_stage_run_orchestration.gd`
- `tests/gut/test_run_command_view_model.gd`

### Modify

- `scripts/roulette/roulette_service.gd`
  - Add paid-spin open/finalize seams while preserving current `spin()` compatibility behavior and `resolve_board_snapshot()` semantics.
- `scripts/core/stage_run.gd`
  - Compose RunCommandState, live reel state/session and pending deployment plan; gate `advance()` by phase.
- `scripts/units/deployment_service.gd`
  - Add read-only batch preflight and one batch apply primitive; keep current single `deploy()` for compatibility.
- `scripts/battle/battle_simulator.gd`
  - Add read-only `can_spawn_unit()` and deterministic batch preflight/helper only if RED proves StageRun cannot guarantee all-or-none deployment with current surfaces.
- `scripts/presentation/scene_binder.gd`
  - Bind run to new player-facing screen in addition to existing debug StageHud.
- `scenes/main/main.tscn`
  - Instance the new Run Command screen without removing the debug HUD; debug HUD visibility defaults to developer/evidence mode rather than player-primary mode.
- `tests/headless/stage_run_test.gd`
  - Replace the immediate-deployment current-behavior assertion with historical compatibility coverage plus new staged-commit regression boundary once the new current path is Green.
- `tests/headless/economy_roulette_test.gd`
  - Preserve direct service compatibility while adding no new final balance assertions.

### Inspect but do not edit unless a failing test proves necessary

- `scripts/core/combat_clock.gd`
- `scripts/core/stage_economy.gd`
- `scripts/waves/wave_director.gd`
- `scripts/buildings/building_service.gd`
- `scripts/battle/lane_state.gd`
- current visual/text/roulette owner docs

---

### Task 1: Isolate the Execution Workspace and Establish Baseline Evidence

**Files:**
- Inspect: all files in the responsibility map.
- Create first Red test only after the isolated workspace is confirmed.

**Interfaces:**
- Consumes: current remote `main` exact SHA.
- Produces: clean isolated execution worktree/branch and baseline test record.

- [ ] **Step 1: Fresh-read authority and work-item state**

Read, in order:

```text
Base/AGENTS.md
OMENWARD/AGENTS.md
OMENWARD/docs/CURRENT_CONFIRMED_DECISIONS.md
OMENWARD/docs/ACTIVE_CONTEXT.md
OMENWARD/docs/design/APPROVED_OMENWARD_ORCHESTRATION_FIRST_VERTICAL_SLICE_IMPLEMENTATION_ARCHITECTURE_2026-08-24.md
OMENWARD/docs/design/APPROVED_ROULETTE_CORE_RULES.md
OMENWARD/docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md
OMENWARD/docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md
```

Fresh-query open PRs/issues. Other open workstreams are read-only. If another current-task implementation PR already owns these same files, stop as `BLOCKED_CONCURRENT_OWNER` rather than taking it over.

- [ ] **Step 2: Create the isolated worktree**

```bash
git fetch origin
git worktree add ../omenward-orchestration-vslice -b runtime/orchestration-first-vslice-20260824 origin/main
cd ../omenward-orchestration-vslice
git rev-parse HEAD
git status --short --branch
```

Expected:

```text
HEAD == fresh origin/main
working tree clean
branch == runtime/orchestration-first-vslice-20260824
```

- [ ] **Step 3: Confirm exact engine/addon inventory before mutation**

Read `project.godot` and verify:

```text
Godot feature = 4.7
res://addons/godot_ai/plugin.cfg enabled
res://addons/gut/plugin.cfg enabled
res://addons/hera_agent_godot/plugin.cfg enabled
```

Do not rewrite addon enablement in this task.

- [ ] **Step 4: Run baseline deterministic contracts**

```bash
python -m unittest discover -s tests/python -v
Godot_v4.7.1-stable_win64.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/stage_run_test.gd
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gdir=res://tests/gut -gexit
```

Expected:

- Existing Python/headless/import suites PASS unless a pre-existing exact-main blocker is captured.
- The GUT command may report no current project tests before Task 2; **that zero-test baseline is evidence only and must not be called PASS for the new feature**.
- If an existing exact-main failure occurs, preserve command/output and classify it before writing feature code.

- [ ] **Step 5: Commit nothing**

Task 1 is evidence-only. Do not create a baseline-only commit.

---

### Task 2: Add the Pure Run Command Phase State

**Files:**
- Create: `scripts/run_command/run_command_state.gd`
- Create: `tests/gut/test_run_command_state.gd`

**Interfaces:**

```gdscript
class_name RunCommandState
extends RefCounted

const PREPARE: StringName = &"prepare"
const COMMIT: StringName = &"commit"
const BATTLE: StringName = &"battle"
const REVIEW_RESULT: StringName = &"review_result"
const REVIEW_MAINTENANCE: StringName = &"review_maintenance"

var phase: StringName = PREPARE

func reset() -> void
func can_transition(next_phase: StringName) -> bool
func transition(next_phase: StringName) -> bool
func is_planning_time() -> bool
func is_battle_time() -> bool
func to_dictionary() -> Dictionary
```

Legal first-slice transitions:

```text
PREPARE -> COMMIT
COMMIT -> PREPARE
COMMIT -> BATTLE
BATTLE -> REVIEW_RESULT
REVIEW_RESULT -> REVIEW_MAINTENANCE
REVIEW_MAINTENANCE -> PREPARE
```

`BATTLE -> PREPARE`, `PREPARE -> BATTLE`, `REVIEW_RESULT -> BATTLE` and unknown phase names are rejected.

- [ ] **Step 1: Write the failing GUT test**

Create `tests/gut/test_run_command_state.gd`:

```gdscript
extends GutTest

const RunCommandStateScript = preload("res://scripts/run_command/run_command_state.gd")

func test_starts_in_prepare_and_marks_planning_time() -> void:
    var state = RunCommandStateScript.new()
    assert_eq(state.phase, &"prepare")
    assert_true(state.is_planning_time())
    assert_false(state.is_battle_time())

func test_only_approved_phase_edges_are_accepted() -> void:
    var state = RunCommandStateScript.new()
    assert_false(state.transition(&"battle"))
    assert_true(state.transition(&"commit"))
    assert_true(state.transition(&"battle"))
    assert_true(state.transition(&"review_result"))
    assert_true(state.transition(&"review_maintenance"))
    assert_true(state.transition(&"prepare"))

func test_invalid_transition_does_not_mutate_phase() -> void:
    var state = RunCommandStateScript.new()
    assert_false(state.transition(&"review_result"))
    assert_eq(state.phase, &"prepare")
```

- [ ] **Step 2: Run Red**

```bash
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_run_command_state.gd -gexit
```

Expected: >0 tests discovered and fail because the new script/contract is missing.

- [ ] **Step 3: Implement the minimal phase object through HiGodot**

Implementation rules:

```gdscript
func reset() -> void:
    phase = PREPARE

func is_planning_time() -> bool:
    return phase != BATTLE

func is_battle_time() -> bool:
    return phase == BATTLE
```

`can_transition()` uses an explicit phase→allowed array table. It must not reference `StageRun`, economy, UI, Scene nodes or BattleSimulator.

- [ ] **Step 4: Run Green**

Run the same focused GUT command. Expected: 3/3 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/run_command/run_command_state.gd tests/gut/test_run_command_state.gd
git commit -m "feat: add run command phase state"
```

---

### Task 3: Add Physical Three-Reel State and Immutable Snapshot

**Files:**
- Create: `scripts/roulette/roulette_token_instance.gd`
- Create: `scripts/roulette/roulette_reel_state.gd`
- Create: `scripts/roulette/roulette_run_state.gd`
- Create: `scripts/roulette/roulette_spin_snapshot.gd`
- Create: `tests/gut/test_roulette_physical_domain.gd`

**Interfaces:**

```gdscript
class_name RouletteTokenInstance
extends RefCounted

const NORMAL_X: StringName = &"normal_x"
const SOURCE_BOUND: StringName = &"source_bound"
const GOLD: StringName = &"gold"

var token_instance_id: StringName
var kind: StringName
var symbol_id: StringName
var source_building_instance_id: StringName
var source_tier_id: StringName
var reward_payload: Dictionary

func duplicate_deep() -> RouletteTokenInstance
func to_dictionary() -> Dictionary
```

```gdscript
class_name RouletteReelState
extends RefCounted

const MIN_LENGTH := 3
var reel_id: StringName
var tokens: Array = []
var cursor := 0

func validation_errors() -> PackedStringArray
func normalized_index(index: int) -> int
func visible_tokens() -> Array
func shift_cursor(delta: int) -> void
func replace_lowest_normal_x_or_append(token: RouletteTokenInstance) -> int
func token_index_for_visible_row(row: int) -> int
func replace_token_at(index: int, token: RouletteTokenInstance) -> void
func duplicate_deep() -> RouletteReelState
func to_dictionary() -> Dictionary
```

```gdscript
class_name RouletteRunState
extends RefCounted

const REEL_IDS := [&"left", &"center", &"right"]
var reels: Array = []

static func initial_x_state() -> RouletteRunState
func validation_errors() -> PackedStringArray
func add_source(source: Dictionary) -> void
func deterministic_stopped_copy(base_seed: int, spin_seed: int) -> RouletteRunState
func rotate_visible_row(row: int, direction: int) -> bool
func board_tokens() -> Array
func duplicate_deep() -> RouletteRunState
func to_dictionary() -> Dictionary
```

```gdscript
class_name RouletteSpinSnapshot
extends RefCounted

var base_seed := 0
var spin_seed := 0
var paid_cost := 0
var source_snapshot: Array = []
var _stopped_run: RouletteRunState

static func capture(
    live_run: RouletteRunState,
    base_seed: int,
    spin_seed: int,
    paid_cost: int,
    sources: Array,
) -> RouletteSpinSnapshot
func stopped_run_copy() -> RouletteRunState
func board_copy() -> Array
func board_symbol_ids() -> Array[StringName]
func to_dictionary() -> Dictionary
```

- [ ] **Step 1: Write Red tests for core physical invariants**

`tests/gut/test_roulette_physical_domain.gd` must contain these concrete tests:

```text
initial_x_state has exactly 3 reels, each length 3, all NORMAL_X
all token IDs are unique across all three reels
one source adds one SOURCE_BOUND token to each reel
source addition replaces array-index-0 X before later X regardless of cursor
when no NORMAL_X remains, a new source token appends
cursor -1 wraps to last index and cursor length wraps to zero
visible_tokens always returns 3 wrapped tokens for lengths 3, 4 and 7
vertical shift changes only the selected reel cursor
horizontal right rotation moves right visible token -> left, left -> center, center -> right
horizontal left rotation is the inverse
horizontal rotation changes no reel length and no cursor
horizontal rotation moves token ID/source/payload together
same base seed + spin seed returns identical stopped cursors and board
snapshot is unchanged after live-run mutation
snapshot getters return deep copies
board projection is row-major left/center/right for rows 0,1,2
```

Use fixed source fixtures:

```gdscript
var source_a := {
    "symbol_id": &"warrior",
    "reward_archetype_id": &"shield_guard",
    "source_tier_id": &"tier_1",
    "source_weight": 1,
    "source_building_id": &"lumern_middle:rear",
}
```

- [ ] **Step 2: Run Red**

```bash
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_roulette_physical_domain.gd -gexit
```

Expected: >0 tests discovered and fail on missing physical-domain scripts.

- [ ] **Step 3: Implement token and reel through HiGodot**

`initial_x_state()` uses fixed initial IDs:

```text
x:left:0 x:left:1 x:left:2
x:center:0 x:center:1 x:center:2
x:right:0 x:right:1 x:right:2
```

A source token ID is deterministic per source and reel:

```text
source:<source_building_id>:left
source:<source_building_id>:center
source:<source_building_id>:right
```

`add_source()` must be idempotent: if that source token already exists in a reel, it does not add a duplicate.

- [ ] **Step 4: Implement row rotation exactly as current canon**

For `direction == 1` (right):

```gdscript
var indexes := [
    reels[0].token_index_for_visible_row(row),
    reels[1].token_index_for_visible_row(row),
    reels[2].token_index_for_visible_row(row),
]
var left = reels[0].tokens[indexes[0]]
var center = reels[1].tokens[indexes[1]]
var right = reels[2].tokens[indexes[2]]
reels[0].replace_token_at(indexes[0], right)
reels[1].replace_token_at(indexes[1], left)
reels[2].replace_token_at(indexes[2], center)
```

For `direction == -1`, rotate the opposite way. Reject row outside `0..2` and direction outside `-1/1` without mutation.

- [ ] **Step 5: Implement deterministic stopped copy and snapshot**

Use explicit fixed reel salts, not runtime string hashing:

```gdscript
const REEL_SALTS := [0x13579BDF, 0x2468ACE0, 0x10203040]
```

For each reel create a local `RandomNumberGenerator`, seed it from `base_seed ^ spin_seed ^ REEL_SALTS[index]`, and select `0..tokens.size()-1`. No shared mutable RNG stream.

`RouletteSpinSnapshot.capture()` deep-copies the stopped run and `sources.duplicate(true)`. Every getter returns another deep copy.

- [ ] **Step 6: Run Green plus legacy roulette regression**

```bash
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_roulette_physical_domain.gd -gexit
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd
```

Expected: focused GUT PASS and existing direct roulette/economy contract remains PASS.

- [ ] **Step 7: Commit**

```bash
git add scripts/roulette/roulette_token_instance.gd \
        scripts/roulette/roulette_reel_state.gd \
        scripts/roulette/roulette_run_state.gd \
        scripts/roulette/roulette_spin_snapshot.gd \
        tests/gut/test_roulette_physical_domain.gd
git commit -m "feat: add physical three-reel roulette state"
```

---

### Task 4: Add SpinSession Manipulation and Preserve Resolver/Payment Compatibility

**Files:**
- Create: `scripts/roulette/roulette_spin_session.gd`
- Create: `tests/gut/test_roulette_spin_session.gd`
- Modify: `scripts/roulette/roulette_service.gd`
- Regression: `tests/headless/economy_roulette_test.gd`
- Regression: existing C1/static validators

**Interfaces:**

```gdscript
class_name RouletteSpinSession
extends RefCounted

const READY: StringName = &"ready"
const STOPPED: StringName = &"stopped"
const CONFIRMED: StringName = &"confirmed"

var status: StringName = READY
var lucky_free_moves := 0
var stored_move_tickets := 0
var _snapshot: RouletteSpinSnapshot
var _working_run: RouletteRunState

func stop_on(snapshot: RouletteSpinSnapshot, lucky_moves: int, stored_moves: int) -> bool
func preview_vertical(reel_index: int, direction: int) -> Dictionary
func execute_vertical(reel_index: int, direction: int) -> bool
func preview_horizontal(row: int, direction: int) -> Dictionary
func execute_horizontal(row: int, direction: int) -> bool
func final_board_symbols() -> Array[StringName]
func confirm() -> bool
func remaining_move_count() -> int
func to_dictionary() -> Dictionary
```

`RouletteService` adds compatibility seams:

```gdscript
func try_open_paid_spin(spin_seed: int) -> Dictionary
func finalize_physical_spin(
    board_input: Array,
    source_snapshot: Array,
    resolution_seed: int,
    paid_cost: int,
) -> RouletteSpinResult
```

`try_open_paid_spin()` returns:

```gdscript
{
    "accepted": true_or_false,
    "failure_reason": StringName,
    "spin_seed": spin_seed,
    "paid_cost": actual_paid_cost,
    "sources": deep_source_snapshot,
}
```

It charges exactly once only when accepted. It does not generate a board, reward, gold payout or input-log result.

`finalize_physical_spin()` resolves/finalizes exactly once, applies existing gold/reward/legendary rules through the current resolver path and appends the result log. It does not charge spin cost.

Existing public `spin(seed_input)` remains a compatibility wrapper using the legacy independent board generator so historical direct service tests are not silently redefined in this task.

- [ ] **Step 1: Write SpinSession Red tests**

Concrete cases:

```text
stop_on enters STOPPED with deep working copy
preview vertical changes returned board but not session state or move count
preview horizontal changes returned board but not session state or move count
execute consumes lucky_free_moves before stored_move_tickets
execute with no move resource returns false and does not mutate board
executed vertical persists cursor shift
executed horizontal persists live working reel token exchange
confirm moves STOPPED -> CONFIRMED only once
all execute/preview methods reject after CONFIRMED
final_board_symbols returns exactly 9 row-major symbols
```

- [ ] **Step 2: Run Red**

Run focused GUT and require >0 failing tests.

- [ ] **Step 3: Implement session through HiGodot**

Move consumption helper:

```gdscript
func _consume_one_move() -> bool:
    if lucky_free_moves > 0:
        lucky_free_moves -= 1
        return true
    if stored_move_tickets > 0:
        stored_move_tickets -= 1
        return true
    return false
```

Preview always duplicates `_working_run`, applies the move to the duplicate and returns only a dictionary/board projection. It never calls `_consume_one_move()`.

- [ ] **Step 4: Add payment/finalization Red coverage before modifying service**

Extend `tests/gut/test_roulette_spin_session.gd` with a minimal fake economy/buildings/manifest fixture and assert:

```text
rejected open does not spend gold
accepted open spends exactly SPIN_COST once
open does not append roulette result log
finalize does not spend a second time
finalize appends one result log
gold payout is applied once
legacy spin(seed) output remains deterministic for identical legacy fixture
```

Run Red; expected failure is missing `try_open_paid_spin`/`finalize_physical_spin`.

- [ ] **Step 5: Implement service seams through HiGodot**

Do not move final balance constants. Keep existing `SPIN_COST`, current gold payout and `resolve_board_snapshot()` behavior intact.

- [ ] **Step 6: Run Green and current C1 regressions**

```bash
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_roulette_spin_session.gd -gexit
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/stage_run_test.gd
python tools/validate_c1_roulette.py
python -m unittest tests.python.test_c1_roulette_contract -v
```

Expected: all exit `0`.

- [ ] **Step 7: Commit**

```bash
git add scripts/roulette/roulette_spin_session.gd \
        scripts/roulette/roulette_service.gd \
        tests/gut/test_roulette_spin_session.gd
git commit -m "feat: add manipulable roulette spin sessions"
```

---

### Task 5: Add Editable PendingDeploymentPlan and Atomic Batch Preflight

**Files:**
- Create: `scripts/units/pending_deployment_plan.gd`
- Create: `tests/gut/test_pending_deployment_plan.gd`
- Modify: `scripts/units/deployment_service.gd`
- Modify only if RED requires it: `scripts/battle/battle_simulator.gd`

**Interfaces:**

```gdscript
class_name PendingDeploymentPlan
extends RefCounted

const LANE_IDS := [&"top", &"middle", &"bottom"]
var assignments := {}

func assign(reward_index: int, lane_id: StringName, reward_count: int) -> bool
func clear(reward_index: int) -> bool
func lane_for(reward_index: int) -> StringName
func assigned_indexes() -> PackedInt32Array
func is_complete_for(reward_count: int) -> bool
func clear_all() -> void
func to_dictionary() -> Dictionary
```

`DeploymentService` adds:

```gdscript
func can_deploy_batch(cards: Array, lane_ids: Array[StringName]) -> Dictionary
func deploy_batch(cards: Array, lane_ids: Array[StringName], position: float = 10.0) -> Array
```

`can_deploy_batch()` returns:

```gdscript
{
    "accepted": bool,
    "failure_reason": StringName,
    "total_food": int,
}
```

It must not mutate economy, manifest or deployed cards.

`deploy_batch()` first calls the same preflight, then reserves total food **once**, duplicates and records all deployed cards in reward-index order. It returns an empty array on any preflight failure and makes no mutation.

- [ ] **Step 1: Write PendingDeploymentPlan Red tests**

Concrete cases:

```text
negative reward index rejected
index >= reward_count rejected
invalid lane rejected
assign/reassign before confirm changes only pending plan
clear removes only that assignment
assigned_indexes are sorted ascending
is_complete_for(2) false with one assignment and true with two
clear_all removes all assignments
```

- [ ] **Step 2: Write deployment batch Red tests**

Use current `StageEconomy` + `StageManifest` fixture and two `UnitSpawnDefinition`s.

Assert:

```text
invalid lane -> accepted false, food delta 0, log delta 0, deployed_cards delta 0
aggregate food > capacity -> accepted false with same zero deltas
valid two-card batch -> food reserved by sum once, two cards recorded, two deploy log entries in input order
```

- [ ] **Step 3: Run Red**

Focused GUT must discover >0 tests and fail on missing plan/batch methods.

- [ ] **Step 4: Implement minimal plan and batch preflight through HiGodot**

Do not add sell/recall/cross-lane movement.

- [ ] **Step 5: Decide BattleSimulator helper only from evidence**

Read current `BattleSimulator.spawn_unit()` and `LaneState.add_unit()`. If all failure conditions are fully preflightable from `spawn.archetype_id` and `lane_id`, add only:

```gdscript
func can_spawn_unit(spawn: UnitSpawnDefinition) -> bool:
    return spawn != null and registry.archetypes.has(str(spawn.archetype_id)) and lanes.has(spawn.lane_id)
```

Do **not** add a generic transaction framework. If a Red integration test demonstrates an additional spawn-time failure that can cause partial commit, then add a bounded `spawn_units_atomic()` helper in the same file with preflight-before-mutation semantics.

- [ ] **Step 6: Run Green and legacy deployment regression**

```bash
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_pending_deployment_plan.gd -gexit
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd
```

Expected: all PASS.

- [ ] **Step 7: Commit**

```bash
git add scripts/units/pending_deployment_plan.gd \
        scripts/units/deployment_service.gd \
        scripts/battle/battle_simulator.gd \
        tests/gut/test_pending_deployment_plan.gd
git commit -m "feat: stage atomic deployment plans"
```

If `battle_simulator.gd` did not need modification, omit it from `git add`.

---

### Task 6: Integrate Orchestration into StageRun and Gate Active Time

**Files:**
- Modify: `scripts/core/stage_run.gd`
- Create: `tests/gut/test_stage_run_orchestration.gd`
- Modify: `tests/headless/stage_run_test.gd`

**Interfaces added to `StageRun`:**

```gdscript
var run_command: RunCommandState
var roulette_run_state: RouletteRunState
var roulette_session: RouletteSpinSession
var pending_deployment_plan: PendingDeploymentPlan
var stored_move_tickets := 0
var lucky_free_moves := 0

func command_phase() -> StringName
func request_commit_phase() -> bool
func begin_roulette_spin(seed_input: Dictionary) -> Dictionary
func preview_roulette_vertical(reel_index: int, direction: int) -> Dictionary
func execute_roulette_vertical(reel_index: int, direction: int) -> bool
func preview_roulette_horizontal(row: int, direction: int) -> Dictionary
func execute_roulette_horizontal(row: int, direction: int) -> bool
func confirm_roulette_result() -> RouletteSpinResult
func assign_pending_reward(reward_index: int, lane_id: StringName) -> bool
func clear_pending_assignment(reward_index: int) -> bool
func confirm_deployment_and_start_battle() -> bool
func review_snapshot() -> Dictionary
```

First-slice phase permissions:

```text
construct_home = PREPARE only
begin/preview/execute/confirm roulette = PREPARE only
request_commit_phase = PREPARE -> COMMIT only when no unresolved SpinSession
pending assignment edit = COMMIT only
confirm deployment = COMMIT only
battle mutation via advance = BATTLE only
review_snapshot = REVIEW_RESULT/REVIEW_MAINTENANCE
```

- [ ] **Step 1: Write Red integration tests first**

`test_stage_run_orchestration.gd` creates a real tutorial StageRun and asserts:

```text
start() phase == PREPARE
clock.is_planning == true
advance(60) during PREPARE changes planning time but not current_wave, battle tick, or economy gold
construct_home works in PREPARE and is rejected in BATTLE
begin spin in PREPARE returns accepted and opens STOPPED session
setting stored_move_tickets = 1 enables exactly one executed row/column move in integration fixture
confirm roulette stores result and closes session
request COMMIT succeeds only after session resolved
assigning rewards changes no food/battle/storage truth
reassign works before confirm
confirm with incomplete assignment fails with zero food/battle/storage mutation
complete valid plan confirms all rewards and transitions to BATTLE
advance(60) in BATTLE advances wave/battle/economy active time
battle result transitions to REVIEW_RESULT
advance(60) in REVIEW changes no battle/wave/economy active state
```

For manipulation integration, set `run.stored_move_tickets = 1` directly in the test fixture. Default runtime value remains `0`; this proves the session path without inventing a starting player grant.

- [ ] **Step 2: Run Red**

Focused GUT must fail before `StageRun` integration.

- [ ] **Step 3: Compose new domain in `start()` through HiGodot**

At a successful start:

```text
run_command.reset() -> PREPARE
clock.is_planning = true
roulette_run_state = initial X state
add each current active TokenSource exactly once
roulette_session = null
pending_deployment_plan.clear_all()
stored_move_tickets/lucky_free_moves preserve current run values or reset only according to current run-start contract
```

Do not call legacy `roulette.spin()` from the new player path.

- [ ] **Step 4: Implement phase-gated `advance()`**

At function start:

```gdscript
if result_state != RUNNING:
    return
clock.is_planning = not run_command.is_battle_time()
clock.advance(delta)
if not run_command.is_battle_time():
    return
```

Then reuse the existing WaveDirector/Battle/Building sync/CoreUX/Economy path unchanged below that gate.

When natural battle result occurs, set `result_state` as today **and** transition RunCommandState to `REVIEW_RESULT` before returning player-facing review data. If current `StageRun` result semantics immediately stop all `advance()`, review remains a read-only post-result state; do not fake a running battle.

- [ ] **Step 5: Implement spin orchestration**

`begin_roulette_spin()`:

1. Require PREPARE and no unresolved session/pending reward.
2. Add any currently active TokenSources not yet represented in live reels; do not implement source removal in this first slice unless a current test requires it.
3. Call `roulette.try_open_paid_spin()` once.
4. Capture `RouletteSpinSnapshot` from the live reel state and returned source snapshot.
5. Create a new session and pass current lucky/stored move counts.
6. Do not resolve reward yet.

`confirm_roulette_result()`:

1. Require STOPPED session.
2. Copy the session's working run back into `roulette_run_state` so horizontal/vertical executed moves persist.
3. Call `roulette.finalize_physical_spin()` with final board, snapshot sources/cost and deterministic resolution seed.
4. Store resulting unit rewards through existing `store_roulette_result()`.
5. Pull remaining move counts back into StageRun.
6. Confirm/close the session.

- [ ] **Step 6: Implement staged deployment orchestration**

`confirm_deployment_and_start_battle()` must preflight every pending reward/lane and aggregate food before any mutation. On failure, keep phase COMMIT and leave storage, food, battle units and manifest log unchanged.

On success:

```text
deployment batch apply
→ battle spawn using deployed clones
→ remove committed pending rewards in descending storage index order
→ clear pending plan
→ transition COMMIT -> BATTLE
→ clock.is_planning = false
```

- [ ] **Step 7: Update the old headless stage test without erasing history**

The old assertion `deploy_next_roulette_reward()` proves the historical immediate prototype. Keep a direct compatibility test for the method only if it remains intentionally callable by debug code, but add explicit text that the **current player path** uses staged commit. Do not use the legacy immediate method from the new player-facing scene.

- [ ] **Step 8: Run Green and full focused regression**

```bash
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_stage_run_orchestration.gd -gexit
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/stage_run_test.gd
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd
```

Expected: all PASS with >0 GUT tests discovered.

- [ ] **Step 9: Commit**

```bash
git add scripts/core/stage_run.gd \
        tests/gut/test_stage_run_orchestration.gd \
        tests/headless/stage_run_test.gd
git commit -m "feat: orchestrate prepare commit battle review"
```

---

### Task 7: Add a Player-safe ViewModel and Focus-adaptive Run Command Screen

**Files:**
- Create: `scripts/ui/run_command_view_model.gd`
- Create: `scripts/ui/run_command_screen.gd`
- Create: `scenes/ui/run_command_screen.tscn`
- Create: `tests/gut/test_run_command_view_model.gd`
- Modify: `scripts/presentation/scene_binder.gd`
- Modify: `scenes/main/main.tscn`
- Preserve: `scripts/ui/stage_hud.gd`
- Preserve: `scenes/ui/stage_hud.tscn`

**Interfaces:**

```gdscript
class_name RunCommandViewModel
extends RefCounted

func snapshot(run: Variant) -> Dictionary
```

Required top-level dictionary:

```gdscript
{
    "phase": String,
    "top_hud": {
        "gold": int,
        "food_used": int,
        "food_cap": int,
        "wave": int,
        "forecast_summary": String,
    },
    "focus": {
        "kind": String,
        "question": String,
        "primary_cta": String,
        "primary_cta_enabled": bool,
        "block_reason": String,
    },
    "roulette": {
        "visible": bool,
        "board": Array,
        "move_count": int,
        "can_manipulate": bool,
    },
    "commit": {
        "visible": bool,
        "rewards": Array,
        "assignments": Dictionary,
        "irreversible_warning": String,
    },
    "battle": {"visible": bool},
    "review": {"visible": bool, "blocks": Array},
}
```

It must not expose:

```text
source_building_ids
reward_archetype_ids as raw debug list
unit IDs
target IDs
raw internal cause codes
raw Token Ledger weights
```

- [ ] **Step 1: Write ViewModel Red tests**

Use a real StageRun or minimal deterministic fake and assert:

```text
PREPARE question = 다가오는 문제를 보고 무엇을 바꿀 것인가?
COMMIT question = 지금 얻은 병력을 어느 전선에 되돌릴 수 없게 투입할 것인가?
BATTLE question = 지금 전술적으로 개입할 가치가 있는 순간인가?
REVIEW question = 내 설계와 배치가 왜 이런 결과를 만들었는가?
exactly one primary CTA string is non-empty in PREPARE/COMMIT/REVIEW
roulette visible only in roulette PREPARE focus
commit surface visible only in COMMIT
raw debug keys do not exist anywhere in JSON.stringify(snapshot)
```

- [ ] **Step 2: Run Red**

Focused GUT must fail before ViewModel exists.

- [ ] **Step 3: Implement ViewModel through HiGodot**

Keep copy/block-reason mapping in presentation-safe language. Do not recalculate combat, probability, reward or eligibility rules in UI code.

- [ ] **Step 4: Build the new scene through HiGodot**

At 960×540 reference:

```text
Top HUD / compact forecast: upper strip
Battlefield: remains visible behind/above UI and retains primary visual mass
Lower Control Deck: 25~32% exploration
Roulette focus: 3×3 center + 12 direct arrows + one action area
Commit focus: reward/storage list + three-lane assignment controls + irreversible warning + one CTA
Battle focus: no build/spin/commit mutation controls
Review focus: five causal blocks + next transition CTA
```

Use Godot Containers for lower-deck internal layout where practical. Do not hardcode every child to absolute pixel positions like the debug StageHud.

- [ ] **Step 5: Wire events as forwarding only**

`run_command_screen.gd` event methods call only `StageRun` public orchestration methods, for example:

```gdscript
func _on_spin_pressed() -> void:
    run.begin_roulette_spin({"seed": _next_spin_seed()})

func _on_row_move_pressed(row: int, direction: int) -> void:
    run.execute_roulette_horizontal(row, direction)

func _on_confirm_result_pressed() -> void:
    run.confirm_roulette_result()

func _on_commit_pressed() -> void:
    run.confirm_deployment_and_start_battle()
```

The screen does not mutate `run.economy`, `run.battle`, `run.pending_roulette_rewards`, reel arrays or phase fields directly.

- [ ] **Step 6: Bind the new screen while preserving debug HUD**

`SceneBinder` binds `UI/RunCommandScreen` if present. `main.tscn` instances the new scene. The debug StageHud stays available but must not be the player-primary surface in the runtime evidence configuration.

- [ ] **Step 7: Run Green, import and UI parse**

```bash
Godot_v4.7.1-stable_win64.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gtest=res://tests/gut/test_run_command_view_model.gd -gexit
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gdir=res://tests/gut -gexit
```

Expected: import/parse PASS, >0 GUT tests, all Green.

- [ ] **Step 8: Commit**

```bash
git add scripts/ui/run_command_view_model.gd \
        scripts/ui/run_command_screen.gd \
        scenes/ui/run_command_screen.tscn \
        tests/gut/test_run_command_view_model.gd \
        scripts/presentation/scene_binder.gd \
        scenes/main/main.tscn
git commit -m "feat: add focus-adaptive run command screen"
```

---

### Task 8: Full Verification, Adversarial Review, Runtime Evidence and PR Handoff

**Files:**
- No feature expansion.
- Add/update only repository evidence files required by current project workflow after actual results exist.

**Interfaces:**
- Consumes: exact implementation branch HEAD.
- Produces: exact-head verification record and ready-for-review implementation PR; no completion claim before required gates.

- [ ] **Step 1: Run the full automated matrix on exact HEAD**

```bash
git status --short
git rev-parse HEAD
python -m unittest discover -s tests/python -v
Godot_v4.7.1-stable_win64.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64.exe --headless --path . -s addons/gut/gut_cmdln.gd -gdir=res://tests/gut -gexit
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd
Godot_v4.7.1-stable_win64.exe --headless --path . -s res://tests/headless/stage_run_test.gd
git diff --check origin/main...HEAD
```

A GUT run with zero discovered tests is FAIL.

- [ ] **Step 2: Determinism replay**

Run the StageRun orchestration integration fixture twice with identical seed/input command sequence. Serialize these observables and require byte-identical JSON:

```text
stopped reel state
executed move sequence
final board
roulette result
pending deployment plan before confirm
actual deployment log after confirm
battle event sequence used by the fixture
review snapshot
```

Do not collapse results into a weighted score.

- [ ] **Step 3: Run five full adversarial review loops**

Each loop rereads the entire current changed state and checks:

```text
Loop 1 — canon/phase semantics: PREPARE/COMMIT/BATTLE/REVIEW authority and no forbidden transition
Loop 2 — transaction integrity: no double spin charge, no preview mutation, no partial deployment commit
Loop 3 — deterministic physical roulette: token identity, reel persistence, horizontal/vertical semantics, snapshot immutability
Loop 4 — presentation leakage: one active work surface, one primary CTA, no raw debug IDs/weights, full three-lane visibility contract
Loop 5 — regression/rollback/evidence ceiling: existing services/debug HUD preserved, economy numerics not promoted, NOT_RUN remains NOT_RUN
```

Any new blocking finding returns review to Loop 1 after correction and reruns impacted tests.

- [ ] **Step 4: Hera live QA only after Green**

Before Hera:

```bash
git status --short
git diff --name-only
```

Use Hera only for:

```text
run/stop
runtime tree readback
semantic input/click
state assertions
screenshots
runtime diagnostics
```

Capture at least 960×540, 1280×720 and 1920×1080 when the local runtime surface supports those sizes. Verify:

```text
three lanes remain visible
lower deck is secondary to battlefield
PREPARE/COMMIT/BATTLE/REVIEW focus changes are visible
only one primary CTA is visually dominant
build/spin/commit mutation controls are closed in BATTLE
```

After Hera:

```bash
git status --short
git diff --name-only
```

Require `HERA_TRACKED_SOURCE_DELTA = NONE`.

- [ ] **Step 5: Record evidence ceilings exactly**

Allowed claims after successful execution:

```text
AUTOMATED_CONTRACTS = PASS
GODOT_IMPORT_PARSE = PASS
GUT = PASS_WITH_NONZERO_TESTS
DETERMINISM_FIXTURE = PASS
HERA_RUNTIME_SMOKE = PASS if actually run
```

Do not claim without direct evidence:

```text
WINDOWS_RELEASE_READY
ANDROID_READY
ACCESSIBILITY_PASS
HUMAN_USABILITY_PASS
PLAYER_EXPERIENCE_PASS
FINAL_BALANCE_PASS
FINAL_UI_PIXEL_GEOMETRY_APPROVED
```

- [ ] **Step 6: Push and open the implementation PR**

```bash
git push -u origin runtime/orchestration-first-vslice-20260824
```

PR body must include:

```text
Authority: OMW-PLAN-20260824-ORCHESTRATION-FIRST-VSLICE-01
Base SHA / implementation HEAD SHA
Red evidence commands and intended failures
Green evidence commands and counts
five adversarial review loop result
Hera source-delta result
changed files
explicit NOT_RUN evidence
rollback path
no final balance selection
```

Do not merge locally or bypass repository checks/rulesets.

- [ ] **Step 7: Exact-head remote verification**

Before any merge decision:

```text
PR head SHA == reviewed/tested SHA
required checks success
unresolved review threads = 0
no stale-base conflict
no new unrelated files
```

If remote CI finds a current-task issue, fix only the approved scope through the correct authority and rerun the affected Red/Green/regression gates.

- [ ] **Step 8: Post-merge readback only if current-task merge becomes authorized and eligible**

After a safe merge, read `main` back and verify:

```text
merge commit present
expected files present
current code matches reviewed semantics
no implementation evidence promoted beyond actual runs
```

Then and only then update current implementation status/Notion Production Handoff from actual merged evidence.

---

## Self-review Result

### Spec coverage

- Run Command phases and active-time gating: Tasks 2, 6.
- Physical triple reels, source-bound token identity, vertical/horizontal move, immutable snapshot: Task 3.
- Preview/no-spend and executed move resource consumption: Task 4.
- Existing resolver/payment compatibility and no double charge: Task 4.
- Staged editable COMMIT and no partial preflight failure: Tasks 5, 6.
- Existing battle/economy/building reuse: Tasks 5, 6.
- Player-safe Focus-adaptive lower deck and one CTA: Task 7.
- Debug HUD preservation: Task 7.
- TDD, exact Godot 4.7.1, determinism, 5-loop review, Hera source-delta, evidence ceiling: Task 8.
- Economy drift remains unresolved and no final numeric selection: Global Constraints + Task 8.

### Placeholder scan

No `TBD`, `TODO`, `implement later`, unspecified "appropriate handling", or unbounded generic cleanup instructions are allowed by this plan. Follow-up product systems are explicitly excluded rather than left as placeholders.

### Type consistency

The plan uses one naming chain throughout:

```text
RunCommandState
RouletteTokenInstance
RouletteReelState
RouletteRunState
RouletteSpinSnapshot
RouletteSpinSession
PendingDeploymentPlan
StageRun orchestration API
RunCommandViewModel
RunCommandScreen
```

`StageRun` owns orchestration; UI never writes internal domain fields directly.

## Execution Handoff

Plan is complete when this document and the approved architecture spec are merged into planning canon. Execution then has two valid Superpowers routes:

1. **Subagent-Driven (recommended)** — fresh worker per task with review between tasks; implementation still uses HiGodot for persistent Godot authoring.
2. **Inline Execution** — use `superpowers:executing-plans` in one Codex/HiGodot-capable session with checkpoints.

This ChatGPT session must not bypass the HiGodot single-authority rule by writing `.gd`/`.tscn` through GitHub APIs.
