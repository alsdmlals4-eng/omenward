# OMENWARD · Runtime Consumer Image Asset Master Checklist

```yaml
tracker_id: OMW-VIS-TRACKER-20260826-MASTER-01
policy_id: OMW-VIS-POLICY-20260826-RUNTIME-CONSUMER-ASSET-FIRST-01
status: USER_APPROVED_CURRENT_POLICY
updated_at: 2026-08-26
scope: PLANNING_AND_GAME_CONSUMED_IMAGE_ASSET_TRACKING
current_user_work_mode: PLANNING_PLUS_IMAGE_ONLY
current_user_order: REQUIRED_GAME_IMAGES_FIRST_THEN_CODEX
product_code_mutation: NONE
godot_execution: NOT_IN_SCOPE
codex_execution: NOT_IN_SCOPE
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
current_reference_asset: OM-IMG-023
current_approved_runtime_asset_source: ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
current_next_brief: OMW-ASSET-BRIEF-20260826-VEIL-SHIELD-GUARD-01
goal_queue: OMW-IMG-GOALS-20260826-RUNTIME-CONSUMER-COVERAGE-01
goal_queue_status: PROPOSED_FOR_USER_REVIEW
```

## 1. Production rule

```text
NO_RUNTIME_OR_PRODUCT_CONSUMER = NO_IMAGE_PRODUCTION_TASK
EXPLANATION_SHEET = PLANNING_REFERENCE_ONLY
FULL_SCREEN_MOCKUP = PLANNING_REFERENCE_ONLY
COMPARISON_BOARD = PLANNING_REFERENCE_ONLY
RUNTIME_TEXTURE_OR_SPRITE_OR_ICON_OR_VFX = IMAGE_PRODUCTION_CANDIDATE
```

Notion/Markdown/Mermaid/Figma-native structure remains the default for production information. A generated picture is required only when an actual game/player-facing/product-distribution surface consumes pixels.

Detailed remaining Goal packets and future Codex handoff order:

`docs/images/planning/OMENWARD_REMAINING_IMAGE_GOALS_AND_CODEX_INTEGRATION_QUEUE_2026-08-26.md`

## 2. Current implementation reality

Current player-facing product art is still graybox.

- `scripts/units/unit_view.gd` draws circles/polygons/lines.
- `scripts/battle/battlefield_view.gd` draws rectangles/lines/outpost circles.
- `scenes/ui/stage_hud.tscn` uses Labels/Buttons without OMENWARD product textures/icons.

```text
PROJECT_PRODUCT_IMAGE_ASSETS_IMPLEMENTED = 0
PROJECT_PRODUCT_IMAGE_ASSETS_RUNTIME_VERIFIED = 0
CURRENT_GODOT_RUNTIME_IMAGE_EVIDENCE = NOT_RUN
```

## 3. Current visual locks

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
VEIL_SHAPES = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
ROLE_SILHOUETTE_FIRST = TRUE
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
CASINO_SLOT_MACHINE_LANGUAGE = FORBIDDEN
```

`OM-IMG-023` remains a visual direction/composition reference and is not a runtime background texture.

## 4. Existing image lifecycle inventory

| Item | Status | Decision |
|---|---|---|
| `OM-IMG-023` | `REFERENCE_ONLY` · user-approved visual direction | `REUSE_AS_IS` as reference only |
| `ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1` | `APPROVED` | `REUSE_WITH_EDIT` for cleanup/runtime export/animation/token crop |
| `ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1` | not generated; brief ready | `NEW_REQUIRED` · current next image candidate |
| old `OMW-VIS-001~012` full-screen/sheet lineage | `REFERENCE_ONLY` / some `SUPERSEDED` | no production-image counting |
| historical VR-001/VR-002/old image-gen candidates | `REFERENCE_ONLY` / `SUPERSEDED` | selective reference only |
| unregistered second blue-knight generation after Lumern approval | `REJECTED` | conflicts with Veil brief; not canon |
| GUT/addon/editor images | tool assets | `REJECT` for OMENWARD product content |

Approved Lumern durable record:

```text
APPROVAL = OMW-ASSET-APPROVAL-20260826-LUMERN-SHIELD-GUARD-IDLE-V1
FILE = OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1.png
SIZE = 1254x1254 RGBA
SHA256 = 3e98fb83f5ac9169c387e6669c8ba545375700fc2346fc004781754884b2a50a
DRIVE_ID = 1ZiVrA2mxO8sfzzct6uuPAk_b0NDMK8b8
PIXEL_CLEANUP = NOT_RUN
IMPLEMENTATION_READY = NO
IMPLEMENTED = NO
RUNTIME_VERIFIED = NO
```

## 5. Existing Solution First

- Unit tokens: derive from approved unit art; no token-only character illustration.
- Gold: one shared image for HUD/reward/Roulette.
- Token frame: one reusable family for Roulette/Result/Storage/COMMIT.
- Manipulation arrows: one source rotated/flipped for 12 controls.
- Building thumbnails: crop/reframe world building source.
- Panel/Button/selected/disabled/valid-invalid states: prefer Godot Theme/NinePatch/shader/primitive before new raster images.
- Minimap: runtime context + marker atlas; no painted mini-battle duplicate.
- Base/cross-project title-specific art: no direct OMENWARD pixel reuse found; process/reference only.

## 6. P0 Goal summary · current playable scope blockers

| Goal | Asset family | Current state |
|---|---|---|
| IMG-01 | Shield Guard faction pair | Lumern idle `APPROVED`; Veil idle `BRIEF_READY` |
| IMG-02 | Greatsword + Spear 2 factions | `NEW_REQUIRED` |
| IMG-03 | Archer + Cavalry 2 factions | `NEW_REQUIRED` |
| IMG-04 | Priest + Mage 2 factions | `NEW_REQUIRED` |
| IMG-05 | Assassin + Flier 2 factions | `NEW_REQUIRED`; extra states `STATE_RECHECK` |
| IMG-06 | Giant 2 factions | `NEW_REQUIRED`; giant extra states `STATE_RECHECK` |
| IMG-07 | Unit crops + Gold/X/frame/state overlay | crops `DERIVED`; others `NEW_REQUIRED` |
| IMG-08 | 5 Omen Signature icons | `NEW_REQUIRED` |
| IMG-09 | Mana + troop capacity + minimap markers | `NEW_REQUIRED`; Gold reused |
| IMG-10 | 3×3 board/arrow/device textures | `NEW_REQUIRED_IF_IMAGE_NEEDED`; Theme delete-test first |
| IMG-11 | Vault/Farm/General Barracks/Defense Tower T1 | `NEW_REQUIRED` |
| IMG-12 | Command Post/Mana Tower T1 | `NEW_REQUIRED` |
| IMG-13 | terrain/stronghold/Veil anchor/outpost-route props | `NEW_REQUIRED` |

## 7. P1 Goal summary · Vertical Slice/Demo quality

| Goal | Asset family | Current state |
|---|---|---|
| IMG-14 | Omen Warden command representation | `NEW_REQUIRED` after exact consumer confirmation |
| IMG-15 | deploy/hit/siege/capture combat feedback | `NEW_REQUIRED_IF_RASTER_REQUIRED` |
| IMG-16 | roulette snap/line-lock/reward VFX | `NEW_REQUIRED_IF_RASTER_REQUIRED` |
| IMG-17 | current T2 building specialization visuals | `NEW_REQUIRED` in subpackets |
| IMG-18 | 10 tactical skill icons | `NEW_REQUIRED` in T1 4 / T2 3 / T3 3 packs |
| IMG-19 | Unit tier/rank variants | `CANON_DATA_RECHECK` before exact count |

Current building authority is **7 base building types**, not the old six-family universal A/B model:

```text
Vault / Farm / General Barracks / Special Barracks / Defense Tower / Command Post / Mana Tower
```

Stage-1 required T1 foundation remains six: Special Barracks is optional later. T2 current branches are current only from `OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1`; the 2026-08-05 universal A/B document is `SUPERSEDED / IMPLEMENTATION_INPUT_FORBIDDEN`.

## 8. P2/P3 deferred nonblocking

P2:
- IMG-20 Stage 5/10/15/20 Boss runtime visual families.
- IMG-21 REVIEW.MAINTENANCE Merchant actual portrait/sprite if concrete surface uses it.
- IMG-22 Bellu guide asset only after current player-facing surface recheck.
- IMG-23 authored additional biome/environment sets.
- IMG-24 T3 buildings/high-rank variants after current canon/data resolves them.

P3:
- IMG-25 title/main-menu art after concrete menu consumer exists.
- IMG-26 Steam/distribution marketing set after official platform spec fresh-read.

These are actual-use candidates but do not block the current playable-scope Codex start gate.

## 9. Non-image prerequisites

Do not generate explanation images for these gaps.

```text
UNIT_ANIMATION_PRODUCTION_CONTRACT
→ exact frame/FPS/pivot/atlas arrangement + missing choreography

UNIT_TIER_VISUAL_DATA_CONTRACT
→ exact tier/rank runtime mapping before IMG-19

BUILDING_T3_CANON_RECHECK
BOSS_BEHAVIOR_VISUAL_RECHECK
BELLU_CURRENT_SURFACE_RECHECK
PLATFORM_SPEC_RECHECK
```

## 10. Current production queue

```text
NOW
1. User review/approval of OMW-IMG-GOALS-20260826-RUNTIME-CONSUMER-COVERAGE-01
2. IMG-01 / ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1
3. Shield pair user approval / style lock
4. finalize non-image UNIT_ANIMATION_PRODUCTION_CONTRACT
5. complete P0 image Goal packets
6. complete current-consumer P1 Goal packets
7. pixel cleanup / Notion approved registration / implementation-ready evidence
8. only then prepare Codex Integration Goals for execution

CODEX = NOT_STARTED
```

## 11. Asset completion definition

An asset is not complete at generation.

```text
Generated
→ Reviewed
→ Approved
→ Notion Registered
→ Pixel/Transparency/Edge Cleanup
→ Consumer + File Role + Hash recorded
→ Implementation Ready
→ Codex Imported
→ Implemented
→ Runtime Verified
```

- Static approval is not runtime proof.
- Runtime validation must include target-resolution screenshots/play evidence.
- No unrelated PR/workstream takeover.

## 12. Adversarial review

1. Missing: added tactical skill icons and current building T2 structure.
2. Excess: removed explanation sheets/panels/minimap backgrounds where semantic UI can solve the need.
3. Reuse: Lumern source, unit-token crops, Gold/frame/arrow/building crops are reused.
4. Canon: obsolete building A/B branches forbidden; T3 unresolved states gated.
5. Feasibility: unit bulk atlas production is blocked until exact animation production contract exists.
6. Player value: P0/P1 current consumers first; P2/P3 deferred until their stage.

```text
ADVERSARIAL_REVIEW = CLEAN_6_OF_6_AFTER_CORRECTIONS
IMAGE_GENERATION_THIS_AUDIT = NOT_RUN
IMPLEMENTATION = NOT_RUN
RUNTIME_VERIFICATION = NOT_RUN
```

## 13. Boundary

```text
SCREEN_MOCKUP_IMAGE_PRODUCTION = STOPPED
EXPLANATION_SHEET_IMAGE_PRODUCTION = STOPPED
RUNTIME_CONSUMER_ASSET_PLANNING = ACTIVE
CURRENT_NEXT_ASSET = ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1
CURRENT_NEXT_ASSET_GENERATION = AWAITING_GOAL_QUEUE_USER_APPROVAL
CODEX_PRODUCT_IMAGE_INTEGRATION = BLOCKED_BY_USER_ORDER
UNBLOCK_CODEX = CURRENT_CONSUMER_P0_P1_IMAGE_GOALS_APPROVED_AND_IMPLEMENTATION_READY
GOOGLE_SHEET = COMPATIBILITY_HISTORY_ONLY_STALE
```