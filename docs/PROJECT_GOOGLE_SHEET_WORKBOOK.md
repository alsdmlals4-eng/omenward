# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_pr: 129
current_branch: gpt/omenward-hero-kit-planning-20260802
current_pr_head: RESOLVE_FROM_PR_129
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
status: PROJECT_SHEET_CONFIGURED / SYNC_REQUIRED_TO_PR_HEAD / READBACK_REQUIRED / CI_REQUIRED / COUNTER_10_OF_10
product_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. 연결 Sheet는 기획자가 읽고 운영하는 `USER_FACING_GDD_WORKSPACE`다. 모든 변경은 정본 Decision ID와 근거를 먼저 갖춘 `PROPOSED_SHEET_CHANGE`로 취급한 뒤 read-back과 CI를 통과해야 동기화 완료로 기록한다.

PR HEAD는 자기참조 commit을 만들지 않도록 GitHub PR #129와 Sheet에서 해석한다.

## 1. 이번 Decision

```text
READY
→ public trigger
→ same-lane legal filter
→ public priority score
→ stability window
→ stable tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

```text
A = 표준 [영웅]
B = 해금 이름 지정 [영웅]
C = 표준 [전설]
```

- 공개 Trigger·Priority·tie-break와 공통 Resolver를 사용한다.
- 숨은 AI·랜덤 tie-break·임의 fallback target·수동 발동을 금지한다.
- B는 의도된 encounter에서 A보다 강하고 C는 전체 대표 encounter 합산 가치에서 B보다 강해야 한다.
- 모든 encounter 자동 최선과 다른 두 전선 비결정화는 실패다.
- exact threshold·sample size·tolerance·값은 simulation 계획에서 고정한다.

## 2. Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| 프로젝트 Hub·카운터·HEAD | `00_프로젝트_허브!E2:L2` |
| 작업순서 | `01_작업순서!A38:N38` |
| 확정 Decision | `02_현재_확정결정!A46:M46` |
| 벤치마크 근거 | `03_근거_라이브러리!A25:J28` |
| 적대적 감사 | `04_누락_충돌_감사!A191:H202` |
| GDD 상태 요약 | `05_GDD_요약!D8:J8`, `05_GDD_요약!B9:J9` |
| 핵심루프 | `12_핵심루프!A21:J21` |
| 조작·게임 규칙 | `15_조작_게임규칙!A24:J24` |
| 핵심 시스템 | `40_핵심시스템_메인콘텐츠!A24:J24` |
| 성장·경제 경계 | `41_성장_경제!A34:I34` |
| encounter 검증 | `50_메인콘텐츠!A31:J31` |
| UX·접근성 | `60_UX_UI_접근성!A32:J32` |
| 아트·오디오 | `70_아트_오디오_에셋!A15:J15` |
| 변경 이력 | `99_변경이력!A49:H49` |

## 3. 근거 라이브러리

- `OM-EVD-024`: Riot Games `Clarity in League` — 전투 이해·대응 가능성, 중요도 위계, 노이즈 관리.
- `OM-EVD-025`: TFT `Neon Nights Gameplay Overview` — largest group·lowest health ally 같은 설명 가능한 자동 대상 규칙.
- `OM-EVD-026`: Riot `Champion Balance Framework`·`Balancing for Pro Play` — 일관된 측정과 특정 선택의 과도한 필수화 감시.
- `OM-EVD-027`: 내부 Trigger·target·A/B/C encounter validation contract.

공식 자료는 exact OMENWARD 값 권위가 아니다.

## 4. 적대적 감사

```text
OMW-AUD-191 hidden AI
OMW-AUD-192 one-frame trigger flicker
OMW-AUD-193 unstable tie-break
OMW-AUD-194 barrier permanent uptime
OMW-AUD-195 anti-air encounter deletion
OMW-AUD-196 Priest invulnerability/heal drift
OMW-AUD-197 undodgeable Meteor
OMW-AUD-198 autonomous clone scope expansion
OMW-AUD-199 unlocked Hero exceeds Legendary
OMW-AUD-200 one Hero best in all encounter families
OMW-AUD-201 late commit value loss
OMW-AUD-202 other two lanes become non-decisive
```

## 5. 쓰기·검증·병합 절차

```text
1. 대상 범위 bounded read
2. 기존 서식·검증 확인
3. 같은 Decision ID로 batch update
4. 동일 범위 bounded read-back
5. exact PR HEAD CI 3종 확인
6. latest main compare
7. changed path·review·thread 확인
8. OPEN_P0·OPEN_P1·MERGE_BLOCKER 검색
9. Sheet에 exact HEAD·run 번호 마감
10. PR 설명 갱신
11. fresh Green이면 Draft 해제
12. expected HEAD SHA로 직접 병합
13. merged PR·main SHA·Sheet merge 상태 확인
```

## 6. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 exact PR HEAD에서 `success`여야 `CI_3_GREEN`으로 기록한다.

## 7. blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 문자열의 실제 데이터 행을 검색한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

헤더 외 일치 행이 없어야 한다.

## 8. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
PUBLIC_TRIGGER_TARGET_RESOLVER = APPROVED_CONCEPT
POWER_VALIDATION_MATRIX = APPROVED_CONCEPT
EXACT_SCHEMA_AND_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 카운터·병합

```text
GRILL_ME_COUNT = 10/10
PREFLIGHT = REQUIRED_NOW
```

fresh preflight가 Green이면 standing user authorization에 따라 문서 PR #129를 별도 승인 대기 없이 병합한다. 제품 구현 권한은 포함하지 않는다.