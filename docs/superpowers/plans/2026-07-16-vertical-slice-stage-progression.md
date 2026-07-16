# Vertical Slice and Stage Progression Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a playable tutorial and a W1–W20 regular stage using the existing shared-archetype Godot bootstrap, then validate and merge it into `main`.

**Architecture:** `GameSession` composes a `StageRun`, which loads deterministic stage definitions, owns the clock/economy/roulette/wave flow, and sends commands to three isolated lane simulators. One `Unit` scene receives an archetype, tier, rank, team, and faction visual profile; static stage definitions are `.tres` Resources while the resolved runtime manifest and input log are JSON.

**Tech Stack:** Godot 4.7.1 Standard, GDScript, Compatibility renderer, headless GDScript tests, Python unittest for Issue mirror validation.

## Global Constraints

- Keep the existing 960×540 logical viewport, 1920×1080 output, Compatibility renderer, and no AutoLoad/global event bus.
- Preserve exactly ten shared `UnitArchetypeProfile` definitions; never add enemy-only combat resources, unit scenes, statistics, skills, targeting, or animation contracts.
- Keep ordinary movement inside one of `top`, `middle`, or `bottom`; only assassin bypass logic may travel off-map and it must emerge in the same lane.
- Model three gates per side, six middle outposts, three clash zones, and two forward plus one rear node per outpost. Do not add a minimap, gate repair, save/load, multiplayer, final art, or final audio.
- Implement tutorial W1–W4 and regular W1–W20; W15 is the standard legendary victory target and W16–W20 are overtime pressure, ending with a mythic boss.

---

### Task 1: Add deterministic stage and wave data contracts

**Files:**
- Create: `scripts/data/stage_definition.gd`, `scripts/data/wave_definition.gd`, `scripts/data/unit_spawn_definition.gd`, `scripts/data/building_definition.gd`
- Modify: `scripts/core/stage_manifest.gd`, `scripts/core/data_registry.gd`, `scripts/core/bootstrap_validator.gd`, `scripts/data/bootstrap_catalog.gd`, `data/bootstrap_catalog.tres`
- Test: `tests/headless/stage_data_contract_test.gd`

**Interfaces:**
- Produces `StageDefinition.build_manifest(seed: int) -> StageManifest`.
- Produces `WaveDefinition` with `wave_number`, `omen_lead_seconds`, `spawns`, `boss_kind`, and `is_overtime`.
- Produces `UnitSpawnDefinition` with `archetype_id`, `tier_id`, `rank_id`, `owner_team_id`, `visual_faction_id`, `lane_id`, and `spawn_delay_seconds`.
- Extends `StageManifest.to_json()` with resolved stage, economy, wave, and input-log fields.

- [ ] **Step 1: Write the failing data-contract test**

```gdscript
func _init() -> void:
    var tutorial := _load_stage("res://data/stages/tutorial_stage.tres")
    var regular := _load_stage("res://data/stages/regular_stage.tres")
    _expect(tutorial.waves.size() == 4, "tutorial has four waves", failures)
    _expect(regular.waves.size() == 20, "regular stage has W1 through W20", failures)
    _expect(regular.waves[14].boss_kind == &"legendary", "W15 is legendary", failures)
    _expect(regular.waves[19].boss_kind == &"mythic", "W20 is mythic", failures)
```

- [ ] **Step 2: Run the test and confirm it fails because stage resources do not exist**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/stage_data_contract_test.gd`

- [ ] **Step 3: Implement the Resource contracts and runtime JSON manifest**

```gdscript
class_name StageDefinition
extends Resource

@export var stage_id: StringName
@export var starting_gold := 160
@export var starting_food_cap := 12
@export var tutorial_stage := false
@export var waves: Array[WaveDefinition] = []

func build_manifest(seed: int) -> StageManifest:
    var manifest := StageManifest.new()
    manifest.stage_id = str(stage_id)
    manifest.seed = seed
    manifest.wave_count = waves.size()
    manifest.waves = waves.map(func(wave): return wave.to_dictionary())
    return manifest
```

- [ ] **Step 4: Add `tutorial_stage.tres` and `regular_stage.tres` with declarative W1–W20 contents**

Use the shared IDs `shield_guard`, `archer`, `assassin`, `priest`, and `giant`; specify enemy teams with `visual_faction_id = &"veil"`, never an enemy archetype ID. Set W5 elite, W10 hero, W15 legendary giant boss, W16–W19 overtime, and W20 mythic giant boss.

- [ ] **Step 5: Run the data-contract test and commit**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/stage_data_contract_test.gd`

Commit: `feat: add deterministic tutorial and wave data`

### Task 2: Implement deterministic unit and three-lane battle simulation

**Files:**
- Create: `scripts/battle/unit_instance.gd`, `scripts/battle/lane_state.gd`, `scripts/battle/gate_state.gd`, `scripts/battle/outpost_state.gd`, `scripts/battle/clash_zone_state.gd`, `scripts/battle/battle_simulator.gd`
- Test: `tests/headless/battle_simulation_test.gd`

**Interfaces:**
- `BattleSimulator.spawn_unit(spawn: UnitSpawnDefinition) -> UnitInstance`
- `BattleSimulator.advance(delta: float) -> void`
- `BattleSimulator.snapshot() -> Dictionary`
- `LaneState` stores no references to another lane's ordinary unit list.

- [ ] **Step 1: Write failing simulation tests**

```gdscript
func test_shared_visuals_do_not_change_combat() -> void:
    var allied := simulator.spawn_unit(_spawn(&"shield_guard", &"lumern"))
    var veil := simulator.spawn_unit(_spawn(&"shield_guard", &"veil"))
    _expect(allied.combat_stats() == veil.combat_stats(), "visual faction must not change stats", failures)

func test_lanes_are_isolated() -> void:
    simulator.spawn_unit(_spawn(&"shield_guard", &"lumern", &"top"))
    _expect(not simulator.can_move_to_lane(&"top", &"middle"), "ordinary movement cannot cross lanes", failures)
```

- [ ] **Step 2: Run the test and confirm the missing simulator failure**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/battle_simulation_test.gd`

- [ ] **Step 3: Implement a fixed-step shared combat model**

`UnitInstance` derives all combat values from the registry archetype + tier + rank. It tracks target, state, health, cooldown, lane position, and deterministic animation offset. `BattleSimulator` advances at 0.1 seconds, searches only the current lane, uses attack preparation/hit/recovery, applies the approved gate multipliers, and removes dead units without creating faction-specific state machines.

- [ ] **Step 4: Implement gates, clash zones, and outpost transitions**

```gdscript
func apply_structure_damage(raw_damage: float, siege: bool) -> int:
    var multiplier := 2.0 if siege else 0.4
    return maxi(1, floori(raw_damage * multiplier * 100.0 / (100.0 + armor)))
```

Implement 10s neutralize + 10s capture at power 1, cap effective power at 2, 3s hold, 10%/sec reversion, 5s stabilization, building disable/ruin behavior, and independent gate collapse after two seconds.

- [ ] **Step 5: Run simulation tests and commit**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/battle_simulation_test.gd`

Commit: `feat: simulate shared units across three lanes`

### Task 3: Add economy, node construction, roulette, and deployment services

**Files:**
- Create: `scripts/core/stage_economy.gd`, `scripts/buildings/building_state.gd`, `scripts/buildings/building_service.gd`, `scripts/roulette/roulette_service.gd`, `scripts/units/deployment_service.gd`
- Test: `tests/headless/economy_roulette_test.gd`

**Interfaces:**
- `StageEconomy.try_spend_gold(amount: int) -> bool`
- `BuildingService.try_construct(outpost_id: StringName, node_id: StringName, building_id: StringName) -> bool`
- `RouletteService.spin(seed_input: Dictionary) -> Array[UnitSpawnDefinition]`
- `DeploymentService.deploy(card: UnitSpawnDefinition, lane_id: StringName, position: float) -> bool`

- [ ] **Step 1: Write failing economy and roulette tests**

```gdscript
_expect(economy.gold == 160, "regular stage starts at 160 gold", failures)
_expect(roulette.spin({"seed": 12}).size() > 0, "a valid spin produces deployable shared units", failures)
_expect(not buildings.try_construct(&"enemy_top", &"front_a", &"tower"), "enemy-owned node rejects player building", failures)
```

- [ ] **Step 2: Run the test and confirm it fails**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd`

- [ ] **Step 3: Implement minimal services**

Implement 160 starting gold, 12 food cap, +5 per active 20 seconds, +4 per controlled clash zone every 60 seconds, +2 per stable owned outpost every 30 seconds, 20 gold spin, and only `tower` plus `farm` building definitions. Completed buildings contribute roulette tokens; construction requires a currently owned, stabilized node and is locked during capture.

- [ ] **Step 4: Implement deterministic 3×3 roulette and hand/deploy flow**

Use the determinism service RNG and append each spin/build/deploy command to `StageManifest.input_log`. Roulette outputs only `UnitSpawnDefinition` objects with shared archetype IDs and player visual faction. Reject deployment when food capacity is exceeded; never charge food for un-deployed results.

- [ ] **Step 5: Run tests and commit**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/economy_roulette_test.gd`

Commit: `feat: add stage economy roulette and deployment`

### Task 4: Add waves, omen, boss, assassin bypass, and stage state machine

**Files:**
- Create: `scripts/core/stage_run.gd`, `scripts/waves/wave_director.gd`, `scripts/battle/assassin_bypass_state.gd`, `scripts/core/stage_progression.gd`
- Modify: `scripts/core/game_session.gd`, `scripts/core/combat_clock.gd`, `scripts/core/determinism_service.gd`
- Test: `tests/headless/stage_run_test.gd`

**Interfaces:**
- `StageRun.start(stage: StageDefinition, seed: int) -> void`
- `StageRun.submit_command(command: Dictionary) -> bool`
- `StageRun.advance(delta: float) -> void`
- `StageRun.result_state -> StringName` with `running`, `victory`, `defeat`.

- [ ] **Step 1: Write failing end-to-end state tests**

```gdscript
run.start(regular_stage, 1001)
_advance_until_wave(run, 15)
_expect(run.current_wave == 15, "W15 is reached", failures)
_expect(run.wave_director.current_wave().boss_kind == &"legendary", "W15 spawns the legendary boss", failures)
_advance_until_wave(run, 20)
_expect(run.wave_director.current_wave().boss_kind == &"mythic", "W20 spawns the mythic boss", failures)
```

- [ ] **Step 2: Run the test and confirm it fails**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/stage_run_test.gd`

- [ ] **Step 3: Implement wave scheduling and stage progression**

Spawn each wave from the declarative definition after its omen lead. Tutorial ends after W4. Normal stage records W15 as the standard legendary objective, permits W16–W20 only while still running, and ends on enemy-base destruction, the W15 objective, or the configured W20 outcome. `StageProgression` unlocks regular stage only after tutorial victory for the current app session.

- [ ] **Step 4: Implement assassin bypass timing**

```gdscript
const ENTRY_WINDUP := 1.0
const TRAVEL_DURATION := 9.0
const WARNING_LEAD := 2.5
const ARRIVAL_RECOVERY := 0.6
```

Remove the assassin from the lane list during travel, expose the defender warning at 6.5 seconds, spawn it 120 units behind the enemy outpost in the same lane, and give it zero capture power before and after bypass.

- [ ] **Step 5: Run end-to-end tests and commit**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/stage_run_test.gd`

Commit: `feat: run tutorial and twenty-wave stages`

### Task 5: Build playable Godot scenes and graybox presentation

**Files:**
- Create: `scenes/battle/battlefield.tscn`, `scenes/units/unit.tscn`, `scenes/ui/stage_hud.tscn`, `scenes/ui/stage_select.tscn`, `scripts/battle/battlefield_view.gd`, `scripts/units/unit_view.gd`, `scripts/ui/stage_hud.gd`, `scripts/ui/stage_select.gd`
- Modify: `scenes/main/main.tscn`, `scripts/core/game_session.gd`
- Test: `tests/headless/scene_contract_test.gd`

**Interfaces:**
- `BattlefieldView.bind_run(run: StageRun) -> void`
- `StageHud.bind_run(run: StageRun) -> void`
- `StageSelect.stage_requested(stage_id: StringName)` signal.

- [ ] **Step 1: Write the scene-contract test**

```gdscript
var packed := load("res://scenes/main/main.tscn") as PackedScene
var main := packed.instantiate()
_expect(main.get_node_or_null("Battlefield") != null, "main includes battlefield", failures)
_expect(main.get_node_or_null("UI/StageHud") != null, "main includes stage HUD", failures)
```

- [ ] **Step 2: Run the test and confirm it fails**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/scene_contract_test.gd`

- [ ] **Step 3: Implement scenes with intentionally minimal controls**

The stage-select view starts tutorial and locks the regular button until victory. The HUD exposes gold, food, current wave, omen, roulette spin, pending result cards, three lane deploy buttons, two building buttons, pause, retry, and result overlay. The battlefield view draws all lanes, gates, outposts, node state, clash ownership, bypass warning, and simple shared unit silhouettes from `FactionVisualProfile.palette_color`.

- [ ] **Step 4: Wire shared-unit state presentation**

`UnitView` renders state-driven geometry for deploy, idle, move, attack, hit, death, capture, bypass, structure attack, and victory. It reads only `UnitInstance` state and visual profile; no enemy scene or faction-specific timing code is created.

- [ ] **Step 5: Run scene test, editor load, and commit**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit`

Commit: `feat: add playable vertical slice scenes`

### Task 6: Add full integration, documentation, and manual QA handoff

**Files:**
- Create: `tests/headless/vertical_slice_integration_test.gd`, `docs/VERTICAL_SLICE_VALIDATION.md`
- Modify: `tests/headless/phase_0_contract_test.gd`, `README.md`, `docs/HANDOFF_CONTEXT.md`, `docs/ACTIVE_CONTEXT.md`, `docs/DOCUMENTATION_MAP.md`, `docs/goals/0002-core-vertical-slice.md`, `docs/issues/0032.md`

**Interfaces:**
- `vertical_slice_integration_test.gd` runs tutorial victory, stage unlock, fixed-seed regular-stage simulation, W1–W20 schedule, and a repeatability comparison.

- [ ] **Step 1: Write the failing full-flow integration test**

```gdscript
var first := _simulate_regular_stage(4242)
var second := _simulate_regular_stage(4242)
_expect(first.to_json() == second.to_json(), "same seed and command log reproduce the run", failures)
_expect(first.waves_seen == 20, "regular stage reaches W20", failures)
```

- [ ] **Step 2: Run the integration test and confirm it fails before final wiring**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/vertical_slice_integration_test.gd`

- [ ] **Step 3: Complete integration and documentation**

Update contexts and Goal 0002 to an implementation-complete record, update Issue #32 mirror to request GitHub closure after merge, and document exact commands plus the 1080p/720p manual path. Record remaining risks only for final art/audio, balance tuning, and save/campaign expansion.

- [ ] **Step 4: Run the complete verification suite**

Run:

```powershell
python -m unittest tests/python/test_issue_mirror.py
Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/phase_0_contract_test.gd
Get-ChildItem tests/headless/*_test.gd | ForEach-Object { & Godot_v4.7.1-stable_win64_console.exe --headless --path . -s ("res://" + $_.FullName.Substring((Get-Location).Path.Length + 1).Replace("\\", "/")) }
Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64_console.exe --headless --path . --quit-after 1
git diff --check
```

- [ ] **Step 5: Perform manual QA, commit, push, open a PR, and merge**

Run a complete tutorial and a regular-stage W1–W20 path at 1920×1080 and 1280×720. Commit with `feat: add playable vertical slice stage flow`, push `codex/vertical-slice-stage-progression`, open a PR to `main`, inspect comments/checks, merge after all required checks pass, then fast-forward the standard local clone using `tools/sync_repo.ps1`.
