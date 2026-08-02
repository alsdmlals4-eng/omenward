# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PASS / CI_3_GREEN
current_grill_me_count: 6
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1
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
| `12_핵심루프` | 맵 선택·MapRun·Stage·Wave·정산·정비시간 흐름 |
| `15_조작_게임규칙` | Stage 중 운영 기능·룰렛·보관함·active hero·전선 배치 규칙 |
| `40_핵심시스템_메인콘텐츠` | Stage/Wave 상태기·정비시간·전장 시스템 연결 |
| `41_성장_경제` | 영구재화·주점·영웅 명부·병영·연구 |
| `50_메인콘텐츠` | 맵·Stage·Wave·미션·선택지·적 역할 콘텐츠 |
| `60_UX_UI_접근성` | Stage/Wave/정비시간·보관함·active hero 표시 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1`

```text
맵 선택
→ MapRun 생성·RunState 초기화
→ Stage
→ Stage 내부 Wave 1...N
   ↔ 건설·업그레이드·수리
   ↔ 룰렛 조작과 병력 확보
   ↔ 보관함 관리
   ↔ 병력 배치
→ Stage 정산·checkpoint
→ 정비시간: 전투·Wave 일시정지, 미션·선택지 처리
→ 다음 Stage
```

- 현재 MapRun 목표는 20 Stage다.
- 각 Stage는 맵·Stage 데이터가 정의한 하나 이상의 Wave로 구성된다.
- `라운드`는 별도 상태가 아니며 공식 용어는 `Wave / 웨이브`다.
- Wave 사이에는 기본 정비시간을 두지 않고 Stage 종료 뒤 한 번만 발생한다.
- 위험 Stage에서도 Stage 경계 정비시간은 존재한다.
- 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치는 Stage 진행 중에도 사용 가능하다.
- 정비시간 중 경제·건설·수리·회복·쿨다운 clock matrix는 pending이다.
- MapRun 초기화는 RunState만 초기화하며 Profile 영구 해금을 지우지 않는다.
- 정비시간 진입은 active 영웅 슬롯 해제 사건이 아니다.

## 4. 동기화 증거

```text
PR #121 verified head before workbook closure commit:
20e5fd1fb446dc03fadafb90c22305d786b1d499

SHEET_BOUNDED_READBACK: PASS
REQUIRED_CI_AT_VERIFIED_HEAD:
- Project Core Documentation run 559: PASS
- GDD Sheet Adoption run 270: PASS
- Base v9 adoption run 245: PASS
```

동기화 범위:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A21:N21`
- `02_현재_확정결정!A30:M30`
- `04_누락_충돌_감사!A78:H83`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A6:J7`
- `15_조작_게임규칙!A10:J10`
- `40_핵심시스템_메인콘텐츠!A9:J10`
- `50_메인콘텐츠!A16:J17`
- `60_UX_UI_접근성!A17:J18`
- `99_변경이력!A31:H31`

## 5. 기존 승인 연결

- 병종별 영웅 후보는 복수 해금 가능하고 Profile 명부에 등록된다.
- 별도의 pre-run 영웅 편성·계약은 없다.
- 영웅 변환은 `1토큰 → 1유닛`이며 보너스 유닛과 릴 odds 변경이 없다.
- 전장 전체 이름 지정 active 영웅은 최대 1명이다.
- 동일 영웅도 이전 인스턴스 종료 뒤 새 토큰으로 반복 출전할 수 있다.
- 원본 영웅 등급 병종 유닛은 영웅 미해금·active slot 점유 중에도 정상 사용 가능하다.
- 영웅은 수동 퇴각·교대할 수 없고 Stage·Act·정비시간에 동일 인스턴스로 유지된다.
- 게임 코어는 세 물리 릴 설계와 한 전선 비가역 커밋이다.

## 6. 동기화 절차

```text
사용자 승인
→ GitHub 분야 정본·Core·Ledger·Map·Context 갱신
→ commit
→ Sheet 결정·분야·감사·변경이력 갱신
→ bounded read-back
→ exact PR HEAD·CI 확인
→ 승인 10건 또는 사용자 지시 시 preflight·merge
→ main·Sheet 재검증
```

`PARTIAL_SYNC_BLOCKED`, `SYNC_CONFLICT`, `OPEN_P0_OR_P1`이면 다음 중요 Decision 또는 병합으로 진행하지 않는다.

## 7. 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 맵·MapRun·Stage·Wave·정비시간 | `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` |
| 영웅 해금·명부 | `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` |
| 영웅 토큰 변환·배치 | `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` |
| 영웅 단일 활성·반복 출전 | `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` |
| 영웅 퇴각·교대·active 종료 | `docs/design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md` |
| 주점·병영·연구 | `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` |
| Profile 성장 | `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` |
| 이계 생물종·경계파쇄자 | `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` |
| 화면 | `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` |
| 병합 운영 | `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` |
| 실제 구현 | `docs/CURRENT_IMPLEMENTATION_STATUS.md`와 실제 파일 |
| 현재 작업 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |

## 8. 금지

- Sheet-only 변경을 승인 Decision으로 처리.
- MapRun 초기화로 Profile 영구 해금을 삭제.
- Stage와 Wave를 같은 상태로 처리.
- `라운드`를 Wave와 별개인 중복 상태로 추가.
- 정비시간을 건설·룰렛·보관함·배치가 가능한 유일한 구간으로 처리.
- Stage 진행 중 네 가지 운영 기능을 일괄 차단.
- 정비시간을 무한 무료 생산·수리·회복 시간으로 간주.
- 위험 Stage라는 이유로 Stage 경계 정비시간을 제거.
- 영웅 해금을 모든 런의 자동 효과로 처리.
- 영웅을 다른 병종에 자유 배속.
- 별도 pre-run 영웅 계약을 다시 도입.
- 영웅 변환을 숨은 릴 확률 상승·전역 능력치·보너스 유닛으로 처리.
- 이름·병종·전선을 달리해 active Hero 1명 제한을 우회.
- 동일 영웅 반복 출전을 한 런 1회 제한으로 오해.
- 수동 퇴각·교대·재화 취소권을 추가.
- Stage·Act·정비시간마다 active 슬롯을 자동 해제.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 9. 현재 상태

```text
SHEET_STATUS = READBACK_PASS / CI_3_GREEN
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 6_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1
PRODUCT_CODE = UNCHANGED
```