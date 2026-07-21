# Legacy Artifact Reconciliation

| Current path | Responsibility | Canonical replacement | Unique information | Active references | Decision | Approval | Validation | Rollback |
|---|---|---|---|---|---|---|---|---|

Allowed decisions:

- `CURRENT`
- `UPDATE_IN_PLACE`
- `MERGE_TO_CANONICAL`
- `COMPATIBILITY_STUB`
- `ARCHIVE_HISTORY`
- `DELETE_APPROVED`
- `KEEP_UNRESOLVED`

## Required order

```text
inventory·hash·references
→ canonical judgment
→ unique decisions/assets/exceptions/deferred preservation
→ conflict separation
→ approval
→ update/merge/stub/archive/delete
→ Registry·references·tests·derivatives
→ freshness·regression·rollback verification
```

삭제는 고유 정보 승계, 모든 활성 참조 갱신, 파생본·Manifest 검증, 복구 경로, 사용자 승인, freshness 차단 finding 없음이 모두 필요하다.
