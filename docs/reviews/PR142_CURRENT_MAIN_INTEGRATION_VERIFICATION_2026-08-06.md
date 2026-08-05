# PR #142 최신 main 통합 검증

```yaml
decision_id: OMW-DEC-20260806-PLANNING-UNIT-BUILDING-TIER-MATRIX-V1
verified_at: 2026-08-06 KST
scope: PR142_CURRENT_MAIN_INTEGRATION
product_change: NONE
result: BRANCH_ANCESTRY_RESOLVED / FULL_SUITE_PENDING
```

## 1. 통합 계보

```text
PREVIOUS_PR_HEAD = 67c0bd03df4bd0215bf6bc94b9e06cd5b6201b56
CURRENT_MAIN_PARENT = aea0cf667e7c6fc5d4b9924cf9bb1ffc9eeddbe6
TWO_PARENT_MERGE_COMMIT = 7ac604443156f9aa8f1fc26431c0e581bd0d2dd9
MERGE_TREE = 6b8e64a674d579ff4a5da37ae0acbb793d22c8ea
```

두 parent가 Git commit API read-back으로 확인됐다.

## 2. 충돌 범위

공통 merge base 이후 양쪽이 함께 수정한 파일은 다음 두 개였다.

- `AGENTS.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`

두 문서는 다음 내용을 모두 보존하도록 수동 통합했다.

- 7/10 첫 10~15분 기획 상태.
- 건물 Tier 재정렬과 `SPECIAL_T1_TOKEN_SOURCE = NONE`.
- 궁병 T3 석궁병·연사궁병 2분기와 대공궁병 폐기.
- PC·Android 공용 코어·어댑터 설계 경계.
- Phase 0 무료 로컬 정적 검사·특성화 증거.
- 제품 코드 권한 없음과 출시 Gate 미실행 상태.

최신 main의 나머지 플랫폼 파일은 main의 Git blob SHA를 그대로 사용했다.

## 3. 브랜치 비교

```text
BASE = aea0cf667e7c6fc5d4b9924cf9bb1ffc9eeddbe6
MERGED_HEAD = 7ac604443156f9aa8f1fc26431c0e581bd0d2dd9
COMPARE_STATUS = AHEAD
AHEAD_BY = 107
BEHIND_BY = 0
MERGE_BASE = BASE
MAIN_IS_HEAD_ANCESTOR = PASS
```

따라서 이전 `DIVERGED / BEHIND_21` 계보 문제는 해소됐다.

## 4. 궁병 계약 테스트

원격 Git blob과 로컬 재구성 파일의 SHA 일치를 먼저 확인했다.

```text
ARCHER_AUTHORITY_BLOB = f329c1907d468173b05c10d49814b06373a80a37 / MATCH
ARCHER_REVIEW_BLOB = a352658c975a0e5d13504bf381bfb264642ae8d3 / MATCH
ARCHER_TEST_BLOB = 77ed02c5f6f5c1586c22443fca92d09fab6d7a85 / MATCH
```

실행 결과:

```text
python -m unittest -v tests/python/test_archer_t3_two_branch_canon.py
RESULT = 7 PASS / 0 FAIL / 0 ERROR

python -m py_compile tests/python/test_archer_t3_two_branch_canon.py
RESULT = EXIT 0
```

## 5. 검증 한계

```text
FULL_REPOSITORY_CHECKOUT = UNAVAILABLE_IN_EXECUTION_ENVIRONMENT
FULL_PLANNING_CONTRACT_SUITE = NOT_RUN
GITHUB_HEAD_COMBINED_STATUSES = NONE_RETURNED
GITHUB_ACTIONS_GREEN = NOT_PROVEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

GitHub compare API는 `behind=0`을 반환하지만 PR mergeability API가 직전 조회에서 `dirty`를 반환했다. 새 HEAD 생성 후 재조회하며, 해소되지 않으면 provider mergeability 불일치로 계속 차단한다.

## 6. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
EXACT_NUMERICS = PENDING_SIMULATION
```

이 검증은 PR 병합 승인이나 제품 구현 완료를 뜻하지 않는다.
