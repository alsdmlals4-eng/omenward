# OMENWARD · Natural Tutorial Battle-to-Review QA

```yaml
issue: 233
date: 2026-08-28
scope: EXISTING_TUTORIAL_NO_UNIT_NATURAL_DEFEAT_PATH
method: GODOT_4_7_1_HEADLESS_DETERMINISTIC_SIMULATION
result: PASS
```

## What was proved

`tests/headless/natural_tutorial_resolution_test.gd` starts the existing four-wave tutorial without deployed rewards, then advances the existing `StageRun` and `BattleSimulator` rules until they resolve naturally.

- All four declared waves emit.
- The no-unit path reaches the existing Lumern-base destruction defeat result.
- `StageRun.command_phase` changes from `BATTLE` to `REVIEW` through `_finish_defeat()`, not through `submit_command()` or a scripted tutorial result.

## Boundaries

- This is a deterministic machine regression result, not a live visual REVIEW-frame capture.
- The live Hera run independently captured BATTLE wave 4 with runtime diagnostics at zero errors and zero warnings.
- Human usability, play feel, battle readability over a full session, and a player-controlled successful tutorial completion remain `NOT_RUN`.
- No balance values, stage victory rule, or asset consumer were changed.
