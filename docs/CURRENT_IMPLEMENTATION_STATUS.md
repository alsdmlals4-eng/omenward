# 오멘워드 현재 구현 상태

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- Harness 정본: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 정본: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 피해 의미 정본: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- 수치 기본값 정본: `docs/design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`
- 작업 모드: `TOTAL_PLANNING / PLANNING_ONLY_PROFILE`
- 최신 기획 상태: `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED`
- 제품 코드 승인: `NOT_AUTHORIZED`
- Simulation tool 코드 승인: `NOT_AUTHORIZED`
- 최신 Vertical Slice 구현: `NOT_STARTED`
- 기존 구현: `LEGACY_C1_C2_C3_PROVEN`
- 최신 자동 계약: `LATEST_AUTOMATED_CONTRACTS_NOT_RUN`
- Simulation 실행: `NOT_RUN`
- Runtime 검증: `NOT_RUN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- Core Lock: `NOT_ALLOWED`

이 문서는 사용자 승인 기획·현재 제품 구현·기존 실행 증거를 분리한다. 문서·PR·Sheet에 정본이 존재해도 제품·도구 구현 또는 검증 완료를 의미하지 않는다.

---

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED` | 사용자 승인 기획이 계획 브랜치에 기록됐으나 main 병합·제품 구현되지 않음 |
| `HARNESS_SCOPE_APPROVED_NOT_IMPLEMENTED` | Harness 목적·입출력·검증 Tier만 승인 |
| `COMMON_COMBAT_SCHEMA_APPROVED_NOT_IMPLEMENTED` | 전투 상태·phase·동일 tick 계약만 승인 |
| `DAMAGE_SEMANTICS_APPROVED_NOT_IMPLEMENTED` | 피해·보호·상태 의미만 승인 |
| `NUMERIC_DEFAULTS_APPROVED_NOT_IMPLEMENTED` | 공식·cap·duration·초기 수치만 승인 |
| `LEGACY_IMPLEMENTED` | 과거 설계 기준 제품 코드가 존재 |
| `LEGACY_PROVEN` | 과거 요구 계약과 실행 증거가 존재 |
| `MIGRATION_REQUIRED` | 최신 설계와 충돌해 보존 seam 또는 교체 필요 |
| `NOT_STARTED` | 최신 제품·도구 구현 시작 전 |
| `NOT_RUN` | 자동·simulation·runtime·사람 검증 미실행 |
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
- 공용 UnitArchetypeProfile과 진영 Visual 데이터 분리.
- 최신 계약과 양립하는 기존 상태·서비스·테스트 자산.

기술 기준선은 최신 Vertical Slice·영웅·Harness·전투 공식 구현 증거가 아니다.

---

## 3. 보존 가능한 Legacy 증거

### Legacy C1 — 룰렛

보존 후보:

- 중앙 가로줄 선행 판정.
- 완성선·등급 계산.
- 금화 resolver.
- 출처 결정론 개념.

Migration 필요:

- 독립 9칸 생성.
- 구형 TokenSource 장부.
- 구형 럭키·이동 거래.
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

Migration 필요:

- capture_power 합산.
- 구형 중간거점·라인 수명주기.
- 구형 주기적 출격.
- SceneTree·node iteration 의존.
- 동일 tick actor 순차 선공 편향.
- 신규 Damage/Protection 공식 부재.

```text
LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
+ LATEST_BATTLEFIELD_MIGRATION_REQUIRED
```

### Legacy C3 — UX·원인 보고

보존 후보:

- 도메인 snapshot→HUD 경계.
- 전투 원인 보고.
- 표시와 규칙 계산 분리.

Migration 필요:

- 독립 9칸 확률 미리보기.
- 구형 토큰 장부.
- channel·Barrier·raw/final damage 단계 표시 부재.

```text
LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ LATEST_UX_MIGRATION_REQUIRED
+ HUMAN_QA_NOT_RUN
```

---

## 4. 최신 승인 기획

### 4.1 전체 Vertical Slice

- 세 물리 원형 릴과 immutable SpinSnapshot.
- 금고·병영 TokenSource.
- 3전선·5구간·30개 건설 노드.
- 5개 건물.
- 20 Stage MapRun과 준비·전투·정산·정비.
- checkpoint·미션·메타·벨루 UX.

### 4.2 영웅·전설

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

공개 Trigger·same-lane Filter·Priority·stable tie-break·commit Snapshot과 A/B/C 검증 방향이 main 정본이다.

### 4.3 Deterministic Harness

```text
versioned fixture
+ fixed integer tick
+ named RNG streams
+ stable object IDs
+ ordered commands
+ pure domain transition
→ events / normalized state / metrics / fingerprints
```

T0~T3의 기획 계약만 승인됐다.

### 4.4 Core-First Common Combat

```text
CombatRunState
+ LaneState[TOP,MID,BOTTOM]
+ Combatant / Building / Objective
+ DeploymentProvenance
+ OrderedCommand / Intent / Protection / Status
+ R00~R130
```

동일 tick actor는 같은 post-movement snapshot에서 commit한다.

### 4.5 Damage·Protection·Status Semantics

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

- channel·delivery·target profile 분리.
- Barrier·Restore·Redirection·Floor·Status 의미 분리.
- true damage·execute·revive 금지.
- R80A~R80G·R90 death finalize.

### 4.6 Numeric Defaults

```text
effective_defense = clamp(base + buff - debuff, 0, 300)
post_mitigation = max(1, round_half_up(adjusted_damage * 100 / (100 + effective_defense)))
```

```text
Barrier = application 20% / total 30% max HP / 3000ms
Redirection = 30% / recipient 1 / invalid returns original
Health Floor = 1 HP / one trigger / exclusive
Status = stack 3 / pulse 1000ms / Control 2000ms / lockout 1000ms
```

밀리초→tick 변환은 아직 미확정이다.

---

## 5. 최신 미구현 영역

### 룰렛·경제·건물·전장

- 세 원형 릴과 source lifecycle.
- PendingReward·보관·판매·식량.
- 금고·수리·에스크로 프로젝트.
- 3전선 5구간·점령·소유권 원자 이전.
- 5개 건물 Tier·분기·병영 전문화.
- DeploymentProvenance 생성·event 연결.

### 공통 전투·AI

- 공통 상태 DTO/Resource.
- quantized 2D 위치·anchor·collision.
- ordered command·phase snapshot·barrier resolver.
- Damage/Protection/Status Intent와 R80A~G.
- 정수 방어 공식·Barrier cap·Redirection·Floor·Status default.
- fixed tick·ms 변환·activation policy.
- modifier stacking·threat·target score.
- R120 event·fingerprint.

### 영웅·Harness

- 전역 단일 영웅·전설 resolver.
- 고유 2스킬 Trigger·commit payload.
- warmup·cooldown·READY·Stage 직렬화.
- 영웅 exact 값.
- Harness fixture/domain/event/fingerprint 구현.
- T0~T3 실행 도구.
- A/B/C sample·tolerance·stop-ship.
- 제품 Scene adapter.

### 저장·UX·메타

- 20 Stage checkpoint schema·migration.
- timer·RNG·commit·Protection·Status 저장.
- save round-trip fixture.
- channel·Barrier·raw/final damage HUD.
- provenance 기반 결과 복기.
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
+ DAMAGE_SEMANTICS_USER_APPROVED
+ NUMERIC_DEFAULTS_USER_APPROVED
+ PRODUCT_CODE_NOT_CHANGED
+ SIMULATION_TOOL_CODE_NOT_AUTHORIZED
+ VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
+ LATEST_AUTOMATED_CONTRACTS_NOT_RUN
+ SIMULATION_NOT_RUN
+ RUNTIME_NOT_RUN
+ HUMAN_QA_NOT_RUN
+ CORE_LOCK_NOT_ALLOWED
```

---

## 7. 다음 Gate

1. `OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1`.
2. tick rate·ms 변환·spawn activation·pulse·expiry 경계를 고정한다.
3. source/target modifier stacking을 후속 결정한다.
4. 영웅 exact Trigger·timer·effect 값을 작성한다.
5. A/B/C sample·tolerance·stop-ship을 결정한다.
6. 별도 제품·도구 구현 승인 뒤에만 GDScript·Scene·Resource·test를 변경한다.

```text
GRILL_ME_COUNT = 4/10
NEXT_PREFLIGHT = AT_10_OF_10
```
