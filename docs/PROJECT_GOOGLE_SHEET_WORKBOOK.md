# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / ACTIVE_DECISION_SYNC
current_grill_me_count: 1
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1
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
| `05_GDD_요약` | 최신 세계·게임플레이·Meta·구현 요약 |
| `11_세계관` | MapRun·베일·이계 생물종·오멘워드 |
| `14_조연_세력_관계` | 이계 생물종·경계파쇄자·조직 관계 |
| `21_스테이지_콘텐츠` | Act·Stage·적 역할·위험 패키지 |
| `41_성장_경제` | 영구재화·주점·병영·연구·Readiness·Retry |
| `60_UX_UI_접근성` | 메인 작전 허브·노드 그래프·화면 정보 위계 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1`

```text
사용자 노출 = 균열에서 넘어온 이계 생물종
내부 통칭 = 베일종
단일 종족·제국 = 요구하지 않음
상세 정치·외교·우주론 = 현재 범위 밖
경계파쇄자 = 균열 고정·확장 보스급 생물
```

### 게임플레이 역할 분류

```text
군집형 / 돌격형 / 원거리형 / 방호형 / 교란형 / 공성형 / 경계파쇄자
```

- 역할 분류는 정확한 최종 적 명단이 아니다.
- 각 적은 관측 행동·위협 대상·대응법·실패 원인을 가져야 한다.
- 장문의 설정 설명 없이 전조·행동·결과 로그로 전달한다.
- 세계관 확장은 멈추고 다음 Decision부터 실제 게임 구조를 설계한다.

## 4. 기존 승인 연결

- MapRun은 별개의 실제 경계 공세.
- 베일은 비의지적 경계 겹침.
- 오멘워드는 루메른 왕실 인가 자율 경계대응단.
- 메인 허브는 주점·허브 병영·연구.
- 정산 영구재화로 유한 공개 노드 개방.
- 영웅 영입은 결정론적 공개 노드.
- 영웅의 런 참여 방식은 다음 Decision에서 확정.

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
| 세계·MapRun | `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` |
| 베일 존재론 | `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` |
| 이계 생물종·경계파쇄자 | `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` |
| 오멘워드 조직 | `docs/design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` |
| Profile 성장 | `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` |
| 주점·병영·연구 | `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` |
| 화면 | `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` |
| 병합 운영 | `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 현재 작업 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |

## 7. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- 베일종 승인을 단일 제국·상세 외교 승인으로 확대.
- 사용자에게 세계관을 알아야만 전투할 수 있는 구조 강요.
- 경계파쇄자를 단순 체력 보스로 축소.
- Hero+를 무한 전투력·필수 과금·랜덤 뽑기로 확대.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 8. 현재 상태

```text
SHEET_STATUS = ACTIVE_DECISION_SYNC
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 1_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1
PRODUCT_CODE = UNCHANGED
```
