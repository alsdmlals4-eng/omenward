# Single March Front and Three-Tab Command Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the three-front Run Command prototype with one deterministic advancing front and player-facing `내정 / 룰렛 / 전선` tabs, without reintroducing battlefield buildings or weakening the honest 3×3 probability engine.

**Architecture:** `BattleSimulator` owns exactly one `front` collection and the five route objectives. `StageRun` owns a single pending deployment queue and an `active_tab` UI state that never bypasses `command_phase`. `RunCommandScreen`, `StrategicMapView`, and `BattlefieldView` only present the three tabs and one directional front; they do not write combat, roulette, economic, or capture outcomes.

**Tech Stack:** Godot 4.7 GDScript; `.tres` resources; deterministic headless SceneTree tests; existing repository Python document-contract tests; ImageGen only for a separately approved terrain candidate.

**Spec:** `docs/design/APPROVED_OMENWARD_SINGLE_MARCH_FRONT_AND_THREE_TAB_COMMAND_2026-08-30.md`

## Global Constraints

- `ACTIVE_FRONT_ID = front`; `top / middle / bottom` must not appear in new stage data, public snapshots, UI, or player copy.
- The route grammar is `WARD_CITADEL -> WARD_FORWARD_BASE -> CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL`.
- Buildings remain a global roster only; the visible battlefield excludes building models, construction nodes, and placement controls.
- Slot capacity is `6 + stable Lumern Ward Forward Base + stable Lumern Clash Zone`; the single-front opening maximum is eight.
- There is exactly one visible fixed tower, derived from Ward Forward Base ownership, with zero capture power and no new income path.
- 3×3 direct row/column manipulation, deterministic results, no gambling framing, no fake near misses, and atomic irreversible commit remain mandatory.
- The existing true-alpha Shield Guard pair remains a bound runtime asset. The old three-front terrain is retained history, not a single-front runtime consumer.
- No save schema is currently implemented. Do not claim a save migration; define one only with a future versioned save implementation.
- Machine, runtime, human UX, player comprehension, rights, balance, and release evidence remain separate claims.

---

### Task 1: Establish the approved single-front canon and RED regression boundary

**Files:**
- Create: `tests/headless/single_front_contract_test.gd`
- Modify: `docs/CURRENT_CONFIRMED_DECISIONS.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/PROJECT_CORE.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

**Interfaces:**
- Consumes: `OMW-PLAN-20260830-SINGLE-MARCH-FRONT-THREE-TAB-01`.
- Produces: current routing to the single-front owner and tests that reject three public front IDs.

- [ ] **Step 1: Write the RED single-front domain contract.**

```gdscript
var run := _new_run(REGULAR_STAGE_PATH, 39001)
_expect(run.battle.front_ids() == [&"front"], "runtime exposes exactly one active front", failures)
_expect(not run.battle.accepts_front_id(&"top"), "legacy top ID is rejected", failures)
_expect(run.front_slot_capacity() == 6, "opening capacity starts at six", failures)
```

- [ ] **Step 2: Run it before implementation.**

```powershell
& $godot --headless --path . -s tests/headless/single_front_contract_test.gd
```

Expected: FAIL because the simulator exposes `top`, `middle`, and `bottom`.

- [ ] **Step 3: Register the approved owner and current routing.**

Mark historical three-front documents and evidence retained but superseded only for current topology, UI, and terrain consumer scope. Do not delete historical assets or evidence.

- [ ] **Step 4: Run document contracts and the focused RED contract.**

```powershell
& $py -m unittest discover -s tests/python -p "test_*.py" -v
& $godot --headless --path . -s tests/headless/single_front_contract_test.gd
```

Expected: relevant document contracts pass; the new Godot contract remains RED until Task 2.

### Task 2: Collapse battle state, objectives, and stage resources to one `front`

**Files:**
- Modify: `scripts/battle/battle_simulator.gd`
- Modify: `scripts/battle/battlefield_view.gd`
- Modify: `scripts/battle/assassin_bypass_state.gd`
- Modify: `scripts/data/unit_spawn_definition.gd`
- Modify: `data/stages/tutorial_stage.tres`
- Modify: `data/stages/regular_stage.tres`
- Modify: `tests/headless/battle_simulation_test.gd`
- Modify: `tests/headless/c2_battle_objective_test.gd`
- Test: `tests/headless/single_front_contract_test.gd`

**Interfaces:**
- Consumes: wave `UnitSpawnDefinition` records with `front_id == &"front"`.
- Produces: `BattleSimulator.FRONT_ID`, `front_ids() -> Array[StringName]`, `accepts_front_id(front_id) -> bool`, one formation, one gate per side, one Ward/Veil forward base, one clash zone, and one fixed tower.

- [ ] **Step 1: Add five-objective and one-tower RED assertions.**

```gdscript
var battle := run.battle
_expect(battle.fixed_towers.size() == 1, "one active front has one fixed tower", failures)
_expect(battle.route_state_for(&"front").has_all(["ward_forward", "clash", "veil_forward"]), "front exposes the three capturable route anchors", failures)
_expect(not battle.can_spawn_unit(_spawn(&"lumern", &"top", &"shield_guard")), "legacy spawn ID cannot enter combat", failures)
```

- [ ] **Step 2: Run the focused test and confirm RED.**

```powershell
& $godot --headless --path . -s tests/headless/single_front_contract_test.gd
```

Expected: FAIL on three collections and legacy spawn acceptance.

- [ ] **Step 3: Implement the smallest single-front simulator.**

```gdscript
const FRONT_ID := &"front"
const FRONT_IDS := [FRONT_ID]

func front_ids() -> Array[StringName]:
    return FRONT_IDS.duplicate()

func accepts_front_id(front_id: StringName) -> bool:
    return front_id == FRONT_ID

func can_spawn_unit(spawn: UnitSpawnDefinition) -> bool:
    return spawn != null and registry != null and registry.archetypes.has(str(spawn.archetype_id)) and accepts_front_id(spawn.front_id)
```

Replace loops over `LANE_IDS` with `FRONT_IDS`. Preserve position constants and objective order; do not invent combat numerics. Rename public `lane_id` snapshots and event payloads to `front_id`.

- [ ] **Step 4: Migrate resources and presentation coordinates.**

Set every stage spawn to `front_id = &"front"`. Draw one horizontal directional formation in `BattlefieldView`; remove top/middle/bottom Y offsets and branch drawing.

- [ ] **Step 5: Run focused simulation tests.**

```powershell
& $godot --headless --path . -s tests/headless/single_front_contract_test.gd
& $godot --headless --path . -s tests/headless/battle_simulation_test.gd
& $godot --headless --path . -s tests/headless/c2_battle_objective_test.gd
```

Expected: PASS with one front, one tower, and deterministic capture progression.

### Task 3: Convert commitment and building capacity to the single front

**Files:**
- Modify: `scripts/core/stage_run.gd`
- Modify: `scripts/core/stage_economy.gd`
- Modify: `scripts/core/core_ux_service.gd`
- Modify: `scripts/units/deployment_service.gd`
- Modify: `tests/headless/run_command_phase_contract_test.gd`
- Modify: `tests/headless/stage_run_test.gd`
- Modify: `tests/headless/global_building_roster_contract_test.gd`
- Test: `tests/headless/single_front_contract_test.gd`

**Interfaces:**
- Consumes: `BattleSimulator.FRONT_ID`, one fixed tower, and global roster capacity sync.
- Produces: `StageRun.assign_pending_reward(reward_index)`, `confirm_pending_deployment()`, `front_slot_capacity()`, and a pending queue whose every staged card uses `front_id = &"front"`.

- [ ] **Step 1: Add atomic queue RED assertions.**

```gdscript
_expect(run.begin_roulette_session({"seed": 39002}), "prepare begins an honest stopped board", failures)
_expect(run.lock_roulette_result() and run.confirm_roulette_result(), "result reaches commit", failures)
_expect(run.confirm_pending_deployment(), "all rewards commit to the only front without a selector", failures)
_expect((run.battle.front_units(&"front") as Array).size() > 0, "commit spawns the queue on the active front", failures)
```

- [ ] **Step 2: Run the contract and confirm RED.**

```powershell
& $godot --headless --path . -s tests/headless/single_front_contract_test.gd
```

Expected: FAIL because `assign_pending_reward` still requires a selected lane.

- [ ] **Step 3: Remove player-facing front assignment.**

```gdscript
func assign_pending_reward(reward_index: int) -> bool:
    if command_phase != COMMIT or reward_index < 0 or reward_index >= pending_roulette_rewards.size():
        return false
    pending_deployment_assignments[reward_index] = BattleSimulator.FRONT_ID
    return true
```

`confirm_pending_deployment` must set `front_id`, validate one front, and deploy atomically. No `top/middle/bottom` fallback remains.

- [ ] **Step 4: Synchronize capacity from exactly two eligible states.**

```gdscript
func _sync_building_roster_capacity() -> void:
    buildings.sync_occupation_capacity(
        1 if battle.ward_forward_is_stable_for(&"lumern") else 0,
        1 if battle.clash_is_stable_for(&"lumern") else 0,
    )
```

Keep the current inactive/no-refund/reactivation logic and assert the maximum capacity is eight.

- [ ] **Step 5: Run commitment, roster, and UX contracts.**

```powershell
& $godot --headless --path . -s tests/headless/single_front_contract_test.gd
& $godot --headless --path . -s tests/headless/run_command_phase_contract_test.gd
& $godot --headless --path . -s tests/headless/stage_run_test.gd
& $godot --headless --path . -s tests/headless/global_building_roster_contract_test.gd
& $godot --headless --path . -s tests/headless/c3_core_ux_test.gd
```

Expected: PASS; roulette remains deterministic and the roster has no battlefield placement path.

### Task 4: Build phase-gated `내정 / 룰렛 / 전선` tab controls

**Files:**
- Modify: `scenes/ui/run_command_screen.tscn`
- Modify: `scripts/ui/run_command_screen.gd`
- Modify: `tests/headless/scene_contract_test.gd`
- Modify: `tests/headless/roulette_picker_ui_test.gd`
- Create: `tests/headless/run_command_tab_contract_test.gd`
- Test: `tests/headless/run_command_tab_contract_test.gd`

**Interfaces:**
- Consumes: `StageRun.active_tab`, `set_active_tab(tab_id)`, `command_phase`, and building/roulette/front snapshots.
- Produces: `TabRail/DomesticTab`, `TabRail/RouletteTab`, `TabRail/FrontTab`, one visible work surface, and phase-locked actions.

- [ ] **Step 1: Write the tab ownership RED test.**

```gdscript
var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
_expect(screen.get_node_or_null("TabRail/DomesticTab") is Button, "domestic tab exists", failures)
_expect(screen.get_node_or_null("TabRail/RouletteTab") is Button, "roulette tab exists", failures)
_expect(screen.get_node_or_null("TabRail/FrontTab") is Button, "front tab exists", failures)
_expect(screen.has_method("visible_work_surface_id"), "screen exposes exactly one active work surface", failures)
```

- [ ] **Step 2: Run it and confirm RED.**

```powershell
& $godot --headless --path . -s tests/headless/run_command_tab_contract_test.gd
```

Expected: FAIL because the lower deck is phase-only and no tab rail exists.

- [ ] **Step 3: Add tab state without changing command state.**

```gdscript
const TAB_DOMESTIC := &"domestic"
const TAB_ROULETTE := &"roulette"
const TAB_FRONT := &"front"

func set_active_tab(tab_id: StringName) -> bool:
    if not [TAB_DOMESTIC, TAB_ROULETTE, TAB_FRONT].has(tab_id):
        return false
    active_tab = tab_id
    return true
```

Auto-focus domestic in PREPARE, roulette on spin, front at COMMIT/BATTLE, and keep action buttons disabled whenever `command_phase` forbids their action.

- [ ] **Step 4: Replace the commit selector with one queue summary.**

```gdscript
_commit_label.text = "획득 병력 %d개를 단일 전선에 되돌릴 수 없게 투입합니다." % run.pending_roulette_rewards.size()
```

Delete the three `OptionButton` assignments. The confirm button remains a single atomic action.

- [ ] **Step 5: Run UI contracts.**

```powershell
& $godot --headless --path . -s tests/headless/run_command_tab_contract_test.gd
& $godot --headless --path . -s tests/headless/scene_contract_test.gd
& $godot --headless --path . -s tests/headless/roulette_picker_ui_test.gd
```

Expected: PASS with one visible work surface and no top/middle/bottom selector text.

### Task 5: Replace the three-branch map with one advancing front projection

**Files:**
- Modify: `scripts/ui/strategic_map_view.gd`
- Modify: `scripts/battle/battlefield_view.gd`
- Modify: `scenes/battle/battlefield.tscn`
- Modify: `tests/headless/strategic_map_ui_contract_test.gd`
- Modify: `tests/headless/roulette_picker_ui_test.gd`
- Test: `tests/headless/single_front_contract_test.gd`

**Interfaces:**
- Consumes: `BattleSimulator.route_state_for(&"front")`, fixed tower state, current objective owner, and front unit positions.
- Produces: `StrategicMapView.route_state_for(&"front")`, `front_count() == 1`, `current_sector_id()`, and a wide single route with Ward on the left and Veil on the right.

- [ ] **Step 1: Add the one-route rendering RED test.**

```gdscript
map.bind_run(run)
_expect(map.front_count() == 1, "map has one active front", failures)
_expect(map.fixed_tower_count() == 1, "map draws one fixed tower", failures)
_expect(map.current_sector_id() == &"ward_forward", "opening focus is the Ward forward route sector", failures)
```

- [ ] **Step 2: Run it and confirm RED.**

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
```

Expected: FAIL because the projection still exposes three front rows.

- [ ] **Step 3: Draw one path and state-driven sector emphasis.**

```gdscript
const FRONT_ID := &"front"
const SECTOR_IDS := [&"ward_citadel", &"ward_forward", &"clash", &"veil_forward", &"veil_citadel"]

func current_sector_id() -> StringName:
    return _sector_for_route_state(route_state_for(FRONT_ID))
```

Draw only one broad route, terrain edges, one tower, objective markers, and unit positions. Do not draw river splits, lane rows, minimaps, construction pads, or buildings.

- [ ] **Step 4: Run presentation contracts.**

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
& $godot --headless --path . -s tests/headless/single_front_contract_test.gd
& $godot --headless --path . -s tests/headless/shield_guard_visual_asset_test.gd
```

Expected: PASS; the approved unit pair remains bound and the map has one route.

### Task 6: Prepare the new terrain image as a candidate, not an unverified runtime claim

**Files:**
- Create: `docs/images/planning/OMENWARD_SINGLE_MARCH_FRONT_TERRAIN_CANDIDATE_2026-08-30.md`
- Create: `tests/python/test_single_march_front_visual_contract.py`
- Create: `assets/art/battlefield/omenward_single_march_front_terrain_candidate_v1.png`

**Interfaces:**
- Consumes: the approved single-front visual brief and ImageGen output path/SHA-256.
- Produces: a `GENERATED_CANDIDATE` provenance record and user-facing preview; it does not produce a bound runtime asset.

- [ ] **Step 1: Write the candidate boundary test.**

```python
def test_single_front_terrain_is_not_promoted_by_generation() -> None:
    text = CANDIDATE.read_text(encoding="utf-8")
    assert "status: GENERATED_CANDIDATE" in text
    assert "runtime_binding: NOT_APPROVED" in text
    assert "three-front terrain is not a consumer" in text
```

- [ ] **Step 2: Generate one candidate using the approved brief.**

The candidate is an original 16:9 storybook-watercolor tactical terrain plate: wide traversable single route, no river cut, no parallel paths, no buildings, one small tower clearing, Ward-left/Veil-right color progression, open center, and enough negative space for SD units and UI markers.

- [ ] **Step 3: Record provenance and run the boundary test.**

```powershell
& $py -m unittest tests.python.test_single_march_front_visual_contract -v
```

Expected: PASS with candidate-only status. Show the preview to the user and request the separate asset lock before binding it to a scene.

### Task 7: Full verification, current-state readback, and bounded evidence record

**Files:**
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Create: `docs/reviews/ADVERSARIAL_SINGLE_MARCH_FRONT_IMPLEMENTATION_REVIEW_2026-08-30.md`

**Interfaces:**
- Consumes: completed single-front state, three-tab UI, one-route projection, and image-candidate status.
- Produces: exact machine results, explicitly separated runtime/human/asset-lock status, and five adversarial reviews.

- [ ] **Step 1: Run parser/import verification.**

```powershell
& $godot --headless --editor --quit --path .
```

Expected: exit code 0. This is script/scene import evidence only.

- [ ] **Step 2: Run every headless contract.**

```powershell
Get-ChildItem tests/headless -Filter '*_test.gd' | ForEach-Object { & $godot --headless --path . -s $_.FullName; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }
```

Expected: exit code 0 and no retained contract that requires public `top/middle/bottom` behavior.

- [ ] **Step 3: Run Python and approved operating-contract checks.**

```powershell
& $py -m unittest discover -s tests/python -p 'test_*.py' -v
& $py C:\Users\user\Documents\GitHub\Base\tools\check_approved_project_operating_contract.py --project-root . --base-repository C:\Users\user\Documents\GitHub\Base --protected-base 9a67a267a69c80fba6f25d5a37e360a15dcc2419 --approval docs/approvals/PROJECT_PROTECTED_CHANGE_APPROVAL_GLOBAL_ROSTER_AND_STRATEGIC_MAP_2026-08-30.json --external-approval true --check
git diff --check
```

Expected: report environment-only Base fixture failures separately; never suppress or call them a product pass.

- [ ] **Step 4: Perform five full-scope adversarial reviews.**

Each review must search for public legacy IDs, visible building-node paths, duplicate income, tab phase bypass, and unsupported evidence promotion. Record concrete commands, findings, and repairs.

- [ ] **Step 5: Run one live Godot smoke after code contracts are green.**

Observe PREPARE domestic roster, stopped 3×3 roulette, single queue commit, live single battle, tower ownership, and sector display. Record only `RUNTIME_TECHNICAL_SMOKE`; human UX and player comprehension remain `NOT_RUN` until human playtest.

## Plan Self-Review

- **Spec coverage:** Tasks 1–3 replace the three-front domain, preserve deterministic roulette and global slots, and make the lone tower/economy boundary testable. Tasks 4–5 implement the three tabs and one wide route. Task 6 isolates art production from asset promotion. Task 7 separates machine, runtime, human, and approval evidence.
- **Type consistency:** `BattleSimulator.FRONT_ID`, `front_ids`, `accepts_front_id`, `route_state_for`, `StageRun.active_tab`, `set_active_tab`, and `front_slot_capacity` are introduced before their consumers.
- **No placeholders:** final numerical balance and terrain promotion are deliberately outside this plan until separately observed or user-approved; no production task defers an unspecified implementation detail.
