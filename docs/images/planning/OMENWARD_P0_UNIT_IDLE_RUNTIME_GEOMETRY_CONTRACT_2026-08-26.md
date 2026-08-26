# OMENWARD · P0 Unit Idle Runtime Geometry Contract

```yaml
contract_id: OMW-ASSET-20260826-P0-UNIT-IDLE-RUNTIME-CELL-01
status: APPROVED_BY_CONTINUATION_AUTHORITY
scope: NINE_APPROVED_P0_UNIT_PAIRS_EXCLUDING_LOCKED_SHIELD_GUARD_PILOT
```

## Intent

Use the already approved P0 cleanup masters in the shared battle renderer without changing their source art, gameplay data, or animation state.  The derivative makes the visible feet or lowest art extent share a predictable battle ground line; it is not a new art candidate.

## Locked runtime format

- Each pair produces a transparent `512×512` idle PNG under `res://assets/art/units/`.
- The common renderer pivot is `(256, 448)`.
- The cleanup master is alpha-bounds cropped, nearest-neighbour scaled to fit the recorded height limit, and horizontally centred with its bottom at `y=448`.
- All output alpha is binary (`0` or `255`); no blur, recolour, inpainting, or image generation occurs.
- The source masters remain immutable in `.asset-vault`; the committed PNG is a Godot-only derivative.  The generated run record stores both source and output SHA-256 values.
- All sources face right; the existing shared `UnitView` mirrors Veil at runtime. No enemy-only Scene or gameplay branch is introduced.

## Scope

Greatsword Warrior, Assassin, Spear Guard, Archer, Cavalry, Priest, Mage, Flier, and Giant for Lumern and Veil. Shield Guard keeps its separately approved `1280×1344`, `(640,1280)` pilot contract unchanged.

## Evidence ceiling

The contract proves asset geometry and importer binding only. Interactive SD combat readability, collision overlap, and player evidence remain `NOT_RUN` until a Godot run is reviewed.
