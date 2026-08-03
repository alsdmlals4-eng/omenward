# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- Harness 정본: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 정본: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 피해 의미 정본: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- 수치 기본값 정본: `docs/design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`
- 시간·활성화 정본: `docs/design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md`
- 현재 Grill Me: `5/10`
- 제품·Simulation tool 구현: `NOT_AUTHORIZED`

## 1. 이번 Decision으로 해결된 항목

`OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1`

```text
DOMAIN_TPS = 30
AUTHORING_TIME = integer ms
RUNTIME_TIME = integer tick
DURATION_TICKS = ceil(ms * 30 / 1000)
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
SPAWN_AT_T → ACTIVATE_AT_T_PLUS_1
```

```text
3000ms = 90 ticks
1000ms = 30 ticks
2000ms = 60 ticks
1000ms = 30 ticks
```

해결:

- fixed Tick rate.
- ms→Tick 변환과 rounding.
- R00 expiry fencepost.
- DOT/HOT 첫 due Tick과 exclusive end.
- Control 종료·lockout 구간.
- R10 scheduled command 경계.
- R20 spawn과 다음 Tick activation.
- spawn same-tick targetability와 action 금지.
- pause·maintenance·preparation의 domain clock 동결.
- R130 Save boundary와 integer Timer 저장.
- render interpolation·Godot Timer·animation callback 비권위.
- overload에서 Tick skip·merge 금지.

## 2. 다음 최우선 사용자 Decision

`OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1`

결정 필요:

- source outgoing modifier 합산·곱연산 경계.
- target incoming modifier와 vulnerability 순서.
- Armor/Resistance additive buff·debuff ordering.
- 동일 family buff/debuff stack·refresh·exclusive 규칙.
- immunity·barrier·redirection·Health Floor·Status precedence.
- 동일 Tick에 여러 Effect가 들어올 때 batch와 canonical key.
- 영웅·전설 effect가 공통 Resolver를 우회하지 않는 extension seam.
- modifier cap·minimum·overflow 방어.

설계 충돌이므로 exact 기본값만으로 자동 확정하지 않고 Grill Me 6/10 승인을 받는다.

## 3. 후속 검증 Decision

### 콘텐츠 Parameter Set

- 표준 병종·적·건물의 HP·공격·Armor·Resistance.
- 이동속도·사거리·공격속도·cooldown.
- 다섯 영웅 Trigger·Timer·Effect 실제 값.
- 전설 power budget과 동일 전장 1명 제한 검증.
- Stage·Wave·Danger·Boss Fixture 값.

### Harness Fixture·Sample·Tolerance

- T0 Fixture schema와 invalid data matrix.
- T1 replay seed·반복 횟수.
- T2 invariant fixture 목록.
- T3 paired A/B/C sample size와 허용오차.
- Barrier·Control stop-ship guard의 통계 처리.
- other-two-lane contribution과 causal attribution 합격선.

### Runtime Adapter

- pure domain state와 Godot node adapter 경계.
- render interpolation snapshot.
- catch-up step 상한과 slow-mode UX.
- Save/Load adapter와 version migration.
- headless command와 CI 실행 경로.

Runtime adapter는 T0~T3 구현 권한 뒤 별도 승인한다.

## 4. 제품·UX 미확정

- Normal 전투의 tactical pause 허용 범위.
- Danger 전투의 실시간 강제 범위.
- 세 전선·세 릴 동시 정보의 UX 부하 기준.
- Damage/Barrier/Status debug trail의 플레이어용 축약.
- PC 16:9 우선 HUD와 모바일 별도 타당성 Gate.
- 첫 10~15분 사람 검증 절차와 성공 기준.

## 5. 이미지·Animation·HX Gate

기획 Decision batch가 완료되고 검토를 통과하기 전에는 제작하지 않는다.

순서:

```text
planning complete
→ adversarial review
→ image/animation/HX planning and approval
→ Codex implementation contract
```

## 6. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
GDSCRIPT_SCENE_RESOURCE_FIXTURE_TEST = NOT_AUTHORIZED
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
DEFENSE_PENETRATION = FORBIDDEN_UNTIL_SEPARATE_DECISION
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. Merge Cadence

```text
CURRENT_COUNT = 5/10
NEXT_PREFLIGHT = AT_10_OF_10
EARLY_PREFLIGHT = only high-risk conflict / session boundary / large canon impact
```
