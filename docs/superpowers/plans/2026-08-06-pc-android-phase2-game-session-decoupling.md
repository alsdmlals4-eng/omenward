# PC·Android Phase 2 GameSession Decoupling Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split GameSession into application state, frame driving, Scene binding, and composition while preserving current gameplay behavior and Scene-facing APIs.

**Architecture:** Keep a thin `GameSession` Node facade in `scripts/application`. Put deterministic state and stage orchestration in a `RefCounted GameApplication`; delegate frame advancement to `SessionDriver`; isolate all SceneTree lookup in `SceneBinder`; and assemble the parts through `PlatformBootstrap`.

**Tech Stack:** Godot 4.7.1 GDScript, Python 3 unittest, existing platform boundary scanner, GitHub PR workflow, Google Sheets Decision sync.

## Global Constraints

- Decision ID: `OMW-DEC-20260806-PC-ANDROID-PHASE2-GAME-SESSION-DECOUPLING-V1`.
- Preserve the `GameSession` Scene node name, signals, `start_stage()`, `retry_stage()`, and readable state properties.
- Preserve default deferred start of `tutorial_stage` after successful bootstrap.
- Do not change StageRun rules, data, Scene visuals, save behavior, platform adapters, workflows, export presets, or SDKs.
- `GameApplication` must extend `RefCounted` and contain no SceneTree lookup.
- `GameSession` must contain no `_process`, direct registry loading, direct stage rules, or SceneTree lookup.
- `SceneBinder` is the only new owner of Battlefield and StageHud lookup.
- Remove `scripts/core/game_session.gd` and all three Phase 0 legacy allowances.
- Use free local Godot and Python verification only; do not invoke paid CI.

---

### Task 1: Freeze Phase 2 structural RED contracts

**Files:**
- Create: `tests/python/test_game_session_decoupling_contract.py`
- Modify: `tests/python/test_platform_boundary_static_guard.py`
- Test: `tests/python/test_game_session_decoupling_contract.py`
- Test: `tests/python/test_platform_boundary_static_guard.py`

**Interfaces:**
- Consumes: current `scripts/core/game_session.gd`, `tools.platform_boundary_guard.DEFAULT_LEGACY_ALLOWLIST`, and `scenes/main/main.tscn`.
- Produces: executable requirements for the five target scripts, main Scene path, and zero legacy allowances.

- [ ] **Step 1: Add the structural test**

Create assertions that require:

```python
EXPECTED_FILES = {
    "scripts/application/game_application.gd",
    "scripts/application/game_session.gd",
    "scripts/application/session_driver.gd",
    "scripts/application/platform_bootstrap.gd",
    "scripts/presentation/scene_binder.gd",
}
```

The test must also assert that `scripts/core/game_session.gd` does not exist, `GameApplication` extends `RefCounted`, the facade has no `_process` or Scene lookup, `SessionDriver` owns `_process`, `SceneBinder` contains the two approved lookup paths, and `main.tscn` points at `res://scripts/application/game_session.gd`.

- [ ] **Step 2: Change the static-guard repository expectation to zero allowances**

Replace:

```python
self.assertEqual(3, len(report.allowed))
```

with:

```python
self.assertEqual(0, len(report.allowed))
self.assertEqual((), DEFAULT_LEGACY_ALLOWLIST)
```

- [ ] **Step 3: Run the RED tests**

Run:

```bash
python -m unittest \
  tests.python.test_game_session_decoupling_contract \
  tests.python.test_platform_boundary_static_guard -v
```

Expected: FAIL because the five target files are absent, the old core file still exists, the Scene path is unchanged, and the legacy allowlist still contains three entries.

- [ ] **Step 4: Commit the RED tests**

```bash
git add tests/python/test_game_session_decoupling_contract.py tests/python/test_platform_boundary_static_guard.py
git commit -m "test: define GameSession decoupling contract"
```

---

### Task 2: Add Godot behavioral RED coverage

**Files:**
- Create: `tests/headless/game_session_decoupling_test.gd`

**Interfaces:**
- Consumes: target class paths from Task 1.
- Produces: behavior requirements for `GameApplication`, `SessionDriver`, `SceneBinder`, `PlatformBootstrap`, and the compatibility facade.

- [ ] **Step 1: Create injected fakes in the headless test**

The test must define fake registry, validator, determinism, progression, stage, stage run, application, driver, binder targets, and bootstrapper objects. The fake application must expose:

```gdscript
signal bootstrap_ready(manifest: Variant)
signal bootstrap_failed(errors: PackedStringArray)
signal stage_started(stage_id: StringName, run: Variant)
```

- [ ] **Step 2: Cover application behavior**

Assert successful bootstrap, failed bootstrap, locked-stage rejection, successful start, retry using `current_stage_id`, and `advance(delta)` delegation.

- [ ] **Step 3: Cover driver and binder behavior**

Assert that `_process(delta)` advances the application, deferred start invokes the requested stage, and one emitted stage event binds the same run to both `Battlefield` and `UI/StageHud`.

- [ ] **Step 4: Cover composition and facade compatibility**

Assert that composition creates one `SessionDriver` and one `SceneBinder`, facade signals are forwarded once, public getters return application state, and `start_stage()` and `retry_stage()` delegate.

- [ ] **Step 5: Run the Godot RED test**

Run:

```bash
godot --headless --path . -s tests/headless/game_session_decoupling_test.gd
```

Expected: parse/load failure because the target scripts do not exist.

- [ ] **Step 6: Commit the Godot RED test**

```bash
git add tests/headless/game_session_decoupling_test.gd
git commit -m "test: characterize decoupled session behavior"
```

---

### Task 3: Implement the platform-neutral GameApplication

**Files:**
- Create: `scripts/application/game_application.gd`

**Interfaces:**
- Consumes: injected dependency dictionary or the existing production scripts loaded on demand.
- Produces:
  - `bootstrap() -> PackedStringArray`
  - `start_stage(stage_id: StringName) -> bool`
  - `retry_stage() -> bool`
  - `advance(delta: float) -> void`
  - signals `bootstrap_ready`, `bootstrap_failed`, `stage_started`
  - readable fields `clock`, `registry`, `determinism`, `validator`, `progression`, `stage_run`, `current_stage_id`

- [ ] **Step 1: Implement dependency injection and defaults**

Use `_init(dependencies: Dictionary = {})`. Accept keys `clock`, `registry`, `determinism`, `validator`, `progression`, and `stage_run_factory`. In `bootstrap()`, create missing defaults with `load(path).new(...)` using the existing production paths.

- [ ] **Step 2: Implement bootstrap**

Load `res://data/bootstrap_catalog.tres`, append validator errors, emit `bootstrap_failed` and return on error, otherwise create the stage run and emit the manifest from `determinism.create_stage_manifest("phase_0", registry.archetype_ids())`.

- [ ] **Step 3: Implement start, retry, and advance**

Keep the existing acceptance conditions and return value:

```gdscript
return stage_run.result_state == &"running"
```

Emit `stage_started` only after calling `stage_run.start(...)`.

- [ ] **Step 4: Run the focused Godot test**

Run the headless Phase 2 test. Expected: application cases pass; driver, binder, bootstrap, and facade cases still fail because those classes are absent.

- [ ] **Step 5: Commit**

```bash
git add scripts/application/game_application.gd
git commit -m "feat: extract platform-neutral GameApplication"
```

---

### Task 4: Implement SessionDriver and SceneBinder

**Files:**
- Create: `scripts/application/session_driver.gd`
- Create: `scripts/presentation/scene_binder.gd`

**Interfaces:**
- `SessionDriver.configure(application: Variant) -> void`
- `SessionDriver.start_stage_deferred(stage_id: StringName) -> void`
- `SceneBinder.configure(application: Variant, host: Node) -> void`

- [ ] **Step 1: Implement SessionDriver**

Store one application reference, delegate `_process(delta)`, and use `call_deferred("_start_stage", stage_id)` for initial-stage scheduling. Disable processing when no application is configured.

- [ ] **Step 2: Implement SceneBinder**

Connect once to `application.stage_started`. On each event, resolve `host.get_parent()`, then independently locate and bind:

```gdscript
scene_root.get_node_or_null("Battlefield")
scene_root.get_node_or_null("UI/StageHud")
```

Disconnect from an old application when reconfigured.

- [ ] **Step 3: Run the headless Phase 2 test**

Expected: application, driver, and binder cases pass; composition and facade cases still fail.

- [ ] **Step 4: Commit**

```bash
git add scripts/application/session_driver.gd scripts/presentation/scene_binder.gd
git commit -m "feat: isolate session driving and Scene binding"
```

---

### Task 5: Implement composition and compatibility facade

**Files:**
- Create: `scripts/application/platform_bootstrap.gd`
- Create: `scripts/application/game_session.gd`
- Modify: `scenes/main/main.tscn`
- Delete: `scripts/core/game_session.gd`

**Interfaces:**
- `PlatformBootstrap.compose(host: Node, assigned_application: Variant = null) -> Dictionary`
- compatibility facade methods and getters from the design spec.

- [ ] **Step 1: Implement PlatformBootstrap**

Create or accept an application, add exactly one driver and binder child to the host, configure them, and return:

```gdscript
{
    "application": application,
    "driver": driver,
    "binder": binder,
}
```

Return `{}` for a null host.

- [ ] **Step 2: Implement the GameSession facade**

Support optional bootstrapper injection in `_init`. In `_ready()`, compose, connect signals, call `application.bootstrap()`, report validation failure, and schedule `tutorial_stage` only when no errors were returned. Re-emit each application signal exactly once.

- [ ] **Step 3: Add compatibility getters and delegates**

Expose `clock`, `registry`, `determinism`, `validator`, `progression`, `stage_run`, and `current_stage_id` through getters. Delegate `start_stage()` and `retry_stage()` and return `false` before composition.

- [ ] **Step 4: Move the Scene script path and remove the old file**

Change the ext_resource path in `main.tscn` to `res://scripts/application/game_session.gd`, then delete `scripts/core/game_session.gd`.

- [ ] **Step 5: Run the Phase 2 Godot test**

Expected: PASS with `GameSession decoupling checks passed`.

- [ ] **Step 6: Commit**

```bash
git add scripts/application/platform_bootstrap.gd scripts/application/game_session.gd scenes/main/main.tscn
git rm scripts/core/game_session.gd
git commit -m "refactor: compose GameSession through application boundaries"
```

---

### Task 6: Remove the Phase 0 exceptions and make all static tests GREEN

**Files:**
- Modify: `tools/platform_boundary_guard.py`
- Modify: `tests/python/test_platform_boundary_static_guard.py`

**Interfaces:**
- Produces `DEFAULT_LEGACY_ALLOWLIST: tuple[LegacyAllowance, ...] = ()`.

- [ ] **Step 1: Empty the legacy allowlist**

Keep the type and public constant but set it to an empty tuple. Do not weaken scanner rules.

- [ ] **Step 2: Run Python verification**

Run:

```bash
python -m unittest \
  tests.python.test_game_session_decoupling_contract \
  tests.python.test_platform_boundary_static_guard -v
python tools/platform_boundary_guard.py
python -m compileall tools tests/python
```

Expected: all tests PASS, `allowed_legacy_findings=0`, `unapproved_findings=0`, `stale_allowances=0`.

- [ ] **Step 3: Commit**

```bash
git add tools/platform_boundary_guard.py tests/python/test_platform_boundary_static_guard.py
git commit -m "refactor: retire GameSession boundary exceptions"
```

---

### Task 7: Run regression verification and adversarial review

**Files:**
- Create: `docs/reviews/ADVERSARIAL_PC_ANDROID_PHASE2_GAME_SESSION_REVIEW_2026-08-06.md`

**Interfaces:**
- Consumes: exact branch source and all Phase 0, Phase 1, and Phase 2 tests.
- Produces: evidence and unresolved boundary list.

- [ ] **Step 1: Run Godot tests**

Run:

```bash
godot --headless --editor --quit --path .
godot --headless --path . -s tests/headless/platform_core_characterization_test.gd
godot --headless --path . -s tests/headless/platform_contracts_test.gd
godot --headless --path . -s tests/headless/game_session_decoupling_test.gd
```

Expected: all exit 0.

- [ ] **Step 2: Run Python tests and scanner**

Run all platform-boundary and Phase 2 structural tests. Expected: PASS and zero allowances.

- [ ] **Step 3: Adversarially inspect**

Check for duplicate signal connections, multiple dynamic driver/binder children, facade state ownership, initial-stage double start, Scene lookup outside SceneBinder, dependency defaults loading before injection, and false claims of platform readiness.

- [ ] **Step 4: Record and fix any defect through a new RED test first**

Every behavior defect found in review must receive a failing Godot or Python regression test before implementation changes.

- [ ] **Step 5: Commit the review**

```bash
git add docs/reviews/ADVERSARIAL_PC_ANDROID_PHASE2_GAME_SESSION_REVIEW_2026-08-06.md
git commit -m "docs: record adversarial Phase 2 review"
```

---

### Task 8: Update authority, publish PR, merge, and sync Sheet

**Files:**
- Create: `docs/APPROVED_PC_ANDROID_PHASE2_GAME_SESSION_DECOUPLING_2026-08-06.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/GODOT_PROJECT_STRUCTURE.md` only when it contains an active old-path reference.

**Interfaces:**
- Produces exact Decision ID, source head, merge commit, verification evidence, and remaining Phase 3+ boundary.

- [ ] **Step 1: Write authority and status**

Record `GAME_SESSION_DECOUPLING = IMPLEMENTED_LOCAL_PASS`, `PHASE3_SHARED_SAVE = NOT_STARTED`, full runtime/build/export as `NOT_RUN`, and all release Gates as `NOT_RUN`.

- [ ] **Step 2: Verify the branch diff**

Require zero changes to gameplay services, data, UI behavior scripts, workflows, export presets, and SDKs. `StageSelect` must remain unchanged unless a test forced a documented fix.

- [ ] **Step 3: Open a Draft PR**

Include the complete RED/GREEN commit chain, exact free-local commands, changed-file inventory, review state, and limitations.

- [ ] **Step 4: Sync the Google Sheet**

Write the same Decision ID and exact source head to the next empty rows in `01_작업순서`, `02_현재_확정결정`, `03_근거_라이브러리`, `90_본제작_출시_사업`, and `99_변경이력`. Preserve concurrent PR #142 planning rows.

- [ ] **Step 5: Read back, review, and merge**

Require Sheet bounded readback, mergeable PR, zero unresolved review threads, and exact head stability. Merge with a merge commit to preserve the TDD chain.

- [ ] **Step 6: Re-run exact-main verification and close Sheet state**

Verify the merged main blobs with Godot and Python again, then change Sheet status to `MAIN_CANONICAL` and `MAIN_READBACK_PASS`.
