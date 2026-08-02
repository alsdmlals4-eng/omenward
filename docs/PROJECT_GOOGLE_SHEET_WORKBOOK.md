# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / ACTIVE_DECISION_SYNC
current_grill_me_count: 3
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
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
| `15_조작_게임규칙` | 룰렛·보관함 변환·전선 배치 규칙 |
| `41_성장_경제` | 영구재화·주점·영웅 명부·병영·연구 |
| `50_메인콘텐츠` | Stage·적 역할·영웅 활용 콘텐츠 |
| `60_UX_UI_접근성` | 메인 허브·주점·보관함 영웅 변환·정보 위계 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1`

```text
병종별 영웅 후보 복수 가능
→ 주점에서 영구 해금·Profile 명부 등록
→ 룰렛에서 같은 병종 [영웅] 등급 토큰 획득
→ 보관함에서 원본 유지 또는 해금 영웅 선택
→ 1토큰을 1유닛으로 변환
→ 한 전선에 비가역 배치
```

- 별도의 런 시작 전 영웅 등록·계약 단계는 없다.
- 병종 불일치·미해금 영웅은 변환 후보가 아니다.
- 변환하지 않은 원본 영웅 등급 병종도 정상 사용 가능하다.
- 변환은 추가 병력·전역 패시브·릴 odds 변경을 만들지 않는다.
- 배치 확정 전 취소 가능, 확정 뒤 undo·회수·판매·라인 변경 불가다.
- 동일 영웅 중복 배치와 동병종 활성 상한은 pending이다.

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
| 영웅 해금·명부 | `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` |
| 영웅 토큰 변환·배치 | `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` |
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
- 영웅 미해금을 이유로 원본 영웅 등급 병종을 불완전하게 설계.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 8. 현재 상태

```text
SHEET_STATUS = ACTIVE_DECISION_SYNC
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 3_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
PRODUCT_CODE = UNCHANGED
```
