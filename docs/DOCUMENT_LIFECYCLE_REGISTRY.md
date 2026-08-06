# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-06
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
status: CURRENT_LIFECYCLE_AUTHORITY
latest_approved_decision: OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
current_count: 4_OF_10
```

이 레지스트리는 파일명·과거 YAML·부분 문구보다 우선한다. 분석 결과는 제품 구현 권위가 아니다.

## [현행]

- `design/APPROVED_OMENWARD_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_CONTRACT_2026-08-06.md`
- `design/APPROVED_OMENWARD_BARRACKS_SIMULATION_INPUT_PROVENANCE_MANIFEST_2026-08-06.md`
- `design/APPROVED_OMENWARD_CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE_2026-08-06.md`
- `design/APPROVED_OMENWARD_BARRACKS_SMOKE_SWEEP_RESULTS_2026-08-06.md`
- `analysis/barracks_simulation/input_provenance_manifest.v1.json`
- `analysis/barracks_simulation/current_maprun_economy_pressure_baseline.v1.json`
- `analysis/barracks_simulation/smoke_model_assumptions.v1.json`
- `analysis/barracks_simulation/run_barracks_smoke_sweep.py`
- `analysis/barracks_simulation/smoke_sweep_2000.v1.json`
- `analysis/barracks_simulation/smoke_sweep_2000.v1.csv`
- `reviews/ADVERSARIAL_BARRACKS_SMOKE_SWEEP_REVIEW_2026-08-06.md`

## [승인]

```text
decision = OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
status = APPROVED / 4_OF_10 / CONDITIONAL_FAIL
smoke_sweep = COMPLETED
decision_sweep = BLOCKED
next_gate = PLAYER_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION
```

## [보류]

- 승인된 Stage 1~5 player-capability proxy.
- 복수 특수병 TokenSource burst 해결 또는 KPI 상한 재승인.
- 수정된 2,000-seed smoke 재실행.
- 10,000 / 50,000 seed sweep.
- 최종 제품 수치와 Stage 6~20 확장.
- 제품 구현·runtime·human QA.

## [증거]

- `smoke_sweep_2000.v1.json`과 CSV는 4/10의 재현 가능한 분석 증거다.
- LOW/MID/HIGH support envelope는 식별 가능성 검사용 비정본 가정이며 제품 입력이 아니다.
- 1/10~3/10 문서와 과거 PR·Sheet revision은 결정 계보다.

## [폐기]

- fractional TokenInstance로 0.50 burst를 숨기는 방식.
- 조건부 실패를 KPI 다수결 PASS로 승격하는 방식.
- 승인되지 않은 HP/DPS·타워·전술 수치를 제품 사실처럼 사용하는 방식.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
DECISION_SWEEP = BLOCKED
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
LOCAL_GODOT_PROJECT = UNCHANGED
```
