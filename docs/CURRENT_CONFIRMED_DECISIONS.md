# OMENWARD · Current Confirmed Decisions

```yaml
updated_at: 2026-08-20
status: CURRENT_DECISION_RECOVERY_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_reopened_at: 2026-08-20
current_planning_track: WORLD_STORY_CONTENT_BALANCE_TEXT_UX_VISUAL_REPLAN
adversarial_review_decisions_1_to_6: CLEAN_REVIEW_EXIT
adversarial_review_full_loop_count: 6
runtime_evidence_ceiling: NOT_CHANGED_BY_THIS_INDEX
human_play_evidence: NOT_RUN
visual_style: ANIME_PIXEL_ART_UNITS_PLUS_CLEAN_PIXEL_BATTLEFIELD
visual_generation: USER_REQUEST_ONLY
```

이 문서는 현재 승인 Decision을 새 채팅에서 빠르게 복원하기 위한 인덱스다. 상세 규칙은 각 Decision owner가 책임지고, Notion은 사람용 전체 그림/Flow/비교표를 책임진다. code/data/scene/test/runtime evidence는 repository truth가 책임진다.

## 2026-08-20 재기획 승인 Decision

| Decision ID | 승인 핵심 | Repository owner | 상태 |
|---|---|---|---|
| `OMW-PLAN-20260820-WORLD-ROLE-01` | 플레이어는 `징조수호관(Omen Warden)`이며 룰렛은 도박이 아니라 군사적 확률/동원 장치다. | `docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-MAPRUN-WORLD-01` | 한 MapRun = 한 Ward Citadel + 20 Stage Omen Cycle. | `docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-PRESSURE-LANGUAGE-01` | 5 Pressure는 적 종족이 아니라 복합 가능한 Omen Signature다. | `docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01` | 자동생산과 TokenSource는 별도 획득 경로이며 세 징조륜은 세 전선과 1:1 대응하지 않는다. | `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-FIRST5-FTUE-01` | Stage 1~5 = 인과 이해 → 미래 수정 → 순간 개입 → 응용 시험 → 첫 결산. | `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01` | Run Command Screen = PREPARE → COMMIT → BATTLE → REVIEW Focus Mode. | `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01` | Veil은 적 종족이 아닌 적대적 경계현상이며 20 Stage는 지역 수렴기다. | `docs/design/APPROVED_OMENWARD_VEIL_CONVERGENCE_FRONT_AND_CORE_STORY_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-CONTENT-BOSS-ARC-01` | 20 Stage = 4×5 authored spine; Boss 5/10/15/20 = Priority/Route/Stance/Sequential Synthesis. | `docs/design/APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-BALANCE-BUDGET-01` | 최종 숫자보다 `SE / ME / TU + Threat Vector` normalized envelope를 먼저 사용한다. | `docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md` + `docs/analysis/balance/current_normalized_balance_budget.v1.json` | CONFIRMED |
| `OMW-PLAN-20260820-TEXT-UX-STATE-01` | 각 Mode는 하나의 질문/Primary CTA를 우선하고 COMMIT은 staged plan 후 atomic irreversible confirm을 사용한다. | `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md` + `docs/analysis/ui/current_text_ux_state_contract.v1.json` | CONFIRMED |
| `OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01` | 캐릭터/유닛 = Anime Pixel Art, 전장/배경 = Clean Pixel Art. 전장 메인/하단 보조, 3×3 룰렛+행·열 화살표, 병종/Gold Token을 보호한다. | `docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-BATTLEFIELD-SCALE-READABILITY-01` | 유닛 크기에서 길 폭을 역산해 2~3열 교전이 읽히는 넓은 길과 full-three-lane 기본 카메라를 사용한다. | `docs/design/APPROVED_OMENWARD_BATTLEFIELD_SCALE_AND_COMBAT_READABILITY_2026-08-20.md` + `docs/analysis/visual/current_battlefield_scale_readability.v1.json` | CONFIRMED |
| `OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01` | 낮은 하단에서 `3×3 + 각 열 상·하 + 각 행 좌·우` 직접 화살표 작업대를 사용한다. Hover/focus는 preview, 실행은 이동권 소비 후 즉시 확정이며 중앙 가로줄 판정과 기존 line reward를 보존한다. | `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md` + `docs/analysis/ui/current_3x3_roulette_component.v1.json` | CONFIRMED |
| `OMW-PLAN-20260820-TOKEN-COMPONENT-01` | 실제 Anime Pixel 병종 아트를 재사용하고 작은 타일에서는 역할 앵커가 먼저 읽히게 crop한다. T1/T2 token art만 사용하고 reward rarity와 token tier를 분리하며 Gold/X도 같은 tile grammar를 사용한다. | `docs/design/APPROVED_OMENWARD_TOKEN_COMPONENT_SPEC_2026-08-20.md` + `docs/analysis/ui/current_token_component.v1.json` | CONFIRMED |

## 보호되는 제품 정체성

```text
건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.

징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
→ 다음 설계
```

보호:

- `ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE`
- `GAMBLING_FANTASY_POSITIONING = FORBIDDEN`
- `PAID_SPIN = FORBIDDEN`
- 자동생산과 TokenSource 별도 경로.
- 세 릴 ↔ 세 전선 고정 대응 금지.
- 최종 commit 이후 recall/sell/cross-lane 이동 금지.
- `Veil ≠ Pressure ≠ 단일 적 종족`.
- Boss Stage = 5/10/15/20.
- 모든 Stage final-wave Elite.
- `DANGER_STAGE_TYPE = REMOVED`.
- Forecast/REVIEW가 정답 빌드를 지시하지 않음.
- 최종 제품 수치는 simulation/runtime/human evidence 전 승인하지 않음.
- player-experience PASS는 release-near Vertical Slice 사람 플레이 전까지 금지.

## Visual current contract

```text
CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART
BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART
PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
BATTLEFIELD_HEIGHT_EXPLORATION = 68~75%
LOWER_DECK_HEIGHT_EXPLORATION = 25~32%
ROULETTE_EXPOSURE = 3×3
ROW_COLUMN_ARROWS = PROMINENT
GOLD_TOKEN = SUPPORTED
DUPLICATE_LOWER_RESOURCE_DISPLAY = FORBIDDEN
```

Battlefield planning envelope:

```text
REFERENCE = 960×540
COMMON_UNIT_VISUAL_HEIGHT = 30~36 px exploration
COMMON_FOOTPRINT_WIDTH = 18~22 px exploration
ROAD_USABLE_WIDTH = 60~72 px exploration = 2.75~3.25× footprint
LATERAL_RANK_TARGET = 2~3
LANE_CENTER_SPACING = 105~125 px exploration
CLASH_NODE = 78~96 px exploration
DEFAULT_CAMERA = FULL_THREE_LANES_VISIBLE
```

3×3 roulette component planning envelope:

```text
ROULETTE_FOCUS_LOWER_DECK = 28~32%
TOKEN_TILE = 32~34 px exploration
BOARD_ONLY = 100~108 px exploration
BOARD_PLUS_ARROWS_HEIGHT = 146~154 px exploration
ARROWS = 12 direct target/direction controls
PREVIEW = hover/focus without spend
EXECUTE = immediate spend + committed move
UNDO_AFTER_MOVE = FORBIDDEN
PRIMARY_JUDGING_LINE = CENTER_HORIZONTAL_ROW
```

Token planning contract:

```text
SOURCE_ART = ACTUAL_GAME_UNIT_ART
TOKEN_TILE = 32~34 px exploration
INNER_SAFE_ART = 26~29 px exploration
READ_ORDER = ROLE_ANCHOR → SILHOUETTE → FACE → TIER → DECORATION
T1_T2_TOKEN_ART = ALLOWED
T3_TOKEN_ART = FORBIDDEN
TOKEN_RARITY_FRAME = FORBIDDEN
GOLD_TOKEN_USES_GAME_GOLD_ART = TRUE
X_TOKEN = CLEAR_EMPTY_NON_REWARD
```

이 값들은 North Star/Vertical Slice 검증용 planning envelope이며 런타임 최종 수치가 아니다.

## Balance open reconciliation

```text
analysis baseline = base 3/20s + Vault 3/20s + foundation 250
current main observation = base 5/20s + control 4/60s + outpost 2/30s + StageDefinition default 160
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

## Current work order

```text
COMPLETED = BATTLEFIELD_SCALE_AND_ROAD_WIDTH_PLANNING_CONTRACT
COMPLETED = 3X3_ROULETTE_COMPONENT_SPEC
COMPLETED = TOKEN_COMPONENT_SPEC
CURRENT_NEXT = LOWER_CONTROL_DECK_SPEC
THEN = ROULETTE_DDD_FEEDBACK_SPEC
THEN = NEW_NORTH_STAR_ONE_IMAGE
THEN = COMPONENT_SHEET
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
THEN = IMPLEMENTATION_HANDOFF_AFTER_EXPLICIT_USER_AUTHORITY
```

## Current GitHub work-item truth

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

## 재개 규칙

1. fresh `main`과 이 인덱스를 먼저 읽는다.
2. 기존 CONFIRMED Decision은 같은 질문을 다시 묻지 않는다.
3. `docs/ACTIVE_CONTEXT.md`를 읽는다.
4. Visual 작업 시 visual style/component + battlefield scale + 3×3 roulette + Token owner를 함께 읽는다.
5. 진행 중 open/draft PR은 별도 workstream으로 읽기 전용 처리한다.
6. runtime/사람 검증을 수행하지 않은 항목은 `NOT_RUN / UNVERIFIED`를 유지한다.
7. Balance 구현 전에 economy drift를 fresh main/runtime 대상으로 재대조한다.
