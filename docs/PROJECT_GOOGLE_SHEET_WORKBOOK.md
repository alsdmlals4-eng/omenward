# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
recovery_pr: 119
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / META_DECISION_SYNC_PENDING
ci_validation: PREVIOUS_HEAD_3_GREEN / CURRENT_HEAD_PENDING
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. 독립 정본이 아니며 GitHub의 현재 Decision·책임 원본·실제 구현 상태를 임의로 덮어쓰지 않는다.

`PROJECT_SHEET_CONFIGURED`는 Workbook 연결·구성이 완료됐다는 호환성 상태다. 현재 Decision의 exact PR HEAD는 Sheet `00_프로젝트_허브`, `02_현재_확정결정`, `99_변경이력`과 PR #119에서 재조회한다.

GitHub 정본에 없는 Sheet-only 편집은 `PROPOSED_SHEET_CHANGE`로 보존하고, 사용자 승인과 GitHub 반영·재조회가 끝나기 전에는 현행 Decision으로 승격하지 않는다.

## 1. 필수 상태 축

Sheet의 각 주요 행은 가능한 범위에서 다음을 분리한다.

```text
Decision status
Canonical authority commit
Current main commit
Current working PR head
Implementation status
Automated validation status
Human validation status
Sheet read-back status
```

다음 값을 한 열이나 한 상태로 혼합하지 않는다.

- Base release SHA.
- 프로젝트 main SHA.
- Decision authority commit.
- PR head SHA.
- 구현 commit.
- 검증 evidence commit.

## 2. 현재 탭

- `00_프로젝트_허브`
- `01_작업순서`
- `02_현재_확정결정`
- `03_근거_라이브러리`
- `04_누락_충돌_감사`
- `05_GDD_요약`
- `10_제품방향`
- `11_세계관`
- `12_핵심루프`
- `13_주요인물`
- `14_조연_세력_관계`
- `15_조작_게임규칙`
- `20_코어경험_데모목표`
- `30_데모범위_품질기준_제작기반`
- `40_핵심시스템_메인콘텐츠`
- `41_성장_경제`
- `50_메인콘텐츠`
- `60_UX_UI_접근성`
- `70_아트_오디오_에셋`
- `71_이미지기획_생성목록`
- `72_이미지검수_승인로그`
- `80_데모_버티컬슬라이스_플레이테스트`
- `90_본제작_출시_사업`
- `98_Base_반영후보`
- `99_변경이력`

## 3. 복구 Finding과 검증 결과

| Finding | Sheet 영향 | 처리 |
|---|---|---|
| Base v9.1 기록이 current main v9.4와 충돌 | `00`, `04`, `99` | v9.4로 복구, read-back PASS |
| `SYNCED_TO_PR_HEAD`가 실제 PR #116 HEAD와 다름 | `00`, `02`, `99` | PR #116 closed/superseded, PR #119 HEAD 기록 |
| authority commit과 main commit 의미 혼합 | `02` | 상태·설명에서 분리 |
| Evidence 행 열 밀림 | `03` | 검증된 행 재정렬, read-back PASS |
| System ID 누락으로 행 밀림 | `40` | `OM-S-04`, `OM-S-07` 복구, read-back PASS |
| 사업 milestone 행이 헤더보다 넓음 | `90` | 8열 milestone schema로 정렬, read-back PASS |
| `60_UX_UI_접근성` schema 오류 주장 | `60` | 재조회 결과 10열 일치, `REJECTED_CRITIQUE` |

## 4. 현재 Meta Decision

Decision: `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1`

```text
PRIMARY = 수평 해금 + 제한된 편의
SECONDARY = 선택형·상한형 준비 보정
FORBIDDEN = 무한 영구 능력치 누적
```

Sheet는 다음을 명시한다.

- 기본 Profile로 모든 콘텐츠 완료 가능.
- 수평 해금은 sidegrade.
- 시작 보관 편의는 hard cap.
- 준비 보정은 한 런 1개·유한 랭크·시작/Act 1 중심.
- Retry spendable balance와 준비 보정 milestone 해금 분리.
- 정확 효과량·milestone·비용·재화명은 `EXACT_VALUES_PENDING`.
- P0/P1/P2 simulation·runtime·human 검증은 `NOT_RUN`.

## 5. Decision 즉시 동기화

사용자가 주요 기획 Decision을 승인하면 다음을 한 흐름 안에서 수행한다.

```text
Decision ID 생성 또는 재사용
→ GitHub 분야 정본·Decision Ledger·Context 갱신
→ commit
→ 연결 Sheet의 결정·분야·감사·변경이력 행 갱신
→ GitHub와 Sheet 재조회
→ ID·의미·상태·경로·commit 일치
→ SYNCED
```

`PARTIAL_SYNC_BLOCKED` 또는 `SYNC_CONFLICT`이면 다음 주요 Grill Me 질문이나 제품 구현으로 진행하지 않는다.

## 6. 상세 수치 셀 상태

- `LEGACY_H0 / HISTORICAL_ONLY`
- `RECOMMENDED_DEFAULT`
- `TEST_VALUE`
- `SIMULATION_CANDIDATE`
- `USER_APPROVED_VALUE`
- `IMPLEMENTED_VALUE`
- `VALIDATED_VALUE`
- `NOT_APPROVED`

빈칸이나 과거값을 제품 기본값으로 자동 해석하지 않는다.

Meta candidate guardrail의 5 percentage points, 3~8 percentage points, 준비 보정 3개 후보, 랭크 2단계 후보는 제품 확정값이 아니다. 한 런 장착 1개만 승인 제약이다.

## 7. 현재 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| Profile 영구 성장 | `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 작업 상태 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |
| 인계 | `docs/HANDOFF_CONTEXT.md` |

## 8. 이번 동기화 대상

- `00_프로젝트_허브!E2:L2`: 현재 Decision·다음 Grill Me·exact PR HEAD.
- `01_작업순서!A10:N10`: Meta 승인 Bundle.
- `02_현재_확정결정!A19:M19`: 같은 Decision ID와 승인 역할.
- `04_누락_충돌_감사!E26:H26`: 기존 영구 성장 공백 해결 상태.
- `04_누락_충돌_감사!A30:H32`: B 노가다·숨은 상위 호환·Retry 지갑 충돌 검토.
- `41_성장_경제`: Profile·준비 보정·가드레일·저장 책임.
- `99_변경이력!A19:H19`: GitHub path·commit·Sheet 범위·재검증.

## 9. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- PR #116의 과거 HEAD를 current HEAD로 표시.
- 승인된 역할을 정확 수치 승인으로 확대.
- 준비 보정을 직접 공격력·생산량 전 구간 배율로 확대.
- 시험값을 제품 확정값으로 표시.
- 승인 기획을 구현 완료로 표시.
