# OMENWARD · Top-Down Battlefield Layout Specification

```yaml
decision_id: OMW-PLAN-20260820-TOPDOWN-BATTLEFIELD-LAYOUT-01
status: CONFIRMED_PLANNING_CANON
implementation_authorized: false
```

## Direction

Battlefield uses a top-down focused strategy view.

- Full three lanes remain visible.
- Slight perspective depth is allowed.
- Strategic readability has priority over cinematic camera.

## Layout Goals

```text
PLAYER
 ↓
Three lane battlefield
 ↓
Veil enemy territory
```

Required:

- Upper / middle / lower lanes readable at once.
- Wide combat roads.
- Clear clash nodes.
- Buildings do not block combat information.

## Lane Roles

| Lane | Identity |
|---|---|
| Upper | mobility / alternate routes |
| Middle | main clash area |
| Lower | variation / infiltration pressure |

## Camera Rules

```text
DEFAULT_CAMERA = FULL_THREE_LANE_VIEW
AUTO_HIDE_LANES = FORBIDDEN
CINEMATIC_ZOOM = EVENT_ONLY
```

## Exploration Envelope

```text
reference_resolution: 960x540
battlefield_share: 75%
lower_deck_share: 25%
road_width: 70~90px exploration
clash_node: 90~120px exploration
```

## Unit Readability

Priority:

1. weapon silhouette
2. body size
3. movement shape
4. faction color
5. details

The battlefield must communicate role before character detail.

## Next Gate

TOPDOWN_LAYOUT → UNIT_SILHOUETTE_RULES → NORTH_STAR_REBUILD
