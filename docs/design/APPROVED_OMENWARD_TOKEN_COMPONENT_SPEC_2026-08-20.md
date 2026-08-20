# [현행] OMENWARD · Roulette Token Component Spec

```yaml
decision_id: OMW-PLAN-20260820-TOKEN-COMPONENT-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_WORK_ORDER_AND_ROLE_READABLE_TOKEN_DIRECTION
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01
  - OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01
preserves:
  - OMW-AMEND-20260804-HUD-ROULETTE-LAYOUT-AND-BATTLEFIELD-VIEW-V1
runtime_mutation: NONE
scene_mutation: NONE
human_validation: NOT_RUN
```

## 1. 결정

룰렛 병종 토큰은 **실제 인게임 Anime Pixel 병종 아트를 그대로 재사용하되, 작은 3×3 타일에서 역할이 먼저 읽히도록 Role-Anchor Crop을 사용**한다.

```text
SOURCE_ART = ACTUAL_GAME_UNIT_ART
TOKEN_EXCLUSIVE_CHARACTER_ART = FORBIDDEN_BY_DEFAULT
ABSTRACT_WEAPON_ONLY_ICON = NOT_DEFAULT
ROLE_SILHOUETTE_FIRST = TRUE
T1_T2_TOKEN_ART = ALLOWED
T3_TOKEN_ART = FORBIDDEN
```

Gold Token도 실제 게임 Gold 자산을 같은 타일 규격으로 재사용한다.

## 2. 대안 검토

### A · Actual Unit Art + Role-Anchor Crop — 채택

- 실제 병종 sprite/approved unit art를 crop한다.
- 얼굴보다 대표 무기/방패/날개/체급을 먼저 읽게 한다.
- Token → Result → Storage → Commit → Battlefield의 시각 연속성이 가장 강하다.

### B · Full-body Miniature — 비채택

전체 캐릭터를 32~34px 타일 안에 다 넣으면 얼굴/무기/실루엣이 동시에 작아져 병종 판독성이 떨어진다.

### C · Abstract Emblem / Weapon Icon — 비채택

작은 크기 판독은 좋지만 캐릭터 매력과 actual-unit continuity가 약해지고 기존 승인 자산 재사용 규칙과 충돌한다. 도움말/필터용 보조 아이콘은 별도 허용 가능하지만 기본 Token을 대체하지 않는다.

## 3. 공통 타일 planning envelope

3×3 component와 동일 reference를 사용한다.

```text
REFERENCE = 960×540
TOKEN_TILE = 32~34 px exploration
INNER_SAFE_ART = 26~29 px exploration
FRAME_THICKNESS = 1~2 px exploration
```

이 수치는 North Star/Vertical Slice 검증용이며 final runtime geometry가 아니다.

## 4. Crop hierarchy

한 타일에서 읽히는 순서:

```text
1. ROLE ANCHOR
2. BODY / MOUNT / WING SILHOUETTE
3. FACE / HEAD IDENTITY
4. TIER MARKER
5. DECORATION
```

Role anchor는 safe art 영역의 약 `40~60%` 폭/질량을 차지하는 것을 탐색 기준으로 둔다.

- 얼굴만 크게 보여주는 portrait crop은 기본값이 아니다.
- 장비가 프레임 밖으로 잘려 병종이 모호해지는 crop은 실패다.
- 작은 장신구/천/광택은 제거하거나 단순화할 수 있으나 새 캐릭터를 그리지 않는다.

## 5. 병종별 Role Anchor

| Token family | 1차 판독 앵커 | Crop 우선 |
|---|---|---|
| `BASIC_INFANTRY` | 한손검 + 소형 방패/헬멧 | 상체 + 검/방패 |
| `SHIELD` | 큰 방패 면적 | 방패 + 머리/상체 |
| `GREATSWORD` | 큰 양손검 | 대각 검 + 상체 |
| `SPEAR` | 긴 창 | 창날 + 긴 shaft + 상체 |
| `ARCHER` | 활/석궁 arc | 활/석궁 + 상체 |
| `CAVALRY` | 말 + 탑승 실루엣 | mount head/body + rider |
| `MAGE` | 지팡이/구체 | 지팡이/구체 + 얼굴 |
| `PRIEST` | 성직 지팡이/인장 | staff/sigil + 상체 |
| `ASSASSIN` | 짧은 이중 무기/후드 | twin blades + hood |
| `FLYING_UNIT` | 큰 날개 | wingspan + 몸통 |
| `GIANT` | 해머 + 대형 갑주 | hammer head + large torso |

Role anchor가 작은 크기에서 사라지면 얼굴/장식을 더 줄여 앵커를 키운다.

## 6. T1 / T2 표현

기존 계약대로 Roulette Token은 T1/T2 actual unit art까지만 사용한다.

```text
TOKEN_TIER_ALLOWED = T1 / T2
TOKEN_TIER_T3 = FORBIDDEN
```

Tier는 token art를 덮는 큰 배너가 아니라 작은 corner marker로 표현한다.

탐색 후보:

```text
T1 = 1 notch / I
T2 = 2 notches / II
MARKER_AREA = one corner only
```

색상만으로 Tier를 구분하지 않는다.

T1과 T2가 같은 계열임을 다음으로 유지한다.

- 핵심 무기/실루엣 유지.
- T2는 장비/복장/VFX를 확장하되 role anchor는 바꾸지 않는다.

## 7. Reward rarity와 Token Tier 분리

룰렛의 `일반 / 엘리트 / 영웅 / 전설`은 **최종 line count에서 결정되는 보상 등급**이지 Token 자체 희귀도가 아니다.

따라서 기본 Token에 다음을 금지한다.

```text
TOKEN_RARITY_COLORED_FRAME = FORBIDDEN
TOKEN_STAR_RARITY_BADGE = FORBIDDEN
GACHA_RARITY_GLOW = FORBIDDEN
```

선 완성 뒤 Result Preview에서 reward grade를 별도 표현한다.

## 8. Gold Token

```text
SOURCE_ART = same in-game gold image used by HUD/reward
TILE_GRAMMAR = same as unit tokens
TIER_MARKER = NONE
PREMIUM_CURRENCY_LOOK = AVOID
```

Gold art는 safe area의 약 `65~75%`를 채우는 큰 원형 실루엣을 탐색 기준으로 둔다.

- 별도 룰렛 전용 금화 문양을 만들지 않는다.
- 보석/현금상점/프리미엄 재화 느낌을 피한다.

## 9. X Token

X는 보상이 없는 빈 Token이다.

```text
X_READ = CLEAR_EMPTY_NON_REWARD
X_FLASHY_FAILURE = FORBIDDEN
```

- unit/gold art와 혼동되지 않는 어두운 empty sigil / X rune을 사용한다.
- 실패를 벌주는 빨간 경고 카드처럼 과장하지 않는다.
- 중앙줄 X 3개도 보상이 아니므로 reward-line glow를 사용하지 않는다.

## 10. Token state overlays

Token art를 가리지 않는 최소 상태만 허용한다.

```text
NORMAL
FOCUS / HOVER
MOVE_PREVIEW_SOURCE
MOVE_PREVIEW_DESTINATION
JUDGING_SYMBOL
COMPLETED_LINE
```

원칙:

- 상태는 frame/outline/underlay로 표현한다.
- sprite 위를 큰 아이콘/텍스트로 덮지 않는다.
- judging symbol/line lock 연출은 DDD spec에서 timing을 별도 확정한다.

## 11. 결과 화면 연속성

```text
Roulette Token
→ larger Result Preview
→ Storage card
→ Commit card
→ Battlefield unit
```

같은 캐릭터/병종 시각 계보를 유지한다.

Result Preview는 실제 지급 Tier/등급의 큰 인게임 아트를 사용하며, Roulette Token의 T1/T2 제한과 혼동하지 않는다.

## 12. Internal metadata boundary

기본 Token 표면에서 숨김:

```text
source_building_instance_id
internal token_instance_id
board weight
source weight
exact probability debug metadata
```

요청 시 상세/Debug에서만 확인한다.

## 13. Benchmark adaptation

채택 원리:

- Into the Breach: 최소 정보와 명확한 pixel silhouette로 tactical state를 읽는 원리.
- The King is Watching: pixel-graphic strategy에서 소규모 화면 요소와 군대/운영 정보를 함께 읽는 원리.

비채택:

- 타 게임 캐릭터/아이콘 형태 복제.
- 독립 gacha rarity frame.
- unit art와 동떨어진 별도 token-only 캐릭터.

## 14. 검증

다음 크기/상태에서 token sheet를 비교한다.

```text
32 px reference tile
34 px reference tile
2× presentation scale
3×3 board full view
selected / preview / completed-line states
```

PASS 후보:

- 이름 없이 병종 역할을 대부분 구분할 수 있음.
- T1/T2 계열 연속성이 보임.
- Gold와 X가 즉시 구분됨.
- state overlay가 role anchor를 가리지 않음.
- 실제 Battlefield unit과 같은 병종임을 알아볼 수 있음.
- AI-generated token-only look가 생기지 않음.

## 15. 다음 작업 순서

```text
COMPLETE = TOKEN_COMPONENT_SPEC
CURRENT_NEXT = LOWER_CONTROL_DECK_SPEC
THEN = ROULETTE_DDD_FEEDBACK_SPEC
THEN = NEW_NORTH_STAR_ONE_IMAGE
THEN = COMPONENT_SHEET
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
THEN = IMPLEMENTATION_HANDOFF_AFTER_USER_AUTHORITY
```

## 16. 경계

```text
PRODUCT_CODE = UNCHANGED
ASSET_PRODUCTION = NOT_STARTED
SCENE = UNCHANGED
RUNTIME = NOT_RUN
HUMAN_VALIDATION = NOT_RUN
FINAL_TOKEN_PIXEL_GEOMETRY = NOT_APPROVED_AS_RUNTIME_NUMERICS
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```
