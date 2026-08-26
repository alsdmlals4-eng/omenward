# P0 Building Button Thumbnail Consumer · Execution Packet

```yaml
issue: 223
scope: CURRENT_STAGE_HUD_BUILD_ACTIONS_ONLY
status: IMPLEMENTED__PARTIAL_RUNTIME_EVIDENCE
```

## Goal

Replace only the three existing Stage HUD build-action graybox buttons with compact, transparent thumbnails derived from their approved P0 cleanup masters. The player keeps the same construction choices and sees a small visual role cue beside each existing action name.

## Exact consumer mapping

| Approved master | Runtime derivative | Existing consumer |
|---|---|---|
| General Barracks T1 | `assets/art/buildings/general_barracks_t1_build_button.png` | `BarracksButton` |
| Defense Tower T1 | `assets/art/buildings/defense_tower_t1_build_button.png` | `TowerButton` |
| Farm T1 | `assets/art/buildings/farm_t1_build_button.png` | `FarmButton` |

The renderer exports nearest-neighbor `192×144` transparent PNG cells with binary alpha, a `160×120` content bound, and a shared bottom baseline. `StageHud` constrains each button icon to `22` pixels wide so the current text remains legible.

## Scope boundary

- Preserved: button text, offsets, construction costs, construction service, disabled state, tooltip, and battlefield scene.
- Excluded: placing full-size buildings in the three simultaneous front views; new building rules; and consumers for Command Post, Mana Tower, Special Barracks, or Vault. Those approved masters remain source-only until a real consumer is approved.

## Verification

- RED/GREEN: `tests/headless/p0_building_button_thumbnail_test.gd` first failed with all thumbnail/binding assertions absent, then passed after export and scene binding.
- Regression: the current 18-test headless suite passed.
- Runtime: Godot imported all three PNGs. A live Stage HUD capture showed the compact images, and activating Barracks and Tower preserved their existing occupied/disabled behavior with clean Hera diagnostics and no automated clipping signal.

## Evidence ceiling

This is `PARTIAL` runtime/UI evidence only. It does not claim broad player readability, battlefield building placement, or human hands-on usability PASS.
