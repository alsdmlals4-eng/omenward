# 체크포인트 9 검증 — 벨루 개입·실패·재시도·스킵

```yaml
decision_id: OMW-DEC-20260806-PLANNING-BELU-INTERVENTION-FAILURE-RETRY-SKIP-RULES-V1
verified_at: 2026-08-06 KST
scope: BOUNDED_REMOTE_MARKER_CONTRACT
```

## RED

```text
RED_COMMIT = f600318eb6df4adbd7d5c77bd63cd74d24252e3c
RED_EXPECTATION = AUTHORITY_REVIEW_SPEC_ABSENT
```

테스트 계약을 책임 원본보다 먼저 추가했다. 새 책임 원본이 없는 상태에서는 파일 존재와 marker 검사가 실패하는 것이 정상이다.

## GREEN

원격 read-back으로 확인한 blob:

```text
AUTHORITY_BLOB = 0498f8b683f1b52b7e47444105d85b2fafc5a99d
REVIEW_BLOB = c9f61a18fad0cee50ed6d568910f1bab42e297c9
SPEC_BLOB = 5fe9ec94870d7d24df54bc5a966f0073c64afa95
```

동일 내용을 제한된 로컬 트리에 재구성해 실행했다.

```text
CHECKPOINT_9_BOUNDED_CONTRACT = 9_PASS / 0_FAIL / 0_ERROR
PY_COMPILE_EXIT = 0
```

Python 시작 과정에서 artifact spreadsheet warm-up 경고가 stderr에 출력됐지만 unittest와 py_compile의 종료 코드는 모두 0이었다.

## 검증 한계

```text
FULL_PRIVATE_REPOSITORY_CHECKOUT = UNAVAILABLE
EXACT_HEAD_FULL_TEST_EXECUTION = NOT_RUN
FULL_PLANNING_CONTRACT_SUITE = NOT_RUN
FRESH_GODOT_TEST_ON_CURRENT_HEAD = NOT_RUN
GITHUB_ACTIONS_GREEN = NOT_PROVEN
AUTOMATED_GREEN = NOT_PROVEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

9 PASS는 체크포인트 9 문서 marker 계약에만 적용한다. 실제 체크포인트 저장·복구·스킵·벨루 UI 동작을 검증한 결과가 아니다.
