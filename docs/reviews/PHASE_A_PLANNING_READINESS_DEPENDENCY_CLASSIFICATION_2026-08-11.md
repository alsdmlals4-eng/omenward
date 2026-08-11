# [검토] OMENWARD Phase A 기획 준비도 의존성 분류

```yaml
updated_at: 2026-08-11
decision_id: OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
parent_decision_id: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
source_main_observed: a57e533c30c47cb3b31766bae27bcf0d7eed5bc6
base_main_observed: 315c66eea9614c284b9c11c4d522141065dfa4b0
work_phase: PHASE_A_GPT_CHAT_PLANNING
review_result: READINESS_DEPENDENCIES_CLASSIFIED / NOT_PLANNING_COMPLETE
product_code_mutation: NONE
godot_persistent_mutation: NONE
final_numeric_selection: NONE
new_t3_content_decision: NONE
```

## 1. 목적과 권위 경계

이 문서는 새 게임플레이 값을 승인하는 문서가 아니다. 이미 승인된 책임 원본을 다시 읽어 **현재 PR175 runtime package에 들어가기 전에 필요한 결정**과 **runtime/측정/출시 뒤에 남겨야 하는 결정**을 분리한다.

분류는 다음 일곱 종류만 사용한다.

```text
IMPLEMENTATION_COMPLETENESS
PROVISIONAL_IMPLEMENTATION_INPUT_APPROVED
POST_RUNTIME_EVIDENCE_TUNING
FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER
LEVEL_OR_IMPLEMENTATION_DETAIL_DEFERRED
RELEASE_PHASE_DEFERRED
HISTORICAL_OR_SUPERSEDED
```

현재 단계 Gate는 변하지 않는다.

```text
PHASE_A_GPT_CHAT_PLANNING
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
PHASE_C_BLOCKED
```

사용자의 연속작업 승인은 이 review의 실행 권한이지만 `기획 완료` 선언이 아니다.

## 2. PR175 / Issue176

승인된 runtime package, 기능가치 정의 review, deterministic measurement scenarios, Issue176을 교차 확인한 결과:

```text
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
NO_NEW_PRODUCT_DECISION_REQUIRED_FOR_ISSUE176_7_GAPS = TRUE
```

일곱 항목은 Priest provisional support output, deterministic fallback 보존, flying priority/permission 분리, cluster deterministic tie-break, Giant collectors, registered FV fixtures, true per-cast `TARGETS_HIT_PER_CAST`다.

이 분류는 구현 허가가 아니다. Phase C가 닫혀 있으므로 PR175의 persistent product/Godot 변경은 계속 금지된다.

## 3. 승인된 provisional 구현 입력과 final tuning의 분리

runtime package는 역할 출력과 측정 경로를 먼저 만들고, 그 출력으로 functional-value를 비교한 뒤 final tuning을 선택하도록 설계되어 있다.

```text
ROLE_OUTPUT_RUNTIME -> DETERMINISTIC_MEASUREMENT -> FUNCTIONAL_VALUE_COMPARISON -> FINAL_TUNING
```

따라서:

```text
PRIEST_PROVISIONAL_5S_PLUS_8_PERCENT_AS = PROVISIONAL_IMPLEMENTATION_INPUT_APPROVED
ROLE_OUTPUT_MEASUREMENT_FIXTURES = IMPLEMENTATION_COMPLETENESS
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = POST_RUNTIME_EVIDENCE_TUNING
FINAL_WEIGHTED_SCORE = NOT_SELECTED / NEW_APPROVAL_REQUIRED_IF_INTRODUCED
```

기존 10,000-seed robustness 결과는 economy/production/physical-token 구조 증거이며 final combat-value 또는 final product numeric selection을 대신하지 않는다.

## 4. TokenSource — 물리 릴 문법과 특수병 선정 분포를 분리

초기 amendment의 blanket `TOKEN_SOURCE_WEIGHT_AND_COUNT` pending 표현은 후속 승인 remediation 이후 current-facing 상태를 정확히 표현하지 못한다.

후속 승인 owner는 확률축을 fractional weight가 아니라 **실제 릴의 물리 TokenInstance 개수**로 고정하고 active source당 릴에 한 개만 두며 fractional weight workaround를 금지한다. Sheet `45_병영_입력_출처`도 source building 하나가 세 릴에 총 세 개의 TokenInstance를 공급하는 current-ready contract를 보존한다.

current-facing 정규화:

```text
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN
```

이 세 문장은 물리 릴 instance count를 요약한 것이며 **특수병 5종 중 어느 병종이 선택되는 최종 확률**을 정한 문장이 아니다.

```text
SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
SPECIAL_T1_SELECTION_DISTRIBUTION_FINAL_VALUES = NOT_SELECTED
```

즉 `physical TokenInstance count`와 `selected special-unit distribution`을 하나의 `weight/count pending`으로 묶지 않는다.

## 5. 플랫폼·save·export·store

PC·Android architecture는 save, responsive UI/input, PC adapter/build, Android lifecycle/build, store integration을 Phase 3~7의 별도 단계로 둔다. current state에서도 해당 작업은 완료되지 않았다.

```text
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
EXPORT_PRESETS = ABSENT
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
```

분류:

```text
SHARED_SAVE_SCHEMA / PLATFORM_ADAPTERS / EXPORT_PRESETS / STORE_INTEGRATION = RELEASE_PHASE_DEFERRED
```

이 문장은 위 작업이 완료됐다는 뜻이 아니다. PR175의 role-output runtime completeness와 전체 출시 readiness를 분리한다는 뜻이다.

## 6. T3·이름·전체 제품 범위

현재 core vertical-slice 범위는 T3 unlock과 save/load를 필수 구현 범위로 두지 않는다. 따라서 아직 최신 owner가 닫지 않은 T3 상세와 최종 display naming을 PR175의 role-output runtime blocker로 올리지 않는다.

```text
T3_CONTENT_AND_FINAL_NAMES = FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER
DEFENSE_TOWER_T3_DETAILS = FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER
DEFENSE_BRANCH_FINAL_DISPLAY_NAME = FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER
```

단, 이미 후속 승인된 항목은 open으로 되돌리지 않는다.

```text
ARCHER_T3_LATER_APPROVED_DETAIL = CROSSBOW_ARCHER / RAPID_FIRE_ARCHER
ANTI_AIR_ARCHER_T3 = SUPERSEDED / REMOVED / IMPLEMENTATION_INPUT_FORBIDDEN
```

일반·특수 병종의 다른 T3 세부, 영웅 exact identity, 방어탑 T3 세부 등은 각 최신 owner를 확인해 전체 제품 기획에서 별도로 닫는다. 이 review에서 새 병종·효과·이름을 만들지 않는다.

## 7. Level·구현 상세

정확 node coordinate, 일부 layout/UX timing처럼 approved semantics를 바꾸지 않는 항목은 최신 owner가 별도 결정을 요구하지 않는 한 다음으로 분리한다.

```text
T1_EXACT_NODE_COORDINATES = LEVEL_OR_IMPLEMENTATION_DETAIL_DEFERRED
EXACT_PRESENTATION_TIMINGS = LEVEL_OR_IMPLEMENTATION_DETAIL_DEFERRED_UNLESS_PRODUCT_SEMANTIC_CONFLICT_APPEARS
```

이는 사용자가 선택해야 할 gameplay rule을 몰래 구현자가 결정해도 된다는 뜻이 아니다. gameplay meaning이 달라지는 순간 Phase A product decision으로 승격한다.

## 8. 역사 pending 처리

과거 checkpoint의 `HISTORICAL_PENDING_*`는 당시 상태 증거다. 후속 Decision이 닫은 항목을 current blocker로 재발행하지 않는다.

```text
HISTORICAL_CHECKPOINT_PENDING = HISTORICAL_OR_SUPERSEDED_WHEN_LATER_OWNER_EXISTS
```

예:
- Special T1 selection trigger는 successful construction commit amendment가 닫음.
- onboarding minimum valid paths / Belu retry-skip / human stop-ship은 후속 approved owner가 닫음.
- Archer T3는 later matrix correction이 `CROSSBOW_ARCHER / RAPID_FIRE_ARCHER`로 정정.
- 물리 TokenSource count/weight grammar는 later burst-remediation owner가 닫음.

## 9. Phase A readiness 판정

현재 PR175에 대해서는 다음을 구분한다.

```text
PR175_PRODUCT_SEMANTIC_DECISION_BLOCKERS_FOUND_IN_ISSUE176 = 0
PR175_RUNTIME_COMPLETENESS_GAPS = 7
PR175_FINAL_FV_REQUIRED_BEFORE_RUNTIME = FALSE
PR175_PLATFORM_RELEASE_WORK_REQUIRED_BEFORE_RUNTIME = FALSE
PR175_T3_FULL_PRODUCT_CONTENT_REQUIRED_BEFORE_RUNTIME = FALSE
```

따라서 PR175의 일곱 gap을 구현할 **기획 입력은 존재**한다. 그러나 프로젝트 전체 Phase A가 자동 완료된 것은 아니다. 전체 제품에서 open인 T3/이름/최종 tuning/release 영역은 그 책임 단계에 남아 있고, 사용자의 명시적 `기획 완료` 선언도 아직 없다.

## 10. Source-derived vs inference

### 직접 source-derived

- active TokenSource는 물리 TokenInstance 축을 사용하고 source당 릴 1개, fractional weight workaround 금지.
- runtime role output 뒤 deterministic measurement/FV 비교가 수행되어야 함.
- final parameter/product numerics는 아직 미선택·미승인.
- platform save/adapters/export/store는 architecture의 후속 단계이며 current state는 NOT_STARTED/ABSENT/NOT_RUN.
- Archer T3는 later approved correction으로 석궁병/연사궁병 두 분기.

### 이 review의 dependency-classification inference

```text
SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
T3_CONTENT_AND_FINAL_NAMES = FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER
```

이 inference는 새 확률·수치·T3 content·release 완료를 승인하지 않는다. 목적은 current Phase A에서 의존성 방향을 뒤집지 않는 것이다.

## 11. 다음 Gate

```text
PR175_PHASE_A_READINESS_REVIEW = CLASSIFIED
WHOLE_PROJECT_PHASE_A_OPEN_CONTENT_INVENTORY = CONTINUE
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
PHASE_C_BLOCKED
```
