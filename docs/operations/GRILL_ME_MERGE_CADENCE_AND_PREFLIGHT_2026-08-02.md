# Grill Me 승인 묶음 병합 주기·사전 검증 프로토콜

```yaml
decision_id: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
approved_at: 2026-08-02 15:09 KST
approval: USER_DIRECT_APPROVAL
status: CURRENT_OPERATING_RULE
current_batch: PR_121
current_grill_me_count: 10
preflight_trigger: REACHED
preflight: CONTENT_PASS / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED_BEFORE_MERGE
preflight_report: docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md
current_merge_authorization: NOT_GRANTED
future_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
product_code_authority: NONE
```

## 1. 목적

승인 기획이 Draft PR과 Sheet에 누적되어 main 정본과 분리되는 문제를 막되, 숫자만 채웠다는 이유로 불완전한 PR을 병합하지 않는다.

```text
승인 Decision 누적
→ 즉시 GitHub·Sheet 동기화
→ 10번째 승인
→ 적대적 preflight
→ blocker 0·최종 exact HEAD Green
→ 사용자 명시적 병합 승인
→ 병합
→ main·Sheet 재동기화
```

## 2. 카운트 규칙

카운트에는 사용자가 승인하고 GitHub·Sheet에 같은 Decision ID로 정본화한 Grill Me만 포함한다. 오타·경로·CI 호환 수정, 적대적 finding, 동일 Decision 보완, 브랜치·병합·Sheet 운영은 제외한다.

## 3. PR #121 승인 10건

1. `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1`
2. `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1`
3. `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1`
4. `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1`
5. `OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1`
6. `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1`
7. `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1`
8. `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1`
9. `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1`
10. `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1`

## 4. 10건의 의미

```text
TEN_APPROVALS = PREFLIGHT_TRIGGER
PREFLIGHT_PASS = MERGE_ELIGIBLE_AFTER_FINAL_HEAD_REVALIDATION
PREFLIGHT_PASS != MERGE_AUTHORIZED
OPEN_P0_OR_P1 = MERGE_BLOCKED
```

- 10번째 승인은 병합 명령이 아니다.
- P0/P1 blocker가 있으면 병합하지 않는다.
- blocker 0이어도 사용자의 별도 병합 승인 전에는 Draft를 유지한다.
- Draft→Ready 전환과 병합은 승인 단계에서만 수행한다.
- auto-merge는 금지한다.

## 5. 필수 검증

### GitHub 권위

- Decision Ledger의 승인 목록·상태·미확정 범위.
- Documentation Map의 책임 원본 존재·Decision ID.
- Legacy·현재 승인·미구현·미검증 경계.
- Vertical Slice·적대적 검토·Evidence Pilot 계보.
- 후속 문서가 이전 결정을 조용히 약화·확대하지 않았는지.

### PR

- Open·Draft·base·head·exact HEAD·mergeability.
- current main 대비 ahead/behind와 merge base.
- changed paths·제품 경로·scope drift.
- 댓글·리뷰·미해결 thread.
- PR 본문의 최신 Decision·Sheet·검증 상태.

### CI

최종 exact PR HEAD에서 다음을 확인한다.

- `Validate Project Core Documentation`
- `Validate Omenward GDD Sheet Adoption`
- `Validate Base v9 adoption`

### Google Sheet

- Workbook ID·25개 탭.
- Hub·작업순서·현재 결정·분야 탭·감사·변경이력.
- 같은 Decision ID·exact HEAD·상태의 bounded read-back.
- `OPEN_P0`, `OPEN_P1`, `MERGE_BLOCKER` 검색.

## 6. PR #121 preflight 결과

주 책임 보고서:

`docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md`

후보 증거 HEAD `be552b54b96a029dfa042675ae002ad21b96af65`:

```text
CONTENT_PREFLIGHT = PASS
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
PRODUCT_PATHS = 0
BEHIND_MAIN = 0
COMMENTS = 0
REVIEWS = 0
UNRESOLVED_THREADS = 0
```

필수 CI:

```text
Project Core Documentation run 615 = PASS
GDD Sheet Adoption run 332 = PASS
Base v9 adoption run 308 = PASS
```

해결된 주요 finding:

- latest main Base v9.4.1 ancestry 누락 → main→feature PR #124로 해결.
- Documentation Map의 Vertical Slice·review·Evidence Pilot 계보 누락 → 복원 후 Core CI Green.
- 과거 PR #116 `OPEN_P1` CI 행 → 역사적 해결 상태로 전환.
- 제품 구현 전 parser·simulation·fault test → `TEST_REQUIRED`로 유지하되 문서-only 병합 blocker와 분리.

## 7. 병합 방식

- 문서·기획 묶음 기본 권장은 `squash`다.
- 병합 직전 expected HEAD를 고정한다.
- HEAD가 움직이면 필수 CI·compare·review·Sheet exact HEAD를 다시 확인한다.
- 사용자 승인 후에만 Draft를 Ready로 전환하고 병합한다.
- 현재 PR #121의 사용자 병합 승인은 없다.

## 8. 병합 차단 조건

```text
OPEN_P0_OR_P1
MISSING_AUTHORITY_FILE
DECISION_ID_MISMATCH
SHEET_GITHUB_DIVERGENCE
REQUIRED_CI_NOT_GREEN
UNRESOLVED_REVIEW_THREAD
MERGE_CONFLICT
UNDECLARED_PRODUCT_PATH_CHANGE
STALE_EXACT_HEAD
```

## 9. 병합 직후 작업

- merged 상태와 merge commit 확인.
- main HEAD·정본 파일 재조회.
- Sheet를 `SYNCED_TO_MAIN / MERGE_VERIFIED`로 갱신.
- 카운터를 `0/10`으로 초기화.
- 새 branch·새 Draft PR에서 다음 묶음 시작.

## 10. 현재 상태

```text
CURRENT_BATCH = PR_121
CURRENT_GRILL_ME_COUNT = 10_OF_10
CONTENT_PREFLIGHT = PASS
FINAL_EXACT_HEAD_REVALIDATION = REQUIRED_BEFORE_MERGE
CURRENT_USER_MERGE_AUTHORIZATION = NO
DRAFT_MUST_REMAIN = TRUE
AUTO_MERGE = FORBIDDEN
POST_MERGE_NEXT_COUNT = 0_OF_10
```
