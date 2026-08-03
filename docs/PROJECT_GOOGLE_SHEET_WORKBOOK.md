# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
parent_time_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
current_grill_me_count: 6_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
```

## 1. 역할

GitHub APPROVED 문서가 기획 정본이며 이 Sheet는 사용자 가시 GDD·계획·근거·감사·변경 이력 Workspace다. 모든 승인 변경은 같은 Decision ID와 exact PR HEAD로 양쪽에 기록한다.

## 2. Decision 6 Sheet 동기화 계약

Decision ID:

```text
OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
```

반영 내용:

```text
SOURCE_OUTGOING = 50%~150%
TARGET_INCOMING = 50%~150%
COMBINED_PRE_DEFENSE = 25%~200%
R60 = source snapshot
R80 = target snapshot
```

```text
REFRESH_DURATION
REPLACE_IF_STRONGER
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

```text
P00 validity → P10 immunity → P20 source → P30 target incoming
→ P40 defense → P50 Barrier → P60 redirection → P70 Floor
→ P80 HP/Restore → P90 Status → P100 death pending
```

## 3. 필수 탭

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

## 4. 탭별 반영 의미

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·PR HEAD·6/10 상태 |
| `01_작업순서` | Modifier 승인 작업·검증·다음 Gate |
| `02_현재_확정결정` | Decision 6 정식 행 |
| `03_근거_라이브러리` | Unreal GAS·내부 결정론·프로젝트 코어 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-276~289` |
| `05_GDD_요약` | family cap·snapshot·precedence 요약 |
| `12_핵심루프` | 전선 배치→Modifier 인과→결과 복기 연결 |
| `15_조작_게임규칙` | family·stacking·trigger 규칙 |
| `40_핵심시스템_메인콘텐츠` | ModifierRecord·aggregate·precedence system |
| `41_성장_경제` | Modifier가 경제·룰렛 출처를 직접 재실행하지 않는 경계 |
| `50_메인콘텐츠` | duplicate·snapshot·immunity·Barrier Fixture matrix |
| `60_UX_UI_접근성` | Damage Dealt/Taken·Barrier·HP loss debug trail |
| `70_아트_오디오_에셋` | VFX·animation은 Modifier 권위가 아님 |
| `99_변경이력` | 위치·HEAD·CI·경계 기록 |

## 5. 적대적 감사

```text
OMW-AUD-276 operation order dependency
OMW-AUD-277 positive raw damage rounded to zero
OMW-AUD-278 source snapshot drift
OMW-AUD-279 target response ignored
OMW-AUD-280 same-source duplicate growth
OMW-AUD-281 multi-source family cap bypass
OMW-AUD-282 generic override bypass
OMW-AUD-283 iteration-order result drift
OMW-AUD-284 outgoing/incoming UI polarity confusion
OMW-AUD-285 immune attack false trigger
OMW-AUD-286 Barrier hit and HP hit conflation
OMW-AUD-287 transferred damage second pass
OMW-AUD-288 next-hit consumption ID bias
OMW-AUD-289 hero direct HP mutation
```

## 6. Bounded Read-Back

쓰기 후 다음을 다시 읽는다.

- Decision ID.
- exact PR HEAD.
- `50~150%`, `25~200%`, R60/R80 값.
- 다섯 Stacking 정책.
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
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-SPATIAL-QUANTIZATION-MOVEMENT-AND-TARGETING-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
GRILL_ME_COUNT = 6/10
```
