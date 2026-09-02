# [Candidate] OMENWARD Wide Connected Strategic Front Terrain

```yaml
asset_id: OMW-IMG-20260830-WIDE-CONNECTED-STRATEGIC-FRONT-TERRAIN-V1
created_at: 2026-08-30 KST
status: USER_APPROVED__CANON_REGISTERED__SUPERSEDED_RUNTIME_CONSUMER__RUNTIME_NOT_RUN
generator: BUILT_IN_IMAGEGEN
source_path: C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-d92537dd-f555-4281-a9c8-bb3abc943b38.png
source_sha256: 1E56ACBD1B75394ADC7A7D059D0C3AB4AFCECA3B7CAF39F294886B7714768FA8
source_dimensions_px: 1672x941
historical_consumer: scenes/battle/battlefield.tscn/Backdrop
current_runtime_binding: NONE__SUPERSEDED_BY_OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
implementation_issue: Issue #235
runtime_asset: assets/art/battlefield/wide_connected_strategic_front_terrain_v1.png
repository_runtime_path: assets/art/battlefield/wide_connected_strategic_front_terrain_v1.png
runtime: NOT_RUN
human_readability: NOT_RUN
rights_status: GENERATION_PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
user_asset_lock: USER_APPROVED_EXACT_CANDIDATE
approval_source: USER_CHAT__"승인, 진행해줘"
```

## Purpose

This user-approved candidate is retained as provenance for the earlier wide
single-march composition. The current battle-primary decision no longer binds
it: the close combat viewport uses the legacy runtime backdrop as a temporary
input while a future dedicated combat-background asset follows its own review
and promotion gate.

```text
HISTORICAL_ROUTE_GRAMMAR = ONE_WARD_ROOT -> THREE_WIDE_CONNECTED_FRONTS -> ONE_VEIL_ROOT
NO_RIVER = REQUIRED
NO_BRIDGE = REQUIRED
NO_FENCE_OR_WALL = REQUIRED
NO_BUILDING_OR_CONSTRUCTION_PAD = REQUIRED
NO_UNIT_OR_TOWER_BAKED_INTO_TERRAIN = REQUIRED
BATTLEFIELD_VISIBLE_EXCLUDES = CONSTRUCTION_PADS + PRODUCTION_BUILDINGS + MAP_BUILDING_POPUPS
```

## Exact generation brief

The source was generated as an original 16:9, no-text, no-UI battlefield
background in the storybook watercolor SD tactical language: ivory paper,
blue-gray ink, restrained watercolor, a cool Ward-side tone and a restrained
Veil-side violet tone. It specifically requested no water, river, bridge,
fence, wall, castle, camp, building, tower, construction pad, character, unit,
or combat; those stateful layers remain Godot runtime presentation.

## Promotion and evidence boundary

- The user approved this exact terrain candidate and the bitmap remains stored
  without modification at the recorded repository path.
- It is no longer bound to `scenes/battle/battlefield.tscn::Backdrop`; the
  current consumer is the recorded legacy backdrop, cropped by the live battle
  focus view.
- `StrategicMapView`, units, objective state, and fixed towers remain dynamic
  Godot presentation. This terrain contains none of those stateful layers.
- Successful image generation and machine checks do not establish player
  readability, visual style-fit, human UX, release rights, or runtime PASS.

## Remaining gate

```text
USER_APPROVED__CANON_REGISTERED
-> SUPERSEDED_RUNTIME_CONSUMER
-> RETAINED_FOR_PROVENANCE_ONLY
```
