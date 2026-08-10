# [현행] 오멘워드 미확정 결정·Gate 목록

```yaml
updated_at: 2026-08-11
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
current_process_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
contract_version: 4.5
work_phase: PHASE_A_GPT_CHAT_PLANNING
current_runtime_package: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
runtime_status: PR175_DRAFT_7_RUNTIME_GAPS_OPEN
phase_c_gate: BLOCK
product_code_authority: NONE_FOR_CURRENT_DECISION
```

## 1. 현재 단계 blocker

```text
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
PHASE_C_BLOCKED
```

사용자의 `[연속작업 진행해]`는 현재 승인된 planning/canon scope의 연속 수행 flag이며 `기획 완료` 선언이 아니다.

따라서 이 파일의 runtime pending 항목은 **승인 범위가 존재하더라도 현재 Phase C가 열릴 때까지 persistent implementation을 시작하지 않는다.**

## 2. Durable 병영 분석 상태

```text
5_OF_10 = REMEDIATION_SMOKE_PASS
6_OF_10_REVIEW = COMPLETE
7_OF_10 = OBSERVABLES_DEFINED
8_OF_10_REVIEW = ROBUSTNESS_EXECUTION_REVIEW_COMPLETE
9_OF_10 = EXACT_10000_ROBUSTNESS_PASS
FUNCTIONAL_VALUE_COMBAT_NUMERICS_REVIEW = COMPLETE
FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS = DEFINED
```

9/10 evidence:

```text
SPECIAL_TOKEN_SHARE_10_MIN = 0.296265
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333
10K_JSON_SHA256 = 1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3
10K_CSV_SHA256 = e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b
IDENTIFIABILITY = DIAGNOSTIC_NON_IDENTIFIABLE
```

Measurement contract:

```text
FIXTURE_POLICY = DETERMINISTIC_SAME_INPUT
FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE
BLOCKED_RUNTIME_OUTPUT = NEVER_SYNTHESIZE_AS_ZERO
FV-COMMON-01 / FV-PRIEST-01 / FV-MAGE-01 / FV-FLIER-01 / FV-GIANT-01
```

## 3. 현행 Special T1 TokenSource

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
```

구형 “Special T1 TokenSource 없음”은 final amendment로 대체됐으며 미확정 항목이 아니다.

## 4. Runtime package — 승인됐지만 현재 실행 보류

```text
PR175 = OPEN_DRAFT
PR175_HEAD_OBSERVED = bde85549560fca90f7aa25fc4842bc0a3afb92e7
PR175_HISTORICAL_EXACT_HEAD_ACTIONS = 11_SUCCESS_0_FAILURE
ISSUE176 = OPEN
ISSUE176_APPROVED_RUNTIME_GAPS = 7
PR175_MERGE = FORBIDDEN
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
```

Issue176의 7개 gap:

1. Priest encouragement: provisional 5s +8% attack speed, start/end events, support uptime, timing regression.
2. Support role이 기존 deterministic movement/combat/objective fallback을 전부 가로채지 않도록 보존.
3. `flying`은 priority이며 universal target permission boundary가 아님.
4. `cluster` density tie = lane order / unit-id semantics.
5. Giant `FRONTLINE_SURVIVAL_TIME` + `STRUCTURE_DAMAGE` collector.
6. Registered deterministic FV-PRIEST/MAGE/FLIER/GIANT/COMMON fixtures.
7. true per-cast `TARGETS_HIT_PER_CAST` with multi-cast coverage.

이 7개는 새 product Decision이 필요한 항목이 아니라 기존 approved runtime package completeness gap이다. 하지만 현재 v4.5 Phase Gate 때문에 아직 구현 단계가 아니다.

## 5. Final value·numeric pending

```text
FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED
FINAL_WEIGHTED_SCORE = FORBIDDEN_WITHOUT_NEW_APPROVAL
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PARAMETER_SELECTION_10000 = NOT_AUTHORIZED_AS_FINAL_SELECTION
CONFIRMATION_SWEEP_50000 = BLOCKED
```

기존 10k robustness는 economy/production/physical-token robustness evidence이지 final product numeric selection이 아니다.

## 6. Tool·runtime pending

```text
GODOT_AI = 3.1.3 / approved authority when Phase C is active
GUT = 9.7.1
HERA = 1.0.0 / LIVE_QA_AND_OBSERVABILITY_ONLY
HERA_PERSISTENT_SOURCE_MUTATION = FORBIDDEN
```

과거 HiGodot session/process/socket 진단은 historical evidence다. Phase C 진입 시 local process/session truth를 fresh-read한다.

## 7. Platform pending

```text
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
REPRESENTATIVE_PC_BUILD = NOT_RUN
REPRESENTATIVE_ANDROID_BUILD = NOT_RUN
```

## 8. Current planning/canon closure

현재 먼저 닫아야 하는 것은 product implementation이 아니라 `OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1`이다.

```text
GitHub current canon propagation
→ Google Sheet same-Decision proposed sync
→ bounded reread
→ exact-head CI
→ adversarial review
→ Base/project race check
→ planning merge when eligible
→ merged-main readback
→ Sheet MERGED_CANON readback
```

## 9. 다음 사용자 Gate

현재 Decision이 검증·병합되더라도 다음 제품 단계는 자동으로 시작하지 않는다.

```text
NEXT_USER_GATE = USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION
```

사용자가 명시적으로 `기획 완료`를 선언하면 fresh-read 후 Phase B 전체 기획 최종 검토·기능 분해·벤치마킹·의존성·보호범위·Definition of Ready를 닫는다. 그 뒤에만 Phase C를 검토한다.
