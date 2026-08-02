# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
current_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
current_pr: 129
working_branch: gpt/omenward-hero-kit-planning-20260802
grill_me_count: 8_of_10
sheet_status: PROJECT_SHEET_CONFIGURED / SYNC_PENDING_FOR_CURRENT_DECISION
workspace_mode: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
exact_head_source: RESOLVE_FROM_PR_129_METADATA_AND_CONNECTED_SHEET
final_ci_source: RESOLVE_FROM_PR_129_BODY_AND_CONNECTED_SHEET
product_code_authority: NONE
```

## 1. 고정 Sheet 계약

```text
PROJECT_SHEET_CONFIGURED
USER_FACING_GDD_WORKSPACE
PROPOSED_SHEET_CHANGE
```

GitHub 기획 정본과 연결 Google Sheet는 같은 Decision ID와 같은 PR HEAD를 사용한다. 최종 exact HEAD와 CI run은 PR #129 메타데이터와 연결 Sheet에서 해석한다.

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= SIMULATION_VALIDATED
!= RUNTIME_VALIDATED
!= HUMAN_VALIDATED
```

## 2. 현행 Decision

```text
INITIAL_WARMUP
→ READY_WAITING_FOR_VALID_CONDITION
→ CAST_PRECHECK
→ CAST_COMMIT
→ RESOLUTION_OR_ACTIVE_EFFECT
→ COOLDOWN
→ READY
```

```text
MAX_STORED_READY_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
COOLDOWN_DURING_ACTIVE_EFFECT = FALSE
```

- 새 전장 배치 뒤 첫 사용 전에 initial warmup을 거친다.
- 유효 조건이 없으면 READY 1회를 보존한다.
- precommit 무효화는 READY 복귀·cooldown 소비 0이다.
- 단발 해결형은 commit payload를 한 번 해결한다.
- owner-bound 지속형은 시전자 제거 시 종료한다.
- cooldown은 해결 또는 지속효과 종료 뒤 시작한다.
- save/load·Retry로 timer·target·READY를 재굴림하지 않는다.

## 3. 초기 5명 적용

```text
불퇴의 성벽: 지속시간 또는 흡수 예산 종료 후 cooldown
천공 소거: 일제사격 판정 완료 후 cooldown
생명의 서약: 체력 하한 지속시간 종료 후 cooldown
메테오: 낙하·폭발 완료 후 cooldown
그림자 분신: 분신 종료 후 cooldown
```

천공 소거와 메테오는 commit 뒤 단발 해결형이다. 불퇴의 성벽·생명의 서약·그림자 분신은 owner-bound 지속형이다.

## 4. Sheet 반영 계획

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A36:N36`
- `02_현재_확정결정!A44:M44`
- `03_근거_라이브러리!A19:J21`
- `04_누락_충돌_감사!A173:H181`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A19:J19`
- `15_조작_게임규칙!A22:J22`
- `40_핵심시스템_메인콘텐츠!A22:J22`
- `41_성장_경제!A32:I32`
- `50_메인콘텐츠!A29:J29`
- `60_UX_UI_접근성!A30:J30`
- `70_아트_오디오_에셋!A13:J13`
- `99_변경이력!A47:H47`

쓰기 전 빈 행·서식을 확인하고 쓰기 뒤 같은 범위를 bounded read-back한다.

## 5. read-back 필수 확인

```text
SAME_DECISION_ID = PASS
EXACT_PR_HEAD_MATCH = PASS
COMMON_STATE_MACHINE_PRESENT = PASS
SINGLE_READY_STORAGE_PRESENT = PASS
CHARGE_ACCUMULATION_FALSE = PASS
INITIAL_WARMUP_PRESENT = PASS
PRECOMMIT_FAILURE_NO_COOLDOWN = PASS
COOLDOWN_AFTER_RESOLUTION = PASS
PRODUCT_CODE_UNCHANGED = PASS
```

## 6. 적대적 검토 기록

- `OMW-AUD-173`: warmup 길이 양극단 위험.
- `OMW-AUD-174`: effect 중 cooldown 진행으로 상시 유지 위험.
- `OMW-AUD-175`: 유효 조건 없는 cooldown 낭비.
- `OMW-AUD-176`: charge 누적 연속 폭발.
- `OMW-AUD-177`: save/load·Retry·Stage timer reset exploit.
- `OMW-AUD-178`: precommit 대상 소멸로 사용권 손실.
- `OMW-AUD-179`: commit 뒤 시전자 사망 처리 모호성.
- `OMW-AUD-180`: READY·cooldown 이유 불투명.
- `OMW-AUD-181`: Stage·정비시간 timer 정책 pending.

## 7. exact-head 검증 절차

```text
1. PR #129 actual head 조회
2. latest main 대비 behind 0 확인
3. changed paths docs-only·product paths 0 확인
4. actual head 필수 CI 3개 Green 확인
5. comments·reviews·unresolved threads 확인
6. Sheet OPEN_P0·OPEN_P1·MERGE_BLOCKER 검색
7. Sheet exact SHA·CI run·status 기록
8. bounded read-back
9. PR 설명에 동일 증거 기록
```

## 8. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
COMMON_STATE_MACHINE = APPROVED
SINGLE_READY_STORAGE = APPROVED
INITIAL_WARMUP = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWNS = PENDING
STAGE_AND_MAINTENANCE_TIMER_POLICY = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 Gate

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
```
