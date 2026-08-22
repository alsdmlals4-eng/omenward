# RM-TOOL-003 Read-only Balance Pilot — 2026-08-22

## 목적과 경계

이 문서는 `OMW-PLAN-20260820-BALANCE-BUDGET-01`의 **wave budget search envelope**를 Base `RM-TOOL-003 BALANCE_SCENARIO_BATCH_SIMULATOR` 계약으로 읽기 전용 분석한 sidecar evidence다.

- Source commit: `9a85021989bb7b8d2cf3b92d060d519f691e877f`
- Source contract: `docs/analysis/balance/current_normalized_balance_budget.v1.json`
- Product/runtime mutation: **NONE**
- Current `implementation_authorized: false`와 open PR #201의 canon reconciliation을 변경하거나 우회하지 않는다.
- 이 결과는 final product numerics나 runtime PASS가 아니다.

## 실행 계약

현재 planning envelope의 세 raw share를 seed마다 독립 추출한 뒤, source contract의 `normalize_selected_shares_to_one: true`를 적용했다.

```text
seed = 1..10000
W1 raw   ~ Uniform(0.20, 0.30)
W2 raw   ~ Uniform(0.25, 0.35)
Final raw~ Uniform(0.40, 0.50)
normalized_i = raw_i / (W1 + W2 + Final)
```

난수는 Python `random.Random(seed)`를 seed별로 새로 만들고 W1 → W2 → Final 순서로 소비했다. 세부 수치는 같은 경로의 JSON evidence에 기록한다.

## 결과

| 항목 | Raw mean | Normalized mean | Normalized P05–P95 | Normalized min–max |
|---|---:|---:|---:|---:|
| W1 | 0.24930 | 0.24943 | 0.21096–0.28768 | 0.19426–0.31326 |
| W2 | 0.29969 | 0.30003 | 0.26198–0.33886 | 0.24001–0.36582 |
| Final | 0.44960 | 0.45054 | 0.41138–0.49153 | 0.38467–0.52146 |

Raw 합계는 평균 `0.99859`, 최소 `0.85456`, 최대 `1.14159`였다. 정규화 후 합계는 모든 표본에서 1이 된다.

Final wave가 W1/W2보다 작아지는 표본은 이번 10,000 seed에서 없었다.

## 발견된 모호성

세 raw search envelope를 각각 독립 추출한 뒤 합계 1로 정규화하면 **정규화된 값이 원래 raw envelope 밖으로 나갈 수 있다.**

- W1: `1.24%`
- W2: `1.93%`
- Final: `3.44%`

이것은 곧바로 balance 오류를 뜻하지 않는다. 현재 정본은 해당 범위를 `wave_budget_search_envelope`로 두고 별도로 `normalize_selected_shares_to_one: true`를 명시한다. 따라서 합리적인 1차 해석은 **범위가 정규화 전 탐색 범위**라는 것이다.

다만 향후 final numerics를 고를 때 다음 둘 중 어느 계약인지 명확히 해야 한다.

1. raw proposal만 envelope 안에 있으면 되고, normalization 뒤 값은 벗어날 수 있다.
2. normalization 뒤 값도 envelope 안에 있어야 하며, 그렇다면 constrained sampler/재추출 규칙이 추가로 필요하다.

이 Pilot은 1번을 임의 확정하지 않는다.

## 판정

```text
KEEP planning envelope
+ CLARIFY post-normalization semantics before final numerics
+ DO NOT mutate runtime
```

현재 economy drift reconciliation, runtime execution, human validation, final product numerics 선택은 모두 기존 gate를 유지한다.

## Evidence ceiling

- `PLANNING_ENVELOPE_ONLY`
- `RUNTIME_NOT_RUN`
- `HUMAN_VALIDATION_NOT_RUN`
- `FINAL_PRODUCT_NUMERICS_NOT_APPROVED`
- `ECONOMY_DRIFT_RECONCILIATION_STILL_REQUIRED`

Machine-readable summary: `docs/analysis/balance/rm_tool_003_read_only_pilot_20260822.json`.
