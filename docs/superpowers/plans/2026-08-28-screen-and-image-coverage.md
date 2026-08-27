# Screen And Image Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Maintain complete image coverage for every implemented Omenward player-facing surface without generating duplicate or consumerless assets.

**Architecture:** The screen inventory is the routing owner. Each runtime row names the exact Godot consumer and uses raster only when a theme, procedural draw, shader, or existing shared asset cannot communicate its state. Planning and release images remain distinct families with their own evidence.

**Tech Stack:** Godot 4.7, GDScript, PNG, `StyleBoxFlat`, procedural canvas drawing, Hera technical capture, Notion Visual Bible.

**Spec:** `docs/design/OMENWARD_GAME_SCREEN_AND_IMAGE_COVERAGE_2026-08-28.md`

**GitHub Issue:** `#231`

## Global Constraints

- `RUNTIME_IMAGE`, `PRODUCTION_VISUAL`, and `RELEASE_IMAGE` are not interchangeable.
- Preserve `PREPARE -> COMMIT -> BATTLE -> REVIEW`; do not change probability, rewards, or combat rules during visual coverage work.
- Every generated runtime PNG must be stored locally and attached/recorded in Notion before promotion.
- Human/player readability remains `NOT_RUN` until actual player evidence exists.

### Task 1: Verify the current raster and procedural consumer matrix

**Files:**
- Read: `scenes/main/main.tscn`, `scenes/battle/battlefield.tscn`, `scenes/ui/run_command_screen.tscn`, `scripts/units/unit_view.gd`
- Read: `docs/design/OMENWARD_GAME_SCREEN_AND_IMAGE_COVERAGE_2026-08-28.md`
- Test: `tests/headless/scene_contract_test.gd`, `tests/headless/roulette_picker_ui_test.gd`

- [ ] Run the existing scene and roulette contracts.
- [ ] Run main through Hera at 960×540 and capture PREPARE, stopped 3×3, COMMIT, BATTLE, and REVIEW when those states are reachable.
- [ ] Record only an observed missing visual expression as a new asset request; do not replace an adequate Godot theme/procedural expression with a duplicate PNG.

### Task 2: Produce a consumer-bound gap only when evidence identifies one

**Files:**
- Modify: the exact consuming `.tscn`/`.gd` file identified by Task 1
- Create: `assets/art/<family>/<asset>.png` only if raster is the selected expression
- Create: `docs/images/approved/<asset>.md`
- Test: a focused headless contract under `tests/headless/`

- [ ] Write a failing test that names the exact node/resource/method consuming the new asset.
- [ ] Generate or derive exactly the missing raster, save it locally, record dimensions/hash/provenance, and attach it to Notion.
- [ ] Bind it behind existing gameplay authority; do not encode combat/probability state into art.
- [ ] Run the focused test, Godot import check, and Hera screenshot at the target resolution.

### Task 3: Open future surfaces only with a product consumer contract

**Files:**
- Modify: `docs/design/OMENWARD_GAME_SCREEN_AND_IMAGE_COVERAGE_2026-08-28.md`
- Modify: the new screen scene and route only after approval/consumer definition

- [ ] For title, save/load, pause/settings, event, archive, result/reward, or release assets, add a screen row with `screen_id`, player question, entry/exit, runtime consumer, state list, expression method, and destination before generating visual files.
- [ ] Fresh-read the platform release authority before generating any capsule, icon, logo, or marketing screenshot.
