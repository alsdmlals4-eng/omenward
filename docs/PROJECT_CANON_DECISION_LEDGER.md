# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
work_mode: TOTAL_PLANNING
current_count: 5_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
```

## 1. 운영 원칙

- GitHub APPROVED 문서가 기획 정본이다.
- Google Sheet는 사용자 가시 GDD·계획 데이터이며 같은 Decision ID로 동기화한다.
- exact 수치는 권장 기본안을 사용할 수 있으나 설계 충돌은 Grill Me 승인 대상이다.
- 승인 Decision 최대 10개마다 PR preflight·적대적 검토·병합을 수행한다.
- 제품 코드·Simulation tool·이미지·animation·HX는 별도 권한 전까지 금지한다.
- 벤치마크는 ADOPT·ADAPT·REJECT 경계를 기록하며 외부 수치를 무비판적으로 복사하지 않는다.

## 2. 현재 승인 결정

| 순번 | Decision ID | 요약 | 책임 원본 | 상태 |
|---:|---|---|---|---|
| 1 | `OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1` | Godot headless 순수 도메인·고정 Tick·명명 RNG·ordered Event Harness 범위 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | `USER_APPROVED / NOT_IMPLEMENTED` |
| 2 | `OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1` | 세 전선·배치 provenance·R00~R130·동일 Tick phase barrier | `design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md` | `USER_APPROVED / NOT_IMPLEMENTED` |
| 3 | `OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1` | KINETIC/ARCANE·Armor/Resistance·Barrier/Restore/Status 의미 | `design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md` | `USER_APPROVED / NOT_IMPLEMENTED` |
| 4 | `OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1` | 쌍곡선 방어·Barrier 20/30%·이전30%·Floor1·Status ms 기본값 | `design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md` | `USER_APPROVED / NOT_IMPLEMENTED` |
| 5 | `OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1` | 30 TPS·integer tick·exclusive expiry·T+1 activation·render 비권위 | `design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md` | `USER_APPROVED / NOT_IMPLEMENTED` |

## 3. Decision 5 세부 정본

```text
DOMAIN_TICKS_PER_SECOND = 30
AUTHORING_TIME_UNIT = INTEGER_MILLISECONDS
RUNTIME_TIME_AUTHORITY = INTEGER_DOMAIN_TICK
DURATION_TICKS = CEIL(duration_ms * 30 / 1000)
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
```

```text
3000ms Barrier = 90 ticks
1000ms pulse = 30 ticks
2000ms Control max = 60 ticks
1000ms Control lockout = 30 ticks
```

```text
scheduled command at T
→ R10 ingest
→ R20 spawn
→ activation_tick = T + 1
```

Tick T spawn은 상태·대상 후보에 존재하고 피해받을 수 있으나, 이동·Target·Action·Skill·Protection·Objective 기여는 T+1부터 가능하다.

## 4. Time·Pause·Save 불변식

```text
R00_EXCLUSIVE_EXPIRY_BEFORE_R10
PAST_COMMAND = REJECT_WITH_REASON
FUTURE_COMMAND = KEEP_QUEUED
ACTIVE_COMBAT = TICK_ADVANCES
MAINTENANCE_PREPARATION_APPLICATION_PAUSE = TICK_PAUSED
SAVE_BOUNDARY = AFTER_R130_ONLY
SAVE_TIMER = INTEGER_TICK
RENDER_INTERPOLATION = VISUAL_ONLY
GODOT_TIMER_ANIMATION_WALL_CLOCK = NON_AUTHORITATIVE
TICK_SKIP_OR_MERGE = FORBIDDEN
```

## 5. 전투·수치 불변식

```text
KINETIC → ARMOR
ARCANE → RESISTANCE
DEFENSE = clamp(base + buffs - debuffs,0,300)
ROUNDING = POSITIVE_INTEGER_HALF_UP
BARRIER = application 20% / total 30% / 90 ticks
REDIRECTION = 30% / one recipient / return invalid share
HEALTH_FLOOR = 1 HP / one trigger / target batch
STATUS = stack 3 / pulse 30 / control 60 / lockout 30 ticks
```

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
HIDDEN_FALLBACK_RETARGET = FORBIDDEN
DEATH_FINALIZE_AFTER_DAMAGE_BATCH
OBJECTIVE_USES_POST_DEATH_ACTIVE_SURVIVORS
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS = FORBIDDEN
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
```

## 6. 적대적 감사 계보

| 범위 | 주제 |
|---|---|
| `OMW-AUD-208~220` | Harness 범위·결정론 |
| `OMW-AUD-221` | Sheet stale HEAD 교정 / RESOLVED / NON_COUNTER |
| `OMW-AUD-222~232` | 공통 전투 Schema·동일 Tick |
| `OMW-AUD-233~246` | 피해·보호·상태 의미 |
| `OMW-AUD-247~260` | 방어·보호 수치 기본값 |
| `OMW-AUD-261` | CI 호환 marker 복구 / RESOLVED / NON_COUNTER |
| `OMW-AUD-262~275` | 30 TPS·시간 변환·spawn/activation·pause/save/render |

## 7. 벤치마크 경계

Decision 5는 Godot의 physics interpolation과 Timer 문서를 제작 참고로 사용했다.

```text
ADOPT = render/domain separation and interpolation concept
ADAPT = 30 TPS strategy autobattle domain
REJECT = callback/Timer/wall clock as combat authority
```

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

## 9. 다음 Decision

```text
OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
```

이 Decision은 outgoing/incoming modifier, buff/debuff, vulnerability, immunity, barrier·status 적용 순서와 영웅 예외가 공통 Resolver를 우회하지 않는 precedence를 소유한다.

```text
GRILL_ME_COUNT = 5/10
NEXT_PREFLIGHT = AT_10_OF_10
```
