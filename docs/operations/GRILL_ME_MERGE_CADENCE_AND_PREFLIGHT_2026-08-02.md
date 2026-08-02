# Grill Me 승인 묶음 병합 주기·사전 검증 프로토콜

```yaml
decision_id: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
approved_at: 2026-08-02 15:09 KST
approval: USER_DIRECT_APPROVAL
status: CURRENT_OPERATING_RULE
current_batch: PR_121
current_grill_me_count: 10
preflight_trigger: REACHED
preflight: REQUIRED_IN_PROGRESS
current_merge_authorization: NOT_GRANTED
future_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
product_code_authority: NONE
```

## 1. 목적

승인된 기획이 Draft PR과 Sheet에 장기간 누적되어 main 정본과 분리되는 문제를 막되, 숫자만 채웠다는 이유로 불완전한 PR을 강제 병합하지 않는다.

```text
승인 Decision 누적
→ 즉시 GitHub·Sheet 동기화
→ 10번째 Grill Me 승인
→ 적대적 병합 사전 검증
→ blocker 0 + 사용자 명시적 병합 승인
→ 병합
→ main·Sheet 재동기화
→ 새 branch·새 Draft PR에서 다음 묶음 시작
```

## 2. 카운트 규칙

카운트 단위는 사용자에게 한 번에 하나씩 제시되고 사용자가 승인한 Grill Me Decision ID다.

포함:

- 선택지와 권장안을 제시한 Grill Me 질문.
- 사용자가 `권장안대로`, 번호 선택 또는 수정안으로 승인한 Decision.
- GitHub·Sheet에 같은 Decision ID로 정본화된 항목.

제외:

- 오타·경로·상태·CI 호환 수정.
- 적대적 finding만 추가한 작업.
- 이미 카운트된 Decision의 문구 보완.
- 병합·브랜치·Sheet 동기화 같은 운영 작업.

## 3. PR #121 현재 10건

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
APPROVAL_COUNT_REACHED = PREFLIGHT_REQUIRED
PREFLIGHT_PASS = MERGE_ELIGIBLE
PREFLIGHT_PASS != MERGE_AUTHORIZED
OPEN_P0_OR_P1 = MERGE_BLOCKED
```

- 10번째 승인은 무조건 병합 명령이 아니라 preflight 시작 트리거다.
- P0/P1 blocker가 있으면 병합하지 않는다.
- blocker를 수정하고 동일 preflight를 다시 통과해야 한다.
- blocker 0이어도 사용자의 명시적 병합 승인 전에는 병합하지 않는다.
- Draft→Ready 전환도 병합 승인 단계에서만 수행한다.
- 자동 병합과 auto-merge 설정은 금지한다.

## 5. 필수 GitHub 검증

### 5.1 권위·내용

- 최신 사용자 승인 Decision 목록과 Decision Ledger 대조.
- Documentation Map의 책임 원본 경로 존재 확인.
- 역사 PR에만 있는 문서를 current authority처럼 가리키는 참조 탐지.
- CURRENT_CANON·CURRENT_IMPLEMENTATION·LEGACY·REJECTED·PENDING 구분 확인.
- Decision ID·상태·대체 관계·미확정 범위 확인.
- 미검증 수치가 제품 확정값으로 잘못 승격되지 않았는지 확인.
- 최신 승인 규칙이 이전 결정을 조용히 약화·확대하지 않았는지 확인.

### 5.2 PR

- state·draft·base·head·exact HEAD 확인.
- main 대비 ahead/behind·mergeability·충돌 확인.
- 전체 changed paths와 제품 경로 변경 여부 확인.
- PR 설명이 최신 Decision·Sheet 범위·검증 결과를 포함하는지 확인.
- 댓글·리뷰·미해결 inline thread 전수 확인.
- scope drift·폐기 자료 혼입·동일 내용 중복 커밋 위험 확인.

### 5.3 CI

exact PR HEAD에서 다음 workflow를 새로 확인한다.

- `Validate Project Core Documentation`
- `Validate Omenward GDD Sheet Adoption`
- `Validate Base v9 adoption`

하나라도 없거나 queued·in_progress·failure·cancelled면 병합할 수 없다.

## 6. 필수 Google Sheet 검증

- Workbook ID와 25개 필수 탭 확인.
- `00_프로젝트_허브` 현재 단계·다음 Gate·exact PR HEAD 확인.
- `01_작업순서` 승인 순서와 선행·후속 관계 확인.
- `02_현재_확정결정` Decision ID·정본 경로·PR surface 확인.
- 분야 탭의 승인 내용·금지선 확인.
- `04_누락_충돌_감사`의 열린 P0/P1·MERGE_BLOCKER 확인.
- `99_변경이력` GitHub path·HEAD·Sheet 범위·read-back 확인.
- Sheet-only 변경이 `PROPOSED_SHEET_CHANGE` 없이 정본으로 승격되지 않았는지 확인.
- GitHub·Sheet의 같은 Decision ID·문구·상태·exact HEAD를 bounded read-back으로 재검증.

## 7. 적대적 공격 질문

1. 승인 내용 중 GitHub나 Sheet 한쪽에만 있는 항목이 있는가?
2. 책임 원본이 실제로 존재하지 않거나 역사 PR에만 남아 있는가?
3. 후속 문서가 이전 결정을 조용히 약화·확대했는가?
4. Legacy 구현을 승인 제품으로 오인하게 만드는 표현이 있는가?
5. 미검증 수치·성능·아트·서사가 완료 상태로 표시됐는가?
6. Hero 해금·자동 능력·Meta가 pay/grind-to-win 또는 원본 사장을 만드는가?
7. 폐기·실패 증거가 삭제되거나 `NOT_CREATED`로 되돌아갔는가?
8. 병합 뒤 main에서 branch·PR·pending 표현이 즉시 낡게 되는가?
9. 새 작업자가 Documentation Map만 읽고 다음 작업을 찾을 수 있는가?
10. 롤백 시 어떤 commit·Decision·Sheet 범위를 되돌려야 하는가?

모든 finding은 `RESOLVED`, `ACCEPTED_RISK`, `TEST_REQUIRED`, `USER_DECISION_REQUIRED`, `MERGE_BLOCKER` 중 하나로 분류한다.

## 8. 병합 방식

- 문서·기획 묶음의 기본 권장 방식은 `squash`다.
- 병합 직전 exact HEAD를 고정하고 expected HEAD가 움직이면 preflight를 다시 수행한다.
- PR이 Draft이면 사용자 병합 승인 후 Ready로 전환한다.
- 제품 코드가 포함된 PR은 이 문서만으로 병합하지 않는다.
- 현재 PR #121은 문서-only 기획 묶음이지만 **사용자 병합 승인은 아직 없다**.

## 9. 병합 직후 필수 작업

- `merged=true`와 merge commit 확인.
- main HEAD와 변경 경로 재조회.
- 필수 정본 파일이 main에서 읽히는지 확인.
- Sheet의 PR head를 merged main SHA로 교체.
- `SYNCED_TO_MAIN / MERGE_VERIFIED` bounded read-back.
- Grill Me 카운터를 `0/10`으로 초기화.
- 새 branch·새 Draft PR에서 다음 묶음을 시작.
- 병합된 PR branch를 후속 작업에 재사용하지 않는다.

## 10. 병합 차단 조건

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

## 11. 현재 상태

```text
CURRENT_BATCH: PR_121
CURRENT_GRILL_ME_COUNT: 10_OF_10
PREFLIGHT_TRIGGER: REACHED
PREFLIGHT: REQUIRED_IN_PROGRESS
CURRENT_USER_MERGE_AUTHORIZATION: NO
AUTO_MERGE: FORBIDDEN
POST_MERGE_NEXT_COUNT: 0_OF_10
```
