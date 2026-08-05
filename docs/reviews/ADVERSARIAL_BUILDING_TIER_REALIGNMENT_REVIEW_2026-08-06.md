# OMENWARD 건물 Tier 구조 재정렬 적대적 검토

```yaml
review_id: OMW-REV-20260806-BUILDING-TIER-REALIGNMENT-V1
decision_id: OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1
status: REVIEWED / PLANNING_ONLY
product_code_authority: NONE
```

## 1. 검토 결론

```text
CORE_FIT = STRONG
BUILDING_IDENTITY = CLEARER_THAN_UNIVERSAL_AB_GRAMMAR
GENERAL_SPECIAL_DIFFERENTIATION = COHERENT
TOKEN_SOURCE_BOUNDARY = EXPLICIT
DOCUMENT_IMPLEMENTATION_READINESS = PASS_FOR_PLANNING_ONLY
PRODUCT_IMPLEMENTATION_READINESS = BLOCKED_BY_NUMERICS_T3_AND_RUNTIME_PLAN
```

기존의 모든 건물 A/B 분기 구조는 건물 기능보다 형식 통일을 우선해 실제 사용자 의도와 충돌했다. 새 구조는 병종 전문화·전투 역할 전문화·직선 기능 강화로 나누어 각 건물의 정체성을 명확하게 만든다.

## 2. 적대적 발견

### OMW-AUD-530 — SPECIAL_T1_TOKEN_LEAK

위험: 특수병 병영 T1이 무작위 특수병 자동생산과 함께 TokenSource까지 제공하면 T2 전문화의 핵심 가치가 약해진다.

수용 기준:

```text
SPECIAL_T1_TOKEN_SOURCE = NONE
```

### OMW-AUD-531 — SPECIAL_DOUBLE_ADVANTAGE

위험: 특수병이 일반병보다 기능이 강한데 생산 간격까지 같거나 짧으면 일반병 투자 가치가 붕괴한다.

수용 기준:

```text
SPECIAL_UNIT_FUNCTIONAL_POWER = STRONGER_THAN_GENERAL_UNIT
SPECIAL_AUTO_PRODUCTION_INTERVAL = LONGER_THAN_GENERAL_UNIT
EXACT_INTERVAL = PENDING_SIMULATION
```

### OMW-AUD-532 — AUTO_PRODUCTION_TOKEN_SOURCE_CONFLATION

위험: 자동생산과 룰렛 TokenSource 공급을 같은 이벤트로 처리하면 특수병 T1의 예외 규칙과 룰렛 확률 설계가 무너진다.

수용 기준:

```text
AUTO_PRODUCTION_IS_NOT_TOKEN_SOURCE = REQUIRED
```

### OMW-AUD-533 — DEFENSE_BRANCH_ROLE_OVERLAP

위험: 포격·방어 강화·저격의 공격 범위와 역할이 겹치면 사실상 수치 비교만 남는다.

수용 기준:

- 포격탑은 범위 공격을 소유한다.
- 방어 강화형은 방어력·내구 유지에 집중한다.
- 저격탑은 긴 사거리를 소유한다.
- 정확 수치와 T3는 후속 결정으로 남긴다.

### OMW-AUD-534 — OLD_CANON_AUTHORITY_LEAK

위험: 기존 `안정/행운`, `징집/예비`, `전열/기동`, `연사/포격`, `돌격/수비` 분기가 현재 구현 입력으로 남는다.

수용 기준:

```text
OLD_BUILDING_BRANCH_CANON = SUPERSEDED
OLD_BUILDING_BRANCH_IMPLEMENTATION_INPUT = FORBIDDEN
```

### OMW-AUD-535 — STAGE1_SEVEN_BUILDING_OVERLOAD

위험: 기본 건물이 7종이 됐다는 이유로 효과가 느린 특수병 병영까지 Stage 1 의무 건물에 포함하면 첫 세팅 비용과 설명량이 증가한다.

수용 기준:

```text
FOUNDATION_REQUIRED_T1_COUNT = 6
SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE
```

### OMW-AUD-536 — LINEAR_BUILDING_FEATURE_CREEP

위험: 금고·농장·지휘소·마력탑의 Tier 상승 때 신규 분기·별도 자원·독립 미니게임을 덧붙여 역할이 다시 불명확해진다.

수용 기준:

```text
LINEAR_T2_BRANCHING = FORBIDDEN
EXISTING_FUNCTION_ENHANCEMENT_ONLY = REQUIRED
```

### OMW-AUD-537 — PREMATURE_T3_AND_NUMERIC_FIXATION

위험: T2 구조 수정과 동시에 T3 세부 효과, 생산시간, 토큰 가중치, 비용을 임의 확정한다.

수용 기준:

```text
T3_IDENTITIES_AND_EFFECTS = PENDING_GRILLME
EXACT_NUMERICS = PENDING_SIMULATION
```

### OMW-AUD-538 — GENERAL_T1_IDENTITY_AMBIGUITY

위험: T1 기본 보병이 기존 T2 일반 병종 중 하나와 혼동된다.

수용 기준:

- T1은 `기본 보병`으로 별도 표기한다.
- T2의 방패·대검·창·궁병·기병과 구분한다.
- 정확 외형·능력치는 병종 데이터 결정에서 확정한다.

### OMW-AUD-539 — DEFENSE_NAME_COLLISION

위험: T1 `방어탑`과 T2 `방어탑`의 명칭이 UI에서 충돌한다.

수용 기준:

```text
CURRENT_FUNCTION_LABEL = 방어탑(방어 강화형)
FINAL_DISPLAY_NAME = PENDING_NAMING
```

### OMW-AUD-540 — TOKEN_SOURCE_OVERPOPULATION

위험: 여러 전문 병영이 동시에 TokenSource를 추가할 때 룰렛 풀이 과도하게 희석된다.

수용 기준:

```text
TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION
```

건물 구조만으로 정확 토큰 수·가중치를 고정하지 않는다.

### OMW-AUD-541 — PRODUCT_AUTHORITY_OVERCLAIM

위험: 문서 정본과 테스트 추가를 제품 구현 완료로 오해한다.

수용 기준:

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 3. 남은 의사결정

1. 특수병 T1 무작위 선정·공개 시점
2. T3 병종·방어탑·직선 강화 세부 효과
3. 방어 강화형 T2의 최종 표시 이름
4. 일반병·특수병 생산 간격과 토큰 가중치
5. Stage 2 첫 T2 후보와 골드·잔여 골드 규칙

## 4. 최종 판정

```text
SPECIAL_T1_TOKEN_LEAK = CLOSED_BY_CONTRACT
SPECIAL_DOUBLE_ADVANTAGE = STRUCTURALLY_GUARDED
AUTO_PRODUCTION_TOKEN_SOURCE_CONFLATION = CLOSED_BY_SEPARATE_RULES
DEFENSE_BRANCH_ROLE_OVERLAP = PARTIALLY_GUARDED / NUMERICS_PENDING
OLD_CANON_AUTHORITY_LEAK = REQUIRES_LIFECYCLE_SYNC
STAGE1_SEVEN_BUILDING_OVERLOAD = CLOSED_BY_OPTIONAL_SPECIAL_BARRACKS
PREMATURE_T3_AND_NUMERIC_FIXATION = CLOSED_BY_PENDING_GATES
PRODUCT_CODE = UNCHANGED
```
