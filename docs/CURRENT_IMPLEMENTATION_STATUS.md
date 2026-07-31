# 오멘워드 현재 구현 상태

- 갱신일: `2026-08-01`
- 상태: `CURRENT_IMPLEMENTATION_AUTHORITY / LEGACY_PROTOTYPE`
- 최신 제품 설계: `USER_APPROVED / NOT_IMPLEMENTED`
- 작업 모드: `PLAN / PLANNING_ONLY_PROFILE`
- 제품 코드 승인: `NOT_AUTHORIZED`
- 자동 검증: `LATEST_CONTRACTS_NOT_RUN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 이미지 상태: `PREVIOUS_GENERATIONS_REJECTED / NO_APPROVED_PRODUCT_ASSET`
- 잠금: `CORE_LOCK_NOT_ALLOWED`

이 문서는 실제 Scene·Script·Resource·data·tests에 존재하는 구현만 소유한다. 승인 문서나 생성 이미지는 구현 증거가 아니다.

---

## 1. 기술 기준선

- Godot `4.7` feature set.
- GDScript.
- Compatibility renderer.
- 논리 화면 `960×540`, 출력 override `1920×1080`.
- 실행 Scene: `res://scenes/main/main.tscn`.
- Main 구성: `GameSession`, `Battlefield`, `StageHud`, `StageSelect`.
- 별도 제품 메인 메뉴 없음.

---

## 2. 실제 구현 파일 지도

| 영역 | 실제 파일 | 현재 구현 |
|---|---|---|
| 세션 | `scripts/core/game_session.gd` | tutorial/regular Stage 시작, 무료 동일 Stage 재시작 |
| Stage | `scripts/core/stage_run.gd` | Legacy economy/building/roulette/deployment/wave/battle 연결 |
| 전장 시뮬레이션 | `scripts/battle/battle_simulator.gd` | 하나의 시뮬레이션, 상·중·하 3라인, 양측 outpost·중앙 clash·gate·base |
| 전장 화면 | `scripts/battle/battlefield_view.gd` | 코드 드로잉 graybox, 라인·거점·노드 원 표시 |
| 유닛 화면 | `scripts/units/unit_view.gd` | 원·마름모·선 형태 기술 표현 |
| 건물 | `scripts/buildings/building_service.gd` | barracks/tower/farm 3종, outpost당 임의 node ID 등록 |
| 룰렛 | `scripts/roulette/roulette_service.gd` | 독립 9칸 가중 심벌 생성과 중앙줄/완성선 resolver |
| HUD | `scenes/ui/stage_hud.tscn`, `scripts/ui/stage_hud.gd` | Label 중심 기술 HUD, Spin/3건물/3라인 배치/free Retry 버튼 |
| Legacy tests | `tests/headless/economy_roulette_test.gd`, `tests/headless/c2_battle_objective_test.gd` | 구형 9칸·capture_power·3노드 outpost·구형 건물 lifecycle 검증 |

---

## 3. 전장·노드 구현 경계

### 실제 구현

- 상·중·하 세 라인.
- 각 라인에 아군 outpost, 중앙 clash, 적 outpost 상태.
- BattlefieldView는 각 양측 outpost에 원 3개를 그린다.
- StageRun은 모든 `team × lane` outpost에 `front_a / front_b / rear` 세 node ID를 등록한다.

### 최신 정본과의 차이

```text
최신 정본
- 건설 노드 종류 1개
- 본진 6노드/진영
- 중간 거점 3라인×2진영=6곳
- 중간 거점 3노드/거점
- 중앙 접전지 0노드
- 전체 30노드

현재 구현
- 본진 건설 노드 모델 없음
- 중간 거점 6곳에 각 3개의 Legacy node ID만 등록
- construct_home()가 실제 본진 대신 lumern_middle outpost를 사용
- 전체 30노드 데이터 계약·검증 없음
```

판정:

```text
LEGACY_MIDPOINT_NODE_SEAM_PRESENT
LATEST_30_NODE_TOPOLOGY_NOT_IMPLEMENTED
MIGRATION_REQUIRED
```

---

## 4. 룰렛 구현 경계

### 보존 후보

- 중앙 가로줄 선행 판정.
- 동일 심벌 완성선 수 계산.
- 일반/엘리트/영웅/전설 등급 resolver.
- 금화 75/200/500% resolver.
- deterministic seed 개념.

### 최신 정본과의 차이

현재 `RouletteService`는 9개 셀을 각각 가중 추첨한다. 다음 최신 계약은 구현되지 않았다.

- 왼쪽·중앙·오른쪽 세 원형 TokenInstance 배열.
- 각 릴 cursor와 연속 3칸 노출.
- TokenSource 건물 1동이 세 릴에 같은 출처 토큰을 하나씩 공급.
- X 안정 index 교체와 append.
- 세로 이동.
- live 배열을 영구 변경하는 가로 이동.
- immutable SpinSnapshot과 SpinSession.
- PendingReward와 명시적 확정 거래.
- 럭키 15/25/35/45/55/100%.

판정:

```text
LEGACY_NINE_CELL_RESOLVER_PROVEN
LATEST_PHYSICAL_REELS_NOT_IMPLEMENTED
MIGRATION_REQUIRED
```

---

## 5. 건물·경제 구현 경계

### 실제 구현

- barracks, tower, farm.
- 즉시 건설과 즉시 골드 차감.
- farm food cap 효과.
- barracks가 Legacy roulette source entry 하나 제공.
- outpost capture revision 변경 시 기존 건물을 RUINED 처리.

### 최신 정본과의 차이

- 금고와 지휘소 없음.
- 5건물 Tier·분기·전문화 없음.
- 본진 6노드 없음.
- 최신 호환 이전/BLOCKED/source-bound X 계약 없음.
- 건설·업그레이드·철거·수리 시간·에스크로·정산 없음.
- 금고 TokenSource와 실제 세 릴 결속 없음.

---

## 6. 전투·점령 구현 경계

### 보존 후보

- 3라인 격리.
- 공용 archetype 데이터.
- 구조물 피해와 gate/base 승패.
- 전투 이벤트와 원인 보고 seam.

### 최신 정본과의 차이

- 현재 점령은 archetype별 `capture_power` 합산을 사용한다.
- 최신 계약의 유닛 수·Tier·등급과 무관한 고정시간 점령·유예·회복은 구현되지 않았다.
- Legacy 테스트도 capture_power와 즉시 lifecycle을 검증한다.
- 전체 20 Stage와 위험 패키지·보스 패키지는 구현되지 않았다.

---

## 7. 저장·패배·재시도 구현 경계

### 실제 구현

- `GameSession.retry_stage()`는 현재 Stage를 새로 시작한다.
- HUD의 RetryButton은 승리·패배 모두에서 표시될 수 있다.
- 영구재화·횟수·checkpoint·원자 transaction이 없다.

### 최신 정본과의 차이

- 본진 HP 0 기본 MapRun 종료.
- Stage 5 이후 MapRun당 최대 1회 영구재화 재시도.
- 실패 Stage 준비 checkpoint 복원.
- 동일 공세·보스·룰렛·미션 RNG 계보 유지.
- 제품 유료 Retry와 개발 무료 Retry의 보상·업적·기록 분리.

판정:

```text
LEGACY_FREE_STAGE_RESTART_ONLY
LATEST_PAID_RETRY_NOT_IMPLEMENTED
```

---

## 8. UI·비주얼 구현 경계

### 실제 구현

- 별도 메인 메뉴 없음.
- StageHud는 텍스트 Label과 개발 버튼 중심.
- 룰렛 결과는 쉼표로 연결된 9개 심벌 문자열로 표시.
- 전장과 유닛은 code-drawn graybox.

### 최신 제품 상태

- 과거 화면 명세 보드 V1은 사용자 검토에서 `REJECTED_EVIDENCE`가 됐다.
- 후속 생성 이미지도 룰렛·전장·노드·비주얼 불일치로 폐기됐다.
- 사용자 제공 최신 비주얼 자료는 `docs/images/VISUAL_REFERENCE_INDEX.md`에 등록됐지만 바이너리 이동은 `MIGRATION_PENDING`이다.
- 승인된 제품 UI·최종 전장·최종 캐릭터·제품 에셋은 없다.

---

## 9. 자동 검증 상태

### Legacy 증거

- C1 룰렛 resolver 관련 원격 증거 존재.
- C2 전투 목적 루프 관련 원격 증거 존재.
- 현재 repository의 headless tests는 Legacy 계약을 검증한다.

### 최신 계약 미검증

다음 자동 계약은 아직 없다.

- 건설 노드 종류 1개.
- 본진 6노드/진영.
- 중간 거점 6곳·3노드/거점.
- 중앙 접전지 0노드.
- 전체 건설 노드 30개.
- 세 물리 릴과 TokenInstance 영속 가로 이동.
- 고정시간 점령.
- 5건물 구조.
- versioned checkpoint.
- 영구재화 유료 Retry 원자 거래.
- 20 Stage·위험·보스 패키지.

이번 문서 검토에서는 Godot import, headless tests, Runtime과 사람 플레이를 실행하지 않았다.

---

## 10. 현재 판정

```text
TECHNICAL_BASELINE: IMPLEMENTED
CURRENT_PRODUCT: LEGACY_PROTOTYPE
LATEST_VERTICAL_SLICE: NOT_IMPLEMENTED
LATEST_CONTRACT_TESTS: NOT_RUN
HUMAN_QA: NOT_RUN
VISUAL_SCREEN_BOARD_V1: REJECTED
GENERATED_IMAGES: REJECTED_EVIDENCE
PRODUCT_ASSET_APPROVAL: NO
PRODUCT_CODE_AUTHORIZATION: NO
CODEX_EXECUTION: BLOCKED
CORE_LOCK: NOT_ALLOWED
```

최신 설계 구현은 `PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE`, 사용자 승인 Plan, Red 계약, 마이그레이션·롤백 계획이 준비된 뒤에만 시작한다.