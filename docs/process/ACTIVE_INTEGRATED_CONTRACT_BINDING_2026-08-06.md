# [현행] OMENWARD 통합 작업지시문 v4.4 활성 바인딩

```yaml
decision_id: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.4"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
source_repository_main: 4da8ed64baaa66b15d110490f1b15fd9be20aee0
base_recovery_exact_commit: fa69a77a14f923a756064f6ae151d34cadb374f7
base_current_main_observed: cf4c7a60c5b31b042043f91b268f381372fec69a
reconciliation_branch: planning/barracks-10000-robustness-review-20260808
entry_gate: BLOCK
```

## 1. 활성 계약

사용자가 제공한 `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4.md`를 현재 OMENWARD 운영 계약으로 유지한다.

- v4.4: `ACTIVE`
- v4.3 / v4.2: `HISTORICAL_COMPARISON_ONLY`
- 계약 활성화는 제품 구현 진입 허가와 다르다.

## 2. 현재 재조정 사실

- Base current `main`: `cf4c7a60c5b31b042043f91b268f381372fec69a`
- Base recovery/validator exact baseline: `fa69a77a14f923a756064f6ae151d34cadb374f7`
- OMENWARD gate baseline main: `4da8ed64baaa66b15d110490f1b15fd9be20aee0`
- 온보딩 기획: `APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT`
- 병영 5/10: `APPROVED_5_OF_10_REMEDIATION_SMOKE_PASS`
- 병영 6/10 review: `REVIEW_COMPLETE / PARAMETER_SELECTION_NOT_IDENTIFIABLE / EXECUTION_NOT_AUTHORIZED`
- 병영 7/10: `OBSERVABLES_DEFINED / ECONOMY_PRODUCTION_ENVELOPE_IDENTIFIED / FUNCTIONAL_VALUE_DEFERRED`
- 병영 8/10 review: `ROBUSTNESS_REVIEW_COMPLETE / DEDICATED_RUNNER_REQUIRED / USER_APPROVAL_REQUIRED / 10K_NOT_RUN`
- PR #155: Draft / GUT 9.7.1 adoption spec not merged
- PR #159: `MERGED` / Base recovery `COMPLETE`
- PR #163: `MERGED` / Project Base Adapter freshness `RECONCILED`
- PR #164: `MERGED` / exact 2,000-seed remediation smoke `PASS`
- PR #165: `MERGED` / 10k parameter-selection pre-review complete
- PR #166: `MERGED` / parameter-selection observables defined
- local Windows checkout / local Godot / shared audio vault: 현재 agent 환경에서 접근 불가

### Base·Project Base Adapter

```text
Base release pin = 9.4.3 / PRESERVED
Base current main automatic migration = FORBIDDEN
Base 8ea80e85→cf4c7a60 delta = CONTINUOUS_WORK_EXECUTION_TRIGGER_PROCESS_ROUTING_ONLY
Project Base Adapter schema/generator/validator delta = NONE_OBSERVED
OMENWARD Godot/barracks contract delta = NONE_OBSERVED
GDD Sheet = CURRENT after this Gate sync
protected baseline = 1f23981fdfc3e965ff46c8866e978c4701eb3d4e
protected policy source = CANONICAL_ADAPTER_SOURCE
protected policy hash = 1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52
generated views = BASE_GENERATOR_VALIDATED
```

Base 최신 delta는 `AGENTS.md`, 운영/Work Mode/intake Skill, continuous-work reference/plan/spec/tests 및 BCP registry에 국한된다. released Base pin과 protected adapter baseline을 자동 변경하지 않는다.

### Barracks 5/10 remediation

```text
PLAYER_CAPABILITY_PROXY = STRUCTURAL_CHANNEL_VECTOR
COMBAT_POWER_SCALAR = FORBIDDEN
SUPPORT_TU_NUMERIC_INJECTION = FORBIDDEN
COMBAT_VALIDITY / ROLE_BLIND_REGRET = DIAGNOSTIC_NON_IDENTIFIABLE
SECOND_SPECIAL_TOKEN_SOURCE = DEFERRED_UNTIL_3_NON_SPECIAL_ACTIVE_SOURCES
AUTO_PRODUCTION = UNCHANGED
PHYSICAL_TOKEN_INSTANCE_GRAMMAR = PRESERVED
SMOKE_RERUN = PASS
failed_decision_gates = []
SPECIAL_TOKEN_SHARE_10_MIN = 0.296259
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333 <= 0.45
```

### Barracks 6/10 review

```text
DECISION_SWEEP_10000_PARAMETER_SELECTION = NOT_AUTHORIZED
PARAMETER_SELECTION = NOT_IDENTIFIABLE_WITH_CURRENT_DECISION_METRICS
ROBUSTNESS_ONLY_10000 = OPTIONAL_AFTER_SEPARATE_APPROVAL
CONFIRMATION_SWEEP_50000 = BLOCKED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
```

### Barracks 7/10 observable 계약

```text
SPECIAL_INTERVAL_CANON_GATE = STRICTLY_LONGER_THAN_RELEVANT_GENERAL_INTERVAL
RELEVANT_GENERAL_INTERVAL_MAX_SECONDS = 65
INTERVAL_MULTIPLIER_1.45 = CANON_FAIL
EXCLUDED_VECTORS = V01 / V02 / V05 / V06
COMPARISON_FORM = VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE
SELECTION_MODE = HARD_FILTER_THEN_PARETO
V07_V08 = PARETO_DOMINATED_BY_V03_V04_ON_GOLD_WITH_SAME_INTERVAL
BASELINE_PRESERVATION_TIEBREAK = KEEP_APPROVED_BASELINE_IF_HARD_GATE_PASS_AND_PARETO_NONDOMINATED
ECONOMY_PRODUCTION_ENVELOPE = V00_BASELINE_COST_INTERVAL_ONLY
ROBUSTNESS_SPECIAL_BARRACKS_COST_GOLD = 60
ROBUSTNESS_SPECIAL_INTERVAL_MULTIPLIER = 1.70
SPECIAL_FUNCTIONAL_VALUE_INDEX = DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS
FINAL_PARAMETER_VECTOR = NOT_SELECTED
```

### Barracks 8/10 robustness-only review

`OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1`은 실제 10k 실행 전 실행 가치·범위·evidence provenance를 검토한다.

현행 runner는 seed count를 받을 수 있지만 다음 durable identity를 5/10 2k에 고정한다.

```text
RUNNER = docs/analysis/barracks_simulation/run_barracks_remediation_smoke.py
OUTPUT_STEM = smoke_sweep_2000.v2
DEFAULT_OUTPUT_DIRECTORY = docs/analysis/barracks_simulation
RESULT_DECISION_ID = 5_OF_10_REMEDIATION_DECISION
CURRENT_RUNNER_FOR_DURABLE_10K = UNSAFE_EVIDENCE_PROVENANCE
```

따라서 현재 runner의 기본 출력으로 10k를 실행하지 않는다. 기존 2k evidence overwrite와 10k evidence의 2k/5-of-10 오표기를 구조적으로 막는 dedicated execution contract가 필요하다.

```text
ROBUSTNESS_10000 = RECOMMENDED_AFTER_DEDICATED_EXECUTION_CONTRACT_AND_USER_APPROVAL
EXECUTION_CONTRACT = DEDICATED_RUNNER_REQUIRED
EXECUTION_USER_APPROVAL = REQUIRED
ACTUAL_10000_EXECUTION = NOT_RUN
PARAMETER_SELECTION_10000 = NOT_AUTHORIZED
CONFIRMATION_SWEEP_50000 = BLOCKED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
CONTINUOUS_WORK_AFTER_REVIEW = STOPPED_USER_DECISION
```

`COMBAT_POWER_SCALAR`, `SUPPORT_TU`, 단일 weighted opportunity score를 재도입하지 않는다. dedicated package는 unique Decision/output stem, 2k overwrite 방지, seed count assertion, input hashes, V00 envelope, diagnostic-only combat boundary, result hashes를 갖춰야 한다.

## 3. 직접 main 변경 provenance

과거 Sheet 기준 이후 확인된 Hera direct-main 유입과 `.asset-vault` ignore 변경은 저장소 존재 사실만 인정하며 소급 승인하지 않는다. Hera는 `NOT_VERIFIED_INSTALLED_UNUSED`이며 Existing Solution First disposition이 필요하다.

## 4. 역할 경계

```text
HiGodot = SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY
GUT 9.7.1 = DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED
Hera = LIVE_QA_AND_OBSERVABILITY_ONLY
Hera persistent source mutation = FORBIDDEN
role overlap = FORBIDDEN
```

현재 HiGodot exact source/version은 미검증이다. GUT adoption spec PR #155는 미병합이고 formal GUT 실행은 차단한다. Hera adoption도 검증되지 않았다.

## 5. Entry Gate

```text
ENTRY_GATE = BLOCK
```

현재 독립 차단 조건:

- `BARRACKS_10000_ROBUSTNESS_EXECUTION_USER_APPROVAL_REQUIRED`
- `BARRACKS_10000_ROBUSTNESS_DEDICATED_RUNNER_REQUIRED`
- `BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED`
- GUT adoption spec PR #155 not merged
- HiGodot exact source/version unverified
- Hera direct-main import disposition not closed
- local Godot / shared audio vault unavailable
- historical secret scan unproven accepted risk

따라서 제품 구현, Godot 저작 mutation, formal GUT, Hera live-QA 완료 주장, 이미지 생성, audio import, local-main/Godot runtime 완료 주장, robustness 10k 실행, parameter-selection 10k 실행, 50k confirmation은 금지한다.

## 6. 다음 허용 작업

1. `BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION_PACKAGE_USER_APPROVAL`
2. PR #155 GUT adoption-spec review
3. Hera Existing Solution First disposition

Base continuous-work 계약상 `[연속작업] 진행해`는 새 승인 자체를 만들지 않는다. 7/10 authority의 별도 실행 승인 요구가 유지되므로 연속작업은 1번 사용자 결정에서 중지한다.

## 7. Sheet 동기화

v4.4 활성 계약 Decision은 유지한다.

```text
OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
```

현재 Gate 변경은 다음 Decision ID로 GitHub와 Sheet에 함께 기록한다.

```text
OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1
```

PR exact-head와 병합 결과는 Sheet의 PR/변경이력 surface에서 추적한다. 실제 10k seed run이 없으므로 `47_병영_Smoke_결과`에는 신규 실행 행을 만들지 않는다.

## 8. v4.3 역사

`OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1`은 역사 비교 전용이다. v4.4가 현재 운영 바인딩이다.
