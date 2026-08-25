# [현행] OMENWARD Active Context

```yaml
updated_at: 2026-08-25
status: CURRENT_V4_8_FRONT_STATE_MINIMAP_SD_FANTASY_SPEC_REVIEW_CONTEXT
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
current_project_core: docs/PROJECT_CORE.md
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_open_work_items: FRESH_GITHUB_QUERY_REQUIRED
current_activity: VISUAL_PLANNING_ONLY
current_visual_spec: docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
implementation_authorized: true
implementation_scope: RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE_ONLY
implementation_execution: NOT_RESUMED_IN_CURRENT_VISUAL_REVIEW
implementation_packet: docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md
implementation_plan: docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md
persistent_godot_authoring: HIGODOT_ONLY
visual_generation: USER_REQUEST_ONLY
current_chat_runtime_status: NOT_RUN
human_player_evidence: NOT_RUN
```

## Current planning state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 20
WORLD_ROLE = CONFIRMED
MAPRUN_WORLD_MEANING = CONFIRMED
PRESSURE_LANGUAGE = CONFIRMED
MOBILIZATION_REGISTRY = CONFIRMED
FIRST5_FTUE = CONFIRMED
RUN_COMMAND_SCREEN = CONFIRMED
WORLD_CONFLICT_AND_STORY = CONFIRMED
CONTENT_BOSS_ARC = CONFIRMED
NORMALIZED_BALANCE_BUDGET = CONFIRMED
TEXT_UX_STATE = CONFIRMED
VISUAL_STYLE_COMPONENTS_20260820 = PARTIALLY_SUPERSEDED
BATTLEFIELD_SCALE_AND_COMBAT_READABILITY = RETAINED_WITH_LAYOUT_OVERRIDE
ROULETTE_3X3_COMPONENT = CONFIRMED
TOKEN_COMPONENT = CONFIRMED
LOWER_CONTROL_DECK = CONFIRMED
ROULETTE_DDD_FEEDBACK = CONFIRMED
TOPDOWN_BATTLEFIELD_LAYOUT_20260820 = PARTIALLY_SUPERSEDED
TOPDOWN_UNIT_SILHOUETTE = CONFIRMED
NORTH_STAR_V2_1 = REFERENCE_WITH_NEW_OVERRIDE
FRONT_STATE_MINIMAP_SD_FANTASY = CONFIRMED_CURRENT
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED
RUN_COMMAND_IMPLEMENTATION_EXECUTION = NOT_RESUMED_IN_THIS_VISUAL_REVIEW
CURRENT_NEXT = USER_REVIEW_OF_FRONT_STATE_MINIMAP_SD_FANTASY_WRITTEN_SPEC
IMAGE_GENERATION = STOPPED_FOR_CURRENT_REVIEW
```

2026-08-25 사용자 승인 Decision `OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01`이 visual/battlefield 표현의 current owner다. 이전 `Anime Pixel + Clean Pixel`, 긴 3-lane road 전체표시, 미니맵 비요구는 해당 범위에서 superseded다. 세 전선 동시 가독성, 전장-primary, 하단-secondary, 병종 실루엣 우선은 유지한다.

Current visual owner:
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`

Implementation authority owners remain retained but are not being executed by this visual-planning task:
- `docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md`
- `docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md`

각 개별 Decision owner의 과거 `CURRENT_NEXT / THEN`은 승인 당시의 local sequence다. 현재 작업 순서는 `docs/CURRENT_CONFIRMED_DECISIONS.md`와 이 Active Context를 사용한다.

## Current product core

```text
건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.

징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 3×3 징조륜 결과 / 제한된 행·열 조작
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
```

## Authorized implementation slice — retained, not currently executing

```text
PREPARE
→ stopped 3×3 snapshot
→ limited row/column manipulation
→ confirmed resolution
→ reward storage
→ COMMIT pending lane plan
→ aggregate food/spawn preflight
→ atomic deployment apply
→ BATTLE
→ REVIEW
```

### Architecture lock

```text
ARCHITECTURE = ORCHESTRATION_FIRST_VERTICAL_SLICE
PERSISTENT_GODOT_AUTHORING = HIGODOT_ONLY
STAGE_RUN = EXISTING_FOUNDATION_COORDINATOR
ROULETTE_SERVICE = EXISTING_OUTCOME_AUTHORITY_WITH_STOPPED_SNAPSHOT_SEAM
DEPLOYMENT_SERVICE = EXISTING_FOUNDATION_PLUS_BATCH_TRANSACTION
BATTLE_SIMULATOR = EXISTING_FOUNDATION_PLUS_NON_MUTATING_SPAWN_PREFLIGHT
STAGE_ECONOMY = EXISTING_FOUNDATION_PLUS_NON_MUTATING_FOOD_PREFLIGHT
RUN_COMMAND_STATE = NEW_THIN_OWNER
ROULETTE_MANIPULATION_SESSION = NEW_THIN_TRANSACTION_OWNER
PENDING_DEPLOYMENT_PLAN = NEW_THIN_PLAN_OWNER
PLAYER_UI = READ_ONLY_VIEW_MODEL_PLUS_COMMAND_SURFACE
TECHNICAL_STAGE_HUD = PRESERVE_AS_DEBUG_EVIDENCE_SURFACE
```

Implementation authority is **not** a project-wide build approval. This visual-planning Decision also does not itself authorize Godot/UI implementation. Runtime implementation resumes only under the existing scoped packet after current visual spec review and fresh execution bootstrap.

## Current world

```text
PLAYER_ROLE = Omen Warden / 징조수호관
PLAYER_FANTASY = 전조를 읽고 수호성을 준비하며 병력을 세 전선에 보내는 지휘관
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상
OMEN = 실제 공세 전에 나타나는 전조 / Pre-Echo
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
RUN_HISTORY_RESET = FALSE
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
DANGER_STAGE_TYPE = REMOVED
```

## Current UI / visual

```text
RUN_COMMAND_SCREEN = PREPARE -> COMMIT -> BATTLE -> REVIEW
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
MATERIAL_FINISH = HIGH_RES_PIXEL_TEXTURE_AND_RESTRAINED_LIGHTING
WORLD_TONE = FANTASY_WARD_CITADEL + MAGIC_WARFARE

BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
UNIT_BY_UNIT_MINIMAP_REPLICATION = FORBIDDEN
LONG_FULL_ROAD_PRESENTATION = SUPERSEDED_AS_DEFAULT

NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
ROULETTE_EXPOSURE = 3×3
ROW_COLUMN_ARROWS = PROMINENT
PLAYER_MOVE_FEEDBACK_PRIORITY = HIGHEST
NORTH_STAR_V2_1 = REFERENCE_ONLY_AFTER_2026_08_25
VISUAL_GENERATION = USER_REQUEST_ONLY
```

### Faction language retained

```text
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
VEIL_SHAPES = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
```

### Front-State information split

```text
FRONT_STATE_VIEW = CURRENT_UNITS + CURRENT_THREAT + CURRENT_CLASH + COMMIT_OUTCOME
PER_FRONT_MINIMAP = FRONT_PROGRESS + STRONGHOLD + ROUTE + INFILTRATION/AIR + BOSS/SIEGE_CONTEXT
```

미니맵은 작은 두 번째 전장이 아니다. 개별 병사/VFX를 그대로 복제하지 않는다.

## North Star v2.1 evidence boundary

```text
NOTION_UPLOAD_ATTACH = PASS
NOTION_SERVER_READBACK = PASS
NORTH_STAR_V2_1_OVERALL = REFERENCE_ONLY_AFTER_2026_08_25
RETAINED = BATTLEFIELD_PRIMARY_HIERARCHY + ALLY_VS_VEIL_CONTRAST + COMPACT_LOWER_DECK_DIRECTION
SUPERSEDED = LONG_ROAD_FULL_THREE_LANE_COMPOSITION + NO_MINIMAP + ANIME_PIXEL_ONLY_STYLE
FINAL_UI_GEOMETRY = NOT_APPROVED
FINAL_COPY_FROM_IMAGE = NOT_APPROVED
FINAL_PRODUCT_NUMERICS_FROM_IMAGE = NOT_APPROVED
HUMAN_VISIBLE_NOTION_CLIENT = NOT_RUN
```

Notion server readback은 브라우저/모바일 실제 렌더 PASS가 아니다.

## Balance boundary

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

The visual Decision does not authorize final economy/balance values.

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
LEGACY_C1_C2_C3_PROVEN
HUMAN_QA_NOT_RUN
```

과거 C1/C2/C3 exact proof와 signal11/HiGodot/GUT/Hera 기록은 history/evidence다. 현재 visual/runtime/player-experience PASS로 승격하지 않는다.

## GitHub routing

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

현재 파일은 PR 번호나 branch HEAD를 live state로 고정하지 않는다. unrelated open/draft work remains read-only.

## Current work order

```text
1. COMPLETE — existing world/story/content/balance envelope/Text UX
2. COMPLETE — retained 3×3/token/lower deck/roulette DDD contracts
3. SUPERSEDED_IN_PART — old Anime Pixel/Clean Pixel + long-road battlefield default
4. COMPLETE — user approved Front-State + per-front minimap + Fantasy/Magic/SD direction
5. COMPLETE — written spec + alternatives + planning adversarial review 5/5
6. CURRENT — user review of written visual spec
7. AFTER_REVIEW — synchronize any accepted wording corrections and close/merge planning PR under normal PR gates
8. NOT_STARTED — runtime blockout/readability validation for minimaps and SD units
9. RETAINED_NOT_RESUMED — scoped Run Command implementation packet
10. OPTIONAL IMAGE — only on a later explicit user image request
```

## Resume order

1. fresh Base current authority.
2. fresh OMENWARD main + PR/Issue inventory.
3. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
4. this file.
5. visual/battlefield scope: `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`.
6. current GDD/Project Core + relevant owner; when an older visual phrase conflicts, the 2026-08-25 Decision supersession applies.
7. Project Notion Home + Visual Bible + Visual Component page.
8. implementation scope is reopened only after the current spec review and fresh execution decision/bootstrap; no product mutation is implied by this planning sync.
9. image generation only on explicit user request.
