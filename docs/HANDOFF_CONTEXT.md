# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_APPROVED
current_validation_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
working_branch: gpt/omenward-simulation-harness-planning-20260803
current_grill_me_count: 5_OF_10
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
```

### 시간축 핵심

```text
DOMAIN_TPS = 30
AUTHORING_TIME = integer ms
RUNTIME_TIME_AUTHORITY = integer tick
DURATION_TICKS = ceil(duration_ms * 30 / 1000)
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
```

```text
3000ms = 90 ticks
1000ms = 30 ticks
2000ms = 60 ticks
1000ms = 30 ticks
```

### Spawn·Activation

```text
scheduled command at Tick T
→ R10 ingest
→ R20 spawn
→ activation_tick = T + 1
```

Tick T spawn:

- canonical state·serialization·Target 후보에 존재.
- 피해·보호·상태 대상이 될 수 있음.
- 이동·Target 선택·Action·Skill·Protection commit 불가.
- Objective 점령 기여 불가.
- Tick T+1부터 적격 행동 가능.

## 4. R00~R130 핵심

```text
R00 expiry before commands
R10 ordered command ingest
R20 spawn and activation
R30 movement intent
R40 movement resolve
R50 target select
R60 action/skill commit
R70 impact/effect intents
R80 damage/protection/status
R90 death/destruction
R100 objective/ownership
R110 timer/status advance
R120 metrics/event/fingerprint
R130 close and save boundary
```

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
DEATH_FINALIZE_AFTER_DAMAGE_BATCH
OBJECTIVE_USES_POST_DEATH_ACTIVE_SURVIVORS
HIDDEN_FALLBACK_RETARGET = FORBIDDEN
```

## 5. Damage·Numeric 핵심

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
DEFENSE = clamp(base + buff - debuff,0,300)
ROUNDING = positive integer half-up
BARRIER = application20% / total30% / 90ticks
REDIRECTION = 30% / one recipient / invalid returns original
HEALTH_FLOOR = 1HP / one trigger / target batch
STATUS = stack3 / pulse30 / control60 / lockout30 ticks
```

## 6. Pause·Save·Render

```text
ACTIVE_COMBAT = TICK_ADVANCES
MAINTENANCE_PREPARATION_APPLICATION_PAUSE = TICK_PAUSED
SAVE = AFTER_R130_ONLY
SAVE_TIMER = INTEGER_TICKS
RENDER_INTERPOLATION = VISUAL_ONLY
WALL_CLOCK_TIMER_ANIMATION_CALLBACK = NON_AUTHORITATIVE
TICK_SKIP_OR_MERGE = FORBIDDEN
```

Normal/Danger tactical pause 가용성은 별도 UX·콘텐츠 Decision이다.

## 7. 적대적 감사

```text
OMW-AUD-208~220 Harness
OMW-AUD-221 Sheet HEAD correction / resolved / non-counter
OMW-AUD-222~232 Common Combat
OMW-AUD-233~246 Damage Semantics
OMW-AUD-247~260 Numeric Defaults
OMW-AUD-261 CI compatibility restore / resolved / non-counter
OMW-AUD-262~275 Time/Activation
```

P4 주요 위험:

- wall clock·Timer callback 권위.
- ms floor 변환.
- expiry fencepost.
- spawn same-tick 선공 또는 숨은 무적.
- pause 중 일부 Timer 진행.
- float Save Timer.
- frame overload Tick 유실.
- interpolation writeback.

모두 정본에서 차단했으나 구현·T1/T2 검증은 아직 실행되지 않았다.

## 8. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = FIXED_TICK_TIME_ACTIVATION_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
GDSCRIPT_SCENE_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 작업

다음 사용자 Decision:

```text
OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
```

검토 범위:

- outgoing/incoming modifier 합산·곱연산.
- defense buff/debuff·vulnerability·immunity ordering.
- effect family stacking·refresh·exclusive.
- Barrier·redirection·Floor·Status precedence.
- 동일 Tick Effect batch.
- 영웅 예외가 공통 Resolver를 우회하지 않는 extension seam.

```text
NEXT_GRILL_ME = 6/10
NEXT_PREFLIGHT = AT_10_OF_10
```
