# Omenward Battlefield Map + Roulette Picker Design

```yaml
decision_id: OMW-VISUAL-20260828-BATTLEFIELD-MAP-ROULETTE-PICKER-01
issue: 229
status: PARTIALLY_SUPERSEDED__ROULETTE_INSPECTION_RETAINED
approval_source: 2026-08-28 user instruction plus continuous approval
scope: RUN_COMMAND_VERTICAL_SLICE_PRESENTATION_ONLY
```

## Current boundary

`OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01`이 close-battlefield backdrop 표현을 supersede한다. 현재 지도 topology는 단일 Ward 본진에서 세 branch가 갈라지는 구조이며, 이 문서의 3×3 tile/list inspection behavior와 관련 QA는 retained historical implementation evidence다.

## Goal

The battlefield must read as a wide, close conflict immediately in front of the Ward outposts: three simultaneous lanes, forward bases, central clashes and bypass routes must be visible without requiring the main citadel to appear. The roulette must feel like a friendly choice workbench: a player can inspect a board result and select a tile to see its unit/reward meaning before using the existing row/column moves and confirm path.

## Visual direction

- Use the supplied references only as composition and tone guidance: broad foreground battlefield, storybook watercolor SD rendering, three horizontal main routes, clear central clash spaces and recognisable terrain.
- Retain Omenward faction language: navy/ivory/cool-gray/gold allies; black-purple/dark-red/carapace-gray Veil; restrained glow; existing approved unit sprites remain the live combat actors.
- The background is deliberately enlarged above distant-map scale. Front-state information must remain translucent so terrain, forward bases, clashes and bypass routes remain the primary visual mass.
- This supersedes only the current `BattlefieldView` graybox presentation and the plain roulette inspection surface. It does not change combat, probability, rewards, commitment, animation timing or the 3×3 rule set.

## Implementation contract

### Battlefield

- Generate one original 16:9 storybook-watercolor SD battlefield backdrop with opaque background, no text/UI/labels and protected open lane centres for actual `UnitView` sprites.
- Add it as a `Sprite2D` behind `BattlefieldView`.
- Keep the three actual lane Y positions and dynamic unit placement. Replace graybox road/gate rectangles with restrained runtime overlays only: lane progress, central clash emphasis and bypass warning.
- The background is decorative/contextual; it must not encode combat positions or become a second source of gameplay state.

### Roulette picker

- Keep the existing 3×3 board, row/column buttons, move budget, preview, lock and confirm callbacks unchanged.
- Make every board tile selectable. Selection opens a local detail/readout panel containing the selected reward identity, a compact friendly description and its current board position.
- Add a visible selectable result list beside the board. Selecting either the list or tile updates the same readout. The list is an inspection aid, not a new reward choice or probability control.
- Use clear Korean copy and existing token/unit textures. No character mascot, copied illustration, or random reward selection is added.

## Acceptance criteria

1. Godot imports the new enlarged backdrop and shows three forward bases, three central clash zones and bypass routes behind active unit sprites at 960×540.
2. Existing Run Command state progression and `begin_battle()` behavior remain unchanged.
3. In stopped/manipulate/result-confirm roulette states, a tile and a list entry can be selected and the matching detail readout changes.
4. Selection cannot alter board order, moves, rewards, deployment or combat state.
5. No new runtime error/warning appears in a Hera capture; relevant headless tests pass.
6. The generated backdrop is stored in the project and recorded in Notion before it is promoted as a runtime input.

## Exclusions

- Full long-road strategic map rules, title screen, save/settings UI, animation atlases, VFX packs, new gameplay art families, balance, and human player-experience PASS.
