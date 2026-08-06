# 적대적 검토 — 병영 자동생산·TokenSource 정정

```yaml
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-AUTO-PRODUCTION-AND-TOKEN-SOURCE-AMENDMENT-V1
reviewed_at: 2026-08-06 KST
result: CONDITIONALLY_ACCEPTABLE / SIMULATION_AND_HUMAN_QA_PENDING
product_code_authority: NONE
```

## 결론

일반병·특수병 병영 모두 자동생산과 TokenSource를 제공한다는 사용자 결정은 룰렛과 병영 투자의 연결을 일관되게 만든다. 특수병 T1은 건설 때 선정된 같은 병종을 두 경로에 사용하되, 자동생산과 TokenSource를 하나의 보상 이벤트로 합치지 않는다.

## 위험과 통제

### SPECIAL_T1_DOUBLE_VALUE_RISK

강한 특수병을 자동생산하면서 TokenSource까지 공급하면 일반병 병영보다 총가치가 과도할 수 있다.

```text
SPECIAL_AUTO_PRODUCTION_INTERVAL = LONGER_THAN_GENERAL_UNIT
SPECIAL_T1_TOKEN_WEIGHT = PENDING_SIMULATION
SPECIAL_T1_BUILD_COST = PENDING_SIMULATION
```

생산 간격·토큰 가중치·건설비용을 묶어 검증하고, 특수병 T1이 모든 합리적 상황에서 일반병 투자를 압도하면 Stop-ship이다.

### RANDOM_SOURCE_LOCK_IN

무작위로 선정된 병종이 자동생산과 룰렛 공급을 모두 점유하므로 불리한 결과의 체감 비용이 커질 수 있다.

```text
ALL_SPECIAL_T1_RESULTS_MUST_HAVE_VALID_USE = REQUIRED
SPECIAL_T1_RESULT_HARD_COUNTER_REQUIREMENT = FORBIDDEN
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
```

다섯 결과 모두 유효한 활용처가 있어야 하며 특정 결과를 다음 전투의 필수키로 만들지 않는다.

### TOKEN_POOL_DILUTION

여러 병영이 TokenSource를 추가하면 룰렛 풀이 희석되거나 특정 결과가 과도하게 누적될 수 있다.

```text
TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION
TOKEN_SOURCE_STACKING_RULE = PENDING_SIMULATION
```

정확 가중치·중첩·상한은 건물 구조 문서가 아니라 확률 시뮬레이션이 소유한다.

### AUTO_PRODUCTION_TOKEN_SOURCE_CONFLATION

같은 병종을 사용한다는 이유로 자동생산 완료 시 토큰까지 동시에 지급하면 독립 획득 경로가 사라지고 기대값이 이중 계산될 수 있다.

```text
AUTO_PRODUCTION_IS_NOT_TOKEN_SOURCE = REQUIRED
SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
```

### FREE_REROLL_AMPLIFICATION

결과 공개 뒤 무료 취소·재건설·불러오기로 자동생산과 TokenSource를 동시에 다시 뽑으면 악용 가치가 더 커진다.

```text
SPECIAL_T1_FREE_REROLL = FORBIDDEN
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_REVEAL_THEN_FREE_CANCEL = FORBIDDEN
```

## 검증 Gate

- 방패병·궁병 기본 경로가 특수병 없이도 완료 가능해야 한다.
- 특수병 다섯 결과 모두 자동생산·TokenSource 연결이 저장 복구 후 유지돼야 한다.
- 어떤 특수병 결과도 일반병 투자, 다른 특수병 결과, 룰렛 조작의 가치를 지속적으로 압도해서는 안 된다.
- UI는 자동생산 진행과 룰렛 공급을 별도 상태로 표시해야 한다.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
