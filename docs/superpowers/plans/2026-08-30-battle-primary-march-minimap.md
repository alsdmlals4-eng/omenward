# Battle-Primary March-Minimap Implementation Plan

**Goal:** Make a live close combat view the primary `BATTLE` surface and reduce the single five-sector march route to a read-only minimap.

**Architecture:** Two presentational controls read one `StageRun`. `BattleFocusView` renders the current front formation, combat focus, tower state, and unit count. `MarchMinimapView` renders only route context. Neither control mutates battle, route, economy, roulette, building, or deployment state.

**Decision:** `docs/design/APPROVED_OMENWARD_BATTLE_PRIMARY_MARCH_MINIMAP_2026-08-30.md`

## Tasks

- [ ] Add the RED `battle_primary_march_minimap_contract_test.gd` and verify the old wide-map scene fails it.
- [ ] Add `BattleFocusView` with a close battlefield frame, state-derived Ward/Veil formations, current-sector treatment, and the sole tower; bind it only to live run state.
- [ ] Convert the old strategic projection into compact `MarchMinimapView`; retain its five-sector route and tower projection but remove large unit markers and terrain-road presentation.
- [ ] Replace `StrategicMap` in `RunCommandScreen` with `BattleFocusViewport` plus `MarchMinimap`, and show the pair during `BATTLE` on the front tab.
- [ ] Update focused scene/UI contracts, verify no wide primary map remains, and preserve the three-tab/one-front/roster contracts.
- [ ] Run headless Godot checks, parser/import validation, the operating-contract validator, then a live technical smoke. Record `RUNTIME_TECHNICAL_SMOKE` separately from human UX.

## Verification Commands

```powershell
& $godot --headless --path . -s tests/headless/battle_primary_march_minimap_contract_test.gd
& $godot --headless --path . -s tests/headless/strategic_map_ui_contract_test.gd
& $godot --headless --path . -s tests/headless/scene_contract_test.gd
& $godot --headless --editor --quit --path .
```
