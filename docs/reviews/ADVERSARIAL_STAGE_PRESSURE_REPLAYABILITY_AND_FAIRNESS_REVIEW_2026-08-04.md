# [현행] OMENWARD Stage 압력·리플레이성·공정성 적대적 검토

```yaml
review_id: OMW-REV-20260804-STAGE-PRESSURE-REPLAYABILITY-FAIRNESS-V1
status: PASS / REQUIRED_CANON_FIXES_APPLIED
review_scope: STAGE / WAVE / DANGER / BOSS / REPLAYABILITY / FAIRNESS / PR_PREFLIGHT
product_code_authority: NONE
simulation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결론

20 Stage를 다음 네 막으로 나눈 구조는 오멘워드의 핵심 재미와 맞는다.

```text
압력 문해력
→ 압력 조합
→ 기회비용
→ 종합 숙련
```

강점:

- Stage가 단순 수치 상승이 아니라 어떤 결정을 시험하는지 명확하다.
- `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`가 Route·목표·행동 차이로 구분된다.
- Danger는 공개된 한 가지 규칙 변형을 사용한다.
- Boss는 Route·태세·Pattern을 바꾸므로 HP Sponge로 수렴하지 않는다.
- 고정 압력 역할과 맵별 작성 변형을 분리해 학습과 리플레이성을 함께 유지한다.

현재 한계:

- 건물 T2/T3, 병종 역할, 전술스킬이 아직 압력과 실제로 연결되지 않았다.
- 정확한 Wave 길이·Threat Budget·보상은 시뮬레이션 전 확정할 수 없다.
- 따라서 Stage 매트릭스는 콘텐츠 구조 정본이며 제품 구현 준비 완료를 의미하지 않는다.

## 2. 핵심 재미 적합성

| 핵심 축 | 평가 | Stage 구조와의 연결 | 남은 위험 |
|---|---|---|---|
| 예고된 압력 | 강함 | 모든 Stage가 주 압력·Route·목표를 사전 공개 | UI 표현 검증 필요 |
| 제작한 확률 | 강함 | 다음 Wave를 보고 TokenSource·릴을 조정 | 건물 분기 미확정 |
| 제한 조작 | 강함 | 겹침·주 전선 이동 전에 이동권·보관을 계획 | 정확한 획득 리듬 미확정 |
| 비가역 커밋 | 매우 강함 | Stage 9·14·19가 과투자와 예비대 가치를 시험 | 사람 플레이 검증 필요 |
| 설명 가능한 결과 | 강함 | 압력 태그·Route·목표가 실패 원인과 연결 | 결과 요약 UX 미구현 |
| 반복 동기 | 개선됨 | 네 막마다 새 판단 층을 추가 | 적 패키지 다양성 필요 |

종합:

```text
CORE_FIT = STRONG
CONTENT_PROGRESSION = COHERENT
REPLAYABILITY = VIABLE_WITH_AUTHORED_VARIANTS
FAIRNESS = PASS_IF_FULL_OMEN_DISCLOSURE_IS_PRESERVED
DOCUMENT_PR_MERGE_READINESS = PASS
IMPLEMENTATION_READINESS = BLOCKED_BY_BUILDING_AND_TROOP_COUNTER_DECISIONS
```

## 3. P0 공격 — 공정성·정본 충돌

### OMW-AUD-376 — 구형 `15웨이브=1스테이지` 계약 충돌

- 현상: `APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`는 하나의 Stage가 15~20 Wave로 진행된다고 서술한다.
- 현행: 한 MapRun은 20 Stage이며 각 Stage는 현재 3개 Wave Beat 기준선이다.
- 위험: Codex가 20 Stage 안에 다시 15~20 Wave를 넣어 런 길이·콘텐츠 계층을 잘못 구현.
- 조치: 구형 문서를 `[대체됨]`으로 표시하고 새 Stage 압력 매트릭스가 승계.

### OMW-AUD-377 — 구형 첫 4공세 문서의 식량·자동생산·바리케이드

- 현상: 구형 튜토리얼 밸런스가 식량, 병영 자동생산, 바리케이드, 구형 첫 10분 흐름을 전제로 한다.
- 충돌: 현재 자원·TokenSource·건물 6종·룰렛 중심 학습과 다름.
- 조치: `[보류]`; 첫 10~15분 Decision에서 Stage 1~5 학습 목표만 재검토해 승계.

### OMW-AUD-378 — Vertical Slice 기준선의 구형 Stage·자원 세부

- 현상: 전체 시스템 기준선에 식량·건물 5종·주변 지휘소 등 구형 세부가 남아 있다.
- 위험: 파일 전체를 최신 세부 권위로 오해.
- 조치: 기준선은 시스템 연결 계보로 유지하고 PROJECT_CORE·Documentation Map·Lifecycle Registry에서 부분 승계와 최신 Overlay를 명시.

### OMW-AUD-379 — 비가역 배치 뒤 주 전선 무작위 변경

- 공격: Stage 14 같은 주 전선 이동이 전투 중 무작위로 바뀌면 기존 배치가 함정이 된다.
- 조치: 전체 Wave 순서와 전선 배치를 Stage 시작 전에 공개. 숨은 전환 금지.

### OMW-AUD-380 — Danger가 기본 기능을 강제로 끔

- 공격: 룰렛·건설·배치·정보 공개를 막는 방식으로 난도를 만들 수 있다.
- 조치: Danger는 Route·시간·전선 이동·Route 수렴 같은 한 가지 규칙 변형만 사용하고 핵심 기능과 치명적 정보는 유지.

## 4. P1 공격 — 콘텐츠 구조

### OMW-AUD-381 — Stage 1~5 학습 과밀

- 공격: 첫 다섯 Stage에서 다섯 압력과 Danger·Boss까지 소개하면 초반이 과밀할 수 있다.
- 완화:
  - 각 Stage의 주 압력은 하나만 둔다.
  - Wave 1에서 안전한 단일 사례를 먼저 보여준다.
  - Stage 4 Danger는 침투 Route 공개라는 한 규칙만 사용한다.
  - 정확한 Stage 길이는 첫 10~15분 Decision과 사람 검증에서 조정한다.

### OMW-AUD-382 — 압력 태그가 이름만 다르고 실제 플레이는 같음

- 공격: 체력·수량만 바꾼 뒤 태그만 달면 다섯 압력이 실질적으로 동일하다.
- 완화: 각 압력은 Route, 우선 목표, 화면 밀도, 공격 가능 Layer 중 하나 이상이 달라야 한다.

### OMW-AUD-383 — 고정 20 Stage가 한 번 풀면 끝나는 퍼즐이 됨

- 공격: 모든 적과 전선이 완전히 고정되면 반복 플레이가 암기화된다.
- 완화:
  - 압력 역할·학습 목표는 고정.
  - 실제 적 패키지와 전선 배치는 맵별 작성 변형.
  - 변형은 Stage 시작 전에 전부 공개.
  - 같은 막에서 동일 패키지 반복 금지.

### OMW-AUD-384 — 반대로 무작위가 압력 정체성을 파괴

- 공격: 리플레이성을 위해 Stage 시작 뒤 적 패키지·주 전선·필요 카운터를 바꾸면 공정성이 무너진다.
- 완화: Stage 시작 뒤 압력 정체성과 치명적 행동을 바꾸지 않는다.

### OMW-AUD-385 — 세 압력 조합이 화면 가독성을 파괴

- 공격: Stage 16~19가 세 전선·공중·우회·공성을 모두 겹치면 무엇이 중요한지 읽히지 않는다.
- 완화:
  - 각 전선에 역할을 분리한다.
  - 결정 전선과 가장 위험한 목표를 강조한다.
  - Final Boss는 Pattern별로 핵심 압력을 나눈다.

### OMW-AUD-386 — 모든 Stage가 3 Wave라 리듬이 단조로움

- 공격: 동일한 3 Wave 숫자가 기계적 반복을 만든다.
- 판정: 유효하지만 현재 3개는 Spawn 수가 아니라 콘텐츠 Beat 기준선이다.
- 완화: 각 Beat 내부의 적 묶음·간격·지속시간은 Stage와 맵에 따라 달라질 수 있다. 정확한 Wave 수 변경은 시뮬레이션 근거가 있을 때만 재결정한다.

## 5. P1 공격 — Danger

### OMW-AUD-387 — Stage 9와 Stage 19가 둘 다 겹침으로 느껴짐

- Stage 9 핵심: **시간표 겹침**. 이전 Wave 잔존 중 다음 Wave 시작.
- Stage 19 핵심: **Route 수렴**. 서로 다른 출발 전선이 한 결정 전선으로 모임.
- 두 Stage는 시간 압박과 공간 해석으로 구분한다.

### OMW-AUD-388 — Stage 14가 비가역 배치를 과도하게 처벌

- 완화:
  - 세 Wave 전체 순서를 Stage 시작 전에 공개.
  - 각 Wave는 이전 배치를 완전히 무효화하지 않고 보조 압력을 남긴다.
  - 주 전선이 바뀌더라도 기존 전선의 병력이 가치 있는 잔존 전투를 수행해야 한다.

### OMW-AUD-389 — Danger 보상이 필수 파밍이 됨

- 조치: 위험 보상은 높되 반복 파밍·의도적 지연으로 무한 성장할 수 없게 한다. 정확한 보상 계약은 상인·경제 Decision으로 이관.

## 6. P1 공격 — Boss

### OMW-AUD-390 — Boss가 태세 이름만 바뀐 HP Sponge

- 완화: 각 Boss는 Route·목표·호위·집중 공격 기회 중 최소 두 요소를 실제로 변경해야 한다.

### OMW-AUD-391 — Boss 전용 규칙이 코어를 대체

- 공격: 별도 미니게임·QTE·전용 퍼즐이 룰렛·건물·전선 선택을 무의미하게 만들 수 있다.
- 조치: Boss 규칙은 기존 Route·Target·전선 커밋을 재해석해야 하며 별도 게임으로 분리하지 않는다.

### OMW-AUD-392 — Final Boss가 다섯 압력을 한꺼번에 쏟음

- 완화: 세 Omen Pattern으로 분리하고 다음 Pattern을 전환 전에 공개한다.

### OMW-AUD-393 — Boss 보상이 순수 수치 증가

- 조치: 다음 막의 압력에 맞춰 런 방향을 바꿀 수 있는 재조정 기회를 제공해야 한다. 정확한 항목은 상인·경제 Decision에서 확정.

## 7. P2 공격 — 역할·구현 경계

### OMW-AUD-394 — GPT가 정확한 Spawn 초·개체 수를 조기 고정

- 조치: Stage 역할·압력·Wave Beat만 정본. Spawn 초·수량·Threat Budget은 시뮬레이션과 Codex 콘텐츠 데이터 설계에 위임.

### OMW-AUD-395 — 실제 카운터가 없는 압력을 먼저 구현

- 조치: 제품 구현 전에 건물 T2/T3와 병종 역할 Decision이 각 압력에 최소 두 대응 경로를 제공하는지 확인.

### OMW-AUD-396 — 맵별 변형 알고리즘을 기획 정본으로 고정

- 조치: 작성 규칙과 플레이어 약속만 정본화한다. 선택 알고리즘·시드·데이터 구조는 Codex가 결정.

### OMW-AUD-397 — Stage 이름을 최종 세계관 이름으로 오해

- 조치: 현재 이름은 기능 식별용 가칭이다. 세계관 지역·Boss 이름은 콘텐츠·아트 제작 단계에서 현행 명명 규칙에 맞춰 확정.

## 8. 더 나은 방향 검토

### 대안 A — 완전 고정 20 Stage

장점: 학습 통제와 밸런스가 쉽다.

단점: 반복 플레이가 암기화된다.

판정: 단독 채택하지 않는다.

### 대안 B — 매 런 완전 무작위 Stage

장점: 겉보기 다양성이 높다.

단점: 필요한 카운터와 압력을 예측하기 어렵고 핵심 재미가 운에 종속된다.

판정: 폐기.

### 채택안 — 고정 압력 역할 + 맵별 작성 변형

장점:

- 핵심 학습 곡선 유지.
- 맵마다 적 패키지·Route·전선 배치 변화.
- Stage 시작 전 완전 공개로 공정성 유지.
- 후속 맵 제작 시 같은 20 Stage 뼈대를 재사용 가능.

판정: 최적안.

## 9. 다음 작업 순서

Stage 매트릭스가 정의한 요구를 다음 Decision이 실제 콘텐츠로 채운다.

```text
건물 6종 T2/T3 분기·카운터
→ 병종 역할·시너지·카운터
→ 마석·전술스킬
→ Stage 종료 상인
→ 첫 10~15분 사람 검증 흐름
```

Hero·Meta는 위 기본 Run 콘텐츠가 연결되기 전 재개하지 않는다.

## 10. PR 검수 결과

- [x] 새 Stage 압력 정본이 Documentation Map·Lifecycle Registry에 연결됨.
- [x] `15웨이브=1스테이지` 구형 문서가 `[대체됨]`으로 표시됨.
- [x] 구형 첫 4공세 밸런스가 `[보류]`로 표시됨.
- [x] Vertical Slice 구형 세부에 최신 Overlay·부분 승계 경계가 표시됨.
- [x] 현재 GDD·Project Core·Pending·Roadmap이 2/10을 동일하게 말함.
- [x] Google Sheet가 같은 Decision ID와 exact PR HEAD를 기록함.
- [x] 제품 코드·실제 자산 변경 0.
- [x] CI 3종 Green: Project Core 882 / GDD Sheet 594 / Base v9 576.
- [x] main 대비 ahead 19 / behind 0.
- [x] 리뷰 0 / 미해결 Thread 0.
- [x] `OPEN_P0`·`OPEN_P1`·`MERGE_BLOCKER` 0.
- [x] 미완성 `TODO/TBD` 0.
- [x] Sheet bounded read-back PASS.

## 11. Blocker 판정

```text
BLOCKER_BEFORE_CANON_SYNC = TRUE
DOCUMENT_PR_BLOCKER_AFTER_CANON_SYNC = FALSE
PRODUCT_IMPLEMENTATION_BLOCKER = TRUE_UNTIL_BUILDING_AND_TROOP_COUNTER_DECISIONS
PRODUCT_CODE = UNCHANGED
SHEET_READBACK = PASS
CI_3_GREEN = TRUE
SIMULATION = NOT_RUN
HUMAN_QA = NOT_RUN
```
