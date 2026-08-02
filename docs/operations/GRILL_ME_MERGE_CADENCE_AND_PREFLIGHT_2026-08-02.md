# Grill Me 승인 묶음 병합 주기·사전 검증 프로토콜

```yaml
decision_id: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
approved_at: 2026-08-02 15:09 KST
updated_at: 2026-08-02 20:18 KST
approval: USER_DIRECT_APPROVAL_WITH_STANDING_MERGE_AUTHORIZATION
status: CURRENT_OPERATING_RULE
last_completed_batch: PR_121
last_merge_commit: 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
current_batch: NEXT_BATCH_NOT_OPENED
current_grill_me_count: 0
next_preflight_at: 10
future_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_authorization: STANDING_USER_AUTHORIZATION
product_code_merge_authorization: NOT_GRANTED_BY_THIS_RULE
product_code_authority: NONE
```

## 1. 목적

승인 기획이 Draft PR과 Sheet에 누적되어 main 정본과 분리되는 문제를 막고, 10건 단위로 적대적 검토·검증·병합·main/Sheet 동기화를 반복한다.

```text
승인 Decision 누적
→ 즉시 GitHub·Sheet 동기화
→ 10번째 승인
→ 적대적 preflight
→ blocker 수정·재검증
→ Green exact HEAD 고정
→ Ready 전환·직접 병합
→ main·Sheet 재동기화
→ 카운터 0/10
```

## 2. 카운트 규칙

포함:

- 사용자가 승인한 Grill Me Decision ID.
- GitHub·Sheet에 같은 Decision ID로 정본화된 결정.

제외:

- 오타·경로·상태·CI 호환 수정.
- 적대적 finding만 추가한 작업.
- 이미 카운트된 Decision의 문구 보완.
- 브랜치·병합·Sheet 동기화 같은 운영 작업.

## 3. standing authorization 범위

사용자는 2026-08-02 20:18 KST에 같은 작업에 대해 승인 대기 없이 적대적 검토·PR 체크·병합까지 진행하도록 지시했다.

이 standing authorization은 다음 조건을 모두 만족하는 **문서·기획 PR**에 적용한다.

```text
latest main ancestry synced
required CI green at exact HEAD
Sheet bounded read-back pass
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
unresolved review threads = 0
undeclared product paths = 0
merge conflict = false
```

조건을 만족하면 별도 승인 질문 없이 다음을 수행한다.

1. Draft PR을 Ready로 전환한다.
2. expected HEAD를 고정한다.
3. repo 기본 권장 방식으로 직접 병합한다.
4. main과 Sheet를 merged SHA로 재동기화한다.
5. 카운터를 `0/10`으로 초기화한다.

## 4. standing authorization 제외 범위

다음은 자동 확장하지 않는다.

- 제품 코드·데이터·Scene·Resource 변경 PR.
- 결제·보안·개인정보·법률·배포·Release 권한 변경.
- 기존 승인 제품 코어를 약화하거나 뒤집는 변경.
- 사용자가 중단·보류·검토 대기를 명시한 작업.

위 범위는 별도 작업 계약 또는 사용자 지시가 필요하다.

## 5. 적대적 preflight

### GitHub 권위

- Decision Ledger와 Documentation Map의 책임 원본을 대조한다.
- Legacy·승인 기획·구현·미검증 경계를 확인한다.
- 역사 PR·Evidence Pilot이 current canon으로 오인되지 않는지 확인한다.
- 후속 문서가 이전 결정을 조용히 약화·확대하지 않는지 확인한다.

### PR

- state·draft·base·head·exact HEAD·mergeability.
- current main 대비 ahead/behind와 merge base.
- changed paths·제품 경로·scope drift.
- 댓글·리뷰·미해결 thread.
- PR 본문의 Decision·Sheet·검증 상태.

### CI

- `Validate Project Core Documentation`
- `Validate Omenward GDD Sheet Adoption`
- `Validate Base v9 adoption`
- Base release가 추가한 관련 필수 workflow.

### Google Sheet

- Hub·작업순서·현재 결정·분야 탭·감사·변경이력.
- 같은 Decision ID·exact HEAD·상태의 bounded read-back.
- `OPEN_P0`, `OPEN_P1`, `MERGE_BLOCKER` 검색.

## 6. blocker 처리

blocker가 있으면 승인 질문으로 되돌리지 않는다.

```text
finding 기록
→ 원인 확인
→ 정본·Sheet·CI 수정
→ exact HEAD 재고정
→ 전체 preflight 반복
```

해결할 수 없거나 결정 충돌이 실제로 존재하면 병합을 중단하고 사용자에게 blocker와 필요한 결정만 보고한다.

## 7. 병합 방식

- 문서·기획 묶음 기본 권장은 `squash`다.
- GitHub auto-merge 기능은 사용하지 않는다.
- expected HEAD가 움직이면 병합하지 않고 preflight를 반복한다.
- 병합 뒤 main 파일 존재·merged 상태·merge commit을 다시 확인한다.

## 8. PR #121 완료 증거

```text
PR = 121
APPROVED_DECISIONS = 10
PR_HEAD = 79cb43b71d0072374a9586bb66dd4a24c3b069a9
MERGE_METHOD = SQUASH
MERGE_COMMIT = 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
Project Core run 630 = PASS
GDD Sheet run 347 = PASS
Base v9 run 324 = PASS
BEHIND_MAIN = 0
PRODUCT_PATHS = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
```

## 9. 현재 상태

```text
LAST_COMPLETED_BATCH = PR_121
CURRENT_COUNT = 0_OF_10
CURRENT_PR = NONE
NEXT_GATE = NEXT_PLANNING_BATCH_SELECTION
PLANNING_DOCS_STANDING_AUTHORIZATION = ACTIVE
PRODUCT_CODE_STANDING_AUTHORIZATION = INACTIVE
```
