# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-04
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_phase: CORE_FUN_AND_CONTENT_DEEPENING
current_grill_me_count: 1_OF_10
product_implementation: NOT_AUTHORIZED
art_asset_production: NOT_AUTHORIZED
human_validation: NOT_RUN
```

전체 시스템 기준선은 `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`이며, 최신 권위는 `docs/PROJECT_CORE.md`, `docs/OMENWARD_GDD_CURRENT_CANON.md`, `docs/DOCUMENTATION_MAP.md`가 라우팅한다.

## 1. 완료된 기획 기반

- 결과 재현·원인 복기 요구.
- 공통 전투 공정성·Damage/Protection/Status 의미.
- 전투 공간·세 전선·Route·Targeting 경험.
- 전장 시각 계층·카메라.
- HUD·룰렛·골드·마석·병력 한도.
- 금고·농장·병영·방어탑·지휘소·마력탑 6종.
- 인게임 금화·T1/T2 병종 자산 룰렛 재사용.
- 픽셀·일러스트 하이브리드 아트 방향.
- 문서 수명주기와 동적 current-main 정책.

이 완료는 제품 구현 완료가 아니다.

## 2. 현재 위치

```text
[현재] 정본 충돌 제거·핵심 재미 가드레일
→ Stage·Wave·Danger·Boss 압력 매트릭스
→ 건물 6종 T2/T3 분기·카운터
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

## 3. Planning Batch 1 — 콘텐츠 압력

### Decision 1 — 핵심 재미·콘텐츠 가드레일

상태: 승인 진행·PR 검증 중.

- 예고된 압력.
- 제작한 확률.
- 비가역 전선 커밋.
- 설명 가능한 결과.
- MASS/ARMORED/FLYING/INFILTRATION/SIEGE 압력 분류.

### Decision 2 — Stage 압력 매트릭스

다음 작업:

- 일반 Stage가 하나씩 가르칠 압력.
- Danger의 규칙 변형.
- Boss의 선택 구조 변화.
- 공세 예고 카드와 실제 행동 일치.

### Decision 3 — 건물 T2/T3

- 특정 압력에 강하고 다른 상황에서 비용이 있는 분기.
- 순수 색·수치 분기 금지.
- TokenSource·전장·경제 역할 연결.

### Decision 4 — 병종 역할

- T1 원형, T2 역할 분기, T3 전문화.
- Ground/Flying/침투·전열/후열·건물 대응.
- 아트 실루엣과 전투 기능 일치.

### Decision 5 — 전술스킬·마석

- 획득·저장·소비 리듬.
- 긴급 대응과 선제 계획의 차이.
- 마력탑 분기와 선택 압력.

### Decision 6 — Stage 종료 상인

- 제한 재고.
- 건설·회전과 골드 기회비용.
- 런 방향을 바꾸는 상품·이벤트.

### Decision 7 — 첫 10~15분

- 공세→건물→룰렛→배치→복기 두 번.
- 최신 HUD·자원·건물 6종 사용.
- 구형 식량·바리케이드·강제 Pause 가정 제거.

### Decision 8 — Hero·Legendary 재조정

- lifecycle registry의 `[보류]` 문서군 재검토.
- 최신 Targeting·Modifier·콘텐츠 압력과 통합.

### Decision 9 — Meta·Hub 재조정

- 기본 런을 우회하지 않는 수평 해금.
- 메타가 코어 콘텐츠보다 먼저 구현되지 않도록 제한.

### Decision 10 — 통합 검수

- 첫 10~15분 플레이 시나리오.
- Sheet·GitHub·PR fresh preflight.
- 제품 구현 handoff 준비 여부 판정.

## 4. 구현 Gate

Codex 구현은 다음 이후에만 시작한다.

- 현재 Planning Batch의 핵심 콘텐츠가 사용자 승인됨.
- `[보류]` Hero·Meta 문서가 최신 정본과 재조정됨.
- 제품 범위·파일·상태 소유·테스트·롤백 계획 승인.
- 문서 PR과 제품 코드 PR 분리.

## 5. 검증 단계

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
