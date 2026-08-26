# OMENWARD · Current Confirmed Decisions

```yaml
updated_at: 2026-08-26
status: CURRENT_DECISION_RECOVERY_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
planning_reopened_at: 2026-08-20
current_planning_track: PAUSED_AFTER_FRONT_STATE_VISUAL_APPROVAL
runtime_evidence_ceiling: CURRENT_REPLAN_RUNTIME_NOT_RUN
human_play_evidence: NOT_RUN
visual_style: FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
current_visual_asset: OM-IMG-023
current_approved_runtime_asset_pair: SHIELD_GUARD_IDLE_PAIR
visual_generation_policy: USER_REQUEST_ONLY
visual_generation: USER_REQUEST_ONLY
```

이 문서는 현재 승인 Decision을 새 작업자가 빠르게 복원하는 **인덱스**다. 상세 규칙은 각 owner가 소유한다. 사람용 전체 그림·Flow·비교표는 Project Notion, 구조화 계약·code/data/scene/test/runtime evidence는 repository가 소유한다. GitHub PR/Issue의 live 상태는 문서에 고정하지 않고 매 작업 시작 시 fresh 조회한다.

각 개별 Decision owner 안의 과거 `CURRENT_NEXT / THEN`은 승인 시점의 local sequence로 읽는다. 현재 작업 순서와 supersession은 이 문서가 우선한다.

## Current approved replan decisions

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 21
```

| Decision ID | 승인 핵심 | Repository owner | 상태 |
|---|---|---|---|
| `OMW-PLAN-20260820-WORLD-ROLE-01` | 플레이어 = 징조수호관(Omen Warden), 룰렛 = 군사적 확률/동원 장치 | `docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-MAPRUN-WORLD-01` | 한 MapRun = 한 Ward Citadel + 20 Stage Omen Cycle | `docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-PRESSURE-LANGUAGE-01` | 5 Pressure = 복합 가능한 Omen Signature | `docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01` | 자동생산과 TokenSource는 별도 획득 경로, 세 릴↔세 전선 고정 대응 금지 | `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-FIRST5-FTUE-01` | Stage 1~5 = 인과 이해→미래 수정→순간 개입→응용→첫 결산 | `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01` | PREPARE→COMMIT→BATTLE→REVIEW | `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01` | Veil = 적대적 경계현상, 20 Stage = 지역 수렴기 | `docs/design/APPROVED_OMENWARD_VEIL_CONVERGENCE_FRONT_AND_CORE_STORY_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-CONTENT-BOSS-ARC-01` | 20 Stage = 4×5 authored spine, Boss 5/10/15/20 | `docs/design/APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-BALANCE-BUDGET-01` | 최종 숫자보다 normalized envelope 우선 | `docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-TEXT-UX-STATE-01` | Mode당 하나의 질문/Primary CTA, COMMIT은 staged→atomic irreversible confirm | `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01` | 과거 Anime Pixel + Clean Pixel 및 긴 전장 표현의 기반 owner. 2026-08-25 Visual Decision이 스타일/전장 표현 일부를 supersede | `docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md` | PARTIALLY_SUPERSEDED |
| `OMW-PLAN-20260820-BATTLEFIELD-SCALE-READABILITY-01` | 2~3열 교전·병종 실루엣 가독성 원칙 유지. 긴 도로 전체표시는 superseded | `docs/design/APPROVED_OMENWARD_BATTLEFIELD_SCALE_AND_COMBAT_READABILITY_2026-08-20.md` | RETAINED_WITH_LAYOUT_OVERRIDE |
| `OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01` | 3×3 + 행/열 직접 화살표 + 이동권 + 중앙줄 판정 | `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-TOKEN-COMPONENT-01` | 실제 병종 아트 T1/T2 토큰, 역할 실루엣 우선 | `docs/design/APPROVED_OMENWARD_TOKEN_COMPONENT_SPEC_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-LOWER-CONTROL-DECK-01` | Focus-adaptive compact lower deck, one active work surface | `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-ROULETTE-DDD-FEEDBACK-01` | Agency-first tactical crescendo | `docs/design/APPROVED_OMENWARD_ROULETTE_DDD_FEEDBACK_SPEC_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-TOPDOWN-BATTLEFIELD-LAYOUT-01` | 세 전선 동시 가독성·전술 시점 원칙 유지. 긴 3-lane road composition은 superseded | `docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md` | PARTIALLY_SUPERSEDED |
| `OMW-PLAN-20260820-TOPDOWN-UNIT-SILHOUETTE-01` | 역할→무기→체급→진영색→Tier→장식 순으로 읽히는 실루엣 | `docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260824-NORTH-STAR-V2-1-AUDIT-01` | 전장 우선 계층·진영 대비는 reference로 유지. 긴 길 전체표시와 스타일은 2026-08-25 Decision이 supersede | `docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md` | REFERENCE_WITH_NEW_OVERRIDE |
| `OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01` | 3개 Front-State View 동시 표시 + 전선별 미니맵 + Fantasy/Magic/SD Tactical Pixel + 긴 지휘 깃발 Omen Warden + 승인 이미지 `OM-IMG-023` | `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md` | CONFIRMED_CURRENT |
| `OMW-PLAN-20260826-UNIT-ANIMATION-PRODUCTION-CONTRACT-01` | Shield Guard Lumern/Veil pair의 공통 state·facing·pivot·보관·cleanup 경계를 승인하고 exact geometry/timing은 cleaned-pair addendum으로 유보 | `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md` | CONFIRMED_CURRENT |

## Protected product identity

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
→ 다음 설계
```

- `ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE`
- `GAMBLING_FANTASY_POSITIONING = FORBIDDEN`
- `SCRIPTED_FAKE_NEAR_MISS = FORBIDDEN`
- 자동생산과 TokenSource 별도 획득 경로
- 세 릴 ↔ 세 전선 고정 대응 금지
- Roulette result ≠ automatic lane deployment
- commit 이후 recall/sell/cross-lane 이동 금지
- `Veil ≠ Pressure ≠ 단일 적 종족`
- Boss = 5/10/15/20, every Stage final-wave Elite
- `DANGER_STAGE_TYPE = REMOVED`
- Forecast/Review는 정답 빌드를 지시하지 않음
- 최종 수치는 simulation/runtime/human evidence 전 승인하지 않음

## Current visual contract

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
MATERIAL_FINISH = HIGH_RES_PIXEL_TEXTURE_AND_RESTRAINED_LIGHTING
WORLD_TONE = FANTASY_WARD_CITADEL + MAGIC_WARFARE
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG

BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
LONG_FULL_ROAD_PRESENTATION = SUPERSEDED_AS_DEFAULT
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
UNIT_BY_UNIT_MINIMAP_REPLICATION = FORBIDDEN

PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
ROULETTE_EXPOSURE = 3×3
ROW_COLUMN_ARROWS = PROMINENT
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
NORTH_STAR_V2_1 = REFERENCE_ONLY_AFTER_2026_08_25
APPROVED_VISUAL = OM-IMG-023
```

Retained faction language:

```text
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
VEIL_SHAPES = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
```

Approved visual asset record:
- `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`
- Drive ID `1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5`
- Notion Home and Visual Bible contain the current inline preview and full-resolution link.

## Current balance / evidence boundary

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_MINIMAP_READABILITY = NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN
CURRENT_HUMAN_PLAYER_EVIDENCE = NOT_RUN
```

## Retained implementation authority

```text
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED
IMPLEMENTATION_PACKET = docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md
IMPLEMENTATION_PLAN = docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md
AUTHORIZED_SCOPE = RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE
AUTHORIZED_FLOW = PREPARE -> STOPPED_3X3 -> MANIPULATE -> CONFIRM -> COMMIT_PENDING -> ATOMIC_DEPLOY -> BATTLE -> REVIEW
RUNTIME_EVIDENCE = NOT_RUN
HUMAN_EVIDENCE = NOT_RUN
CURRENT_EXECUTION = NOT_RESUMED
```

Historical compatibility note: `CURRENT_NEXT = RUN_COMMAND_VERTICAL_SLICE_EXECUTION` was the retained pre-pause execution router after the 2026-08-24 scoped implementation approval. It is not the current project gate; the current Gate is maintained in the current work-order block below.

The 2026-08-25 visual Decision does not cancel the retained orchestration architecture, but this closeout does not resume or complete that implementation.

## Current work order

```text
COMPLETED = WORLD / CONTENT / BALANCE_ENVELOPE / TEXT_UX
COMPLETED = RETAINED_3X3 / TOKEN / LOWER_DECK / ROULETTE_DDD
COMPLETED = ORCHESTRATION_FIRST_VERTICAL_SLICE_ARCHITECTURE_AND_EXECUTION_PACKET
COMPLETED = FRONT_STATE_MINIMAP_SD_FANTASY_VISUAL_DECISION
COMPLETED = OM_IMG_023_USER_APPROVAL
COMPLETED = NOTION_HOME_AND_VISUAL_BIBLE_IMAGE_READBACK
COMPLETED = DURABLE_VISUAL_ASSET_RECORD_AND_NEW_CHAT_HANDOFF
COMPLETED = SHIELD_GUARD_IDLE_PAIR_USER_APPROVAL_AND_DUAL_STORAGE
COMPLETED = UNIT_ANIMATION_PRODUCTION_CONTRACT
COMPLETED = SHIELD_GUARD_CLEANUP_MASTER_PAIR_APPROVAL
COMPLETED = P0_UNITS_BUILDINGS_SOURCE_BATCH_APPROVAL
PROJECT_STATE = PAUSED_AT_BATCH_EDGE_CLEANUP_APPROVAL_GATE
CURRENT_NEXT = USER_EXPLICIT_BATCH_EDGE_CLEANUP_AND_MASTER_EXPORT_APPROVAL
IMAGE_GENERATION = USER_REQUEST_ONLY
GODOT_CODEX = BLOCKED_UNTIL_B_SCOPE_ASSETS_ARE_IMPLEMENTATION_READY
```

## GitHub work-item rule

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

Open/draft work not owned by the current task remains read-only. Fresh GitHub state always wins over old PR numbers in historical documents.

## Resume

1. fresh Base + fresh OMENWARD `main`/PR/Issue;
2. this Decision index;
3. `docs/ACTIVE_CONTEXT.md`;
4. `docs/HANDOFF_CONTEXT.md`;
5. `docs/handoffs/2026-08-26-gpt-work-image-production-handoff.md`;
6. `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md`;
7. current visual spec + approved visual asset record;
8. Notion Home + Visual Bible + Visual Components + full-resolution Drive image;
8. current GDD/Project Core + relevant owners, treating conflicting older visual wording as superseded by the 2026-08-25 Decision;
9. Google Sheet only as compatibility/history;
10. only resume runtime/code work or image generation after an explicit user request and fresh authority/readback.
