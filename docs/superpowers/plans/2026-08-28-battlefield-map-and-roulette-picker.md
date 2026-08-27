# Battlefield Map And Roulette Picker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to execute this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the vertical slice graybox with a composed three-lane battlefield and make the roulette inspectable through selectable tiles and a result list.

**Architecture:** A single project-owned background image provides environment context behind the existing dynamic `BattlefieldView` unit renderer. `RunCommandScreen` gains presentational selection state only; `StageRun` remains the authority for roulette and combat state.

**Tech Stack:** Godot 4.7, GDScript, PNG raster asset, Hera live QA, headless GDScript tests.

**Spec:** `docs/superpowers/specs/2026-08-28-battlefield-map-and-roulette-picker-design.md`

## Global Constraints

- Existing 3×3 roulette, rewards, deployment and combat rules remain unchanged.
- New GDScript files require a Korean role header; no new script is planned.
- Backdrop is opaque, contains no copy/UI, and leaves live lane combat readable.
- Generated project asset is retained locally and recorded in Notion.

---

### Task 1: Produce and register the battlefield backdrop

**Files:**
- Create: `assets/art/battlefield/ward_veil_three_lane_backdrop_v1.png`
- Create: `docs/images/approved/OMENWARD_BATTLEFIELD_BACKDROP_V1.md`

- [ ] Generate one original 16:9 background using the supplied reference only for composition and Omenward's existing approved visual language.
- [ ] Inspect that it has no text, UI, watermark, copied character, or blocked lane centres.
- [ ] Store the final PNG in the project and add checksum, dimensions, prompt, consumer and dual-storage record.
- [ ] Add the approved record to Notion and read it back.

### Task 2: Bind the backdrop without changing combat semantics

**Files:**
- Modify: `scenes/battle/battlefield.tscn`
- Modify: `scripts/battle/battlefield_view.gd`
- Test: `tests/headless/scene_contract_test.gd`

- [ ] Add a failing contract assertion that the battlefield scene loads the project backdrop.
- [ ] Bind the background behind the existing `BattlefieldView` and replace only the graybox drawing with readable low-intensity lane/clash overlays.
- [ ] Run the focused headless test and Godot import/parse check.

### Task 3: Add roulette selection and result list

**Files:**
- Modify: `scenes/ui/run_command_screen.tscn`
- Modify: `scripts/ui/run_command_screen.gd`
- Test: `tests/headless/roulette_picker_ui_test.gd`

- [ ] Add a failing test for a UI-only selected-board-item state that cannot mutate `StageRun` roulette data.
- [ ] Replace passive texture tiles with buttons, add an inspectable result list and detail readout, and update selection only from UI callbacks.
- [ ] Run focused headless and integration tests.

### Task 4: Capture and review the vertical slice

**Files:**
- Create: `docs/qa/OMENWARD_BATTLEFIELD_MAP_AND_ROULETTE_PICKER_QA_2026-08-28.md`
- Modify: `docs/ACTIVE_CONTEXT.md`

- [ ] Run the existing main scene with Hera at 960×540; capture PREPARE, roulette inspection and BATTLE.
- [ ] Check control bounds, diagnostics and unit readability over the backdrop.
- [ ] Record technical evidence only; retain human/player experience as `NOT_RUN`.
- [ ] Run adversarial review for background-as-state, lane occlusion, selection side-effects and asset provenance.
