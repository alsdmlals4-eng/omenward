# [승인] OMENWARD 병영 2,000-seed Smoke Sweep 결과·식별 가능성 Gate

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
parent_decision_id: OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1
status: APPROVED_SMOKE_RESULT / CONDITIONAL_FAIL
approval: USER_DIRECT_PROCEED_AUTHORIZATION
approval_count: 4_OF_10
scope: ANALYSIS_ARTIFACT_ONLY
product_code_authority: NONE
```

## 1. 결론

2,000개 공통 seed로 9개 비용·생산간격·기능가치 벡터를 실행했다. 결과 파일은 두 번의 독립 재실행에서 바이트 단위로 일치했다.

```text
SMOKE_SWEEP = COMPLETED
SMOKE_STATUS = SMOKE_COMPLETED_CONDITIONAL_FAIL
DECISION_SWEEP = BLOCKED
CONFIRMATION_SWEEP = BLOCKED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

조건부 실패 원인은 둘이다.

1. `MODEL_IDENTIFIABILITY_FAIL`: 비병영 지원 기여 LOW에서는 일반 경로 유효성이 `0.195417`, MID/HIGH에서는 `1.000000`으로 임계값을 가로지른다.
2. `SPECIAL_TOKEN_SHARE_BURST_MAX = 0.500000`: 승인 상한 `0.45`를 초과한다.

이 결과를 이유로 제품 수치를 확정하거나 10,000-seed 단계로 자동 승격하지 않는다.

## 2. 실행 범위

```text
SEEDS = 2000
COMMON_RANDOM_NUMBERS = TRUE
PARAMETER_VECTORS = 9
STAGE2_PATHS = SHIELD / ARCHER
GOLD_SCENARIOS = LOW / STANDARD / HIGH
SPIN_POLICIES = AGGRESSIVE / RESERVE / MAINTENANCE_ONLY
BUILD_PLANS = GENERAL_ONLY / SPECIAL_ONLY / GENERAL_AND_SPECIAL / MULTI_SPECIAL
FIXED_SPECIAL_OUTCOMES = ASSASSIN / PRIEST / MAGE / FLYING_UNIT / GIANT
```

분석 방식:

```text
APPROACH = PROXY_MONTE_CARLO_WITH_IDENTIFIABILITY_ENVELOPE
CANON_BACKED = ECONOMY / PRODUCTION CLOCK / PHYSICAL REEL / STAGE1_TO_5_TU_TIMELINE
NON_CANON_ASSUMPTION = UNIT FUNCTIONAL PROXY / PRESSURE AFFINITY / NON_BARRACKS SUPPORT
SUPPORT_ENVELOPES = LOW / MID / HIGH
```

## 3. 기준 벡터 결과

기준 벡터:

```text
SPECIAL_COST_MULTIPLIER = 1.50
SPECIAL_INTERVAL_MULTIPLIER = 1.70
SPECIAL_FUNCTIONAL_VALUE_INDEX = 1.50
```

| KPI | 결과 | 계약선 | 판정 |
|---|---:|---:|---|
| `SPECIAL_OPTION_DOMINANCE_RATE` | `0.199417` | `<= 0.60` | PASS |
| `GENERAL_PATH_VALIDITY_RATE` | `1.000000` | `>= 0.95` | PASS_IN_MID_PROXY_ONLY |
| `EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE` | 모든 5종 `1.000000` | `>= 0.85` | PASS_IN_MID_PROXY_ONLY |
| `WORST_SPECIAL_REGRET_RATE` | `0.114500` | `<= 0.15` | PASS |
| `SPECIAL_TOKEN_SHARE_10_MIN` | `0.296259` | `<= 0.35` | PASS |
| `SPECIAL_TOKEN_SHARE_BURST_MAX` | `0.500000` | `<= 0.45` | FAIL |
| `MULTI_SPECIAL_DOMINANCE_RATE` | `0.000000` | `<= 0.55` | PASS |
| `SECOND_SPECIAL_MARGINAL_VALUE_RATIO` | `0.000000` | `<= 0.80` | PASS_WITH_CAVEAT |
| `REROLL_EXPECTED_VALUE_GAIN` | `0.000000` | `= 0` | PASS_BY_CONTRACT |

`SECOND_SPECIAL_MARGINAL_VALUE_RATIO = 0`은 두 번째 특수병이 항상 무가치하다는 뜻이 아니다. 10분 censored window 안에서 두 번째 병영이 구매·생산되지 못한 시나리오가 많다는 진단이며, 노드·시간·생산 첫 도착 분포를 후속 Gate에서 분리해야 한다.

## 4. 식별 가능성 결과

같은 기준 벡터와 같은 seed를 유지하고 비병영 지원 기여만 변경했다.

```text
GENERAL_PATH_VALIDITY_LOW  = 0.195417
GENERAL_PATH_VALIDITY_MID  = 1.000000
GENERAL_PATH_VALIDITY_HIGH = 1.000000
SENSITIVITY_DELTA = 0.804583
THRESHOLD = 0.95
THRESHOLD_FLIP = TRUE
IDENTIFIABILITY = FAIL
```

현재 정본은 방어탑 화력, 지휘소 오라, 마력탑·전술 출력, 실제 HP·DPS·사거리·이동·사상자·전선 커밋의 절대값을 제공하지 않는다. 따라서 일반 경로 생존율과 특수병별 전투 유효성을 제품 밸런스 결론으로 사용할 수 없다.

## 5. 물리 릴 결과

TokenSource 건물 한 동이 각 릴에 한 토큰씩 공급하는 현행 정본을 사용했다.

```text
ONE_SPECIAL_SOURCE_SHARE_WITH_VAULT_AND_GENERAL = 1 / 3 = 0.333333 MAX BEFORE_REEL_GROWTH
TWO_SPECIAL_SOURCES_WITH_VAULT_AND_GENERAL = 2 / 4 = 0.500000
SPECIAL_TOKEN_SHARE_10_MIN = 0.296259
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.500000
```

10분 평균은 통과하지만 복수 특수병 병영이 활성화되는 순간 물리 출처 점유율이 상한을 초과한다. 이 문제는 구형 fractional 가중치로 숨기지 않는다. 후속 Gate는 다음 중 정본과 일치하는 해결책을 비교해야 한다.

- 복수 특수병 건설 시점·비용·노드 압력 강화.
- 두 번째 특수병 TokenSource 활성 지연 또는 조건부 활성.
- 금고·일반병 등 다른 실제 TokenSource 추가에 따른 자연 희석.
- 상한 자체가 물리 릴 문법과 충돌하는지 KPI 재검토.

`건물당 각 릴 1개` 정본을 몰래 fractional token으로 변경하는 방법은 금지한다.

## 6. 9개 벡터 판정

- 모든 벡터가 `SPECIAL_TOKEN_SHARE_BURST_MAX`에서 실패했다. 이는 비용·생산간격·기능가치가 아니라 물리 TokenSource 개수 구조에서 발생한다.
- `V01_CHEAP_FAST_LOW`, `V02_CHEAP_FAST_HIGH`는 추가로 `WORST_SPECIAL_REGRET_RATE`를 실패했다.
- 기준 벡터와 나머지 여섯 corner는 countable KPI 8/9를 통과했지만 식별 가능성 실패 때문에 순위를 제품 추천으로 사용하지 않는다.
- 비싼·느린 벡터의 낮은 regret는 강한 밸런스가 아니라 특수병 접근 자체가 늦어 차이가 관찰되지 않는 censoring 결과일 수 있다.

## 7. 모델 경계

```text
ROULETTE = NATURAL_CENTERLINE_ONLY
LUCKY_AND_MOVE_OPTIMIZATION = NOT_MODELED
REWARD_GRADE = NORMAL_ONLY
CASUALTY_AND_DEATH = NOT_MODELED
IRREVERSIBLE_LANE_ASSIGNMENT = NOT_MODELED
PRODUCT_HP_DPS_RANGE_SPEED = NOT_MODELED
EXACT_TOWER_COMMAND_AND_TACTIC_OUTPUT = NOT_MODELED
FIFTEEN_MINUTE_WINDOW = CENSORED_AT_STAGE5_END_830_SECONDS
```

따라서 이 Smoke는 경제·생산·물리 릴 구조의 screening과 미확정 입력 탐지에 유효하지만 실제 승률·난이도·전투 체감 예측으로 사용하지 않는다.

## 8. 재현성

```text
BASELINE_INPUT_SHA256 = a8424ae1b5f22e86db3eca52b7942ff5b1f0e50a3c689ae57b9062550c066878
MODEL_INPUT_SHA256 = 9fd10ad3ad131c4dbfcf2700144e61449e890324a861892e470004a5bfdc627a
RESULT_JSON_SHA256 = b04824ca7eb5241d45199227e3866a19b5e55e15deee03856e24cc7ea29d7b52
RESULT_CSV_SHA256 = 1b4c11b52dd016c8b4e0ea9e2cfe4f06b48e9722ab6e89b177a28b71d562f9aa
JSON_BYTES = 11563
CSV_BYTES = 1437
REPEAT_RUN_BYTE_IDENTICAL = PASS
```

32-seed 표준 라이브러리 경로도 바이트 단위 재현성을 통과했다. 100 seeds에서 가속 NumPy 경로와 표준 경로의 모든 KPI·지원 민감도가 정확히 일치했다.

## 9. 다음 Gate

```text
NEXT_GATE = PLAYER_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION
```

다음 Gate에서 최소한 다음을 결정한다.

1. Stage 1~5 비병영 전투 기여를 `방어탑 / 지휘소 / 마력·전술 / 기본 전선 상태`로 분리한 승인 proxy.
2. HP·DPS 제품 수치 없이도 비교 가능한 Stage별 player-capability budget.
3. 복수 특수병 TokenSource 0.50 burst의 구조적 해결 또는 KPI 상한 재설계.
4. 두 번째 특수병의 첫 생산 도착·노드·골드 censoring 진단.

이 Gate를 통과하고 2,000-seed smoke를 다시 통과하기 전에는 10,000-seed decision sweep를 실행하지 않는다.
