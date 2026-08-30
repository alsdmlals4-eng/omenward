# Single-Front Close Battlefield Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the legacy cropped backdrop and vertical-tab battle layout with a new close single-front terrain and battle-first Godot screen.

**Architecture:** `BattleFocusView` remains the only renderer of live combat units and the fixed tower, but it stops sampling the legacy three-front image and instead uses a user-locked original terrain plate. `RunCommandScreen` moves its three tabs into the top rail, freeing the full left battle area; `MarchMinimap` remains a read-only projection of the same `StageRun` route state.

**Tech Stack:** Godot 4.7 GDScript, `.tscn` Control scene layout, built-in ImageGen for candidate raster art, deterministic SceneTree headless tests, existing project documentation and asset provenance records.

**Spec:** `docs/superpowers/specs/2026-08-30-single-front-close-battlefield-redesign.md`

## Global Constraints

- `BATTLEFIELD_PRESENTATION = BATTLE_PRIMARY_CLOSE_COMBAT_VIEW__MARCH_MINIMAP_CONTEXT`.
- `BUILDING_MAP_PLACEMENT = FORBIDDEN` and `FIXED_TOWER_COUNT_PER_ACTIVE_FRONT = 1`.
- The final terrain asset is bound only after `GENERATED_CANDIDATE -> USER_APPROVED -> CANON_REGISTERED`.
- No river, bridge, path gap, parallel lane, baked unit, baked tower, baked building, construction node, wall, or barricade.
- Lumern and Veil Shield Guard pair V1 remain the runtime unit texture pair.
- The minimap is a read-only five-sector route context, not a second battle surface.

---

### Task 1: Produce and review the two visual candidates

**Files:**
- Create: `docs/images/candidates/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_TERRAIN_2026-08-30.md`
- Create: `docs/images/candidates/OMENWARD_CLOSE_SINGLE_FRONT_BATTLE_UI_REFERENCE_2026-08-30.md`
- Inspect: `assets/art/units/lumern_shield_guard_storybook_idle_v1.png`
- Inspect: `assets/art/units/veil_shield_guard_storybook_idle_v1.png`

**Interfaces:**
- Produces: exactly one terrain candidate source path/SHA/dimensions and one UI-reference candidate source path/SHA/dimensions.
- Does not produce: a runtime asset path, texture preload, scene binding, or altered game state.

- [ ] **Step 1: Generate the terrain-only candidate**

Use built-in ImageGen with the terrain requirements from the spec and no image
text. Confirm that the visual center is a broad continuous battle field.

- [ ] **Step 2: Inspect against the map exclusions**

Reject the candidate if a river, bridge, road barrier, hard gap, baked combatant,
tower, building, UI, node, label, logo, or watermark appears.

- [ ] **Step 3: Generate the whole-screen UI reference candidate**

Use the terrain candidate and the two existing shield-guard files only as style
references. Require a wide left battle frame, narrow five-sector minimap,
top command rail, and compact lower deck, but no readable generated text.

- [ ] **Step 4: Record both as candidates and request exact user lock**

Record generator, source path, SHA-256, dimensions, non-runtime status,
reference inputs, intended consumer, exclusions, and approval boundary. Show
both images to the user; do not copy either into `assets/` before lock.

### Task 2: Bind the user-locked terrain with a RED-to-GREEN contract

**Files:**
- Create: `assets/art/battlefield/omenward_close_single_front_battlefield_v1.png`
- Create: `tests/headless/close_battlefield_redesign_contract_test.gd`
- Modify: `scripts/ui/battle_focus_view.gd`
- Modify: `docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_V1.md`

**Interfaces:**
- Consumes: the exact terrain candidate selected by the user and its recorded SHA-256.
- Produces: `BattleFocusView::BATTLEFIELD_TERRAIN` preloading the approved
  project-local PNG and no `ward_veil_three_lane_backdrop_v1.png` preload.

- [ ] **Step 1: Write the failing texture-contract test**

```gdscript
var source := FileAccess.get_file_as_string("res://scripts/ui/battle_focus_view.gd")
assert(not source.contains("ward_veil_three_lane_backdrop_v1.png"))
assert(source.contains("omenward_close_single_front_battlefield_v1.png"))
assert(FileAccess.file_exists("res://assets/art/battlefield/omenward_close_single_front_battlefield_v1.png"))
```

- [ ] **Step 2: Run the test and verify the expected RED failure**

Run: `Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/close_battlefield_redesign_contract_test.gd`

Expected: failure because the legacy preload exists and the approved terrain path
does not yet exist.

- [ ] **Step 3: Register and bind only the locked terrain**

Copy the exact locked file non-destructively to the new project-local path,
write provenance/approval metadata, replace the preload constant, and draw the
full terrain plate within the combat rectangle without a three-front crop.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run the same command. Expected: exit 0 with the new asset path and no legacy
backdrop reference.

- [ ] **Step 5: Commit the asset binding**

```powershell
git add assets/art/battlefield/omenward_close_single_front_battlefield_v1.png scripts/ui/battle_focus_view.gd tests/headless/close_battlefield_redesign_contract_test.gd docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_V1.md
git commit -m "feat: bind close single-front battlefield"
```

### Task 3: Replace the battle surface composition with a RED-to-GREEN scene contract

**Files:**
- Modify: `scenes/ui/run_command_screen.tscn`
- Modify: `scripts/ui/run_command_screen.gd`
- Modify: `scripts/ui/battle_focus_view.gd`
- Modify: `tests/headless/close_battlefield_redesign_contract_test.gd`
- Inspect: `scripts/ui/march_minimap_view.gd`

**Interfaces:**
- Consumes: the existing `BattleFocusViewport`, `MarchMinimap`, three tab button
  handlers, and `StageRun.battle.route_state_for(&"front")`.
- Produces: a `BattleFocusViewport` at least 686 logical pixels wide and a
  top-rail tab selector with the same three existing handlers.

- [ ] **Step 1: Extend the failing scene-layout test**

```gdscript
assert(scene_text.contains('offset_left = 16.0\noffset_top = 62.0\noffset_right = 702.0'))
assert(scene_text.contains('[node name="TopTabRail" type="HBoxContainer" parent="TopBar"]'))
assert(not scene_text.contains('[node name="TabRail" type="VBoxContainer" parent="."]'))
assert(scene_text.contains('[node name="MarchMinimap" type="Control" parent="."]'))
```

- [ ] **Step 2: Run the test and verify RED**

Run the focused test command from Task 2. Expected: failure because the scene
still has the vertical `TabRail` and a 576-pixel battle viewport.

- [ ] **Step 3: Implement the minimal new composition**

Move the three current tab buttons into `TopBar/TopTabRail`, update their
node-path lookups in `run_command_screen.gd`, set the battle focus bounds to
`x16 y62 w686 h292`, retain the minimap at `x712 y62 w230 h292`, and retain
the lower deck at `x16 y364 w928 h164`.

- [ ] **Step 4: Keep live combat rendering readable**

Render the current approved unit pair in a two-to-three-row cluster, preserve
the one dynamic tower, avoid buildings, and retain current health/faction
feedback. Do not add gameplay state or write through the minimap.

- [ ] **Step 5: Run the focused test and verify GREEN**

Run the focused test command. Expected: exit 0 with one wide battle focus,
top tabs, a right minimap, and no vertical tab rail.

- [ ] **Step 6: Commit the scene composition**

```powershell
git add scenes/ui/run_command_screen.tscn scripts/ui/run_command_screen.gd scripts/ui/battle_focus_view.gd tests/headless/close_battlefield_redesign_contract_test.gd
git commit -m "feat: redesign close battle screen"
```

### Task 4: Verify the renderer, document evidence, and preserve the rollback

**Files:**
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/PROJECT_CORE.md`
- Create: `docs/qa/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_RUNTIME_SMOKE_2026-08-30.md`
- Inspect: `tests/headless/battle_primary_march_minimap_contract_test.gd`
- Inspect: `tests/headless/run_command_tab_contract_test.gd`

**Interfaces:**
- Consumes: Task 2's locked asset and Task 3's scene contract.
- Produces: machine/runtime/human evidence statuses that distinguish technical
  smoke from human readability, plus a documented non-destructive rollback.

- [ ] **Step 1: Run focused regressions**

```powershell
& $godot --headless --path . -s res://tests/headless/close_battlefield_redesign_contract_test.gd
& $godot --headless --path . -s res://tests/headless/battle_primary_march_minimap_contract_test.gd
& $godot --headless --path . -s res://tests/headless/run_command_tab_contract_test.gd
& $godot --headless --path . -s res://tests/headless/scene_contract_test.gd
```

- [ ] **Step 2: Run editor import and every headless test**

```powershell
& $godot --headless --path . --editor --quit
Get-ChildItem tests/headless -Filter '*_test.gd' | Sort-Object Name | ForEach-Object { & $godot --headless --path . -s ("res://tests/headless/" + $_.Name); if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }
```

- [ ] **Step 3: Capture runtime technical evidence at two reference sizes**

Run the BATTLE phase at 1920x1080 and 1280x720. Capture only technical facts:
new terrain loaded, one tower, unit silhouettes inside the battle frame,
minimap visible, no building objects. Do not label this as human readability
or player-experience PASS.

- [ ] **Step 4: Update canonical status and rollback notes**

Record exact asset hash, runtime consumer, test results, capture paths,
`HUMAN_READABILITY = NOT_RUN`, and rollback as restoring the legacy preload
without deleting its texture or either terrain candidate.

- [ ] **Step 5: Commit verification metadata**

```powershell
git add docs/ACTIVE_CONTEXT.md docs/OMENWARD_GDD_CURRENT_CANON.md docs/PROJECT_CORE.md docs/qa/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_RUNTIME_SMOKE_2026-08-30.md
git commit -m "docs: record close battlefield verification"
```
