# OMENWARD 공통 전투 Schema·Resolution Order

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
child_damage_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
grill_me_count: 2_OF_10
current_branch_counter: 3_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD의 최초 공통 전투 계약은 **코어 우선 공통 Schema**로 구성한다.

```text
공세·세 전선 상태
→ SpinSnapshot·TokenSource가 추적되는 배치 명령
→ 표준 유닛·적·건물·목표 공통 상태
→ fixed-tick phase resolver
→ ordered event·metrics·fingerprint
→ 결과 원인 복기
```

영웅·전설·고유 2스킬은 공통 전투 계약 위에 올라가는 확장 계층이다. 초기 공통 Schema를 특정 영웅 5명의 예외에 맞춰 설계하지 않는다.

룰렛 전체·경제 전체를 P1 전투 Harness가 다시 계산하지는 않는다. 대신 전장에 들어온 모든 유닛은 룰렛 결과와 비가역 전선 커밋을 추적할 수 있는 `DeploymentProvenance`를 필수로 가진다.

## 2. 목적과 플레이어 코어 연결

```text
건물·TokenSource가 미래 릴 구조를 변경
→ SpinSnapshot에서 병력 결과 생성
→ 플레이어가 한 전선에 비가역 커밋
→ 표준 전투 규칙으로 전황 변화
→ event provenance로 결과 원인 설명
→ 다음 Stage 설계에 환류
```

따라서 세 전선, 배치 provenance, 건물·목표·점령, 다른 두 전선의 상태와 기여도는 공통 Schema의 선택 필드가 아니라 필수 경계다.

## 3. 범위

### 3.1 포함

- `CombatRunState`, `LaneState`, `CombatantState`, `BuildingState`, `ObjectiveState`.
- `DeploymentProvenance`, `OrderedCommand`, `ActionIntent`, `EffectIntent`.
- `ProtectionInstance`, `StatusInstance`, `PendingCommit`, `ActiveEffect`, `RngStreamState`.
- quantized 2D 위치와 lane·anchor 관계.
- 표준 이동·targeting·공격·효과·죽음·파괴·점령 순서.
- 공통 event envelope·phase barrier·fingerprint 시점.
- 세 전선 전체 상태와 다른 두 전선의 기여 metric.
- 영웅·전설이 공통 필드를 상속·확장할 수 있는 명시적 extension seam.

### 3.2 제외

- 룰렛 회전·릴 편집·경제 분포의 실제 실행.
- 정확 tick rate·피해·방어·이동속도·사거리·cooldown 수치.
- 다섯 영웅 고유 2스킬의 exact Trigger·효과값.
- 전설 전체 exact kit와 허용오차.
- Godot SceneTree·NavigationServer·PhysicsServer를 전투 권위로 사용.
- GDScript·Scene·Resource·test·fixture 구현.
- simulation 실행과 밸런스 결론.

Damage·Protection·Status 의미는 하위 책임 원본 `design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`가 소유한다. 이 부모 문서는 phase 위치와 공통 extension seam만 소유한다.

## 4. 공통 상태 Schema

### 4.1 `CombatRunState`

```text
schema_version
engine_contract_version
parameter_set_id
battle_id
map_id / stage_id / wave_id
tick_index
phase_id
lane_states[TOP, MID, BOTTOM]
combatants_by_id + canonical_combatant_order
buildings_by_id + canonical_building_order
objectives_by_id + canonical_objective_order
scheduled_commands
pending_commits
active_effects
protection_instances
status_instances
named_rng_streams
event_sequence_state
termination_state
```

ID lookup table은 허용하지만 Dictionary·SceneTree 순회를 resolution order로 사용하지 않는다. 모든 resolver는 명시적 canonical order 배열 또는 sort key를 사용한다.

### 4.2 `LaneState`

```text
lane_id
lane_order
segment_states
frontline_anchor_id
combatant_ids
building_ids
objective_ids
pending_deployment_ids
lane_pressure_metrics
lane_contribution_metrics
```

`lane_order`는 `TOP=0`, `MID=1`, `BOTTOM=2`로 고정한다. 이 순서는 결과 우선권이 아니라 canonical serialization·event 정렬용이다.

### 4.3 `CombatantState`

```text
entity_id
spawn_sequence
side
unit_archetype_id
grade / tier
lane_id
position_q{x_q,y_q,anchor_id}
facing
movement_layer / collision_class
hp_q / max_hp_q
armor_q / resistance_q
attack_state
ability_state_refs
target_id
role_tags
protection_instance_ids
status_instance_ids
deployment_provenance
alive / death_pending
```

위치는 quantized 2D 좌표를 사용한다. 단일 1D lane 좌표만 사용하면 실제 거리 기반 호위 오라와 명시적 cross-lane 범위를 검증할 수 없으므로 금지한다.

### 4.4 `DeploymentProvenance`

```text
deployment_id
spin_snapshot_id
pending_reward_id
token_instance_id
token_source_id
reward_resolution_sequence
lane_commit_id
commit_sequence
source_building_or_system_id
```

전투 Harness는 이 출처를 소비하지만 룰렛 결과를 재추첨하지 않는다. 전투 결과 event는 최소한 `deployment_id`까지 역추적 가능해야 한다.

### 4.5 `BuildingState`

```text
building_id
node_id
building_type / tier
owner_side
lane_id
position_q
hp_q / max_hp_q
armor_q / resistance_q
operational_state
targetable_flags
passive_effect_refs
active_action_state
protection_instance_ids
status_instance_ids
alive / destruction_pending
```

전투에 직접 영향을 주지 않는 경제 상세는 별도 경제 Schema가 소유한다. 전투 중인 건물의 소유권·HP·방어축·가동 상태·전투 효과 출처는 공통 전투 상태에 존재해야 한다.

### 4.6 `ObjectiveState`

```text
objective_id
objective_type
lane_id
segment_id
position_q
owner_side
capture_progress_q
capture_state
eligible_contestant_ids
blocked_or_locked_state
ownership_change_sequence
hp_targetable_flag
```

점령은 유닛 수·Tier·등급의 합산 `capture_power`를 부활시키지 않는다. Objective는 기본 HP target이 아니며 파괴형 Objective는 별도 승인과 명시적 flag가 필요하다.

### 4.7 공통 행동·효과

```text
OrderedCommand:
  command_id / scheduled_tick / command_order / actor_id / payload

ActionIntent:
  intent_id / source_id / action_type / commit_tick / target_snapshot / position_snapshot / interrupt_policy

EffectIntent:
  effect_id / source_id / target_ids / effect_category / raw_payload / application_priority

ProtectionInstance:
  protection_id / protection_type / source_id / owner_id / start_tick / end_tick_exclusive / remaining_budget_q / filter / consume_priority

StatusInstance:
  status_instance_id / status_type / source_id / start_tick / end_tick_exclusive / stacking_group_id / stacking_policy / stack_state / payload

PendingCommit:
  commit_id / source_id / immutable_target_snapshot / immutable_position_snapshot / resolve_tick / resolved_flag

ActiveEffect:
  effect_instance_id / owner_id / start_tick / end_tick_exclusive / remaining_budget_q / cleanup_policy
```

새로운 target으로 자동 fallback하지 않는다. commit 뒤 대상 상실은 효과 유형별 `CANCEL`, `RESOLVE_AT_COMMITTED_POINT`, `RESOLVE_ON_SNAPSHOT` 중 명시된 정책으로만 처리한다.

## 5. Canonical Sort Key

```text
lane_order
→ entity_kind_order
→ spawn_sequence
→ stable_entity_id
→ local_sequence
```

공통 event key:

```text
tick
→ phase_order
→ resolver_order
→ source_canonical_key
→ local_sequence
```

stable ID 정렬은 결과를 결정하는 은닉 AI가 아니다. phase snapshot과 barrier가 결과 의미를 소유하고, sort key는 동일 결과의 표현 순서를 고정한다.

## 6. Fixed-Tick Resolution Order

```text
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

### `R00 TICK_OPEN_AND_EXPIRE`

- `end_tick_exclusive <= current_tick` 상태·효과·보호를 제거한다.
- 이전 tick에서 완료된 cleanup을 검증한다.
- 현재 tick 전투 권위 snapshot을 연다.

### `R10 ORDERED_COMMAND_INGEST`

- 외부 입력은 `(scheduled_tick, command_order, command_id)`로 적용한다.
- 같은 tick 배치·건설·전술 명령은 명시적 순서가 없으면 fixture invalid다.
- 입력 처리 중 global RNG·wall clock·frame delta 사용은 금지한다.

### `R20 SPAWN_AND_ACTIVATION`

- 유효한 배치 provenance와 lane commit을 검증한다.
- `activation_tick` 필드로 행동 가능 시점을 명시한다.
- 정확한 즉시 행동/다음 tick 행동 정책은 후속 numeric/technical Decision까지 parameterized 상태로 둔다.

### `R30~R40 MOVEMENT`

- 이동 intent는 같은 start snapshot에서 생성한다.
- 충돌·anchor·movement layer 규칙으로 barrier에서 일괄 반영한다.
- SceneTree child order·NavigationServer callback order를 전투 권위로 사용하지 않는다.

### `R50 TARGET_SENSE_AND_SELECT`

- 이동 완료 snapshot에서 filter→priority→stable tie-break를 평가한다.
- 기본 범위는 same-lane이며 cross-lane은 명시적 scope와 quantized distance가 있을 때만 허용한다.
- target 후보 배열은 canonical order로 생성한다.

### `R60 ACTION_AND_SKILL_COMMIT`

- 같은 post-movement snapshot에서 모든 적격 actor가 intent를 commit한다.
- 낮은 stable ID actor가 먼저 피해를 줘 높은 ID actor의 같은 tick 적격 행동을 지우는 순차 편향을 금지한다.
- commit 뒤 source 사망 시 처리 방식은 `interrupt_policy`가 소유하며 숨은 예외를 두지 않는다.

### `R70 IMPACT_AND_EFFECT_INTENT_BUILD`

- immutable commit snapshot으로 Damage·Restore·Protection·Status intent를 생성한다.
- channel·delivery tag·target profile·root effect provenance를 명시한다.
- target 상실 뒤 hidden fallback을 생성하지 않는다.

### `R80 DAMAGE_PROTECTION_STATUS_APPLY`

세부 권위는 Damage 책임 원본이 소유한다.

```text
R80A VALIDITY_AND_ELIGIBILITY
R80B PROTECTION_SETUP
R80C DAMAGE_MITIGATION_AND_BARRIER
R80D HP_LOSS_REDIRECTION_AND_FLOOR
R80E HP_DELTA_AND_RESTORE
R80F STATUS_APPLICATION_AND_POST_HIT_QUEUE
R80G DEATH_OR_DESTRUCTION_MARK
```

상위 불변식:

```text
KINETIC → ARMOR
ARCANE → RESISTANCE
BARRIER != HP_OR_HEAL
RESTORE != NEGATIVE_DAMAGE
TRANSFER_DEPTH_MAX = 1
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
```

정확 mitigation formula·rounding·cap·duration은 후속 numeric Decision이다.

### `R90 DEATH_AND_DESTRUCTION_FINALIZE`

- 동일 tick commit된 합법 행동을 actor ID 순서로 취소하지 않는다.
- damage/effect batch 뒤 죽음·파괴를 원자 확정한다.
- 파괴된 건물의 passive effect는 이후 phase부터 제거되지만 이미 commit된 합법 행동을 소급 취소하지 않는다.

### `R100 OBJECTIVE_AND_OWNERSHIP_RESOLVE`

- post-death 생존자와 post-destruction 가동 상태만 사용한다.
- 사망·파괴 전 snapshot을 점령 기여에 재사용하지 않는다.
- 소유권 변경은 event·건설권·전투 효과에 하나의 ownership sequence로 기록한다.

### `R110 TIMER_COOLDOWN_STATUS_ADVANCE`

- 전투 clock에 속한 timer만 진행한다.
- status·protection은 `[start_tick, end_tick_exclusive)` 규칙을 따른다.
- 정비시간 pause·Stage carry 정책은 기존 영웅 timer 정본을 따른다.

### `R120 METRICS_EVENT_FINGERPRINT`

- 모든 phase barrier 적용 뒤 canonical state를 직렬화한다.
- ordered event log·lane contribution·other-two-lane contribution·fingerprint를 기록한다.
- raw damage·mitigated damage·barrier absorbed·final HP loss를 분리한다.
- fingerprint 생성 뒤 state mutation은 금지하며 다음 tick에서만 변경한다.

## 7. 동일 Tick 공정성 불변식

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
DESTROYED_BUILDING_PASSIVE_REMOVED_AFTER_FINALIZE = REQUIRED
RETROACTIVE_STATUS_COMMIT_CANCELLATION = FORBIDDEN
CANONICAL_EVENT_ORDER = REQUIRED
```

## 8. 영웅·전설 Extension Seam

영웅·전설은 다음 공통 요소를 재사용한다.

```text
CombatantState
ActionIntent / EffectIntent
DamageIntent / RestoreIntent / ProtectionIntent / StatusApplicationIntent
PendingCommit
ActiveEffect / ProtectionInstance / StatusInstance
Target Filter/Priority/Tie-break
Damage/Protection hooks
Timer/Stage boundary
Event envelope
```

영웅별 별도 AI loop·별도 tick clock·별도 death resolver·별도 save identity를 만들지 않는다. 고유 2스킬은 공통 resolver에 data payload와 허용된 effect category를 제공한다.

## 9. 벤치마크·현업 비교

- Godot fixed processing·instance RNG·JSON serialization 경계를 참고하되 엔진 callback 자체를 결정론 권위로 사용하지 않는다.
- TFT의 Armor/Magic Resistance 분리는 두 방어축의 읽기 쉬운 참고 사례지만 아이템 중심 메타를 복사하지 않는다.
- Guild Wars 2 Barrier의 임시 HP buffer·분리 UI를 참고하되 exact cap·duration을 복사하지 않는다.
- Overwatch barrier 조정 사례처럼 barrier uptime이 전투 pace와 선택을 대체하면 stop-ship으로 본다.
- 외부 게임 전투 순서를 복사하지 않고 OMENWARD의 세 전선·TokenSource·SpinSnapshot·비가역 배치·점령 인과를 우선한다.

## 10. 적대적 검토

```text
OMW-AUD-222 ~ OMW-AUD-232 = common schema·resolution order
OMW-AUD-233 ~ OMW-AUD-246 = damage·protection·status semantics
```

핵심 방어:

- `DeploymentProvenance` 필수.
- 영웅 special-case Schema 금지.
- phase snapshot·intent·barrier 필수.
- damage batch 뒤 death finalize.
- post-death objective.
- channel/tag/target profile 분리.
- barrier·restore·redirection 의미 분리.
- 일반 status의 same-tick 소급 취소 금지.
- R120 fingerprint 이후 mutation 금지.

## 11. 검증 계약

```text
T0:
  required field·enum·ID·provenance·canonical order
  exactly-one channel·valid tags·target profile·stacking policy

T1:
  동일 fixture·input·RNG에서 phase event와 final fingerprint 동일

T2:
  same-tick fairness·death/objective order·no fallback·provenance
  no true/execute/revive·no recursive transfer·barrier/restore/status invariants

T3:
  세 전선 전체·other-two-lane contribution·KINETIC/ARCANE 대응을 포함한 paired A/B/C
```

현재는 테스트 파일을 만들거나 실행하지 않는다.

## 12. 경계·후속

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
COMMON_COMBAT_SCHEMA = USER_APPROVED_DOCUMENTED_NOT_IMPLEMENTED
DAMAGE_PROTECTION_STATUS_SEMANTICS = USER_APPROVED_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_MITIGATION_FORMULA = PENDING
EXACT_ARMOR_RESISTANCE_DEFAULTS = PENDING
EXACT_BARRIER_BUDGET_CAP_DURATION = PENDING
EXACT_STATUS_STACK_CAP_DURATION = PENDING
EXACT_TICK_RATE_AND_ACTIVATION_POLICY = PENDING
EXACT_HERO_TRIGGER_TIMER_EFFECT_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
CURRENT_BRANCH_GRILL_ME_COUNT = 3/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
