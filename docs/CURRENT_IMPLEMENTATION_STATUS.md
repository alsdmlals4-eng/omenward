# 오멘워드 현재 구현 상태

- 갱신일: 2026-07-27
- 최신 설계 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 적대적 검토: `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- 작업 모드: `PLAN / PLANNING_ONLY_PROFILE`
- 제품 코드 승인: `NOT_AUTHORIZED`
- 최신 버티컬 슬라이스 구현: `NOT_STARTED`
- 기존 구현: `LEGACY_C1_C2_C3_PROVEN`
- 자동 검증: `LATEST_CONTRACTS_NOT_RUN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_NOT_ALLOWED`

이 문서는 최신 사용자 승인 설계, 현재 제품 구현, 기존 실행 증거를 분리한다. 문서나 PR이 존재하는 것만으로 구현·검증 완료를 주장하지 않는다.

---

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `LATEST_USER_DESIGN_INTEGRATED` | 2026-07-27까지의 사용자 결정을 최신 통합 설계 문서에 기록 |
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

기술 기준선의 존재는 최신 버티컬 슬라이스 구현을 의미하지 않는다.

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

## 4. 2026-07-27 문서 작업

문서 브랜치에서 수행한 작업:

- 최신 사용자 승인 계약 통합.
- 적대적 검토 기록.
- PROJECT_CORE 갱신.
- GDD 갱신.
- pending 목록 갱신.
- 구현 상태 문서 갱신.

수행하지 않은 작업:

- Godot Scene·Resource·GDScript 변경.
- 제품 테스트 작성 또는 실행.
- 경제 100,000시드 시뮬레이션.
- checkpoint 저장 구현.
- 사람 플레이.

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

### 5.6 벨루·UX

- 자동 벨루 조언.
- 비모달 벨루 팁.
- RecommendationSnapshot과 stale 처리.
- 우선 큐, 최근 조언, 선택 음성.
- 건물 유형·오라·보호 범위·점령 상태 UI.

### 5.7 MapRun·저장·메타

- 20스테이지 MapRun.
- 일반·위험 시간 행렬.
- 준비·정산 versioned checkpoint.
- 저장 원자 교체와 migration.
- 미션·등급·메타 재화·영구 성장.

---

## 6. 기존 승인 문서와 최신 정본 관계

기존 V2 문서는 설계 이력과 세부 근거로 보존한다. 다음 항목은 최신 계약에 의해 대체되었다.

- 3스테이지 최소 슬라이스.
- 첫 슬라이스 mid-run save 미지원.
- 라인당 중앙 접전지 하나만 사용하는 토폴로지.
- 작업자 임금·글로벌 수리 예산.
- 파괴 건물 재건.
- 병영만 TokenSource로 해석하는 구조.

최신 구현은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`를 먼저 따른다.

---

## 7. 현재 판정

```text
TECHNICAL_BASELINE_IMPLEMENTED
+ LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
+ LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
+ LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ LATEST_USER_DESIGN_INTEGRATED
+ ADVERSARIAL_REVIEW_RECORDED
+ PRODUCT_CODE_NOT_CHANGED
+ VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
+ LATEST_AUTOMATED_CONTRACTS_NOT_RUN
+ HUMAN_QA_NOT_RUN
+ CORE_LOCK_NOT_ALLOWED
```

---

## 8. 다음 게이트

1. 문서 브랜치 diff와 정본 참조를 재검증한다.
2. 미확정 수치·콘텐츠를 `DECISIONS_PENDING.md` 순서로 결정한다.
3. 100,000시드 룰렛·경제·판매·비축·수리 시뮬레이션 계약을 설계한다.
4. 20스테이지 checkpoint schema와 원자 저장 계약을 설계한다.
5. 첫 제품 구현 패키지의 목표, 포함·제외, 상태 소유, Red 테스트, 회귀, 롤백 계획을 작성한다.
6. 사용자의 별도 Plan Mode 승인 뒤에만 제품 구현을 시작한다.

문서 병합만으로 제품 구현을 시작하거나 완료 상태를 선언하지 않는다.
