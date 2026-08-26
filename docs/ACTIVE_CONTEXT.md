# [현행] OMENWARD Active Context

```yaml
updated_at: 2026-08-26
status: IMAGE_GOAL_AUDIT_AND_PRODUCTION_QUEUE_REVIEW
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
current_project_core: docs/PROJECT_CORE.md
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_open_work_items: FRESH_GITHUB_QUERY_REQUIRED
current_user_work_mode: PLANNING_PLUS_IMAGE_ONLY
current_user_order: REQUIRED_GAME_IMAGES_FIRST_THEN_CODEX
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
current_visual_reference: OM-IMG-023
current_image_policy: OMW-VIS-POLICY-20260826-RUNTIME-CONSUMER-ASSET-FIRST-01
current_image_goal_package: OMW-IMG-GOALS-20260826-RUNTIME-CONSUMER-COVERAGE-01
current_image_goal_package_status: PROPOSED_FOR_USER_REVIEW
current_approved_runtime_asset_source: ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
current_next_asset_brief: OMW-ASSET-BRIEF-20260826-VEIL-SHIELD-GUARD-01
current_next_asset_generation: AWAITING_GOAL_QUEUE_USER_APPROVAL
implementation_authorized: true
implementation_scope: RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE_ONLY
implementation_execution: BLOCKED_BY_CURRENT_USER_IMAGE_FIRST_ORDER
codex_image_integration: NOT_STARTED
current_godot_runtime: NOT_RUN
human_player_evidence: NOT_RUN
google_sheet: STALE_COMPATIBILITY_HISTORY_ONLY
```

## Current authority / freshness

Fresh-read required on every task:

```text
Base main
→ OMENWARD main + open PRs/issues
→ AGENTS.md
→ CURRENT_CONFIRMED_DECISIONS.md
→ this Active Context
→ current Notion Home + relevant image/visual pages
→ actual code/scenes/resources/assets/tests
```

Current known open PRs at this update are #205/#209/#212. They are unrelated/read-only unless fresh-read says otherwise; do not take them over from image work.

Google Sheet remains compatibility/history-only and is materially stale relative to GitHub/Notion current image work.

## Current product core

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 3×3 징조륜 결과 / 제한된 행·열 조작
→ 병력 획득
→ 세 전선 중 하나에 비가역 COMMIT
→ 자동전투 + 제한된 수동 전술
→ REVIEW 인과 복기
```

Player = **Omen Warden commander**, not frontline melee hero.

## Current visual canon

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
UNIT_BY_UNIT_MINIMAP_REPLICATION = FORBIDDEN
LONG_FULL_ROAD_PRESENTATION = SUPERSEDED_AS_DEFAULT
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
ROULETTE_EXPOSURE = 3×3
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
```

Faction language:

```text
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
VEIL_SHAPES = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
```

Current visual Decision owner:
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`

Current approved visual reference:
- `OM-IMG-023`
- `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`
- reference only; not a runtime background.

## Current image-production policy

```text
NO_RUNTIME_OR_PRODUCT_CONSUMER = NO_IMAGE_PRODUCTION_TASK
EXPLANATION_SHEET = PLANNING_REFERENCE_ONLY
FULL_SCREEN_MOCKUP = PLANNING_REFERENCE_ONLY
COMPARISON_BOARD = PLANNING_REFERENCE_ONLY
```

Actual product-image candidates are sprites/animations, token textures, actual HUD/icons/minimap markers, world/building/environment pixels, actual player-facing character assets, and VFX where raster/flipbook is genuinely required.

Godot Theme/NinePatch/shader/primitive is preferred over generating unnecessary panel/button/state images.

Policy/tracker owners:
- `docs/images/planning/OMENWARD_IMAGE_PRODUCTION_MASTER_CHECKLIST_2026-08-26.md`
- `docs/images/planning/OMENWARD_REMAINING_IMAGE_GOALS_AND_CODEX_INTEGRATION_QUEUE_2026-08-26.md`

## Current image lifecycle

### Reference

```text
OM-IMG-023 = REFERENCE_ONLY / USER_APPROVED_DIRECTION
```

### First actual approved game-asset source

```text
ASSET = ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
APPROVAL = OMW-ASSET-APPROVAL-20260826-LUMERN-SHIELD-GUARD-IDLE-V1
STATUS = APPROVED
FILE = OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1.png
SIZE = 1254x1254 RGBA
SHA256 = 3e98fb83f5ac9169c387e6669c8ba545375700fc2346fc004781754884b2a50a
DRIVE_ID = 1ZiVrA2mxO8sfzzct6uuPAk_b0NDMK8b8
PIXEL_CLEANUP = NOT_RUN
IMPLEMENTATION_READY = NO
IMPLEMENTED = NO
RUNTIME_VERIFIED = NO
```

Approval owner:
- `docs/images/approved/OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1_APPROVAL_2026-08-26.md`

### Current next asset

```text
BRIEF = OMW-ASSET-BRIEF-20260826-VEIL-SHIELD-GUARD-01
TARGET = ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1
BRIEF_STATUS = READY
IMAGE_GENERATION = NOT_RUN
USER_APPROVAL = NOT_RUN
```

Brief owner:
- `docs/images/planning/assets/ASSET_UNIT_VEIL_SHIELD_GUARD_BRIEF_2026-08-26.md`

An unregistered later blue-knight generation does not satisfy the Veil brief and has no approval; treat it as `REJECTED / NOT_CANON`.

## Implementation reality

Current OMENWARD product image integration is still zero.

```text
scripts/units/unit_view.gd = procedural circle/polygon/line graybox
scripts/battle/battlefield_view.gd = procedural rect/line/outpost graybox
scenes/ui/stage_hud.tscn = Label/Button graybox
PROJECT_PRODUCT_IMAGE_ASSETS_IMPLEMENTED = 0
PROJECT_PRODUCT_IMAGE_ASSETS_RUNTIME_VERIFIED = 0
```

No static image approval may be reported as Godot implementation/runtime proof.

## Current Goal queue

Detailed package:

`OMW-IMG-GOALS-20260826-RUNTIME-CONSUMER-COVERAGE-01`

```text
P0 = 13 Goal Packets / current playable-scope core consumers
P1 = 6 Goal Packets / Vertical Slice/Demo quality + current state completeness
P2 = 5 Goal Packets / later content expansion / current Codex gate nonblocking
P3 = 2 Goal Packets / release/marketing / current production forbidden
```

Current next sequence after user approves the Goal queue:

```text
IMG-01
→ generate ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1
→ user APPROVE/REVISE/REJECT
→ Shield pair style lock
→ finalize non-image UNIT_ANIMATION_PRODUCTION_CONTRACT
→ finish P0 image goals
→ finish current-consumer P1 image goals
→ pixel/edge/transparency cleanup + Notion registration
→ mark only proven files IMPLEMENTATION_READY
→ Codex Integration Goals
→ Godot import/scene/resource connection
→ target-resolution runtime screenshots/play QA
```

## Important non-image gates

These gaps are text/data contracts, not image-generation tasks:

```text
UNIT_ANIMATION_PRODUCTION_CONTRACT
UNIT_TIER_VISUAL_DATA_CONTRACT
BUILDING_T3_CANON_RECHECK
BOSS_BEHAVIOR_VISUAL_RECHECK
BELLU_CURRENT_SURFACE_RECHECK
PLATFORM_SPEC_RECHECK
```

Bulk unit animation art must not be produced before exact frame/FPS/pivot/atlas arrangement and missing choreography are locked.

Current building Tier authority is `OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1`:
- 7 base types = Vault / Farm / General Barracks / Special Barracks / Defense Tower / Command Post / Mana Tower.
- Stage-1 required foundation = 6; Special Barracks not mandatory at Stage 1.
- old universal A/B building branch document is `SUPERSEDED / IMPLEMENTATION_INPUT_FORBIDDEN`.

Tactical Skill canon has 10 player-facing skills (T1 4 / T2 3 / T3 3); their actual panel icons are included in P1 IMG-18.

## Runtime / evidence boundary

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_MINIMAP_READABILITY = NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN
CURRENT_GUT_RED = NOT_RUN
CURRENT_GUT_GREEN = NOT_RUN
CURRENT_HERA_LIVE_QA = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
```

## Current work order

```text
1. COMPLETE — current world/system/UX/visual Decisions retained
2. COMPLETE — runtime-consumer-first image policy
3. COMPLETE — Lumern Shield Guard idle visual approval
4. COMPLETE — Veil Shield Guard idle brief
5. COMPLETE — fresh existing-visual/consumer gap audit
6. CURRENT — Remaining Image Goal queue user review
7. NEXT_AFTER_APPROVAL — IMG-01 Veil Shield Guard idle production
8. THEN — P0/P1 current-consumer image production + approval + implementation-ready cleanup
9. BLOCKED_BY_USER_ORDER — Codex product image integration
10. AFTER_CODEX — runtime screenshot/play validation and correction
```

## Resume order

1. fresh Base main/required Base owners;
2. fresh OMENWARD main + open PR/issues;
3. `AGENTS.md`;
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`;
5. this file;
6. current image tracker + Remaining Image Goal package;
7. Notion Home → `19 · 이미지 제작 · Runtime Consumer Asset Checklist` → `23 · Remaining Image Goals · Codex Handoff Queue`;
8. approved Lumern asset record + current Veil brief;
9. actual code/scenes/resources/assets/tests;
10. Google Sheet only as stale compatibility/history unless authority changes.
