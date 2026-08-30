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

The new background is an original, terrain-only 16:9 watercolor plate for a
close battle. It uses a broad, gently irregular, continuously traversable
center field from left to right. The playable visual ground is warm muted
grass and earth with low, soft edge terrain: broken slabs, shallow flowered
banks, sparse shrubs, haze, and distant ward/Veil atmosphere.

The Ward side uses cool navy/ivory light and restrained gold; the Veil side
uses charcoal/violet shadow and limited rift glow. Their transition is a
gradual environmental change, not a road, river, bridge, cliff, moat, hard
border, or gap. The center must remain open enough for two-to-three readable
unit rows. It contains no baked characters, tower, buildings, UI, words,
logos, pads, flags, or route nodes.

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

Two non-runtime candidates are required before any binding:

1. a terrain-only close-battlefield plate that satisfies the map contract;
2. a no-copy UI composition reference showing that terrain, the approved unit
   language, the wide battle view, the narrow minimap, and the compact lower
   deck together.

Both candidates are `GENERATED_CANDIDATE` only. The user must lock the exact
selected terrain candidate before it is copied under `assets/`, referenced by
Godot, or registered as canonical. The UI reference is a direction guide;
runtime controls remain Godot-native text and controls, never image-generated
text.

## Acceptance criteria

- No legacy three-front backdrop texture is referenced by the battle focus.
- The battle focus is wider than the current 576px presentation at 960x540.
- The original terrain has no route-breaking water or obstacle and no baked
  buildings, construction objects, units, or tower.
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
