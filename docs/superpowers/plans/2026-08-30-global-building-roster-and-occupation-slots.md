# Global Building Roster and Occupation Slots Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace per-outpost construction nodes with a player-only, priority-ordered global building roster whose capacity is `6 + stable Lumern forward bases + stable Lumern clash zones`, while showing exactly one fixed ownership tower on each shared front.

**Architecture:** `BuildingService` becomes the sole roster/effect authority. `StageRun` derives stable-objective counts from `BattleSimulator` and supplies them to the service before any snapshot, roulette calculation, or UI render. `BattleSimulator` owns objective transitions and three presentation-only fixed-tower states; `RunCommandScreen` renders the roster in PREPARE and `BattlefieldView` draws only routes, fixed towers, units, and ownership feedback.

**Tech Stack:** Godot 4.7 GDScript; deterministic headless SceneTree contract tests; Python documentation contracts; existing generated project UI/building textures only.

**Spec:** `docs/design/APPROVED_OMENWARD_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOTS_2026-08-30.md`

## Global Constraints

- `BATTLEFIELD_VISIBLE_EXCLUDES = CONSTRUCTION_PADS + PRODUCTION_BUILDINGS + MAP_BUILDING_POPUPS`.
- `BASE_BUILDING_SLOT_CAPACITY = 6`; only stable Lumern forward bases and stable Lumern clash zones grant one additional slot.
- Capacity loss locks cards below the top-to-bottom boundary without deleting their tier/history or refunding them.
- An inactive card contributes no passive effect or Roulette TokenSource.
- There are exactly three fixed route towers, one per front, with zero capture power and no invented combat numerics.
- Stage 1 roster mutation is forbidden; research/tier numerics remain simulation-pending.
- Generated planning images are not runtime assets; no new image is promoted by this plan.
- Runtime, human UX, player comprehension, release, and final-balance claims remain unverified unless separately observed.

---

### Task 1: Lock the Phase 2 contract and regression boundary

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOTS_2026-08-30.md`
- Create: `docs/superpowers/plans/2026-08-30-global-building-roster-and-occupation-slots.md`
- Modify: `docs/CURRENT_CONFIRMED_DECISIONS.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Test: `tests/python/test_global_building_roster_decision_contract.py`

**Interfaces:**
- Consumes: Issue #255 and current Phase 2 gate.
- Produces: `OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01` as the current owner for the migration.

- [x] **Step 1: Write the failing documentation contract.**

```python
def test_current_index_routes_to_global_roster_owner(self):
    self.assertIn("OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01", self.index)
    self.assertIn("FIXED_TOWER_COUNT_PER_SHARED_FRONT = 1", self.owner)
    self.assertIn("BUILDING_MAP_PLACEMENT = FORBIDDEN", self.owner)
```

- [x] **Step 2: Run the contract and verify it fails before routing is updated.**

Run: `python -m unittest tests.python.test_global_building_roster_decision_contract -v`

Expected: FAIL because the decision index still routes construction through per-outpost nodes.

- [x] **Step 3: Add the approved owner and current-index/context references.**

Update the decision count and active work gate without editing unrelated historical decisions. Mark construction pads and per-outpost building state superseded only inside this Phase 2 scope.

- [x] **Step 4: Run the documentation contract.**

Run: `python -m unittest tests.python.test_global_building_roster_decision_contract -v`

Expected: PASS.

### Task 2: Define RED behavior for roster capacity and fixed-tower lifecycle

**Files:**
- Create: `tests/headless/global_building_roster_contract_test.gd`
- Modify: `tests/headless/c2_battle_objective_test.gd`
- Modify: `tests/headless/run_command_phase_contract_test.gd`
- Test: `tests/headless/global_building_roster_contract_test.gd`

**Interfaces:**
- Consumes: `BuildingService.sync_occupation_capacity(forward_count, clash_count)`, `try_install(building_id)`, `roster_snapshot()`, and `BattleSimulator.fixed_towers`.
- Produces: deterministic checks for all active/inactive effect, tower, income, and Stage 1 gates.

- [x] **Step 1: Write a failing global roster contract.**

```gdscript
buildings.sync_occupation_capacity(3, 0)
_expect(buildings.unlocked_slot_capacity() == 9, "three stable forward bases unlock nine roster slots", failures)
_expect(buildings.try_install(&"farm"), "a non-tutorial run installs from the global roster", failures)
buildings.sync_occupation_capacity(0, 0)
_expect(buildings.roster_snapshot()[0]["state"] == "inactive_locked", "loss locks without deleting", failures)
_expect(economy.food_cap == 12, "inactive farm removes passive food cap", failures)
buildings.sync_occupation_capacity(3, 0)
_expect(buildings.roster_snapshot()[0]["state"] == "active", "recovery reactivates top-down", failures)
```

- [x] **Step 2: Add failing tower and UI-boundary assertions.**

```gdscript
_expect(battle.fixed_towers[&"top"].owner_team_id == &"lumern", "one top-front tower starts with Lumern", failures)
battle.outposts[&"lumern"][&"top"].begin_capture(&"veil", 1.0)
battle.advance(0.1)
_expect(not battle.fixed_towers[&"top"].active, "tower disables during capture", failures)
_expect(not battlefield_source.contains("_draw_outpost_nodes"), "battlefield has no construction-node drawing", failures)
```

- [x] **Step 3: Run the focused test to verify RED.**

Run: `godot --headless --path . -s tests/headless/global_building_roster_contract_test.gd`

Expected: FAIL because the current service requires `outpost_id/node_id`, has no capacity API, and no fixed tower state exists.

### Task 3: Replace per-outpost building state with the global roster service

**Files:**
- Modify: `scripts/buildings/building_state.gd`
- Modify: `scripts/buildings/building_service.gd`
- Modify: `scripts/data/building_definition.gd`
- Modify: `scripts/core/core_ux_service.gd`
- Test: `tests/headless/global_building_roster_contract_test.gd`

**Interfaces:**
- Consumes: stable objective counts and `StageEconomy` methods.
- Produces: `BuildingService.set_roster_mutation_allowed(bool)`, `sync_occupation_capacity(int, int)`, `try_install(StringName)`, `unlocked_slot_capacity()`, `roster_snapshot()`, and unchanged `roulette_token_sources_snapshot()`.

- [x] **Step 1: Implement the smallest global `BuildingState`.**

```gdscript
const ACTIVE := &"active"
const INACTIVE_LOCKED := &"inactive_locked"
var slot_index := -1
var tier_id: StringName = &"tier_1"
var definition: BuildingDefinition
var effect_active := false
```

- [x] **Step 2: Implement capacity sync before installation/effect reads.**

```gdscript
func sync_occupation_capacity(stable_forward_base_count: int, stable_clash_zone_count: int) -> void:
    _unlocked_slot_capacity = BASE_SLOT_CAPACITY + maxi(0, stable_forward_base_count) + maxi(0, stable_clash_zone_count)
    for state in _buildings:
        _set_effect_active(state, state.slot_index < _unlocked_slot_capacity)
        state.state = state.ACTIVE if state.effect_active else state.INACTIVE_LOCKED
```

- [x] **Step 3: Install into the first empty active roster slot.**

```gdscript
func try_install(building_id: StringName) -> bool:
    if not _roster_mutation_allowed or not definitions.has(building_id):
        return false
    var slot_index := _first_empty_active_slot()
    if slot_index < 0 or not economy.try_spend_gold(definitions[building_id].gold_cost):
        return false
    var state := BuildingStateScript.new(slot_index, definitions[building_id])
    _buildings.append(state)
    _set_effect_active(state, true)
    return true
```

- [x] **Step 4: Convert Core UX comparison into roster availability data.**

`CoreUxService` must derive install previews from `definitions` and `roster_snapshot`, with no `HOME_OUTPOST_ID`, node ID, or objective ownership predicate.

- [x] **Step 5: Run the focused test.**

Run: `godot --headless --path . -s tests/headless/global_building_roster_contract_test.gd`

Expected: roster capacity, effect loss, deterministic top-down reactivation, and token-source removal pass.

### Task 4: Add objective-derived fixed-tower state and preserve income boundaries

**Files:**
- Create: `scripts/battle/fixed_tower_state.gd`
- Modify: `scripts/battle/battle_simulator.gd`
- Modify: `scripts/core/stage_run.gd`
- Modify: `scripts/core/stage_economy.gd`
- Test: `tests/headless/global_building_roster_contract_test.gd`
- Test: `tests/headless/c2_battle_objective_test.gd`

**Interfaces:**
- Consumes: `OutpostState.is_stable_for`, `BattleSimulator.stable_owned_outpost_count`, and `controlled_clash_count`.
- Produces: `fixed_towers[lane_id]`, `stable_player_forward_base_count()`, and a single `StageRun._sync_building_roster_capacity()` bridge.

- [x] **Step 1: Implement a presentation-only tower state.**

```gdscript
class_name FixedTowerState
extends RefCounted

var lane_id: StringName
var owner_team_id: StringName = &""
var active := false
const capture_power := 0.0
```

- [x] **Step 2: Refresh each tower from its Ward-side forward objective.**

```gdscript
func _refresh_fixed_towers() -> void:
    for lane_id in LANE_IDS:
        var objective: OutpostState = outposts[&"lumern"][lane_id]
        fixed_towers[lane_id].active = objective.state == objective.STABLE
        fixed_towers[lane_id].owner_team_id = objective.owner_team_id if fixed_towers[lane_id].active else &""
```

- [x] **Step 3: Synchronize roster capacity after battle objective updates and before every roster consumer.**

```gdscript
func _sync_building_roster_capacity() -> void:
    buildings.sync_occupation_capacity(
        battle.stable_owned_outpost_count(&"lumern"),
        battle.controlled_clash_count(&"lumern"),
    )
```

- [x] **Step 4: Keep the existing two income paths and prove no third payment is added.**

The test must retain the current 60-second `base + control + forward-base` total and assert that fixed-tower ownership does not add a payment.

- [x] **Step 5: Run focused objective tests.**

Run: `godot --headless --path . -s tests/headless/global_building_roster_contract_test.gd`

Run: `godot --headless --path . -s tests/headless/c2_battle_objective_test.gd`

Expected: PASS.

### Task 5: Replace construction controls and map nodes with player-only roster presentation

**Files:**
- Modify: `scenes/ui/run_command_screen.tscn`
- Modify: `scripts/ui/run_command_screen.gd`
- Modify: `scenes/ui/stage_hud.tscn`
- Modify: `scripts/ui/stage_hud.gd`
- Modify: `scripts/battle/battlefield_view.gd`
- Modify: `tests/headless/scene_contract_test.gd`
- Test: `tests/headless/global_building_roster_contract_test.gd`

**Interfaces:**
- Consumes: `BuildingService.roster_snapshot()`, `unlocked_slot_capacity()`, `try_install`, and `BattleSimulator.fixed_towers`.
- Produces: PREPARE roster cards ordered by slot and visible fixed-tower ownership feedback.

- [x] **Step 1: Replace all `construct_home` and `construct_at_outpost` UI calls with `install_building`.**

```gdscript
func _on_barracks_pressed() -> void:
    if run != null:
        run.install_building(&"barracks")
```

- [x] **Step 2: Render a single roster card list in PREPARE.**

```gdscript
for entry in run.building_roster_snapshot():
    var card := Button.new()
    card.text = "#%d %s · %s" % [entry.slot_index + 1, entry.display_name, entry.state]
    card.disabled = not entry.can_install_or_active
    _roster_container.add_child(card)
```

The visible text must describe slot capacity and locked reason. It must not offer coordinates, forward-base selection, or map placement. The roulette panel remains a separate lower-deck surface.

- [x] **Step 3: Draw exactly one fixed tower and no construction nodes per lane.**

```gdscript
func _draw_fixed_tower(lane_id: StringName, center: Vector2) -> void:
    var tower := run.battle.fixed_towers[lane_id]
    var color := Color(0.55, 0.72, 0.98) if tower.owner_team_id == &"lumern" else Color(0.72, 0.36, 0.76)
    draw_rect(Rect2(center - Vector2(7, 15), Vector2(14, 30)), color if tower.active else Color(0.35, 0.35, 0.35), true)
```

- [x] **Step 4: Update scene assertions.**

The test must assert a `BuildingRoster` container exists, legacy map node methods are absent, and the three fixed tower states can be rendered without new texture resources.

- [x] **Step 5: Run scene and roster contracts.**

Run: `godot --headless --path . -s tests/headless/scene_contract_test.gd`

Run: `godot --headless --path . -s tests/headless/global_building_roster_contract_test.gd`

Expected: PASS.

### Task 6: Reconcile regressions and record evidence honestly

**Files:**
- Modify: `tests/headless/stage_run_test.gd`
- Modify: `tests/headless/run_command_phase_contract_test.gd`
- Modify: `tests/headless/c3_core_ux_test.gd`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

**Interfaces:**
- Consumes: completed roster, tower, and UI contracts.
- Produces: a bounded implementation/evidence record with runtime and human gates unchanged unless executed.

- [x] **Step 1: Update old node-oriented assertions.**

Replace `construct_home` success expectations with Stage 1 rejection and non-tutorial `install_building` success. Preserve the roulette, deployment, economy, and battle contract assertions.

- [x] **Step 2: Run deterministic verification.**

Run: `godot --headless --editor --quit --path .`

Run: `godot --headless --path . -s tests/headless/global_building_roster_contract_test.gd`

Run: `godot --headless --path . -s tests/headless/c2_battle_objective_test.gd`

Run: `godot --headless --path . -s tests/headless/run_command_phase_contract_test.gd`

Run: `godot --headless --path . -s tests/headless/c3_core_ux_test.gd`

Run: `godot --headless --path . -s tests/headless/scene_contract_test.gd`

Expected: all named deterministic checks pass.

- [x] **Step 3: Run the Python suite with the bundled Python 3.12 runtime.**

Run: `python -m unittest discover -s tests/python -p 'test_*.py' -v`

Expected: document the CI-only Base checkout prerequisite separately; do not call it a product regression if the checkout is absent locally.

- [x] **Step 4: Record evidence without promotion.**

Set only actually executed static/headless results to `MACHINE_VERIFIED`. Keep target-resolution runtime observation, human UX, player comprehension, asset provenance promotion, final balance, and release status as `NOT_RUN` or `UNVERIFIED`.

## Self-Review

**Spec coverage:** Tasks 2–3 cover capacity, priority, no-refund loss, reactivation, and effect/token deactivation. Task 4 covers ownership, tower disablement, zero capture contribution, and no income duplication. Task 5 covers the roster-only player surface and removal of visible construction nodes. Task 6 covers Stage 1, regressions, and evidence boundaries.

**Placeholder scan:** No task defers an implementation detail with a placeholder. Simulation-pending tower and upgrade numerics are explicitly excluded rather than invented.

**Type consistency:** `BuildingService` exposes `sync_occupation_capacity`, `try_install`, `roster_snapshot`, and `unlocked_slot_capacity`; `StageRun` exposes `install_building` and `building_roster_snapshot`; `BattleSimulator` exposes `fixed_towers` and objective count methods. All later tasks use these exact names.
