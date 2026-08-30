# OMENWARD Wide Connected Strategic Front Terrain V1

```yaml
asset_id: OMW-IMG-20260830-WIDE-CONNECTED-STRATEGIC-FRONT-TERRAIN-V1
status: USER_APPROVED__CANON_REGISTERED__SUPERSEDED_RUNTIME_CONSUMER__RUNTIME_NOT_RUN
approval_source: USER_CHAT__"승인, 진행해줘"
approved_at: 2026-08-30 KST
creation_route: AI_GENERATED
generator: BUILT_IN_IMAGEGEN
source_type: ORIGINAL_GENERATION__NO_REFERENCE_IMAGE
source_sha256: 1E56ACBD1B75394ADC7A7D059D0C3AB4AFCECA3B7CAF39F294886B7714768FA8
dimensions_px: 1672x941
format: PNG_RGBA_OPAQUE
repository_path: assets/art/battlefield/wide_connected_strategic_front_terrain_v1.png
sha256: 1E56ACBD1B75394ADC7A7D059D0C3AB4AFCECA3B7CAF39F294886B7714768FA8
historical_consumer: scenes/battle/battlefield.tscn::Backdrop
current_runtime_binding: NONE__SUPERSEDED_BY_OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
implementation_issue: Issue #235
user_asset_lock: USER_APPROVED_EXACT_CANDIDATE
runtime: NOT_RUN
human_readability: NOT_RUN
release_rights: REVIEW_PENDING__NOT_RELEASE_PASS
```

## Asset boundary

This is the approved terrain-only source for the historical wide connected
battlefield. It remains canon-registered for provenance but is not a current
runtime consumer after the battle-primary presentation decision.
It contains no units, fixed towers, construction pads, buildings, UI, or
objective state. `BattlefieldView` renders those stateful layers dynamically.

```text
HISTORICAL_ROUTE_GRAMMAR = ONE_WARD_ROOT -> THREE_WIDE_CONNECTED_FRONTS -> ONE_VEIL_ROOT
NO_RIVER = REQUIRED
NO_BRIDGE = REQUIRED
NO_FENCE_OR_WALL = REQUIRED
NO_BUILDING_OR_CONSTRUCTION_PAD = REQUIRED
NO_UNIT_OR_TOWER_BAKED_INTO_TERRAIN = REQUIRED
```

## Evidence ceiling

The file remains retained and hash-verified, but it is not bound to the current
scene consumer. Neither its prior deterministic coverage nor its approval
proves a live gameplay render, human readability, final art quality,
commercial release rights, or release pass.
Those remain recorded as `NOT_RUN` / pending until separately observed.
