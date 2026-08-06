# [승인] OMENWARD 병영 시뮬레이션 입력 출처 매니페스트·룰렛 축 정정

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SIMULATION-INPUT-PROVENANCE-AND-ROULETTE-AXIS-CORRECTION-V1
parent_decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-ECONOMY-PRODUCTION-TOKEN-SOURCE-SIMULATION-CONTRACT-V1
status: APPROVED_INPUT_PROVENANCE_MANIFEST
approval: USER_APPROVED_RECOMMENDED_OPTION
approval_count: 2_OF_10
scope: SIMULATION_INPUT_PROVENANCE_ONLY
product_code_authority: NONE
```

## 1. 결론

현재 자료는 **무차원 비용·생산 간격 탐색 범위와 KPI**는 제공하지만, 현행 20 Stage MapRun에 적용할 절대 경제·생산·압력 시간축은 제공하지 않는다.

```text
SIMULATION_RUNNABLE = FALSE
SMOKE_SWEEP = BLOCKED
DECISION_SWEEP = BLOCKED
CONFIRMATION_SWEEP = BLOCKED
ABSOLUTE_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

기계 판독 매니페스트:

- `docs/analysis/barracks_simulation/input_provenance_manifest.v1.json`
- canonical SHA-256: `706ec6da767d1102af7c8b2b39a711b981fa9692f8a949b2e473c90dabb5a33b`

## 2. 출처 우선순위

```text
현행 승인 정본
→ 현행 Google Sheet 정본
→ 승인된 무차원 시뮬레이션 가설
→ 과거 PoC 수치 후보
→ legacy 구현 비교 증거
```

파일명에 `APPROVED`가 있어도 최신 수명주기·상위 정정·현재 게임 구조와 충돌하면 현재 수치 권위로 사용하지 않는다.

## 3. 룰렛 확률 축 정정

현행 V2 룰렛은 추상 가중치 보드가 아니라 세 개의 물리 릴과 `TokenInstance`로 구성된다. TokenSource 건물 한 동은 각 릴에 하나씩 총 세 토큰을 공급한다.

```text
TOKEN_SOURCE_PROBABILITY_AXIS = PHYSICAL_TOKEN_INSTANCES_PER_REEL
TOKEN_SOURCE_BUILDING_CONTRIBUTION = 1_TOKEN_PER_REEL
TOTAL_TOKEN_INSTANCES_PER_SOURCE_BUILDING = 3
SPECIAL_TOKEN_SOURCE_WEIGHT_MULTIPLIER_0_35_TO_0_80 = SUPERSEDED
SAME_SYMBOL_SOURCE_WEIGHT = REWARD_SOURCE_SELECTION_ONLY
LEGACY_BOARD_WEIGHT = NOT_V2_PROBABILITY_AUTHORITY
```

따라서 특수병 토큰 점유율은 다음으로 검증한다.

```text
건설한 TokenSource 수
건설 완료 시점
릴의 X 교체와 append 결과
릴 길이와 심벌 구성
같은 심벌 TokenSource의 수
건물 파괴·비활성화 시점
```

`source_weight`는 같은 심벌이 이미 당첨된 뒤 어느 출처 병종을 보상할지 정하는 축이며, 심벌 자체가 정지 보드에 나타날 확률을 만드는 축이 아니다.

## 4. 유지되는 승인 탐색축

```text
GENERAL_BARRACKS_COST_INDEX = 1.00
SPECIAL_BARRACKS_COST_MULTIPLIER = 1.25 / 1.50 / 1.75 / 2.00
GENERAL_PRODUCTION_INTERVAL_INDEX = 1.00
SPECIAL_PRODUCTION_INTERVAL_MULTIPLIER = 1.45 / 1.70 / 1.95 / 2.20
GENERAL_UNIT_FUNCTIONAL_VALUE_INDEX = 1.00
SPECIAL_UNIT_FUNCTIONAL_VALUE_INDEX = 1.35 / 1.50 / 1.65
WINDOWS_MINUTES = 5 / 10 / 15
SMOKE_SEEDS = 2000
DECISION_SEEDS = 10000
CONFIRMATION_SEEDS = 50000
```

위 값은 상대 비교를 위한 시뮬레이션 계약이며 제품의 금화·초·실제 전투 수치가 아니다.

## 5. 과거 수치 판정

### 5.1 7월 Stage 경제 기준표

다음 값은 과거 첫 PoC 후보로 보존한다.

```text
starting_gold = 160
base_income = 5 gold / 20 seconds
control_income = 4 gold / point / 60 seconds
general_barracks_t1 = 40 gold / 20 seconds
special_barracks_t1 = 40 gold / 25 seconds
base_spin_cost = 20 gold
```

그러나 이 문서는 15분 정규 Stage와 구형 특수병단 구조를 전제로 한다. 현행은 20 Stage MapRun이고 정비시간 경제·생산 Clock이 미정이므로 다음과 같이 판정한다.

```text
LEGACY_STAGE_ECONOMY_BASELINE = CANDIDATE_ONLY
CURRENT_MAPRUN_GOLD_TIMELINE = MISSING_BLOCKER
ABSOLUTE_BUILD_COSTS = NOT_CURRENTLY_APPROVED
```

### 5.2 특수병 생산시간

과거 후보:

```text
priest = 180 seconds
mage = 210 seconds
flying = 240 seconds
giant = 300 seconds
```

현재 특수병 T1은 마도사·사제·암살자·비행병·거인 5종 무작위 고정 생산이며 암살자 수치가 없다. 과거 값은 T2 전용 4병종 구조이므로 현행 절대값으로 사용할 수 없다.

```text
LEGACY_SPECIAL_PRODUCTION_TIMES = CANDIDATE_ONLY
ASSASSIN_PRODUCTION_INTERVAL_SECONDS = MISSING_BLOCKER
GENERAL_PRODUCTION_INTERVAL_SECONDS = MISSING_BLOCKER
```

## 6. 룰렛 회전 빈도

룰렛은 자동 고정 주기 시스템이 아니라 플레이어가 비용·예약 자원·정비시간을 보고 실행하는 선택이다.

```text
ROULETTE_DRAW_CADENCE = POLICY_SCENARIO_NOT_FIXED_CLOCK
```

시뮬레이션 정책 후보:

1. `AGGRESSIVE_WHEN_AFFORDABLE`
2. `RESERVE_ESSENTIAL_OBLIGATIONS`
3. `MAINTENANCE_ONLY`

고정 초 단위 회전 주기를 만들어 플레이어 선택을 지우지 않는다.

## 7. 현재 차단 입력

```text
GENERAL_PRODUCTION_INTERVAL_SECONDS = MISSING_BLOCKER
ASSASSIN_PRODUCTION_INTERVAL_SECONDS = MISSING_BLOCKER
FOOD_SLOT_AND_NODE_OPPORTUNITY_COST = MISSING_BLOCKER
CURRENT_MAPRUN_GOLD_TIMELINE = MISSING_BLOCKER
ENEMY_THREAT_BUDGET_AND_TIMELINE = MISSING_BLOCKER
MAINTENANCE_CLOCK_MATRIX = MISSING_BLOCKER
```

압력 정본은 `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`와 3개 Wave Beat 역할을 승인하지만 정확 등장 초·Spawn 수·Threat Budget은 승인하지 않았다.

## 8. 다음 Gate

```text
NEXT_GATE = CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE
```

다음 결정은 한 묶음으로 다음 최소 입력을 고정해야 한다.

1. 시작 골드·전투 중 수입·접전지 수입·기본 회전비.
2. 정비시간 중 경제·생산·건설 Clock의 ON/OFF.
3. 일반병 생산 기준 초와 특수병 5종 생산 초.
4. Stage 1~5의 Wave Beat 시간표와 압력별 Threat Budget.
5. 식량·건설 노드 기회비용의 정규화 공식.

이 Gate를 통과하기 전에는 2,000 seed smoke sweep도 실행하지 않는다.
