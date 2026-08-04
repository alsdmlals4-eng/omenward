# OMENWARD 공통 전투 Schema·Resolution Order

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
child_damage_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
child_time_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
grill_me_count: 2_OF_10
current_branch_counter: 5_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD의 최초 전투 계약은 **코어 우선 공통 Schema**다.

```text
세 전선 공세·전장 상태
→ SpinSnapshot·TokenSource가 추적되는 배치 명령
→ 표준 유닛·적·건물·목표 공통 상태
→ 30 TPS fixed-tick phase resolver
→ ordered event·metrics·fingerprint
→ 결과 원인 복기
```

영웅·전설·고유 2스킬은 공통 계약을 소비하는 확장 계층이다. 별도 AI loop·clock·damage formula·death resolver·save identity를 만들지 않는다.

전투 Harness는 룰렛·경제를 재실행하지 않고 모든 배치 개체의 `DeploymentProvenance`를 필수로 소비한다.

## 2. 플레이어 코어 연결

```text
건물·TokenSource가 미래 릴 변경
→ SpinSnapshot에서 병력 생성
→ 플레이어가 한 전선에 비가역 커밋
→ 공통 전투 규칙으로 세 전선 변화
→ event provenance로 원인 설명
→ 다음 Stage 설계
```

세 전선 전체, 다른 두 전선 기여도, 건물·목표·점령, 배치 출처는 선택 필드가 아니라 필수 경계다.

## 3. 범위

### 포함

- `CombatRunState`, `LaneState`, `CombatantState`, `BuildingState`, `ObjectiveState`.
- `DeploymentProvenance`, `OrderedCommand`, `ActionIntent`, `EffectIntent`.
- `ProtectionInstance`, `StatusInstance`, `PendingCommit`, `ActiveEffect`, `RngStreamState`.
- quantized 2D 위치와 lane·anchor 관계.
- 이동·targeting·공격·효과·죽음·파괴·점령 순서.
- phase barrier·event envelope·fingerprint 시점.
- 30 TPS integer Tick과 spawn/activation seam.
- 영웅·전설 공통 extension seam.

### 제외

- 룰렛 회전·릴 편집·경제 분포 실행.
- 피해·방어·이동속도·사거리·cooldown의 콘텐츠별 실제 값.
- modifier stacking·effect precedence의 exact 규칙.
- 영웅·전설 exact kit와 허용오차.
- Godot SceneTree·NavigationServer·PhysicsServer·Timer·animation callback을 전투 권위로 사용.
- GDScript·Scene·Resource·fixture·test 구현.
- Simulation·Runtime·Human QA와 밸런스 결론.

하위 권위:

```text
Damage/Protection/Status
= design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md

Mitigation/Protection Numeric Defaults
= design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md

Fixed Tick/Time/Activation
= design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md
```

## 4. 공통 상태 Schema

### CombatRunState

```text
schema_version
engine_contract_version
parameter_set_id
battle_id / map_id / stage_id / wave_id
tick_index / phase_id
lane_states[TOP,MID,BOTTOM]
combatants_by_id + canonical_combatant_order
buildings_by_id + canonical_building_order
objectives_by_id + canonical_objective_order
scheduled_commands
pending_commits / active_effects
protection_instances / status_instances
named_rng_streams
event_sequence_state
termination_state
```

Dictionary lookup은 허용하되 순회를 resolution order로 사용하지 않는다.

### LaneState

```text
lane_id / lane_order
segment_states
frontline_anchor_id
combatant_ids / building_ids / objective_ids
pending_deployment_ids
lane_pressure_metrics
lane_contribution_metrics
```

```text
TOP=0 / MID=1 / BOTTOM=2
```

lane order는 serialization·event 정렬용이며 전투 우선권이 아니다.

### CombatantState

```text
entity_id / spawn_sequence
side / unit_archetype_id / grade / tier
lane_id / position_q{x_q,y_q,anchor_id} / facing
movement_layer / collision_class
hp_q / max_hp_q / armor_q / resistance_q
attack_state / ability_state_refs / target_id
role_tags
protection_instance_ids / status_instance_ids
deployment_provenance
spawn_tick / activation_tick
alive / death_pending
```

단일 1D 위치만으로 실제 거리·cross-lane 범위를 판단하지 않는다.

### DeploymentProvenance

```text
deployment_id
spin_snapshot_id
pending_reward_id
token_instance_id
token_source_id
reward_resolution_sequence
lane_commit_id / commit_sequence
source_building_or_system_id
```

모든 전투 결과 Event는 최소 `deployment_id`까지 역추적 가능해야 한다.

### BuildingState

```text
building_id / node_id / building_type / tier
owner_side / lane_id / position_q
hp_q / max_hp_q / armor_q / resistance_q
operational_state / targetable_flags
passive_effect_refs / active_action_state
protection_instance_ids / status_instance_ids
alive / destruction_pending
```

### ObjectiveState

```text
objective_id / objective_type
lane_id / segment_id / position_q
owner_side / capture_progress_q / capture_state
eligible_contestant_ids
blocked_or_locked_state
ownership_change_sequence
hp_targetable_flag
```

기본 Objective는 HP target이 아니며 점령은 구형 합산 `capture_power`를 부활시키지 않는다.

## 5. 행동·효과 Schema

```text
OrderedCommand:
  command_id / scheduled_tick / command_order / actor_id / payload

ActionIntent:
  intent_id / source_id / action_type / commit_tick
  target_snapshot / position_snapshot / interrupt_policy

EffectIntent:
  effect_id / root_effect_id / source_id / target_ids
  effect_category / raw_payload / application_priority

ProtectionInstance:
  protection_id / protection_type / source_id / owner_id
  start_tick / end_tick_exclusive / remaining_budget_q
  filter / consume_priority

StatusInstance:
  status_instance_id / status_type / source_id
  start_tick / end_tick_exclusive
  stacking_group_id / stacking_policy / stack_state / payload

PendingCommit:
  commit_id / source_id / immutable_target_snapshot
  immutable_position_snapshot / resolve_tick / resolved_flag

ActiveEffect:
  effect_instance_id / owner_id / start_tick
  end_tick_exclusive / remaining_budget_q / cleanup_policy
```

Commit 뒤 target 상실 시 hidden fallback을 만들지 않는다. `CANCEL`, `RESOLVE_AT_COMMITTED_POINT`, `RESOLVE_ON_SNAPSHOT` 중 명시 정책만 허용한다.

## 6. Canonical Sort Key

```text
lane_order
→ entity_kind_order
→ spawn_sequence
→ stable_entity_id
→ local_sequence
```

Event key:

```text
tick
→ phase_order
→ resolver_order
→ source_canonical_key
→ local_sequence
```

Sort key는 표현 순서를 고정하며 phase snapshot·barrier가 결과 의미를 소유한다.

## 7. Fixed-Tick Resolution Order

```text
DOMAIN_TPS = 30
R00 TICK_OPEN_AND_EXPIRE
R10 ORDERED_COMMAND_INGEST
R20 SPAWN_AND_ACTIVATION
R30 MOVEMENT_INTENT_BUILD
R40 MOVEMENT_RESOLVE
R50 TARGET_SENSE_AND_SELECT
R60 ACTION_AND_SKILL_COMMIT
R70 IMPACT_AND_EFFECT_INTENT_BUILD
R80 DAMAGE_PROTECTION_STATUS_APPLY
R90 DEATH_AND_DESTRUCTION_FINALIZE
R100 OBJECTIVE_AND_OWNERSHIP_RESOLVE
R110 TIMER_COOLDOWN_STATUS_ADVANCE
R120 METRICS_EVENT_FINGERPRINT
R130 TICK_CLOSE
```

### R00

- `end_tick_exclusive <= current_tick` instance를 R10 이전 제거한다.
- 현재 Tick snapshot을 연다.
- wall clock·frame delta는 사용하지 않는다.

### R10

- `(scheduled_tick, command_order, command_id)`로 명령을 적용한다.
- `scheduled_tick == current_tick`만 ingest한다.
- 과거 명령은 reject event, 미래 명령은 queue 유지다.

### R20

```text
spawn_tick = T
activation_tick = T + 1
```

- Tick T spawn은 상태·serialization·대상 후보에 존재한다.
- 같은 Tick 피해·보호·상태 대상이 될 수 있다.
- T+1 전에는 이동·target 선택·action/skill/protection commit·점령 기여가 불가하다.
- spawn 즉시 무적·선공권을 주지 않는다.

### R30~R40

- 모든 이동 Intent는 같은 start snapshot에서 생성한다.
- 충돌·anchor·movement layer 결과를 일괄 반영한다.
- callback·child order를 권위로 사용하지 않는다.

### R50

- 이동 완료 snapshot에서 filter→priority→stable tie-break를 평가한다.
- 기본 same-lane이며 cross-lane은 명시 scope와 quantized distance가 필요하다.

### R60

- 모든 적격 actor는 같은 post-movement snapshot에서 commit한다.
- 낮은 ID가 먼저 피해를 주어 다른 actor의 같은 Tick 행동을 삭제하지 않는다.
- active actor의 합법 Protection commit은 같은 Tick R80B 적용이 가능하다.

### R70

- immutable commit snapshot으로 Damage·Restore·Protection·Status Intent를 만든다.
- channel·delivery·target profile·root effect provenance를 기록한다.

### R80

```text
R80A VALIDITY_AND_ELIGIBILITY
R80B PROTECTION_SETUP
R80C DAMAGE_MITIGATION_AND_BARRIER
R80D HP_LOSS_REDIRECTION_AND_FLOOR
R80E HP_DELTA_AND_RESTORE
R80F STATUS_APPLICATION_AND_POST_HIT_QUEUE
R80G DEATH_OR_DESTRUCTION_MARK
```

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
BARRIER != HP_OR_HEAL
RESTORE != NEGATIVE_DAMAGE
TRANSFER_DEPTH_MAX = 1
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
```

### R90

- 동일 Tick 합법 commit을 actor ID 순서로 취소하지 않는다.
- damage/effect batch 뒤 죽음·파괴를 원자 확정한다.

### R100

- post-death 생존자와 post-destruction 가동 상태만 사용한다.
- spawn됐지만 아직 inactive인 개체는 contestant가 아니다.

### R110

- 전투 clock Timer만 integer Tick으로 진행한다.
- 상태·보호는 `[start_tick,end_tick_exclusive)`를 따른다.
- pause에서는 모든 전투 Timer가 함께 멈춘다.

### R120

- 모든 barrier 적용 뒤 canonical state를 직렬화한다.
- ordered event·lane contribution·other-two-lane contribution·fingerprint를 기록한다.
- fingerprint 뒤 state mutation은 다음 Tick까지 금지한다.

### R130

- invariant를 검사하고 Save 가능 canonical boundary를 연다.
- mid-phase Save는 금지한다.

## 8. 시간·Pause·Render 불변식

```text
AUTHORING_TIME = INTEGER_MILLISECONDS
RUNTIME_TIME_AUTHORITY = INTEGER_TICK
DURATION_TICKS = CEIL(duration_ms * 30 / 1000)
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
ACTIVE_COMBAT = TICK_ADVANCES
MAINTENANCE_PREPARATION_PAUSE = TICK_PAUSED
RENDER_INTERPOLATION = VISUAL_ONLY
GODOT_TIMER_ANIMATION_CALLBACK = NON_AUTHORITATIVE
TICK_SKIP_OR_MERGE = FORBIDDEN
```

## 9. 영웅·전설 Extension

허용:

```text
extra ability state
named trigger data
additional intents
status/protection payload
hero metrics tags
```

금지:

```text
separate clock
separate damage/death resolver
unordered callback effects
hidden target fallback
untracked direct HP mutation
```

## 10. Event Envelope

```text
event_id / battle_id / tick / phase_id / sequence
lane_id / source_id / target_id
root_effect_id / action_id / commit_id
deployment_id / token_source_id when applicable
event_type / reason_code / payload
```

시간 Event는 `spawn_tick`, `activation_tick`, `start_tick`, `end_tick_exclusive`, `next_due_tick`을 필요한 경우 포함한다.

## 11. 적대적 검토

```text
OMW-AUD-222 ~ 232 = schema·resolution risks
OMW-AUD-262 ~ 275 = fixed tick·time·activation risks
```

주요 방어:

- 배치 provenance 누락 금지.
- 세 전선 중 일부만 시뮬레이션해 승패 원인을 왜곡하지 않음.
- ID 순차 선공·조기 death·hidden retarget 금지.
- spawn same-tick action과 hidden immunity 모두 금지.
- wall clock·Timer·animation callback 권위 금지.
- pause clock leak·Tick skip·render writeback 금지.

## 12. 검증 Tier

```text
T0 = schema·time field·sort key validation
T1 = replay determinism across render cadence and save/load
T2 = phase·spawn·expiry·same-tick invariants
T3 = paired A/B/C metrics across all three lanes
T4 = aggregate balance after acceptance approval
T5 = product runtime adapter after separate authorization
```

## 13. 구현 경계

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
GDSCRIPT_SCENE_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
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
