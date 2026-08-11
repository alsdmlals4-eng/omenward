# [현행] OMENWARD Elite 최종 Wave·Boss Stage cadence 승인안

```yaml
decision_id: OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1
approved_at: 2026-08-11 KST
approval: USER_DIRECT_CHANGE_AUTHORIZATION
status: USER_APPROVED / CURRENT_PLANNING_CANON / NOT_IMPLEMENTED
work_phase: PHASE_A_GPT_CHAT_PLANNING
supersedes_current_cadence_from: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
ELITE_PRESENCE_REQUIRED = TRUE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_BOSS_PRESENCE_REQUIRED = TRUE
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING
ELITE_EXACT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
BOSS_EXACT_ENTRY_WAVE_AND_NUMERICS = CONTENT_AND_RUNTIME_EVIDENCE_TUNING
```

- 별도 `Danger Stage` 타입과 4/9/14/19 cadence를 제거한다.
- Stage 1~20 모두 마지막 Wave에 Elite를 반드시 포함한다.
- Stage 5/10/15/20은 Boss Stage다.
- Boss Stage에도 공통 최종 Wave Elite 규칙이 적용되므로 Boss + Elite 위협이 함께 존재한다.
- 정확한 Elite 수, Elite 스탯, Boss 스탯, 정확한 spawn 초·entry wave는 지금 확정하지 않는다.

## 2. Elite의 역할

Elite는 `HP만 높은 일반 적`이 아니다.

```text
ELITE_ROLE = STAGE_LEARNING_CHECK_AND_ESCALATION
ELITE_HP_ONLY_VARIANT = AVOID
ELITE_MUST_REFLECT_STAGE_PRESSURE = TRUE
```

- 해당 Stage에서 이미 보여준 주·보조 압력의 이해를 마지막 Wave에서 더 강하게 시험한다.
- 플레이어가 Stage 안에서 읽은 대응축을 다시 적용하거나 우선순위를 바꾸게 해야 한다.
- 숨은 공격 Layer, 숨은 Route, 전투 도중 갑자기 생긴 필수 단일 카운터로 난도를 만들지 않는다.
- Elite의 exact archetype·modifier pool은 후속 콘텐츠/런타임 evidence로 조정한다.

## 3. Boss의 역할

```text
BOSS_ROLE = ACT_LEVEL_SYNTHESIS_TEST
BOSS_IS_NOT_ELITE_REPLACEMENT = TRUE
BOSS_HP_BAG_ONLY = FORBIDDEN
```

- Boss는 Elite를 대체하지 않는다.
- Boss는 5-Stage 단위로 누적된 전선·건물·TokenSource·병종·전술 선택을 종합 시험한다.
- 단순 HP/공격력 증가만으로 Boss를 정의하지 않는다.
- Route, 목표 우선순위, 호위, 취약창, 전선 커밋 중 하나 이상을 플레이어가 읽을 수 있는 방식으로 변화시켜야 한다.
- 다음 치명적 패턴과 대응 단서는 사전에 읽을 수 있어야 한다.

## 4. Stage 문법

### 일반 Stage: 1~4 / 6~9 / 11~14 / 16~19

```text
Wave 1 = pressure introduction or current-stage opening test
Wave 2 = complication / secondary pressure / route variation
Final Wave = commitment test + Elite
```

마지막 Wave의 Elite는 해당 Stage가 요구한 선택을 명확하게 종결한다.

### Boss Stage: 5 / 10 / 15 / 20

```text
Boss presence = REQUIRED
Final Wave Elite presence = REQUIRED
Boss + Elite = REQUIRED_WITH_READABLE_PRESSURE_BUDGET
```

- Boss와 Elite가 동시 또는 같은 Stage에서 순차적으로 출현할 수 있으나 정확한 entry wave/초는 후속 evidence가 결정한다.
- 두 위협을 단순 합산해 대응 불가능한 burst로 만들지 않는다.
- Boss Stage 시작 전에 Boss의 핵심 위협, Elite 존재, 치명적 Route/Layer/목표를 예고한다.

## 5. 기존 4/9/14/19 아이디어의 처리

구형 current cadence:

```text
DANGER_STAGES = 4 / 9 / 14 / 19
```

은 이 Decision으로 대체된다.

다만 2026-08-04 pressure matrix에 있던 다음 authored 아이디어는 **일반 Stage 변주 후보**로 재사용할 수 있다.

- 공개된 우회 Route.
- 공개된 Wave overlap timetable.
- 공개된 주 전선 이동.
- 공개된 Route convergence.

```text
LEGACY_DANGER_RULE_VARIATIONS = OPTIONAL_NORMAL_STAGE_AUTHORED_VARIATIONS
LEGACY_DANGER_CADENCE_AUTHORITY = NONE
```

이 아이디어를 재사용하더라도 특별 `Danger Stage` 타입을 다시 만들거나 4/9/14/19를 자동 privilege cadence로 복원하지 않는다.

## 6. 공정성·예고 계약

```text
ELITE_FORECAST_REQUIRED = TRUE
BOSS_FORECAST_REQUIRED = TRUE
HIDDEN_REQUIRED_COUNTER = FORBIDDEN
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
```

- 마지막 Wave에 Elite가 온다는 사실은 Stage UX에서 이해 가능해야 한다.
- Boss Stage는 5/10/15/20이라는 landmark를 플레이어가 학습할 수 있게 유지한다.
- Elite/Boss는 기존 비가역 배치를 예고 없이 무가치하게 만들지 않는다.
- 최소 두 대응축을 유지하는 quality guardrail을 따른다.

## 7. 반복성·seed와의 관계

```text
ELITE_CADENCE_FIXED = EVERY_STAGE_FINAL_WAVE
BOSS_CADENCE_FIXED = 5 / 10 / 15 / 20
SEED_CAN_VARY_ELITE_IDENTITY = TRUE
SEED_CAN_VARY_PRESSURE_COMPOSITION = TRUE
SEED_CAN_HIDE_CORE_THREAT = FALSE
```

- cadence는 학습 가능한 고정 landmark다.
- seed는 Elite identity, 압력 조합, Route, 적 변형을 바꿀 수 있다.
- seed 결과가 결정된 뒤 필요한 핵심 정보는 전투 시작 전에 공개한다.

## 8. 콘텐츠 수치 경계

지금 선택하지 않는 값:

```text
ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING
ELITE_HP_MULTIPLIER = NOT_SELECTED
ELITE_DAMAGE_MULTIPLIER = NOT_SELECTED
ELITE_MODIFIER_POOL = NOT_SELECTED
BOSS_HP = NOT_SELECTED
BOSS_DAMAGE = NOT_SELECTED
BOSS_EXACT_ENTRY_WAVE = NOT_SELECTED
BOSS_EXACT_ENTRY_SECOND = NOT_SELECTED
THREAT_BUDGET = NOT_SELECTED
```

이 값들은 deterministic simulation/runtime measurement와 human playtest 뒤 별도 승인 또는 승인된 tuning 절차에서 정한다.

## 9. 대체 관계

이 Decision이 current authority가 된 뒤:

```text
OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
= SUPERSEDED_FOR_STAGE_TYPE_AND_CADENCE
= HISTORICAL_AUTHORED_PRESSURE_LINEAGE_ONLY
IMPLEMENTATION_INPUT_FOR_CURRENT_PHASE = FORBIDDEN
```

다섯 pressure taxonomy 자체는 유지한다.

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

기존 20 Stage 학습곡선의 개별 Stage 이름·압력 조합은 후속 current 콘텐츠 매트릭스에서 이 cadence에 맞게 재라우팅할 수 있으며, 이 Decision만으로 exact enemy count나 threat budget을 확정하지 않는다.

## 10. 상태 경계

```text
ELITE_BOSS_CADENCE = APPROVED
DANGER_STAGE_TYPE = REMOVED
PRODUCT_CODE = UNCHANGED
GODOT_MUTATION = NONE
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PHASE_A = ACTIVE
PHASE_C = BLOCKED
```
