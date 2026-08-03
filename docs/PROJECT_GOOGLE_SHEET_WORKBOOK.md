# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
current_grill_me_count: 5_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
```

## 1. 역할

GitHub APPROVED 문서가 기획 정본이며 이 Sheet는 사용자 가시 GDD·계획·근거·감사·변경 이력 Workspace다. 모든 승인 변경은 같은 Decision ID와 exact PR HEAD로 양쪽에 기록한다.

```text
GitHub responsibility document
+ PROJECT_CANON_DECISION_LEDGER
+ DECISIONS_PENDING
+ CURRENT_IMPLEMENTATION_STATUS
↔ same Decision ID
Google Sheet hub/decision/evidence/audit/system/history rows
```

## 2. 필수 탭

```text
00_프로젝트_허브
01_작업순서
02_현재_확정결정
03_근거_라이브러리
04_누락_충돌_감사
05_GDD_요약
12_핵심루프
15_조작_게임규칙
40_핵심시스템_메인콘텐츠
41_성장_경제
50_메인콘텐츠
60_UX_UI_접근성
70_아트_오디오_에셋
99_변경이력
```

## 3. Decision 5 Sheet 동기화 계약

Decision ID:

```text
OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
```

반영 내용:

```text
DOMAIN_TPS = 30
AUTHORING_TIME = integer ms
RUNTIME_TIME = integer tick
DURATION_TICKS = ceil(ms * 30 / 1000)
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
SPAWN_AT_T → ACTIVATE_AT_T_PLUS_1
```

```text
Barrier 3000ms = 90 ticks
DOT/HOT pulse 1000ms = 30 ticks
Control max 2000ms = 60 ticks
Control lockout 1000ms = 30 ticks
```

## 4. 탭별 반영 의미

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·PR HEAD·5/10 상태 |
| `01_작업순서` | 시간축 승인 작업·검증·다음 Gate |
| `02_현재_확정결정` | Decision 5 정식 행 |
| `03_근거_라이브러리` | Godot interpolation·Timer·내부 결정론·프로젝트 코어 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-262~275` |
| `05_GDD_요약` | 30 TPS·exclusive expiry·T+1 activation 요약 |
| `12_핵심루프` | 룰렛 배치→Tick 전투→결과 복기 연결 |
| `15_조작_게임규칙` | R00/R10/R20/R110/R130 시간 규칙 |
| `40_핵심시스템_메인콘텐츠` | integer Tick·Timer·spawn/activation system |
| `41_성장_경제` | 전투 Tick과 경제·정비 clock 경계 |
| `50_메인콘텐츠` | 시간·spawn·pause·save Fixture matrix |
| `60_UX_UI_접근성` | Tick debug trail·pause·expiry·activation 표시 |
| `70_아트_오디오_에셋` | interpolation은 visual-only, callback 비권위 |
| `99_변경이력` | 위치·HEAD·CI·경계 기록 |

## 5. 적대적 감사

```text
OMW-AUD-262 wall clock authority
OMW-AUD-263 ms floor conversion
OMW-AUD-264 positive duration to zero
OMW-AUD-265 exclusive-end fencepost
OMW-AUD-266 spawn same-tick action
OMW-AUD-267 hidden spawn immunity
OMW-AUD-268 same-tick protection ID bias
OMW-AUD-269 Timer/animation callback authority
OMW-AUD-270 pause clock leak
OMW-AUD-271 float Save timer
OMW-AUD-272 Tick skip/merge under overload
OMW-AUD-273 interpolation state writeback
OMW-AUD-274 past command silent correction
OMW-AUD-275 long-run Tick overflow
```

## 6. Bounded Read-Back

쓰기 후 다음을 다시 읽는다.

- Decision ID.
- exact PR HEAD.
- `30 TPS`, `90/30/60/30 Tick` 값.
- 대상 행 위치.
- 감사 ID 연속성.
- status·CI cells.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 7. 상태 표기

```text
SHEET_SYNC = SYNCED_TO_PR_HEAD_AFTER_WRITE_AND_READBACK
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 Gate

```text
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
NEXT_PREFLIGHT = AT_10_OF_10
GRILL_ME_COUNT = 5/10
```
