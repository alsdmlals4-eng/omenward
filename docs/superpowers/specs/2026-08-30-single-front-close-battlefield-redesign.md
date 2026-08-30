# Single-Front Close Battlefield Redesign

```yaml
decision_status: USER_DIRECTED__DESIGN_APPROVED_FOR_CANDIDATE_PRODUCTION
approval_source: "user: 맵이랑 전투화면 새로 만들어야지 -> 진행해"
scope: BATTLE_PHASE__ONE_ACTIVE_MARCH_FRONT
work_mode: PLAN_THEN_ASSET_CANDIDATE
runtime_asset_status: NOT_CREATED
runtime_binding: FORBIDDEN_UNTIL_EXACT_CANDIDATE_LOCK
```

## Goal

Replace the current close-battle presentation that crops the legacy
three-front backdrop with a genuinely new single-front combat map and a new
battle-first screen composition. The player must read soldiers and the current
clash before route progress, while the five-sector march remains context only.

## Retained product rules

- One active march front; no three-front return and no parallel lanes.
- The route grammar stays `WARD_CITADEL -> WARD_FORWARD -> CLASH ->
  VEIL_FORWARD -> VEIL_CITADEL`.
- Buildings, pads, construction nodes, walls, fences, and barricades do not
  appear in the battlefield. Building installation and upgrades remain in the
  Domestic roster.
- A single dynamic fixed defense tower may appear on the active front. Its
  ownership remains driven by the existing `StageRun` route state.
- The existing approved Lumern and Veil Shield Guard pair remains the runtime
  unit identity. This redesign does not redraw or replace those units.
- The right-side march minimap is read-only, uses five sectors, and never
  becomes a second battlefield or repeats individual unit art.

## New battlefield map contract

The battlefield is a three-layer composition rather than a single baked
illustration.

1. `Foundation`: an original terrain-only 16:9 watercolor plate with broad,
   gently irregular, continuously traversable neutral grass and earth. It has
   distant atmosphere and restrained ground texture, but no foreground rock,
   shrub, crystal, character, tower, building, UI, words, pads, flags, or
   route nodes.
2. `TerritoryProps`: independently placed transparent PNG terrain objects.
   Lumern props are pale broken slab clusters, blue meadow banks, and
   ivory/blue flower banks. Veil props are charcoal rubble, low violet crystal
   clusters, and dark thorny brush. Each object can be moved, omitted, reused,
   and layered without editing the foundation image.
3. `BattleOverlay`: existing live unit sprites, their health/faction feedback,
   the one live fixed tower, and small runtime effects.

The `Foundation` stays visibly and physically continuous from left to right.
Lumern territory props are placed only when `x_ratio < 0.36`; Veil territory
props are placed only when `x_ratio > 0.64`. The transition bands
`0.36..0.46` and `0.54..0.64` reduce their respective prop density; the
central `0.46..0.54` remains a clear, neutral clash ground. This makes the
territory change feel gradual without drawing a road, river, bridge, cliff,
moat, hard border, or gap. The center remains open enough for two-to-three
readable unit rows.

The previously generated single combined terrain candidate remains preserved
as a historical candidate and is excluded from runtime binding because its
foreground terrain is baked into the image.

## New battle screen contract

At the 960x540 logical reference size:

| Surface | Bounds | Player question |
|---|---:|---|
| Top command rail | x16 y12 w928 h40 | What phase am I in and what resources remain? |
| Compact three-tab selector | inside the command rail | Which work surface am I viewing: Domestic, Roulette, or Front? |
| Battle focus | x16 y62 w686 h292 | Who is clashing here, where is the pressure, and who owns the tower? |
| March minimap | x712 y62 w230 h292 | Which of the five route sectors is currently contested or held? |
| Focus-adaptive lower deck | x16 y364 w928 h164 | What is the one currently available command or explanation? |

`BattleFocusViewport` occupies the left field without an overlaid vertical tab
rail. Units use the current approved transparent SD art in a clear two-to-three
row formation: Lumern approaches from the left, Veil from the right, and the
active clash is visibly centered. The dynamic tower is the only static combat
object. Health bars and faction halos remain compact and never cover the unit
silhouette.

## Candidate and approval boundary

Eight non-runtime candidates are required before any binding:

1. one neutral terrain `Foundation` plate;
2. three individual Lumern `TerritoryProps` with actual transparency;
3. three individual Veil `TerritoryProps` with actual transparency;
4. a no-copy UI composition reference showing the composited terrain, the
   approved unit language, the wide battle view, the narrow minimap, and the
   compact lower deck together.

All eight candidates are `GENERATED_CANDIDATE` only. The user must lock the
exact foundation and six selected terrain props before any are copied under
`assets/`, referenced by Godot, or registered as canonical. The UI reference
is a direction guide; runtime controls remain Godot-native text and controls,
never image-generated text.

## Acceptance criteria

- No legacy three-front backdrop texture is referenced by the battle focus.
- The battle focus is wider than the current 576px presentation at 960x540.
- The foundation has no route-breaking water or obstacle, no baked foreground
  terrain prop, and no baked buildings, construction objects, units, or tower.
- Lumern and Veil terrain props are independent transparent assets and are
  selected by their placement ratio, never painted into the foundation.
- One dynamic tower and live Lumern/Veil units remain drawn from current battle
  state.
- The existing five-sector minimap keeps its read-only state projection.
- Deterministic headless tests, editor import, focused runtime technical smoke,
  1920x1080 and 1280x720 captures are run after asset lock. Human readability
  remains `NOT_RUN` until a person reviews the live screen.

## Explicit exclusions

- No gameplay balance, route ownership, tower rule, roster-slot rule, or
  roulette rule changes.
- No new building placement system, pathfinding system, unit archetype, or
  third-party asset/plugin.
- No deletion or overwrite of the legacy backdrop or prior generated
  candidates.
