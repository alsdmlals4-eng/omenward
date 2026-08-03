# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: MODIFIER_STACKING_AND_EFFECT_PRECEDENCE_APPROVED
current_validation_decision: OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
parent_time_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
working_branch: gpt/omenward-simulation-harness-planning-20260803
current_grill_me_count: 6_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_qa: NOT_RUN
```

## 1. 먼저 읽을 문서

```text
PROJECT_CORE.md
ACTIVE_CONTEXT.md
CURRENT_IMPLEMENTATION_STATUS.md
DOCUMENTATION_MAP.md
PROJECT_CANON_DECISION_LEDGER.md
DECISIONS_PENDING.md
```

현재 책임 원본:

```text
design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md
design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md
design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md
design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md
design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md
design/APPROVED_OMENWARD_MODIFIER_STACKING_AND_EFFECT_PRECEDENCE_2026-08-03.md
```

전체 시스템 제품 범위는 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`가 소유한다.

## 2. 제품 코어

```text
예고된 세 전선 공세
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ SpinSnapshot 결과
→ 비가역 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 provenance 복기
→ 다음 Stage 설계
```

Harness와 전투 기술 계약은 이 핵심 재미를 대체하지 않는다.

## 3. 현재 승인된 기술 기획 Stack

```text
P0 Deterministic Harness Scope
P1 Core-First Common Combat Schema
P2 Damage/Protection/Status Semantics
P3 Mitigation/Protection Numeric Defaults
P4 Fixed Tick/Time/Activation Defaults
P5 Modifier Stacking/Effect Precedence
```

## 4. Modifier 핵심

```text
SOURCE_OUTGOING = 50%~150%
TARGET_INCOMING = 50%~150%
COMBINED_PRE_DEFENSE = 25%~200%
R60 = source snapshot
R80 = target snapshot
```

```text
REFRESH_DURATION
REPLACE_IF_STRONGER
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

Armor·Resistance는 integer point additive만 허용한다. Generic flat damage·override·penetration·next-hit 소비형 Modifier는 금지한다.

## 5. Effect Precedence

```text
P00 validity
→ P10 immunity
→ P20 source snapshot
→ P30 target incoming
→ P40 defense
→ P50 Barrier
→ P60 redirection
→ P70 Health Floor
→ P80 HP/Restore
→ P90 Status/post-hit
→ P100 death pending
```

Transferred HP loss는 두 번째 Modifier·mitigation·Barrier pass를 거치지 않는다.

## 6. Trigger 의미

```text
ON_VALID_IMPACT
ON_POST_MITIGATION_DAMAGE
ON_BARRIER_ABSORBED
ON_FINAL_HP_LOSS
ON_STATUS_APPLIED
ON_TARGET_DEATH_FINALIZED
```

`on hit` 단독 문자열과 영웅 직접 HP 변경은 금지한다.

## 7. 시간·전투 핵심

```text
DOMAIN_TPS = 30
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
SPAWN_AT_T → ACTIVATE_AT_T_PLUS_1
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
DEATH_FINALIZE_AFTER_DAMAGE_BATCH
OBJECTIVE_USES_POST_DEATH_ACTIVE_SURVIVORS
SAVE = AFTER_R130_ONLY
WALL_CLOCK_TIMER_ANIMATION_CALLBACK = NON_AUTHORITATIVE
```

## 8. 적대적 감사

```text
OMW-AUD-208~220 Harness
OMW-AUD-221 Sheet HEAD correction / resolved / non-counter
OMW-AUD-222~232 Common Combat
OMW-AUD-233~246 Damage Semantics
OMW-AUD-247~260 Numeric Defaults
OMW-AUD-261 CI compatibility restore / resolved / non-counter
OMW-AUD-262~275 Time/Activation
OMW-AUD-276~289 Modifier/Precedence
```

P5 주요 위험은 배율 순서 의존, source snapshot drift, target response 무시, duplicate 폭증, family cap 우회, 모호한 on-hit, transferred second pass, 영웅 direct HP mutation이다. 정본에서 차단했으나 구현·T1/T2 검증은 아직 실행되지 않았다.

## 9. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MODIFIER_STACKING_EFFECT_PRECEDENCE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
GDSCRIPT_SCENE_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 작업

다음 사용자 Decision:

```text
OMW-DEC-20260803-VALIDATION-SPATIAL-QUANTIZATION-MOVEMENT-AND-TARGETING-DEFAULTS-V1
```

검토 범위:

- quantized 2D integer scale.
- movement·range의 tick당 변환.
- lane anchor·segment·frontline 관계.
- same-lane/cross-lane targeting.
- ground/flying layer·collision.
- distance metric·range boundary.
- movement batch·blocking·swap.
- target filter·priority·tie-break.

```text
NEXT_GRILL_ME = 7/10
NEXT_PREFLIGHT = AT_10_OF_10
```
