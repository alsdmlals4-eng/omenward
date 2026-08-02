# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / ACTIVE_DECISION_SYNC
current_grill_me_count: 2
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. 독립 정본이 아니며 GitHub 정본을 임의로 덮어쓰지 않는다.

`PROJECT_SHEET_CONFIGURED`는 Workbook 연결과 필수 탭 계약이 구성됐음을 뜻한다. GitHub 정본에 없는 Sheet-only 편집은 `PROPOSED_SHEET_CHANGE`다.

## 1. 상태 축

```text
Decision ID
Canonical authority path
Baseline main commit
Active planning PR head
Implementation status
Automated validation status
Human validation status
Sheet read-back status
Grill Me approval count
```

## 2. 주요 탭 역할

| 탭 | 역할 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·main/PR SHA·다음 Gate·카운터 |
| `01_작업순서` | 승인·선행/후속·병합 단계 |
| `02_현재_확정결정` | 같은 Decision ID의 승인 내용 |
| `04_누락_충돌_감사` | 적대적 finding·해결·검증·merge blocker |
| `05_GDD_요약` | 최신 게임플레이·Meta·구현 요약 |
| `15_조작_게임규칙` | 런 준비·등록·룰렛·배치 규칙 |
| `41_성장_경제` | 영구재화·주점·병영·연구·영웅 해금·등록 |
| `50_메인콘텐츠` | Stage·적 역할·영웅 활용 콘텐츠 |
| `60_UX_UI_접근성` | 메인 허브·주점·런 등록 화면·정보 위계 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1`

```text
기존 병종
→ 고정 대응 영웅
→ 주점 공개 노드에서 영구 해금
→ 런 시작 전 대응 병종에 등록
→ 등록된 영웅만 해당 런에서 사용 가능
```

- 영웅은 하나의 기존 `UnitArchetype`에 고정 연결한다.
- 해금은 영구 Profile 소유권, 등록은 해당 런의 사용 자격이다.
- 다른 병종에 교차 등록하지 않는다.
- 등록은 런 시작 스냅샷에 고정하며 런 중 변경하지 않는다.
- 등록은 즉시 전장 배치·전 구간 패시브·릴 odds 변경이 아니다.
- 미해금·미등록 기본 병종도 완전하고 전체 콘텐츠 완료가 가능해야 한다.
- 동시에 등록 가능한 수와 전장 등장 방식은 pending이다.

## 4. 기존 승인 연결

- 주점·허브 병영·연구는 유한 공개 영구 노드다.
- 영웅 해금은 랜덤 뽑기·유료 재굴림·중복 합성이 아니다.
- 세계관은 균열에서 넘어온 이계 생물종 수준으로 최소 노출한다.
- 게임 코어는 세 물리 릴 설계와 한 전선 비가역 커밋이다.

## 5. 동기화 절차

```text
사용자 승인
→ GitHub 분야 정본·Ledger·Map·Context 갱신
→ commit
→ Sheet 결정·분야·감사·변경이력 갱신
→ bounded read-back
→ exact PR HEAD·CI 확인
→ 승인 10건 또는 사용자 지시 시 preflight·merge
→ main·Sheet 재검증
```

`PARTIAL_SYNC_BLOCKED`, `SYNC_CONFLICT`, `OPEN_P0_OR_P1`이면 다음 중요 Decision 또는 병합으로 진행하지 않는다.

## 6. 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 영웅 해금·등록 | `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` |
| 주점·병영·연구 | `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` |
| Profile 성장 | `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` |
| 이계 생물종·경계파쇄자 | `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` |
| 화면 | `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` |
| 병합 운영 | `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 현재 작업 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |

## 7. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- 영웅 해금과 런 등록을 하나의 자동 적용으로 혼합.
- 영웅을 다른 병종에 자유 배속.
- 등록을 숨은 릴 확률 상승·전역 능력치 누적으로 처리.
- 영웅 미해금을 이유로 기본 병종을 불완전하게 설계.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 8. 현재 상태

```text
SHEET_STATUS = ACTIVE_DECISION_SYNC
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 2_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
PRODUCT_CODE = UNCHANGED
```
