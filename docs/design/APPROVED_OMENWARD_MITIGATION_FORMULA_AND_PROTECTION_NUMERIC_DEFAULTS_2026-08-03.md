# OMENWARD Mitigation Formula·Protection Numeric Defaults

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
grill_me_count: 4_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD의 최초 공통 방어 수치 계약은 Armor와 Resistance가 같은 쌍곡선 감소 공식을 사용하는 구조로 확정한다.

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

Barrier·HP-loss redirection·Health Floor·Status의 최초 제작 기본값도 이 Decision에서 함께 확정한다.

## 2. 제품 코어와의 연결

이 수치 계약은 방어 수치를 쌓는 게임을 만드는 것이 아니다. 플레이어가 공세 예고에서 `KINETIC / ARCANE` 압력을 읽고 룰렛·건물·병력 조합으로 `ARMOR / RESISTANCE` 대응을 설계한 뒤, 비가역 전선 커밋의 결과를 설명할 수 있게 하는 최소 기준이다.

```text
세 전선 공세 채널 확인
→ 대응 방어축을 가진 병력·건물 선택
→ 룰렛 결과를 전선에 비가역 배치
→ 공통 공식으로 피해·Barrier·이전·상태 처리
→ event에서 raw→final 결과 복기
→ 다음 Stage 설계에 환류
```

방어·Barrier·Control이 세 전선 판단과 병종 선택을 대체하면 수치가 공식에 맞더라도 실패다.

## 3. 범위와 경계

### 포함

- Armor·Resistance 공통 감소 공식.
- defense clamp와 최소 유효 피해.
- 정수 반올림 방식.
- Barrier 단일 적용 cap·전체 cap·기본 지속시간·소비 순서.
- Barrier 과잉분 폐기와 cap 기준 시점.
- HP-loss redirection 기본 비율·recipient 수·무효 recipient 정책.
- Health Floor 값·발동 횟수·동일 tick batch 처리.
- Status 기본 stack cap·DOT/HOT pulse·Control 지속 상한·동일 group lockout.
- Barrier 과집중 조기 stop-ship guard.

### 제외

- source outgoing·target incoming modifier의 exact stacking 공식.
- Armor/Resistance 관통·감소·무시.
- critical hit·lifesteal·overheal conversion.
- true damage·execute·revive.
- 병종·영웅·건물별 실제 능력치.
- fixed-tick rate와 밀리초→tick 변환.
- movement·range·position quantization scale.
- GDScript·Resource·fixture·test 구현.
- simulation 실행과 최종 밸런스 결론.

```text
DEFENSE_PENETRATION = FORBIDDEN_UNTIL_SEPARATE_DECISION
PLACEHOLDER_PARAMETER_RESULT = EXPLORATORY_ONLY
```

## 4. 공통 방어 공식

### 4.1 입력

`adjusted_damage_q`는 상위 Damage Semantics의 source outgoing·target incoming modifier 단계가 끝난 비음수 정수다. 해당 modifier의 stacking 공식은 별도 Decision이 소유한다.

```text
defense_axis = KINETIC ? armor_q : resistance_q
raw_effective_defense = base_defense_q + additive_buff_q - additive_debuff_q
effective_defense = clamp(raw_effective_defense, 0, 300)
denominator = 100 + effective_defense
```

### 4.2 정수식

```text
if adjusted_damage_q <= 0:
    post_mitigation_damage_q = 0
else:
    numerator = adjusted_damage_q * 100
    rounded = (numerator + floor(denominator / 2)) div denominator
    post_mitigation_damage_q = max(1, rounded)
```

- 모든 값은 비음수 정수다.
- `div`는 정수 나눗셈이다.
- 양수 입력에서 `(numerator + floor(denominator / 2)) div denominator`는 half-up 반올림을 구현한다.
- 최소 피해 1은 방어 공식 뒤, Barrier 흡수 전 적용한다.
- 무효 target·면역·0 이하 입력에는 최소 피해를 강제로 만들지 않는다.
- Armor와 Resistance는 동일한 상수·clamp·rounding을 사용한다.

### 4.3 대표 감소율

| Effective Defense | 통과 피해 비율 | 대표 감소율 |
|---:|---:|---:|
| 0 | 100 / 100 | 0% |
| 25 | 100 / 125 | 20% |
| 50 | 100 / 150 | 약 33.3% |
| 100 | 100 / 200 | 50% |
| 200 | 100 / 300 | 약 66.7% |
| 300 | 100 / 400 | 75% |

방어 300 이후 수치는 clamp되므로 추가 감소를 얻지 않는다.

## 5. Barrier 기본값

```text
TOTAL_BARRIER_CAP_RATIO = 30_PERCENT_OF_TARGET_MAX_HP
PER_APPLICATION_CAP_RATIO = 20_PERCENT_OF_TARGET_MAX_HP
DEFAULT_BARRIER_DURATION_MS = 3000
EXCESS_BARRIER = DISCARDED
BARRIER_CAP_ROUNDING = FLOOR
CONSUME_ORDER = consume_priority ASC → start_time ASC → protection_id ASC
```

### 5.1 적용량

Barrier 적용 시점의 현재 `max_hp_q`를 cap 기준으로 사용한다.

```text
per_application_cap_q = floor(max_hp_q * 20 / 100)
total_cap_q = floor(max_hp_q * 30 / 100)
remaining_total_capacity_q = max(0, total_cap_q - active_barrier_budget_q)
accepted_budget_q = min(requested_budget_q, per_application_cap_q, remaining_total_capacity_q)
discarded_budget_q = requested_budget_q - accepted_budget_q
```

- `accepted_budget_q <= 0`이면 새 instance를 만들지 않는다.
- 폐기량은 `BARRIER_EXCESS_DISCARDED` event로 기록한다.
- max HP가 이후 변해도 이미 승인된 Barrier budget을 소급 절단하지 않는다.
- 이후 새 적용은 변경된 현재 max HP cap을 사용한다.
- Barrier는 mitigation 뒤 피해를 소비하며 HP·Heal·Armor·Resistance가 아니다.
- 밀리초 지속시간의 실제 tick 변환은 다음 시간 Decision 전까지 구현 불가 상태다.

### 5.2 소비

여러 Barrier는 다음 canonical order로 피해를 흡수한다.

```text
consume_priority ASC
→ start_time ASC
→ protection_id ASC
```

같은 피해 Intent를 여러 Barrier가 소비해도 총 흡수량은 post-mitigation damage를 넘지 않는다.

### 5.3 조기 Stop-Ship Guard

대표 중립 Fixture에서 다음 중 하나가 성립하면 Barrier overcentralization 후보로 분류한다.

```text
FRONTLINE_MEAN_BARRIER_UPTIME > 40_PERCENT
OR
BARRIER_ABSORBED / POST_MITIGATION_INCOMING_DAMAGE > 35_PERCENT
```

- 이 기준은 조기 중단용 guard이며 최종 밸런스 합격선이 아니다.
- 표본 수·신뢰구간·family별 허용오차는 후속 A/B/C Acceptance Decision이 소유한다.
- 공세 대응·병종 선택을 Barrier 유지가 대체하면 수치 평균과 무관하게 사람 검증 stop-ship 후보다.

## 6. HP-Loss Redirection 기본값

```text
DEFAULT_REDIRECTION_RATIO = 30_PERCENT
MAX_REDIRECTION_RECIPIENTS = 1
ORIGINAL_TARGET_RETAINS_RATIO = 70_PERCENT
INVALID_RECIPIENT_POLICY = RETURN_TO_ORIGINAL_TARGET
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS = FORBIDDEN
```

각 `root_effect_id + original_target_id`의 Barrier 이후 `candidate_hp_loss_q`에 대해 한 번만 계산한다.

```text
redirected_q = round_half_up(candidate_hp_loss_q * 30 / 100)
original_remainder_q = candidate_hp_loss_q - redirected_q
```

정수식:

```text
redirected_q = (candidate_hp_loss_q * 30 + 50) div 100
```

- remainder를 뺄셈으로 구해 총량을 정확히 보존한다.
- recipient가 무효하면 `redirected_q`를 original target에 반환한다.
- 반환 또는 이전된 양은 Armor/Resistance와 Barrier를 다시 통과하지 않는다.
- 이전은 새 공격·true damage·재귀 trigger가 아니다.
- `root_effect_id`, `original_source_id`, `deployment_id`를 유지한다.

## 7. Health Floor 기본값

```text
DEFAULT_HEALTH_FLOOR_Q = 1_HP
HEALTH_FLOOR_TRIGGER_COUNT = 1_PER_PROTECTION_INSTANCE
HEALTH_FLOOR_EXCLUSIVE_GROUP = CORE_HEALTH_FLOOR
MULTIPLE_ACTIVE_CORE_FLOORS = FORBIDDEN
```

동일 tick 처리 순서에 따른 편향을 막기 위해 Health Floor는 개별 hit 순서가 아니라 R80D의 target별 최종 candidate HP-loss batch에 적용한다.

```text
all post-barrier and post-redirection loss for target
→ aggregate without mutating HP
→ apply one active Health Floor clamp
→ consume the Floor instance when it prevents any loss
→ emit final HP delta
```

- Floor는 HP를 증가시키지 않는다.
- Floor가 발동하지 않으면 instance를 소비하지 않는다.
- 한 instance가 발동하면 남은 지속시간과 관계없이 소비한다.
- 같은 exclusive group의 새 Floor는 기존 것보다 높은 floor만 교체할 수 있다. 현재 기본 floor가 1이므로 동급 중첩은 duration refresh만 허용한다.
- death·execute·revive system이 아니다.

## 8. Status 기본값

```text
DEFAULT_ADD_STACKS_CAP = 3
DEFAULT_DOT_HOT_PULSE_INTERVAL_MS = 1000
MAX_SINGLE_CONTROL_DURATION_MS = 2000
SAME_CONTROL_GROUP_LOCKOUT_MS = 1000
```

### 8.1 Stack

- `DEFAULT_ADD_STACKS_CAP=3`은 `ADD_STACKS_CAPPED` 정책의 기본값이다.
- `REPLACE_IF_STRONGER`, `REFRESH_DURATION`, `INDEPENDENT_BY_SOURCE`, `EXCLUSIVE_GROUP`는 별도 의미를 유지한다.
- Status Definition이 stacking policy를 누락하면 invalid다.
- Status Definition이 `ADD_STACKS_CAPPED`를 사용하면서 cap을 명시하지 않으면 3을 사용한다.

### 8.2 DOT/HOT Pulse

- 최초 pulse는 `start_time + 1000ms`다.
- 이후 1000ms 간격으로 새 DamageIntent 또는 RestoreIntent를 생성한다.
- `end_time_exclusive` 이상인 due time은 생성하지 않는다.
- DOT/HOT는 매 pulse마다 공통 channel·protection·event 계약을 소비한다.
- 실제 tick 정렬은 다음 시간 Decision에서 고정한다.

### 8.3 Control Duration·Lockout

- 단일 Control application의 승인 지속시간은 최대 2000ms다.
- Control 종료 시 같은 `stacking_group_id`에 1000ms lockout을 부여한다.
- lockout 중 같은 group의 새 Control은 `STATUS_REJECTED_CONTROL_LOCKOUT` event와 함께 거절한다.
- 다른 group은 별도 면역·exclusive 규칙이 허용할 때만 적용한다.
- lockout은 이미 commit된 행동을 소급 취소하지 않는다.

## 9. Event·Metric 계약

필수 단계 값:

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

불변식:

```text
POST_MITIGATION_DAMAGE_Q >= BARRIER_ABSORBED_Q
CANDIDATE_HP_LOSS_Q = POST_MITIGATION_DAMAGE_Q - BARRIER_ABSORBED_Q
REDIRECTED_PLUS_REMAINDER = CANDIDATE_HP_LOSS_Q
FINAL_HP_LOSS_Q <= CANDIDATE_HP_LOSS_Q
RAW_DAMAGE_Q and FINAL_HP_LOSS_Q are not double-counted
```

## 10. Fixture·검증 계약

### T0 Schema

- channel과 defense axis 일치.
- defense clamp 0~300.
- Barrier ratio·duration·consume order 필드.
- redirection recipient 최대 1.
- Health Floor exclusive group.
- Control `stacking_group_id`와 lockout.

### T1 Replay

- 동일 입력에서 모든 중간 정수 값과 event가 동일.
- float·platform-specific rounding 금지.
- 첫 divergent tick·phase·root effect 보고.

### T2 Invariant

- defense 0/25/50/100/200/300 경계.
- 양수 피해 최소 1.
- Barrier cap·과잉 폐기·canonical consume.
- 30% 이전 총량 보존과 무효 recipient 반환.
- Floor batch 적용과 1회 소비.
- stack cap 3·pulse 1000ms·Control 2000ms·lockout 1000ms.

### T3 Paired A/B/C

- 세 전선 전체를 포함한다.
- Barrier 흡수·uptime·final HP loss·Control uptime을 분리한다.
- placeholder parameter 결과는 `EXPLORATORY_ONLY`다.

현재 테스트·fixture·simulation은 작성하거나 실행하지 않는다.

## 11. 벤치마크·현업 비교

- 분모형 방어 계산은 방어가 증가할수록 추가 감소가 완만해져 선형 상한 직전의 절벽을 피하는 참고가 된다.
- Armor·Resistance를 같은 곡선으로 두면 두 공세 채널의 학습비용과 QA 조합을 제한할 수 있다.
- 임시 Barrier를 HP와 분리하고 cap·duration을 두는 제작 관행을 참고하되 외부 게임의 정확 수치를 복사하지 않는다.
- 공격 1회당 고정 차감은 연타와 단발 병종 사이의 구조적 편향이 커 현재 OMENWARD 공통식에서 기각한다.
- OMENWARD 권위는 세 전선·룰렛 provenance·비가역 배치·원인 복기다.

## 12. 적대적 검토

| Audit ID | 공격 | 판정·대응 |
|---|---|---|
| `OMW-AUD-247` | 음수 defense가 피해 증폭 우회가 됨 | 0 clamp·음수 금지 |
| `OMW-AUD-248` | defense 300 이상이 무한 생존으로 연결 | 300 clamp·최대 75% 감소 |
| `OMW-AUD-249` | float·언어별 rounding으로 replay 분기 | 양수 정수 half-up 식 고정 |
| `OMW-AUD-250` | 0 피해에도 최소 1을 만들어 면역이 깨짐 | 양수 유효 입력에만 최소 1 |
| `OMW-AUD-251` | Barrier application이 total cap을 우회 | 20% per-application·30% total 동시 적용 |
| `OMW-AUD-252` | max HP 변화가 기존 Barrier를 비결정적으로 절단 | 적용 시 cap 고정·소급 절단 금지 |
| `OMW-AUD-253` | Barrier 소비 순서가 collection order에 의존 | canonical consume key 고정 |
| `OMW-AUD-254` | Barrier가 세 전선 선택을 대체 | 40% uptime·35% absorption 조기 guard |
| `OMW-AUD-255` | 30% 이전 반올림으로 HP loss가 생성·소실 | redirected half-up·remainder subtraction |
| `OMW-AUD-256` | 무효 recipient에서 손실이 사라짐 | original target 반환 |
| `OMW-AUD-257` | Health Floor를 hit 순차 적용해 ID 편향 발생 | target별 same-tick batch clamp |
| `OMW-AUD-258` | Floor 다중 중첩으로 장기 불사 | exclusive group·active 1개 |
| `OMW-AUD-259` | Control 연쇄로 영구 행동불능 | 2000ms cap·1000ms same-group lockout |
| `OMW-AUD-260` | ms 기본값을 임의 tick으로 반올림해 runtime 분기 | fixed-tick Decision 전 구현 금지 |

## 13. 경계·다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
NUMERIC_DEFAULTS = USER_APPROVED_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
FIXED_TICK_RATE = PENDING
MS_TO_TICK_CONVERSION = PENDING
SOURCE_TARGET_MODIFIER_STACKING = PENDING
DEFENSE_PENETRATION = FORBIDDEN_UNTIL_SEPARATE_DECISION
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
A_B_C_SAMPLE_AND_TOLERANCE = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 4/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
