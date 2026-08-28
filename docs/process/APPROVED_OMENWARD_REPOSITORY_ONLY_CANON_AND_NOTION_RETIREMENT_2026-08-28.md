# [현행 운영] OMENWARD Repository 정본화와 Notion 사용 중단

```yaml
decision_id: OMW-OPS-20260828-REPOSITORY-ONLY-CANON-NOTION-RETIREMENT-01
approved_at: 2026-08-28 KST
approval: USER_APPROVED
status: CURRENT_OPERATING_POLICY
scope: DOCUMENTATION / DECISION / VISUAL_PLANNING / ASSET_PROVENANCE / HANDOFF
product_code_authority: NONE
notion_write: FORBIDDEN_UNTIL_USER_REENABLES
notion_delete: FORBIDDEN
notion_read: USER_APPROVED_READ_ONLY_MIGRATION__COMPLETE
```

## 결정

```text
REPOSITORY_HUMAN_FACING_CANON = Markdown owners under docs/ + README.md
REPOSITORY_STRUCTURED_CANON = Markdown / JSON / code / data / Scene / Resource / test / runtime evidence
GITHUB_LIVE_STATE = FRESH_QUERY_REQUIRED
NOTION_CURRENT_AUTHORITY = RETIRED
NOTION_FUTURE_READ_OR_WRITE = FORBIDDEN_UNTIL_USER_REENABLES
NOTION_HISTORICAL_RECORDS = PRESERVE_READ_ONLY_HISTORY
NOTION_DESTINATION_READBACK = NOT_REQUIRED
NOTION_MIGRATION_READ = COMPLETE__USER_APPROVED_READ_ONLY
NOTION_MIGRATION_REPORT = docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md
```

이 정책 이후 의미 있는 기획·시각·자산·구현 증거는 repository의 명시된 owner에만 기록한다. Notion의 기존 Home, Direction, Flow, Visual Bible, Asset page는 과거 시점의 기록으로 보존하지만, 새 정본·승인·자산·runtime evidence의 source of truth가 아니다.

사용자는 2026-08-28에 기존 Notion의 현재 구조와 작업 연결을 저장소로 옮기기 위한 **읽기 전용 1회 migration**을 승인했다. 해당 readback은 `docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md`에 기록한다. 이 예외는 Notion write/delete 또는 이후 routine read 권한을 만들지 않는다.

## 작업 규칙

- Notion 페이지를 수정·삭제·새로 만들지 않는다.
- 과거 Notion attachment/readback은 당시 사실을 보여주는 **historical evidence**일 뿐, 현재 usability·approval·runtime PASS가 아니다.
- 사용자에게 보여 줄 계획서·Flow·Visual Bible·Asset provenance는 repository Markdown과 GitHub PR/Issue에서 관리한다.
- 이미지 생성은 `USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES`에 따라 먼저 생성하고, 사용자에게는 생성 후 **Visual Lock 여부만** 요청한다. 새 이미지의 provenance, prompt, source hash, consumer, rights state는 repository에 기록한다.
- 이 정책은 프로젝트 운영 방식이므로 Base 공용 규칙으로 승격하지 않는다.

```text
NO_BASE_PROMOTION = USER_SELECTED_PROJECT_TOOLING_BOUNDARY
```
