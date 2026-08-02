# Grill Me 승인 묶음 병합 주기·사전 검증 프로토콜

```yaml
decision_id: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
approved_at: 2026-08-02 15:09 KST
approval: USER_DIRECT_APPROVAL
status: CURRENT_OPERATING_RULE
current_merge_authorization: PR_119_APPROVED_FOR_PREFLIGHT_AND_MERGE
future_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
product_code_authority: NONE
```

## 1. 목적

승인된 기획이 Draft PR과 Sheet에 장기간 누적되어 main 정본과 분리되는 문제를 막는다. 동시에 숫자만 채웠다는 이유로 불완전한 PR을 강제 병합하지 않는다.

```text
승인 Decision 누적
→ 즉시 GitHub·Sheet 동기화
→ 10번째 Grill Me 승인
→ 병합 사전 검증
→ blocker 0이면 병합
→ main·Sheet 재동기화
→ 새 브랜치·새 PR에서 다음 묶음 시작
```

## 2. 카운트 규칙

카운트 단위는 사용자에게 한 번에 하나씩 제시되고 사용자가 승인한 **Grill Me Decision ID**다.

포함:

- 선택지·권장안을 제시한 Grill Me 질문.
- 사용자가 `권장안대로`, 번호 선택, 혼합 수정안 등으로 승인한 Decision.
- GitHub·Sheet에 같은 Decision ID로 정본화된 항목.

제외:

- 오타·경로·상태·CI 호환 수정.
- 적대적 검토 finding만 추가한 작업.
- 사용자가 직접 추가한 세부 요구 중 Grill Me 질문이 아니었던 항목.
- 병합·브랜치·Sheet 동기화 같은 운영 작업.
- 이미 카운트된 Decision의 문구 보완.

현재 PR #119에서 카운트되는 Grill Me 승인은 다음 네 건이다.

1. `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1`
2. `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1`
3. `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1`
4. `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1`

사용자가 이번 묶음의 즉시 병합을 명시했으므로 10건 미만이어도 병합 사전 검증을 실행한다. 병합이 확인되면 다음 묶음 카운터는 `0/10`으로 초기화한다.

## 3. 10건의 의미

10번째 승인은 **무조건 병합 명령**이 아니라 **병합 사전 검증을 즉시 시작하는 트리거**다.

```text
APPROVAL_COUNT_REACHED = PREFLIGHT_REQUIRED
PREFLIGHT_PASS = MERGE_ALLOWED
OPEN_P0_OR_P1 = MERGE_BLOCKED
```

- P0/P1 blocker가 있으면 병합하지 않는다.
- 카운터는 `10/10_PENDING_MERGE`로 유지한다.
- blocker를 수정하고 동일 사전 검증을 다시 통과한 뒤 병합한다.
- 사용자의 별도 즉시 병합 지시는 10건 주기를 앞당길 수 있다.
- 사용자의 명시적 보류·병합 금지 지시는 주기보다 우선한다.

## 4. 병합 직전 필수 GitHub 검증

### 4.1 권위·내용

- 최신 사용자 승인 Decision 목록과 Decision Ledger 대조.
- Documentation Map의 현재 책임 원본 경로 존재 확인.
- 로컬에 없는 PR·역사 문서를 현재 책임 원본처럼 가리키는 참조 탐지.
- CURRENT_CANON·CURRENT_IMPLEMENTATION·LEGACY·REJECTED·PENDING 구분 확인.
- 승인 문서의 Decision ID·상태·대체 관계·미확정 범위 확인.
- 정확 수치가 `RECOMMENDED_DEFAULT / TEST_VALUE / PENDING`에서 제품값으로 잘못 승격되지 않았는지 확인.

### 4.2 PR

- PR state·draft 여부·base·head·exact HEAD 확인.
- main 대비 ahead/behind·mergeability·충돌 확인.
- 전체 changed paths와 제품 경로 변경 여부 확인.
- PR 설명이 최신 Decision·Sheet 범위·검증 결과를 포함하는지 확인.
- 리뷰 제출·대화 댓글·미해결 inline thread 전수 확인.
- 불필요한 동일 내용 커밋·scope drift·폐기 자료 혼입 확인.

### 4.3 CI

exact PR HEAD에서 최소 다음을 새로 확인한다.

- `Validate Project Core Documentation`
- `Validate Omenward GDD Sheet Adoption`
- `Validate Base v9 adoption`

필수 workflow가 없거나 queued/in_progress/failure/cancelled이면 병합하지 않는다.

## 5. 병합 직전 필수 Google Sheet 검증

- Workbook ID와 25개 필수 탭 확인.
- `00_프로젝트_허브`의 현재 단계·다음 Gate·exact PR HEAD 확인.
- `01_작업순서`의 승인 순서·선행·후속 관계 확인.
- `02_현재_확정결정`의 Decision ID·정본 경로·PR surface 확인.
- 분야 탭의 실제 승인 내용과 금지선 확인.
- `04_누락_충돌_감사`의 열린 P0/P1 확인.
- `99_변경이력`의 GitHub path·HEAD·Sheet 범위·read-back 확인.
- Sheet-only 변경이 `PROPOSED_SHEET_CHANGE` 없이 정본으로 승격되지 않았는지 확인.
- GitHub와 Sheet의 같은 Decision ID·문구·상태·exact HEAD를 bounded read-back으로 재검증.

## 6. 적대적 검토 루프

병합 직전 최소 다음 공격 질문을 적용한다.

1. 승인 내용 중 GitHub나 Sheet 한쪽에만 있는 항목이 있는가?
2. 책임 원본이 실제로 존재하지 않거나 역사 PR에만 남아 있는가?
3. 후속 문서가 이전 결정을 조용히 약화·확대했는가?
4. 현재 Legacy 구현을 승인 제품으로 오인하게 만드는 표현이 있는가?
5. 미검증 수치·성능·아트·서사가 완료 상태로 표시됐는가?
6. 하나의 기능이 코어 판단을 대체하거나 pay/grind-to-win을 만들 수 있는가?
7. 폐기·거절·실패 증거가 삭제되거나 `NOT_CREATED`로 되돌아갔는가?
8. 병합 뒤 main에서 branch·PR·pending 표현이 즉시 낡게 되는가?
9. 새 작업자가 Documentation Map만 읽고 다음 작업을 정확히 찾을 수 있는가?
10. 롤백 시 어떤 commit·Decision·Sheet 범위를 되돌려야 하는가?

모든 finding은 `RESOLVED`, `ACCEPTED_RISK`, `TEST_REQUIRED`, `USER_DECISION_REQUIRED`, `MERGE_BLOCKER` 중 하나로 분류한다.

## 7. 병합 방식

문서·기획 승인 묶음은 여러 중간 동기화 커밋을 포함할 수 있으므로 기본 권장 병합 방식은 `squash`다.

- 병합 직전 exact HEAD를 고정한다.
- expected head SHA가 달라지면 병합을 중단하고 사전 검증을 다시 수행한다.
- PR이 Draft이면 사전 검증 통과 후 Ready로 전환한다.
- 제품 코드가 포함된 PR은 이 문서만으로 자동 병합하지 않는다.
- 현재 PR #119는 문서·Sheet 정본 복구 및 기획 승인 묶음으로, 사용자 명시 승인과 사전 검증 통과 시 squash 병합한다.

## 8. 병합 직후 필수 작업

- PR의 `merged=true`와 merge commit 확인.
- main HEAD와 병합된 변경 경로 재조회.
- 필수 정본 파일이 main에서 읽히는지 확인.
- Google Sheet의 PR head 표기를 merged main SHA로 교체.
- `SYNCED_TO_MAIN / MERGE_VERIFIED` bounded read-back.
- 다음 Grill Me 카운터를 `0/10`으로 초기화.
- 다음 작업은 새 branch·새 Draft PR에서 시작.
- 병합된 PR을 후속 작업 브랜치로 재사용하지 않는다.

## 9. 병합 차단 조건

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

하나라도 참이면 병합하지 않고 원인·수정 위치·재검증 결과를 기록한다.

## 10. 상태

```text
CURRENT_BATCH: PR_119
CURRENT_GRILL_ME_COUNT: 4
CURRENT_USER_MERGE_AUTHORIZATION: YES
PREFLIGHT: REQUIRED
POST_MERGE_NEXT_COUNT: 0_OF_10
```
