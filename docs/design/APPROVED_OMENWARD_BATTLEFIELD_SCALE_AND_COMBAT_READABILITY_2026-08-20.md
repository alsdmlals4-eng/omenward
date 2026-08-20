# [현행] OMENWARD · Battlefield Scale & Combat Readability

```yaml
decision_id: OMW-PLAN-20260820-BATTLEFIELD-SCALE-READABILITY-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_DIRECTION
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
  - OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01
runtime_mutation: NONE
scene_mutation: NONE
product_data_mutation: NONE
human_validation: NOT_RUN
exact_runtime_geometry: NOT_FINAL
```

## 1. 결정 요약

OMENWARD의 메인 화면은 전장이고, 하단 Control Deck은 보조다. 전투 가독성은 `유닛 크기 → 길 폭 → 접전지/전선 간격 → 카메라` 순서로 역산한다.

```text
PRIMARY = BATTLEFIELD
SECONDARY = LOWER_CONTROL_DECK
DEFAULT_CAMERA = FULL_THREE_LANE_CONTEXT
MINIMAP = NONE
```

현재 planning target:

```text
INTERNAL_REFERENCE = 960x540
BATTLEFIELD_HEIGHT = 68~75%
LOWER_DECK_HEIGHT = 25~32%
REFERENCE_BASELINE = 72% / 28%
```

이 비율은 제품 고정값이 아니라 North Star/Vertical Slice 가독성 검증용 범위다.

## 2. 대안 검토

### A · Combat-readable Wide Lanes — 채택

```text
ROAD_USABLE_WIDTH = 2.75~3.25 × COMMON_UNIT_COMBAT_FOOTPRINT
COMMON_UNIT_VISUAL_HEIGHT = 30~36 internal px exploration
COMMON_UNIT_COMBAT_FOOTPRINT_WIDTH = 18~22 internal px exploration
```

목표:
- 보통 체급 유닛이 한 길에서 2~3열로 엇갈려 교전하는 장면이 읽힌다.
- 공격/피격/VFX가 있어도 병종 silhouette가 유지된다.
- 3전선 전체를 한 화면에서 계속 본다.

### B · Cinematic Extra-wide Lanes — 비채택

```text
ROAD_USABLE_WIDTH ≈ 3.75~4.5 × COMMON_UNIT_COMBAT_FOOTPRINT
```

장점은 교전 장면이 화려하고 넓지만, 세 전선을 한 화면에 유지할 때 지형/거점/성채 대비가 약해지고 길 자체가 화면을 과점유한다.

### C · Compact Tactical Lanes — 비채택

```text
ROAD_USABLE_WIDTH ≈ 2.0~2.5 × COMMON_UNIT_COMBAT_FOOTPRINT
```

맵 맥락은 많이 남지만 다수 병력과 VFX가 겹칠 때 병종 판독과 애니메 픽셀 캐릭터 매력이 급격히 떨어질 위험이 있다.

## 3. 유닛 스케일 계약

### Common combatant

```text
VISUAL_HEIGHT_TARGET = 30~36 px @ 960x540 internal reference
FOOTPRINT_WIDTH_TARGET = 18~22 px
ROLE_SILHOUETTE_FIRST = TRUE
FACE_DETAIL_FIRST = FALSE
```

병종 인식은 얼굴보다 다음 요소가 우선한다.

```text
SHIELD = shield mass
GREATSWORD = two-hand sword
SPEAR = long spear
ARCHER = bow/crossbow
CAVALRY = mount silhouette
MAGE = staff/orb
PRIEST = cleric staff/sigil
ASSASSIN = twin short weapons
FLYING = wings
GIANT = large armor/hammer/scale
```

### Large units

```text
GIANT_VISUAL_SCALE = 1.35~1.60 × common exploration
BOSS_COMBAT_SCALE = 1.40~1.80 × common footprint exploration
```

Boss가 길 전체를 가려 다른 병종과 Route 정보를 읽지 못하는 크기는 금지한다.

## 4. 길 폭과 교전 밀도

```text
ROAD_USABLE_WIDTH_TARGET = 60~72 px @ 960x540 exploration
ROAD_EDGE_DECORATION = outside usable combat band
```

- 길의 시각 장식/난간/잔디 경계는 실제 교전 band를 침범하지 않는다.
- melee frontline 한 지점에서 2~3개 lateral rank가 생길 여유를 둔다.
- 병력 수가 많아져도 한 점에 전부 겹치게 하지 않고 길의 진행 방향으로 전투 cluster가 늘어진다.

Readability cluster target:

```text
LOCAL_ENGAGEMENT_READABILITY_TARGET = 8~12 visible combatants per immediate clash cluster
THIS_IS_NOT_A_GAMEPLAY_UNIT_CAP = TRUE
```

즉 한 전선 전체 병력 수를 제한하는 값이 아니라, 동일 화면 공간에 겹쳐 판독 불가해지는 것을 막는 시각/formation 목표다.

## 5. 전선 간격과 접전지

```text
LANE_CENTER_SPACING_TARGET = 105~125 px exploration
CLASH_NODE_DIAMETER = 1.25~1.45 × road usable width
CLASH_NODE_TARGET = 78~96 px exploration
```

- 상/중/하 lane VFX와 health/status marker가 서로 침범하지 않게 한다.
- 접전지는 길보다 넓어 `여기서 전선이 부딪힌다`는 landmark가 즉시 보인다.
- Clash node 안에서도 3전선 전체 카메라 맥락을 잃지 않는다.

## 6. 카메라 계약

```text
DEFAULT_STRATEGIC_ZOOM = FULL_THREE_LANES_VISIBLE
AUTO_COMBAT_ZOOM_THAT_HIDES_OTHER_LANES = FORBIDDEN
MINIMAP_REQUIRED = FALSE
```

기본 전투 중에는 줌 변화보다 highlight/outline/status cue를 우선한다.

장기 optional:

```text
MANUAL_INSPECT_ZOOM = OPTIONAL_NOT_REQUIRED
SHORT_MICRO_CAMERA_PUNCH = ALLOWED_WITH_LIMITS
```

단, 자동 카메라가 전투 중 다른 전선을 숨기거나 판단 맥락을 빼앗으면 금지한다.

## 7. VFX / UI occlusion guardrail

- 공격 이펙트는 병종 silhouette와 전선 방향을 지우지 않는다.
- lane label/forecast marker는 길 중앙 교전부를 가리지 않는다.
- 전투 HUD는 전장 가장자리/상단 오버레이를 우선하며 하단 Control Deck과 자원 정보를 중복하지 않는다.
- Boss telegraph는 크더라도 실제 위험 영역/Route를 읽을 수 있게 한다.

## 8. Benchmark adaptation

채택 원리:

- Mechabellum: formation/positioning이 전략의 핵심이므로 병력 배치와 전투 결과를 한눈에 읽을 수 있게 한다.
- Thronefall: 전투/건설 정보를 streamlined하게 유지해 핵심 행동을 시각 노이즈보다 앞세운다.
- Into the Breach: 위협 정보를 사전에 읽고 대응하게 하되 전투 공간 자체의 판독을 해치지 않는다.

비채택:

- 타 게임의 실제 unit size, camera zoom, lane width 숫자 직접 복제.
- cinematic camera가 플레이어 대신 전선을 선택하는 연출.
- 병종이 작아져 색점처럼만 보이는 초광각.

## 9. 검증 규칙

다음 세 해상도에서 같은 battle scene을 비교한다.

```text
960x540 internal reference
1280x720 validation
1920x1080 presentation
```

PASS 후보 조건:

```text
ALL_THREE_LANES_VISIBLE = TRUE
COMMON_UNIT_ROLE_SILHOUETTE_READABLE = TRUE
2_TO_3_LATERAL_RANKS_POSSIBLE = TRUE
CLASH_NODE_READABLE = TRUE
LOWER_DECK_DOES_NOT_DOMINATE = TRUE
VFX_DOES_NOT_ERASE_FORMATION = TRUE
```

Human readability/feel은 실제 release-near Vertical Slice 전까지 `NOT_RUN`이다.

## 10. 다음 작업 순서

```text
1. BATTLEFIELD_SCALE_AND_ROAD_WIDTH = CONFIRMED_DIRECTION
2. NEXT = 3X3_ROULETTE_COMPONENT_SPEC
3. THEN = TOKEN_COMPONENT_SPEC
4. THEN = LOWER_CONTROL_DECK_SPEC
5. THEN = ROULETTE_DDD_FEEDBACK_SPEC
6. THEN = NEW_NORTH_STAR_1_IMAGE
7. THEN = COMPONENT_SHEET
8. THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
9. THEN = IMPLEMENTATION_HANDOFF_AFTER_EXPLICIT_USER_AUTHORITY
```

## 11. 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_GEOMETRY = UNCHANGED
RUNTIME = NOT_RUN
HUMAN_VALIDATION = NOT_RUN
FINAL_PIXEL_GEOMETRY = NOT_APPROVED_AS_RUNTIME_NUMERICS
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```
