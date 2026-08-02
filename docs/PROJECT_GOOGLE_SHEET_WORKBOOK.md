# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PENDING / CI_PENDING
current_grill_me_count: 8
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. 독립 정본이 아니며 GitHub 정본을 임의로 덮어쓰지 않는다.

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
| `12_핵심루프` | 맵런·Stage 정산·영웅 생존/사망·재출전 흐름 |
| `15_조작_게임규칙` | 영웅 토큰 변환·post-death provenance·새 인스턴스 규칙 |
| `40_핵심시스템_메인콘텐츠` | Hero active slot·token provenance·fresh instance transaction |
| `41_성장_경제` | 영구재화·주점·영웅 명부·사망 회수 보상 금지 |
| `50_메인콘텐츠` | 영웅 사망·사망 이후 룰렛 결과·재출전 연결 |
| `60_UX_UI_접근성` | 사망 무보상·사망 이후 새 결과 필요·초기 상태 표시 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1`

```text
Hero death or complete removal
→ end old unit instance and clear active Hero slot
→ no source-token return and no death recovery reward
→ pre-death stored Hero-grade tokens remain original-unit options only
→ obtain a new matching [영웅] result from Roulette after the death event
→ verify token.created_sequence > previous_hero.ended_sequence
→ consume one eligible token and create one fresh named-Hero instance
→ deploy irreversibly to one lane
```

- 이름 지정 영웅의 첫 출전에는 기본 토큰 변환 조건을 적용한다.
- 영웅 사망은 소비한 source token·토큰 조각·회수권·부활권·무료 재배치권을 반환하지 않는다.
- 사망 자체는 골드·식량·런 재화·영구재화·보장 토큰·다음 스핀 pity를 생성하지 않는다.
- 별도의 Stage·미션·선택지·적 처치 정상 보상은 이 무회수 규칙의 대상이 아니다.
- 사망 전에 보관한 동병종 `[영웅]` 등급 토큰은 원본 영웅 등급 병종으로는 사용할 수 있다.
- 사망 전 보관 토큰은 이름 지정 영웅의 사망 후 재출전에 사용할 수 없다.
- 이름 지정 영웅 재출전에는 사망 이후 룰렛에서 새로 확정된 동병종 `[영웅]` 등급 토큰이 필요하다.
- 일반·다른 등급·병종 불일치 토큰은 사용할 수 없다.
- 새 적격 영웅 인스턴스는 최대 HP, 남은 쿨다운 `0`, 능력 기본 사용 횟수·충전, 능력 초기 고유 자원으로 시작한다.
- 고유 자원 초기값은 능력 계약이 정하며 별도 명시가 없으면 `0`이다.
- 이전 사망 인스턴스의 HP·쿨다운·충전·고유 자원·일시 상태·파생 개체를 승계하지 않는다.
- 동일 hero_id를 다시 선택해도 새 unit_instance_id와 deployment_id를 만든다.
- 사망·슬롯 해제 transaction과 provenance 검증·토큰 소비·새 유닛 생성 transaction을 분리한다.

## 4. 재동기화 후보

```text
PR #121 candidate head before Sheet correction:
44744647546e3b8b1c4d1111284dcfb2cface056

SHEET_BOUNDED_READBACK: PENDING
REQUIRED_CI_AT_CANDIDATE_HEAD: PENDING
```

재동기화 예정 범위:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!D23:N23`
- `02_현재_확정결정!D32:M32`
- `04_누락_충돌_감사!A91:H91`
- `04_누락_충돌_감사!A95:H96`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!C9:J9`
- `15_조작_게임규칙!C12:J12`
- `40_핵심시스템_메인콘텐츠!C12:J12`
- `41_성장_경제!C22:I22`
- `50_메인콘텐츠!C19:J19`
- `60_UX_UI_접근성!C20:J20`
- `99_변경이력!D33:H33`

## 5. 기존 승인 연결

- 공식 게임 진행 계층은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- 네 가지 런 운영 기능은 Stage 전투 중과 정비시간 모두 사용할 수 있다.
- 병종별 영웅 후보는 복수 해금 가능하고 Profile 명부에 등록된다.
- 별도의 pre-run 영웅 편성·계약은 없다.
- 영웅 변환은 `1토큰 → 1유닛`이며 보너스 유닛과 릴 odds 변경이 없다.
- 전장 전체 이름 지정 active 영웅은 최대 1명이다.
- 영웅은 수동 퇴각·교대할 수 없고 Stage·Act·정비시간에 동일 인스턴스로 유지된다.
- 생존 인스턴스의 HP·쿨다운·충전·고유 자원은 Stage 경계를 넘어 유지하고 일시 전투 상태는 제거한다.
- 사망한 인스턴스에는 생존 persistent-state 규칙을 적용하지 않으며 회수 보상도 없다.
- 사망 후 이름 지정 영웅 반복 출전은 post-death token provenance를 요구한다.
- 게임 코어는 세 물리 릴 설계와 한 전선 비가역 커밋이다.

## 6. 동기화 절차

```text
사용자 승인
→ GitHub 분야 정본·관련 계약·Ledger·Map·Context 갱신
→ candidate commit
→ Sheet 결정·분야·감사·변경이력 교정
→ bounded read-back
→ candidate HEAD·CI 확인
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
| 영웅 사망 무회수·post-death 결과·새 인스턴스 초기 상태 | `docs/design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` |
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
- 영웅 사망 시 source token·재화·회수권·부활권·무료 재배치권을 생성.
- 영웅 사망으로 다음 룰렛 영웅 확률·보장·pity를 변경.
- 사망 전에 보관한 영웅 등급 토큰으로 사망 후 이름 지정 영웅을 재출전.
- 일반·다른 등급·병종 불일치 토큰을 이름 지정 영웅으로 승격.
- 새 영웅 인스턴스에 이전 사망 인스턴스 상태를 승계.
- 저장·재시도로 토큰 하나에서 영웅 둘을 생성.
- Stage마다 생존 영웅 HP·쿨다운·충전·고유 자원을 무료 초기화.
- 정비시간 체류로 생존 영웅 상태를 회복.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 9. 현재 상태

```text
SHEET_STATUS = READBACK_PENDING / CI_PENDING
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 8_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
PRODUCT_CODE = UNCHANGED
```