# OMENWARD · Top-Down Unit Silhouette Rules

```yaml
decision_id: OMW-PLAN-20260820-TOPDOWN-UNIT-SILHOUETTE-01
status: USER_APPROVED_PLANNING_CANON
work_mode: PLANNING_ONLY
implementation_authorized: false
```

## Purpose

Define how Anime Pixel units remain readable from the approved top-down battlefield camera.

## Read order

```text
ROLE SILHOUETTE
→ WEAPON / UNIQUE SHAPE
→ BODY SCALE
→ FACTION COLOR
→ TIER DETAIL
→ DECORATION
```

## Unit rules

| Unit Role | Primary silhouette anchor |
|---|---|
| Shield | oversized shield front shape |
| Knight | mount + lance/weapon line |
| Archer | bow silhouette and ranged posture |
| Mage | staff and magic core |
| Flying | wing span |
| Assassin | narrow body + dual weapon |
| Heavy Hammer | large hammer + heavy frame |
| Giant | scale difference |

## Tier rules

- T1/T2 must remain readable at battlefield zoom.
- T3 detail must not reduce role recognition.
- Decoration is lower priority than combat role.

## Battlefield relationship

Units are not individual portraits during normal combat.

```text
Small scale = role readability
Large reveal = character appeal
```

Elite, Boss and reward previews may use richer Anime Pixel presentation.

## Validation

This is a North Star / Vertical Slice planning envelope, not final runtime asset specification.
