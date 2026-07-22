# 오멘워드 현재 구현 상태

- 조사일: 2026-07-22
- 기준 main: `ef9e66e3bc5be7711c36123e6c6d7fe8ec8dc9a2`
- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- C1 최종 검증 run: `29926598807`
- 프로젝트 코어: `CORE_CONFIRMED` / `CORE_LOCKED`
- 판정:
  - `TECHNICAL_BASELINE_IMPLEMENTED`
  - `C1_ROULETTE_CORE_REMOTE_PROVEN`
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
| Godot 프로젝트 | `project.godot`, main Scene, 960×540 논리 화면, 1920×1080 출력, Compatibility renderer | `REMOTE_PROVEN` |
| 상태 소유 | `GameSession`, `StageRun`, `CombatClock`, `DataRegistry`, `DeterminismService` | `IMPLEMENTED` |
| 공용 데이터 | 공용 archetype·Tier·Rank·FactionVisual·Animation 계약과 bootstrap catalog | `IMPLEMENTED` |
| 경제 | 기본·접전지·거점 수입 계산 서비스, 금화·식량 | `IMPLEMENTED_COMPONENT` |
| 건설 | 소유·안정화·점령 revision을 검사하는 건설 서비스 | `IMPLEMENTED_COMPONENT` |
| 전투 | 독립 3라인, 공용 유닛, 기본 이동·타기팅·공격, 암살자 우회 상태 | `IMPLEMENTED_COMPONENT` |
| 웨이브 | 튜토리얼 W1~4, 정규 W1~20 데이터와 60초 출격 시계 | `IMPLEMENTED_COMPONENT` |
| 테스트 | bootstrap·데이터·경제·C1 룰렛·전투·웨이브·우회 headless 회귀와 Python 계약 | `REMOTE_PROVEN` |

## 3. 부분 구현 또는 승인 계약과 다른 영역

### 3.1 룰렛 — `C1_ROULETTE_CORE_REMOTE_PROVEN`

검증된 구현:

```text
3×3 결정론적 보드
→ 중앙 가로줄 동일 비-X 선행 판정
→ 전체 8개 완성선
→ common / elite / hero / legendary
→ 출처 선택
→ 유닛 1개 또는 금화
→ StageRun 보관·라인 배치
```

- 기존 9개 직접 카드 API와 placeholder 테스트를 제거했다.
- 기본 병영 전사 토큰을 추가하고 농장·포탑의 유닛 토큰을 제거했다.
- 전설 1회 제한과 이후 영웅 2기 변환, 금화 75%/200%/500%를 구현했다.
- 보상 없는 결과는 저장하지 않고, 보관 차단 회전은 금화를 소비하지 않는다.
- 보관 유닛 배치 시 식량을 예약하며 복수 병영 출처 선택도 같은 시드로 재현된다.
- 고정 상위 등급 템플릿은 미확정이므로 `source_archetype_rank_fallback`을 명시한다.
- 이동권 지급량과 상충하는 럭키 규칙은 런타임 생성 풀에서 가역적으로 보류한다.
- Godot 스크립트 회귀는 `load()` 존재뿐 아니라 `Script.can_instantiate()`까지 검사한다.

판정: `C1_ROULETTE_CORE_REMOTE_PROVEN` — Godot 4.7.1 import·전체 headless·runtime smoke와 4환경 계약 검증 통과 (`29926598807`).

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

현재 HUD는 금화·식량·웨이브·전조 초·Spin·Barracks·Tower·Farm·룰렛 보드·결과·라인 배치 버튼을 제공한다.

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

### 이번 C1에서 원격 실행한 것

- Godot 4.7.1 editor import.
- 전체 `tests/headless/*_test.gd`.
- runtime smoke.
- Ubuntu/Windows × Python 3.12/3.13 계약·문서·Skill 검증.
- C1 결정론·중앙 판정·등급·금화·전설 제한·보관·배치 회귀.
- 보상 없는 결과·차단 회전 금화 불변·식량 예약·복수 출처 결정론 회귀.
- 스크립트가 실제 인스턴스화 가능한지 확인하는 테스트 러너 방어.
- 활성 문서의 구형 Work Order·Goal·Proposal 직접 참조와 깨진 링크 검사.

증거: GitHub Actions run `29926598807` / 구현 검증 head `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`.

### 실행하지 않은 것

- 1920×1080 사람 플레이.
- 1280×720 가독성 QA.
- W1~W20 연속 플레이.
- 100,000시드 확률·경제 분포.
- 재미·밸런스·성능 계측.

따라서 C1 룰렛 핵심 계약은 `REMOTE_PROVEN`이지만 전체 코어 루프와 사람 플레이는 아직 완료가 아니다.

## 5. 현재 우선순위

```text
1. PR #49 병합
2. 승인된 전투 → 거점·성문·승패 목적 루프 연결
3. C1U 이동권·럭키·고정 상위 템플릿 결정과 100,000시드 시뮬레이션
4. 승인 코어 UX 6종 최소 구현
5. 10~15분 코어 플레이테스트
6. 밸런스 안정화와 콘텐츠·아트 확장
```

C1U는 사용자 결정을 요구하므로 임의 구현하지 않는다. 다음 자동 구현 작업은 이미 승인된 전투 목적 루프 C2로 진행할 수 있다.

## 6. C1 완료 판정과 다음 게이트

C1 룰렛 핵심 계약 완료 조건:

- 중앙 판정·8개 완성선·등급·금화·전설 제한이 승인 정본과 일치한다.
- 9개 직접 카드 placeholder와 관련 회귀 계약이 제거됐다.
- 기본 병영 토큰, StageRun 보관과 라인 배치가 연결된다.
- 같은 시드·건물 스냅샷과 복수 출처가 같은 결과를 만든다.
- Godot 4.7.1 editor import·전체 headless·runtime smoke가 통과한다.
- 활성 문서의 구형 실행 입력 직접 참조가 0건이다.
- 테스트 러너가 스크립트 파싱 오류를 허위 성공으로 통과시키지 않는다.

위 조건은 run `29926598807`에서 통과했다. 다음 승인 구현 게이트는 C2 전투 목적 루프이며, 다음 제품 결정 게이트는 C1U 이동권·럭키·고정 상위 등급 템플릿·100,000시드 분포다.
