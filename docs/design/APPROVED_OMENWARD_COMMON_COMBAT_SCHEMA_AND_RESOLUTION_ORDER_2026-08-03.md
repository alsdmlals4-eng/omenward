# OMENWARD 공통 전투 Schema·Resolution Order

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
grill_me_count: 2_OF_10
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

이 결정의 목적은 추상적인 범용 전투 엔진을 만드는 것이 아니다. 다음 OMENWARD 인과를 재현·검증 가능하게 만드는 것이다.

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
- `StatusInstance`, `PendingCommit`, `ActiveEffect`, `RngStreamState`.
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
attack_state
ability_state_refs
target_id
role_tags
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
operational_state
targetable_flags
passive_effect_refs
active_action_state
alive / destruction_pending
```

전투에 직접 영향을 주지 않는 경제 상세는 별도 경제 Schema가 소유한다. 다만 전투 중인 건물의 소유권·HP·가동 상태·전투 효과 출처는 공통 전투 상태에 존재해야 한다.

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
```

점령은 유닛 수·Tier·등급의 합산 `capture_power`를 부활시키지 않는다. exact 점령 속도는 별도 값 계약이 소유한다.

### 4.7 공통 행동·효과

```text
OrderedCommand:
  command_id / scheduled_tick / command_order / actor_id / payload

ActionIntent:
  intent_id / source_id / action_type / commit_tick / target_snapshot / position_snapshot / interrupt_policy

EffectIntent:
  effect_id / source_id / target_ids / effect_category / raw_payload / application_priority

StatusInstance:
  status_instance_id / status_type / source_id / start_tick / end_tick_exclusive / stack_state / payload

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

- `end_tick_exclusive <= current_tick` 상태·효과를 제거한다.
- 이전 tick에서 완료된 cleanup을 검증한다.
- 현재 tick 전투 권위 snapshot을 연다.

### `R10 ORDERED_COMMAND_INGEST`

- 외부 입력은 `(scheduled_tick, command_order, command_id)`로 적용한다.
- 같은 tick 배치·건설·전술 명령은 명시적 순서가 없으면 fixture invalid다.
- 입력 처리 중 global RNG·wall clock·frame delta 사용은 금지한다.

### `R20 SPAWN_AND_ACTIVATION`

- 유효한 배치 provenance와 lane commit을 검증한다.
- `activation_tick` 필드로 행동 가능 시점을 명시한다.
- 정확한 즉시 행동/다음 tick 행동 정책은 후속 값 계약까지 parameterized 상태로 둔다.

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

### `R70~R80 IMPACT·DAMAGE·EFFECT`

공통 적용 단계:

```text
impact validity
→ immunity / eligibility
→ pre-mitigation modifier
→ armor / resistance formula hook
→ barrier / absorption
→ health-floor clamp
→ HP delta or restore
→ post-hit status and trigger
→ death_or_destruction_mark
```

정확 공식·상한·최소 피해·회복량은 후속 Decision이다. `health-floor`는 회복이 아니며 실제 HP를 증가시키지 않는다. 명시적 revive 계약 없이는 사망 상태를 되돌리지 않는다.

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
- status는 `[start_tick, end_tick_exclusive)` 규칙을 따른다.
- 정비시간 pause·Stage carry 정책은 기존 영웅 timer 정본을 따른다.

### `R120 METRICS_EVENT_FINGERPRINT`

- 모든 phase barrier 적용 뒤 canonical state를 직렬화한다.
- ordered event log·lane contribution·other-two-lane contribution·fingerprint를 기록한다.
- fingerprint 생성 뒤 state mutation은 금지하며 다음 tick에서만 변경한다.

## 7. 동일 Tick 공정성 불변식

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
DESTROYED_BUILDING_PASSIVE_REMOVED_AFTER_FINALIZE = REQUIRED
CANONICAL_EVENT_ORDER = REQUIRED
```

## 8. 영웅·전설 Extension Seam

영웅·전설은 다음 공통 요소를 재사용한다.

```text
CombatantState
ActionIntent
PendingCommit
ActiveEffect
StatusInstance
Target Filter/Priority/Tie-break
Damage/Protection hooks
Timer/Stage boundary
Event envelope
```

영웅별 별도 AI loop·별도 tick clock·별도 death resolver·별도 save identity를 만들지 않는다. 고유 2스킬은 공통 resolver에 data payload와 허용된 effect category를 제공한다.

## 9. 벤치마크·현업 비교

Godot 4.x 공식 문서는 `_physics_process()`가 가변 렌더 frame과 분리된 고정 주기로 실행됨을 설명한다. OMENWARD Harness는 이를 참고하되 엔진 callback 자체를 결정론 보장으로 오해하지 않고 명시적 integer tick과 phase barrier를 권위로 둔다.

Godot `RandomNumberGenerator`는 instance별 seed·state 저장과 재현 가능한 sequence를 제공한다. OMENWARD는 전역 RNG 대신 domain별 named stream·state·draw count를 기록한다.

Godot JSON parser는 숫자 처리와 규격 허용 범위가 canonical hash 권위로 충분하지 않다. 따라서 raw JSON text가 아니라 stable field order·scaled integer·quantized position으로 normalized state를 만든다.

외부 게임의 전투 순서를 복사하지 않는다. OMENWARD의 세 전선·TokenSource·SpinSnapshot·비가역 배치·점령 인과가 이 Schema의 우선 기준이다.

## 10. 적대적 검토

| Audit ID | 공격 | 판정·대응 |
|---|---|---|
| `OMW-AUD-222` | 범용 Schema가 룰렛 인과를 지움 | `DeploymentProvenance` 필수 |
| `OMW-AUD-223` | 영웅 5명 예외가 공통 Schema를 오염 | 영웅은 extension seam만 사용 |
| `OMW-AUD-224` | entity 순차 처리로 낮은 ID가 선공 특권 획득 | phase snapshot·intent·barrier 필수 |
| `OMW-AUD-225` | damage 중 즉시 death finalize로 같은 tick 반격 삭제 | damage batch 뒤 death finalize |
| `OMW-AUD-226` | target 상실 시 숨은 fallback이 결과 원인을 변경 | fallback 금지·명시적 commit policy |
| `OMW-AUD-227` | 사망한 유닛이 같은 tick 점령에 기여 | post-death survivors만 사용 |
| `OMW-AUD-228` | 건물 파괴가 이미 commit된 행동을 소급 취소 | commit 보존·passive는 이후 phase 제거 |
| `OMW-AUD-229` | 1D 위치가 cross-lane 실제 거리 효과를 왜곡 | quantized 2D position 필수 |
| `OMW-AUD-230` | Schema 승인에 exact 밸런스 값이 밀수됨 | formula·rate·value는 pending 유지 |
| `OMW-AUD-231` | SceneTree·callback 순서가 도메인 결과를 지배 | pure domain canonical order 필수 |
| `OMW-AUD-232` | fingerprint 시점이 불명확해 replay diff가 흔들림 | R120 이후 mutation 금지 |

## 11. 검증 계약

```text
T0:
  required field·enum·ID·provenance·canonical order 검사

T1:
  동일 fixture·input·RNG에서 phase event와 final fingerprint 동일

T2:
  same-tick fairness·death/objective order·no fallback·provenance invariants

T3:
  세 전선 전체와 other-two-lane contribution을 포함한 paired A/B/C
```

필수 Red-test 후보는 후속 구현 계획에서 작성한다. 현재는 테스트 파일을 만들거나 실행하지 않는다.

## 12. 경계·다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
COMMON_COMBAT_SCHEMA = USER_APPROVED_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_TICK_RATE = PENDING
EXACT_DAMAGE_DEFENSE_PROTECTION_FORMULAS = PENDING
EXACT_ACTIVATION_POLICY = PENDING
EXACT_HERO_TRIGGER_TIMER_EFFECT_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 2/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
