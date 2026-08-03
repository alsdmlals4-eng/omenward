# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
parent_time_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
work_mode: TOTAL_PLANNING
current_count: 6_OF_10
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
| 6 | `OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1` | outgoing/incoming 단일 집계·R60/R80 snapshot·5 stacking 정책·effect precedence | `design/APPROVED_OMENWARD_MODIFIER_STACKING_AND_EFFECT_PRECEDENCE_2026-08-03.md` | `USER_APPROVED / NOT_IMPLEMENTED` |

## 3. Decision 6 세부 정본

```text
SOURCE_OUTGOING = clamp(10000 + sum(delta),5000,15000)
TARGET_INCOMING = clamp(10000 + sum(delta),5000,15000)
COMBINED_PRE_DEFENSE = clamp(round_half_up(source * target / 10000),2500,20000)
```

```text
R60 = source outgoing snapshot
R80 = target incoming·defense·Barrier snapshot
```

```text
REFRESH_DURATION
REPLACE_IF_STRONGER
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

Armor·Resistance는 integer point additive만 허용하며 Generic flat damage·override·penetration·next-hit 소비형 Modifier는 현 Slice에서 금지한다.

## 4. Effect Precedence

```text
P00 validity
→ P10 immunity
→ P20 source snapshot
→ P30 target incoming
→ P40 Armor/Resistance
→ P50 Barrier
→ P60 redirection
→ P70 Health Floor
→ P80 HP delta / Restore
→ P90 Status / post-hit
→ P100 death pending
```

Transferred HP loss는 두 번째 Modifier·mitigation·Barrier pass를 거치지 않는다.

## 5. Trigger 불변식

```text
ON_VALID_IMPACT
ON_POST_MITIGATION_DAMAGE
ON_BARRIER_ABSORBED
ON_FINAL_HP_LOSS
ON_STATUS_APPLIED
ON_TARGET_DEATH_FINALIZED
```

모호한 `on hit` 단독 정의와 영웅 직접 HP 변경은 금지한다.

## 6. 기존 시간·수치 불변식

```text
DOMAIN_TPS = 30
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
SPAWN_AT_T → ACTIVATE_AT_T_PLUS_1
KINETIC → ARMOR
ARCANE → RESISTANCE
DEFENSE = clamp(base + buffs - debuffs,0,300)
BARRIER = application20% / total30% / 90ticks
REDIRECTION = 30% / one recipient
HEALTH_FLOOR = 1 HP / one trigger
STATUS = stack3 / pulse30 / control60 / lockout30 ticks
```

## 7. 적대적 감사 계보

| 범위 | 주제 |
|---|---|
| `OMW-AUD-208~220` | Harness 범위·결정론 |
| `OMW-AUD-221` | Sheet stale HEAD 교정 / RESOLVED / NON_COUNTER |
| `OMW-AUD-222~232` | 공통 전투 Schema·동일 Tick |
| `OMW-AUD-233~246` | 피해·보호·상태 의미 |
| `OMW-AUD-247~260` | 방어·보호 수치 기본값 |
| `OMW-AUD-261` | CI 호환 marker 복구 / RESOLVED / NON_COUNTER |
| `OMW-AUD-262~275` | 30 TPS·시간 변환·spawn/activation·pause/save/render |
| `OMW-AUD-276~289` | Modifier stacking·snapshot·precedence·trigger 의미 |

## 8. 벤치마크 경계

Decision 6은 Unreal Gameplay Ability System의 data-driven Attribute·Gameplay Effect·stacking 구조를 제작 참고로 사용했다.

```text
ADOPT = reusable data-driven modifier calculation boundaries
ADAPT = four current families and five explicit stacking policies
REJECT = arbitrary per-effect operation and unrestricted stacking combinations
```

## 9. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MODIFIER_STACKING_EFFECT_PRECEDENCE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
MODIFIER_RESOLVER_CODE = NOT_AUTHORIZED
GDSCRIPT_SCENE_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 Decision

```text
OMW-DEC-20260803-VALIDATION-SPATIAL-QUANTIZATION-MOVEMENT-AND-TARGETING-DEFAULTS-V1
```

이 Decision은 quantized 2D scale, 이동 단위, 사거리, same-lane/cross-lane target scope, collision·anchor·target tie-break의 exact 기본값을 소유한다.

```text
GRILL_ME_COUNT = 6/10
NEXT_PREFLIGHT = AT_10_OF_10
```
