# 오멘워드 현재 구현 상태

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 최신 영웅 정본: `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`
- Harness 상위 정본: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 정본: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 최신 검증 정본: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- 작업 모드: `TOTAL_PLANNING / PLANNING_ONLY_PROFILE`
- 최신 기획 상태: `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED`
- 제품 코드 승인: `NOT_AUTHORIZED`
- Simulation tool 코드 승인: `NOT_AUTHORIZED`
- 최신 버티컬 슬라이스 구현: `NOT_STARTED`
- 기존 구현: `LEGACY_C1_C2_C3_PROVEN`
- 최신 자동 계약: `LATEST_AUTOMATED_CONTRACTS_NOT_RUN`
- Simulation 실행: `NOT_RUN`
- Runtime 검증: `NOT_RUN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_NOT_ALLOWED`

이 문서는 최신 사용자 승인 설계, 현재 제품 구현, 기존 실행 증거를 분리한다. 문서·PR·Sheet에 정본이 존재하는 것만으로 제품·도구 구현 또는 검증 완료를 주장하지 않는다.

---

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `MAIN_CANONICAL_NOT_IMPLEMENTED` | 승인 기획이 main과 연결 Sheet에 병합됐지만 제품 코드·데이터·Scene·Resource에는 구현되지 않음 |
| `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED` | 새 기획이 사용자 승인되어 계획 브랜치에 기록됐지만 아직 main 병합·제품 구현되지 않음 |
| `HARNESS_SCOPE_APPROVED_NOT_IMPLEMENTED` | Harness 목적·입출력·재현성·검증 Tier만 승인됐으며 실행 도구는 작성되지 않음 |
| `COMMON_COMBAT_SCHEMA_APPROVED_NOT_IMPLEMENTED` | core-first 전투 상태·phase order·동일 tick 공정성 계약만 승인됐으며 코드·fixture·test는 없음 |
| `DAMAGE_PROTECTION_STATUS_SEMANTICS_APPROVED_NOT_IMPLEMENTED` | KINETIC/ARCANE·barrier·restore·status 의미만 승인됐으며 formula·수치·코드는 없음 |
| `LEGACY_IMPLEMENTED` | 과거 설계 기준 제품 코드가 존재 |
| `LEGACY_PROVEN` | 과거 요구 계약과 실행 증거가 존재 |
| `MIGRATION_REQUIRED` | 최신 설계와 충돌해 보존 seam 또는 교체가 필요 |
| `NOT_STARTED` | 최신 제품 또는 도구 구현을 시작하지 않음 |
| `NOT_RUN` | 해당 자동·simulation·runtime·사람 검증을 실행하지 않음 |
| `PROVEN` | 최신 요구 계약과 fresh 실행 증거가 함께 존재 |

---

## 2. 기술 기준선

유지 대상:

- Godot 4.7.1 Standard.
- Compatibility renderer.
- 960×540 논리 화면, 1920×1080 출력.
- GDScript.
- typed Resource와 명시적 도메인 상태 객체.
- 이름 기반 RNG stream과 재현 가능한 입력 로그.
- 공용 `UnitArchetypeProfile`과 진영 Visual 데이터 분리.
- 기존 상태·서비스·테스트 자산 중 최신 계약과 양립하는 부분.

기술 기준선의 존재는 최신 버티컬 슬라이스·영웅 시스템·Harness·공통 전투 Schema·Damage Semantics 구현을 의미하지 않는다.

---

## 3. 보존 가능한 Legacy 실행 증거

### Legacy C1 — 룰렛

보존 후보:

- 중앙 가로줄 선행 판정.
- 완성선 수와 등급 계산.
- 금화 75/200/500% resolver.
- 출처 결정론 개념.

교체 또는 migration 필요:

- 독립 9칸 생성.
- 구형 TokenSource 장부.
- 구형 럭키와 이동 거래.
- 스테이지당 전설 제한.
- 구형 보관 계약.

```text
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
+ LATEST_ROULETTE_MIGRATION_REQUIRED
```

### Legacy C2 — 전장

보존 후보:

- 3라인 전투 기반.
- 공용 병종 데이터.
- 구조물 피해.
- 전장 상태 기반 승패.

교체 또는 migration 필요:

- `capture_power` 합산.
- 중앙 접전지에 구형 중간거점 상태기 재사용.
- 구형 라인 수명주기.
- 아군 주기적 출격 묶음.
- SceneTree·node iteration 순서에 기대는 처리.
- 동일 tick actor를 순차 실행해 생기는 선공 편향.
- 단일 generic defense 또는 암묵 damage type.
- barrier·heal·status를 하나의 효과 처리로 섞는 구현.

```text
LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
+ LATEST_BATTLEFIELD_MIGRATION_REQUIRED
```

### Legacy C3 — UX·원인 보고

보존 후보:

- 도메인 snapshot→HUD 경계.
- 전투 원인 보고.
- 표시와 규칙 계산 분리.

교체 또는 migration 필요:

- 독립 9칸 확률 미리보기.
- T-30/T-15/T-5 의미.
- 구형 토큰 장부.
- raw damage와 final HP loss를 구분하지 않는 로그.
- channel을 색상만으로 구분하는 UI.

```text
LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ LATEST_UX_MIGRATION_REQUIRED
+ HUMAN_QA_NOT_RUN
```

---

## 4. 최신 승인 기획

### 4.1 전체 Vertical Slice

2026-07-27 정본은 다음을 정의하지만 아직 제품 구현되지 않았다.

- 세 물리 원형 릴과 immutable `SpinSnapshot`.
- 금고·병영 `TokenSource`.
- 3전선·5구간과 30개 건설 노드.
- 금고·농장·타워·병영·지휘소.
- 20 Stage MapRun과 준비·전투·정산·정비시간.
- checkpoint 저장, 미션, 메타 해금, 벨루 UX.

### 4.2 영웅·전설

```text
표준 [영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
표준 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 고유 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

공개 Trigger·same-lane Filter·Priority·stable tie-break·immutable commit Snapshot과 A/B/C encounter 검증 방향이 main 정본이다. Exact schema·수치·runtime은 미확정이다.

### 4.3 Deterministic Simulation Harness

현재 계획 브랜치에서 다음 범위가 승인됐다.

```text
versioned fixture
+ fixed integer tick
+ named RNG streams
+ stable object IDs
+ ordered external commands
+ pure domain state transition
→ ordered event log
→ normalized final state
→ metrics summary
→ state fingerprints
```

승인된 설계 범위:

```text
T0 fixture schema validation
T1 replay determinism
T2 rule invariants
T3 paired A/B/C metrics
```

미승인 범위:

```text
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
FULL_PRODUCT_SCENE_HARNESS = NOT_AUTHORIZED
T4_BALANCE_ACCEPTANCE = PENDING
T5_PRODUCT_RUNTIME_ADAPTER = PENDING
SIMULATION_EXECUTION = NOT_RUN
```

### 4.4 Core-First Common Combat Schema

```text
CombatRunState
+ LaneState[TOP,MID,BOTTOM]
+ CombatantState
+ BuildingState
+ ObjectiveState
+ DeploymentProvenance
+ OrderedCommand
+ ActionIntent / EffectIntent
+ ProtectionInstance / StatusInstance / PendingCommit / ActiveEffect
+ named RNG and canonical event state
```

룰렛 전체를 전투 Harness가 재실행하지는 않지만 모든 전장 유닛은 다음 provenance를 가진다.

```text
SpinSnapshot
→ PendingReward
→ TokenInstance / TokenSource
→ lane commit
→ deployment_id
→ combat events
```

고정 phase 순서:

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

동일 tick actor는 같은 post-movement snapshot에서 commit한다. sequential entity ID order로 같은 tick 행동이 삭제되는 처리를 금지한다.

### 4.5 Damage·Protection·Status Semantics

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
DELIVERY_TAGS = BASIC / SKILL / AREA / DAMAGE_OVER_TIME / ENVIRONMENT / TRANSFERRED
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING
```

R80 내부 의미:

```text
VALIDITY
→ PROTECTION SETUP
→ CHANNEL MITIGATION
→ BARRIER
→ HP-LOSS REDIRECTION
→ HEALTH FLOOR
→ HP DELTA / SEPARATE RESTORE
→ STATUS / POST-HIT
→ DEATH_PENDING
```

핵심 불변식:

```text
BARRIER != HP_OR_HEAL
RESTORE != NEGATIVE_DAMAGE
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS = FORBIDDEN
RETROACTIVE_STATUS_COMMIT_CANCELLATION = FORBIDDEN
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
```

정확 formula·Armor/Resistance 값·barrier cap·duration·status stack cap은 미확정이다.

---

## 5. 최신 미구현 영역

### 5.1 룰렛·경제·건물·전장

- 세 가변 원형 릴과 source lifecycle.
- 보관·판매·식량·PendingReward.
- 금고 지속 수입·다중 수리·에스크로 프로젝트.
- 3전선 5구간·점령·소유권 원자 이전.
- 5개 건물과 Tier·분기·병영 전문화.
- `DeploymentProvenance` 생성과 전투 event 연결.

### 5.2 공통 전투·피해·AI

- `CombatRunState`와 공통 상태 Resource/DTO.
- quantized 2D 위치·anchor·collision layer.
- ordered command·phase snapshot·intent·barrier resolver.
- 동일 tick action commit·damage batch·death finalize·objective order.
- `DamageIntent`, `RestoreIntent`, `ProtectionIntent`, `StatusApplicationIntent`.
- KINETIC/ARCANE과 Armor/Resistance resolver.
- mitigation formula·rounding·cap·최소 피해.
- barrier budget·duration·stack·consume order.
- HP-loss redirection·health-floor resolver.
- status family·stacking·expiry·dispel resolver.
- 방패 표적 우선도·전문화 점수·히스테리시스.
- threat·role·frontline·backline·cluster 의미.
- event ordering·R120 fingerprint.

### 5.3 영웅·Harness

- `[영웅]·[전설]` 전역 단일 활성 resolver.
- 고유 2스킬 상태 머신·Trigger·commit payload.
- warmup·cooldown·READY·Stage 경계 직렬화.
- 다섯 고유 2스킬 exact 값.
- Harness fixture/domain/event/fingerprint schema implementation.
- T0~T3 실행 도구와 fixture.
- A/B/C 표본 수·허용오차·stop-ship 기준.
- 실제 제품 Scene adapter.

### 5.4 저장·UX·메타

- 20 Stage checkpoint schema와 migration.
- timer·RNG·commit·resolved·protection·status 상태 직렬화.
- Harness save round-trip fixture.
- 영웅 상태 표시와 전투 원인 로그.
- KINETIC/ARCANE·Armor/Resistance·Barrier 접근성 UI.
- 배치 provenance 기반 결과 복기 UI.
- 미션·메타 성장·벨루.

---

## 6. 현재 판정

```text
TECHNICAL_BASELINE_IMPLEMENTED
+ LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
+ LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
+ LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ LATEST_USER_DESIGN_MAIN_CANONICAL
+ DETERMINISTIC_HARNESS_SCOPE_USER_APPROVED
+ COMMON_COMBAT_SCHEMA_USER_APPROVED
+ DAMAGE_PROTECTION_STATUS_SEMANTICS_USER_APPROVED
+ PRODUCT_CODE_NOT_CHANGED
+ SIMULATION_TOOL_CODE_NOT_AUTHORIZED
+ VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
+ HERO_IMPLEMENTATION_NOT_STARTED
+ LATEST_AUTOMATED_CONTRACTS_NOT_RUN
+ SIMULATION_NOT_RUN
+ RUNTIME_NOT_RUN
+ HUMAN_QA_NOT_RUN
+ CORE_LOCK_NOT_ALLOWED
```

---

## 7. 다음 Gate

1. `OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1`을 결정한다.
2. Armor·Resistance curve·rounding·modifier group·최소 피해를 고정한다.
3. barrier cap·duration·consume·uptime stop-ship을 고정한다.
4. HP-loss redirection·health-floor·status stack numeric defaults를 고정한다.
5. 이후 fixed tick·activation·quantization 기술 기본값을 고정한다.
6. 다섯 영웅 exact Trigger·timer·효과값을 작성한다.
7. A/B/C 표본 수·허용오차·stop-ship을 결정한다.
8. 별도 제품·도구 구현 승인 뒤에만 GDScript·Scene·Resource·test를 변경한다.

문서 병합만으로 제품 또는 Harness 구현을 시작하거나 완료 상태를 선언하지 않는다.

## Legacy 원격 검증 증거

- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`.
- C1 최종 검증 run: `29926598807`.
- C2 최종 검증 run: `29938742864`.
- 이 증거는 legacy 보존 seam의 원격 검증이며 V2 구현 완료를 뜻하지 않는다.
