# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
superseded_pr: 116
sheet_status: RECOVERY_SYNC_IN_PROGRESS
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. 독립 정본이 아니며 GitHub의 현재 Decision·책임 원본·실제 구현 상태를 임의로 덮어쓰지 않는다.

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

## 3. 현재 복구 Finding

| Finding | Sheet 영향 | 처리 |
|---|---|---|
| Base v9.1 기록이 current main v9.4와 충돌 | `00`, `04`, `99` | v9.4로 복구 |
| `SYNCED_TO_PR_HEAD`가 실제 PR #116 HEAD와 다름 | `00`, `02`, `99` | PR #116 historical 처리, recovery head 기록 |
| authority commit과 main commit 의미 혼합 | `02` | 상태·설명에서 분리 |
| Evidence 행 열 밀림 | `03` | 검증된 행만 재정렬 |
| System ID 누락으로 행 밀림 | `40` | System ID와 필드 정렬 |
| UX/사업 행이 헤더보다 넓음 | `60`, `90` | 명시적 헤더 추가 또는 현행 열 안으로 정렬 |
| 신규 simulator Work Order가 Sheet Decision에 없음 | `02`, `04`, `99` | 계획 artifact로 기록하되 실행·제품값으로 승격 금지 |

## 4. Decision 즉시 동기화

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

## 5. 상세 수치 셀 상태

수치와 공식에는 다음 상태를 사용한다.

- `LEGACY_H0 / HISTORICAL_ONLY`
- `RECOMMENDED_DEFAULT`
- `TEST_VALUE`
- `SIMULATION_CANDIDATE`
- `USER_APPROVED_VALUE`
- `IMPLEMENTED_VALUE`
- `VALIDATED_VALUE`
- `NOT_APPROVED`

빈칸이나 과거값을 제품 기본값으로 자동 해석하지 않는다.

## 6. 현재 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 정본 복구·Finding·Grill Me 큐 | `docs/audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 작업 상태 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |
| 인계 | `docs/HANDOFF_CONTEXT.md` |

## 7. 현재 동기화 대상

Decision: `OMW-DEC-20260802-CANON-RECOVERY-V1`

- `00_프로젝트_허브`: Base v9.4·TOTAL_PLANNING·recovery PR 상태.
- `01_작업순서`: 정본 복구→Grill Me→기획 작성 순서.
- `02_현재_확정결정`: recovery Decision과 PR #116 superseded 관계.
- `03_근거_라이브러리`: Base v9.4·main·PR #116·실제 code evidence 정렬.
- `04_누락_충돌_감사`: recovery finding ledger.
- `40_핵심시스템_메인콘텐츠`: System ID 누락 복구.
- `60_UX_UI_접근성`: 헤더·데이터 열 의미 정렬.
- `90_본제작_출시_사업`: 장기 플랫폼·출시 필드 명시.
- `99_변경이력`: GitHub path·commit·read-back 결과.

## 8. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- PR #116의 과거 HEAD를 current recovery HEAD로 표시.
- Base SHA와 project head를 같은 의미로 사용.
- 승인 기획을 구현 완료로 표시.
- 시험값을 제품 확정값으로 표시.
- 이미지 계획·생성·승인·엔진 적용을 한 상태로 합침.
