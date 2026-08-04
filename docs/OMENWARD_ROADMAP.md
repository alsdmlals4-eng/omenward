# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-04
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_phase: CORE_FUN_AND_CONTENT_DEEPENING
current_grill_me_count: 2_OF_10
current_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
product_implementation: NOT_AUTHORIZED
art_asset_production: NOT_AUTHORIZED
human_validation: NOT_RUN
```

전체 시스템 연결 기준선은 `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. 최신 세부 권위는 `PROJECT_CORE.md`, `OMENWARD_GDD_CURRENT_CANON.md`, `DOCUMENTATION_MAP.md`, `DOCUMENT_LIFECYCLE_REGISTRY.md`가 라우팅한다.

## 1. 보존된 Legacy 증거

```text
C1 승인 룰렛 핵심 계약 원격 검증·병합 완료
상태 = **REMOTE_PROVEN**
```

이 증거는 Legacy C1 중앙 판정·완성선·등급·보상 계약에만 적용된다. 최신 물리 릴·HUD·건물 6종·Stage 압력·아트가 구현됐다는 뜻이 아니다.

## 2. 완료된 기획 기반

- 결과 재현·원인 복기 요구.
- 공통 전투 공정성·Damage/Protection/Status 의미.
- 전투 공간·세 전선·Route·Targeting 경험.
- 전장 시각 계층·카메라.
- HUD·룰렛·골드·마석·병력 한도.
- 금고·농장·병영·방어탑·지휘소·마력탑 6종.
- 인게임 금화·T1/T2 병종 자산 룰렛 재사용.
- 픽셀·일러스트 하이브리드 아트 방향.
- 문서 수명주기와 동적 current-main 정책.
- 핵심 재미 4축과 다섯 압력 분류.
- 20 Stage·3 Wave Beat·Danger/Boss 압력 매트릭스.

이 완료는 제품 구현 완료가 아니다.

## 3. 현재 위치

```text
[완료] 정본 충돌 제거·핵심 재미 가드레일
→ [완료] Stage·Wave·Danger·Boss 압력 매트릭스
→ [현재] 건물 6종 T2/T3 분기·카운터
→ 병종 역할·시너지·카운터
→ 전술스킬·마석 리듬
→ Stage 종료 상인
→ 첫 10~15분 흐름
→ Hero·Legendary 재조정
→ Meta·Hub 재조정
→ 10개 Decision fresh preflight
→ 별도 Codex 구현 계획 승인
→ 구현·자동 검증·사람 플레이
```

## 4. Planning Batch 1 — 콘텐츠 압력

### Decision 1 — 핵심 재미·콘텐츠 가드레일

상태: **main 정본 완료 / 제품 미구현**.

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

압력:

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

### Decision 2 — Stage 압력 매트릭스

상태: **사용자 승인·정본 동기화 진행 / 제품 미구현**.

```text
MapRun = 20 Stage
Wave Beat = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
```

네 막:

- 1~5: 다섯 압력 문해력.
- 6~10: 두 압력 조합.
- 11~15: 대응 기회비용.
- 16~20: 세 전선·여러 Route 종합 숙련.

공정성:

- Stage 시작 전 압력·전선·Route·목표·치명적 행동 공개.
- Danger는 한 가지 공개 규칙 변형.
- Boss는 Route·태세·목표·호위·집중 공격 창을 변경.
- Stage 시작 뒤 필수 카운터를 숨은 무작위로 바꾸지 않음.
- exact 시간·수량·Threat Budget은 시뮬레이션 후 조정.

### Decision 3 — 건물 T2/T3

다음 작업:

- 금고·농장·병영·방어탑·지휘소·마력탑의 T2 양자택일.
- T3 계열 전문화.
- 압력별 강점과 실제 포기 비용.
- 건물·병종·전술스킬 역할 중복 방지.
- TokenSource 분기의 룰렛 영향.
- MapRun 전역 지휘소 오라의 과잉 정답 방지.

### Decision 4 — 병종 역할

- T1 원형, T2 역할 분기, T3 전문화.
- Ground/Flying/침투·전열/후열·건물 대응.
- Stage 압력별 최소 두 대응 경로 완성.
- 아트 실루엣과 전투 기능 일치.

### Decision 5 — 전술스킬·마석

- 획득·저장·소비 리듬.
- 긴급 대응과 선제 계획의 차이.
- 마력탑 분기와 선택 압력.

### Decision 6 — Stage 종료 상인

- 제한 재고.
- 건설·회전과 골드 기회비용.
- Boss 뒤 런 방향 재조정 상품·이벤트.
- 반복 파밍·항상 사는 정답 방지.

### Decision 7 — 첫 10~15분

- Stage 1~3을 사용해 공세→건물→룰렛→배치→복기 두 번.
- 최신 HUD·자원·건물 6종 사용.
- 구형 식량·바리케이드·병영 자동생산·강제 Pause 제거.

### Decision 8 — Hero·Legendary 재조정

- lifecycle registry의 `[보류]` 문서군 재검토.
- 최신 Stage 압력·Targeting·Modifier와 통합.

### Decision 9 — Meta·Hub 재조정

- 기본 런을 우회하지 않는 수평 해금.
- 메타가 Stage 대응 실패를 자동 상쇄하지 않도록 제한.

### Decision 10 — 통합 검수

- 첫 10~15분 플레이 시나리오.
- 20 Stage 장기 선택 구조.
- Sheet·GitHub·PR fresh preflight.
- 제품 구현 handoff 준비 여부 판정.

## 5. 구형 Stage 문서 경계

```text
[대체됨] APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md
[보류] APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md
[부분 승계] APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
```

- `15웨이브=1스테이지`와 고정 60초 공세를 구현하지 않는다.
- 구형 식량·병영 자동생산·바리케이드 수치를 구현하지 않는다.
- Vertical Slice 문서는 시스템 연결 목표만 계승한다.

## 6. 구현 Gate

Codex 구현은 다음 이후에만 시작한다.

- 건물·병종·전술스킬이 다섯 압력에 최소 두 대응 경로를 제공.
- 첫 10~15분 흐름과 사람 검증 기준 승인.
- `[보류]` Hero·Meta 문서가 최신 정본과 재조정.
- 제품 범위·파일·상태 소유·테스트·롤백 계획 승인.
- 문서 PR과 제품 코드 PR 분리.

## 7. 검증 단계

```text
문서 CI
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
