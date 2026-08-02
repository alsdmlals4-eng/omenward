# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
merge_batch_pr: 119
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / MERGE_PREFLIGHT_SYNC
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. 독립 정본이 아니며 GitHub의 현재 Decision·책임 원본·실제 구현 상태를 임의로 덮어쓰지 않는다.

`PROJECT_SHEET_CONFIGURED`는 Workbook 연결과 필수 탭 계약이 구성됐음을 뜻한다. 현재 Decision의 exact PR HEAD는 `00_프로젝트_허브`, `02_현재_확정결정`, `99_변경이력`과 PR 설명에서 추적한다. GitHub 정본에 없는 Sheet-only 편집은 `PROPOSED_SHEET_CHANGE`다.

## 1. 상태 축

```text
Decision status
Canonical authority path
Baseline main commit
Current working PR head
Merged main commit
Implementation status
Automated validation status
Human validation status
Sheet read-back status
Grill Me approval count
```

Base SHA·project main·Decision authority commit·PR head·merge commit·구현 commit·검증 evidence를 혼합하지 않는다.

## 2. 주요 탭 역할

| 탭 | 역할 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·PR/main SHA·다음 Gate·카운터 |
| `01_작업순서` | Approval Bundle·선행/후속·병합 단계 |
| `02_현재_확정결정` | 같은 Decision ID의 사용자 승인 내용 |
| `04_누락_충돌_감사` | 적대적 finding·해결·검증·merge blocker |
| `05_GDD_요약` | 최신 세계·Meta·구현·검증 요약 |
| `11_세계관` | 세계·베일·오멘워드 조직·승패 |
| `13_주요인물` | 플레이어 지휘관·벨루 역할 |
| `14_조연_세력_관계` | 루메른 왕국·오멘워드·왕실군·지방 관계 |
| `41_성장_경제` | 영구재화·주점·병영·연구·Readiness·Retry |
| `60_UX_UI_접근성` | 메인 작전 허브·노드 그래프·8개 화면 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

### 조직·정치

Decision: `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1`

```text
오멘워드 = 루메른 왕실 인가 자율 경계대응단
평시 = 감독·예산 감사·지방 협조
활성 작전 = 지정 구역·기간의 제한된 비상 지휘권
플레이어 = 현장 작전 지휘관 / 통치자 아님
```

### 보조 허브

Decision: `OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1`

```text
메인 1순위 = 이어하기·새 MapRun
보조 시설 = 주점·허브 병영·연구
영구 노드 = 유한·비용/선행/결과 공개
주점 = 결정론적 Hero+ 영입
병영 = 병사·병종·교리 sidegrade
연구 = 시스템·정보·편의 sidegrade
```

- 랜덤 유료 영입·무한 레벨·전 구간 전투/생산 배율·숨은 릴 확률 조작 금지.
- 기본 Profile로 모든 콘텐츠 완료 가능.
- balance는 노드·Retry 소비, total은 비감소 milestone 판정.
- 비용·노드 수·영웅 목록·능력·출전 상한은 pending.

### 병합 운영

Decision: `OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1`

- 현재 PR #119는 사용자 명시 지시로 조기 병합 preflight.
- 이후 승인 Grill Me Decision 10건마다 preflight.
- 10건은 강제 병합이 아니라 검증 시작 트리거.
- P0/P1·누락 권위·Sheet divergence·CI 실패·review thread·merge conflict가 있으면 병합 금지.
- 병합 뒤 Sheet를 merged main SHA와 `SYNCED_TO_MAIN / MERGE_VERIFIED`로 갱신하고 카운터 `0/10`.

## 4. 즉시 동기화 절차

```text
사용자 승인
→ GitHub 분야 정본·Ledger·Map·Context 갱신
→ commit
→ Sheet 결정·분야·감사·변경이력 갱신
→ bounded read-back
→ exact PR HEAD·CI 확인
→ premerge adversarial review
→ merge
→ main SHA·파일 재조회
→ Sheet SYNCED_TO_MAIN
```

`PARTIAL_SYNC_BLOCKED`, `SYNC_CONFLICT`, `OPEN_P0_OR_P1`이면 다음 중요 Decision 또는 병합으로 진행하지 않는다.

## 5. 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 세계·MapRun | `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` |
| 베일 존재론 | `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` |
| 오멘워드 조직·정치 | `docs/design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` |
| Profile 성장 | `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` |
| 주점·병영·연구 | `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` |
| 화면 | `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` |
| 병합 운영 | `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 작업 상태 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |

PR #116의 경로는 역사 증거이며 current local authority가 아니다.

## 6. 이번 동기화 예정 범위

- `00_프로젝트_허브!E2:L2`
- `01_작업순서`: 정치·보조 허브·병합 cadence 행.
- `02_현재_확정결정`: 같은 세 Decision ID.
- `04_누락_충돌_감사`: 정치 권한·영웅/훈련/연구·지갑 경쟁·병합 규칙·누락 권위 finding.
- `05_GDD_요약`: Base v9.4·CI·세계·Meta 최신화.
- `11_세계관`: 오멘워드·왕실·작전 권한.
- `13_주요인물`: 플레이어의 현장 지휘관 책임.
- `14_조연_세력_관계`: 루메른 왕국·오멘워드·왕실군·지방 행정.
- `41_성장_경제`: 영구재화·주점·병영·연구·Hero+ roster.
- `60_UX_UI_접근성`: 메인 작전 허브·노드 UX.
- `99_변경이력`: GitHub path·exact head·Sheet 범위·read-back·merge.

## 7. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- 정치 역할 승인을 왕실 인물·법률·지방 세력 상세 승인으로 확대.
- Hero+를 무한 전투력·필수 과금·랜덤 뽑기로 확대.
- 허브 병영과 MapRun TokenSource 병영의 책임 혼합.
- 연구를 숨은 릴 확률·생산량 전 구간 배율로 사용.
- PR #116 역사 파일을 검증 없이 current authority로 표시.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.
- PR head를 merged main SHA로 표시하거나 그 반대로 혼합.

## 8. 병합 후 상태

```text
SHEET_STATUS = SYNCED_TO_MAIN / MERGE_VERIFIED
GRILL_ME_COUNTER = 0_OF_10
NEXT_DECISION = OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
NEXT_WORK = NEW_BRANCH_AND_DRAFT_PR
```
