# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
recovery_pr: 119
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / ONTOLOGY_SYNC_IN_PROGRESS
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
| `11_세계관` | 베일 존재론·세계 법칙·MapRun·징조·승패·미확정 경계 |
| `13_주요인물` | 플레이어·벨루의 세계 내 역할 |
| `41_성장_경제` | Profile·Retry·준비 보정 |
| `99_변경이력` | GitHub path·HEAD·수정 범위·read-back |

## 3. 현재 베일 존재론 Decision

Decision: `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1`

```text
베일 = 현실과 외부 법칙 영역의 비의지적 경계 겹침
베일의 법칙 = 공세별 유한·관측·반복 가능한 규칙 묶음
징조 = 겹침 전 선행 공명과 제한된 위협 예고
균열 = 겹침이 현실 지형에 고정된 상태
상흔 = 봉쇄 뒤에도 남는 지형·생태·물질·기억 변화
```

Sheet에 기록할 경계:

- 베일은 장소·물리 장벽·악신이 아니다.
- 베일 자체에는 통일된 의지·선악·계획이 없다.
- 균사·혈관·결정처럼 보이는 성장은 생명 의지가 아니라 물질적 패턴이다.
- 베일의 법칙은 임의 마법이 아니라 공개·관측 가능한 유한 규칙이다.
- 베일종은 베일 자체와 분리된 독립 행위자일 수 있다.
- 베일종 발생·지성·목적, 외부 영역의 수·기원, 릴 원리는 pending이다.
- 제품 코드·runtime·human 검증은 미실행이다.

## 4. 세계·MapRun Decision

Decision: `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1`

```text
MapRun = 징조로 감지된 별개의 실제 경계 방어 작전
승리 = 한 균열·침공로 봉쇄
패배 = 전진 방어선 붕괴와 실제 피해
Profile = 여러 작전의 교리·보급망·기록·준비 축적
```

시간 루프·전부 가상 시뮬레이션·예언 결정론을 금지한다. paid Retry는 같은 공세의 비상 재투입이다.

## 5. 기존 명칭 계보

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

이번 Decision으로 베일·법칙·징조·균열·상흔의 상위 관계는 확정된다. 명칭의 정치적 소유·어원·정확한 지리와 역사는 후속 Decision 전 자동 확정하지 않는다.

## 6. Decision 즉시 동기화

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

## 7. 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 베일 존재론 | `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` |
| 세계·MapRun 반복 동기 | `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` |
| Profile 영구 성장 | `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 작업 상태 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |
| 인계 | `docs/HANDOFF_CONTEXT.md` |

## 8. 이번 동기화 예정 범위

- `00_프로젝트_허브!E2:L2`: 현재 Decision·다음 세계관 Gate·exact PR HEAD.
- `01_작업순서!A12:N12`: Veil Ontology Approval Bundle.
- `02_현재_확정결정!A21:M21`: 같은 Decision ID와 승인 원칙.
- `04_누락_충돌_감사!A37:H42`: 신격화·생태적 의지·만능 법칙·침공 주체·봉쇄 한계·외부 우주론 검토.
- `11_세계관!A9:H15`: 베일·법칙·징조·균열·상흔·미확정 경계.
- `99_변경이력!A21:H21`: GitHub path·commit·Sheet 범위·재검증.

## 9. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- 베일 존재론 승인을 왕국 정치·적의 목적·릴 원리 승인으로 확대.
- 베일의 생태적 외형을 통일된 신적 의지로 해석.
- 베일의 법칙을 임의 예외를 허용하는 만능 마법으로 사용.
- 외부 영역의 수·기원·우주론을 자동 확정.
- 승인 기획을 구현 완료로 표시.