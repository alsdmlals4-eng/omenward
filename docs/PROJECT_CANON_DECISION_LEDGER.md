# [현행] 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-06
status: CURRENT_DECISION_LEDGER
latest_approved_decision: OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
latest_approved_contract: OMW-DEC-20260806-PLANNING-BARRACKS-ECONOMY-PRODUCTION-TOKEN-SOURCE-SIMULATION-CONTRACT-V1
contract_status: APPROVED / 4_OF_10
current_count: 4_OF_10
product_code_authority: NONE
```

## 운영 원칙

- GitHub와 Google Sheet는 같은 Decision ID와 exact PR HEAD를 사용한다.
- 시뮬레이션 결과는 제품 수치가 아니다.
- countable KPI 통과보다 식별 가능성·Stop-ship이 우선한다.
- 물리 TokenInstance 정본을 fractional weight로 되돌리지 않는다.
- 조건부 실패 상태에서는 10,000-seed sweep와 제품 구현을 열지 않는다.

## 4/10 결과

```text
DECISION = OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
STATUS = APPROVED_SMOKE_RESULT / CONDITIONAL_FAIL
SEEDS = 2000
VECTORS = 9
MODEL_IDENTIFIABILITY = FAIL
GENERAL_VALIDITY_LOW_MID_HIGH = 0.195417 / 1.000000 / 1.000000
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.500000 / FAIL
DECISION_SWEEP = BLOCKED
NEXT_GATE = PLAYER_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION
```

## 권위

- `design/APPROVED_OMENWARD_BARRACKS_SMOKE_SWEEP_RESULTS_2026-08-06.md`
- `analysis/barracks_simulation/smoke_model_assumptions.v1.json`
- `analysis/barracks_simulation/run_barracks_smoke_sweep.py`
- `analysis/barracks_simulation/smoke_sweep_2000.v1.json`
- `analysis/barracks_simulation/smoke_sweep_2000.v1.csv`
- `reviews/ADVERSARIAL_BARRACKS_SMOKE_SWEEP_REVIEW_2026-08-06.md`

## 제품 경계

```text
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_CODE = UNCHANGED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
