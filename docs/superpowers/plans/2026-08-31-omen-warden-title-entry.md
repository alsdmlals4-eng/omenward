# Omen Warden Title Entry Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a truthful, image-ready title entry that starts the existing tutorial only after the player chooses `원정 시작`.

**Architecture:** `GameSession` owns bootstrap readiness and the explicit `begin_tutorial()` action. `TitleScreen` is a UI adapter that exposes that action, keeps Run Command hidden until the real `stage_started` signal, and never owns a duplicate game run. Generated art stays under `docs/images/candidates/` until the user locks pixels; the first functional screen uses native Godot labels and theme surfaces.

**Tech Stack:** Godot 4.7.1, typed GDScript, SceneTree headless contracts, Python standard-library unittest validators, and image-model candidate generation.

**Spec:** `docs/superpowers/specs/2026-08-31-omen-warden-title-entry-design.md`

## Global Constraints

- `MAP_TOPOLOGY = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL` remains unchanged.
- `RUN_COMMAND_TABS = DOMESTIC / ROULETTE / FRONT` remains unchanged.
- Generated images cannot enter `assets/art/` until the user visually locks them.
- The only title gameplay action is `원정 시작`; no Continue, Save, Settings, Shop, or Record control is added.
- Automated passing is not human UX, rights, release, or player-readability evidence.

---

### Task 1: Establish the boot-to-tutorial behavior contract

**Files:**
- Create: `tests/headless/title_entry_contract_test.gd`
- Modify: `tests/headless/game_session_decoupling_test.gd`
- Modify: `scripts/application/game_session.gd`

**Interfaces:**
- Consumes: `GameSession._ready()` and `GameSession.start_stage(stage_id)`.
- Produces: `GameSession.is_bootstrap_ready() -> bool` and `GameSession.begin_tutorial() -> bool`.

- [ ] **Step 1: Write the failing test**

```gdscript
check(not driver.requested.has(&"tutorial_stage"), "boot does not schedule a stage before the title action")
check(session.is_bootstrap_ready(), "a successful bootstrap reports title-start readiness")
check(session.begin_tutorial(), "the title action can begin the tutorial after bootstrap")
check(application.starts == [&"tutorial_stage"], "the title action starts exactly the tutorial stage")
```

- [ ] **Step 2: Run the focused test to verify RED**

```powershell
& 'C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe' --headless --path . -s res://tests/headless/game_session_decoupling_test.gd
```

Expected: existing code schedules `tutorial_stage` automatically and lacks the title-entry API.

- [ ] **Step 3: Write minimal implementation**

```gdscript
var _bootstrap_succeeded := false

func is_bootstrap_ready() -> bool:
	return _bootstrap_succeeded

func begin_tutorial() -> bool:
	return _bootstrap_succeeded and start_stage(&"tutorial_stage")
```

Set `_bootstrap_succeeded` only after `application.bootstrap()` succeeds and remove automatic driver start.

- [ ] **Step 4: Run the focused test to verify GREEN**

Run the command from Step 2. Expected: exit `0` with `GameSession decoupling checks passed`.

### Task 2: Add the functional title screen

**Files:**
- Create: `scenes/ui/title_screen.tscn`
- Create: `scripts/ui/title_screen.gd`
- Modify: `scenes/main/main.tscn`
- Test: `tests/headless/title_entry_contract_test.gd`

**Interfaces:**
- Consumes: `GameSession.is_bootstrap_ready()`, `GameSession.begin_tutorial()`, and existing bootstrap/stage signals.
- Produces: `TitleScreen` with a disabled-until-ready start button and a post-stage-start Run Command reveal.

- [ ] **Step 1: Extend the failing scene test**

```gdscript
_expect(title_screen.get_node_or_null("Panel/StartExpeditionButton") is Button, "title exposes one actual expedition action", failures)
_expect(run_command_screen != null and not run_command_screen.visible, "Run Command is hidden before the title action", failures)
_expect(not scene_text.contains("계속하기"), "title does not claim a save continuation that the product has not implemented", failures)
```

- [ ] **Step 2: Run the focused test to verify RED**

```powershell
& 'C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe' --headless --path . -s res://tests/headless/title_entry_contract_test.gd
```

Expected: title scene and primary action are absent, and Run Command is visible at boot.

- [ ] **Step 3: Write minimal implementation**

Create a 960×540 `TitleScreen` with Godot Labels for `OMENWARD`, `징조를 읽고, 전선을 지휘하라`, status text, and one Button text `원정 시작`. Resolve `../../GameSession`, subscribe to readiness/failure/stage-start signals, and read the current readiness in `_ready()` to handle signal ordering. On real stage start, hide TitleScreen and reveal sibling RunCommandScreen.

- [ ] **Step 4: Run focused title tests to verify GREEN**

```powershell
& 'C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe' --headless --path . -s res://tests/headless/game_session_decoupling_test.gd
& 'C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe' --headless --path . -s res://tests/headless/title_entry_contract_test.gd
```

Expected: both exit `0`.

### Task 3: Generate reviewable title-art candidates

**Files:**
- Create: `docs/images/candidates/OMENWARD_TITLE_ENTRY_CANDIDATES_2026-08-31.md`
- Create: `docs/images/candidates/title/omenward_title_citadel_dawn_candidate_v1.png`
- Create: `docs/images/candidates/title/omenward_title_ward_seal_candidate_v1.png`

**Interfaces:**
- Consumes: the title visual brief and faction language.
- Produces: `GENERATED_CANDIDATE` records with prompt, dimensions, SHA-256, no runtime consumer, and an explicit `LOCK / REVISE / REJECT` gate.

- [ ] **Step 1: Produce and inspect two non-runtime candidates**

Generate one clean 16:9 background and one text-free square Ward seal. Inspect both before copying them to the candidate directory.

- [ ] **Step 2: Record provenance and gate**

Write exact filenames, SHA-256, prompt, dimensions, intended future consumer, no-runtime-binding state, and `USER_VISUAL_LOCK_REQUIRED`.

- [ ] **Step 3: Show the user a candidate-only composition**

Do not bind a candidate to the runtime `TitleScreen` or create an approved asset manifest until the user explicitly answers `LOCK`.

### Task 4: Promote only a locked candidate and complete machine verification

**Files:**
- Create: `assets/art/ui/title/<locked-image>.png`
- Create: `docs/images/approved/OMENWARD_TITLE_ENTRY_ASSET_V1.md`
- Modify: `scenes/ui/title_screen.tscn`
- Modify: current decision/context/implementation/coverage owners
- Test: `tests/headless/title_entry_contract_test.gd`

**Interfaces:**
- Consumes: explicit user `LOCK`, candidate SHA-256, and prompt provenance.
- Produces: the registered image asset bound only to `TitleScreen` plus updated machine evidence.

- [ ] **Step 1: Receive a visual lock**

The user must see the candidate in composition and answer `LOCK` or give a specific revision. Design approval alone does not promote unseen pixels.

- [ ] **Step 2: Add a failing asset-binding test**

```gdscript
_expect(FileAccess.file_exists(LOCKED_BACKGROUND_PATH), "the locked title backdrop exists in the runtime asset path", failures)
_expect(title_scene_text.contains(LOCKED_BACKGROUND_PATH.get_file()), "TitleScreen is the runtime consumer of the locked backdrop", failures)
```

- [ ] **Step 3: Promote and bind the locked asset**

Copy only the locked image to `assets/art/ui/title/`, bind it to `TitleScreen/Backdrop`, and record SHA-256, prompt, candidate source, consumer, approval, and implementation state.

- [ ] **Step 4: Run all machine checks and a technical runtime capture**

```powershell
& 'C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe' --headless --editor --path . --quit
Get-ChildItem tests/headless/*_test.gd | ForEach-Object { & 'C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe' --headless --path . -s ("res://" + $_.FullName.Substring((Get-Location).Path.Length + 1).Replace('\','/')); if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }
& 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest discover -s tests/python -v
& 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools/validate_project_core_docs.py
git diff --check
```

Run a live title-state and post-click Run Command technical smoke. Leave human UX explicitly `NOT_RUN`.

## Plan self-review

- **Spec coverage:** Tasks 1–2 implement the truthful route and failure state; Task 3 covers both required candidates and the visual gate; Task 4 covers promotion, provenance, machine checks, and technical capture.
- **Placeholder scan:** No product behavior depends on an unknown feature; a runtime filename is intentionally selected only after a visual lock.
- **Type consistency:** `GameSession.is_bootstrap_ready() -> bool` and `GameSession.begin_tutorial() -> bool` are the only new cross-component runtime APIs.
