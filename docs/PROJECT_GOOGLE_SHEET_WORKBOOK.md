# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-04
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_grill_me_count: 8_OF_10
product_code_authority: NONE
image_production_authority: NONE
```

## 1. 역할

GitHub APPROVED 문서가 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사·이미지 계획 Workspace다. 승인 변경은 같은 Decision ID와 exact PR HEAD로 기록한다.

## 2. GPT 역할과 Codex 경계

```text
GPT / Work = core fun, content planning, player-facing rules, UX, image and art direction
Codex = data structures, algorithms, coordinates, pathfinding, physics, performance, code and tests
```

Sheet는 구현 세부보다 다음 순서로 기획 정보를 보존한다.

```text
핵심 재미
→ 콘텐츠 구조와 역할
→ UX·이미지·아트
→ 구현 결과 조건
```

기존 기술 문서의 플레이어 경험은 유지하지만 정확한 구현 표현은 Codex 참고안으로 재분류한다.

## 3. Decision 8 Sheet 동기화 계약

Decision ID:

```text
OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1
```

반영 내용:

```text
CAMERA = PC 16:9 HIGH_ANGLE_THREE_QUARTER_STRATEGY
THREE_FRONTS_VISIBLE = REQUIRED
BATTLEFIELD_SHARE = ABOUT_70_TO_75_PERCENT
BOTTOM_HUD_SHARE = ABOUT_25_TO_30_PERCENT
FORCED_CAMERA_MOVEMENT = MINIMIZED
FRONT_FLOW_BEFORE_UNIT_DETAIL = REQUIRED
```

## 4. 탭별 반영 의미

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·PR HEAD·8/10 상태 |
| `01_작업순서` | GPT 우선순위·Decision 8·다음 HUD Gate |
| `02_현재_확정결정` | 전장 시각 계층·카메라 정식 행 |
| `03_근거_라이브러리` | 프로젝트 코어·전투 공간·카메라 기획 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-300~313` |
| `05_GDD_요약` | 세 전선 동시 가독성·카메라·정보 우선순위 |
| `12_핵심루프` | 릴 배치 결과를 전선 화면에서 읽고 다음 설계로 복기 |
| `15_조작_게임규칙` | 전략 줌·경고·카메라 강제 이동 금지 규칙 |
| `40_핵심시스템_메인콘텐츠` | 전장 시각 계층과 Route·병종 역할 표현 |
| `50_메인콘텐츠` | 기본·위험·교전 확대·Boss 이미지 Fixture |
| `60_UX_UI_접근성` | 체력·Status·Target·경고의 단계적 공개 |
| `70_아트_오디오_에셋` | 고각도 3/4 구도·Route·VFX·광원 검수 기준 |
| `99_변경이력` | 범위·HEAD·CI·GPT 역할 우선순위 기록 |

## 5. Bounded Read-Back

쓰기 후 다음을 다시 읽는다.

- Decision ID와 process policy ID.
- exact PR HEAD.
- `8/10` 상태.
- 고각도 3/4·세 전선 동시 가독성·정보 우선순위.
- 대상 행 위치.
- 감사 `OMW-AUD-300~313` 연속성.
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
9/10 = OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
10/10 = OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
