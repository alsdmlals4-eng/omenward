# Phase 0 Validation

## Automated checks

Run from the repository root with the Godot 4.7.1 Standard console executable:

```powershell
Godot_v4.7.1-stable_win64_console.exe --headless --path . -s res://tests/headless/phase_0_contract_test.gd
Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64_console.exe --headless --path . --quit-after 1
```

The contract test verifies the ten shared archetypes, two Visual Profiles per archetype, AnimationContract presence, deterministic StageManifest generation, and the absence of enemy-specific combat profiles.

## Manual visual QA

1. Run `scenes/main/main.tscn` at 1920×1080 and confirm the status panel and three lane probe are fully visible.
2. Run at 1280×720 and confirm viewport/keep/integer scaling leaves intentional letterboxing rather than non-integer pixel scaling.
3. Confirm the probe only communicates Phase 0 data readiness; it must not simulate combat, roulette, capture, gates, waves, or enemy-specific units.

## Goal 0002 handoff

Goal 0002 receives `DataRegistry`, `StageManifest`, `BattlefieldProfile`, `FactionVisualProfile`, `AnimationContract`, `CombatClock`, and the headless contract command as its bootstrap boundary. It adds actual battle behavior only after its own approved Plan Mode proposal.
