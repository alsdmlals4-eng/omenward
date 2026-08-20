# [현행] OMENWARD · Visual Style & Component Contract

```yaml
decision_id: OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_EXPLICIT_STYLE_APPROVAL_AND_COMPONENT_DIRECTION
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
runtime_mutation: NONE
scene_mutation: NONE
product_data_mutation: NONE
human_validation: NOT_RUN
```

## 1. 확정 그림체

OMENWARD의 기본 시각 방향은 다음 조합으로 잠근다.

```text
CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART
BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART
UI_STYLE = DARK_NAVY_CHARCOAL_PIXEL_FRAME + RESTRAINED_GOLD_TRIM
```

- 캐릭터와 전투 유닛은 애니메 픽셀 아트 기반으로 제작한다.
- 전장·지형·건물 배경은 클린 픽셀 아트로 정리해 병력 전투 가독성을 우선한다.
- painterly blur, 과도한 미세 장식, 혼합 해상도 느낌을 기본 표현으로 사용하지 않는다.
- 캐릭터 매력도는 살리되 전장 줌에서 병종 실루엣이 얼굴 디테일보다 먼저 읽혀야 한다.

## 2. 시각 우선순위

OMENWARD의 화면 주인공은 **전장**이다. 룰렛과 하단 조작면은 핵심 재미를 강화하는 보조 인터페이스다.

```text
PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
BATTLEFIELD_HEIGHT_TARGET = 68_TO_75_PERCENT_EXPLORATION
LOWER_DECK_HEIGHT_TARGET = 25_TO_32_PERCENT_EXPLORATION
```

위 비율은 최종 절대 규격이 아니라 16:9 North Star/960×540 축소 검증용 탐색 범위다.

- 이전 대형 하단 시안 대비 하단 점유를 약 절반 수준으로 줄이는 방향을 우선한다.
- 세 전선 전체가 기본 전략 줌에서 보이게 한다.
- 길 폭을 넓혀 같은 전선 안에서 여러 유닛이 싸우는 장면을 읽기 쉽게 만든다.
- 지형 장식은 길·전선·거점·병력 판독보다 앞서지 않는다.
- 미니맵은 기본값에서 요구하지 않는다.

## 3. 전장 컴포넌트

### 3.1 Battlefield Viewport

필수 요소:

```text
ALLY_CITADEL = LEFT
VEIL_SIDE = RIGHT
LANES = TOP / MID / BOTTOM
WIDE_COMBAT_ROADS = REQUIRED
CLASH / DECISION NODES = LARGE_READABLE_LANDMARKS
FULL_THREE_LANE_CONTEXT = REQUIRED
```

- 전투 유닛 간 간격과 길 폭은 공격/피격/VFX를 봐도 병종 구분이 유지되게 한다.
- 아군은 상아/청색/남색/절제된 금속, Veil 측은 흑자색/암적색/갑각 회색/제한적 균열광 대비를 사용한다.
- Veil 색채는 세계 현상/적 진영 표현이며 `Veil = 단일 적 종족`으로 고정하지 않는다.

### 3.2 Battlefield HUD

상단/전장 위에만 유지할 정보:

```text
STAGE / WAVE
PREPARE_OR_MAINTENANCE_TIMER
GOLD
MANA_OR_CURRENT_SECONDARY_RESOURCE
TROOP_LIMIT
SPEED / PAUSE / SETTINGS
FORECAST_SUMMARY_WHEN_RELEVANT
```

하단에 같은 자원 수치를 다시 복제하지 않는다.

```text
DUPLICATE_RESOURCE_DISPLAY_IN_LOWER_DECK = FORBIDDEN
```

## 4. 3×3 룰렛 컴포넌트

OMENWARD의 player-facing 룰렛 조작면은 **3×3 노출창**을 유지한다.

```text
ROULETTE_EXPOSURE = 3_BY_3
ROW_ARROW_CONTROLS = PROMINENT
COLUMN_ARROW_CONTROLS = PROMINENT
ONE_BY_N_CAROUSEL_REPLACEMENT = FORBIDDEN
```

세계관/시스템에서는 세 징조륜이 하나의 중앙 삼중 동원 장치이며, player-facing 결과/조작면은 3×3 노출창으로 읽힌다.

- 행/열 화살표는 룰렛 조작의 핵심 시각 affordance다.
- 화살표는 토큰보다 시각적으로 사라지지 않게 충분한 크기/대비를 갖는다.
- 세 릴을 세 전선과 1:1로 대응시키지 않는다.
- 카지노 슬롯 레버/7/체리/잭팟 문법은 사용하지 않는다.

## 5. Token Component

병종 토큰은 **병종이 즉시 보이는 것**이 1순위다.

```text
TOKEN_PRIMARY_READ = UNIT_ROLE_SILHOUETTE
TOKEN_SECONDARY_READ = FACTION / TIER / RARITY
FACE_DETAIL_PRIORITY = LOW_AT_SMALL_SIZE
```

병종 식별 앵커 예:

- 방패병 = 큰 방패 면적.
- 대검병 = 큰 양손검과 넓은 공격 실루엣.
- 창병 = 긴 수평/대각 창.
- 궁병 = 활/석궁의 명확한 외곽선.
- 기병 = 말 + 탑승 실루엣.
- 마도사 = 지팡이/구체.
- 사제 = 지팡이/성직 표식.
- 암살자 = 짧은 이중 무기/민첩 실루엣.
- 비행병 = 큰 날개.
- 거인 = 다른 토큰보다 체급이 느껴지는 해머/대형 갑주 실루엣.

Token tile 자체의 프레임 규격은 통일한다. Tier/등급 때문에 병종 실루엣을 가리지 않는다.

## 6. Gold Token

금화 토큰은 룰렛의 정식 토큰 종류로 유지한다.

```text
GOLD_TOKEN = REQUIRED_SUPPORTED_TOKEN
GOLD_TOKEN_PREMIUM_CURRENCY_LOOK = AVOID
```

- 다른 병종 토큰과 같은 타일 규격 안에 들어간다.
- 큰 금화 실루엣으로 즉시 판독한다.
- 과도한 보석/현금상점/유료 재화 문법을 사용하지 않는다.

## 7. 하단 Control Deck 컴포넌트

하단은 전장의 보조이며, 현재 Focus Mode에 필요한 조작만 우선 노출한다.

핵심 컴포넌트 후보:

```text
LOWER_DECK_SHELL
MOVE_TICKET_PANEL
ROULETTE_3X3_BOARD
ROW_CONTROLS
COLUMN_CONTROLS
SPIN_CONTROL
RESULT_CONFIRM_CONTROL
STORAGE_TAB
BUILD_TAB
TACTICAL_TAB
OMEN_WHEEL_OR_ROULETTE_TAB
OPTIONAL_GUIDE_CHARACTER_PANEL
```

- 자원 정보는 상단에 있으므로 하단에서 반복하지 않는다.
- PREPARE/COMMIT/BATTLE/REVIEW에 따라 하단 패널 구성을 바꾸되 전장 뷰포트 크기를 불필요하게 다시 줄이지 않는다.
- 룰렛이 활성 Focus일 때는 3×3 보드와 화살표가 하단에서 가장 중요한 조작 요소다.

## 8. Roulette DDD / 뽕맛 계약

룰렛의 보상감과 기대감은 OMENWARD의 핵심 DDD 요소다. 단, 도박 판타지가 아니라 **내가 설계한 동원 확률이 실제 병력으로 변환되는 순간의 쾌감**으로 연출한다.

허용/권장 피드백:

```text
PRE_SPIN_BUILDUP
WHEEL / TOKEN MOTION
ROW_COLUMN_MANIPULATION_FEEDBACK
MATCH_LINE_LOCK_OR_HIGHLIGHT
OMEN_SIGIL_LIGHTUP
RESULT_SNAP
UNIT_TOKEN_REVEAL
REWARD_TO_STORAGE_OR_COMMIT_TRANSFER
BATTLEFIELD_REINFORCEMENT_LINK_FEEDBACK
SOUND / VFX / MICRO_CAMERA_PUNCH_WITH_LIMITS
```

금지:

```text
CASINO_JACKPOT_LANGUAGE
PAID_SPIN_FANTASY
REAL_MONEY_REWARD_CUES
SCREEN_OBSCURING_EXCESSIVE_FLASH
LONG_UNSKIPPABLE_REWARD_SEQUENCE
```

룰렛 뽕맛은 전장을 대체하지 않고 `전장 준비 → 룰렛 조작/기대 → 결과 획득 → 전선 커밋` 인과를 강화해야 한다.

## 9. 컴포넌트 상태 분류

```text
STYLE_LOCK = CONFIRMED
BATTLEFIELD_PRIMARY_HIERARCHY = CONFIRMED
ANIME_PIXEL_UNITS = CONFIRMED
CLEAN_PIXEL_BACKGROUND = CONFIRMED
3X3_ROULETTE = CONFIRMED_EXISTING_CORE
ROW_COLUMN_ARROWS_IMPORTANT = CONFIRMED
UNIT_ROLE_READABLE_TOKENS = CONFIRMED
GOLD_TOKEN_SUPPORT = CONFIRMED
NO_DUPLICATE_LOWER_RESOURCES = CONFIRMED
LOWER_DECK_EXACT_LAYOUT = NOT_FINAL
GUIDE_CHARACTER_FINAL_DESIGN = NOT_FINAL
EXACT_PIXEL_RESOLUTION_PER_ASSET = NOT_FINAL
EXACT_VFX_TIMING = NOT_FINAL
```

## 10. 현재 생성 이미지의 지위

최근 애니메 픽셀 + 클린 픽셀 예시 화면과 컴포넌트 정리 보드는 **style/reference evidence**로만 사용한다.

- 그림체 방향은 승인됐다.
- 보드 안 실제 하단 배치, 텍스트, 캐릭터/건물 개별 외형, 잘못 표현된 룰렛 구조는 최종 UI 정본이 아니다.
- 향후 North Star는 이 계약을 사용해 `넓은 전장 + 3×3 룰렛 + prominent arrows + compact lower deck`으로 다시 제작한다.

## 11. 다음 Gate

```text
NEXT_VISUAL_WORK = COMPONENT_LEVEL_REFERENCE_AND_NORTH_STAR_REBUILD
IMAGE_GENERATION = USER_REQUEST_ONLY
RUNTIME_IMPLEMENTATION = NOT_AUTHORIZED
HUMAN_USABILITY = NOT_RUN
```
