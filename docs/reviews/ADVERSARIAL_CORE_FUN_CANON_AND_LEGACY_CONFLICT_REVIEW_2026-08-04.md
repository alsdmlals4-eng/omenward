# [현행] OMENWARD 핵심 재미·정본·구형 문서 적대적 검토

```yaml
review_id: OMW-REV-20260804-CORE-FUN-CANON-LEGACY-CONFLICT-V1
status: PASS_WITH_REQUIRED_CANON_FIXES
review_scope: CORE_FUN / AUTHORITY_ROUTING / LEGACY_CONFLICT / PR_PREFLIGHT
product_code_authority: NONE
```

## 1. 결론

오멘워드의 차별점은 충분히 강하다.

> **공세를 보고 건물로 미래 룰렛을 만들고, 제한된 이동으로 필요한 병력을 얻어 세 전선 중 하나에 비가역 배치한 뒤, 결과를 다음 설계에 환류한다.**

다만 최근 기획이 전투 결정론·문서 상태·아트 구조를 깊게 다루는 동안, 실제 반복 플레이를 만드는 Stage 압력·건물 분기·병종 카운터·전술스킬이 뒤로 밀렸다. 코어는 약하지 않지만 **콘텐츠가 코어를 시험하는 구조가 비어 있는 상태**다.

## 2. P0 — 즉시 수정한 정본 충돌

### OMW-AUD-360 — PROJECT_CORE 구형 계약

- 현상: 최상위 권위 문서가 식량·기본 건물 5종·주변 범위 지휘소를 불변 조건으로 보유.
- 최신 정본: 골드·마석·배치 병력/한도, 건물 6종, MapRun 전체 지휘소 오라.
- 위험: Codex와 후속 기획이 구형 코어를 우선 참조.
- 조치: PROJECT_CORE를 최신 규칙으로 전면 갱신.

### OMW-AUD-361 — 구형 master GDD가 Current 표기

- 현상: `OMENWARD_GAME_DESIGN.md`가 `Vertical Slice Current`를 주장하면서 식량·5종 건물·구형 경제를 서술.
- 위험: 문서 지도보다 파일 제목을 먼저 읽는 작업자가 과거 설계를 구현.
- 조치: `[대체됨]`으로 봉인하고 `OMENWARD_GDD_CURRENT_CANON.md`를 신설.

### OMW-AUD-362 — README·AGENTS 진입점 노후화

- 현상: PR #57·V2 current·구형 럭키·전설 주기·식량 등 오래된 상태를 안내.
- 위험: 첫 읽기부터 잘못된 작업 순서와 구현 범위 형성.
- 조치: 현행 읽기 순서와 2026-08-04 정본으로 갱신.

### OMW-AUD-363 — post-merge 고정 SHA 재귀

- 현상: post-merge Sync가 current_main에 당시 merge SHA를 고정해, Sync PR 자체 병합 직후 다시 과거 SHA가 됨.
- 원인: 현재 상태와 과거 merge 증거를 한 필드에 혼합.
- 조치: current fields는 기본 브랜치에서 동적 해석, immutable merge 증거는 별도 필드에 보존. 회귀 테스트 추가.

## 3. P1 — 권위 중첩·기획 누락

### OMW-AUD-364 — 고아 `APPROVED` Hero 문서군

- 현상: 과거 Hero 문서가 `MAIN_CANONICAL`을 주장하지만 현재 Documentation Map에는 권위 라우팅이 없음.
- 충돌: `SAME_LANE_ONLY`, stable-ID tie-break, exact timer 구조가 최신 Cross-lane 허용·Codex 구현 경계와 완전히 재조정되지 않음.
- 조치: Hero·Legendary family를 `[보류]`로 분류. Stage 압력·병종 역할 이후 재검토.

### OMW-AUD-365 — 첫 10분 문서의 구형 자원·건물

- 현상: 식량, 바리케이드, 일시정지 계획 모드, 구형 HUD 공개 순서를 현행처럼 사용.
- 조치: 핵심 감정 흐름은 새 가드레일로 승계하고 세부 흐름은 `[보류]`.

### OMW-AUD-366 — Meta·Hub 조기 구체화

- 현상: 영구 재화·ReadinessPerk·주점·허브 병영·연구가 상세하지만 런 내부 핵심 콘텐츠 압력이 아직 미정.
- 위험: 메타가 핵심 선택을 우회하거나 구현 범위를 팽창.
- 조치: `[보류]`; 기본 런 콘텐츠와 첫 10~15분 검증 이후 재개.

### OMW-AUD-367 — Stage가 코어를 시험하는 매트릭스 누락

- 현상: 20 Stage 구조는 있으나 각 Stage가 어떤 릴·건물·전선 결정을 요구하는지 정의되지 않음.
- 조치: MASS/ARMORED/FLYING/INFILTRATION/SIEGE 압력 분류를 우선 정본화하고 Stage 매트릭스를 다음 Decision으로 지정.

### OMW-AUD-368 — 건물 6종은 역할만 있고 분기·카운터가 없음

- 위험: 건물이 숫자 업그레이드로 수렴해 “확률을 건설한다”는 차별점 약화.
- 조치: T2/T3마다 특정 압력에 강하고 다른 상황에서 비용이 있는 분기 필요.

### OMW-AUD-369 — 병종 아트 계보와 전투 역할 간 간극

- 현상: T1/T2/T3·영웅·전설의 시각 성장 정본은 강하지만 실제 역할·시너지·카운터가 미완성.
- 조치: 아트 제작보다 병종 역할 매트릭스를 먼저 승인.

### OMW-AUD-370 — 마석·전술스킬이 빈 슬롯

- 현상: 마석과 마력탑이 HUD·건물 정본에 존재하지만 전술스킬 목록·사용 압력·획득 리듬이 없음.
- 위험: UI 자원만 있고 핵심 선택이 없는 장식 시스템.
- 조치: 건물 분기 뒤 전술스킬 Decision 진행.

### OMW-AUD-371 — 상인 역할이 약함

- 현상: Stage 종료에만 등장한다는 위치는 확정됐으나 재고·가격·이벤트 변주가 없음.
- 위험: 단순 소모품 정리 또는 항상 사는 정답 화면.
- 조치: 런 방향을 바꾸는 제한 재고와 건설/회전 골드 기회비용을 명시.

## 4. P2 — 표현·용어 위험

### OMW-AUD-372 — 세 원형 릴과 3×3 보드 오해

- 조치: 세 릴이 3×3 노출창의 세 열을 구성한다고 현행 코어에 명시.

### OMW-AUD-373 — 기술 정본화 과잉

- 현상: Tick·정렬 키·Resolver 등 기술 세부가 플레이어 콘텐츠보다 더 자세함.
- 조치: 플레이어 의미·공정성만 정본, 구현 구조는 Codex 참고안으로 유지.

### OMW-AUD-374 — 이미지 정본과 실제 자산 혼동

- 조치: 스타일 방향은 현행, 생성 비교 이미지는 근거·비정본, 실제 제작은 별도 승인.

### OMW-AUD-375 — 보류 문서 재참조

- 조치: lifecycle registry를 읽기 순서에 넣고 CI에서 필수화.

## 5. 핵심 재미 적합성 평가

| 축 | 평가 | 근거 | 보완 |
|---|---|---|---|
| 예측 | 강함 | 베일의 징조·세 전선 사전 공개 | 압력 태그·Stage 매트릭스 필요 |
| 확률 설계 | 매우 강함 | 건물·TokenSource·세 릴·가로 이동 | 건물 분기와 TokenSource 차이 필요 |
| 커밋 | 강함 | 보관·판매·비가역 전선 배치 | 첫 플레이에서 책임감 검증 필요 |
| 전투 판독 | 개선됨 | Route·Targeting·카메라·아트 정본 | 병종 역할·VFX 실제 검증 필요 |
| 반복 동기 | 중간 | 다음 Stage 설계 환류 개념 | Stage 콘텐츠 차이와 장기 빌드 목표 필요 |
| 실패 학습 | 중간 | provenance·원인 복기 의도 | 플레이어용 결과 요약 형식 필요 |

종합:

```text
CORE_IDENTITY = STRONG
CONTENT_PRESSURE = UNDERDEFINED
CANON_ROUTING = FIX_REQUIRED
IMPLEMENTATION_READINESS = BLOCKED
```

## 6. 더 나은 방향

기술 상세를 더 추가하기보다 다음 순서를 따른다.

```text
Stage 압력 매트릭스
→ 건물 6종 T2/T3 분기
→ 병종 역할·시너지·카운터
→ 마석·전술스킬
→ Stage 종료 상인
→ 첫 10~15분 흐름
→ Hero·Legendary 재조정
→ Meta·Hub 재조정
```

이 순서는 모든 후속 콘텐츠가 핵심 루프에 실제로 연결되는지 먼저 검증한다.

## 7. PR 검수 기준

- [ ] main 대비 behind 0.
- [ ] 변경된 게임 제품 경로 0.
- [ ] README·AGENTS·PROJECT_CORE·GDD·Map·Lifecycle이 같은 현행 상태를 말함.
- [ ] `[대체됨]`, `[보류]`, `[폐기]` 파일이 신규 구현 권위로 라우팅되지 않음.
- [ ] `current_main`·`context_baseline_commit` 동적 해석.
- [ ] Core CI·GDD Sheet CI·Base CI Green.
- [ ] OPEN_P0·OPEN_P1·MERGE_BLOCKER 0.
- [ ] TODO·TBD 자리표시자 없음.
- [ ] 리뷰·미해결 thread 0 또는 명시 해결.

## 8. BLOCKER 판정

```text
BLOCKER_BEFORE_FIX = TRUE
BLOCKER_AFTER_CANON_FIX = FALSE_PENDING_CI_AND_SHEET_READBACK
PRODUCT_CODE = UNCHANGED
```
