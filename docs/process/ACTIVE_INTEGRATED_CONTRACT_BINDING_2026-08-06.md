# [현행] OMENWARD 통합 작업지시문 v4.4 활성 바인딩

```yaml
decision_id: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.4"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
source_repository_main: 02260589e1aa374c19005d19e47ba1f3b27332bd
base_recovery_exact_commit: fa69a77a14f923a756064f6ae151d34cadb374f7
base_current_main_observed: cf4c7a60c5b31b042043f91b268f381372fec69a
reconciliation_branch: planning/barracks-10000-robustness-execution-20260809
entry_gate: BLOCK
```

## 1. 활성 계약

사용자가 제공한 `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4.md`를 현재 OMENWARD 운영 계약으로 유지한다. v4.3/v4.2는 역사 비교 전용이며 계약 활성화는 제품 구현 진입 허가가 아니다.

## 2. 현재 재조정 사실

- Base current `main`: `cf4c7a60c5b31b042043f91b268f381372fec69a`
- Base recovery/validator exact baseline: `fa69a77a14f923a756064f6ae151d34cadb374f7`
- OMENWARD 9/10 Gate baseline main: `02260589e1aa374c19005d19e47ba1f3b27332bd`
- 5/10: exact 2,000-seed remediation smoke `PASS`
- 6/10: parameter-selection pre-review complete / selection execution unauthorized
- 7/10: observables defined / V00 cost+interval non-final envelope / functional value deferred
- 8/10: robustness execution review complete; 당시 dedicated runner+user approval required / `10K_NOT_RUN`
- 9/10: user-approved dedicated V00-only exact 10,000-seed robustness `PASS`
- PR #155: GUT 9.7.1 adoption spec not merged
- local Windows checkout / local Godot / shared audio vault: `BLOCKED_UNVERIFIED`

### Base / Project Base Adapter

```text
Base release pin = 9.4.3 / PRESERVED
Base automatic main migration = FORBIDDEN
Base latest delta = BCP-2026-010_CONTINUOUS_WORK_PROCESS_ROUTING_ONLY
Project Base Adapter schema/generator/validator delta = NONE_OBSERVED
GDD Sheet sync = CURRENT after this Gate sync
protected baseline = 1f23981fdfc3e965ff46c8866e978c4701eb3d4e
protected policy SHA256 = 1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52
```

### 5/10 durable evidence

```text
PLAYER_CAPABILITY_PROXY = STRUCTURAL_CHANNEL_VECTOR
COMBAT_POWER_SCALAR = FORBIDDEN
SUPPORT_TU_NUMERIC_INJECTION = FORBIDDEN
SECOND_SPECIAL_TOKEN_SOURCE = DEFERRED_UNTIL_3_NON_SPECIAL_ACTIVE_SOURCES
SPECIAL_TOKEN_SHARE_10_MIN = 0.296259
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333 <= 0.45
2K_JSON_SHA256 = a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2
2K_CSV_SHA256 = 3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560
```

### 7/10 non-final envelope

```text
SPECIAL_INTERVAL_CANON_GATE = STRICTLY_LONGER_THAN_RELEVANT_GENERAL_INTERVAL
COMPARISON_FORM = VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE
SELECTION_MODE = HARD_FILTER_THEN_PARETO
EXCLUDED_INTERVAL_FAIL = V01 / V02 / V05 / V06
PARETO_DOMINATED = V07 / V08
ECONOMY_PRODUCTION_ENVELOPE = V00_BASELINE_COST_INTERVAL_ONLY
ROBUSTNESS_SPECIAL_BARRACKS_COST_GOLD = 60
ROBUSTNESS_SPECIAL_INTERVAL_MULTIPLIER = 1.70
SPECIAL_FUNCTIONAL_VALUE_INDEX = DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS
FINAL_PARAMETER_VECTOR = NOT_SELECTED
```

### 8/10 review — point-in-time history

8/10 authority의 다음 사실은 역사 정본으로 유지한다.

```text
CURRENT_2K_RUNNER_FOR_DURABLE_10K = UNSAFE_EVIDENCE_PROVENANCE
8_OF_10_EXECUTION_CONTRACT = DEDICATED_RUNNER_REQUIRED
8_OF_10_EXECUTION_USER_APPROVAL = REQUIRED
8_OF_10_ACTUAL_10000_EXECUTION = NOT_RUN
```

후속 9/10 완료는 이 당시 사실을 소급 변경하지 않는다.

### 9/10 exact 10,000-seed robustness

사용자의 명시 승인 뒤 별도 runner/output identity에서 V00 하나만 실행했다.

```text
DECISION = OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1
RUNNER = docs/analysis/barracks_simulation/run_barracks_robustness_10000.py
OUTPUT_STEM = robustness_sweep_10000.v1
SEED_COUNT = 10000
COMMON_RANDOM_NUMBERS = TRUE
PARAMETER_VECTOR_COUNT = 1
STATUS = ROBUSTNESS_PASS
ROBUSTNESS_FAILED_GATES = []
SPECIAL_TOKEN_SHARE_10_MIN = 0.296265 <= 0.35
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333 <= 0.45
REROLL_EXPECTED_VALUE_GAIN = 0.0
SECOND_SPECIAL_MIN_NON_SPECIAL_ACTIVE_SOURCES = 3
SECOND_SPECIAL_DEFERRED_OBSERVATIONS = 82181
10K_JSON_SHA256 = 1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3
10K_CSV_SHA256 = e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b
```

10k PASS는 economy/production/physical TokenSource robustness에 한정한다. 다음 raw 진단은 계속 실패·비식별로 보존한다.

```text
GENERAL_PATH_VALIDITY_RATE = 0.0 / DIAGNOSTIC_FAIL
EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE = 0.0 / DIAGNOSTIC_FAIL
WORST_SPECIAL_REGRET_RATE = 1.0 / DIAGNOSTIC_FAIL
SECOND_SPECIAL_MARGINAL_VALUE_RATIO = 0.0 / DIAGNOSTIC_NON_SELECTION
IDENTIFIABILITY = DIAGNOSTIC_NON_IDENTIFIABLE
```

따라서 simulator historical functional-value input `1.5`는 `NON_DECISION_LEGACY_INPUT_ONLY`다. 최종 기능가치, 최종 3D vector, 최종 제품 numerics를 승인하지 않는다.

## 3. 역할 경계

```text
HiGodot = SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY / EXACT_SOURCE_OR_VERSION_UNVERIFIED
GUT 9.7.1 = DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED / PR155_NOT_MERGED
Hera = NOT_VERIFIED_INSTALLED_UNUSED / LIVE_QA_AND_OBSERVABILITY_ONLY_IF_ADOPTED
Hera persistent source mutation = FORBIDDEN
role overlap = FORBIDDEN
```

Hera historical direct-main 유입은 존재 사실만 인정하며 소급 승인하지 않는다.

## 4. Entry Gate

```text
ENTRY_GATE = BLOCK
```

9/10에서 닫힌 blocker:

```text
BARRACKS_10000_ROBUSTNESS_EXECUTION_USER_APPROVAL_REQUIRED = CLOSED
BARRACKS_10000_ROBUSTNESS_DEDICATED_RUNNER_REQUIRED = CLOSED
```

현재 독립 blocker:

- `BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED`
- GUT adoption spec PR #155 not merged
- HiGodot exact source/version unverified
- Hera adoption/direct-main disposition not closed
- local Godot/shared audio vault unavailable
- historical secret scan unproven accepted risk

계속 금지:

```text
PRODUCT_IMPLEMENTATION
GODOT_AUTHORING_MUTATION
FORMAL_GUT_EXECUTION
GUT_PLUGIN_ENABLEMENT
HERA_LIVE_QA_COMPLETION_CLAIM
IMAGE_GENERATION
AUDIO_ASSET_IMPORT_OR_RUNTIME_REFERENCE
LOCAL_MAIN_SYNC_CLAIM
GODOT_RUNTIME_CLAIM
BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION
BARRACKS_50000_SEED_CONFIRMATION
```

## 5. 다음 허용 작업

1. `BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW`
2. PR #155 GUT adoption-spec review
3. Hera Existing Solution First disposition

첫 작업은 기능가치를 식별할 제품 전투·역할 output numerics의 **authority와 측정 surface를 검토하는 계획 Gate**다. 기능가치 숫자, final vector, 50k 또는 제품 구현을 이 바인딩만으로 자동 승인하지 않는다.

## 6. Sheet 동기화

현재 Gate Decision은 GitHub와 Sheet에 같은 ID로 기록한다.

```text
OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1
```

실제 10k run이 존재하므로 `47_병영_Smoke_결과`에는 이 Decision의 10,000-seed 결과 행을 정확히 하나 기록한다. exact-head CI와 merge SHA는 변경이력 surface에 별도로 기록한다.

## 7. v4.3 역사

`OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1`은 역사 비교 전용이다. v4.4가 현재 운영 바인딩이다.
