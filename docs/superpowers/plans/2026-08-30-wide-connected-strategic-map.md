# Wide Connected Strategic Map Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the three Run Command progress-card minimaps with one wide, readable strategic map that projects existing three-front battle state without changing simulation rules.

**Architecture:** `StrategicMapView` is a presentation-only `Control`: it reads a bound `StageRun`, draws one Ward root, one Veil root, three broad connected routes, three fixed-tower anchors, objective states, and compact lane labels. `RunCommandScreen` owns only the map binding and its responsive layout; `BattlefieldView` shares the same fixed simulation positions so dynamic unit sprites align with the map. The map never writes battle, roulette, economy, building, or deployment state.

**Tech Stack:** Godot 4.7 GDScript, `.tscn` Control scene hierarchy, existing deterministic headless SceneTree contracts, Python canon-contract tests.

**Spec:** `docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md`; `docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md`; `docs/design/APPROVED_OMENWARD_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOTS_2026-08-30.md`; GitHub Issue #235.

## Global Constraints

- `MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT`.
- There are exactly three shared fronts and exactly one fixed visible tower per shared front.
- The battlefield excludes construction pads, map buildings, and map-building popups; the player-only building surface remains `PREPARE__GLOBAL_BUILDING_ROSTER`.
- The map is contextual presentation only: no roulette, balance, economy, combat, deployment, or capture-rule mutation.
- A newly generated no-river background remains `GENERATED_CANDIDATE`; this plan must not promote or bind it until its independent asset/provenance gate is satisfied.
- Existing user/runtime/human readability evidence remains `NOT_RUN` unless actually captured and reviewed.

---

### Task 1: Declare the strategic-map screen contract

**Files:**
- Create: `tests/headless/strategic_map_ui_contract_test.gd`
- Modify: `tests/headless/roulette_picker_ui_test.gd`
- Modify: `tests/headless/scene_contract_test.gd`

**Interfaces:**
- Consumes: `res://scenes/ui/run_command_screen.tscn`.
- Produces: the required `StrategicMap` node contract, and explicitly rejects the old `Fronts/Top|Middle|Bottom` progress-card hierarchy.

- [x] **Step 1: Write the failing SceneTree test**

```gdscript
var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
_expect(screen.get_node_or_null("StrategicMap") is Control,
    "Run Command exposes one primary strategic map", failures)
_expect(screen.get_node_or_null("Fronts") == null,
    "three per-front progress-card minimaps are removed", failures)
_expect(screen.get_node_or_null("StrategicMap").has_method("bind_run"),
    "strategic map reads existing StageRun state", failures)
```

- [x] **Step 2: Run the contract to verify it fails**

Run:

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
```

Expected: FAIL because `StrategicMap` does not exist and the old `Fronts` hierarchy still exists.

- [x] **Step 3: Update existing UI contracts**

Replace old `Fronts/Top` translucency assertions with assertions for the single primary map and keep the roulette grid assertions intact.

- [x] **Step 4: Run the three UI contracts**

Run:

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
& $godot --headless --path . -s tests/headless/roulette_picker_ui_test.gd
& $godot --headless --path . -s tests/headless/scene_contract_test.gd
```

Expected: first test remains RED until Task 2; revised legacy contracts parse and retain their unrelated behavior checks.

### Task 2: Implement the read-only connected map projection

**Files:**
- Create: `scripts/ui/strategic_map_view.gd`
- Modify: `scenes/ui/run_command_screen.tscn`
- Modify: `scripts/ui/run_command_screen.gd`
- Test: `tests/headless/strategic_map_ui_contract_test.gd`

**Interfaces:**
- Consumes: `StageRun` with `battle.lanes`, `battle.outposts`, `battle.clash_zones`, and `battle.fixed_towers`.
- Produces: `StrategicMapView.bind_run(assigned_run: Variant) -> void`, and renders its own ownership/forecast labels without mutating `assigned_run`.

- [x] **Step 1: Write the failing map-state test**

```gdscript
var map := StrategicMapView.new()
map.bind_run(run)
_expect(map.front_count() == 3, "map retains exactly three shared fronts", failures)
_expect(map.fixed_tower_count() == 3, "map presents one fixed tower per front", failures)
_expect(map.has_method("route_state_for"), "map exposes read-only route state", failures)
```

- [x] **Step 2: Run the test to verify it fails**

Run:

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
```

Expected: FAIL because `StrategicMapView` is absent.

- [x] **Step 3: Implement the minimal read-only view**

Create a `Control` with fixed semantic anchors for one Ward root, one Veil root, three left/right forward-base pairs, and three central clash anchors. Draw broad connected route bands and their outline, not a second battle simulation. Derive marker tint and text only from objective/fixed-tower snapshots; expose `front_count`, `fixed_tower_count`, and `route_state_for` as queries.

- [x] **Step 4: Replace the old card hierarchy**

Remove `Fronts` and its three `ProgressBar` trees from `run_command_screen.tscn`; add `StrategicMap` between `TopBar` and the adaptive lower control deck. In `RunCommandScreen.bind_run` / refresh, call `StrategicMap.bind_run(run)` and delete `_refresh_fronts`. Do not add building controls to the map.

- [x] **Step 5: Run the focused contracts**

Run:

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
& $godot --headless --path . -s tests/headless/roulette_picker_ui_test.gd
& $godot --headless --path . -s tests/headless/scene_contract_test.gd
```

Expected: PASS with the map retaining all three fronts and no legacy progress-card hierarchy.

### Task 3: Align dynamic battlefield units and fixed towers to the wide map

**Files:**
- Modify: `scripts/battle/battlefield_view.gd`
- Modify: `scenes/battle/battlefield.tscn`
- Test: `tests/headless/strategic_map_ui_contract_test.gd`

**Interfaces:**
- Consumes: deterministic simulator positions `0..100`, `BattleSimulator.OUTPOST_POSITIONS`, and `BattleSimulator.CLASH_POSITION`.
- Produces: `BattlefieldView.world_position_for(lane_id: StringName, lane_position: float) -> Vector2` for presentation alignment only.

- [x] **Step 1: Add the failing alignment assertion**

```gdscript
var battlefield_view := BattlefieldView.new()
var clash := battlefield_view.world_position_for(&"middle", 50.0)
_expect(absf(clash.x - 360.0) < 8.0, "middle clash is centered in the strategic map", failures)
_expect(battlefield_view.world_position_for(&"top", 30.0).y < clash.y,
    "top route remains above the middle route", failures)
```

- [x] **Step 2: Run it to verify it fails**

Run:

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
```

Expected: FAIL because `world_position_for` does not exist.

- [x] **Step 3: Centralize the presentation coordinate transform**

Implement one position transform for unit sprite placement, tower anchors, clash warnings, and route overlays. Place all three routes inside the visible map rectangle; do not adjust `BattleSimulator` positions or any combat arithmetic.

- [x] **Step 4: Run focused contracts**

Run:

```powershell
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
& $godot --headless --path . -s tests/headless/global_building_roster_contract_test.gd
& $godot --headless --path . -s tests/headless/stage_run_test.gd
```

Expected: PASS; fixed-tower ownership and building roster behavior are unchanged.

### Task 4: Record the terrain promotion boundary and verify the complete non-runtime slice

**Files:**
- Create: `docs/images/planning/OMENWARD_WIDE_CONNECTED_STRATEGIC_FRONT_TERRAIN_CANDIDATE_2026-08-30.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Test: `tests/python/test_wide_connected_strategic_map_contract.py`

**Interfaces:**
- Consumes: generated terrain candidate and SHA-256, explicit user approval, current visual lock, global-roster decision, and Issue #235.
- Produces: a candidate provenance record plus an approved-asset record that binds the terrain to its consumer while preserving the independent runtime/human-observation gates.

- [x] **Step 1: Write the failing Python contract**

```python
def test_candidate_is_not_promoted_without_runtime_asset_lock() -> None:
    text = CANDIDATE_RECORD.read_text(encoding="utf-8")
    assert "status: GENERATED_CANDIDATE" in text
    assert "runtime_asset: NOT_CREATED" in text
    assert "Issue #235" in text
```

- [x] **Step 2: Run it to verify it fails**

Run:

```powershell
& $py -m unittest tests.python.test_wide_connected_strategic_map_contract -v
```

Expected: FAIL because the candidate record does not exist.

- [x] **Step 3: Record candidate provenance, then the approved consumer binding**

Record the ImageGen source path, SHA-256, exact no-river/connected-route brief, and the initial `GENERATED_CANDIDATE` boundary. After the user's explicit approval, register the reviewed terrain record, place the raster at its declared runtime asset path, bind it to the battlefield consumer, and retain `RUNTIME_NOT_RUN` plus human-observation limits. Update current routing to distinguish this bound terrain from the still-pending Storybook SD unit runtime cells.

- [x] **Step 4: Run complete mechanical verification**

Run:

```powershell
Get-ChildItem tests/headless -Filter '*_test.gd' | ForEach-Object { & $godot --headless --path . -s $_.FullName; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }
& $godot --headless --editor --quit --path .
& $py -m unittest discover -s tests/python -p "test_*.py" -v
python C:\Users\user\Documents\GitHub\Base\tools\check_project_operating_contract.py --project-root . --base-repository C:\Users\user\Documents\GitHub\Base --check
git diff --check
```

Observed: all 25 headless Godot contracts passed. The Python suite is rerun after each contract-relevant repair; its only remaining local failure is the known CI-only `_base_recovery` checkout fixture, which must be provided by CI rather than fabricated locally. Editor import is machine parse/import evidence only, never visual/human runtime PASS.

- [ ] **Step 5: Commit the coherent non-runtime slice**

```powershell
git add scripts/ui/strategic_map_view.gd scripts/ui/run_command_screen.gd scenes/ui/run_command_screen.tscn scripts/battle/battlefield_view.gd scenes/battle/battlefield.tscn tests/headless/strategic_map_ui_contract_test.gd tests/headless/roulette_picker_ui_test.gd tests/headless/scene_contract_test.gd docs/images/planning/OMENWARD_WIDE_CONNECTED_STRATEGIC_FRONT_TERRAIN_CANDIDATE_2026-08-30.md docs/ACTIVE_CONTEXT.md docs/CURRENT_IMPLEMENTATION_STATUS.md docs/HANDOFF_CONTEXT.md tests/python/test_wide_connected_strategic_map_contract.py docs/superpowers/plans/2026-08-30-wide-connected-strategic-map.md
git commit -m "feat: add wide connected strategic map projection"
```

## Plan Self-Review

- **Spec coverage:** Tasks 1–3 cover the one-root/three-shared-front/one-root topology, broad readable routes, exactly three towers, and dynamic unit alignment. Task 4 preserves the candidate-to-approved terrain provenance trail and evidence ceiling while leaving unit-cell approval and runtime observation separate.
- **Scope:** No task changes simulation, roulette, economy, deployment, or capture semantics. Global buildings remain in the existing player-only roster.
- **Type consistency:** `StrategicMapView.bind_run`, `front_count`, `fixed_tower_count`, `route_state_for`, and `BattlefieldView.world_position_for` are introduced before every consuming test or caller.
- **Placeholder scan:** No unresolved implementation placeholders are left in the task steps.
