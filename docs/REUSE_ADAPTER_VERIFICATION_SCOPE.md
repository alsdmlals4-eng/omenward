# RM-SYS-003 verification scope

- Verify the already-vendored candidate draft engine and Omenward adapter.
- Add `vendor/base-reuse/**` to the existing core workflow triggers.
- Run Python repository regressions, Godot 4.7.1 import, all headless tests, and runtime smoke.
- Do not connect the adapter to RouletteService, economy, save, building, scene, or player-facing runtime paths.
- Close obsolete PR #197 only after current-main verification succeeds.
