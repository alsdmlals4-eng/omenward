# [현행] OMENWARD 건물 Tier 구조 재정렬 정본

```yaml
decision_id: OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1
parent_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
approved_at: 2026-08-06 KST
approval: USER_APPROVED
status: CURRENT_BUILDING_TIER_AUTHORITY / NOT_IMPLEMENTED
planning_checkpoint: PARTIAL_APPROVAL_6_OF_10
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

기존의 `모든 기본 건물은 T2 A/B 두 분기` 문법은 현행 건물 구조와 맞지 않아 폐기한다. 건물마다 실제 역할에 따라 Tier 구조를 다르게 사용한다.

```text
병종 전문화 = 일반병 병영 / 특수병 병영
전투 역할 전문화 = 방어탑
직선 기능 강화 = 금고 / 농장 / 지휘소 / 마력탑
```

현행 기본 건물 종류는 다음 7종이다.

```text
금고 / 농장 / 일반병 병영 / 특수병 병영 / 방어탑 / 지휘소 / 마력탑
```

## 2. 첫 MapRun 기초 세트

Stage 1에서 반드시 설치하는 기초 T1 세트는 다음 6종이다.

```text
금고 / 농장 / 일반병 병영 / 방어탑 / 지휘소 / 마력탑
```

```text
FOUNDATION_REQUIRED_T1_COUNT = 6
SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE
```

특수병 병영은 초반 의무 세금이 아니라, 플레이어가 특수병 투자 필요성을 판단한 뒤 선택적으로 건설한다.

## 3. 일반병 병영

### T1 — 기본 보병

```text
GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY
GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY
```

- 일정 시간마다 기본 보병을 자동생산한다.
- 룰렛에 기본 보병 TokenSource를 공급한다.
- 자동생산과 룰렛 토큰 공급은 서로 다른 획득 경로다.

### T2 — 일반 병종 전문화

```text
일반병 병영 T1
├─ T2 방패병 병영
├─ T2 대검병 병영
├─ T2 창병 병영
├─ T2 궁병 병영
└─ T2 기병 병영
```

```text
GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT
GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT
```

- 선택한 일반 병종만 자동생산한다.
- 선택한 일반 병종의 TokenSource를 룰렛에 공급한다.
- 다른 일반병 병영 인스턴스는 다른 병종으로 전문화할 수 있다.
- T3 병종 강화 방식은 별도 승인 전까지 확정하지 않는다.

## 4. 특수병 병영

특수병은 일반병보다 강한 기능과 전문 역할을 제공하지만 자동생산 간격이 더 길다.

```text
SPECIAL_UNIT_FUNCTIONAL_POWER = STRONGER_THAN_GENERAL_UNIT
SPECIAL_AUTO_PRODUCTION_INTERVAL = LONGER_THAN_GENERAL_UNIT
```

### T1 — 무작위 특수병 자동생산

```text
SPECIAL_T1_AUTO_PRODUCTION = RANDOM_SPECIAL_UNIT
SPECIAL_T1_POOL = MAGE / PRIEST / ASSASSIN / FLYING_UNIT / GIANT
SPECIAL_T1_TOKEN_SOURCE = NONE
```

- 마도사·사제·암살자·비행병·거인 중 하나를 무작위로 자동생산한다.
- T1 특수병 병영은 룰렛에 어떤 특수병 TokenSource도 공급하지 않는다.
- 무작위 선정 시점과 결과 공개 시점은 아직 확정하지 않는다.

### T2 — 특수 병종 전문화

```text
특수병 병영 T1
├─ T2 마도사 병영
├─ T2 사제 병영
├─ T2 암살자 병영
├─ T2 비행병 병영
└─ T2 거인 병영
```

```text
SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT
SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT
```

- 선택한 특수 병종만 자동생산한다.
- 선택한 특수 병종의 TokenSource를 룰렛에 공급한다.
- 긴 자동생산 간격이라는 기회비용은 T2에서도 유지한다.
- 정확 생산 간격과 토큰 가중치는 시뮬레이션 전 확정하지 않는다.

## 5. 방어탑

방어탑은 세 가지 T2 역할로 전문화한다.

```text
방어탑 T1
├─ T2 포격탑 = 범위 공격
├─ T2 방어탑(방어 강화형) = 방어력·내구 강화
└─ T2 저격탑 = 긴 사거리
```

### T2 포격탑

- 밀집된 다수 적을 공격하는 범위형 방어시설이다.
- 정확 범위·재장전·피해 수치는 시뮬레이션 후 결정한다.

### T2 방어탑(방어 강화형)

- 공격 전문화보다 건물 자체의 방어력·내구 유지에 집중한다.
- T1 `방어탑`과 표시 이름이 겹치므로 최종 인게임 명칭은 별도 명칭 결정으로 남긴다.

### T2 저격탑

- 긴 사거리로 먼 적 또는 고가치 표적에 대응한다.
- 정확 표적 우선순위·공격속도·사거리는 아직 확정하지 않는다.

T3 세부 역할은 별도 결정 전까지 확정하지 않는다.

## 6. 직선 기능 강화 건물

다음 네 건물은 T2 분기를 만들지 않는다.

```text
LINEAR_TIER_BUILDINGS = VAULT / FARM / COMMAND_POST / MANA_TOWER
LINEAR_T2_BRANCHING = FORBIDDEN
```

```text
금고 T1 → T2 → T3
농장 T1 → T2 → T3
지휘소 T1 → T2 → T3
마력탑 T1 → T2 → T3
```

- 금고: 기존 골드 관련 기능을 강화한다.
- 농장: 기존 병력 한도 관련 기능을 강화한다.
- 지휘소: 기존 MapRun 전체 아군 오라를 강화한다.
- 마력탑: 기존 마력 수급과 연구 가능 전술 Tier를 강화한다.

Tier 상승은 기존 역할 강화이며, 승인되지 않은 신규 분기·별도 자원·독립 미니게임을 추가하지 않는다.

## 7. 문서 수명주기와 우선순위

이 문서는 다음 기존 규칙보다 우선한다.

```text
모든 6종 건물 공통 A/B 분기
안정 금고 / 행운 금고
징집 농장 / 예비 농장
전열 병영 / 기동 병영
연사탑 / 포격탑 2분기
돌격 지휘소 / 수비 지휘소
```

다음 문서는 역사적 증거로만 보존한다.

```text
docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md
status = SUPERSEDED / HISTORICAL_EVIDENCE_ONLY / IMPLEMENTATION_INPUT_FORBIDDEN
```

병종 정본은 병종 역할·카운터 자체는 유지하지만 `전열 병영 가중 / 기동 병영 가중` 배치 규칙은 이 정본으로 대체한다.

전술·마력 정본은 전술 역할 자체를 유지하지만 `연사탑` 기반 압력 표기는 새 포격·방어 강화·저격 3분기와 재검증해야 한다. 마력탑의 직선 강화와 분기 금지 규칙은 유지한다.

## 8. 적대적 안전선

```text
SPECIAL_T1_TOKEN_SOURCE = NONE
AUTO_PRODUCTION_IS_NOT_TOKEN_SOURCE = REQUIRED
SPECIAL_POWER_AND_PRODUCTION_TRADEOFF = REQUIRED
UNIVERSAL_AB_BRANCH_GRAMMAR = FORBIDDEN
UNAPPROVED_LINEAR_BUILDING_BRANCH = FORBIDDEN
PREMATURE_T3_FIXATION = FORBIDDEN
```

- 특수병 T1이 TokenSource를 제공하면 이 정본 위반이다.
- 특수병이 일반병보다 강한 기능을 가지면서 생산시간도 같거나 짧으면 재검증 대상이다.
- 자동생산 완료와 룰렛 토큰 생성을 동일 사건으로 취급하지 않는다.
- 방어탑 세 T2의 역할이 서로 구분되지 않으면 실패다.
- 직선 강화 건물에 승인되지 않은 신규 분기를 추가하지 않는다.

## 9. 미정 항목

```text
GENERAL_AND_SPECIAL_EXACT_PRODUCTION_INTERVALS = PENDING_SIMULATION
SPECIAL_T1_RANDOM_SELECTION_TIMING = PENDING_GRILLME
SPECIAL_T1_RESULT_PREVIEW = PENDING_GRILLME
TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION
T2_EXACT_COSTS = PENDING_SIMULATION
T3_IDENTITIES_AND_EFFECTS = PENDING_GRILLME
DEFENSE_BRANCH_FINAL_DISPLAY_NAME = PENDING_NAMING
FIRST_STAGE2_T2_CANDIDATES = PENDING_GRILLME
STAGE2_GOLD_AND_LEFTOVER_POLICY = PENDING_GRILLME
```

## 10. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 정본은 제품 코드·데이터·Scene·Resource·아트 제작을 승인하지 않는다.
