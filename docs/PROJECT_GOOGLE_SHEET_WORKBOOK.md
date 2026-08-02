# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / ACTIVE_DECISION_SYNC
current_grill_me_count: 4
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1
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
| `15_조작_게임규칙` | 룰렛·보관함 변환·active hero·전선 배치 규칙 |
| `41_성장_경제` | 영구재화·주점·영웅 명부·병영·연구 |
| `50_메인콘텐츠` | Stage·적 역할·영웅 활용 콘텐츠 |
| `60_UX_UI_접근성` | 메인 허브·주점·보관함 영웅 변환·active slot 표시 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1`

```text
전장 전체 active Hero 최대 1명
→ active Hero가 없을 때만 영웅 등급 토큰을 해금 영웅으로 변환
→ 이전 인스턴스 종료 뒤 동일 hero_id도 새 토큰으로 반복 출전 가능
```

- 상·중·하 전선을 합쳐 이름 지정 영웅 유닛은 동시에 최대 1명이다.
- 서로 다른 영웅도 동시에 둘 이상 배치할 수 없다.
- 같은 영웅도 이전 인스턴스가 종료된 뒤 반복 배치할 수 있다.
- 반복 출전마다 별도의 동병종 `[영웅]` 등급 토큰 1개를 소비한다.
- active hero가 있으면 새 토큰은 보관하거나 원본 영웅 등급 병종 유닛으로 배치한다.
- 제한 때문에 토큰을 소멸시키거나 기존 영웅을 자동 교체하지 않는다.
- 수동 퇴각·교대·Stage 유지·반복 초기화 계약은 pending이다.

## 4. 기존 승인 연결

- 병종별 영웅 후보는 복수 해금 가능하고 Profile 명부에 등록된다.
- 별도의 pre-run 영웅 편성·계약은 없다.
- 영웅 변환은 `1토큰 → 1유닛`이며 보너스 유닛과 릴 odds 변경이 없다.
- 원본 영웅 등급 병종 유닛은 영웅 미해금·active slot 점유 중에도 정상 사용 가능하다.
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
| 영웅 해금·명부 | `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` |
| 영웅 토큰 변환·배치 | `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` |
| 영웅 단일 활성·반복 출전 | `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` |
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
- 영웅 해금을 모든 런의 자동 효과로 처리.
- 영웅을 다른 병종에 자유 배속.
- 별도 pre-run 영웅 계약을 다시 도입.
- 영웅 변환을 숨은 릴 확률 상승·전역 능력치·보너스 유닛으로 처리.
- 이름·병종·전선을 달리해 active Hero 1명 제한을 우회.
- 동일 영웅 반복 출전을 한 런 1회 제한으로 오해.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 8. 현재 상태

```text
SHEET_STATUS = ACTIVE_DECISION_SYNC
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 4_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1
PRODUCT_CODE = UNCHANGED
```
