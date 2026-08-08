# [승인] OMENWARD 병영 10,000-seed Decision Sweep 실행 전 식별성 검토

```yaml
updated_at: 2026-08-08
decision_id: OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-DECISION-SWEEP-REVIEW-V1
parent_decision_id: OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1
status: REVIEW_COMPLETE / PARAMETER_SELECTION_NOT_IDENTIFIABLE / EXECUTION_NOT_AUTHORIZED
approval: USER_APPROVED_RECOMMENDED_REVIEW_PATH
approval_count: 6_OF_10_REVIEW
scope: ANALYSIS_REVIEW_ONLY
product_code_authority: NONE
```

## 1. 결론

현재 2,000-seed 결과는 10,000-seed를 **최종 파라미터 벡터 선택용 decision sweep**으로 바로 실행하기에 충분한 식별성을 제공하지 않는다.

```text
DECISION_SWEEP_10000_EXECUTION = NOT_AUTHORIZED
PARAMETER_SELECTION = NOT_IDENTIFIABLE_WITH_CURRENT_DECISION_METRICS
ROBUSTNESS_ONLY_10000 = OPTIONAL_AFTER_SEPARATE_APPROVAL
FINAL_PARAMETER_VECTOR = NOT_SELECTED
CONFIRMATION_SWEEP_50000 = BLOCKED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
```

2,000-seed PASS를 뒤집는 판정이 아니다. 5/10 remediation smoke는 계속 PASS다. 이번 review는 **seed 수를 늘리는 것과 모델이 실제로 구분 가능한 정보를 늘리는 것은 다르다**는 경계를 확정한다.

## 2. 재현 가능한 근거

PR164에서 보존한 `smoke_sweep_2000.v2.csv`의 9개 벡터는 모두 `decision_failed_thresholds = []`다. 현재 combat-dependent diagnostic을 제외한 decision-eligible 축은 사실상 다음 네 항목이다.

```text
SPECIAL_TOKEN_SHARE_10_MIN
SPECIAL_TOKEN_SHARE_BURST_MAX
SECOND_SPECIAL_MARGINAL_VALUE_RATIO
REROLL_EXPECTED_VALUE_GAIN
```

`REROLL_EXPECTED_VALUE_GAIN`은 계약상 모든 벡터에서 `0.0`이다. 나머지 세 값으로 서명을 만들면 다음 동률 그룹이 재현된다.

```text
V03_CHEAP_SLOW_LOW
V04_CHEAP_SLOW_HIGH
=> 0.296796 / 0.333333 / 0.000000

V05_EXPENSIVE_FAST_LOW
V06_EXPENSIVE_FAST_HIGH
V07_EXPENSIVE_SLOW_LOW
V08_EXPENSIVE_SLOW_HIGH
=> 0.189250 / 0.333333 / 0.000000
```

따라서 10,000 seeds로 Monte Carlo 오차를 줄여도 **현재 출력 함수가 같은 벡터들 사이에 새로운 선택 목적함수나 관측량이 생기지 않는다**. 이 상태에서 하나를 최종값으로 고르면 false precision이다.

## 3. 전투 diagnostic 경계 유지

다음 raw 값은 계속 보존하지만 parameter-selection 점수로 승격하지 않는다.

```text
GENERAL_PATH_VALIDITY_RATE = DIAGNOSTIC_NON_IDENTIFIABLE
EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE = DIAGNOSTIC_NON_IDENTIFIABLE
WORST_SPECIAL_REGRET_RATE = DIAGNOSTIC_NON_IDENTIFIABLE
SPECIAL_OPTION_DOMINANCE_RATE = DIAGNOSTIC_NON_IDENTIFIABLE
MULTI_SPECIAL_DOMINANCE_RATE = DIAGNOSTIC_NON_IDENTIFIABLE
```

제품 HP/DPS/사거리/방어탑 출력/지휘 오라 계수/전술 출력이 없는 상태에서 `COMBAT_POWER_SCALAR`나 `SUPPORT_TU`를 다시 주입해 벡터를 구분하지 않는다.

## 4. 10k의 허용 가능한 미래 역할

10k 실행은 별도 승인 후 두 역할 중 하나로만 정의할 수 있다.

### A. Robustness-only sweep

현재 승인된 경제·물리 릴 invariant가 더 많은 seed에서도 유지되는지 검증한다.

```text
PURPOSE = ROBUSTNESS_ONLY
MAY_CONFIRM = TOKEN_SHARE / TOKEN_BURST / ECONOMY_AND_PRODUCTION_SCREENING
MAY_NOT_SELECT = FINAL_PARAMETER_VECTOR
MAY_NOT_APPROVE = PRODUCT_NUMERICS
```

### B. Parameter-selection decision sweep

실행 전에 반드시 선택 목적함수와 tie-break를 먼저 승인해야 한다.

최소 요구사항:

1. 비용 multiplier, 생산간격 multiplier, 기능가치 index 중 실제 선택하려는 각 차원에 대해 decision-eligible observable이 존재하거나, 식별 불가능한 차원을 명시적으로 범위에서 제거한다.
2. 새 observable은 정본 근거를 가져야 하며 임의 combat-support scalar로 대체할 수 없다.
3. 9개 벡터가 모두 threshold PASS일 때 무엇을 우선하는지 목적함수/Pareto/tie-break를 seed 실행 전에 고정한다.
4. 10k 결과를 본 뒤 선택 규칙을 바꾸는 post-hoc optimization은 금지한다.

## 5. 현재 권장 다음 Gate

```text
NEXT_GATE = BARRACKS_PARAMETER_SELECTION_OBSERVABLES_DEFINITION
```

이 Gate에서는 제품 수치를 바로 확정하지 않는다. 다음 둘 중 하나를 결정한다.

- canon-backed observable과 사전 선택 규칙을 정의해 10k parameter-selection sweep을 식별 가능하게 만든다.
- 현재 단계에서 식별할 수 없는 기능가치/전투 차원을 후속 제품 전투 수치 Gate까지 명시적으로 보류하고, 10k는 robustness-only로 제한한다.

## 6. 변경하지 않는 것

```text
BARRACKS_5_OF_10_REMEDIATION_SMOKE = PASS
SECOND_SPECIAL_TOKEN_SOURCE_GUARD = UNCHANGED
PHYSICAL_TOKEN_INSTANCE_GRAMMAR = UNCHANGED
SPECIAL_TOKEN_SHARE_BURST_CAP = 0.45
COMBAT_POWER_SCALAR = FORBIDDEN
SUPPORT_TU_NUMERIC_INJECTION = FORBIDDEN
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
GAMEPLAY_DATA = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```
