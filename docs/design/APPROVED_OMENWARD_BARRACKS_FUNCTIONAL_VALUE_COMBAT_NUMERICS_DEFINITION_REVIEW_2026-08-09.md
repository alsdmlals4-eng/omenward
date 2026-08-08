# [승인] OMENWARD 병영 Functional-Value Combat Numerics 정의 검토

```yaml
updated_at: 2026-08-09
decision_id: OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-COMBAT-NUMERICS-DEFINITION-REVIEW-V1
parent_decision_id: OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1
status: REVIEW_COMPLETE / BASE_NUMERICS_PRESENT / ROLE_OUTPUT_RUNTIME_PARTIAL / FUNCTIONAL_VALUE_NOT_SELECTED
approval: CONTINUOUS_WORK_AUTO_APPROVED_TECHNICAL_REVIEW_FINDINGS_ONLY
scope: REVIEW_ONLY / NO_PRODUCT_MUTATION
product_code_authority: NONE
```

## 1. 결론

기존 blocker `BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED`는 너무 넓었다. 현재 제품에는 실제 base combat numeric resource가 존재하고, 승인 PoC 문서에도 역할별 수치 가설이 존재한다. 부족한 것은 **제품에서 실제로 발생하고 측정 가능한 role-complete output**이다.

```text
PRODUCT_BASE_COMBAT_NUMERICS = PRESENT
POC_ROLE_NUMERIC_HYPOTHESES = PRESENT_NONFINAL
ROLE_COMPLETE_PRODUCT_OUTPUT_NUMERICS = PARTIAL_INSUFFICIENT
FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE
FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
ENTRY_GATE = BLOCK
```

따라서 기존 broad blocker는 다음 두 구체 blocker로 교체한다.

```text
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED
BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED
```

이 review는 제품 코드를 변경하거나 PoC 가설 수치를 최종 제품 수치로 승격하지 않는다.

## 2. 제품 taxonomy와 역사 simulation taxonomy 분리

현행 제품 Unit Tree V5의 taxonomy:

```text
PRODUCT_BASIC_BARRACKS = SHIELD / GREATSWORD / ASSASSIN / SPEAR / ARCHER / CAVALRY
PRODUCT_SPECIAL_CORPS = PRIEST_MAGE_FLIER_GIANT
```

역사 smoke model의 고정 outcome label set:

```text
HISTORICAL_SIMULATION_SPECIAL_OUTCOME_LABEL_SET = ASSASSIN_PRIEST_MAGE_FLYING_GIANT
```

두 집합은 같은 의미가 아니다. 특히 `assassin`은 현재 제품 taxonomy에서 **기본 병영 전문화**이며 특수병단 소속이 아니다.

```text
TAXONOMY_RECONCILIATION = HISTORICAL_MODEL_LABEL_SET_PRESERVED_AS_POINT_IN_TIME_ANALYSIS_LABELS
ASSASSIN_SPECIAL_CORPS_MEMBERSHIP = FALSE
HISTORICAL_SMOKE_FILES = NO_RETROACTIVE_REWRITE
```

9/10 robustness 결과를 포함한 역사 simulation evidence는 해당 시점 분석 label의 provenance로 유지한다. 이를 제품 special-corps membership 정본으로 사용하지 않는다.

## 3. 현재 제품 base combat numeric evidence

`data/units/*.tres`에 실제 base stats가 존재한다.

### Priest

```text
max_health = 105
attack = 10
armor = 7
magic_resistance = 18
move_speed = 1.0
attack_range = 3.0
capture_power = 0.5
role = support
target_priority = lowest_health_ally
```

### Mage

```text
max_health = 100
attack = 22
armor = 5
magic_resistance = 20
move_speed = 1.0
attack_range = 3.0
capture_power = 0.5
role = ranged
target_priority = cluster / nearest
```

### Flier

```text
max_health = 120
attack = 17
armor = 10
magic_resistance = 12
move_speed = 1.3
attack_range = 1.5
capture_power = 0.0
role = air
target_priority = backline
```

### Giant

```text
max_health = 320
attack = 34
armor = 30
magic_resistance = 20
move_speed = 0.7
attack_range = 1.5
capture_power = 0.5
role = siege
structure_damage_tag = siege
target_priority = structure / nearest
```

즉 `PRODUCT_BASE_COMBAT_NUMERICS = PRESENT`다.

## 4. 승인 PoC 역할 수치 가설도 존재

`APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`는 역할 구조를 승인하되 **수치·이름은 첫 PoC 가설**이라고 명시한다. 따라서 아래는 final product authority가 아니라 검증 가능한 hypothesis/reference다.

### Priest PoC hypothesis

```text
HP = 220
basic_attack = 18 magic
interval = 1.60s
range = 200
heal = max_hp 10% + 40
heal_cooldown = 8s
fallback_encouragement = attack_speed +8% for 5s
```

### Mage PoC hypothesis

```text
HP = 200
attack = 34 magic
interval = 1.70s
range = 220
explosive_orb_center = 60 magic
explosive_orb_outer = 45 magic
max_targets = 5
cooldown = 7s
```

### Flier PoC hypothesis

```text
HP = 250
attack = 38
interval = 1.25s
move = 88
range = 44
frontline_bypass = TRUE
dive_distance = 100
dive_damage = 70
dive_cooldown = 8s
```

### Giant PoC hypothesis

```text
HP = 900
physical_defense = 80
magic_resistance = 20
attack = 120
interval = 2.80s
windup = 1.10s
range = 58
slam_target_cap = 6
outer_damage_ratio = 0.75
structure_multiplier = 1.35
barricade_multiplier = 1.50
```

별도 Giant V3도 절대 전투 수치를 PoC 조정 대상으로 둔다. 따라서 이 수치들을 최종 functional-value scalar로 직접 사용하지 않는다.

## 5. 현재 runtime의 role-output gap

승인 shared-archetype contract는 개념적으로 다음 surface를 요구한다.

```text
movement_layer
passive_ids
skill_ids
targeting_profile_id
threat_cost
```

현재 `UnitArchetypeProfile` Resource schema에는 위 필드들이 없다. 현재 runtime에서 확인되는 gap은 다음과 같다.

### Targeting

`LaneState.find_target()`는 살아 있는 적을 모은 뒤 **거리 기준 nearest**로 정렬한다.

```text
TARGET_PRIORITY_TAGS_IN_DATA = PRESENT
TARGET_PRIORITY_TAGS_CONSUMED_BY_NORMAL_LANE_TARGETING = NO
```

따라서 Priest의 `lowest_health_ally`, Mage의 `cluster`, Flier의 `backline` 같은 data tag가 일반 target selection output으로 이어지지 않는다.

### Damage types / resistance

`UnitInstance.receive_damage()`는 현재 `armor`만 사용해 mitigation한다.

```text
MAGIC_RESISTANCE_IN_DATA = PRESENT
MAGIC_RESISTANCE_USED_BY_RECEIVE_DAMAGE = NO
MAGIC_DAMAGE_OUTPUT_DISTINCTION = NOT_ROLE_COMPLETE
```

### Attack timing

`AttackProfile` default:

```text
preparation_ms = 100
hit_ms = 100
recovery_ms = 100
```

bootstrap attack profiles는 profile ID만 지정하며 개별 timing override가 없다. 따라서 Giant PoC의 1.10s windup/2.80s interval 같은 역할 timing은 현재 product runtime output으로 식별되지 않는다.

### Role mechanics

현재 core battle loop에서 확인되는 것:

```text
ASSASSIN_BYPASS = PARTIALLY_IMPLEMENTED
GIANT_SIEGE_TAG_OBJECTIVE_DAMAGE = IMPLEMENTED
CAPTURE_POWER = IMPLEMENTED
```

현재 core loop에서 role-complete output이 확인되지 않는 것:

```text
PRIEST_HEAL_EFFECTIVE_HP = NOT_IMPLEMENTED_AS_PRODUCT_OUTPUT
PRIEST_BUFF_UPTIME = NOT_IMPLEMENTED_AS_PRODUCT_OUTPUT
MAGE_AOE_DAMAGE_AND_TARGET_COUNT = NOT_IMPLEMENTED_AS_PRODUCT_OUTPUT
MAGE_CONTROL_TARGET_SECONDS = NOT_IMPLEMENTED_AS_PRODUCT_OUTPUT
FLIER_MOVEMENT_LAYER_BYPASS = NOT_IMPLEMENTED_AS_PRODUCT_OUTPUT
FLIER_AIR_TARGETABILITY = NOT_IMPLEMENTED_AS_PRODUCT_OUTPUT
GIANT_SLAM_MULTI_TARGET_OUTPUT = NOT_IMPLEMENTED_AS_PRODUCT_OUTPUT
GIANT_POC_1_35_STRUCTURE_MULTIPLIER = NOT_IMPLEMENTED_AS_ROLE_SPECIFIC_PRODUCT_OUTPUT
```

현재 C2/battle tests는 public base stats parity, deterministic battle snapshot, capture power, generic siege/objective damage를 검증하지만 위 role-complete output을 검증하지 않는다.

## 6. Functional-value 비교 surface

단일 `functional_value_index`를 다시 가정하지 않는다. 역할별 실제 output을 벡터로 측정한다.

```text
FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE
POST_HOC_WEIGHT_TUNING = FORBIDDEN
```

공통 direct-combat surface:

```text
DAMAGE_DEALT
DAMAGE_RECEIVED_OR_ABSORBED
SURVIVAL_TIME
TIME_TO_FIRST_CONTACT
ATTACK_CYCLE_OUTPUT
MOVE_AND_RANGE_OUTPUT
CAPTURE_CONTRIBUTION
STRUCTURE_DAMAGE
```

Priest 추가 surface:

```text
EFFECTIVE_HEALING_HP
OVERHEAL_WASTE
SUPPORTED_TARGET_SECONDS
BUFF_UPTIME
BUFF_AFFECTED_TARGET_SECONDS
ALLY_DEATHS_PREVENTED_DIAGNOSTIC
```

Mage 추가 surface:

```text
PRIMARY_TARGET_DAMAGE
COLLATERAL_AOE_DAMAGE
TARGETS_HIT_PER_CAST
CONTROL_TARGET_SECONDS
DEBUFF_TARGET_SECONDS
```

Flier 추가 surface:

```text
TIME_TO_BACKLINE_CONTACT
FRONTLINE_BYPASS_DISTANCE_OR_TIME
DIVE_DAMAGE
BACKLINE_PRESSURE_SECONDS
AIR_TARGETABILITY_EXPOSURE
GROUND_OBSTACLE_BYPASS
```

Giant 추가 surface:

```text
SLAM_TARGETS_HIT
SLAM_TOTAL_DAMAGE
FRONTLINE_SURVIVAL_TIME
STRUCTURE_DAMAGE
BARRICADE_DAMAGE
STAGGER_OR_KNOCKBACK_TARGET_SECONDS
```

역할이 다른 수치를 하나의 가중 utility로 합산하지 않는다. 비교는 hard role requirements + role-specific vector/Pareto 방식으로 유지한다.

## 7. 기존 정본이 제공하는 상대 비교 방향

PoC lineage contract의 검증 경계는 functional-value scenario의 방향 constraint로 재사용할 수 있다.

```text
ARCHER_SUSTAINED_SINGLE_TARGET_DPS > MAGE_SUSTAINED_SINGLE_TARGET_DPS
ASSASSIN_SINGLE_TARGET_BURST > FLIER_SINGLE_TARGET_BURST
FLIER_BACKLINE_PRESSURE_DURATION > ASSASSIN_BACKLINE_PRESSURE_DURATION
GREATSWORD_SPEED_AND_COST_ADVANTAGE > GIANT
GIANT_SURVIVAL_AOE_SIEGE_ADVANTAGE > GREATSWORD
PRIEST_VALUE_REQUIRES_SELF_COMBAT_PLUS_HEAL_PLUS_SUPPORTED_TARGETS_PLUS_BUFF_UPTIME
```

이 방향 constraint는 다음 measurement-scenario Gate에서 pre-registered acceptance/diagnostic relationship으로 사용할 수 있다. 현재 review에서 새 숫자를 만들지 않는다.

## 8. Blocker 정제

기존:

```text
BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED
```

은 다음으로 supersede한다.

```text
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED
BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED
```

해석:

- base stats 부재가 blocker가 아니다.
- PoC 역할 수치 가설 부재가 blocker가 아니다.
- product runtime이 role-specific output을 실제로 생성·측정하지 못하는 것이 blocker다.
- 어떤 동일 입력 scenario에서 role output을 비교할지 사전등록되지 않은 것이 blocker다.

## 9. 다음 Gate

제품 mutation 없이 지금 계속 가능한 planning task는 measurement scenario 정의다.

```text
NEXT_GATE = BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_DEFINITION
```

이 Gate는 다음을 정의한다.

- 공통 baseline opponent/ally compositions
- same-lane/backline/cluster/structure/air scenario
- seed 또는 deterministic fixture policy
- role-specific measured outputs
- hard role relationships
- no-single-weighted-score comparison rules
- runtime에 아직 없는 output은 `BLOCKED_RUNTIME_OUTPUT`로 명시

그 뒤 persistent Godot authoring이 필요한 role-output runtime implementation은 HiGodot 권위 경로로 별도 준비/실행한다.

## 10. 계속 금지

```text
FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
PARAMETER_SELECTION_10000 = NOT_AUTHORIZED
CONFIRMATION_SWEEP_50000 = BLOCKED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
GODOT_AUTHORING_MUTATION = NOT_AUTHORIZED
```

9/10 robustness PASS는 유지하되 combat/role functional value를 승인했다는 뜻으로 확장하지 않는다.
