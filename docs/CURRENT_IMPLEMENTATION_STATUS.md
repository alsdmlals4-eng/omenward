# 오멘워드 현재 구현 상태

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- Harness 정본: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 정본: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 피해 의미 정본: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- 수치 기본값 정본: `docs/design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`
- 시간·활성화 정본: `docs/design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md`
- 작업 모드: `TOTAL_PLANNING / PLANNING_ONLY_PROFILE`
- 최신 기획 상태: `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED`
- 제품 코드 승인: `NOT_AUTHORIZED`
- Simulation tool 승인: `NOT_AUTHORIZED`

## 1. 정확한 상태 표기

```text
최신 버티컬 슬라이스 구현: `NOT_STARTED`
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED_PLANNING = FIXED_TICK_TIME_ACTIVATION_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

문서 계약과 CI 통과는 최신 Vertical Slice·Harness·전투 시스템이 구현됐다는 뜻이 아니다.

## 2. Legacy 검증 증거

```text
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
```

- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- C1 최종 검증 run: `29926598807`

이 증거는 과거 Legacy C1 룰렛 계약의 원격 검증을 뜻한다. 최신 V2 전체 시스템, 20 Stage Vertical Slice, Harness, Common Combat, Damage, Numeric, Time 계약 구현을 증명하지 않으며 **V2 구현 완료를 뜻하지 않는다**.

## 3. 현행 승인 Planning Stack

```text
P0 Harness Scope
P1 Common Combat Schema and R00~R130
P2 Damage/Protection/Status Semantics
P3 Mitigation/Protection Numeric Defaults
P4 Fixed Tick/Time/Activation Defaults
```

### P4 승인 내용

```text
DOMAIN_TPS = 30
AUTHORING_TIME = integer milliseconds
RUNTIME_TIME_AUTHORITY = integer tick
DURATION_TICKS = ceil(duration_ms * 30 / 1000)
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
SPAWN_AT_T → ACTIVATE_AT_T_PLUS_1
```

```text
Barrier 3000ms = 90 ticks
DOT/HOT pulse 1000ms = 30 ticks
Control max 2000ms = 60 ticks
Control lockout 1000ms = 30 ticks
```

Tick T spawn은 상태·대상 후보에 존재하고 피해받을 수 있지만 T+1 전에는 이동·Target·Action·Skill·Protection·Objective 기여를 할 수 없다.

## 4. 구현 상태 행렬

| 영역 | 기획 상태 | 제품 구현 | 자동 검증 | 사람 검증 |
|---|---|---|---|---|
| 20 Stage 전체 시스템 Vertical Slice | 승인 정본 존재 | `NOT_STARTED` | `NOT_RUN_LATEST` | `NOT_RUN` |
| Deterministic Harness | 범위 승인 | `NOT_STARTED` | `NOT_RUN` | `N/A` |
| Common Combat Schema | 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| Damage·Protection·Status | 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| Mitigation·Protection Numeric | 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 30 TPS·Time·Activation | 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| Modifier stacking·precedence | 미확정 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |
| 콘텐츠 Parameter Set | 미확정 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |
| Runtime Adapter | 미승인 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |
| 이미지·Animation·HX | 후속 Gate | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |

## 5. 구현 시 필수 시간 계약

```text
R00 = exclusive expiry before commands
R10 = ingest current scheduled commands only
R20 = spawn at T, activate at T+1
R110 = integer Tick Timer advance
R130 = Save canonical boundary
```

```text
WALL_CLOCK = NON_AUTHORITATIVE
GODOT_TIMER = NON_AUTHORITATIVE_FOR_COMBAT
ANIMATION_CALLBACK = NON_AUTHORITATIVE
RENDER_INTERPOLATION = VISUAL_ONLY
TICK_SKIP_OR_MERGE = FORBIDDEN
```

## 6. 전투·수치 필수 계약

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
DEATH_FINALIZE_AFTER_DAMAGE_BATCH
OBJECTIVE_USES_POST_DEATH_ACTIVE_SURVIVORS
KINETIC → ARMOR
ARCANE → RESISTANCE
DEFENSE = clamp(base + buff - debuff,0,300)
BARRIER = application20% / total30% / 90ticks
REDIRECTION = 30% / one recipient
HEALTH_FLOOR = 1 HP / one trigger
STATUS = stack3 / pulse30 / control60 / lockout30 ticks
```

## 7. Pause·Save 경계

```text
ACTIVE_COMBAT = DOMAIN_TICK_ADVANCES
MAINTENANCE_PREPARATION_APPLICATION_PAUSE = DOMAIN_TICK_PAUSED
SAVE = AFTER_R130_ONLY
SAVE_TIMERS = INTEGER_TICKS
```

전술 pause의 허용 여부는 Normal/Danger UX·콘텐츠 정책이 소유하지만, pause가 허용되면 모든 전투 시간은 함께 멈춘다.

## 8. CI 호환 회귀 기록

`OMW-AUD-261`에서 중앙 문서 간소화로 Legacy C1·Vertical Slice 상태·Review·Pilot 라우팅 marker가 누락되어 CI가 실패했다. 다음 커밋에서 복구했고 non-counter 유지보수로 기록했다.

```text
CURRENT_IMPLEMENTATION_STATUS restore commit = 1cca3bdb4a278aa741e4112a5c16970472daa9bb
DOCUMENTATION_MAP restore commit = 601be3bb5a885b8ada966621b994973accf17577
```

## 9. 남은 구현 차단 요인

```text
SOURCE_TARGET_MODIFIER_STACKING = PENDING_USER_DECISION
EFFECT_PRECEDENCE = PENDING_USER_DECISION
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
FIXTURE_SAMPLE_TOLERANCE = PENDING
IMPLEMENTATION_PLAN = NOT_WRITTEN_FOR_CURRENT_STACK
PRODUCT_CODE_AUTHORITY = NONE
```

## 10. 다음 Gate

```text
GRILL_ME_COUNT = 5/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
