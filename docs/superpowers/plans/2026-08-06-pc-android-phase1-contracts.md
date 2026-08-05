# PC·Android Phase 1 Command/Event and Platform Contracts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 플랫폼별 구현을 시작하기 전에 OMENWARD의 의미 기반 `GameCommand`·`GameEvent`와 입력·표시·저장·수명주기·성능·상점·capability 계약을 Godot `RefCounted` 타입으로 고정한다.

**Architecture:** domain에는 장치·Scene·SDK 객체를 담지 않는 명령과 이벤트만 추가한다. platform/contracts에는 실제 PC·Android 동작이 없는 실패 폐쇄형 base contract만 추가하며, 기존 게임 서비스와 Scene은 수정하지 않는다. 검증은 GitHub Actions 없이 Python 정적 검사와 사용자 제공 Godot 4.7.1 headless 실행으로 수행한다.

**Tech Stack:** Godot 4.7.1, GDScript, `SceneTree` headless test, Python 3 standard-library boundary guard, GitHub Draft PR, Google Sheet bounded read-back.

## Global Constraints

- Decision ID: `OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1`.
- Parent architecture: `OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1`.
- Parent baseline: `OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1`.
- Base main: `aea0cf667e7c6fc5d4b9924cf9bb1ffc9eeddbe6`.
- GitHub Actions and external paid CI/build services are not used.
- Existing product services, Scene, Resource, data, export presets, and store SDKs remain unchanged.
- `GameCommand` and `GameEvent` reject payloads containing `Object`, `Callable`, `Signal`, or `RID` values, including nested values.
- Domain and contract classes extend `RefCounted`; no new `Node`, SceneTree lookup, `Input`, `DisplayServer`, `FileAccess`, `OS.has_feature`, Steam, STOVE, or Google Play reference is allowed.
- Adapter base methods return deterministic empty/default values or `{"ok": false, "error": "not_implemented"}`.
- Platform implementation, composition root, save schema, UI changes, builds, and release Gates remain out of scope.
- Every product-code commit follows RED → GREEN → REFACTOR with fresh exit-code evidence.

---

### Task 1: Contract Test RED

**Files:**
- Create: `tests/headless/platform_contracts_test.gd`

**Interfaces exercised:**
- `GameCommand.new(action_id, payload)` and `GameEvent.new(event_id, payload)`.
- Seven adapter contract classes and `PlatformCapabilities`.

- [ ] **Step 1: Write the failing headless test**

The test preloads these missing paths:

```gdscript
const GameCommandScript = preload("res://scripts/domain/commands/game_command.gd")
const GameEventScript = preload("res://scripts/domain/events/game_event.gd")
const InputAdapterScript = preload("res://scripts/platform/contracts/input_adapter.gd")
const DisplayAdapterScript = preload("res://scripts/platform/contracts/display_adapter.gd")
const SaveAdapterScript = preload("res://scripts/platform/contracts/save_adapter.gd")
const LifecycleAdapterScript = preload("res://scripts/platform/contracts/lifecycle_adapter.gd")
const PerformanceAdapterScript = preload("res://scripts/platform/contracts/performance_adapter.gd")
const StoreAdapterScript = preload("res://scripts/platform/contracts/store_adapter.gd")
const PlatformCapabilitiesScript = preload("res://scripts/platform/contracts/platform_capabilities.gd")
```

Assertions:

- semantic command/event IDs and deep-copied payload dictionaries round-trip;
- empty IDs are invalid;
- nested `RefCounted` payload values are invalid;
- adapters are `RefCounted`, not `Node`;
- default input returns no commands and `unknown` device;
- display/save/performance methods fail closed with `not_implemented`;
- lifecycle contract exposes `lifecycle_event`;
- store contract is unavailable with no capabilities;
- `PlatformCapabilities` reports only explicitly supplied IDs.

- [ ] **Step 2: Run RED**

Run:

```bash
Godot_v4.7.1-stable_linux.x86_64 --headless --path <phase1-harness> --script tests/headless/platform_contracts_test.gd
```

Expected: non-zero exit because the command/event and contract scripts do not exist.

- [ ] **Step 3: Commit the failing test only**

Commit message:

```text
test: define phase1 platform contract behavior
```

### Task 2: Domain Command and Event GREEN

**Files:**
- Create: `scripts/domain/commands/game_command.gd`
- Create: `scripts/domain/events/game_event.gd`

**Produces:**

```gdscript
GameCommand.action_id: StringName
GameCommand.payload: Dictionary
GameCommand.is_valid() -> bool
GameCommand.to_dictionary() -> Dictionary

GameEvent.event_id: StringName
GameEvent.payload: Dictionary
GameEvent.is_valid() -> bool
GameEvent.to_dictionary() -> Dictionary
```

- [ ] **Step 1: Implement `GameCommand` minimally**

Use `class_name GameCommand`, `extends RefCounted`, deep-copy constructor payloads, and recursively reject `TYPE_OBJECT`, `TYPE_CALLABLE`, `TYPE_SIGNAL`, and `TYPE_RID`.

- [ ] **Step 2: Implement `GameEvent` with the same neutral payload rule**

Do not introduce inheritance between command and event; their names and semantic roles remain explicit.

- [ ] **Step 3: Run the headless test**

Expected: preload proceeds beyond command/event files and still fails because adapter contracts are missing.

### Task 3: Seven Platform Contracts GREEN

**Files:**
- Create: `scripts/platform/contracts/input_adapter.gd`
- Create: `scripts/platform/contracts/display_adapter.gd`
- Create: `scripts/platform/contracts/save_adapter.gd`
- Create: `scripts/platform/contracts/lifecycle_adapter.gd`
- Create: `scripts/platform/contracts/performance_adapter.gd`
- Create: `scripts/platform/contracts/store_adapter.gd`
- Create: `scripts/platform/contracts/platform_capabilities.gd`

**Produces:**

```gdscript
InputAdapter.poll_commands() -> Array[GameCommand]
InputAdapter.active_device() -> StringName
DisplayAdapter.display_snapshot() -> Dictionary
DisplayAdapter.apply_settings(settings: Dictionary) -> Dictionary
SaveAdapter.load_payload(slot_id: StringName) -> Dictionary
SaveAdapter.write_payload_atomic(slot_id: StringName, payload: Dictionary) -> Dictionary
LifecycleAdapter.lifecycle_event(event_id: StringName)
PerformanceAdapter.budget_snapshot() -> Dictionary
StoreAdapter.capabilities() -> PackedStringArray
StoreAdapter.is_available() -> bool
PlatformCapabilities.has_capability(capability_id: StringName) -> bool
PlatformCapabilities.all_capabilities() -> PackedStringArray
```

- [ ] **Step 1: Implement input and lifecycle contracts**

Input returns a typed empty `Array[GameCommand]` and `&"unknown"`. Lifecycle declares only the signal; no OS notification mapping is added.

- [ ] **Step 2: Implement display, save, and performance contracts**

Each unimplemented operation returns:

```gdscript
{"ok": false, "error": "not_implemented"}
```

Ignore input dictionaries without mutating them.

- [ ] **Step 3: Implement store and capability contracts**

The base store is unavailable and returns an empty `PackedStringArray`. `PlatformCapabilities` copies and deduplicates supplied IDs and exposes no mutator.

- [ ] **Step 4: Run GREEN**

Run:

```bash
Godot_v4.7.1-stable_linux.x86_64 --headless --path <phase1-harness> --editor --quit
Godot_v4.7.1-stable_linux.x86_64 --headless --path <phase1-harness> --script tests/headless/platform_contracts_test.gd
python -m unittest tests.python.test_platform_boundary_static_guard -v
python tools/platform_boundary_guard.py --root .
python -m py_compile tools/platform_boundary_guard.py tests/python/test_platform_boundary_static_guard.py
```

Expected:

```text
Godot editor scan EXIT_0
Platform contract checks passed
Godot contract test EXIT_0
Python unittest 3 PASS
unapproved_findings=0
stale_allowances=0
Python compile PASS
```

- [ ] **Step 5: Refactor only duplication that does not add behavior**

Keep command and event payload validation local to each type for this phase; do not create an unapproved shared framework.

- [ ] **Step 6: Commit implementation**

Commit message:

```text
feat: add platform-neutral command and adapter contracts
```

### Task 4: Authority, Review, and Draft PR

**Files:**
- Create: `docs/APPROVED_PC_ANDROID_PHASE1_CONTRACTS_2026-08-06.md`
- Create: `docs/reviews/ADVERSARIAL_PC_ANDROID_PHASE1_CONTRACTS_REVIEW_2026-08-06.md`
- Modify: `scripts/platform/README.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

- [ ] **Step 1: Record the exact contract boundary**

Document that Phase 1 creates types and default behavior only. Explicitly preserve:

```text
GAME_SESSION_DECOUPLING = NOT_STARTED
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
FULL_PROJECT_RUNTIME = NOT_RUN
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
```

- [ ] **Step 2: Adversarially review failure modes**

Cover empty semantic IDs, mutable payload aliasing, nested Object leakage, base adapters accidentally claiming availability, capability mutation, platform logic entering contracts, and Phase 1 PASS being misreported as release readiness.

- [ ] **Step 3: Open a Draft PR against current main**

The PR must list the exact RED commit, GREEN commands, exit codes, changed files, and the full-project verification boundary.

- [ ] **Step 4: Sync the same Decision ID to Google Sheet**

Write only bounded rows in `01_작업순서`, `02_현재_확정결정`, `03_근거_라이브러리`, `90_본제작_출시_사업`, and `99_변경이력`. Preserve concurrent planning rows.

## Completion Boundary

```text
PHASE1_COMMAND_EVENT_CONTRACTS = IMPLEMENTED_LOCAL_PASS
PRODUCT_BEHAVIOR_CHANGE = NONE
FULL_PROJECT_RUNTIME = NOT_RUN
GAME_SESSION_DECOUPLING = NOT_STARTED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
RELEASE_BLOCKED_UNVERIFIED
```
