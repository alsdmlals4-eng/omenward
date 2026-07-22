# 오멘워드 현재 구현 상태

- 조사일: 2026-07-22
- 기준 브랜치: `main`
- 기준 커밋: `69c571c5a49502f9da57e1c8d8eba04455380c0f`
- 판정:
  - `TECHNICAL_BASELINE_IMPLEMENTED`
  - `CORE_VERTICAL_SLICE_PARTIAL`
  - `CORE_LOOP_NOT_PROVEN`
  - `HUMAN_QA_NOT_RUN`

이 문서는 “파일이 존재하는가”, “승인 계약이 구현됐는가”, “사람이 플레이해 재미와 가독성을 검증했는가”를 분리한다. 상태 문구가 다른 문서와 충돌하면 최신 실제 파일·테스트와 이 문서를 우선 확인한다.

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `IMPLEMENTED` | 실제 파일과 실행 경로가 존재함 |
| `PARTIAL` | 구성요소 일부가 존재하지만 승인된 End-to-End 계약이 닫히지 않음 |
| `PROVEN` | 요구 계약과 실제 실행 증거가 함께 존재함 |
| `NOT_PROVEN` | 파일 또는 테스트가 있어도 제품 계약 전체 증거가 없음 |
| `NOT_RUN` | 이번 기준점에서 해당 실행·수동 검증을 하지 않음 |
| `DIVERGENT` | 현재 구현·테스트가 승인 책임 문서와 다름 |

## 2. 구현된 기술 기준선

| 영역 | 현재 증거 | 판정 |
|---|---|---|
| Godot 프로젝트 | `project.godot`, main Scene, 960×540 논리 화면, 1920×1080 출력, Compatibility renderer | `IMPLEMENTED` |
| 상태 소유 | `GameSession`, `StageRun`, `CombatClock`, `DataRegistry`, `DeterminismService` | `IMPLEMENTED` |
| 공용 데이터 | 공용 archetype·Tier·Rank·FactionVisual·Animation 계약과 bootstrap catalog | `IMPLEMENTED` |
| 경제 | 기본·접전지·거점 수입 계산 서비스, 금화·식량 | `IMPLEMENTED_COMPONENT` |
| 건설 | 소유·안정화·점령 revision을 검사하는 건설 서비스 | `IMPLEMENTED_COMPONENT` |
| 전투 | 독립 3라인, 공용 유닛, 기본 이동·타기팅·공격, 암살자 우회 상태 | `IMPLEMENTED_COMPONENT` |
| 웨이브 | 튜토리얼 W1~4, 정규 W1~20 데이터와 60초 출격 시계 | `IMPLEMENTED_COMPONENT` |
| 테스트 | bootstrap·데이터·경제·룰렛 placeholder·전투·웨이브·우회 관련 headless 테스트 파일 | `IMPLEMENTED` |

## 3. 부분 구현 또는 승인 계약과 다른 영역

### 3.1 룰렛 — `DIVERGENT`

승인 계약:

```text
3×3 보드
→ 중앙 가로줄 동일 비-X 심벌 판정
→ 동일 심벌 완성선 계산
→ 일반·엘리트·영웅·전설 등급
→ 실제 보상 1개 생성
→ 결과 보관·배치
```

현재 구현:

- 20 Gold를 지불하고 9개의 `UnitSpawnDefinition`을 직접 반환한다.
- 중앙 판정 줄, X·금화, 완성선, 등급, 전설 제한, 럭키 찬스, 이동권이 없다.
- 현재 테스트도 9개 카드 반환을 기대하므로 승인 계약이 아니라 placeholder 계약을 고정한다.

판정: `CORE_CONTRACT_DIVERGENT`.

### 3.2 전투 목적 루프 — `PARTIAL`

- 유닛끼리 이동·공격하는 기본 전투는 존재한다.
- `OutpostState`, `GateState`, 암살자 우회 상태는 존재한다.
- 정상 전투 흐름에서 유닛 점령력과 거점 점령 시작이 연결되지 않는다.
- 성문 공격·본진 파괴·전장 상태 기반 승리·패배가 닫히지 않았다.
- 현재 승패는 외부 `stage_victory`·`stage_defeat` 명령으로 기록한다.
- `StageEconomy.advance()`에 전달되는 접전지 소유 수가 현재 `0`으로 고정돼 있다.

판정: `CORE_LOOP_PARTIAL`.

### 3.3 베일의 징조 — `PARTIAL`

- 다음 공세까지의 시간 계산과 HUD 텍스트는 존재한다.
- 승인된 T-30 라인·병종·수량, T-15 집결·경로, T-5 위험 라인 강조가 없다.

판정: `CORE_INFORMATION_LOOP_PARTIAL`.

### 3.4 코어 UX — `NOT_IMPLEMENTED`

현재 HUD는 금화·식량·웨이브·전조 초·Spin·Tower·Farm·문자열 카드·라인 버튼을 제공한다.

다음 승인 UX는 아직 실제 데이터와 연결되지 않았다.

1. 건설 전 룰렛 확률 미리보기.
2. 룰렛 토큰 장부.
3. T-30/T-15/T-5 공세 전조.
4. 상성·사거리·타기팅 오버레이.
5. 웨이브 종료 후 라인별 원인 보고.
6. 건설 선택 비교 UI.

### 3.5 콘텐츠 검증력 — `INSUFFICIENT_FOR_CORE_PLAYTEST`

- W1~W20 시간표와 보스 표식은 존재한다.
- 다수 웨이브가 단일 유닛 중심이라 라인 분산·상성·복합 대응의 재미를 검증하기 어렵다.
- 콘텐츠 확대보다 코어 계약 복구가 먼저다.

## 4. 검증 증거 경계

### 확인한 것

- 저장소 정적 파일.
- 현재 코드·데이터·headless 테스트의 계약.
- 승인 책임 문서와 구현 간 차이.
- 최근 `main`과 열린 PR·Issue 상태.

### 이번 문서 복구에서 실행하지 않은 것

- Godot editor import.
- headless 테스트 재실행.
- runtime smoke.
- 1920×1080 사람 플레이.
- 1280×720 가독성 QA.
- W1~W20 연속 플레이.
- 재미·밸런스·성능 계측.

따라서 “프로젝트가 실행된다”는 과거 증거와 “현재 기준점에서 재검증했다”는 주장을 혼동하지 않는다.

## 5. 현재 우선순위

```text
1. 정본·프로젝트 코어 복구
2. 승인 룰렛 계약 복구
3. 전투 → 거점·성문·승패 목적 루프 연결
4. 승인 코어 UX 6종 최소 구현
5. 10~15분 코어 플레이테스트
6. 밸런스 안정화와 콘텐츠·아트 확장
```

## 6. 다음 완료 게이트

정본 복구 완료 조건:

- `PROJECT_CORE.md`가 제품 코어와 변경 가능한 외피를 분리한다.
- README·GDD·로드맵·상태·인수인계·미확정 목록이 같은 단계 용어를 사용한다.
- 현재 구현과 미구현을 파일 증거로 분리한다.
- 과거 `구현 전`과 과도한 `수직 슬라이스 완료` 주장을 현재 상태로 사용하지 않는다.
- 다음 변경은 게임 코드 전체가 아니라 승인 룰렛 계약 복구로 한정한다.
