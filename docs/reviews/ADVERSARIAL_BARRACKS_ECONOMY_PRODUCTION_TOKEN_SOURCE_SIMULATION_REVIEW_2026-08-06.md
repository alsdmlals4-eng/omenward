# [적대적 검토] 병영 경제·자동생산·TokenSource 시뮬레이션

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-ECONOMY-PRODUCTION-TOKEN-SOURCE-SIMULATION-CONTRACT-V1
status: ADVERSARIAL_REVIEW_FOR_PROPOSED_CONTRACT
approval: USER_REVIEW_PENDING
product_code_authority: NONE
```

## 결론

현재 정본은 특수병 T1에 자동생산과 같은 병종 TokenSource를 모두 부여한다. 이중 가치 자체는 허용되지만, 비용·생산 간격·토큰 기여를 따로 조정하면 특수병 병영이 사실상 필수 건물이 될 가능성이 높다.

```text
SPECIAL_T1_DOUBLE_VALUE_RISK
TOKEN_POOL_MONOPOLY_RISK
MULTI_SPECIAL_COMPOUNDING_RISK
LOW_ROLL_DEAD_PATH_RISK
RANDOM_SOURCE_LOCK_IN
TOKEN_POOL_DILUTION
AUTO_PRODUCTION_TOKEN_SOURCE_CONFLATION
```

## 공격 관점

1. 특수병 기능 가치가 일반병보다 큰데 TokenSource까지 동일 강도로 공급하면 건설 선택의 기회비용이 사라진다.
2. 무작위 결과별 상성이 다르므로 평균 승률만 맞추면 특정 결과가 죽거나 특정 결과가 압도할 수 있다.
3. 복수 특수병 병영은 서로 다른 특수 토큰을 추가하며 룰렛 폭과 전투 가치가 동시에 증가할 수 있다.
4. 저장·철거·실패 복구에서 결과 재선정 경로가 생기면 기대값 최적화가 플레이를 지배한다.
5. 첫 생산 시점과 첫 토큰 유입 시점이 너무 빠르면 실제 비용보다 조기 파워 스파이크가 크다.
6. 입력 출처가 없는 지수 시뮬레이션은 상대 비교만 가능하며 절대 골드·초 단위 승인 근거가 될 수 없다.

## 강제 규칙

```text
FREE_REROLL_REINTRODUCTION = FORBIDDEN
SAVE_RELOAD_RESELECT = FORBIDDEN
COST_INTERVAL_TOKEN_WEIGHT_MUST_BE_TUNED_JOINTLY
SIMULATION_GREEN_WITHOUT_INPUT_PROVENANCE = FORBIDDEN
AVERAGE_ONLY_BALANCE_JUDGMENT = FORBIDDEN
STATIC_CONTRACT_PASS_AS_BALANCE_PASS = FORBIDDEN
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

## 필수 반증 시나리오

- 일반병만 건설해도 방패·궁병 최소 경로가 유지되는가.
- 특수병만 건설했을 때 전체 압력에서 보편 우위가 생기지 않는가.
- 5개 특수 결과 각각이 표준 경로를 유지하면서 특정 결과만 전역 최적이 되지 않는가.
- 두 번째 특수병의 한계가치가 첫 번째보다 충분히 낮아지는가.
- 작은 룰렛 풀과 희석된 룰렛 풀에서 특수 토큰이 독점하거나 무의미해지지 않는가.
- 저장·불러오기·건설 실패·철거 후 재건으로 결과 기대값을 올릴 수 없는가.
- 낮은 골드 여유에서 특수병 선택이 필수 T1·첫 T2를 굶기지 않는가.

## 조정 우선순위

1. 토큰 독점만 문제면 `SPECIAL_TOKEN_SOURCE_WEIGHT_MULTIPLIER`를 먼저 낮춘다.
2. 전투·룰렛 모두 압도하면 생산 간격과 비용을 함께 올린다.
3. 특정 결과만 죽으면 무료 재추첨 대신 해당 병종 가치 또는 선정 가중치를 조정한다.
4. 일반병 경로가 무너지면 특수병을 약화하는 것보다 일반병의 기초 역할·비용 회수 시간을 먼저 확인한다.
5. 복수 특수병이 스노우볼이면 두 번째 이후 건설 기회비용 또는 한계가치 체감을 검토한다.

## Stop-ship

```text
GENERAL_PATH_VALIDITY_RATE < 0.95
ANY_SPECIAL_OUTCOME_PATH_VALIDITY_RATE < 0.85
REROLL_EXPECTED_VALUE_GAIN > 0
SPECIAL_TOKEN_SHARE_BURST_MAX > 0.45
MULTI_SPECIAL_DOMINANCE_RATE > 0.55
MISSING_INPUT_PROVENANCE
```

위 조건이 하나라도 남으면 수치 승인·제품 구현 계획으로 넘어가지 않는다.
