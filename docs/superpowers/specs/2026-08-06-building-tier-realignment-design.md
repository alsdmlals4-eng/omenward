# OMENWARD 건물 Tier 구조 재정렬 설계

```yaml
decision_id: OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1
parent_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
approval: USER_APPROVED
planning_checkpoint: PARTIAL_APPROVAL_6_OF_10
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 목표

기존의 `모든 건물 T2 A/B 분기` 문법을 폐기하고, 건물의 실제 기능에 맞춰 다음 세 종류로 재구성한다.

1. 병종 전문화 건물
2. 전투 역할 전문화 건물
3. 기존 기능 직선 강화 건물

정확 비용·생산시간·확률·수치·T3 효과는 이 설계에서 확정하지 않는다.

## 2. 현행 기본 건물 구성

```text
금고
농장
일반병 병영
특수병 병영
방어탑
지휘소
마력탑
```

기본 건물 종류는 7종이다. 첫 MapRun Stage 1의 필수 기초 세트는 다음 6종으로 유지한다.

```text
금고 / 농장 / 일반병 병영 / 방어탑 / 지휘소 / 마력탑
```

특수병 병영은 Stage 1 의무 건물이 아니다. 특수병 투자 시점에 선택적으로 건설한다.

## 3. 일반병 병영

```text
일반병 병영 T1
= 기본 보병 자동생산
+ 기본 보병 TokenSource 공급
```

```text
일반병 병영 T2
├─ 방패병 병영
├─ 대검병 병영
├─ 창병 병영
├─ 궁병 병영
└─ 기병 병영
```

각 T2 전문 병영은 다음 두 기능을 함께 가진다.

```text
선택한 일반 병종 자동생산
+ 선택한 일반 병종 TokenSource 공급
```

다른 일반병 병영 인스턴스는 서로 다른 T2 병종으로 전문화할 수 있다. T3의 정확한 병종 강화 방식은 별도 결정으로 남긴다.

## 4. 특수병 병영

특수병은 일반병보다 기능이 강하고 전문적이지만 자동생산 시간이 더 길다.

```text
특수병 병영 T1
= 마도사 / 사제 / 암살자 / 비행병 / 거인 중 하나를 무작위 자동생산
+ TokenSource 공급 없음
```

```text
특수병 병영 T2
├─ 마도사 병영
├─ 사제 병영
├─ 암살자 병영
├─ 비행병 병영
└─ 거인 병영
```

각 T2 전문 병영은 다음 두 기능을 함께 가진다.

```text
선택한 특수 병종 자동생산
+ 선택한 특수 병종 TokenSource 공급
```

특수병 T1의 무작위 선정 시점, 결과 공개 시점, 중복 가중치와 정확 생산시간은 시뮬레이션·UX 결정 전까지 확정하지 않는다.

## 5. 방어탑

```text
방어탑 T1
├─ T2 포격탑: 범위 공격
├─ T2 방어탑(방어 강화형): 방어력·내구 강화
└─ T2 저격탑: 긴 사거리
```

`방어탑(방어 강화형)`은 사용자 승인 기능명이며, T1 건물명과의 UI 중복을 해소할 최종 표시 이름은 별도 명칭 결정으로 남긴다. T3 역할과 정확 공격 규칙은 아직 확정하지 않는다.

## 6. 직선 강화 건물

다음 네 건물은 T2 분기를 만들지 않는다.

```text
금고 T1 → T2 → T3
농장 T1 → T2 → T3
지휘소 T1 → T2 → T3
마력탑 T1 → T2 → T3
```

Tier 상승은 새 전문 분기를 추가하는 대신 기존 기능을 강화한다.

- 금고: 기존 골드 관련 기능 강화
- 농장: 기존 병력 한도 관련 기능 강화
- 지휘소: 기존 전 아군 오라 강화
- 마력탑: 기존 마력 수급·연구 가능 Tier 강화

정확 증가량과 추가 효과는 수치 시뮬레이션 전 고정하지 않는다.

## 7. 룰렛·자동생산 계약

```text
GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY
GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY
GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT
GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT

SPECIAL_T1_AUTO_PRODUCTION = RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = NONE
SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT
SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT

SPECIAL_UNIT_FUNCTIONAL_POWER = STRONGER_THAN_GENERAL_UNIT
SPECIAL_AUTO_PRODUCTION_INTERVAL = LONGER_THAN_GENERAL_UNIT
```

자동생산과 TokenSource는 별개의 획득 경로다. 하나가 다른 하나를 대체하지 않는다.

## 8. 문서 수명주기

다음 기존 규칙은 이 결정으로 대체된다.

```text
모든 6종 건물 공통 A/B 분기 문법
금고 안정/행운 분기
농장 징집/예비 분기
병영 전열/기동 분기
방어탑 연사/포격 2분기
지휘소 돌격/수비 분기
```

다음 기존 문서는 증거로 보존하되 위 항목을 구현 입력으로 사용할 수 없다.

- `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- `docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md`
- `docs/reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md`

병종 정본의 `전열 병영 가중 / 기동 병영 가중` 구절과 전술 정본의 `연사탑` 참조도 이 결정의 새 병영·방어탑 구조에 맞춰 부분 대체된다. 병종 역할 자체와 전술 역할 자체는 유지한다.

마력탑의 `분기 금지 / T1→T2→T3 직선 강화`는 기존 전술·마력 정본과 일치하므로 유지한다.

## 9. 적대적 안전선

- 특수병 T1이 TokenSource를 제공해서 T2 전문화 가치를 잠식하면 실패다.
- 특수병이 일반병보다 기능도 강하고 생산도 빠르면 실패다.
- 자동생산과 룰렛 공급을 동일 이벤트로 취급하면 실패다.
- 직선 강화 건물에 승인되지 않은 신규 미니게임·분기·별도 자원을 추가하면 실패다.
- 방어탑 세 T2가 역할상 구분되지 않으면 실패다.
- T3 세부안을 이 결정에서 자동 확정하면 실패다.
- 정확 수치나 제품 구현을 문서 승인으로 간주하면 실패다.

## 10. 아직 미정인 항목

```text
GENERAL_AND_SPECIAL_EXACT_PRODUCTION_INTERVALS = PENDING_SIMULATION
SPECIAL_T1_RANDOM_SELECTION_TIMING = PENDING_DESIGN
SPECIAL_T1_RESULT_PREVIEW = PENDING_UX_DECISION
TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION
T2_EXACT_COSTS = PENDING_SIMULATION
T3_IDENTITIES_AND_EFFECTS = PENDING_GRILLME
DEFENSE_BRANCH_FINAL_DISPLAY_NAME = PENDING_NAMING
FIRST_STAGE2_T2_CANDIDATES = PENDING_GRILLME
STAGE2_GOLD_AND_LEFTOVER_POLICY = PENDING_GRILLME
```

## 11. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
