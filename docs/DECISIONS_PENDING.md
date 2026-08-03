# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- Harness 정본: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 정본: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 피해 의미 정본: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- 수치 기본값 정본: `docs/design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`
- 시간·활성화 정본: `docs/design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md`
- Modifier·precedence 정본: `docs/design/APPROVED_OMENWARD_MODIFIER_STACKING_AND_EFFECT_PRECEDENCE_2026-08-03.md`
- 현재 Grill Me: `6/10`
- 제품·Simulation tool 구현: `NOT_AUTHORIZED`

## 1. 이번 Decision으로 해결된 항목

`OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1`

해결:

- source outgoing family 합산·cap.
- target incoming family 합산·cap.
- combined pre-defense 25~200% cap.
- 유효 양수 damage의 pre-defense 최소 1.
- Armor/Resistance integer point additive.
- R60 source snapshot과 R80 target snapshot.
- projectile·DOT/HOT·environment source snapshot.
- duplicate key와 다섯 Stacking 정책.
- immunity→defense→Barrier→redirection→Floor→HP→Status→death precedence.
- valid impact·Barrier hit·final HP loss·Status·death trigger 분리.
- transferred damage second pass 금지.
- generic flat damage·override·penetration·next-hit 소비형 Modifier 금지.

## 2. 다음 최우선 사용자 Decision

`OMW-DEC-20260803-VALIDATION-SPATIAL-QUANTIZATION-MOVEMENT-AND-TARGETING-DEFAULTS-V1`

결정 필요:

- quantized 2D 좌표 단위와 integer scale.
- 이동속도·사거리의 tick당 정수 변환.
- lane anchor·segment·frontline 좌표 관계.
- same-lane 기본 targeting과 cross-lane 허용 범위.
- ground/flying movement layer와 collision class.
- range 경계 포함 여부와 distance metric.
- movement collision·swap·blocking batch 규칙.
- target filter·priority·stable tie-break exact order.
- projectile travel과 impact point quantization.
- 건물·Objective targetability와 후열 침투 규칙.

설계 충돌이므로 Grill Me 7/10 승인 대상으로 유지한다.

## 3. 후속 검증 Decision

### 콘텐츠 Parameter Set

- 표준 병종·적·건물 HP·공격·Armor·Resistance.
- 이동속도·사거리·공격속도·cooldown.
- 다섯 영웅 Trigger·Timer·Effect 실제 값.
- 전설 power budget과 동일 전장 1명 제한 검증.
- Stage·Wave·Danger·Boss Fixture 값.

### Harness Fixture·Sample·Tolerance

- T0 Fixture schema와 invalid data matrix.
- T1 replay seed·반복 횟수.
- T2 invariant fixture 목록.
- T3 paired A/B/C sample size와 허용오차.
- Barrier·Control stop-ship guard 통계 처리.
- other-two-lane contribution과 causal attribution 합격선.

### Runtime Adapter

- pure domain state와 Godot node adapter 경계.
- render interpolation snapshot.
- catch-up step 상한과 slow-mode UX.
- Save/Load adapter와 version migration.
- headless command와 CI 실행 경로.

Runtime adapter는 T0~T3 구현 권한 뒤 별도 승인한다.

## 4. 제품·UX 미확정

- Normal 전투 tactical pause 허용 범위.
- Danger 전투 실시간 강제 범위.
- 세 전선·세 릴 동시 정보 UX 부하 기준.
- Damage/Barrier/Status/Modifier debug trail의 플레이어용 축약.
- PC 16:9 우선 HUD와 모바일 별도 타당성 Gate.
- 첫 10~15분 사람 검증 절차와 성공 기준.

## 5. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
GDSCRIPT_SCENE_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
GENERIC_FLAT_DAMAGE_MODIFIER = FORBIDDEN_CURRENT_SLICE
GENERIC_OVERRIDE_OPERATION = FORBIDDEN
CONSUMABLE_NEXT_HIT_MODIFIER = FORBIDDEN_CURRENT_SLICE
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
DEFENSE_PENETRATION = FORBIDDEN_UNTIL_SEPARATE_DECISION
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 6. Merge Cadence

```text
CURRENT_COUNT = 6/10
NEXT_PREFLIGHT = AT_10_OF_10
EARLY_PREFLIGHT = only high-risk conflict / session boundary / large canon impact
```
