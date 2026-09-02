# Battle-Primary Hierarchy Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore the approved single-front battle screen hierarchy so the close battle, not a blank lower deck or a second map, carries the visual mass.

**Architecture:** `RunCommandScreen` changes rects only when `StageRun.command_phase == BATTLE`; outside BATTLE it restores the existing work-surface layout. `BattleFocusView` remains a read-only projection, but uses a documented 104px role cell and restrained ground shadows. `MarchMinimapView` remains read-only while exposing a small presentation contract and drawing five connected sector cells. No domain, save, asset, or economy data changes.

**Tech Stack:** Godot 4.7 / GDScript, project headless SceneTree contracts, project-local validator, Hera only when an Omenward editor is available.

**Spec:** `docs/superpowers/specs/2026-09-02-battle-primary-hierarchy-recovery-design.md`

## Global Constraints

- Keep one active front, one fixed tower, the five-sector route, top one-row read-only minimap, and no unit replication on the minimap.
- Preserve `y=0.36..0.80` as the prop-free unit travel corridor, and do not add map buildings, construction nodes, fences, or barricades.
- Reuse only the locked foundation, six terrain props, and already bound role profiles. Do not create or promote raster assets in this task.
- BATTLE uses `BattleFocus 926×304`, `MarchMinimap 926×40`, `LowerDeck 928×106`; non-BATTLE keeps `LowerDeck 928×164`.
- Preserve all existing tabs, phase gates, roulette handling, front commitment, data/save behavior, human-evidence and rights ceilings.

### Task 1: Establish the layout-recovery RED contract

**Files:**
- Create: `tests/headless/battle_hierarchy_recovery_contract_test.gd`
- Read: `scenes/ui/run_command_screen.tscn`
- Read: `scripts/ui/run_command_screen.gd`
- Read: `scripts/ui/battle_focus_view.gd`
- Read: `scripts/ui/march_minimap_view.gd`

**Interfaces:**
- Consumes: `RunCommandScreen.bind_run(run)`, `StageRun.BATTLE`, `BattleFocusView`, `MarchMinimapView`.
- Produces: a failing contract for `BattleFocusView.role_display_cell_size()`, `MarchMinimapView.presentation_contract()`, and BATTLE-only rect changes.

- [x] **Step 1: Write the failing test**

```gdscript
screen.bind_run(run)
_enter_battle(run, screen)
_expect(battle_focus.size == Vector2(926, 304), "BATTLE grants the close battle the recovered visual height", failures)
_expect(lower_deck.size == Vector2(928, 106), "BATTLE compresses the explanatory deck", failures)
_expect(battle_focus.role_display_cell_size() == Vector2(104, 104), "roles receive the readable V2 cell", failures)
var contract := march_minimap.presentation_contract()
_expect(contract == {"front_count": 1, "sector_count": 5, "top_single_row": true, "read_only": true, "unit_replication": false}, "minimap is a five-sector context ribbon", failures)
```

- [x] **Step 2: Run the focused SceneTree test and verify RED**

Run: `& $godot --headless --path . -s tests/headless/battle_hierarchy_recovery_contract_test.gd`

Expected: FAIL because BATTLE still uses `926×256`, the lower deck stays `928×164`, and the two new read-only presentation methods do not exist.

### Task 2: Implement BATTLE-only rect routing

**Files:**
- Modify: `scripts/ui/run_command_screen.gd`
- Modify: `scenes/ui/run_command_screen.tscn`
- Test: `tests/headless/battle_hierarchy_recovery_contract_test.gd`

**Interfaces:**
- Consumes: `run.command_phase`, `BattleFocusViewport`, `MarchMinimap`, `LowerDeck`.
- Produces: `_apply_phase_layout(phase: StringName) -> void`, restoring a default non-BATTLE lower deck and applying the V2 BATTLE rects.

- [x] **Step 1: Add rect constants and a layout router**

```gdscript
const DEFAULT_LOWER_DECK_RECT := Rect2(16, 364, 928, 164)
const BATTLE_FOCUS_RECT := Rect2(16, 110, 926, 304)
const BATTLE_MINIMAP_RECT := Rect2(16, 62, 926, 40)
const BATTLE_LOWER_DECK_RECT := Rect2(16, 422, 928, 106)

func _apply_phase_layout(phase: StringName) -> void:
    var is_battle := phase == run.BATTLE
    _battle_focus.position = BATTLE_FOCUS_RECT.position
    _battle_focus.size = BATTLE_FOCUS_RECT.size
    _march_minimap.position = BATTLE_MINIMAP_RECT.position
    _march_minimap.size = BATTLE_MINIMAP_RECT.size
    var deck_rect := BATTLE_LOWER_DECK_RECT if is_battle else DEFAULT_LOWER_DECK_RECT
    $LowerDeck.position = deck_rect.position
    $LowerDeck.size = deck_rect.size
```

- [x] **Step 2: Invoke `_apply_phase_layout` before refreshing visible panels**

```gdscript
func _refresh() -> void:
    if run == null:
        return
    var phase: StringName = run.command_phase
    _apply_phase_layout(phase)
    # existing state labels, visibility, and action refresh remain below
```

- [x] **Step 3: Update the scene’s neutral default rects to match the non-BATTLE layout**

Keep `BattleFocusViewport` and `MarchMinimap` hidden until BATTLE. Keep the default `LowerDeck` at `x=16, y=364, w=928, h=164`; the dynamic BATTLE rect is applied from the live phase only.

- [x] **Step 4: Re-run the focused contract and verify the rect assertions are GREEN**

Run: `& $godot --headless --path . -s tests/headless/battle_hierarchy_recovery_contract_test.gd`

Expected: PASS for BATTLE and non-BATTLE rect transitions while existing phase/tabs keep their original behavior.

### Task 3: Make the battle and context ribbon carry their intended visual roles

**Files:**
- Modify: `scripts/ui/battle_focus_view.gd`
- Modify: `scripts/ui/march_minimap_view.gd`
- Test: `tests/headless/battle_hierarchy_recovery_contract_test.gd`
- Test: `tests/headless/battle_primary_march_minimap_contract_test.gd`
- Test: `tests/headless/close_battlefield_redesign_contract_test.gd`

**Interfaces:**
- Produces: `BattleFocusView.role_display_cell_size() -> Vector2` returning `Vector2(104, 104)`.
- Produces: `MarchMinimapView.presentation_contract() -> Dictionary` returning five static read-only presentation invariants.

- [x] **Step 1: Add a V2 role display-cell method before changing draw geometry**

```gdscript
const ROLE_DISPLAY_CELL_SIZE := Vector2(104, 104)

func role_display_cell_size() -> Vector2:
    return ROLE_DISPLAY_CELL_SIZE
```

- [x] **Step 2: Replace the 88px circular-pad emphasis with a 104px role cell and a restrained ground shadow**

```gdscript
var draw_rect := Rect2(center - Vector2(52.0, 83.0), ROLE_DISPLAY_CELL_SIZE)
draw_circle(center + Vector2(0.0, 22.0), 22.0, Color(0.01, 0.02, 0.04, 0.34))
```

Do not draw the former large faction ring/arc. Preserve unit health bars, faction facing, role lookup, one tower, and terrain placement validation.

- [x] **Step 3: Expose a minimap presentation contract and draw connected sector cells in one row**

```gdscript
func presentation_contract() -> Dictionary:
    return {
        "front_count": 1,
        "sector_count": 5,
        "top_single_row": true,
        "read_only": true,
        "unit_replication": false,
    }
```

Each cell uses only its sector label, ownership/contested color, current-sector outline, and the existing single tower glyph at Ward Forward. It must not draw unit markers, counts, battle effects, controls, or a second tower.

- [x] **Step 4: Re-run focused and retained battle-layout contracts**

Run:

```powershell
& $godot --headless --path . -s tests/headless/battle_hierarchy_recovery_contract_test.gd
& $godot --headless --path . -s tests/headless/battle_primary_march_minimap_contract_test.gd
& $godot --headless --path . -s tests/headless/close_battlefield_redesign_contract_test.gd
```

Expected: PASS; all one-front, one-tower, prop-band, no-map-building, and top-read-only constraints remain green.

### Task 4: Reconcile canonical blueprint and runtime evidence owners

**Files:**
- Modify: `docs/superpowers/specs/2026-09-02-battle-primary-hierarchy-recovery-design.md`
- Modify: `docs/superpowers/plans/2026-09-02-battle-primary-hierarchy-recovery.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_MODULAR_V1.md`
- Create: `docs/qa/OMENWARD_BATTLE_PRIMARY_HIERARCHY_RUNTIME_SMOKE_2026-09-02.md`

**Interfaces:**
- Consumes: fresh exact-head tests and a BATTLE technical capture when an Omenward Hera editor is available.
- Produces: a single V2 blueprint pointer and truthful evidence ceiling.

- [x] **Step 1: Replace stale side-minimap dimensions in the asset record**

Record `MarchMinimap = x16/y62/w926/h40`, `BattleFocus = x16/y110/w926/h304 during BATTLE`, and `LowerDeck = x16/y422/w928/h106 during BATTLE`. State that the normal non-BATTLE deck remains `928×164`.

- [x] **Step 2: Point current context/document map at the V2 blueprint without altering product decisions**

Use `current_blueprint = OMW-BLUEPRINT-20260902-BATTLE-PRIMARY-HIERARCHY-RECOVERY-V2`; leave the actual product owner as `OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01`.

- [x] **Step 3: Run full machine verification and record its exact result**

Run the project-local validator, every headless test, and the full Python suite. Do not write PASS until the fresh commands exit successfully.

- [x] **Step 4: Capture only if a live Omenward Hera editor is available**

Use the real BATTLE fixture and record its exact Git head, screenshot path, diagnostics, and caveats. If no Omenward editor is available, record `RUNTIME_TECHNICAL_SMOKE = NOT_RUN_IN_THIS_TURN` rather than opening or changing another project.

- [ ] **Step 5: Commit and push the coherent repair**

Run `git diff --check`, inspect `git status --short`, commit only scoped blueprint/UI/test/evidence files, push the current PR branch, then read back the exact PR head and its CI state. Do not merge, force-push, bypass protection, or alter unrelated PRs.

## Self-review

- Spec coverage: Task 1 makes every V2 geometry and read-only invariant testable; Task 2 changes only phase-local layout; Task 3 fixes the visual hierarchy without new art; Task 4 reconciles all current owners and evidence.
- Placeholder scan: no deferred implementation marker, generated asset, or unstated interface remains.
- Type consistency: `StringName` is used for the phase argument; both new presentation methods return the types asserted by Task 1.
