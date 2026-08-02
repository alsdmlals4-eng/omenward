# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_gate: NEXT_PLANNING_BATCH_SELECTION
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
pr121_merge_commit: 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
working_branch: NONE
active_base: 9.4.2
last_merged_planning_pr: 121
current_planning_pr: NONE
sheet_status: PROJECT_SHEET_CONFIGURED / SYNCED_TO_MAIN / MERGE_VERIFIED
current_grill_me_count: 0
preflight: PR121_PASS_AND_MERGED
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. GitHub main이 기획 정본이며 Sheet는 같은 Decision ID와 main SHA를 표시한다. `current_main`은 저장소 기본 브랜치에서 실행 시점에 해석하며 `pr121_merge_commit`은 최근 기획 묶음의 역사적 병합 증거다.

## 1. 현재 동기화 상태

```text
PROJECT_SHEET_CONFIGURED
PR #121 = MERGED
MERGE_METHOD = SQUASH
PR121_MERGE_COMMIT = 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
SHEET_STATUS = SYNCED_TO_MAIN / MERGE_VERIFIED
GRILL_ME_COUNTER = 0_OF_10
PRODUCT_STATUS = NOT_IMPLEMENTED
```

## 2. 최근 병합 Decision

- `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1`
- `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1`
- `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1`

## 3. 병합 전 검증 증거

```text
PR_HEAD = 79cb43b71d0072374a9586bb66dd4a24c3b069a9
Project Core Documentation run 630 = PASS
GDD Sheet Adoption run 347 = PASS
Base v9 adoption run 324 = PASS
AHEAD = 117
BEHIND = 0
CHANGED_PATHS = 21_DOCUMENTATION_ONLY
PRODUCT_PATHS = 0
COMMENTS = 0
REVIEWS = 0
UNRESOLVED_THREADS = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
```

## 4. 주요 탭 역할

| 탭 | 역할 |
|---|---|
| `00_프로젝트_허브` | main SHA·현재 단계·카운터·다음 Gate |
| `01_작업순서` | 완료된 묶음과 다음 계획 순서 |
| `02_현재_확정결정` | 승인 Decision·main 정본 경로 |
| `04_누락_충돌_감사` | 열린 P0/P1·blocker·해결 이력 |
| `05_GDD_요약` | 최신 기획·구현 경계·검증 상태 |
| `12_핵심루프` | 핵심 플레이 흐름 |
| `15_조작_게임규칙` | 조작·결정론·금지선 |
| `40_핵심시스템_메인콘텐츠` | 시스템 계약·데이터 구조 |
| `41_성장_경제` | 성장·공정성 경계 |
| `50_메인콘텐츠` | 콘텐츠·encounter 요구 |
| `60_UX_UI_접근성` | 정보 공개·접근성 요구 |
| `99_변경이력` | main SHA·PR·검증·Sheet 범위 |

## 5. 현재 승인 경계

- 최신 승인 기획은 main 정본이다.
- 제품 구현은 시작되지 않았다.
- 정확 영웅 능력·수치·경제 clock·simulation·runtime·human QA는 pending이다.
- Sheet-only 변경은 `PROPOSED_SHEET_CHANGE` 없이 정본으로 승격하지 않는다.

## 6. 향후 동일 작업 운영

- 중요 결정 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 다음 10건 동안 카운터를 `1/10`부터 누적한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 별도 승인 대기 없이 병합한다.
- GitHub auto-merge는 사용하지 않는다.
- 제품 코드 PR은 별도 작업 계약 대상이다.

## 7. 다음 Gate

```text
NEXT_PLANNING_BATCH_SELECTION
```
