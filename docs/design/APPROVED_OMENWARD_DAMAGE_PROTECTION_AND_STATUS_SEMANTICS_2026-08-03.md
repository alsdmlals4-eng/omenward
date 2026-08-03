# OMENWARD Damage·Protection·Status Semantics

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
numeric_child_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
grill_me_count_when_approved: 3_OF_10
current_grill_me_count: 4_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD 전투의 피해 계약은 2개 피해 채널과 독립된 전달·대상 분류로 구성한다.

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
DAMAGE_CHANNEL = exactly one of [KINETIC, ARCANE]
DELIVERY_TAGS = zero or more of [BASIC, SKILL, AREA, DAMAGE_OVER_TIME, ENVIRONMENT, TRANSFERRED]
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING eligibility
```

현 버티컬 슬라이스 기본 경계:

```text
TRUE_DAMAGE = FORBIDDEN
EXECUTE_OR_INSTANT_KILL = FORBIDDEN
REVIVE = FORBIDDEN
FRIENDLY_FIRE = FORBIDDEN_BY_DEFAULT
SELF_DAMAGE = FORBIDDEN_BY_DEFAULT
OBJECTIVE_HP_DAMAGE = FORBIDDEN_BY_DEFAULT
```

## 2. 제품 코어 연결

이 계약은 상성표를 늘리기 위한 것이 아니다. 세 전선 공세를 읽고 룰렛·TokenSource로 만든 병력을 Armor/Resistance 대응에 맞춰 비가역 배치하며, 전투 결과를 provenance와 event로 설명하기 위한 최소 방어축이다.

```text
공세 KINETIC / ARCANE 확인
→ 대응 병력·건물 선택
→ SpinSnapshot 결과를 전선에 commit
→ 공통 Damage·Protection·Status resolver
→ root_effect_id·deployment_id 기반 복기
→ 다음 Stage 릴·건물 설계
```

## 3. 권위 계층

의미 권위는 이 문서가 소유한다.

정확 공식·cap·duration·초기 수치 권위는 다음 자식 문서가 소유한다.

`APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`

충돌 시:

```text
Damage/Protection/Status의 의미·순서 → 이 문서
정확 방어식·Barrier/Redirection/Floor/Status 기본 수치 → Numeric Defaults 문서
fixed tick·ms 변환·activation → 후속 Decision
영웅·병종별 실제 값 → 후속 content parameter Decision
```

## 4. 공통 Intent Schema

### DamageIntent

```text
intent_id
root_effect_id
source_id / original_source_id
target_id
commit_id
impact_tick / impact_sequence
damage_channel
delivery_tags
raw_amount_q
source_modifier_refs / target_modifier_refs
target_profile_requirement
mitigation_policy
barrier_policy
hp_loss_redirection_policy
health_floor_policy
post_hit_payload_refs
deployment_id_if_applicable
```

### RestoreIntent

```text
intent_id
root_effect_id
source_id / target_id
restore_amount_q
restore_category
max_hp_clamp_policy
overheal_policy
status_payload_refs
```

Restore는 음수 DamageIntent가 아니다.

### ProtectionIntent

```text
intent_id
source_id / target_id
protection_type
start_time / end_time_exclusive
remaining_budget_q
channel_filter / delivery_filter
consume_priority
spillover_policy
health_floor_q_if_any
```

```text
PROTECTION_TYPE = BARRIER | IMMUNITY | HEALTH_FLOOR | HP_LOSS_REDIRECTION
```

### StatusApplicationIntent

```text
intent_id
source_id / target_id
status_definition_id
status_family
start_time / end_time_exclusive
stacking_group_id
stacking_policy
stack_delta
payload
```

Stacking policy가 없으면 fixture와 data는 invalid다.

## 5. Channel·Tag·Target 분리

```text
KINETIC_AREA != third channel
ARCANE_DOT != third channel
FLYING_DAMAGE != third channel
SIEGE_DAMAGE != third channel
```

한 action이 두 채널을 사용하면 두 개의 명시적 DamageIntent로 나눈다. delivery tag나 VFX 색상·병종 이름으로 channel을 추론하지 않는다.

```text
ENTITY_CLASS = UNIT | BUILDING | OBJECTIVE
MOVEMENT_CLASS = GROUND | FLYING
SIDE_RELATION = ALLY | ENEMY | SELF
```

Objective 소유권은 기본적으로 `R100 OBJECTIVE_AND_OWNERSHIP_RESOLVE`가 소유한다.

## 6. R80 내부 의미 순서

```text
R80A VALIDITY_AND_ELIGIBILITY
R80B PROTECTION_SETUP
R80C DAMAGE_MITIGATION_AND_BARRIER
R80D HP_LOSS_REDIRECTION_AND_FLOOR
R80E HP_DELTA_AND_RESTORE
R80F STATUS_APPLICATION_AND_POST_HIT_QUEUE
R80G DEATH_OR_DESTRUCTION_MARK
```

### R80A

- target·side·entity class·ground/flying·immunity를 검사한다.
- 무효·면역은 이유 event를 남긴다.

### R80B

- R60에서 합법적으로 commit된 same-tick ProtectionIntent를 공통 snapshot에 materialize한다.
- entity ID 처리 순서로 보호 획득 여부가 바뀌지 않는다.

### R80C

```text
raw
→ outgoing/incoming modifier
→ KINETIC: Armor | ARCANE: Resistance
→ Barrier
→ candidate HP loss
```

정확 방어식과 Barrier 수치는 Numeric Defaults 문서가 소유한다.

### R80D

- Barrier 흡수량은 HP loss가 아니다.
- HP loss만 명시적으로 재배분한다.
- 재배분 양은 방어·Barrier를 다시 통과하지 않는다.
- Health Floor는 재배분 뒤 batch에 적용한다.

### R80E

- Damage와 Restore를 별도 event로 적용한다.
- 기본 overheal은 폐기한다.
- dead·death_pending을 revive하지 않는다.

### R80F

- 새 Control status는 이미 commit된 same-tick action을 소급 취소하지 않는다.
- 일반 Status의 이동·target·action 제한은 다음 관련 phase부터 적용한다.
- 즉시 보호는 ProtectionIntent로 표현한다.

### R80G

- `death_pending`만 표시하며 실제 death·destruction finalize는 R90이 소유한다.

## 7. Barrier·Redirection·Floor 의미

```text
BARRIER != HP
BARRIER != HEAL
BARRIER != ARMOR_OR_RESISTANCE
TRANSFER_DEPTH_MAX = 1
RECURSIVE_REDIRECTION = FORBIDDEN
SECOND_MITIGATION_PASS = FORBIDDEN
ROOT_EFFECT_ID_PRESERVED = REQUIRED
```

- Barrier는 mitigation 뒤 남은 피해를 흡수하는 임시 budget이다.
- HP-loss redirection은 최종 후보 손실의 재배분이며 새 공격이 아니다.
- Health Floor는 damage clamp이며 HP를 증가시키지 않는다.
- exact ratio·cap·duration·Floor 값은 Numeric Defaults 문서가 소유한다.

## 8. Restore·Status 의미

```text
RESTORE != NEGATIVE_DAMAGE
OVERHEAL_DEFAULT = DISCARDED
REVIVE = FORBIDDEN
```

Status family:

```text
STAT_MODIFIER
CONTROL
DAMAGE_OVER_TIME
HEAL_OVER_TIME
IMMUNITY
TARGETING_RULE
MOVEMENT_RULE
MARK
```

Stacking policy:

```text
REPLACE_IF_STRONGER
REFRESH_DURATION
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

정확 stack cap·pulse·Control duration·lockout은 Numeric Defaults 문서가 소유한다.

## 9. Event·Metric 계약

```text
RAW_DAMAGE
!= ADJUSTED_DAMAGE
!= POST_MITIGATION_DAMAGE
!= BARRIER_ABSORBED
!= FINAL_HP_LOSS
!= RESTORE_APPLIED
```

모든 event는 가능한 경우 다음을 보존한다.

```text
root_effect_id
source_id / original_source_id
target_id
damage_channel / delivery_tags
tick / phase / sequence
deployment_id
rejection_or_clamp_reason
```

## 10. 검증 계약

```text
T0 = channel/tag/profile·Intent·stacking schema
T1 = 동일 fixture의 단계별 event·fingerprint parity
T2 = same-tick 보호·Barrier·이전·Floor·Status invariants
T3 = 세 전선 전체 paired A/B/C metrics
```

제품·Simulation tool 구현과 실행은 별도 승인 전 금지한다.

## 11. 적대적 검토

```text
OMW-AUD-233 = channel/tag conflation
OMW-AUD-234 = flying-as-damage-type
OMW-AUD-235 = Barrier double counting
OMW-AUD-236 = recursive transfer
OMW-AUD-237 = second mitigation
OMW-AUD-238 = retroactive Status cancellation
OMW-AUD-239 = missing stacking policy
OMW-AUD-240 = hidden immunity
OMW-AUD-241 = Restore as negative damage
OMW-AUD-242 = true/execute/revive bypass
OMW-AUD-243 = accidental Objective damage
OMW-AUD-244 = Barrier overcentralization
OMW-AUD-245 = color-only accessibility
OMW-AUD-246 = raw/final metric double count
```

수치 관련 후속 감사는 `OMW-AUD-247~260`이 소유한다.

## 12. 경계·다음 Gate

```text
DAMAGE_SEMANTICS = USER_APPROVED_DOCUMENTED_NOT_IMPLEMENTED
NUMERIC_DEFAULTS = USER_APPROVED_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
FIXED_TICK_RATE = PENDING
MS_TO_TICK_CONVERSION = PENDING
SOURCE_TARGET_MODIFIER_STACKING = PENDING
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
CURRENT_GRILL_ME_COUNT = 4/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
