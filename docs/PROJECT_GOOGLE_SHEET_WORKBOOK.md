# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-04
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_grill_me_count: 9_OF_10
product_code_authority: NONE
image_production_authority: PAUSED_BY_USER
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

## 3. Decision 9 Sheet 동기화 계약

Decision ID:

```text
OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
```

반영 내용:

```text
BOTTOM_FUNCTIONS = ROULETTE / STORAGE / BUILD / TACTICAL_SKILL / BELU
SHOP_BUTTON = REMOVED
MAIN_HUD_RESOURCES = GOLD / MANA_STONE / DEPLOYED_TROOP_CAPACITY
MOVE_TICKET_DISPLAY = ROULETTE_PANEL_ONLY
MERCHANT = AFTER_STAGE_MAINTENANCE_ONLY
BUILDINGS = VAULT / FARM / BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
COMMAND_POST_AURA = MAPRUN_WIDE_ALLIED_TROOPS
```

## 4. 탭별 반영 의미

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·PR HEAD·9/10 상태 |
| `01_작업순서` | Decision 9 완료와 10/10 아트 Gate |
| `02_현재_확정결정` | HUD·룰렛·자원·상인·건물 6종 정식 행 |
| `03_근거_라이브러리` | 룰렛·건물·Stage 정비·벨루 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-314~330` |
| `05_GDD_요약` | 하단 기능·자원·이동권·상인·건물 목록 |
| `12_핵심루프` | 건물→릴→결과→배치→전투→Stage 종료 상인 |
| `15_조작_게임규칙` | 릴/행 선택→미리보기→이동 실행 |
| `40_핵심시스템_메인콘텐츠` | 룰렛 정보·상인·마석·6종 건물 역할 |
| `41_성장_경제` | 골드·마석·병력 한도·상인 경제 역할 |
| `50_메인콘텐츠` | 6종 건물과 Stage 종료 상인 콘텐츠 |
| `60_UX_UI_접근성` | 이동권 룰렛 내부 표시·벨루 우측 하단 조언 |
| `70_아트_오디오_에셋` | 건물 6종·마석·벨루·룰렛 정보의 시각 구분 요구 |
| `71_이미지기획_생성목록` | 사용자 지시에 따른 이미지 생성 중단 상태 |
| `99_변경이력` | 범위·HEAD·9/10·이미지 중단 기록 |

## 5. Bounded Read-Back

쓰기 후 다음을 다시 읽는다.

- Decision ID와 process policy ID.
- exact PR HEAD.
- `9/10` 상태.
- 하단 기능 순서와 상점 버튼 제거.
- 골드·마석·배치 병력/병력 한도.
- 이동권 룰렛 패널 전용 표시.
- Stage 종료 상인.
- 건물 6종과 지휘소 전역 오라.
- 감사 `OMW-AUD-314~330` 연속성.
- 이미지 생성 중단 상태.
- CI 상태 셀.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 6. 상태 표기

```text
SHEET_SYNC = SYNCED_TO_PR_HEAD_AFTER_WRITE_AND_READBACK
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = PAUSED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 다음 Gate

```text
10/10 = OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
