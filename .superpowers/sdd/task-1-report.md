# Task 1 Report: Deterministic Stage and Wave Data Contracts

## Scope and Outcome

Implemented Task 1 only in the OMENWARD vertical-slice worktree. The change adds declarative tutorial and regular-stage Resources, deterministic wave/spawn serialization, and registry/validation support without adding combat behavior, enemy-specific data, scenes, AutoLoads, lane traversal, or a minimap.

## Changed Files

- Created `scripts/data/stage_definition.gd` to define static stage data and build a resolved `StageManifest` from a seed.
- Created `scripts/data/wave_definition.gd` and `scripts/data/unit_spawn_definition.gd` to serialize declarative waves and shared-archetype enemy spawns.
- Created `scripts/data/building_definition.gd` as the Task 1 building Resource contract; it intentionally contains no Task 3 construction behavior.
- Extended `scripts/core/stage_manifest.gd` JSON with stage economy, tutorial flag, wave count, resolved waves, and the existing input log.
- Extended `scripts/data/bootstrap_catalog.gd`, `data/bootstrap_catalog.tres`, and `scripts/core/data_registry.gd` to register the two stage Resources.
- Extended `scripts/core/bootstrap_validator.gd` to require a four-wave tutorial and twenty-wave regular stage.
- Created `data/stages/tutorial_stage.tres` and `data/stages/regular_stage.tres`. Their enemy spawns use only `shield_guard`, `archer`, `assassin`, `priest`, and `giant`, with `owner_team_id = &"veil"` and `visual_faction_id = &"veil"`. W5 is elite, W10 hero, W15 is a legendary giant boss, W16-W19 are overtime, and W20 is a mythic giant boss.
- Created `tests/headless/stage_data_contract_test.gd`.
- Godot generated `.uid` files for the new scripts and test.

## TDD Record

1. Wrote `tests/headless/stage_data_contract_test.gd` before production code.
2. The requested Godot 4.7.1 executable was not installed or on PATH. A filesystem search found only Godot 4.7.
3. Ran the red test with the installed Godot 4.7 console build. It failed as expected because both stage Resources were absent:
   - `Cannot open file 'res://data/stages/tutorial_stage.tres'`
   - `Cannot open file 'res://data/stages/regular_stage.tres'`
   - `Cannot open file 'res://data/stages/regular_stage.tres'`
4. Added the minimal static Resources, manifest serialization, catalog loading, and validation needed for the test.
5. Ran the focused stage-data contract test again and it passed.

## Verification

All executed Godot checks used the installed `C:\Users\user\Downloads\Godot_v4.7-stable_win64.exe\Godot_v4.7-stable_win64_console.exe` binary.

| Check | Result |
|---|---|
| Focused `stage_data_contract_test.gd` after implementation | Passed: `Stage data contract checks passed` |
| `phase_0_contract_test.gd` | Passed: `Phase 0 contract checks passed` |
| `--headless --path . --editor --quit` | Passed; generated global class index and task-owned `.uid` files |
| `git diff --check` | Passed; exit code 0 (only existing line-ending conversion notices) |

The first Phase 0 run failed before the editor import because this fresh worktree had no `.godot/global_script_class_cache.cfg`; the existing Phase 0 test relies on the global `StageManifest` class index. The required editor import generated that index, and the rerun passed without source changes for that issue.

## Unverified Item and Remaining Risk

- Godot 4.7.1 validation is unverified because no 4.7.1 executable is available in the accessible filesystem. The implementation was verified with Godot 4.7 only.
- The existing baseline test needs an editor scan in a fresh worktree before it can resolve existing global GDScript classes. This is an environment/import prerequisite, not a new gameplay dependency.

## User Recheck

After installing or exposing `Godot_v4.7.1-stable_win64_console.exe`, run from the worktree root:

```powershell
Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/stage_data_contract_test.gd
Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/phase_0_contract_test.gd
Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
git diff --check
```

## Base Promotion

Base promotion candidate 없음.
