# OMENWARD Modifier Stacking·Effect Precedence

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_damage_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_time_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
grill_me_count: 6_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD 최초 공통 Modifier 계약은 **계층별 단일 집계 + R60 Source/R80 Target 하이브리드 Snapshot + 이름 있는 다섯 Stacking 정책**으로 확정한다.

```text
BASIS_POINTS = 10000 = 100_PERCENT
```

```text
R60 ACTION_COMMIT
→ source 공격 능력·outgoing modifier snapshot 고정

R80 IMPACT
→ target eligibility·immunity
→ target incoming modifier snapshot
→ Armor/Resistance
→ Barrier
→ redirection
→ Health Floor
→ HP delta / Restore
→ Status·post-hit
→ death pending
```

영웅·전설·표준 병종·건물은 같은 Modifier family·Intent·Resolver를 사용한다. 직접 HP 변경, 숨은 override, 별도 damage formula는 금지한다.

## 2. 제품 코어와의 연결

이 계약의 목적은 Buff를 많이 쌓는 게임을 만드는 것이 아니다. 플레이어가 세 전선 공세와 룰렛 결과를 보고 배치한 선택이 어떤 outgoing·incoming·방어 효과를 통해 결과를 만들었는지 설명 가능하게 하는 것이다.

```text
세 전선 공세 읽기
→ 건물·TokenSource로 릴 설계
→ SpinSnapshot 결과를 전선에 비가역 커밋
→ 공통 Modifier family와 precedence로 전투 해결
→ source snapshot·target response·final HP loss 복기
→ 다음 Stage 설계
```

Modifier가 전선·병종·배치 판단을 대체하거나 툴팁으로 설명할 수 없는 곱연산 사슬을 만들면 실패다.

## 3. 범위와 금지선

### 포함

- source outgoing damage basis-point family.
- target incoming damage basis-point family.
- Armor·Resistance additive point family.
- family cap과 combined pre-defense cap.
- R60 source snapshot과 R80 target snapshot.
- delayed projectile·DOT/HOT·environmental source snapshot 규칙.
- 동일 effect/source/target duplicate key.
- 다섯 Stacking 정책의 정확 의미.
- immunity·mitigation·Barrier·redirection·Floor·Status precedence.
- valid hit·HP damage·Barrier hit·Status trigger 의미.
- canonical event·explanation 필드.

### 제외

- 공격속도·이동속도·사거리·Cooldown modifier.
- Restore outgoing·incoming multiplier.
- Armor/Resistance penetration·ignore·negative defense.
- critical hit·lifesteal·overheal conversion.
- generic flat damage buff/debuff.
- `next hit`·`next damage` 소비형 Modifier.
- per-effect 자유 곱연산·override operation.
- true damage·execute·revive.
- 영웅·병종·건물별 실제 Modifier 값.
- GDScript·Resource·fixture·test 구현.
- Simulation·밸런스 결론.

```text
GENERIC_FLAT_DAMAGE_MODIFIER = FORBIDDEN_CURRENT_SLICE
CONSUMABLE_NEXT_HIT_MODIFIER = FORBIDDEN_CURRENT_SLICE
GENERIC_OVERRIDE_OPERATION = FORBIDDEN
PENETRATION_OR_IGNORE = FORBIDDEN_UNTIL_SEPARATE_DECISION
```

## 4. 공통 Modifier Schema

```text
ModifierRecord:
  modifier_instance_id
  effect_definition_id
  family_id
  source_id
  target_id
  root_effect_id
  deployment_id_if_applicable
  stacking_group_id
  stacking_policy
  duplicate_key
  magnitude_q
  strength_q
  stack_count
  max_stack_count
  priority
  start_tick
  end_tick_exclusive
  apply_sequence
  snapshot_policy
  active_flag
```

기본 duplicate key:

```text
effect_definition_id
+ source_id
+ target_id
```

허용된 현재 family:

```text
SOURCE_OUTGOING_DAMAGE_BP_DELTA
TARGET_INCOMING_DAMAGE_BP_DELTA
ARMOR_POINT_DELTA
RESISTANCE_POINT_DELTA
```

새 family는 기존 family에 의미가 흡수되지 않을 때만 별도 Decision으로 추가한다.

## 5. Outgoing·Incoming 단일 집계

### 5.1 Source Outgoing

```text
source_outgoing_bp
= clamp(
    10000 + sum(active SOURCE_OUTGOING_DAMAGE_BP_DELTA),
    5000,
    15000
  )
```

### 5.2 Target Incoming

```text
target_incoming_bp
= clamp(
    10000 + sum(active TARGET_INCOMING_DAMAGE_BP_DELTA),
    5000,
    15000
  )
```

양수 target incoming delta는 vulnerability, 음수는 damage-taken reduction이다. UI·event는 `Damage Dealt`와 `Damage Taken`을 서로 다른 축으로 표시한다.

### 5.3 Combined Pre-Defense

```text
combined_pre_defense_bp
= clamp(
    round_half_up(
      source_outgoing_bp * target_incoming_bp / 10000
    ),
    2500,
    20000
  )
```

float 없는 양의 정수식:

```text
combined_pre_defense_bp
= clamp(
    (source_outgoing_bp * target_incoming_bp + 5000) div 10000,
    2500,
    20000
  )
```

```text
if raw_damage_q <= 0:
    adjusted_damage_q = 0
else:
    adjusted_damage_q = max(
      1,
      (raw_damage_q * combined_pre_defense_bp + 5000) div 10000
    )
```

유효 양수 raw damage가 25% 배율에서 0으로 소실되지 않도록 방어 전에도 최소 1을 유지한다. 무효 target·immunity·0 이하 raw input에는 피해 1을 생성하지 않는다.

### 5.4 Cap 의미

```text
SOURCE_OUTGOING_RANGE = 50_PERCENT_TO_150_PERCENT
TARGET_INCOMING_RANGE = 50_PERCENT_TO_150_PERCENT
COMBINED_PRE_DEFENSE_RANGE = 25_PERCENT_TO_200_PERCENT
```

family cap은 각 family 합산 뒤 한 번만 적용한다. 여러 Source가 family cap을 우회할 수 없다.

## 6. Armor·Resistance Modifier

```text
raw_effective_defense
= base_defense_q
+ sum(active positive point deltas)
+ sum(active negative point deltas)

effective_defense
= clamp(raw_effective_defense, 0, 300)
```

- Armor·Resistance Modifier는 integer point additive만 허용한다.
- 퍼센트 방어 증가·감소, penetration, ignore는 금지한다.
- negative delta가 있어도 최종 defense는 0 미만이 될 수 없다.
- KINETIC은 Armor family만, ARCANE은 Resistance family만 소비한다.

## 7. Snapshot 계약

### 7.1 R60 Source Snapshot

ActionIntent가 R60에서 commit될 때 다음을 immutable snapshot으로 저장한다.

```text
source_snapshot_id
source_id
source_outgoing_bp
source_attack_stat_q_if_used
source_grade_tier_if_formula_uses_it
commit_tick
source_modifier_instance_ids
```

- Source Buff가 발사 뒤 종료돼도 이미 commit된 Action의 snapshot은 바뀌지 않는다.
- Source가 R90에서 사망해도 합법적으로 commit된 Action은 interrupt policy가 취소하지 않는 한 snapshot을 유지한다.
- SceneTree·animation callback에서 snapshot을 재계산하지 않는다.

### 7.2 R80 Target Snapshot

R80A validity·immunity 확인 뒤, R80B의 합법적 same-tick Protection setup이 끝난 snapshot에서 다음을 평가한다.

```text
target_incoming_bp
armor_q / resistance_q
active Barrier instances
redirection instance
Health Floor instance
active immunity and Status filters
```

대상이 발사 뒤 Barrier를 얻었다면 명중 시 Barrier가 적용된다. 대상의 실제 대응을 발사 시점에 고정하지 않는다.

### 7.3 Delayed·Periodic·Environment

```text
DIRECT_OR_PROJECTILE_ACTION:
  source snapshot = R60 commit
  target snapshot = each R80 impact

DOT_OR_HOT_STATUS:
  source snapshot = Status application commit
  target snapshot = each pulse impact

ENVIRONMENTAL_WITH_OWNER:
  source snapshot = explicit owner commit

ENVIRONMENTAL_WITHOUT_OWNER:
  source_outgoing_bp = 10000
```

DOT/HOT pulse는 매번 Source modifier를 재평가하지 않는다. Status 적용 원인의 공격자 상태를 보존한다.

## 8. Stacking 정책

모든 Effect Definition은 정확히 하나의 정책을 선언한다.

```text
REFRESH_DURATION
REPLACE_IF_STRONGER
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

정책 누락·복수 선언은 T0 invalid다.

### 8.1 REFRESH_DURATION

- 동일 duplicate key는 하나의 logical instance만 유지한다.
- magnitude와 stack count는 바꾸지 않는다.
- `end_tick_exclusive = max(existing_end, current_tick + new_duration_ticks)`.
- 기존 지속시간을 짧게 만들 수 없다.
- 기본 duplicate policy다.

### 8.2 REPLACE_IF_STRONGER

```text
higher strength_q wins
→ equal strength: higher priority wins
→ equal priority: later end_tick_exclusive wins
→ complete tie: earlier apply_sequence wins
```

새 Effect가 약하면 거절 event를 남긴다. 동급 Effect는 더 긴 종료 Tick으로 갱신할 수 있다.

### 8.3 ADD_STACKS_CAPPED

- 하나의 logical instance와 integer `stack_count`를 유지한다.
- 새 적용마다 `stack_count += 1`, `max_stack_count`에서 clamp한다.
- cap을 명시하지 않으면 승인 기본값 3을 사용한다.
- family magnitude는 `per_stack_magnitude_q * stack_count`다.
- 종료 Tick은 REFRESH_DURATION 규칙으로 갱신한다.
- cap 초과분은 discard event로 기록한다.

### 8.4 INDEPENDENT_BY_SOURCE

- `effect_definition_id + source_id + target_id`당 하나의 instance를 허용한다.
- 같은 Source 중복은 REFRESH_DURATION으로 처리한다.
- 다른 Source instance는 독립적으로 family 합산에 참여한다.
- family cap은 모든 Source 합산 뒤 적용하므로 Source 수로 cap을 우회하지 못한다.

### 8.5 EXCLUSIVE_GROUP

같은 `stacking_group_id`에서 하나만 활성화한다.

```text
higher priority wins
→ equal priority: higher strength_q wins
→ equal strength: earlier apply_sequence wins
→ complete tie: lower modifier_instance_id wins
```

비승자 Effect는 `MODIFIER_REJECTED_EXCLUSIVE_GROUP` event를 남기며 숨은 대기열에 들어가지 않는다.

## 9. Effect Precedence

```text
P00 TARGET_VALIDITY_AND_ELIGIBILITY
P10 IMMUNITY_FILTER
P20 SOURCE_OUTGOING_SNAPSHOT_LOAD
P30 TARGET_INCOMING_SNAPSHOT_AND_AGGREGATE
P40 ARMOR_RESISTANCE_AGGREGATE_AND_MITIGATION
P50 BARRIER_ABSORPTION
P60 HP_LOSS_REDIRECTION
P70 HEALTH_FLOOR
P80 HP_DELTA_OR_SEPARATE_RESTORE
P90 STATUS_APPLICATION_AND_POST_HIT_QUEUE
P100 DEATH_OR_DESTRUCTION_PENDING
```

기존 R80 연결:

```text
R80A = P00~P10
R80B = committed Protection setup
R80C = P20~P50
R80D = P60~P70
R80E = P80
R80F = P90
R80G = P100
```

- immunity가 성립하면 DamageIntent는 P20 이후를 실행하지 않는다.
- immunity는 `IMMUNE` reason event를 남긴다.
- Barrier는 mitigation 뒤 적용한다.
- transferred HP loss는 두 번째 Modifier·mitigation·Barrier pass를 거치지 않는다.
- Health Floor는 target별 same-tick candidate loss batch에 적용한다.
- Status 적용은 HP delta 뒤 R80F에서 처리한다.
- death pending은 모든 R80 effect batch 뒤 표시하고 R90에서 확정한다.

## 10. Trigger 의미

Trigger Definition은 다음 중 명시적 조건을 사용한다.

```text
ON_VALID_IMPACT
ON_POST_MITIGATION_DAMAGE
ON_BARRIER_ABSORBED
ON_FINAL_HP_LOSS
ON_STATUS_APPLIED
ON_TARGET_DEATH_FINALIZED
```

- `ON_VALID_IMPACT`: P00/P10 통과.
- `ON_POST_MITIGATION_DAMAGE`: P40 결과가 1 이상.
- `ON_BARRIER_ABSORBED`: P50 흡수량이 1 이상.
- `ON_FINAL_HP_LOSS`: P80 최종 HP 손실이 1 이상.
- `ON_STATUS_APPLIED`: R80F에서 실제 적용 성공.
- `ON_TARGET_DEATH_FINALIZED`: R90 최종 사망·파괴 확정.

`on hit`라는 모호한 문자열만으로 Trigger를 정의하지 않는다. 면역된 공격, Barrier만 손상한 공격, HP를 잃은 공격을 구분한다.

## 11. Restore·Transferred Damage 경계

- RestoreIntent는 damage outgoing/incoming family를 소비하지 않는다.
- Restore multiplier family는 후속 Decision 전까지 100% 고정이다.
- Restore는 음수 DamageIntent가 아니다.
- transferred amount는 원래 root effect와 source/deployment provenance를 유지한다.
- transferred amount는 `TRANSFER_DEPTH_MAX=1`이며 새로운 공격·on-hit·mitigation pass가 아니다.

## 12. 동일 Tick Batch·Canonical Order

R80C의 target incoming·defense snapshot은 해당 target에 대한 Damage batch 전에 한 번 생성한다.

```text
TARGET_MODIFIER_CONSUMPTION_DURING_R80C = FORBIDDEN_CURRENT_SLICE
CONSUMABLE_NEXT_HIT_EFFECT = FORBIDDEN_CURRENT_SLICE
```

따라서 낮은 stable ID의 hit가 vulnerability를 먼저 소비해 뒤 hit 결과를 바꾸는 순차 편향을 만들지 않는다.

Event 표현 순서:

```text
tick
→ phase_order
→ target_canonical_key
→ root_effect_id
→ effect_local_sequence
→ modifier_instance_id
```

합산은 signed 64-bit intermediate를 사용하고 family cap 적용 전 overflow를 검사한다.

## 13. Event·Explanation 계약

필수 필드:

```text
raw_damage_q
source_outgoing_bp
source_modifier_instance_ids
target_incoming_bp
target_modifier_instance_ids
combined_pre_defense_bp
adjusted_damage_q
effective_defense_q
post_mitigation_damage_q
barrier_absorbed_q
redirected_hp_loss_q
health_floor_prevented_q
final_hp_loss_q
stacking_policy
stack_count_before_after
modifier_apply_or_reject_reason
root_effect_id
deployment_id_if_applicable
```

플레이어용 축약은 최소 다음을 구분한다.

```text
Damage Dealt modifier
Damage Taken modifier
Armor or Resistance
Barrier
Final HP Loss
```

색상만으로 buff·debuff·immunity·Barrier를 구분하지 않는다.

## 14. Benchmark·Production 비교

Unreal Gameplay Ability System의 Attribute base/current 분리, Gameplay Effect·Modifier 중심 데이터 구조, stack·duration 정책과 cosmetic/gameplay 권위 분리는 제작 참고로 사용한다.

```text
ADOPT = data-driven modifier and reusable calculation boundaries
ADAPT = four current OMENWARD families and five explicit stacking policies
REJECT = arbitrary per-effect operation and unrestricted stacking combinations
```

근거:

- `https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-the-unreal-engine-gameplay-ability-system`

OMENWARD 정본은 외부 프레임워크가 아니라 세 전선·SpinSnapshot·TokenSource·비가역 전선 배치·ordered event provenance다.

## 15. 적대적 검토

| Audit ID | 공격 | 결론·완화 |
|---|---|---|
| OMW-AUD-276 | additive·multiplicative 적용 순서가 결과를 바꿈 | family 단일 합산 후 계층별 한 번 적용 |
| OMW-AUD-277 | raw 1이 25% 배율에서 0으로 소실 | 유효 양수 adjusted damage 최소 1 |
| OMW-AUD-278 | 발사 뒤 Source Buff 종료가 투사체 피해 변경 | R60 source snapshot 고정 |
| OMW-AUD-279 | 발사 뒤 Target Barrier 획득이 무시됨 | R80 target snapshot 사용 |
| OMW-AUD-280 | 같은 Source 중복이 배율을 기하급수 증가 | duplicate key + REFRESH_DURATION 기본 |
| OMW-AUD-281 | 여러 Source가 family cap 우회 | 모든 Source 합산 뒤 family cap 적용 |
| OMW-AUD-282 | generic override가 공통 Resolver 우회 | override operation 금지 |
| OMW-AUD-283 | Effect 순회 순서가 event·합산 결과 변경 | canonical event key + integer aggregate |
| OMW-AUD-284 | outgoing·incoming polarity가 UI에서 혼동 | Damage Dealt/Taken 분리 표기 |
| OMW-AUD-285 | 면역 공격이 피해 Trigger를 발동 | explicit trigger condition 분리 |
| OMW-AUD-286 | Barrier hit와 HP hit가 같은 on-hit로 처리 | absorbed/final HP loss trigger 분리 |
| OMW-AUD-287 | transferred damage가 Modifier·방어를 재통과 | second modifier/mitigation pass 금지 |
| OMW-AUD-288 | next-hit 소비가 stable ID 순서 편향 생성 | 소비형 Modifier 현 Slice 금지 |
| OMW-AUD-289 | 영웅 효과가 직접 HP를 수정 | 공통 Intent·family·precedence 필수 |

## 16. Fixture·검증 계약

### T0 Schema

- 허용 family 외 ID 거절.
- stacking policy 정확히 하나.
- duplicate key 필수.
- basis-point·point delta integer.
- cap·priority·strength·duration 유효성.
- generic override·flat damage·next-hit 소비 거절.

### T1 Replay

- 동일 input에서 source snapshot ID·target aggregate·event가 동일.
- Source Buff 종료 전후 delayed impact replay parity.
- render FPS·pause/save/load가 Modifier 결과를 바꾸지 않음.
- signed 64-bit overflow fixture는 명시적 invalid.

### T2 Invariant

- source outgoing 50~150%.
- target incoming 50~150%.
- combined pre-defense 25~200%.
- raw positive damage가 modifier rounding으로 0이 되지 않음.
- 같은 Source duplicate refresh.
- independent Source 합산 뒤 cap.
- immunity·Barrier·HP-loss trigger 분리.
- transferred amount에 second pass 없음.
- 영웅·전설 direct HP mutation 없음.

### T3 Paired A/B/C

- 세 전선 전체와 deployment provenance를 포함한다.
- outgoing only / incoming only / combined 조건을 비교한다.
- source snapshot 고정과 target response가 인과 로그에서 설명 가능해야 한다.
- placeholder 콘텐츠 값 결과는 `EXPLORATORY_ONLY`다.

## 17. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MODIFIER_STACKING_EFFECT_PRECEDENCE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
MODIFIER_RESOLVER_CODE = NOT_AUTHORIZED
FIXTURES_TESTS = NOT_AUTHORIZED
EXACT_CONTENT_VALUES = PENDING
SPATIAL_QUANTIZATION_MOVEMENT_TARGETING = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 18. 다음 Decision

```text
OMW-DEC-20260803-VALIDATION-SPATIAL-QUANTIZATION-MOVEMENT-AND-TARGETING-DEFAULTS-V1
```

이 Decision은 quantized 2D scale, 이동 단위, 사거리, same-lane/cross-lane target scope, collision·anchor·target tie-break의 exact 기본값을 소유한다.

```text
GRILL_ME_COUNT = 6/10
NEXT_PREFLIGHT = AT_10_OF_10
```
