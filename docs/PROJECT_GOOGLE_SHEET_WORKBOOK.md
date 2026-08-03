# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-04
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_grill_me_count: 7_OF_10
product_code_authority: NONE
image_production_authority: NONE
```

## 1. 역할

GitHub APPROVED 문서가 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사·이미지 계획 Workspace다. 승인 변경은 같은 Decision ID와 exact PR HEAD로 기록한다.

## 2. 작업 권한 경계

```text
GPT / Work = planning, player-facing rules, UX, art direction, image brief
Codex = data structures, algorithms, coordinates, pathfinding, physics, performance, code and tests
```

기존 기술 문서의 플레이어 경험은 유지하지만 정확한 구현 표현은 Codex 참고안으로 재분류한다.

## 3. Decision 7 Sheet 동기화 계약

Decision ID:

```text
OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1
```

반영 내용:

```text
THREE_FRONTS = TOP / MID / BOTTOM
VISIBLE_MAIN_ROUTE_PER_FRONT
VISIBLE_BYPASS_AND_AIR_ROUTE
DEFAULT_TARGET = nearest valid on same front/route
CROSS_LANE = explicit and telegraphed only
HIDDEN_AUTO_LANE_CHANGE = FORBIDDEN
```

## 4. 탭별 반영 의미

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·PR HEAD·7/10 상태 |
| `01_작업순서` | 권한 경계 수정·Decision 7·다음 Visual Gate |
| `02_현재_확정결정` | 전투 공간·Route·Targeting 정식 행 |
| `03_근거_라이브러리` | 프로젝트 코어·기존 기획·권한 경계 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-290~299` |
| `05_GDD_요약` | 세 전선·가시 Route·Targeting·Visual 우선순위 |
| `12_핵심루프` | 룰렛 배치→전선 Route→교전 복기 |
| `15_조작_게임규칙` | Ground·Flying·침투·Cross-lane 규칙 |
| `40_핵심시스템_메인콘텐츠` | 전장 공간·Route·Target 역할 구조 |
| `50_메인콘텐츠` | 이미지·사람 검증 Fixture와 Callout |
| `60_UX_UI_접근성` | Target·Route·위험 정보 단계적 표시 |
| `70_아트_오디오_에셋` | 전장 이미지 4종과 실제 규칙 일치 기준 |
| `99_변경이력` | 범위·HEAD·CI·Codex 위임 기록 |

## 5. Bounded Read-Back

쓰기 후 다음을 다시 읽는다.

- Decision ID와 process policy ID.
- exact PR HEAD.
- `7/10` 상태.
- 세 전선·가시 Route·기본 Target·Cross-lane 경계.
- 대상 행 위치.
- 감사 `OMW-AUD-290~299` 연속성.
- CI 상태 셀.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 6. 상태 표기

```text
SHEET_SYNC = SYNCED_TO_PR_HEAD_AFTER_WRITE_AND_READBACK
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = NOT_AUTHORIZED_UNTIL_10_OF_10_PREFLIGHT
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 다음 Gate

```text
8/10 = OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1
9/10 = OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
10/10 = OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
