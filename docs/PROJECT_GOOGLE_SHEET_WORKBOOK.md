# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
sheet_status: PROJECT_SHEET_CONFIGURED
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
active_base_version: 9.1.0
active_base_release_commit: 3c158f52cfdad889970aef4d6ce6650a6fea0645
active_base_evidence_commit: dd20ad3852e264d7e337e34d2cb963f71053a6cb
recommended_next_base: 9.3.0
current_audit_decision: OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1
last_verified_at: 2026-08-01
```

Google Sheets는 3릴·3전선·건물·경제·콘텐츠·플레이테스트의 전체 흐름을 사용자가 확인·수정하고 AI가 GitHub 정본·실제 구현과 함께 읽는 GDD 작업면이다. GitHub 책임 원본과 실제 code/data/Scene/test를 대체하지 않는다.

## 1. 검증된 탭

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

2026-08-01 감사에서 metadata와 위 25개 탭의 사용 셀을 재조회했다.

## 2. 상태·Commit 필드 의미

다음 값을 한 칸에 혼합하지 않는다.

| 필드 | 의미 |
|---|---|
| 활성 Base release SHA | `skills/PROJECT_BASE_ADAPTER.json`의 프로젝트 적용 Base release pin |
| Base evidence SHA | release와 분리된 Base 검증 증거 pin |
| Decision authority commit | 해당 Decision의 GitHub 책임 문서가 처음 정본화된 commit |
| 현재 PR head | Draft PR의 최신 통합 head; authority commit과 다를 수 있음 |
| Sheet sync | `SYNCED_TO_PR_HEAD`, `SYNCED_TO_MAIN`, `PROPOSED_SHEET_CHANGE` 등 동기화 위치 |
| 구현 상태 | 실제 code/data/Scene/Resource 반영 여부 |
| 검증 상태 | 자동·Runtime·접근성·성능·사람 검증 여부 |

`00_프로젝트_허브`의 `Base SHA`는 활성 Base release pin만 기록한다. 프로젝트 정본 commit과 PR head는 별도 필드로 기록한다.

## 3. 프로젝트 책임 매핑

| 의미 구조 | 현재 책임 원본 |
|---|---|
| 제품 정체성·핵심 루프 | `docs/PROJECT_CORE.md` |
| 전체 시스템 관계 | `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` |
| 전장·건설 노드 | `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md` |
| 세 물리 릴·이동·판정 | `docs/design/APPROVED_ROULETTE_CORE_RULES.md` |
| 20 Stage·콘텐츠·미션 | 관련 2026-07-31 APPROVED 계약 |
| 위험 Stage·보스 | `docs/design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md` |
| 패배·제품 유료 재시도 | `docs/design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md` |
| 벨루 | `docs/design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md` |
| 최신 Red 테스트 | `docs/testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 전체 Base·프로젝트·Sheet 감사 | `docs/audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md` |

과거 PR #92/#97, F-30, C1/C2/C3 proof는 삭제하지 않지만 현재 전체 제품 권위가 아니다. `HISTORICAL_APPROVED_SOURCE`, `LEGACY_PROVEN`, `LATEST_OVERRIDES_APPLY`로 해석한다.

## 4. 사용자 편집 처리

GitHub에 없는 사용자 수정은 자동 덮어쓰지 않는다.

```text
Sheet 수정
→ PROPOSED_SHEET_CHANGE
→ 현재 Decision·GitHub 정본·실제 구현과 비교
→ 기술 기본값/사용자 결정 분리
→ 승인
→ 같은 Decision ID로 GitHub 정본 반영
→ authority commit 기록
→ Sheet 반영
→ 양쪽 재조회
→ SYNCED 판정
```

## 5. 현재 검증 경계

```text
WORKBOOK_TABS: 25 / VERIFIED
LATEST_DECISION_SYNC: SYNCED_TO_PR_HEAD
ACTIVE_BASE: v9.1
BASE_V9_3: RECOMMENDED_NOT_ADOPTED
PRODUCT_IMPLEMENTATION: NOT_STARTED
LATEST_RED_TESTS: SPEC_WRITTEN_NOT_EXECUTED
PR_CHECKS: PARTIAL_FAILURE
RUNTIME_AND_HUMAN: NOT_RUN
```

Sheet 한 곳의 `APPROVED` 또는 `CURRENT`만으로 구현·검증 완료를 주장하지 않는다.