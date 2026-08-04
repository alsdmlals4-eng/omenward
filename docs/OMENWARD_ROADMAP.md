# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-05
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_phase: CORE_FUN_AND_CONTENT_DEEPENING
current_grill_me_count: 3_OF_10
current_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
product_implementation: NOT_AUTHORIZED
art_asset_production: NOT_AUTHORIZED
human_validation: NOT_RUN
```

전체 시스템 연결 기준선은 `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. 최신 세부 권위는 `PROJECT_CORE.md`, `OMENWARD_GDD_CURRENT_CANON.md`, `DOCUMENTATION_MAP.md`, `DOCUMENT_LIFECYCLE_REGISTRY.md`가 라우팅한다.

## 1. 보존된 Legacy 증거

```text
기존 기술 기준선·C1·C2·C3 자동 증거 확보
C1 승인 룰렛 핵심 계약 원격 검증·병합 완료
상태 = **REMOTE_PROVEN**
제품 구현: `NOT_STARTED`
```

이 증거는 Legacy C1·C2·C3 계약에만 적용된다. 최신 물리 릴·HUD·건물 6종·Stage 압력·아트가 구현됐다는 뜻이 아니다.

## 2. 완료된 기획 기반

- 결과 재현·원인 복기 요구.
- 공통 전투 공정성과 Damage/Protection/Status 의미.
- 세 전선·Route·Targeting 경험과 전장 시각 계층.
- HUD·룰렛·골드·마석·병력 한도·Stage 종료 상인.
- 금고·농장·병영·방어탑·지휘소·마력탑 6종.
- 인게임 금화·T1/T2 병종 자산의 룰렛 재사용.
- 픽셀·일러스트 하이브리드 아트 방향.
- 문서 수명주기와 동적 current-main 정책.
- 핵심 재미 4축과 다섯 압력 분류.
- 20 Stage·3 Wave Beat·Danger/Boss 매트릭스.
- 건물 인스턴스별 두 T2·선택 경로 T3와 포기 비용.
- 벤치마킹·현업 비교·승인 10건 최대 배치·조기 체크포인트·TDD 정책.

이 완료는 제품 구현 완료가 아니다.

## 3. 현재 위치

```text
[완료] 핵심 재미·구형 충돌 가드레일
→ [완료] Stage·Wave·Danger·Boss 압력 매트릭스
→ [완료] 건물 6종 T2/T3 분기·카운터
→ [현재] 병종 역할·시너지·카운터
→ 전술스킬·마석 리듬
→ Stage 종료 상인
→ 첫 10~15분 흐름
→ Hero·Legendary 재조정
→ Meta·Hub 재조정
→ 통합 검수·fresh preflight
→ 별도 Codex 구현 계획 승인
→ 구현·자동 검증·사람 플레이
```

## 4. Planning Batch

### Decision 1/10 — 핵심 재미·콘텐츠 가드레일

상태: **main 정본 / 제품 미구현**.

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

### Decision 2/10 — Stage 압력 매트릭스

상태: **main 정본 / 제품 미구현**.

```text
MapRun = 20 Stage
Wave Beat = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

- Stage 시작 전에 압력·전선·Route·목표·치명 행동 공개.
- Danger는 한 공개 규칙 변형.
- Boss는 Route·태세·목표·호위·집중 공격 창을 변경.
- exact 시간·수량·Threat Budget은 시뮬레이션 후 조정.

### Decision 3/10 — 건물 T2/T3

상태: **사용자 승인·PR 정본 동기화 진행 / 제품 미구현**.

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
```

- 선택은 건물 인스턴스별.
- 다른 인스턴스는 다른 분기 선택 가능.
- 모든 분기에 얻는 것과 포기하는 것 표시.
- T3는 결과 곡선·표적·전선 교리·Route·자원 타이밍을 변경.
- 건물만으로 다섯 압력을 전부 해결하지 않음.
- 정확한 비용·배율·범위·쿨다운은 `PENDING_SIMULATION`.

```text
금고 = 안정/행운
농장 = 징집/예비
병영 = 전열/기동
방어탑 = 연사/포격
지휘소 = 돌격/수비
마력탑 = 유량/저장
```

### Decision 4/10 — 병종 역할·시너지·카운터

다음 작업:

- T1 원형과 T2 역할 분기, T3 전문화.
- Ground/Flying/침투·전열/후열·건물 대응.
- 전열/기동 병영의 실제 병종 TokenSource.
- 다섯 압력별 최소 두 대응 경로 완성.
- T1/T2 인게임 이미지 룰렛 재사용과 T3 Preview 표현.
- 건물·전술 역할을 무효화하는 만능 병종 방지.

### Decision 5/10 — 전술스킬·마석

- 획득·저장·소비 리듬.
- 긴급 대응과 선제 계획의 차이.
- 유량/저장 마력탑과 실제 선택 연결.

### Decision 6/10 — Stage 종료 상인

- 제한 재고와 골드 기회비용.
- Boss 뒤 런 방향 재조정 상품·이벤트.
- 반복 파밍·항상 사는 정답 방지.

### Decision 7/10 — 첫 10~15분

- Stage 1~3으로 공세→건물→룰렛→배치→복기 두 번.
- 최신 HUD·자원·건물 전문화 사용.
- 구형 식량·바리케이드·자동생산·강제 Pause 제거.

### Decision 8/10 — Hero·Legendary 재조정

- `[보류]` 문서군을 최신 Stage·건물·병종·전술과 재검토.

### Decision 9/10 — Meta·Hub 재조정

- 기본 Run을 우회하지 않는 수평 해금.

### Decision 10/10 — 통합 검수

- 첫 10~15분 플레이 시나리오.
- 20 Stage 장기 선택 구조.
- 핵심 재미·콘텐츠·UX·아트 적대적 종합 검토.
- GitHub·Sheet·PR fresh preflight와 구현 handoff 준비 판정.

## 5. 작업 운영

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
TDD = RED → GREEN → REFACTOR
GITHUB_WRITE = EXPLICIT_NON_DEFAULT_BRANCH_ONLY
```

10건에 도달하면 정본·Sheet·PR을 검증하고 병합한다. P0/P1 충돌, 세션 종료, 다수 핵심 문서 영향이 있으면 조기 체크포인트를 허용하되 카운터를 임의 초기화하지 않는다.

## 6. 구형 문서 경계

```text
[대체됨] APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md
[보류] APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md
[부분 승계] APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
[폐기] 동일 건물 인스턴스 교차 분기·양쪽 T3
```

상세 파일별 상태는 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 소유한다.

## 7. 구현 Gate

Codex 구현은 다음 이후에만 시작한다.

- 건물·병종·전술이 다섯 압력에 실제 최소 두 대응 경로를 제공.
- 첫 10~15분 흐름과 사람 검증 기준 승인.
- 제품 범위·파일·상태 소유·테스트·롤백 계획 승인.
- Red 테스트와 자동·수동 검증 계획 승인.
- 문서 PR과 제품 코드 PR 분리.

## 8. 검증 단계

```text
문서 RED 테스트
→ 최소 Green 정본
→ Refactor·전체 재검증
→ Sheet bounded read-back
→ exact-head PR preflight
→ 제품 단위 테스트·headless
→ deterministic simulation
→ 첫 10~15분 사람 플레이
→ 장기 MapRun 검증
```

```text
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```
