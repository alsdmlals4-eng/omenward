# PC·Android Phase 2 GameSession Decoupling Design

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-PHASE2-GAME-SESSION-DECOUPLING-V1
parent_architecture: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
baseline_main: 32e4482119812c1da62bb909350d2f87087785b3
scope: GAME_SESSION_RESPONSIBILITY_DECOUPLING
product_behavior_change: NONE
phase3_save_work: NOT_AUTHORIZED
```

## 1. Goal

Split the current `GameSession` responsibilities without changing stage bootstrap, stage selection, retry, simulation advancement, Battlefield binding, HUD binding, or the public Scene node name used by existing UI.

## 2. Selected approach

Use a compatibility-facade migration.

- Move the Scene-facing `GameSession` host from `scripts/core` to `scripts/application`.
- Preserve the `GameSession` node name, signals, `start_stage()`, `retry_stage()`, and readable state properties used by current UI.
- Move deterministic session state and stage orchestration into `GameApplication`, which extends `RefCounted`.
- Move `_process(delta)` and deferred initial-stage start into `SessionDriver`.
- Move all Battlefield and HUD SceneTree lookup and binding into `SceneBinder`.
- Let `PlatformBootstrap` assemble and inject the four components.

A full Scene rewrite is rejected because it would require changing all current consumers at once. A partial extraction that leaves state or Scene lookup in `GameSession` is rejected because it would preserve the exact coupling Phase 2 is intended to remove.

## 3. Components

### `GameApplication`

Path: `scripts/application/game_application.gd`

Responsibilities:

- own `clock`, `registry`, `determinism`, `validator`, `progression`, `stage_run`, and `current_stage_id`;
- load and validate the bootstrap catalog;
- create the stage run;
- start, retry, and advance a stage;
- emit `bootstrap_ready`, `bootstrap_failed`, and `stage_started`;
- expose no Node, SceneTree, input, display, file, or store behavior.

The constructor accepts a dependency dictionary for isolated tests. Missing dependencies are created from the existing production scripts only when `bootstrap()` runs.

### `SessionDriver`

Path: `scripts/application/session_driver.gd`

Responsibilities:

- extend `Node`;
- hold one application reference;
- call `application.advance(delta)` from `_process(delta)`;
- schedule the initial stage with `call_deferred`;
- contain no Scene lookup and no gameplay state.

### `SceneBinder`

Path: `scripts/presentation/scene_binder.gd`

Responsibilities:

- extend `Node`;
- subscribe to `application.stage_started`;
- resolve the host Scene root from the compatibility host;
- locate `Battlefield` and `UI/StageHud` only;
- call `bind_run(stage_run)` when the targets exist;
- contain no stage rules or platform selection.

### `PlatformBootstrap`

Path: `scripts/application/platform_bootstrap.gd`

Responsibilities:

- create or accept a `GameApplication`;
- create `SessionDriver` and `SceneBinder` children under the `GameSession` host;
- configure both components;
- return the composition as a dictionary;
- perform no PC/Android adapter selection yet.

Actual PC and Android adapter construction remains Phase 5 and Phase 6 work. The Phase 2 class name establishes the composition boundary without claiming platform readiness.

### `GameSession` compatibility facade

Path: `scripts/application/game_session.gd`

Responsibilities:

- remain the script attached to the `GameSession` Scene node;
- use `PlatformBootstrap` in `_ready()`;
- forward the application signals;
- delegate `start_stage()` and `retry_stage()`;
- expose compatibility getters for the current public state;
- contain no `_process`, direct stage rules, registry loading, or SceneTree lookup.

## 4. Runtime flow

1. `main.tscn` instantiates the existing `GameSession` node using the new application path.
2. `GameSession._ready()` asks `PlatformBootstrap` to compose the application, driver, and binder.
3. `GameSession` connects application signals, then calls `application.bootstrap()`.
4. On successful bootstrap, `SessionDriver` schedules `tutorial_stage` for deferred start.
5. `GameApplication.start_stage()` creates the run and emits `stage_started`.
6. `SceneBinder` binds the run to Battlefield and StageHud.
7. `SessionDriver._process(delta)` advances the same stage run.
8. Existing `StageSelect` continues to call the `GameSession` facade.

## 5. Error handling

- Missing or invalid composition returns an empty dictionary and emits `bootstrap_failed` from the facade.
- Bootstrap validation errors are emitted and prevent deferred stage start.
- Starting a missing or locked stage returns `false` without emitting `stage_started`.
- Missing Battlefield or StageHud nodes are tolerated independently and do not block stage start.
- Reconfiguration disconnects previous signal bindings to avoid duplicate callbacks.

## 6. Compatibility contract

The following remain stable:

```text
SCENE_NODE_NAME = GameSession
SIGNALS = bootstrap_ready, bootstrap_failed, stage_started
METHODS = start_stage, retry_stage
READABLE_STATE = clock, registry, determinism, validator, progression, stage_run, current_stage_id
DEFAULT_STAGE = tutorial_stage
BATTLEFIELD_BIND_PATH = Battlefield
HUD_BIND_PATH = UI/StageHud
```

`StageSelect` is not modified unless a failing regression test proves it necessary.

## 7. Static boundary contract

After Phase 2:

```text
scripts/core/game_session.gd = ABSENT
scripts/application/game_session.gd = NODE_COMPATIBILITY_FACADE
scripts/application/game_application.gd = REFCOUNTED_PLATFORM_NEUTRAL
GAME_SESSION_PROCESS_METHOD = FORBIDDEN
GAME_SESSION_SCENE_LOOKUP = FORBIDDEN
GAME_APPLICATION_NODE_DEPENDENCY = FORBIDDEN
SCENE_LOOKUP_OWNER = scripts/presentation/scene_binder.gd
PHASE0_LEGACY_ALLOWLIST_COUNT = 0
```

The existing static guard continues to scan `scripts/core` and `scripts/domain`. Removing the old file must make all three Phase 0 allowances stale until the allowlist is deleted, providing a RED transition test.

## 8. Tests

### Python structural regression

Add `tests/python/test_game_session_decoupling_contract.py` to verify file ownership, method ownership, Scene path migration, and removal of the three legacy allowances.

Update `tests/python/test_platform_boundary_static_guard.py` to expect zero allowed legacy findings.

### Godot headless behavior

Add `tests/headless/game_session_decoupling_test.gd` using injected fakes to verify:

- bootstrap success and failure;
- stage start, retry, and advance delegation;
- deferred initial-stage start;
- Battlefield and HUD binding;
- compatibility signal forwarding and getters;
- composition creates exactly one driver and one binder.

Re-run the existing platform contract and Phase 0 characterization tests.

## 9. Non-goals

- save schema or `SaveAdapter` implementation;
- PC or Android adapter implementations;
- responsive UI or input normalization;
- store SDK integration;
- export presets or representative builds;
- gameplay balancing or Scene visual changes;
- full repository runtime or release Gate claims.

## 10. Completion criteria

Phase 2 is complete only when the exact GitHub source passes the new Godot and Python tests, the old core file is absent, the static allowlist is empty, main contains the merge commit, and the same Decision ID and exact SHAs are read back from the project Google Sheet.
