# OMENWARD V2 R1+R2 Roulette Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve the remotely proven Legacy C1 board judgment behind a pure `RouletteBoardResolver` seam and add an isolated, deterministic V2 three-reel runtime domain through `RouletteSpinSession` without connecting it to buildings, economy, UI, rewards, or `StageRun`.

**Architecture:** `RouletteService` remains the Legacy runtime orchestrator for this package: it keeps paid-spin economy, independent nine-cell generation, legendary state, reward creation, storage handoff, and input logging. It delegates only board judgment to a pure resolver. The new V2 domain is a separate `RefCounted` object graph—token instance → reel state → run state → immutable snapshot → minimal stopped session—and is exercised directly by headless tests, not by the live stage flow.

**Tech Stack:** Godot 4.7.1 Standard, typed GDScript, Compatibility renderer, Python 3.12/3.13 repository validators and mutation tests, GitHub Actions.

## Global Constraints

- Baseline branch: `main`.
- Baseline commit for Plan Mode investigation: `46f6952d275a3fdff010ad6172f8847e1267d470`.
- Governing Issue: `#69`.
- Current authority: `V2_CANON_CURRENT_BY_PR_57_MERGE` and the GM-01~GM-106 integrated decision ledger.
- Current implementation state: `V2_IMPLEMENTATION_NOT_STARTED` until an implementation PR is merged and separately documented.
- Product code is not authorized by this plan document alone; Codex must first submit the read-only Plan Mode proposal required by Issue #69.
- Keep `RouletteService.spin()` on the Legacy independent nine-cell generator in this package.
- Keep `StageRun`, building events, economy, storage, deployment, UI, Scene, Resource data, and assets disconnected from the V2 reel domain.
- Do not delete, weaken, rename away, or reinterpret the current Legacy C1 regression cases or remote evidence.
- `RouletteBoardResolver` must not own economy, UI, legendary-use state, reward storage, `StageRun`, or input logging.
- Token instance IDs are injected by the caller; this package does not introduce a global ID generator.
- Snapshot immutability must be demonstrated by mutation attempts against both the source live state and returned copies.
- New runtime state classes use `RefCounted`, not `Resource`, because this package creates transient deterministic run state and does not serialize or edit it in the inspector.
- No mid-run save, migration schema, external addon, third-party asset, or new AutoLoad.
- Use Red → Green → Refactor for each task and commit only after the task-specific tests pass.
- Do not use `V2_IMPLEMENTED`, `V2_PROVEN`, `CORE_LOCK_V2`, `MVP_COMPLETE`, or human-play claims.

---

## File Responsibility Map

### Create during the implementation PR

- `scripts/roulette/roulette_board_resolution.gd`
  - Pure resolver output DTO before Legacy legendary conversion and reward-object creation.
- `scripts/roulette/roulette_board_resolver.gd`
  - Central-row gate, completed-line count, base rank, gold payout, and deterministic source choice.
- `scripts/roulette/roulette_token_instance.gd`
  - One runtime token with injected unique ID, kind, symbol, source metadata, and deep-copy behavior.
- `scripts/roulette/roulette_reel_state.gd`
  - One circular reel, cursor normalization, wrapped three-token visibility, and lowest-stable-index `NORMAL_X` replacement or append.
- `scripts/roulette/roulette_run_state.gd`
  - Exactly three ordered reels, cross-reel token-ID uniqueness, deterministic independent stop indices, and deep copy.
- `scripts/roulette/roulette_spin_snapshot.gd`
  - Deep immutable capture of stopped reels plus row-major 3×3 board projection.
- `scripts/roulette/roulette_spin_session.gd`
  - Minimal stopped-session identity, original snapshot, and isolated working-state copy; no moves or confirmation.
- `tests/headless/roulette_resolver_preservation_test.gd`
  - Direct pure resolver golden cases and Legacy service-adapter equality.
- `tests/headless/roulette_v2_domain_test.gd`
  - R2 invariant, determinism, deep-copy, snapshot, and session tests.
- `tools/validate_v2_roulette_domain.py`
  - Static contract for required V2 domain files, ownership boundaries, interfaces, and regression phrases.
- `tests/python/test_v2_roulette_domain_contract.py`
  - Mutation tests proving the V2 static contract rejects missing ownership and invariant markers.

### Modify during the implementation PR

- `scripts/roulette/roulette_service.gd`
  - Instantiate the resolver, delegate board judgment, then retain Legacy legendary conversion and reward creation.
- `tools/validate_c1_roulette.py`
  - Stop requiring line/rank/gold implementation details inside `RouletteService`; require resolver existence, service delegation, and preserved Legacy tests instead.
- `tests/python/test_c1_roulette_contract.py`
  - Copy the new resolver files into mutation fixtures and add a mutation that rejects loss of service delegation.
- `.github/workflows/validate-omenward-core.yml`
  - Compile and run the new V2 validator and Python mutation test in PR and full-matrix contract jobs.
- `tools/validate_ci_usage_contract.py`
  - Require the fast PR job to run `test_v2_roulette_domain_contract` and `validate_v2_roulette_domain.py` while retaining the existing cost topology.
- `tests/python/test_ci_usage_contract.py`
  - Add a mutation proving removal of the V2 fast contract is rejected.

### Do not modify in the implementation PR

- `scripts/core/stage_run.gd`
- `scripts/buildings/building_service.gd`
- `scripts/core/stage_economy.gd`
- `scripts/ui/**`
- `scenes/**`
- `data/**`
- `resources/**`
- `project.godot`
- V2 canonical design documents

### Separate post-merge documentation PR

After the implementation PR is merged and its exact remote runs are known, update only:

- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/OMENWARD_ROADMAP.md`
- Issue `#69`

The post-merge status must distinguish `R1_R2_DOMAIN_REMOTE_PROVEN` from an unproven V2 playable loop.

---

### Task 1: Freeze the Baseline and Add Resolver Golden Tests

**Files:**
- Create: `tests/headless/roulette_resolver_preservation_test.gd`
- Inspect only: `scripts/roulette/roulette_service.gd`
- Inspect only: `tests/headless/roulette_contract_test.gd`
- Inspect only: `tests/headless/stage_run_test.gd`

**Interfaces:**
- Consumes: existing `RouletteService.resolve_board_snapshot(board, sources, resolution_seed, paid_cost, consume_legendary)`.
- Produces: a golden result table that Task 2 must reproduce through the new resolver and service adapter.

- [ ] **Step 1: Create an isolated implementation worktree**

```bash
git fetch origin
git worktree add ../omenward-r1-r2 -b codex/v2-r1-r2-roulette-foundation origin/main
cd ../omenward-r1-r2
git rev-parse HEAD
git status --short --branch
```

Expected before any code work:

```text
HEAD equals the then-current origin/main
working tree is clean
```

- [ ] **Step 2: Run the existing baseline contracts**

```bash
python tools/validate_c1_roulette.py
python -m unittest tests.python.test_c1_roulette_contract -v
godot --headless --path . --editor --quit
godot --headless --path . -s res://tests/headless/roulette_contract_test.gd
godot --headless --path . -s res://tests/headless/stage_run_test.gd
```

Expected: all commands exit `0`. If local `godot` is not exactly 4.7.1, record `LOCAL_GODOT_NOT_RUN` and rely on the PR Godot job; do not substitute a different engine version as proof.

- [ ] **Step 3: Write the direct resolver preservation test before the resolver exists**

The test must load both scripts and fail because `roulette_board_resolver.gd` does not yet exist:

```gdscript
extends SceneTree

const StageManifest = preload("res://scripts/core/stage_manifest.gd")

func _init() -> void:
    var failures := PackedStringArray()
    var resolver_script: GDScript = load("res://scripts/roulette/roulette_board_resolver.gd") as GDScript
    var service_script: GDScript = load("res://scripts/roulette/roulette_service.gd") as GDScript
    _expect(resolver_script != null and resolver_script.can_instantiate(), "pure roulette board resolver loads", failures)
    _expect(service_script != null and service_script.can_instantiate(), "legacy roulette service still loads", failures)
    if resolver_script != null and resolver_script.can_instantiate():
        _test_middle_gate(resolver_script, failures)
        _test_rank_and_gold_table(resolver_script, failures)
        _test_source_determinism(resolver_script, failures)
    if resolver_script != null and resolver_script.can_instantiate() and service_script != null and service_script.can_instantiate():
        _test_service_adapter_equality(resolver_script, service_script, failures)
    _finish(failures)
```

The concrete cases must include:

| Case | Expected |
|---|---|
| complete top row, incomplete middle row | accepted, no reward outcome |
| all X | no reward outcome |
| one unit line | `common` |
| two unit lines | `elite` |
| three unit lines | `hero` |
| eight unit lines | base `legendary` |
| one gold line at cost 20 | 15 |
| two gold lines at cost 20 | 40 |
| three-or-more gold lines at cost 20 | 100 |
| two matching sources, same base seed and resolution seed | same source IDs |

- [ ] **Step 4: Run the new test and verify Red**

```bash
godot --headless --path . -s res://tests/headless/roulette_resolver_preservation_test.gd
```

Expected: non-zero exit with `pure roulette board resolver loads`.

- [ ] **Step 5: Commit only the failing preservation test**

```bash
git add tests/headless/roulette_resolver_preservation_test.gd
git commit -m "test: lock legacy roulette resolver outcomes"
```

---

### Task 2: Extract the Pure Board Resolver and Preserve the Legacy Adapter

**Files:**
- Create: `scripts/roulette/roulette_board_resolution.gd`
- Create: `scripts/roulette/roulette_board_resolver.gd`
- Modify: `scripts/roulette/roulette_service.gd`
- Modify: `tools/validate_c1_roulette.py`
- Modify: `tests/python/test_c1_roulette_contract.py`
- Test: `tests/headless/roulette_resolver_preservation_test.gd`
- Regression: `tests/headless/roulette_contract_test.gd`
- Regression: `tests/headless/stage_run_test.gd`

**Interfaces:**
- Consumes: `Array` board input, `Array[Dictionary]` sources, base seed, resolution seed, paid cost.
- Produces:

```gdscript
class_name RouletteBoardResolution
extends RefCounted

var accepted := false
var failure_reason: StringName = &""
var board: Array[StringName] = []
var judging_symbol: StringName = &""
var completed_line_count := 0
var rank_id: StringName = &""
var outcome_type: StringName = &"none"
var gold_reward := 0
var paid_cost := 0
var resolution_seed := 0
var source_building_id: StringName = &""
var source_tier_id: StringName = &""
var reward_archetype_id: StringName = &""

func to_dictionary() -> Dictionary
```

```gdscript
class_name RouletteBoardResolver
extends RefCounted

func _init(base_seed: int) -> void
func resolve(
    board_input: Array,
    sources: Array,
    resolution_seed: int,
    paid_cost: int,
) -> RouletteBoardResolution
```

- [ ] **Step 1: Add the resolver output DTO**

Implement `RouletteBoardResolution` with the exact fields above. `to_dictionary()` must return primitive strings, integers, booleans, and arrays only; it must not return `Resource` or `RefCounted` instances.

- [ ] **Step 2: Add the pure resolver**

Move these responsibilities from `RouletteService` into `RouletteBoardResolver`:

```text
BOARD_SIZE
X_SYMBOL
GOLD_SYMBOL
LINE_INDEXES
board copy and validation
middle row gate using indexes 3,4,5
completed line count
base rank mapping
75/200/500 percent gold payout
matching source collection
stable source sort
base_seed XOR resolution_seed source RNG
```

The resolver must not preload or reference:

```text
StageRun
StageEconomy
BuildingService
CoreUxService
RouletteService
UnitSpawnDefinition
```

- [ ] **Step 3: Verify the direct resolver test turns Green before service refactor**

```bash
godot --headless --path . -s res://tests/headless/roulette_resolver_preservation_test.gd
```

Expected: direct resolver cases pass; service-adapter equality may still fail until Step 4.

- [ ] **Step 4: Make `RouletteService` delegate and retain orchestration**

Add:

```gdscript
const RouletteBoardResolverScript = preload("res://scripts/roulette/roulette_board_resolver.gd")
var board_resolver: RouletteBoardResolver
```

Initialize with the manifest seed or `0` when no manifest exists:

```gdscript
board_resolver = RouletteBoardResolverScript.new(int(manifest.seed) if manifest != null else 0)
```

`resolve_board_snapshot(...)` must:

1. Call `board_resolver.resolve(...)`.
2. Copy the pure fields into a new Legacy `RouletteSpinResult`.
3. Return gold results without reward creation.
4. Apply the existing `legendary_generated` and `consume_legendary` conversion after the pure base rank is known.
5. Create `UnitSpawnDefinition` rewards with the existing player-team ownership.
6. Preserve the current public signature and all current observed outputs.

Remove `_completed_line_count`, `_rank_for_lines`, `_gold_reward`, `_matching_sources`, and `_choose_source` from `RouletteService` only after delegation tests pass. Keep Legacy `_generate_board`, weights, economy, logging, legendary state, and `_make_reward` in the service.

- [ ] **Step 5: Update the C1 static validator for the new ownership**

`tools/validate_c1_roulette.py` must require:

```python
REQUIRED_FILES += (
    "scripts/roulette/roulette_board_resolution.gd",
    "scripts/roulette/roulette_board_resolver.gd",
    "tests/headless/roulette_resolver_preservation_test.gd",
)
```

Replace the old requirement that implementation terms live inside the service with these checks:

```text
resolver contains LINE_INDEXES, resolve, _completed_line_count, _rank_for_lines, _gold_reward, _choose_source
service preloads roulette_board_resolver.gd
service calls board_resolver.resolve
service still contains legendary_generated, _make_reward, _generate_board, economy charge and gold credit
preservation test contains middle gate, grade table, gold table, source determinism, service adapter equality
```

Add a rejection if `RouletteBoardResolver` references economy, UI, `StageRun`, or `UnitSpawnDefinition`.

- [ ] **Step 6: Add a C1 mutation for lost delegation**

In `tests/python/test_c1_roulette_contract.py`, copy both new resolver files into temporary fixtures and add:

```python
def test_service_delegation_loss_is_rejected(self) -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = pathlib.Path(directory)
        self._copy_contract_files(root)
        service = root / "scripts" / "roulette" / "roulette_service.gd"
        service.write_text(
            service.read_text(encoding="utf-8").replace(
                "board_resolver.resolve",
                "board_resolver_removed",
                1,
            ),
            encoding="utf-8",
        )
        self.assertTrue(any("resolver delegation" in error for error in validate(root)))
```

- [ ] **Step 7: Run Task 2 verification**

```bash
python tools/validate_c1_roulette.py
python -m unittest tests.python.test_c1_roulette_contract -v
godot --headless --path . -s res://tests/headless/roulette_resolver_preservation_test.gd
godot --headless --path . -s res://tests/headless/roulette_contract_test.gd
godot --headless --path . -s res://tests/headless/stage_run_test.gd
```

Expected: all exit `0`; the existing C1 and stage tests produce the same observable results as baseline.

- [ ] **Step 8: Commit the resolver seam**

```bash
git add scripts/roulette/roulette_board_resolution.gd \
        scripts/roulette/roulette_board_resolver.gd \
        scripts/roulette/roulette_service.gd \
        tests/headless/roulette_resolver_preservation_test.gd \
        tools/validate_c1_roulette.py \
        tests/python/test_c1_roulette_contract.py
git commit -m "refactor: isolate deterministic roulette board resolver"
```

---

### Task 3: Add Token Instances and One Circular Reel

**Files:**
- Create: `scripts/roulette/roulette_token_instance.gd`
- Create: `scripts/roulette/roulette_reel_state.gd`
- Create: `tests/headless/roulette_v2_domain_test.gd`

**Interfaces:**

```gdscript
class_name RouletteTokenInstance
extends RefCounted

const KIND_SYMBOL: StringName = &"symbol"
const KIND_NORMAL_X: StringName = &"normal_x"
const KIND_SOURCE_BOUND_X: StringName = &"source_bound_x"

var token_instance_id: StringName
var kind: StringName
var symbol_id: StringName
var source_building_instance_id: StringName
var source_tier_id: StringName
var payload: Dictionary

func _init(
    assigned_token_instance_id: StringName,
    assigned_kind: StringName,
    assigned_symbol_id: StringName = &"",
    assigned_source_building_instance_id: StringName = &"",
    assigned_source_tier_id: StringName = &"",
    assigned_payload: Dictionary = {},
) -> void
func is_normal_x() -> bool
func is_source_bound_x() -> bool
func duplicate_deep() -> RouletteTokenInstance
func to_dictionary() -> Dictionary
```

```gdscript
class_name RouletteReelState
extends RefCounted

const MIN_LENGTH := 3
const VISIBLE_COUNT := 3

var tokens: Array[RouletteTokenInstance] = []
var cursor := 0

func _init(initial_tokens: Array[RouletteTokenInstance], initial_cursor: int = 0) -> void
func validation_errors() -> PackedStringArray
func normalized_index(index: int) -> int
func visible_tokens() -> Array[RouletteTokenInstance]
func replace_lowest_normal_x_or_append(token: RouletteTokenInstance) -> int
func duplicate_deep() -> RouletteReelState
func to_dictionary() -> Dictionary
```

- [ ] **Step 1: Write Red tests for token and reel invariants**

`roulette_v2_domain_test.gd` must fail before the scripts exist and include these exact cases:

```text
three-token reel is valid
zero-, one-, and two-token reels report min-length validation errors
cursor -1 wraps to last index
cursor length wraps to zero
length 3, 4, and 7 expose exactly three consecutive wrapped tokens
duplicate token ID inside one reel is rejected
replace chooses the lowest array index NORMAL_X even when cursor points elsewhere
SOURCE_BOUND_X is not replaced by general addition
no NORMAL_X appends at the end
replacement keeps reel length and cursor unchanged
append increases length by one and keeps cursor unchanged
deep copy mutation does not affect the source token or source reel
```

- [ ] **Step 2: Run Red**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
```

Expected: non-zero exit with missing token/reel script failures.

- [ ] **Step 3: Implement caller-injected token identity**

Reject empty token IDs through `validation_errors()` rather than generating replacements. `duplicate_deep()` must duplicate the payload with `duplicate(true)` and preserve all IDs and metadata exactly.

- [ ] **Step 4: Implement stable reel semantics**

`visible_tokens()` returns deep copies in this order:

```gdscript
for offset in range(VISIBLE_COUNT):
    result.append(tokens[normalized_index(cursor + offset)].duplicate_deep())
```

`replace_lowest_normal_x_or_append()` searches array indexes from `0` upward, never from cursor order. It replaces only `KIND_NORMAL_X`; otherwise it appends. Return the replaced or appended array index.

- [ ] **Step 5: Run Green and regression**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
godot --headless --path . -s res://tests/headless/roulette_contract_test.gd
```

Expected: both exit `0`.

- [ ] **Step 6: Commit token and reel state**

```bash
git add scripts/roulette/roulette_token_instance.gd \
        scripts/roulette/roulette_reel_state.gd \
        tests/headless/roulette_v2_domain_test.gd
git commit -m "feat: add deterministic roulette token and reel state"
```

---

### Task 4: Add Three-Reel Run State and Deterministic Stop Indices

**Files:**
- Create: `scripts/roulette/roulette_run_state.gd`
- Modify: `tests/headless/roulette_v2_domain_test.gd`
- Reuse: `scripts/core/determinism_service.gd`

**Interfaces:**

```gdscript
class_name RouletteRunState
extends RefCounted

const REEL_COUNT := 3
const REEL_IDS: Array[StringName] = [&"left", &"center", &"right"]

var reels: Array[RouletteReelState] = []

func _init(initial_reels: Array[RouletteReelState]) -> void
func validation_errors() -> PackedStringArray
func deterministic_stop_indices(base_seed: int, spin_seed: int) -> PackedInt32Array
func stopped_copy(base_seed: int, spin_seed: int) -> RouletteRunState
func duplicate_deep() -> RouletteRunState
func to_dictionary() -> Dictionary
```

- [ ] **Step 1: Add Red run-state cases**

```text
exactly three reels are required
duplicate token IDs across different reels are rejected
same base seed + spin seed + reel lengths returns the same three stop indices
a different spin seed changes at least one index across a fixed seed table
each stop index is inside its reel length
stop selection does not mutate the live run
stopped_copy sets each copied reel cursor to its stop index and leaves source cursors unchanged
```

Use at least 64 sequential spin seeds and assert every index for reel lengths 3, 4, and 7 is observed at least once. This is a deterministic coverage smoke, not a statistical fairness proof.

- [ ] **Step 2: Run Red**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
```

Expected: non-zero exit with missing run-state contract messages.

- [ ] **Step 3: Implement independent reel RNG streams**

Derive each reel stop from the package inputs without consuming shared mutable RNG state:

```gdscript
var rng := RandomNumberGenerator.new()
rng.seed = base_seed ^ spin_seed ^ hash(REEL_IDS[reel_index])
index = rng.randi_range(0, reels[reel_index].tokens.size() - 1)
```

Codex must verify Godot 4.7.1 `hash(StringName)` determinism within the supported runtime. If repository standards reject built-in hash stability, use explicit fixed integer salts declared in the class:

```gdscript
const REEL_SALTS := PackedInt64Array([0x13579BDF, 0x2468ACE0, 0x10203040])
```

The proposal must choose one approach before Build; do not switch silently during implementation.

- [ ] **Step 4: Run Green**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
```

Expected: all token, reel, and run-state cases pass.

- [ ] **Step 5: Commit run state**

```bash
git add scripts/roulette/roulette_run_state.gd tests/headless/roulette_v2_domain_test.gd
git commit -m "feat: add deterministic three-reel run state"
```

---

### Task 5: Capture an Immutable Spin Snapshot and Row-Major Board

**Files:**
- Create: `scripts/roulette/roulette_spin_snapshot.gd`
- Modify: `tests/headless/roulette_v2_domain_test.gd`

**Interfaces:**

```gdscript
class_name RouletteSpinSnapshot
extends RefCounted

var spin_seed := 0
var base_seed := 0
var _stopped_run: RouletteRunState
var _board: Array[RouletteTokenInstance] = []

static func capture(live_run: RouletteRunState, base_seed: int, spin_seed: int) -> RouletteSpinSnapshot
func stopped_run_copy() -> RouletteRunState
func board_copy() -> Array[RouletteTokenInstance]
func board_symbol_ids() -> Array[StringName]
func to_dictionary() -> Dictionary
```

- [ ] **Step 1: Add Red snapshot cases**

```text
capture rejects or reports an invalid run state
capture contains exactly three stopped reels
board has exactly nine token copies
board is row-major: left row0, center row0, right row0, then row1, then row2
source run cursor mutation after capture does not change snapshot
source token payload mutation after capture does not change snapshot
mutation of stopped_run_copy does not change snapshot
mutation of board_copy token payload does not change snapshot
same state and seeds produce identical snapshot dictionaries
```

Use distinct symbols such as `L0/L1/L2`, `C0/C1/C2`, and `R0/R1/R2` so row/column transposition cannot pass accidentally.

- [ ] **Step 2: Run Red**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
```

Expected: non-zero exit with missing snapshot cases.

- [ ] **Step 3: Implement private ownership and copy-out access**

Do not expose `_stopped_run` or `_board` directly. Construct the row-major board as:

```gdscript
var visible_by_reel: Array[Array] = []
for reel in stopped_run.reels:
    visible_by_reel.append(reel.visible_tokens())
for row in range(3):
    for reel_index in range(3):
        _board.append((visible_by_reel[reel_index][row] as RouletteTokenInstance).duplicate_deep())
```

Every public getter returns a new deep copy. `to_dictionary()` must build from internal primitives, not from externally mutable references.

- [ ] **Step 4: Run Green**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
```

Expected: snapshot immutability and board projection pass.

- [ ] **Step 5: Commit snapshot**

```bash
git add scripts/roulette/roulette_spin_snapshot.gd tests/headless/roulette_v2_domain_test.gd
git commit -m "feat: capture immutable roulette spin snapshots"
```

---

### Task 6: Add a Minimal Stopped Spin Session Without R4 Transactions

**Files:**
- Create: `scripts/roulette/roulette_spin_session.gd`
- Modify: `tests/headless/roulette_v2_domain_test.gd`

**Interfaces:**

```gdscript
class_name RouletteSpinSession
extends RefCounted

const STATUS_STOPPED: StringName = &"stopped"

var session_id: StringName
var status: StringName = STATUS_STOPPED
var _original_snapshot: RouletteSpinSnapshot
var _working_run: RouletteRunState

func _init(assigned_session_id: StringName, snapshot: RouletteSpinSnapshot) -> void
func validation_errors() -> PackedStringArray
func original_snapshot_dictionary() -> Dictionary
func working_run_copy() -> RouletteRunState
func to_dictionary() -> Dictionary
```

- [ ] **Step 1: Add Red session cases**

```text
empty session ID is invalid
null snapshot is invalid
new session status is stopped
original snapshot dictionary equals capture input
working run begins as a deep copy of the stopped run
mutating a returned working_run_copy does not mutate session state
mutating the live run after capture does not mutate session state
session has no move, confirm, cancel, reward, economy, or storage method
```

The final no-transaction boundary must be protected by the Python static validator in Task 7, not by calling nonexistent GDScript methods.

- [ ] **Step 2: Run Red**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
```

Expected: non-zero exit with missing session cases.

- [ ] **Step 3: Implement the stopped-only seam**

The class may store an internal working copy for future R4 move methods, but it must expose copies only and must not add state transitions in this package.

Forbidden method names in this package:

```text
confirm
cancel
move_horizontal
move_vertical
consume_move
grant_reward
store_reward
spend_gold
```

- [ ] **Step 4: Run Green**

```bash
godot --headless --path . -s res://tests/headless/roulette_v2_domain_test.gd
```

Expected: all R2 domain cases pass.

- [ ] **Step 5: Commit the session seam**

```bash
git add scripts/roulette/roulette_spin_session.gd tests/headless/roulette_v2_domain_test.gd
git commit -m "feat: add stopped roulette spin session seam"
```

---

### Task 7: Add V2 Static Contracts and Mutation Tests

**Files:**
- Create: `tools/validate_v2_roulette_domain.py`
- Create: `tests/python/test_v2_roulette_domain_contract.py`
- Modify: `.github/workflows/validate-omenward-core.yml`
- Modify: `tools/validate_ci_usage_contract.py`
- Modify: `tests/python/test_ci_usage_contract.py`

**Interfaces:**
- Consumes: exact new paths and required ownership markers.
- Produces: fast PR rejection for missing files, leaked ownership, removed invariants, or skipped V2 tests.

- [ ] **Step 1: Write the static validator**

Require all new source and headless test files. Check for these interface markers:

```text
RouletteBoardResolver.resolve
RouletteReelState.MIN_LENGTH
replace_lowest_normal_x_or_append
RouletteRunState.REEL_COUNT
validation_errors
deterministic_stop_indices
RouletteSpinSnapshot.capture
stopped_run_copy
board_copy
RouletteSpinSession.STATUS_STOPPED
working_run_copy
```

Reject these ownership leaks from the pure resolver and V2 domain files:

```text
StageRun
StageEconomy
BuildingService
CoreUxService
UnitSpawnDefinition
pending_roulette_rewards
try_spend_gold
add_gold
```

Reject the forbidden R4 method names from `roulette_spin_session.gd`.

Require the headless test phrases for min length, wrap, stable X replacement, source-bound exclusion, ID uniqueness, deterministic stop, row-major board, live-state isolation, returned-copy isolation, and stopped-only session.

- [ ] **Step 2: Write mutation tests**

At minimum add:

```python
def test_current_tree_passes(self): ...
def test_missing_reel_minimum_is_rejected(self): ...
def test_source_bound_x_replacement_regression_is_rejected(self): ...
def test_snapshot_copy_out_loss_is_rejected(self): ...
def test_stage_run_dependency_is_rejected(self): ...
def test_premature_confirm_method_is_rejected(self): ...
def test_headless_invariant_phrase_loss_is_rejected(self): ...
```

Each mutation copies only the validator's declared required files into a temporary directory.

- [ ] **Step 3: Run validator Red/Green locally**

```bash
python tools/validate_v2_roulette_domain.py
python -m unittest tests.python.test_v2_roulette_domain_contract -v
```

Expected: current tree passes; every mutation test passes by observing the intended validation error.

- [ ] **Step 4: Add the V2 contract to fast and full CI**

In both Python compile commands include:

```text
tools/validate_v2_roulette_domain.py
tests/python/test_v2_roulette_domain_contract.py
```

In `contracts_pr`, add:

```yaml
- name: Validate V2 roulette domain contract
  run: python tools/validate_v2_roulette_domain.py
```

Add `tests.python.test_v2_roulette_domain_contract` to the fast unittest command. `contracts_full` already discovers all Python tests but must also run the validator explicitly.

Do not add a new OS matrix, job, workflow, Godot download, or artifact.

- [ ] **Step 5: Extend the CI usage contract**

Require the fast PR section to contain:

```text
python tools/validate_v2_roulette_domain.py
tests.python.test_v2_roulette_domain_contract
```

Add a mutation in `test_ci_usage_contract.py` that removes one marker and expects validation failure.

- [ ] **Step 6: Run all static and Python contracts**

```bash
python -m py_compile \
  tools/validate_c1_roulette.py \
  tools/validate_v2_roulette_domain.py \
  tools/validate_c2_battle_objective.py \
  tools/validate_c3_core_ux.py \
  tools/validate_ci_usage_contract.py \
  tests/python/test_c1_roulette_contract.py \
  tests/python/test_v2_roulette_domain_contract.py \
  tests/python/test_ci_usage_contract.py
python tools/validate_c1_roulette.py
python tools/validate_v2_roulette_domain.py
python tools/validate_c2_battle_objective.py
python tools/validate_c3_core_ux.py
python tools/validate_ci_usage_contract.py
python -m unittest \
  tests.python.test_c1_roulette_contract \
  tests.python.test_v2_roulette_domain_contract \
  tests.python.test_c2_battle_objective_contract \
  tests.python.test_c3_core_ux_contract \
  tests.python.test_ci_usage_contract -v
```

Expected: all exit `0`.

- [ ] **Step 7: Commit validator and CI integration**

```bash
git add tools/validate_v2_roulette_domain.py \
        tests/python/test_v2_roulette_domain_contract.py \
        .github/workflows/validate-omenward-core.yml \
        tools/validate_ci_usage_contract.py \
        tests/python/test_ci_usage_contract.py
git commit -m "test: validate V2 roulette domain boundaries"
```

---

### Task 8: Run Full Regression and Perform Adversarial Scope Review

**Files:**
- Review all changed files.
- Do not add product features while fixing regressions.

**Interfaces:**
- Consumes: Tasks 1–7.
- Produces: a clean implementation branch ready for PR review.

- [ ] **Step 1: Run Godot import and every headless test**

```bash
godot --headless --path . --editor --quit
for test_file in tests/headless/*_test.gd; do
  echo "Running ${test_file}"
  godot --headless --path . -s "res://${test_file}"
done
godot --headless --path . --quit-after 1
```

Expected: import, all headless tests, and runtime smoke exit `0` under Godot 4.7.1.

- [ ] **Step 2: Run the full Python suite**

```bash
python -m unittest discover -s tests/python -v
```

Expected: zero failures and zero errors.

- [ ] **Step 3: Verify protected paths are untouched**

```bash
git diff --name-only origin/main...HEAD
git diff --check
git status --short --branch
```

The changed-file list must not contain:

```text
scripts/core/stage_run.gd
scripts/buildings/
scripts/ui/
scenes/
data/
resources/
project.godot
```

- [ ] **Step 4: Adversarially inspect ownership**

Confirm manually:

```text
Legacy spin still charges economy and generates independent nine-cell boards.
Legacy service still owns legendary conversion and UnitSpawnDefinition creation.
Pure resolver has no stateful service dependency.
V2 domain has no building/economy/UI/StageRun dependency.
No V2 domain object is stored in StageRun.
No move or confirm transaction exists.
No snapshot getter leaks internal mutable references.
No test was weakened to make extraction pass.
```

- [ ] **Step 5: Create the implementation PR only after explicit user Build approval**

The PR body must state:

```text
R1_RESOLVER_SEAM: IMPLEMENTED_CANDIDATE
R2_PURE_REEL_DOMAIN: IMPLEMENTED_CANDIDATE
LEGACY_C1_RESULTS: PRESERVED_LOCALLY
LIVE_V2_ROULETTE: NOT_CONNECTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```

Do not claim remote proof until GitHub Actions completes on the exact head SHA.

---

### Task 9: Verify the Exact PR Head and Merge Safely

**Files:**
- No new files unless a failing contract proves a minimal correction is necessary.

- [ ] **Step 1: Inspect the exact PR head and changed files**

```bash
git rev-parse HEAD
git diff --stat origin/main...HEAD
git diff --name-only origin/main...HEAD
```

- [ ] **Step 2: Require both core contract layers**

Required PR checks on the exact head:

```text
Validate Omenward Core / contracts_pr = success
Validate Omenward Core / godot = success
```

`contracts_full` is expected to be skipped on pull requests and to run after main push or manual dispatch.

- [ ] **Step 3: Review unresolved comments and mergeability**

Required:

```text
mergeable = true
unresolved review threads = 0
behind main = 0
```

- [ ] **Step 4: Squash merge**

Use a single squash commit such as:

```text
feat: add V2 roulette resolver and pure reel domain
```

Do not delete evidence or rewrite the Legacy C1 report.

---

### Task 10: Synchronize Post-Merge Status in a Separate Docs PR

**Files:**
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/OMENWARD_ROADMAP.md`
- Update: Issue `#69`

**Interfaces:**
- Consumes: exact implementation merge SHA and exact successful workflow run IDs.
- Produces: truthful current-state documents without upgrading the playable V2 loop.

- [ ] **Step 1: Record exact evidence**

Use the actual values from GitHub:

```text
implementation merge SHA
final PR head SHA
contracts_pr run ID
Godot job run ID
main/full-matrix run ID if executed
```

- [ ] **Step 2: Update status vocabulary**

Use:

```text
R1_ROULETTE_BOARD_RESOLVER_REMOTE_PROVEN
R2_PHYSICAL_REEL_PURE_DOMAIN_REMOTE_PROVEN
LIVE_V2_ROULETTE_NOT_CONNECTED
V2_IMPLEMENTATION_PARTIAL_FOUNDATION_ONLY
LEGACY_C1_C2_C3_PROVEN
HUMAN_QA_NOT_RUN
CORE_LOCK_V2_PENDING
```

Do not use `V2_IMPLEMENTED` or `CORE_LOOP_V2_PROVEN`.

- [ ] **Step 3: Set the next package**

The next package is R3 only after a new Plan Mode proposal and user approval:

```text
TokenSource completion/destruction/blocked events
→ live reel token synchronization
→ NORMAL_X / SOURCE_BOUND_X transactions
→ stopped snapshot preservation after building changes
```

- [ ] **Step 4: Validate and merge the docs PR**

```bash
python tools/validate_project_core_docs.py
python -m unittest tests.python.test_project_core_docs -v
git diff --check
```

Require the documentation workflow success on the exact docs PR head, then squash merge and close Issue #69 as completed.

---

## Self-Review Results

### Spec coverage

- R1 central-row gate, line count, grade, gold, source determinism: Tasks 1–2.
- Legacy adapter and unchanged live spin path: Task 2 and Task 8 scope review.
- Token identity and token kinds: Task 3.
- Reel minimum, wrap, stable X replacement, append, source-bound exclusion: Task 3.
- Three reels, cross-reel uniqueness, deterministic stop: Task 4.
- Deep immutable snapshot and row-major board: Task 5.
- Minimal session without R4 transactions: Task 6.
- Static contracts, mutation tests, CI: Task 7.
- Full regression, exact remote evidence, merge, separate documentation sync: Tasks 8–10.

### Explicitly deferred

- Live V2 spin integration.
- Building/token lifecycle.
- Horizontal and vertical moves.
- Lucky, movement-item economy, legendary risk-cycle state.
- Confirm transaction and pending rewards.
- MapRun, UI, human play, distribution simulation.

### Type consistency

- `RouletteBoardResolver.resolve()` returns `RouletteBoardResolution`.
- `RouletteReelState` owns `Array[RouletteTokenInstance]`.
- `RouletteRunState` owns exactly three `RouletteReelState` instances.
- `RouletteSpinSnapshot.capture()` consumes a `RouletteRunState` and exposes copies.
- `RouletteSpinSession` consumes a `RouletteSpinSnapshot` and exposes copies only.

## Execution Handoff

This plan is an implementation-ready draft attached to Issue #69, but Build remains blocked by the project Plan Mode gate. Codex must first perform the read-only repository investigation and submit the proposal described in Issue #69. After the user explicitly approves that proposal, execute this plan with `superpowers:subagent-driven-development` or `superpowers:executing-plans` in an isolated worktree.