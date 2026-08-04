# OMENWARD Mitigation Formula·Protection Numeric Defaults

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
child_time_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
grill_me_count: 4_OF_10
current_branch_counter: 5_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

Armor와 Resistance는 같은 쌍곡선 감소 공식을 사용한다.

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
EFFECTIVE_DEFENSE_MIN = 0
EFFECTIVE_DEFENSE_MAX = 300
MITIGATION_CONSTANT = 100
MINIMUM_VALID_DAMAGE = 1
ROUNDING = POSITIVE_INTEGER_HALF_UP
NEGATIVE_DEFENSE = FORBIDDEN
ARMOR_AND_RESISTANCE_CURVE = IDENTICAL
```

Barrier·HP-loss redirection·Health Floor·Status의 최초 제작 기본값도 이 문서가 소유한다. ms→Tick 변환과 활성 구간은 하위 시간 책임 원본이 소유한다.

## 2. 제품 코어 연결

```text
세 전선 KINETIC/ARCANE 공세 확인
→ Armor/Resistance 대응 병력·건물 선택
→ 룰렛 결과를 비가역 전선 배치
→ 공통 공식·보호·상태 처리
→ raw→final Event 복기
→ 다음 Stage 설계
```

방어·Barrier·Control이 룰렛·전선 선택을 대체하면 공식에 맞더라도 실패다.

## 3. 범위

### 포함

- Armor·Resistance 공통 감소 공식과 0~300 clamp.
- positive integer half-up과 최소 유효 피해.
- Barrier 단일 적용 cap·전체 cap·지속시간·소비 순서.
- Barrier cap 기준 시점과 초과분 폐기.
- HP-loss redirection 비율·recipient 수·무효 recipient 정책.
- Health Floor 값·발동 횟수·동일 Tick batch 처리.
- Status stack cap·DOT/HOT pulse·Control duration·lockout ms 값.
- Barrier overcentralization 조기 guard.

### 제외

- source outgoing·target incoming modifier stacking.
- 관통·방어 무시·critical·lifesteal·overheal conversion.
- true damage·execute·revive.
- 병종·영웅·건물별 실제 능력치.
- 이동속도·사거리·position scale.
- GDScript·Resource·fixture·test 구현.
- Simulation·Runtime·Human QA와 밸런스 결론.

```text
DEFENSE_PENETRATION = FORBIDDEN_UNTIL_SEPARATE_DECISION
PLACEHOLDER_PARAMETER_RESULT = EXPLORATORY_ONLY
```

## 4. 공통 방어 공식

```text
defense_axis = KINETIC ? armor_q : resistance_q
raw_effective_defense = base_defense_q + additive_buff_q - additive_debuff_q
effective_defense = clamp(raw_effective_defense, 0, 300)
denominator = 100 + effective_defense
```

```text
if adjusted_damage_q <= 0:
    post_mitigation_damage_q = 0
else:
    numerator = adjusted_damage_q * 100
    rounded = (numerator + floor(denominator / 2)) div denominator
    post_mitigation_damage_q = max(1, rounded)
```

- 모든 전투 수치는 정수다.
- 양수 입력만 최소 피해 1을 만든다.
- 무효 대상·면역·0 피해에 최소 피해를 강제하지 않는다.
- float·플랫폼별 rounding을 deterministic critical path에서 금지한다.

대표 통과·감소:

| Defense | 통과 비율 | 감소율 |
|---:|---:|---:|
| 0 | 100/100 | 0% |
| 25 | 100/125 | 20% |
| 50 | 100/150 | 약 33.3% |
| 100 | 100/200 | 50% |
| 200 | 100/300 | 약 66.7% |
| 300 | 100/400 | 75% |

## 5. Barrier 기본값

```text
PER_APPLICATION_CAP_RATIO = 20_PERCENT_OF_TARGET_MAX_HP
TOTAL_BARRIER_CAP_RATIO = 30_PERCENT_OF_TARGET_MAX_HP
DEFAULT_BARRIER_DURATION_MS = 3000
DEFAULT_BARRIER_DURATION_TICKS = 90
EXCESS_BARRIER = DISCARDED
BARRIER_CAP_ROUNDING = FLOOR
CONSUME_ORDER = consume_priority ASC → start_tick ASC → protection_id ASC
```

적용 시:

```text
per_application_cap_q = floor(max_hp_q * 20 / 100)
total_cap_q = floor(max_hp_q * 30 / 100)
remaining_capacity_q = max(0, total_cap_q - active_barrier_budget_q)
accepted_q = min(requested_q, per_application_cap_q, remaining_capacity_q)
discarded_q = requested_q - accepted_q
```

- 적용 당시 max HP로 cap을 고정한다.
- 이후 max HP 변화가 기존 budget을 소급 절단하지 않는다.
- mitigation 뒤 피해를 흡수한다.
- HP·Heal·Armor·Resistance가 아니다.
- `accepted_q <= 0`이면 instance를 만들지 않는다.
- 만료 범위는 `[start_tick,end_tick_exclusive)`이며 90 Tick이다.

조기 guard:

```text
FRONTLINE_MEAN_BARRIER_UPTIME > 40_PERCENT
OR
BARRIER_ABSORBED / POST_MITIGATION_INCOMING_DAMAGE > 35_PERCENT
```

이는 최종 합격선이 아니라 과집중 후보 분류다.

## 6. HP-Loss Redirection

```text
DEFAULT_REDIRECTION_RATIO = 30_PERCENT
MAX_REDIRECTION_RECIPIENTS = 1
ORIGINAL_TARGET_RETAINS_RATIO = 70_PERCENT
INVALID_RECIPIENT_POLICY = RETURN_TO_ORIGINAL_TARGET
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS = FORBIDDEN
```

```text
redirected_q = (candidate_hp_loss_q * 30 + 50) div 100
original_remainder_q = candidate_hp_loss_q - redirected_q
```

- 뺄셈 remainder로 총량을 보존한다.
- recipient가 무효면 원래 대상에 반환한다.
- 반환·이전 양은 방어와 Barrier를 다시 통과하지 않는다.
- root effect·original source·deployment provenance를 유지한다.

## 7. Health Floor

```text
DEFAULT_HEALTH_FLOOR_Q = 1_HP
HEALTH_FLOOR_TRIGGER_COUNT = 1_PER_PROTECTION_INSTANCE
HEALTH_FLOOR_EXCLUSIVE_GROUP = CORE_HEALTH_FLOOR
MULTIPLE_ACTIVE_CORE_FLOORS = FORBIDDEN
```

같은 Tick의 개별 hit 순서가 아니라 target별 최종 loss batch에 적용한다.

```text
aggregate target loss
→ apply one active Floor clamp
→ consume only when prevented loss > 0
→ emit final HP delta
```

Floor는 Heal·Death·Revive 시스템이 아니다.

## 8. Status 기본값과 Tick 변환

```text
DEFAULT_ADD_STACKS_CAP = 3
DEFAULT_DOT_HOT_PULSE_INTERVAL_MS = 1000
DEFAULT_DOT_HOT_PULSE_INTERVAL_TICKS = 30
MAX_SINGLE_CONTROL_DURATION_MS = 2000
MAX_SINGLE_CONTROL_DURATION_TICKS = 60
SAME_CONTROL_GROUP_LOCKOUT_MS = 1000
SAME_CONTROL_GROUP_LOCKOUT_TICKS = 30
```

### DOT/HOT

```text
first_due_tick = start_tick + 30
next_due_tick = previous_due_tick + 30
emit only when due_tick < end_tick_exclusive
```

적용 Tick 즉시 pulse를 추가하지 않는다.

### Control

```text
control = [start_tick,end_tick_exclusive)
lockout = [end_tick_exclusive,end_tick_exclusive + 30)
```

Lockout 중 같은 `stacking_group_id`의 새 Control은 reason Event와 함께 거절한다. 이미 commit된 same-tick 행동을 소급 취소하지 않는다.

## 9. Event·Metric 계약

```text
RAW_DAMAGE_Q
ADJUSTED_DAMAGE_Q
EFFECTIVE_DEFENSE_Q
POST_MITIGATION_DAMAGE_Q
BARRIER_ABSORBED_Q
CANDIDATE_HP_LOSS_Q
REDIRECTED_HP_LOSS_Q
HEALTH_FLOOR_PREVENTED_Q
FINAL_HP_LOSS_Q
RESTORE_APPLIED_Q
STATUS_APPLIED_OR_REJECTED
```

```text
POST_MITIGATION_DAMAGE_Q >= BARRIER_ABSORBED_Q
CANDIDATE_HP_LOSS_Q = POST_MITIGATION_DAMAGE_Q - BARRIER_ABSORBED_Q
REDIRECTED_PLUS_REMAINDER = CANDIDATE_HP_LOSS_Q
FINAL_HP_LOSS_Q <= CANDIDATE_HP_LOSS_Q
```

## 10. Time Authority 위임

```text
DOMAIN_TPS = 30
DURATION_TICKS = CEIL(duration_ms * 30 / 1000)
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
```

정확 권위:

`design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md`

이 문서의 ms 값과 Tick 값이 충돌하면 시간 책임 원본의 변환·경계 규칙을 따른다. 승인된 네 값은 정확히 나뉘므로 rounding 차이는 없다.

## 11. Fixture·검증

### T0

- channel/defense axis 일치.
- defense 0~300.
- Barrier 20/30%, 3000ms/90 Tick.
- redirection recipient 1.
- Floor exclusive group.
- stack 3, pulse 30 Tick, Control 60 Tick, lockout 30 Tick.

### T1

- 동일 입력에서 모든 중간 정수 Event와 fingerprint 동일.
- float critical path 금지.

### T2

- defense 0/25/50/100/200/300 경계.
- 양수 최소 피해 1.
- Barrier cap·과잉 폐기·canonical consume.
- redirection 총량 보존.
- Floor batch와 1회 소비.
- expiry·pulse·lockout Tick fencepost.

### T3

- 세 전선 전체에서 Barrier uptime·absorption·final loss·Control uptime 분리.
- sample/tolerance 전까지 `EXPLORATORY_ONLY`.

## 12. 적대적 감사

```text
OMW-AUD-247 ~ 260 = numeric default risks
OMW-AUD-262 ~ 275 = time conversion and activation risks
```

핵심 방어:

- 음수 defense·무상한·float divergence 금지.
- Barrier dual cap·canonical consume.
- redirection mass conservation.
- same-tick Floor 순차 편향 금지.
- Control chain lockout.
- ms를 임의 Tick으로 변환하지 않고 승인된 30 TPS 변환 사용.

## 13. 구현 경계

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
GDSCRIPT_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 14. 다음 Gate

```text
CURRENT_BRANCH_COUNT = 5/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
