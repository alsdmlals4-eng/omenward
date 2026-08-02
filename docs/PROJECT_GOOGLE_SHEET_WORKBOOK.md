# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
recovery_pr: 119
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / CONTENT_READBACK_PASS / EXACT_HEAD_TRACKED_IN_SHEET_AND_PR
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. 독립 정본이 아니며 GitHub의 현재 Decision·책임 원본·실제 구현 상태를 임의로 덮어쓰지 않는다.

`PROJECT_SHEET_CONFIGURED`는 Workbook 연결과 필수 탭 계약이 구성됐음을 뜻하는 호환 상태다. 현재 Decision의 exact PR HEAD는 Sheet `00_프로젝트_허브`, `02_현재_확정결정`, `99_변경이력`과 PR #119에서 추적한다. GitHub 정본에 없는 Sheet-only 편집은 `PROPOSED_SHEET_CHANGE`다.

## 1. 필수 상태 축

```text
Decision status
Canonical authority path
Baseline main commit
Current working PR head
Implementation status
Automated validation status
Human validation status
Sheet read-back status
```

Base SHA·project main·Decision authority·PR head·구현 commit·검증 evidence를 같은 의미로 혼합하지 않는다.

## 2. 주요 탭 역할

| 탭 | 역할 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·PR HEAD·차단 상태 |
| `01_작업순서` | Approval Bundle·선행/후속 작업 |
| `02_현재_확정결정` | 같은 Decision ID의 사용자 승인 내용 |
| `04_누락_충돌_감사` | 적대적 finding·해결·검증 요구 |
| `11_세계관` | 세계 법칙·MapRun·징조·승패·미확정 경계 |
| `13_주요인물` | 플레이어·벨루의 세계 내 역할 |
| `41_성장_경제` | Profile·Retry·준비 보정 |
| `99_변경이력` | GitHub path·HEAD·수정 범위·read-back |

## 3. 현재 세계·MapRun Decision

Decision: `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1`

```text
MapRun = 징조로 감지된 별개의 실제 경계 방어 작전
징조 = 공세 구조의 제한된 예측 정보
승리 = 한 균열·침공로 봉쇄
패배 = 전진 방어선 붕괴와 실제 피해
Profile = 여러 작전의 교리·보급망·기록·준비 축적
```

Sheet에는 다음 경계를 기록하고 재조회했다.

- 시간 루프 아님.
- 전부 가상 시뮬레이션 아님.
- 징조는 결과를 확정하지 않음.
- paid Retry는 시간 되감기가 아닌 비상 재투입.
- 벨루는 관측·기록·인과 안내자.
- 기존 세계 명칭 계보는 보존하지만 상세 정의는 pending.
- 제품 코드·runtime·human 검증은 미실행.

## 4. 기존 명칭 계보

`OMENWARD_GAME_DESIGN.md`에는 다음 이름이 있다.

- 루메른 왕국.
- 루미엔 영토.
- 트리븐 전선.
- 실베른 성채.
- 베일런 황야.
- 베일의 법칙.
- 베일의 징조.
- 벨루.
- 베일종.

이름은 Sheet에서 삭제하지 않지만 후속 세계관 Decision 전 최종 정치·지리·존재론으로 자동 승격하지 않는다.

## 5. Decision 즉시 동기화

```text
사용자 승인
→ GitHub 분야 정본·Decision Ledger·Context 갱신
→ commit
→ Sheet 결정·분야·감사·변경이력 갱신
→ bounded read-back
→ exact PR HEAD·CI 확인
→ SYNCED
```

`PARTIAL_SYNC_BLOCKED` 또는 `SYNC_CONFLICT`이면 다음 중요 Decision으로 진행하지 않는다.

## 6. 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 세계·MapRun 반복 동기 | `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` |
| Profile 영구 성장 | `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 작업 상태 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |
| 인계 | `docs/HANDOFF_CONTEXT.md` |

## 7. 이번 동기화 완료 범위

- `00_프로젝트_허브!E2:L2`: 현재 Decision·다음 세계관 Gate·exact PR HEAD.
- `01_작업순서!A11:N11`: World Run Approval Bundle.
- `02_현재_확정결정!A20:M20`: 같은 Decision ID와 승인 원칙.
- `04_누락_충돌_감사!A33:H36`: 시간 루프·승리 무효화·예언 결정론·세계 소모 위험.
- `11_세계관!A4:H8`: MapRun·징조·승패·기존 명칭 보류선.
- `13_주요인물!A2:J2`, `A4:J4`: 지휘자·벨루의 작전 기록 역할.
- `99_변경이력!A20:H20`: GitHub path·commit·Sheet 범위·재검증.

## 8. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- 세계 원칙 승인을 베일의 본질·왕국 정치·적의 목적 승인으로 확대.
- 기존 명칭을 조용히 교체하거나 일반 판타지 설정으로 보충.
- 징조를 완전 예언·운명 결정으로 표시.
- 승인 기획을 구현 완료로 표시.
