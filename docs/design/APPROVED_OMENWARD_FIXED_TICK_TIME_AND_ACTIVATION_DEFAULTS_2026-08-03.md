# OMENWARD Fixed Tick·Time·Activation Defaults

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
grill_me_count: 5_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD 전투 도메인의 최초 시간 계약은 다음으로 확정한다.

```text
DOMAIN_TICKS_PER_SECOND = 30
DOMAIN_TICK_INDEX = SIGNED_64_BIT_INTEGER
AUTHORING_TIME_UNIT = INTEGER_MILLISECONDS
RUNTIME_TIME_AUTHORITY = INTEGER_DOMAIN_TICK
RENDER_FRAME = NON_AUTHORITATIVE_INTERPOLATION_ONLY
WALL_CLOCK = NON_AUTHORITATIVE
GODOT_TIMER = NON_AUTHORITATIVE_FOR_COMBAT
```

```text
command scheduled at tick T
→ R10 command ingest
→ R20 spawn/materialize
→ activation_tick = T + 1
```

새로 생성된 전투 개체는 Tick `T`의 R20 이후 상태와 대상 후보에 존재하지만, `T+1` 이전에는 이동·대상 선택·공격·스킬·보호 행동을 commit하지 못한다.

## 2. 제품 코어와의 연결

이 결정은 반응 속도를 과시하기 위한 고주파 전투를 만드는 것이 아니다. 세 전선의 공세를 읽고 룰렛 결과를 비가역 배치한 원인이 같은 입력에서 같은 결과를 만들도록 시간축을 고정하는 제작 기반이다.

```text
공세 예고
→ 룰렛·건물 설계
→ SpinSnapshot 결과
→ scheduled lane commit
→ 30 TPS 공통 resolver
→ ordered event와 fingerprint
→ 결과 원인 복기
→ 다음 Stage 설계
```

Tick rate·Timer·spawn 순서가 hidden RNG처럼 작동해 전선 판단을 덮으면 실패다.

## 3. 범위

### 포함

- 30 TPS 도메인 Tick.
- integer millisecond authoring과 millisecond→tick 변환.
- `[start_tick, end_tick_exclusive)` 활성 구간.
- R00 expiry와 due-event 경계.
- R10 command ingest와 R20 spawn·activation.
- 생성 Tick과 행동 가능 Tick의 분리.
- 전투·정비·준비·일시정지의 clock 진행 의미.
- Save/Load용 integer tick 상태.
- 렌더 보간과 전투 권위의 분리.
- catch-up·overload 시 Tick 생략 금지.
- Barrier·DOT/HOT·Control·lockout의 승인 ms 값 변환.

### 제외

- 이동속도·사거리·위치 quantization scale.
- 공격속도·cooldown·영웅별 Timer 실제 값.
- source/target modifier stacking과 effect precedence.
- runtime adapter의 최대 catch-up step 수.
- UI pause 허용 여부와 Danger 규칙의 콘텐츠 정책.
- GDScript·Scene·Resource·fixture·test 구현.
- Simulation 실행과 성능·밸런스 결론.

## 4. Tick 기본 계약

```text
FIRST_DOMAIN_TICK = 0
CURRENT_TICK = non-negative signed 64-bit integer
ONE_DOMAIN_STEP = exactly one increment
TICK_DURATION_SECONDS = 1 / 30
```

전투 resolver는 frame delta를 소비하지 않는다. 한 번의 도메인 step은 항상 R00부터 R130까지 정확히 한 번 실행한다.

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

## 5. Millisecond→Tick 변환

데이터와 Fixture는 사람이 읽을 수 있는 integer millisecond를 사용한다. 로드·validation 단계에서 한 번만 integer tick으로 변환하고 전투 중에는 원본 ms를 다시 계산하지 않는다.

```text
if duration_ms < 0:
    data = INVALID
elif duration_ms == 0:
    duration_ticks = 0
else:
    duration_ticks = ceil(duration_ms * 30 / 1000)
```

float 없는 양의 정수식:

```text
duration_ticks = (duration_ms * 30 + 999) div 1000
```

- 양수 지속시간을 0 Tick으로 축소하지 않는다.
- 승인된 ms보다 짧아지는 floor 변환을 금지한다.
- 변환 결과와 원본 ms를 T0 validation report에 함께 기록한다.
- duration·interval·cooldown은 load 후 integer tick만 전투 권위로 사용한다.

현재 승인된 정확 변환:

```text
3000ms Barrier duration       = 90 ticks
1000ms DOT/HOT pulse interval = 30 ticks
2000ms Control duration max   = 60 ticks
1000ms Control lockout        = 30 ticks
```

## 6. 활성 구간·Expiry

모든 보호·상태·활성 효과는 다음 반개구간을 사용한다.

```text
ACTIVE_WHEN = start_tick <= current_tick < end_tick_exclusive
```

R00 규칙:

```text
if end_tick_exclusive <= current_tick:
    expire before R10
```

따라서 `end_tick_exclusive = T`인 Barrier는 Tick `T`의 R80 피해를 막지 않는다. 만료 Event는 R00에서 남기며, 이후 phase가 만료된 instance를 재사용하면 invalid다.

`duration_ticks = 0`인 즉시 효과는 지속 instance를 만들지 않고 해당 intent의 승인 phase에서만 해결한다. 0 Tick Barrier·Control·DOT/HOT instance는 금지한다.

## 7. DOT/HOT·Control 시간

### DOT/HOT

```text
first_due_tick = start_tick + interval_ticks
next_due_tick = previous_due_tick + interval_ticks
emit only when due_tick < end_tick_exclusive
```

- 적용 Tick에 즉시 pulse를 추가하지 않는다.
- 각 pulse는 새 `DamageIntent` 또는 `RestoreIntent`다.
- frame 지연으로 due Tick이 지나가도 pulse를 합치거나 삭제하지 않는다.
- 동일 Tick에 여러 due event가 있으면 canonical effect key로 정렬한다.

### Control·Lockout

```text
control active = [control_start_tick, control_end_tick_exclusive)
lockout active = [control_end_tick_exclusive, control_end_tick_exclusive + 30)
```

- Tick 경계에서 Control과 동일 group lockout이 겹치지 않는다.
- lockout 중 같은 `stacking_group_id`의 Control은 reason event와 함께 거절한다.
- Control이 새로 적용돼도 이미 R60에서 commit된 행동을 소급 취소하지 않는다.

## 8. Command·Spawn·Activation

외부 명령은 다음 키를 가진다.

```text
command_id
scheduled_tick
command_order
actor_or_source_id
payload
```

R10에서 다음만 수용한다.

```text
scheduled_tick == current_tick
```

- 과거 Tick 명령은 자동 보정하지 않고 `PAST_COMMAND_REJECTED`로 거절한다.
- 미래 Tick 명령은 queue에 유지한다.
- 같은 Tick 명령의 `command_order`가 충돌하면 Fixture·Save data는 invalid다.

R20 Spawn:

```text
spawn_tick = current_tick
activation_tick = spawn_tick + 1
```

Tick `T`에서 생성된 개체:

- R20 이후 canonical state와 serialization에 존재한다.
- R50 대상 후보가 될 수 있다.
- 피해·보호·상태의 대상이 될 수 있다.
- Objective contestant·점령 기여자가 되지 않는다.
- 이동 Intent·Target 선택·Action/Skill Commit·ProtectionIntent를 만들지 못한다.
- Tick `T+1`의 R20 activation 검사 뒤 적격 행동이 가능하다.

생성 즉시 무적·숨은 선공권은 없다. 생성 직후 공격받아 R90에서 사망할 수 있으며, 이 결과는 명시적 spawn·damage event로 설명돼야 한다.

## 9. 같은 Tick Protection 경계

이미 활성화된 actor가 Tick `T`의 R60에서 합법적으로 commit한 `ProtectionIntent`는 Tick `T`의 R80B에서 materialize할 수 있다.

```text
active before R60
+ valid protection action commit
→ same-tick R80B protection setup allowed
```

새로 spawn된 actor는 Tick `T`에 action commit 자격이 없으므로 같은 Tick 보호를 생성하지 못한다. 외부 시스템이 R10 command로 직접 부여하는 Protection은 action과 구분된 명시적 command type과 별도 승인 없이는 금지한다.

## 10. Clock 진행·Pause

```text
ACTIVE_COMBAT = DOMAIN_TICK_ADVANCES
MAINTENANCE = DOMAIN_TICK_PAUSED
PREPARATION = DOMAIN_TICK_PAUSED
APPLICATION_PAUSE = DOMAIN_TICK_PAUSED
WALL_CLOCK_ELAPSED_WHILE_PAUSED = IGNORED_BY_COMBAT
```

- 전투 pause 가능 여부는 Normal/Danger UX·콘텐츠 정책이 소유한다.
- pause가 허용되면 모든 전투 Timer·Status·Barrier·cooldown·DOT/HOT due Tick이 함께 멈춘다.
- 일부 시스템만 wall clock으로 진행하는 혼합 clock을 금지한다.
- 정비·준비 화면에서 전투 도메인 Tick은 진행하지 않는다.
- analytics wall time은 기록할 수 있지만 combat state를 변경하지 않는다.

## 11. Save·Load

Save authority:

```text
tick_index
scheduled commands with scheduled_tick
activation_tick
start_tick / end_tick_exclusive
next_due_tick
remaining integer cooldown ticks
ordered event sequence state
named RNG stream state
```

금지:

```text
float seconds remaining as sole authority
render interpolation alpha as authority
Timer node remaining time as authority
wall-clock timestamp reconstruction of combat timers
```

Load 후 첫 domain step은 저장된 `tick_index`와 phase boundary에서 시작한다. mid-phase save는 현 Slice에서 금지하며 Save는 R130 이후 canonical boundary에서만 생성한다.

## 12. Runtime Adapter·Render 보간

Runtime adapter는 실제 시간 누적치를 사용해 필요한 domain step 수를 계산할 수 있지만 각 step의 내부 결과를 바꾸지 않는다.

```text
render frame
→ zero or more complete domain ticks
→ previous canonical transform + current canonical transform
→ visual interpolation only
```

- interpolation 결과를 domain position에 되쓰지 않는다.
- animation callback·Tween 완료·Timer timeout은 Action·Damage·Death 권위가 아니다.
- overload 시 Tick을 합치거나 건너뛰지 않는다.
- 실행이 늦으면 wall-clock 진행이 느려질 수 있으나 deterministic state sequence는 보존한다.
- product runtime의 catch-up 상한·slow-mode UX는 별도 technical Decision이 소유한다.

## 13. Event·Fingerprint 필드

시간 관련 Event는 최소 다음을 기록한다.

```text
tick
phase_id
event_sequence
scheduled_tick_if_any
spawn_tick_if_any
activation_tick_if_any
start_tick_if_any
end_tick_exclusive_if_any
next_due_tick_if_any
duration_ms_source_if_authored
converted_duration_ticks_if_applicable
root_effect_id
deployment_id_if_applicable
```

R120 fingerprint에는 wall clock·render FPS·interpolation alpha·Timer node identity를 포함하지 않는다.

## 14. Benchmark·Production 비교

### Godot Physics Interpolation

공식 문서는 렌더 프레임과 물리 Tick을 분리하고 낮은 Tick 주기에서 보간으로 시각적 부드러움을 보완하는 방식을 제공한다.

```text
ADOPT = render/domain separation + interpolation concept
ADAPT = 30 TPS strategy autobattle domain
REJECT = engine callback order as combat authority
```

근거:

- `https://docs.godotengine.org/en/4.7/tutorials/physics/interpolation/2d_and_3d_physics_interpolation.html`
- `https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/using_physics_interpolation.html`

### Godot Timer

Timer는 제품 UI·비전투 편의 기능에 사용할 수 있지만 float 시간과 callback 처리 순서를 결정론적 전투 권위로 사용하지 않는다.

```text
ADOPT = non-authoritative convenience timing where safe
REJECT = Timer timeout as combat resolver trigger
```

근거:

- `https://docs.godotengine.org/en/4.x/classes/class_timer.html`

### 대안 비교

```text
20 TPS = lower cost but coarser targeting/movement reaction
30 TPS = selected balance of responsiveness and simulation cost
60 TPS = higher cost without validated strategy benefit
```

외부 엔진의 기본값을 정본으로 복사하지 않고 OMENWARD의 세 전선·대량 seed simulation·PC 우선 표현 경계에 맞춰 30 TPS를 채택한다.

## 15. 적대적 검토

| Audit ID | 공격 | 결론·완화 |
|---|---|---|
| OMW-AUD-262 | wall clock이 전투 Timer를 움직임 | integer domain tick만 권위 |
| OMW-AUD-263 | ms floor 변환으로 승인 지속시간 단축 | 양수 ceil 변환 |
| OMW-AUD-264 | 양수 duration이 0 Tick이 됨 | 양수 최소 1 Tick |
| OMW-AUD-265 | end Tick에도 Barrier가 남는 fencepost | R00 exclusive expiry |
| OMW-AUD-266 | spawn 개체가 같은 Tick 선공 | activation `T+1` |
| OMW-AUD-267 | spawn 개체가 숨은 무적 획득 | 같은 Tick targetable·damageable |
| OMW-AUD-268 | entity ID에 따라 same-tick 보호 획득 | active actor commit batch만 허용 |
| OMW-AUD-269 | Timer·animation callback이 결과 권위 | non-authoritative로 금지 |
| OMW-AUD-270 | pause 중 일부 status만 진행 | 전체 domain clock 동결 |
| OMW-AUD-271 | Save에 float 잔여시간 저장 | integer absolute/remaining tick 저장 |
| OMW-AUD-272 | frame overload에서 Tick 병합·유실 | complete step 유지·skip 금지 |
| OMW-AUD-273 | render interpolation이 state에 역기록 | visual-only·writeback 금지 |
| OMW-AUD-274 | 과거 scheduled command 자동 보정 | 명시적 reject event |
| OMW-AUD-275 | 장기 run의 tick overflow | signed 64-bit tick index |

## 16. 검증 계약

### T0 Schema

- Tick rate가 정확히 30.
- 모든 authoring time이 비음수 integer ms.
- 양수 ms의 변환이 1 Tick 이상.
- 승인된 3000/1000/2000/1000ms 변환이 90/30/60/30 Tick.
- active interval이 exclusive end를 가짐.
- spawned entity가 spawn_tick·activation_tick을 가짐.
- Save가 R130 boundary에서만 생성됨.

### T1 Replay

- render FPS·wall-clock 속도·interpolation 설정이 달라도 ordered domain event와 fingerprint가 동일.
- pause/resume 뒤 같은 command sequence에서 동일 결과.
- Save/Load replay가 uninterrupted replay와 동일.
- 첫 divergent tick·phase·event를 보고.

### T2 Invariant

- Tick T expiry는 R10 이전 제거.
- due Tick이 end exclusive 이상이면 pulse 없음.
- Tick T spawn은 T 행동 commit 없음.
- Tick T spawn은 T 대상이 될 수 있음.
- active actor의 합법 Protection commit은 same-tick R80B 적용 가능.
- pause 중 domain timers 불변.
- overload adapter가 Tick을 삭제·병합하지 않음.

### T3 Paired A/B/C

- 동일 Fixture를 20/30/60 TPS exploratory adapter로 비교할 수 있으나 30 TPS만 승인 baseline.
- 세 전선 target switch·spawn survival·effect expiry 차이를 분리 보고.
- balance 결론은 sample/tolerance Decision 전까지 금지.

## 17. 구현 금지선

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
GDSCRIPT = NOT_AUTHORIZED
SCENE_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 문서는 구현 계획과 실행 권한이 아니다. 기획 정본과 후속 구현의 검증 계약만 정의한다.

## 18. 다음 Gate

```text
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
NEXT_PREFLIGHT = AT_10_OF_10
GRILL_ME_COUNT = 5/10
```
