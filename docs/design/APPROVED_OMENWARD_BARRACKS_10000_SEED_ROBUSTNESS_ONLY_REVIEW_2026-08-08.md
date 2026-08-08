# [승인] OMENWARD 병영 10,000-seed Robustness-Only 실행 검토

```yaml
updated_at: 2026-08-08
decision_id: OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1
parent_decision_id: OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1
status: REVIEW_COMPLETE / EXECUTION_CONTRACT_REQUIRED / USER_APPROVAL_REQUIRED / 10K_NOT_RUN
approval: CONTINUOUS_WORK_AUTO_APPROVED_TECHNICAL_REVIEW_FINDINGS_ONLY
scope: REVIEW_ONLY / NO_10000_EXECUTION
product_code_authority: NONE
```

## 1. 결론

10,000-seed robustness-only run은 **경제·생산·물리 TokenSource invariant의 Monte Carlo 안정성 확인용**으로는 가치가 있다. 그러나 현재 runner를 durable 10k evidence writer로 그대로 재사용해서는 안 된다.

```text
ROBUSTNESS_10000 = RECOMMENDED_AFTER_DEDICATED_EXECUTION_CONTRACT_AND_USER_APPROVAL
CURRENT_RUNNER_FOR_DURABLE_10K = UNSAFE_EVIDENCE_PROVENANCE
ACTUAL_10000_EXECUTION = NOT_RUN
EXECUTION_CONTRACT = DEDICATED_RUNNER_REQUIRED
EXECUTION_USER_APPROVAL = REQUIRED
PARAMETER_SELECTION_10000 = NOT_AUTHORIZED
CONFIRMATION_SWEEP_50000 = BLOCKED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
```

이 Decision은 robustness 실행의 가치·범위·필수 실행 계약만 검토한다. 실제 10,000-seed 계산을 수행하지 않는다.

## 2. 현행 runner 적대 검토 finding

현행 runner:

`docs/analysis/barracks_simulation/run_barracks_remediation_smoke.py`

은 `--seeds` 입력을 받아 10,000을 계산할 수 있지만 durable evidence provenance는 2,000-seed remediation에 고정돼 있다.

```text
DEFAULT_OUTPUT_DIRECTORY = docs/analysis/barracks_simulation
OUTPUT_STEM = smoke_sweep_2000.v2
RESULT_DECISION_ID = OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1
```

따라서 현재 runner를 기본 출력으로 `--seeds 10000` 실행하면 다음 위험이 있다.

1. canonical 2k `smoke_sweep_2000.v2.json/.csv`를 덮어쓸 수 있다.
2. 10k evidence가 파일명상 2k로 오표기될 수 있다.
3. 10k evidence가 5/10 remediation Decision ID를 상속해 별도 robustness 실행 provenance를 잃는다.
4. 7/10에서 확정한 V00 **non-final economy/production envelope**와 10k 역할 경계를 durable metadata로 구분하지 못한다.

이 finding은 실행 결과 추정이 아니라 현재 runner 소스에서 직접 판정한 fail-closed evidence-provenance 문제다.

## 3. 현재 2k 증거 보존

기존 canonical evidence는 변경하지 않는다.

```text
JSON = docs/analysis/barracks_simulation/smoke_sweep_2000.v2.json
JSON_SHA256 = a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2
CSV = docs/analysis/barracks_simulation/smoke_sweep_2000.v2.csv
CSV_SHA256 = 3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560
SEED_COUNT = 2000
```

현재 분석 디렉터리에 10,000-seed 결과 파일은 없다. `47_병영_Smoke_결과`에도 신규 10k 행을 만들지 않는다.

## 4. 향후 robustness 실행 envelope

7/10 observable 계약의 non-final envelope를 그대로 보존한다.

```text
ROBUSTNESS_ENVELOPE = V00_BASELINE_COST_INTERVAL_ONLY
SPECIAL_BARRACKS_COST_GOLD = 60
SPECIAL_INTERVAL_MULTIPLIER = 1.70
SPECIAL_FUNCTIONAL_VALUE_INDEX = DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS
```

10k robustness가 검증할 수 있는 범위:

```text
ECONOMY_STABILITY
PRODUCTION_STABILITY
PHYSICAL_TOKEN_SHARE_STABILITY
SPECIAL_TOKEN_SHARE_10_MIN_STABILITY
SPECIAL_TOKEN_SHARE_BURST_MAX_STABILITY
SECOND_SPECIAL_TOKEN_SOURCE_GUARD_STABILITY
DETERMINISTIC_INPUT_AND_COMMON_RANDOM_NUMBER_PROVENANCE
```

검증하거나 선택할 수 없는 범위:

```text
SPECIAL_FUNCTIONAL_VALUE_INDEX
COMBAT_POWER_OR_ROLE_VALUE
FINAL_PARAMETER_VECTOR
FINAL_PRODUCT_NUMERICS
PRODUCT_IMPLEMENTATION
```

`COMBAT_POWER_SCALAR`, `SUPPORT_TU_NUMERIC_INJECTION`, post-hoc weighted utility score를 재도입하지 않는다.

## 5. Dedicated execution contract 필수 조건

실제 10k를 승인·실행하기 전 전용 execution package는 최소 다음을 갖춰야 한다.

```text
UNIQUE_DECISION_ID = REQUIRED
UNIQUE_10000_OUTPUT_STEM = REQUIRED
NO_OVERWRITE_OF_2000_EVIDENCE = REQUIRED
SEED_COUNT_10000_ASSERTION = REQUIRED
INPUT_HASH_BINDING = REQUIRED
V00_COST_INTERVAL_ENVELOPE_ASSERTION = REQUIRED
FUNCTIONAL_VALUE_SELECTION = FORBIDDEN
PARAMETER_SELECTION = FORBIDDEN
RAW_COMBAT_DIAGNOSTICS = DIAGNOSTIC_ONLY
OUTPUT_JSON_AND_CSV_HASHES = REQUIRED
EXACT_HEAD_CI = REQUIRED
SHEET_47_ROW_ONLY_AFTER_REAL_10000_RUN = REQUIRED
```

권장 구현은 기존 2k runner의 canonical evidence semantics를 변경하는 대신 **별도 10k robustness runner/output stem**을 두거나, 최소한 기존 runner에 fail-closed mode와 명시적 unique stem/Decision을 추가해 2k evidence 덮어쓰기가 구조적으로 불가능하도록 하는 것이다. 어느 구현을 채택하든 실제 실행 전에 TDD RED→GREEN과 exact-head 검증을 거친다.

## 6. Base freshness

이 Gate 시작 시 Base current main은 다음으로 재조회됐다.

```text
BASE_CURRENT_MAIN = cf4c7a60c5b31b042043f91b268f381372fec69a
PR166_SHEET_BASE = 8ea80e855917b29aad53d774c5c20b524265e750
DELTA = BCP-2026-010_CONTINUOUS_WORK_EXECUTION_TRIGGER_IMPLEMENTATION_ONLY
PROJECT_BASE_ADAPTER_SCHEMA_GENERATOR_VALIDATOR_DELTA = NONE_OBSERVED
OMENWARD_GODOT_OR_BARRACKS_CONTRACT_DELTA = NONE_OBSERVED
```

Base delta는 `AGENTS.md`, 운영/Work Mode/intake Skill, continuous-work reference/plan/spec/tests 및 BCP registry 영역이다. OMENWARD의 released Base pin, recovery baseline, Project Base Adapter protected policy를 자동 이행하거나 병영 simulation semantics를 바꾸지 않는다.

## 7. 연속작업 경계와 다음 상태

Base continuous-work 계약은 `[연속작업] 진행해`가 새 승인 자체를 만들지 않는다고 명시한다. 또한 7/10 authority는 실제 robustness 10k 실행에 별도 사용자 승인을 요구한다.

따라서 이번 review의 기술 finding은 연속작업 범위에서 자동 승인해 정본화하지만, **전용 10k execution package 작성·실행은 새 별도 승인 없이 자동 시작하지 않는다.**

```text
CONTINUOUS_WORK_AFTER_REVIEW = STOPPED_USER_DECISION
NEXT_REQUIRED_DECISION = APPROVE_DEDICATED_10000_ROBUSTNESS_EXECUTION_PACKAGE
PR155_GUT_REVIEW = NOT_STARTED_BY_THIS_DECISION
HERA_DISPOSITION = NOT_STARTED_BY_THIS_DECISION
```

사용자가 전용 robustness execution package를 승인하면 그 승인 범위에서 runner 계약→TDD→10k 실행→증거 hash/Sheet sync→적대 검토를 진행한다.

## 8. 변경하지 않는 것

```text
BARRACKS_5_OF_10_REMEDIATION_SMOKE = PASS
BARRACKS_6_OF_10_PRE_EXECUTION_REVIEW = COMPLETE
BARRACKS_7_OF_10_OBSERVABLES = DEFINED
CURRENT_CANONICAL_2K_EVIDENCE = UNCHANGED
ACTUAL_10000_EXECUTION = NOT_RUN
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
GAMEPLAY_DATA = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
ENTRY_GATE = BLOCK
```
