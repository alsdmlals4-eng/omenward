# OMENWARD · Shield Guard Cleanup Master Pair V1 · User Approval Record

```yaml
approval_id: OMW-ASSET-APPROVAL-20260826-SHIELD-GUARD-CLEANUP-MASTER-PAIR-V1
contract_id: OMW-PLAN-20260826-UNIT-ANIMATION-PRODUCTION-CONTRACT-01
status: USER_APPROVED_CLEANUP_MASTER_PAIR
approved_at: 2026-08-26
approval_input: "승인"
scope: LUMERN_AND_VEIL_SHIELD_GUARD_IDLE_CLEANUP_MASTERS_ONLY
source_orientation: RIGHT_FACING_THREE_QUARTER
common_canvas: 1280x1344_RGBA_PNG
ground_baseline_y: 1280
pivot: [640, 1280]
partial_alpha_pixels: 0
godot_import: NOT_RUN
implementation_ready: NO
runtime_validation: NOT_RUN
```

## Approved local masters

| Faction | Source original | Cleanup master | SHA-256 |
|---|---|---|---|
| Lumern | `.asset-vault/library/characters/allies/OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1.png` | `.asset-vault/library/characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_CLEANUP_MASTER_V1.png` | `f3189ba44bb2994760075eed1aa8aed97333948116f7d66f618ff66b3db999bf` |
| Veil | `.asset-vault/library/characters/enemies/OMENWARD_ASSET_UNIT_VEIL_SHIELD_GUARD_IDLE_V1.png` | `.asset-vault/library/characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_SHIELD_GUARD_IDLE_CLEANUP_MASTER_V1.png` | `11d6fa548f03b1609afb60344404fac288ba9e5702a15cc57e76ff577eacff0a` |

The source originals remain immutable. The approved masters are alpha-hardened, non-destructive derivatives: alpha values `0–63` were removed as fringe noise; all remaining source pixels retain their original RGB values and are fully opaque. No pose, palette, silhouette, direction, crop, or scale was redrawn.

## Geometry addendum · idle master only

```text
MASTER_CANVAS = 1280x1344
GROUND_BASELINE_Y = 1280
PIVOT_X_Y = 640,1280
SOURCE_FACING = RIGHT
MIRROR_CONVENTION = FUTURE_RUNTIME_ONLY__NOT_LOCKED
IDLE_SOURCE_FRAMES = 1
IDLE_LOOP = TRUE
IDLE_FPS = NOT_APPLICABLE__STATIC_MASTER
ATTACK_IMPACT_FRAME = NOT_APPLICABLE__IDLE_ONLY
PROJECTILE_SPAWN_FRAME = NOT_APPLICABLE__IDLE_ONLY
OTHER_STATE_FRAME_COUNTS_AND_TIMING = NOT_LOCKED
MASS_UNIT_ATLAS_PRODUCTION = BLOCKED_PENDING_STATE_ANIMATION_SOURCES
```

This addendum locks shared canvas, baseline, pivot, and idle-source geometry only. It does not invent missing animation timing, authorize an atlas, or authorize Godot integration.

## Validation

- [x] Lumern/Veil common canvas dimensions are `1280x1344`.
- [x] Both opaque art bounds terminate at ground baseline `Y=1280`.
- [x] Both master files are `Format32bppArgb` with zero partial-alpha pixels and transparent corners.
- [x] Local SHA-256 recorded for both masters.
- [ ] Notion approval-record readback for both masters.
- [ ] Animation-state frame counts, FPS, event frames, and atlas layout.
- [ ] Godot import, runtime scale/readability, and human play evidence.

## Next gate

```text
NEXT_IMAGE_ACTION = IMG_02_GREATSWORD_AND_SPEAR_GOAL_SPECIFIC_APPROVAL
CODEX_GODOT = BLOCKED
```
