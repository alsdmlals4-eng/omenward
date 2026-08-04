# [대체됨][증거] 픽셀·일러스트 하이브리드 Post-Merge Sync

```yaml
status: SUPERSEDED_MERGE_EVIDENCE_ONLY
superseded_at: 2026-08-04
implementation_authority: NONE
```

이 문서는 PR #133과 #134의 병합 사실·당시 CI·counter reset을 증명하는 역사 자료다.

고정된 merge SHA를 `current_main`으로 기록하면 다음 Sync PR 병합 즉시 값이 낡는 재귀 문제가 발생하므로 현재 상태 권위로 사용하지 않는다.

현행 정책:

- `docs/process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/DOCUMENTATION_MAP.md`

```text
current_main = RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
context_baseline_commit = RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
```

과거 병합 증거는 `last_merged_*`·PR·commit·CI 기록으로만 보존한다.
