# PR #142 최신 main 통합 검증

```yaml
decision_id: OMW-DEC-20260806-PLANNING-UNIT-BUILDING-TIER-MATRIX-V1
verified_at: 2026-08-06 KST
scope: PR142_CURRENT_MAIN_INTEGRATION
product_change: NONE
result: LATEST_MAIN_TREE_INTEGRATED / FULL_SUITE_PENDING
```

## 1. 통합 이력

첫 통합 시점의 main은 `aea0cf667e7c6fc5d4b9924cf9bb1ffc9eeddbe6`이었으며, 기획 branch와의 실제 중복 파일은 다음 두 개였다.

- `AGENTS.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`

두 문서를 수동 통합한 뒤 원래 108커밋 계보는 다음 보존 브랜치에 남겼다.

```text
ARCHIVE_BRANCH = archive/pr142-pre-linear-rebase-20260806
ARCHIVED_HEAD = d500428e12c5ff4c148fabf00556e8996fcacfde
```

그 뒤 main이 Phase 1 플랫폼 계약 merge로 다시 이동했다.

```text
LATEST_MAIN = 32e4482119812c1da62bb909350d2f87087785b3
LATEST_MAIN_CHANGE = OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1
```

## 2. 최신 main 추가 변경 처리

`aea0cf66… → 32e44821…` 구간은 9커밋, 15파일이다.

현행 기획 tree와 의미상 겹치는 파일:

- `docs/CURRENT_IMPLEMENTATION_STATUS.md` — 수동 통합.
- `scripts/platform/README.md` — 기획 branch의 독자 변경이 아니므로 최신 main blob을 그대로 채택.

나머지 Phase 1 파일도 최신 main Git blob을 그대로 사용한다.

보존 범위:

- Phase 1 `GameCommand`, `GameEvent`.
- 7개 플랫폼 base contract와 `PlatformCapabilities`.
- Phase 1 책임 원본·적대적 검토·구현 계획.
- Godot contract test.
- 7/10 첫 10~15분 기획.
- 건물 Tier 재정렬과 `SPECIAL_T1_TOKEN_SOURCE = NONE`.
- 궁병 T3 석궁병·연사궁병 2분기와 대공궁병 폐기.

## 3. 궁병 계약 테스트

원격 Git blob과 로컬 재구성 파일의 SHA를 일치시킨 뒤 테스트했다.

```text
ARCHER_AUTHORITY_BLOB = f329c1907d468173b05c10d49814b06373a80a37 / MATCH
ARCHER_REVIEW_BLOB = a352658c975a0e5d13504bf381bfb264642ae8d3 / MATCH
ARCHER_TEST_BLOB = 77ed02c5f6f5c1586c22443fca92d09fab6d7a85 / MATCH
ARCHER_T3_TWO_BRANCH_TEST = 7 PASS / 0 FAIL / 0 ERROR
PY_COMPILE = PASS
```

## 4. 검증 한계

```text
FULL_REPOSITORY_CHECKOUT = UNAVAILABLE_IN_EXECUTION_ENVIRONMENT
FULL_PLANNING_CONTRACT_SUITE = NOT_RUN
FRESH_PHASE1_GODOT_TEST_ON_PR_HEAD = NOT_RUN
GITHUB_ACTIONS_GREEN = NOT_PROVEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

Phase 1 파일은 latest main의 exact Git blobs를 보존하므로 main의 기존 local-pass 증거를 훼손하지 않지만, 이 PR HEAD에서 전체 테스트를 새로 통과했다고 주장하지 않는다.

## 5. 제품 경계

```text
PRODUCT_CODE = UNCHANGED_BY_PLANNING_DECISIONS
GAMEPLAY_SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
EXACT_NUMERICS = PENDING_SIMULATION
```

Phase 1 플랫폼 계약 코드는 latest main에서 이미 canonical이며 이 통합은 해당 코드를 수정하지 않고 그대로 포함한다. 이 문서는 PR 병합 승인이나 제품 구현 완료를 뜻하지 않는다.
