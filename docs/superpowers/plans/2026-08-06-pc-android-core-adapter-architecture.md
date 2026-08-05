# PC·Android Core Adapter Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** OMENWARD의 결정론적 게임 규칙을 하나의 공용 코어로 유지하면서 PC와 Android의 입력·표시·저장·수명주기·성능·상점 기능을 교체 가능한 어댑터로 구현한다.

**Architecture:** 기존 `scripts/core`, `scripts/battle`, `scripts/buildings`, `scripts/roulette`의 규칙 서비스를 characterization test로 고정한 뒤 application composition과 platform contracts를 추가한다. `GameSession`의 frame tick·Scene lookup·HUD binding을 분리하고, 공용 저장 스키마와 shared ViewModel을 만든 다음 PC와 Android adapter를 독립 Gate로 구현한다.

**Tech Stack:** Godot 4.7, GDScript, Python unittest 문서·경계 계약, Godot headless tests, JSON/Resource 기반 데이터, Steam/Google Play SDK는 offline core 이후 별도 단계.

## Global Constraints

- Decision ID: `OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1`
- Parent platform Decision: `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`
- `PRODUCT_CODE_AUTHORITY = NONE` until a separate implementation approval.
- `GATE_TRANSFER_POLICY = PASS_DOES_NOT_TRANSFER`.
- domain/core에서 `Node`, SceneTree lookup, `Input`, `DisplayServer`, `FileAccess`, store SDK 직접 참조 금지.
- 하나의 versioned canonical save schema 사용.
- PC/Android 전체 gameplay Scene tree 복제 금지.
- Steam, STOVE, Google Play adapter 분리.
- 각 Task는 RED → GREEN → REFACTOR 후 독립 커밋.

---

### Task 1: Baseline Characterization and Forbidden-API Guard

**Files:**
- Create: `tests/godot/test_current_core_characterization.gd`
- Create: `tests/python/test_platform_boundary_static_guard.py`
- Create: `scripts/platform/README.md`
- Modify: `.github/workflows/validate-project-core-docs.yml`

**Interfaces:**
- Consumes: 현행 `RouletteService`, `DeterminismService`, `StageManifest`, `StageRun` 공개 API.
- Produces: 동일 seed·입력에 대한 baseline fixture와 `scan_forbidden_references(paths) -> list[str]`.

- [ ] **Step 1: Write the failing static boundary test**

```python
FORBIDDEN = ("Input.", "DisplayServer", "FileAccess", "Steam", "GooglePlay")
CORE_ROOTS = (ROOT / "scripts/domain", ROOT / "scripts/core")


def test_domain_and_core_do_not_call_platform_apis_directly():
    violations = scan_forbidden_references(CORE_ROOTS)
    assert violations == []
```

- [ ] **Step 2: Run the RED test**

Run: `python -m unittest tests.python.test_platform_boundary_static_guard -v`

Expected: FAIL because `scan_forbidden_references` and the explicit allowlist policy do not exist.

- [ ] **Step 3: Implement the scanner and explicit legacy allowlist**

The scanner reads `.gd` files, ignores comments, reports `path:line:token`, and permits only documented existing exceptions. The allowlist must be empty before COMMON_PLATFORM_GATE can pass.

- [ ] **Step 4: Add deterministic characterization tests**

Use fixed seeds and command fixtures for roulette resolution, stage economy, building transaction, and battle snapshot. Assert full normalized dictionaries and state hashes, not frame time.

- [ ] **Step 5: Run baseline tests**

Run:

```bash
godot --headless --path . --script tests/godot/test_current_core_characterization.gd
python -m unittest tests.python.test_platform_boundary_static_guard -v
```

Expected: PASS with zero unapproved platform API references.

- [ ] **Step 6: Commit**

```bash
git add tests/godot tests/python/test_platform_boundary_static_guard.py scripts/platform/README.md .github/workflows/validate-project-core-docs.yml
git commit -m "test: characterize platform-neutral core baseline"
```

### Task 2: Commands, Events, and Platform Contracts

**Files:**
- Create: `scripts/domain/commands/game_command.gd`
- Create: `scripts/domain/events/game_event.gd`
- Create: `scripts/platform/contracts/input_adapter.gd`
- Create: `scripts/platform/contracts/display_adapter.gd`
- Create: `scripts/platform/contracts/save_adapter.gd`
- Create: `scripts/platform/contracts/lifecycle_adapter.gd`
- Create: `scripts/platform/contracts/performance_adapter.gd`
- Create: `scripts/platform/contracts/store_adapter.gd`
- Create: `scripts/platform/contracts/platform_capabilities.gd`
- Test: `tests/godot/test_platform_contracts.gd`

**Interfaces:**
- Produces: `GameCommand.action_id: StringName`, `GameCommand.payload: Dictionary`, `GameEvent.event_id: StringName`, and adapter methods below.

```gdscript
# InputAdapter
func poll_commands() -> Array[GameCommand]
func active_device() -> StringName

# DisplayAdapter
func display_snapshot() -> Dictionary
func apply_settings(settings: Dictionary) -> Dictionary

# SaveAdapter
func load_payload(slot_id: StringName) -> Dictionary
func write_payload_atomic(slot_id: StringName, payload: Dictionary) -> Dictionary

# LifecycleAdapter
signal lifecycle_event(event_id: StringName)

# PerformanceAdapter
func budget_snapshot() -> Dictionary

# StoreAdapter
func capabilities() -> PackedStringArray
func is_available() -> bool

# PlatformCapabilities
func has_capability(capability_id: StringName) -> bool
```

- [ ] **Step 1: Write failing contract tests**

Instantiate fake adapters and assert that domain commands contain no device-specific event objects or SDK types.

- [ ] **Step 2: Run RED**

Run: `godot --headless --path . --script tests/godot/test_platform_contracts.gd`

Expected: FAIL because contract classes do not exist.

- [ ] **Step 3: Implement minimal contracts**

Use `RefCounted` base classes with explicit failure dictionaries such as `{"ok": false, "error": "not_implemented"}`. Do not add platform logic.

- [ ] **Step 4: Run GREEN and refactor names**

Run the same command and the Task 1 tests. Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/domain scripts/platform/contracts tests/godot/test_platform_contracts.gd
git commit -m "feat: add platform-neutral command and adapter contracts"
```

### Task 3: Split GameSession Responsibilities

**Files:**
- Create: `scripts/application/game_application.gd`
- Create: `scripts/application/session_driver.gd`
- Create: `scripts/presentation/scene_binder.gd`
- Create: `scripts/platform/platform_bootstrap.gd`
- Modify: `scripts/core/game_session.gd`
- Modify: `scenes/main/main.tscn`
- Test: `tests/godot/test_game_application_composition.gd`

**Interfaces:**
- Consumes: Task 2 commands/events/adapters.
- Produces:

```gdscript
GameApplication.dispatch(command: GameCommand) -> Dictionary
GameApplication.snapshot() -> Dictionary
SessionDriver.advance_seconds(delta: float) -> void
SessionDriver.pause() -> void
SessionDriver.resume() -> void
SceneBinder.bind(application: GameApplication, root: Node) -> void
PlatformBootstrap.create_bundle(feature_tags: PackedStringArray) -> Dictionary
```

- [ ] **Step 1: Write failing headless composition test**

Create `GameApplication` with fake adapters and no SceneTree. Dispatch a start-stage command and assert that a deterministic snapshot is produced.

- [ ] **Step 2: Run RED**

Run: `godot --headless --path . --script tests/godot/test_game_application_composition.gd`

Expected: FAIL because application and composition classes do not exist.

- [ ] **Step 3: Move rule orchestration out of GameSession**

`GameSession` becomes a thin Node host. Remove parent `get_node_or_null` calls from rule orchestration and place them in `SceneBinder`. Keep current scene behavior unchanged.

- [ ] **Step 4: Add explicit tick boundary**

`SessionDriver` converts `_process(delta)` into the approved simulation tick policy. First preserve current behavior under characterization; introduce fixed-step only in a separately tested change if hashes currently vary.

- [ ] **Step 5: Run all core and composition tests**

Expected: baseline snapshots unchanged and headless application test PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/application scripts/presentation scripts/platform/platform_bootstrap.gd scripts/core/game_session.gd scenes/main/main.tscn tests/godot/test_game_application_composition.gd
git commit -m "refactor: separate application session and scene binding"
```

### Task 4: Shared Versioned Save and Atomic Storage

**Files:**
- Create: `scripts/domain/save/save_snapshot.gd`
- Create: `scripts/domain/save/save_schema.gd`
- Create: `scripts/domain/save/save_migrator.gd`
- Create: `scripts/platform/pc/desktop_save_adapter.gd`
- Create: `scripts/platform/android/android_save_adapter.gd`
- Test: `tests/godot/test_save_schema_and_atomic_storage.gd`
- Fixtures: `tests/fixtures/saves/v1_minimal.json`, `tests/fixtures/saves/corrupt.json`

**Interfaces:**

```gdscript
SaveSchema.CURRENT_VERSION: int
SaveSchema.validate(payload: Dictionary) -> PackedStringArray
SaveMigrator.migrate(payload: Dictionary) -> Dictionary
GameApplication.create_save_snapshot() -> Dictionary
GameApplication.restore_save_snapshot(payload: Dictionary) -> Dictionary
```

- [ ] **Step 1: Write failing round-trip, migration, and corruption tests**

Assert same normalized state hash after save/load, v1 fixture migration, corrupt temporary write leaves last-good payload unchanged, and PC/Android adapters produce the same loaded payload.

- [ ] **Step 2: Run RED**

Expected: FAIL because schema and adapters do not exist.

- [ ] **Step 3: Implement canonical schema and migrator**

Required top-level keys: `schema_version`, `content_version`, `run_state`, `meta_state`, `settings`, `determinism_manifest`.

- [ ] **Step 4: Implement atomic adapters**

Write temporary payload, flush, read back, validate/hash, rotate last-good, replace canonical file. Storage paths are adapter-owned and excluded from domain.

- [ ] **Step 5: Run GREEN plus abrupt-interruption fixture tests**

Expected: all save tests PASS and no platform-specific fields enter canonical payload.

- [ ] **Step 6: Commit**

```bash
git add scripts/domain/save scripts/platform/pc/desktop_save_adapter.gd scripts/platform/android/android_save_adapter.gd tests/godot/test_save_schema_and_atomic_storage.gd tests/fixtures/saves
git commit -m "feat: add canonical atomic save architecture"
```

### Task 5: Shared ViewModel and Responsive Input/UI

**Files:**
- Create: `scripts/presentation/gameplay_view_model.gd`
- Create: `scripts/platform/pc/pc_input_adapter.gd`
- Create: `scripts/platform/android/android_input_adapter.gd`
- Create: `scripts/platform/pc/pc_display_adapter.gd`
- Create: `scripts/platform/android/android_display_adapter.gd`
- Create: `scenes/ui/platform_safe_area.tscn`
- Modify: gameplay HUD and roulette/building UI scenes discovered in the implementation branch
- Test: `tests/godot/test_input_semantic_parity.gd`
- Test: `tests/godot/test_responsive_ui_contract.gd`

**Interfaces:**
- Produces semantic commands such as `roulette_spin`, `roulette_move`, `build_confirm`, `overlay_cancel`, `pause_toggle`; no test asserts raw key or touch indexes in domain.

- [ ] **Step 1: Write failing semantic parity tests**

Feed mouse drag, gamepad navigation, and touch drag fixtures to their adapters and assert equivalent `GameCommand` payloads.

- [ ] **Step 2: Write failing responsive layout tests**

Test 16:9 desktop, 20:9 Android, cutout inset, and compact density. Assert critical controls remain inside safe rectangle and no duplicate platform gameplay root exists.

- [ ] **Step 3: Implement adapters and shared ViewModel**

Keep gameplay meaning shared. Use responsive containers and density tokens rather than copied full scenes.

- [ ] **Step 4: Run GREEN and manual device checklist**

Automated tests must pass. Human device checks remain `NOT_RUN` until recorded with screenshots/video and device metadata.

- [ ] **Step 5: Commit**

```bash
git add scripts/presentation scripts/platform/pc scripts/platform/android scenes/ui tests/godot/test_input_semantic_parity.gd tests/godot/test_responsive_ui_contract.gd
git commit -m "feat: add shared responsive UI and input adapters"
```

### Task 6: PC Adapter Bundle and Representative Build

**Files:**
- Create: `scripts/platform/pc/desktop_lifecycle_adapter.gd`
- Create: `scripts/platform/pc/pc_performance_adapter.gd`
- Create: `scripts/platform/stores/null_store_adapter.gd`
- Create: `export_presets.cfg` with a version-controlled non-secret Windows/Linux development preset selected by project policy
- Test: `tests/godot/test_pc_adapter_bundle.gd`
- Create: `docs/evidence/PC_REPRESENTATIVE_BUILD_EVIDENCE.md`

- [ ] **Step 1: Write failing PC bundle tests**

Assert keyboard/mouse/gamepad capabilities, window settings, local atomic save, focus loss/resume, and null store offline startup.

- [ ] **Step 2: Run RED and implement minimal PC adapters**

Do not add Steam SDK yet. Representative build uses NullStoreAdapter.

- [ ] **Step 3: Export representative PC build**

Run the exact export command recorded in evidence. Record Godot version, commit SHA, preset, artifact hash, input devices, window modes, and performance sample.

- [ ] **Step 4: Evaluate PC Gate honestly**

Export success alone leaves `PC_RELEASE_GATE = NOT_RUN` or `PARTIAL_EVIDENCE` until full checklist and human QA are complete.

- [ ] **Step 5: Commit**

```bash
git add scripts/platform/pc scripts/platform/stores/null_store_adapter.gd export_presets.cfg tests/godot/test_pc_adapter_bundle.gd docs/evidence/PC_REPRESENTATIVE_BUILD_EVIDENCE.md
git commit -m "feat: add PC adapter bundle and build evidence"
```

### Task 7: Android Lifecycle, Performance, and Representative Build

**Files:**
- Create: `scripts/platform/android/android_lifecycle_adapter.gd`
- Create: `scripts/platform/android/android_performance_adapter.gd`
- Modify: `export_presets.cfg` to add non-secret Android development preset
- Test: `tests/godot/test_android_adapter_bundle.gd`
- Test: `tests/godot/test_android_background_save.gd`
- Create: `docs/evidence/ANDROID_REPRESENTATIVE_BUILD_EVIDENCE.md`

- [ ] **Step 1: Write failing lifecycle tests**

Simulate pause → background → process interruption → restore. Assert the last complete transaction is present and no partial roulette/building transaction appears.

- [ ] **Step 2: Write failing safe-area and performance-hint tests**

Assert memory/thermal hints alter presentation quality only, never RNG, rewards, economy, or state hash.

- [ ] **Step 3: Implement Android adapters**

Map Godot notifications into lifecycle events, request debounce checkpoint, expose safe-area/density snapshot, and apply quality tier outside domain.

- [ ] **Step 4: Export and test on representative Android devices**

Record OS/API, SoC/RAM, aspect ratio, cutout, input cases, background/resume, memory, thermal, battery, artifact hash, and commit SHA.

- [ ] **Step 5: Evaluate Mobile Gate independently**

Do not reuse PC PASS. Human QA and store consistency remain separate.

- [ ] **Step 6: Commit**

```bash
git add scripts/platform/android export_presets.cfg tests/godot/test_android_adapter_bundle.gd tests/godot/test_android_background_save.gd docs/evidence/ANDROID_REPRESENTATIVE_BUILD_EVIDENCE.md
git commit -m "feat: add Android lifecycle performance and build evidence"
```

### Task 8: Store Adapters After Offline Core

**Files:**
- Create: `scripts/platform/stores/steam_store_adapter.gd`
- Create: `scripts/platform/stores/google_play_store_adapter.gd`
- Future separate PR only: `scripts/platform/stores/stove_store_adapter.gd`
- Test: `tests/godot/test_store_adapter_degraded_modes.gd`
- Create: `docs/evidence/STORE_ADAPTER_EVIDENCE.md`

- [ ] **Step 1: Write failing degraded-mode tests**

Test unavailable SDK, logged-out user, network timeout, stale cloud save, and conflict resolution. Assert local offline startup/save remains available.

- [ ] **Step 2: Implement Steam and Google Play adapters separately**

Expose capability lists and explicit errors. Do not let SDK objects enter canonical save or domain state.

- [ ] **Step 3: Verify build/store/questionnaire consistency**

Record SDK versions, permissions/data use, achievement/cloud-save behavior, and representative build hashes.

- [ ] **Step 4: Keep STOVE isolated**

Create STOVE implementation only after its separate store Gate is approved. Never add STOVE conditionals inside SteamStoreAdapter.

- [ ] **Step 5: Commit**

```bash
git add scripts/platform/stores tests/godot/test_store_adapter_degraded_modes.gd docs/evidence/STORE_ADAPTER_EVIDENCE.md
git commit -m "feat: add isolated store capability adapters"
```

## Final Verification

Run:

```bash
python -m unittest discover -s tests/python -p 'test_*.py' -v
godot --headless --path . --script tests/godot/run_all.gd
git diff --check main...HEAD
```

Then verify:

- COMMON, PC, MOBILE evidence is reported separately.
- Product code changes match a separately approved implementation Decision.
- save fixtures migrate and recover from corruption.
- no domain/core forbidden API reference exists.
- no duplicated PC/Android gameplay scene root exists.
- Sheet read-back and PR review threads are checked before merge.
