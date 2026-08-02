# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PASS / CI_3_GREEN
current_grill_me_count: 7
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1
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
| `12_핵심루프` | 맵 선택·MapRun·Stage·Wave·정산·정비시간·영웅 정산 흐름 |
| `15_조작_게임규칙` | Stage 중 운영 기능·영웅 상태 지속·룰렛·보관함·전선 배치 규칙 |
| `40_핵심시스템_메인콘텐츠` | Stage/Wave 상태기·정비시간·Hero persistent/transient 상태기 |
| `41_성장_경제` | 영구재화·주점·영웅 명부·병영·연구 |
| `50_메인콘텐츠` | 맵·Stage·Wave·미션·선택지·영웅 장기 손상·적 역할 콘텐츠 |
| `60_UX_UI_접근성` | Stage/Wave/정비시간·영웅 장기 상태·보관함·active hero 표시 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1`

```text
Stage final combat tick
→ damage and Hero death resolution
→ if alive: clear transient combat state and transient child entities
→ capture current HP·remaining cooldowns·charges·uses·unique resources
→ atomic Stage settlement and checkpoint
→ MaintenancePhase: Hero recovery/cooldown/charge/resource clocks paused
→ next Stage: restore the same Hero instance on the same lane
```

- 살아 있는 영웅의 현재 HP·남은 쿨다운·사용 횟수·충전·고유 자원은 다음 Stage에 현재 값 그대로 유지한다.
- 일시 버프·디버프·타깃·어그로·공격/시전 상태는 Stage 정산에서 제거한다.
- 투사체·장판·함정·일시 소환물과 제거된 객체 참조는 Stage 정산에서 제거한다.
- 영웅의 영구 패시브·Profile 해금·영속 능력은 유지한다.
- 정비시간에는 영웅 HP 회복·쿨다운·충전·고유 자원 clock이 진행되지 않는다.
- Stage 경계는 무료 전회복·스킬 초기화·충전 회복·영웅 교체 사건이 아니다.
- 사망 영웅은 persistent snapshot을 만들지 않고 기존 Hero Exit 규칙에 따라 active 슬롯을 해제한다.
- persistent snapshot은 최종 전투 틱과 사망 판정 뒤 원자 저장하고 동일 영웅 인스턴스에 한 번만 복원한다.
- 사망 뒤 새 토큰으로 생성하는 새 영웅 인스턴스의 초기 상태는 pending이다.

## 4. 동기화 증거

```text
PR #121 verified head before workbook closure commit:
85e6669631d57e8879bffc59611a06c10d3d2d4e

SHEET_BOUNDED_READBACK: PASS
REQUIRED_CI_AT_VERIFIED_HEAD:
- Project Core Documentation run 567: PASS
- GDD Sheet Adoption run 281: PASS
- Base v9 adoption run 256: PASS
```

동기화 범위:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A22:N22`
- `02_현재_확정결정!A31:M31`
- `04_누락_충돌_감사!A84:H89`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A8:J8`
- `15_조작_게임규칙!A11:J11`
- `40_핵심시스템_메인콘텐츠!A11:J11`
- `50_메인콘텐츠!A18:J18`
- `60_UX_UI_접근성!A19:J19`
- `99_변경이력!A32:H32`

## 5. 기존 승인 연결

- 공식 게임 진행 계층은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- 네 가지 런 운영 기능은 Stage 전투 중과 정비시간 모두 사용할 수 있다.
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
→ GitHub 분야 정본·Ledger·Map·Context·관련 계약 갱신
→ commit
→ Sheet 결정·분야·감사·변경이력 갱신
→ bounded read-back
→ exact PR HEAD·CI 확인
→ Workbook closure commit
→ final exact HEAD·CI·PR·review·changed-path 확인
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
| 영웅 Stage 상태 지속·전투 잔여물 정리·정비 clock | `docs/design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md` |
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
- 일반 정비시간을 무한 무료 생산·수리 시간으로 간주.
- 위험 Stage라는 이유로 Stage 경계 정비시간을 제거.
- 영웅 해금을 모든 런의 자동 효과로 처리.
- 영웅을 다른 병종에 자유 배속.
- 별도 pre-run 영웅 계약을 다시 도입.
- 영웅 변환을 숨은 릴 확률 상승·전역 능력치·보너스 유닛으로 처리.
- 이름·병종·전선을 달리해 active Hero 1명 제한을 우회.
- 동일 영웅 반복 출전을 한 런 1회 제한으로 오해.
- 수동 퇴각·교대·재화 취소권을 추가.
- Stage·Act·정비시간마다 active 슬롯을 자동 해제.
- Stage마다 영웅 HP·쿨다운·충전·고유 자원을 무료 초기화.
- 정비시간 체류로 영웅 HP·쿨다운·충전·고유 자원을 회복.
- 이전 Stage의 일시 버프·디버프·투사체·장판·일시 소환물을 다음 Stage로 이월.
- 최종 전투 틱 사망보다 먼저 persistent snapshot을 저장.
- 저장·로드로 영웅 상태를 복제하거나 새 영웅을 자동 생성.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 9. 현재 상태

```text
SHEET_STATUS = READBACK_PASS / CI_3_GREEN
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 7_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1
PRODUCT_CODE = UNCHANGED
```