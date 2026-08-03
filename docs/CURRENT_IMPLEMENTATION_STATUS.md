# 오멘워드 현재 구현 상태

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 최신 영웅 정본: `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`
- 적대적 검토 계보: `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- 작업 모드: `TOTAL_PLANNING / PLANNING_ONLY_PROFILE`
- 최신 기획 상태: `MAIN_CANONICAL_NOT_IMPLEMENTED`
- 제품 코드 승인: `NOT_AUTHORIZED`
- 최신 버티컬 슬라이스 구현: `NOT_STARTED`
- 기존 구현: `LEGACY_C1_C2_C3_PROVEN`
- 최신 설계 자동 검증: `NOT_RUN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_NOT_ALLOWED`

이 문서는 최신 사용자 승인 설계, 현재 제품 구현, 기존 실행 증거를 분리한다. 문서·PR·Sheet에 정본이 존재하는 것만으로 구현·검증 완료를 주장하지 않는다.

---

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `MAIN_CANONICAL_NOT_IMPLEMENTED` | 사용자 승인 기획이 main과 연결 Sheet에 병합됐지만 제품 코드·데이터·Scene·Resource에는 구현되지 않음 |
| `LATEST_USER_DESIGN_INTEGRATED` | 최신 사용자 결정을 책임 원본·라우터·원장·Sheet에 반영 |
| `DESIGN_DOCUMENTS_UPDATED` | 기획·코어·pending·상태 문서를 동기화 |
| `LEGACY_IMPLEMENTED` | 과거 설계 기준 제품 코드가 존재 |
| `LEGACY_PROVEN` | 과거 요구 계약과 실행 증거가 존재 |
| `MIGRATION_REQUIRED` | 최신 설계와 충돌해 보존 seam 또는 교체가 필요 |
| `NOT_STARTED` | 최신 제품 구현을 시작하지 않음 |
| `NOT_RUN` | 해당 자동·사람 검증을 실행하지 않음 |
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

기술 기준선의 존재는 최신 버티컬 슬라이스 또는 영웅 시스템 구현을 의미하지 않는다.

---

## 3. 보존 가능한 legacy 실행 증거

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

판정:

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

판정:

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

판정:

```text
LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ LATEST_UX_MIGRATION_REQUIRED
+ HUMAN_QA_NOT_RUN
```

---

## 4. 최신 main 기획 정본

### 4.1 전체 시스템

2026-07-27 버티컬 슬라이스 계약은 다음을 main 기획 정본으로 정의한다.

- 세 물리 원형 릴과 `SpinSnapshot`.
- 금고·병영 `TokenSource`.
- 3전선·5구간 라인 구조와 30개 건설 노드.
- 금고·농장·타워·병영·지휘소.
- 20 Stage MapRun, 준비·전투·정산·정비시간.
- checkpoint 저장, 미션, 메타 해금, 벨루 UX.

이 계약은 아직 제품 구현되지 않았다.

### 4.2 영웅·전설 등급

PR #129와 post-merge 동기화 PR #130, 생명주기 정리 PR #131을 통해 다음 기획이 main 정본이 됐다.

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

초기 해금 영웅 5명:

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

공통 상태 구조:

```text
INITIAL_WARMUP
→ READY_WAITING_FOR_VALID_CONDITION
→ CAST_PRECHECK
→ CAST_COMMIT
→ RESOLUTION_OR_ACTIVE_EFFECT
→ COOLDOWN
→ READY
```

공개 Trigger·대상 Resolver와 A/B/C 대표 encounter 검증 방향까지 승인됐지만 exact schema·수치·시뮬레이션·런타임은 미실행이다.

---

## 5. 최신 버티컬 슬라이스 미구현 영역

### 5.1 룰렛·토큰

- 세 가변 원형 릴.
- 금고 GOLD TokenSource와 병영 UNIT TokenSource.
- 물리 노드 결속 슬롯과 `SOURCE_BOUND_X`.
- source lifecycle 멱등 거래.
- 영구 가로 이동과 세로 이동.
- immutable SpinSnapshot과 SpinSession.
- live source 변경과 기존 보상 불변 경계.

### 5.2 경제·결과 처리

- 금고 지속 수입과 금화 토큰.
- 보관·판매·식량.
- PendingReward.
- 금화 기대수익을 포함한 비용표.
- 다중 건물 수리 실시간 과금.
- 에스크로 기반 건설·업그레이드·취소·파괴 반환.

### 5.3 전장·점령

- 5구간 라인 구조.
- 전체 30개 건설 노드.
- 중앙 경합 지역 3개와 양측 중간 거점 6개.
- 고정시간 점령과 회복.
- 소유권·수입·건설 권리 원자 이전.
- 후방 거점 상실과 전진 병력 예외.

### 5.4 건물

- 금고, 농장, 타워, 병영, 지휘소.
- 금고·농장 선형 Tier.
- 타워 연사/포격 분기와 Tier 3 강화.
- 지휘소 돌격/수비 분기와 Tier 3 강화.
- 병영 T2 10병종과 T3 20전문화.
- 호환 이전과 병영 BLOCKED.
- HP 0 제거, 노드 EMPTY, 잔해·재건 없음.

### 5.5 전투·AI

- 방패병 기본 표적 우선도.
- 전문 프로필과 점수 보정.
- 20% 표적 전환 히스테리시스.
- 호위병 25% 직접·광역 HP 손실 분담.
- 철벽수호병 정지 단계와 추적 제한.
- 나머지 Tier 3 능력.
- 전체 10병종 공통 능력치·피해·방어 기준표.

### 5.6 영웅·전설

- `[영웅]·[전설]` 전역 단일 활성 슬롯 resolver.
- 표준 영웅·해금 영웅·표준 전설 토큰 배치 충돌 처리.
- 고유 2스킬 공통 상태 머신과 deterministic commit payload.
- 공개 Trigger·same-lane filter·priority·stable tie-break.
- warmup·cooldown·READY·Stage 경계 저장 상태.
- 불퇴의 성벽·천공 소거·생명의 서약·메테오·그림자 분신.
- A/B/C 대표 encounter simulation harness.
- 미래 해금 전설의 고유 3스킬은 `NOT_NOW`.

### 5.7 벨루·UX

- 자동 벨루 조언.
- 비모달 벨루 팁.
- RecommendationSnapshot과 stale 처리.
- 우선 큐, 최근 조언, 선택 음성.
- 건물 유형·오라·보호 범위·점령 상태 UI.
- 영웅 warmup·READY·조건대기·commit·active·cooldown 표시.

### 5.8 MapRun·저장·메타

- 20스테이지 MapRun.
- 일반·위험 시간 행렬.
- 준비·정산 versioned checkpoint.
- 저장 원자 교체와 migration.
- 미션·등급·메타 재화·영구 성장.
- 영웅 timer·commit·resolved 상태 직렬화.

---

## 6. 기존 승인 문서와 최신 정본 관계

기존 V2 문서는 설계 이력과 세부 근거로 보존한다. 다음 항목은 최신 계약에 의해 대체됐다.

- 3스테이지 최소 슬라이스.
- 첫 슬라이스 mid-run save 미지원.
- 라인당 중앙 접전지 하나만 사용하는 토폴로지.
- 작업자 임금·글로벌 수리 예산.
- 파괴 건물 재건.
- 병영만 TokenSource로 해석하는 구조.
- 스테이지당 전설 1회.
- 이름 지정 영웅만 전역 1명 제한.
- 해금 영웅 패시브/active 선택형과 강제 상쇄 sidegrade.

전체 시스템 구현은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`를 먼저 따르고, 영웅·전설 구현은 2026-08-02~03 승인 영웅 책임 원본을 추가로 따른다.

---

## 7. 현재 판정

```text
TECHNICAL_BASELINE_IMPLEMENTED
+ LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
+ LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
+ LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ LATEST_USER_DESIGN_MAIN_CANONICAL
+ HERO_TRIGGER_TARGET_POWER_PLAN_MAIN_CANONICAL
+ PRODUCT_CODE_NOT_CHANGED
+ VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
+ HERO_IMPLEMENTATION_NOT_STARTED
+ LATEST_AUTOMATED_CONTRACTS_NOT_RUN
+ SIMULATION_NOT_RUN
+ RUNTIME_NOT_RUN
+ HUMAN_QA_NOT_RUN
+ CORE_LOCK_NOT_ALLOWED
```

---

## 8. 다음 게이트

1. `CURRENT_IMPLEMENTATION_STATUS.md`와 `DECISIONS_PENDING.md`의 post-merge 정본 동기화를 완료한다.
2. deterministic simulation harness의 범위·입출력·재현성·대표 encounter 계약을 승인한다.
3. 전체 병종 공통 전투 schema와 피해·방어·위협도·위치 판정 기준을 고정한다.
4. 다섯 해금 영웅의 Trigger·warmup·cooldown·효과값 초안을 작성한다.
5. A/B/C 파워 허용 범위·표본 수·stop-ship 기준을 고정한다.
6. 100,000시드 룰렛·경제·판매·비축·수리 시뮬레이션 계약을 설계한다.
7. 20스테이지 checkpoint schema와 원자 저장 계약을 설계한다.
8. 첫 제품 구현 패키지의 목표, 포함·제외, 상태 소유, Red 테스트, 회귀, 롤백 계획을 작성한다.
9. 사용자의 별도 제품 구현 승인 뒤에만 Godot 코드·데이터·Scene·Resource를 변경한다.

문서 병합만으로 제품 구현을 시작하거나 완료 상태를 선언하지 않는다.

## Legacy C1 원격 검증 증거

- `C1_ROULETTE_CORE_REMOTE_PROVEN`
- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- C1 최종 검증 run: `29926598807`
- 이 증거는 legacy C1 보존 seam의 원격 검증이며 V2 구현 완료를 뜻하지 않는다.

## Legacy C2 원격 검증 증거

- `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`
- C2 최종 검증 run: `29938742864`
- 이 증거는 legacy C2 전투 목적 루프의 원격 검증이며 V2 전장 구현 완료를 뜻하지 않는다.
