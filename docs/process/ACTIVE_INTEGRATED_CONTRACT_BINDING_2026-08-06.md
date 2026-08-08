# [현행] OMENWARD 통합 작업지시문 v4.4 활성 바인딩

```yaml
decision_id: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.4"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
source_repository_main: 25c4a5953d57acce450c93db1a8b5f0281937586
base_recovery_exact_commit: fa69a77a14f923a756064f6ae151d34cadb374f7
base_current_main_observed: a912cc001ff4d4e3415fb4b4931723c49eb08d9a
reconciliation_branch: planning/barracks-parameter-selection-observables-20260808-final
entry_gate: BLOCK
```

## 1. 활성 계약

사용자가 제공한 `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4.md`를 현재 OMENWARD 운영 계약으로 유지한다.

- v4.4: `ACTIVE`
- v4.3 / v4.2: `HISTORICAL_COMPARISON_ONLY`
- 계약 활성화는 제품 구현 진입 허가와 다르다.

## 2. 현재 재조정 사실

- Base current `main`: `a912cc001ff4d4e3415fb4b4931723c49eb08d9a`
- Base recovery/validator exact baseline: `fa69a77a14f923a756064f6ae151d34cadb374f7`
- OMENWARD gate baseline main: `25c4a5953d57acce450c93db1a8b5f0281937586`
- 온보딩 기획: `APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT`
- 병영 5/10: `APPROVED_5_OF_10_REMEDIATION_SMOKE_PASS`
- 병영 6/10 review: `REVIEW_COMPLETE / PARAMETER_SELECTION_NOT_IDENTIFIABLE / EXECUTION_NOT_AUTHORIZED`
- 병영 7/10: `OBSERVABLES_DEFINED / ECONOMY_PRODUCTION_ENVELOPE_IDENTIFIED / FUNCTIONAL_VALUE_DEFERRED / 10K_NOT_RUN`
- PR #155: Draft / GUT 9.7.1 adoption spec not merged
- PR #159: `MERGED` / Base recovery `COMPLETE`
- PR #163: `MERGED` / Project Base Adapter freshness `RECONCILED`
- PR #164: `MERGED` / exact 2,000-seed remediation smoke `PASS`
- PR #165: `MERGED` / 10k execution pre-review complete
- local Windows checkout / local Godot / shared audio vault: 현재 agent 환경에서 접근 불가

### Base·Project Base Adapter

```text
Base release pin = 9.4.3 / PRESERVED
Base current main automatic migration = FORBIDDEN
Base a912cc delta = SERIAL_FICTION_SKILL_ROUTING_ONLY / NO_PROJECT_BASE_ADAPTER_SCHEMA_GENERATOR_VALIDATOR_DELTA
GDD Sheet = CURRENT / SHEET_GITHUB_SYNCED
protected baseline = 1f23981fdfc3e965ff46c8866e978c4701eb3d4e
protected policy source = CANONICAL_ADAPTER_SOURCE
protected policy hash = 1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52
generated views = BASE_GENERATOR_VALIDATED
PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED = CLEARED
```

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

`OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1`은 현재 정본과 승인 simulation baseline에서 선택 가능한 축만 사전 등록한다.

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
ROBUSTNESS_ONLY_10000 = READY_FOR_SEPARATE_APPROVAL / NOT_RUN
PARAMETER_SELECTION_10000 = NOT_AUTHORIZED
CONFIRMATION_SWEEP_50000 = BLOCKED
NEXT_GATE = BARRACKS_10000_SEED_ROBUSTNESS_ONLY_REVIEW
```

기능가치를 구분하기 위해 `COMBAT_POWER_SCALAR` 또는 `SUPPORT_TU`를 재도입하지 않는다. 단일 weighted opportunity score도 도입하지 않는다.

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

- `BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED`
- GUT adoption spec PR #155 not merged
- HiGodot exact source/version unverified
- Hera direct-main import disposition not closed
- local Godot / shared audio vault unavailable
- historical secret scan unproven accepted risk

따라서 제품 구현, Godot 저작 mutation, formal GUT, Hera live-QA 완료 주장, 이미지 생성, audio import, local-main/Godot runtime 완료 주장, 10k parameter-selection 실행, 50k confirmation은 금지한다.

## 6. 다음 허용 작업

1. `BARRACKS_10000_SEED_ROBUSTNESS_ONLY_REVIEW`
2. PR #155 GUT adoption-spec review
3. Hera Existing Solution First disposition

10k robustness-only sweep는 **별도 승인 전 실행하지 않는다**. 승인되더라도 economy/production/physical-token invariant 확인용이며 final functional-value 또는 final parameter selection 권한을 갖지 않는다.

## 7. Sheet 동기화

v4.4 활성 계약 Decision은 유지한다.

```text
OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
```

현재 Gate 변경은 다음 Decision ID로 GitHub와 Sheet에 함께 기록한다.

```text
OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1
```

PR exact-head와 병합 결과는 Sheet의 PR/변경이력 surface에서 추적한다. 새 seed 실행이 없으므로 `47_병영_Smoke_결과`에는 새 실행 행을 만들지 않는다.

## 8. v4.3 역사

`OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1`은 역사 비교 전용이다. v4.4가 현재 운영 바인딩이다.
