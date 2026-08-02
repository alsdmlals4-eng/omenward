# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
current_operating_gate: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3
last_merged_planning_pr: 127
current_planning_pr: 129
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PASS / CANDIDATE_CI_GREEN / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED
current_grill_me_count: 2
preflight: NEXT_AT_10_OF_10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. GitHub가 기획 정본이며 Sheet는 같은 Decision ID와 PR SHA를 표시한다.

## 1. 현재 동기화 Decision

Decision:

`OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1`

```text
원본 [영웅] 등급 병종 데이터 복사
→ 영웅 전용 패시브 또는 자동 [사용스킬] 하나 적용
→ 직접 관련된 상쇄 축 하나만 하향·조건화
→ 나머지 원본 데이터 유지
```

- 영웅 전용 차이와 상쇄 축은 각각 정확히 하나다.
- 상쇄 축은 차이의 가치와 직접 연결돼야 한다.
- 여러 스탯 동시 조정·전체 성장 곡선 재설계·모든 영웅 공통 세금은 금지한다.
- 조건 의존도를 상쇄로 쓰는 경우 조건 미충족 구간에서 실제 저점이 발생해야 한다.
- 원본 병종이 더 나은 대표 상황을 유지한다.
- 정확 상쇄 수치·허용 편차·표본 수는 simulation 전까지 pending이다.

## 2. 이전 승인 연결

```text
기존 병종 [영웅] 등급 유닛
+ 스킨·이름·최소 식별 연출
+ PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
- ONE_RELATED_COMPENSATION_AXIS
= 이름 지정 영웅
```

- 원본 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- `[사용스킬]`은 수동 버튼이 아닌 규칙 기반 자동 발동이다.
- 고유 자원·궁극기·신규 AI·전체 신규 애니메이션은 기본 금지다.

## 3. Sheet 동기화 범위

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A29:N29`
- `02_현재_확정결정!A37:M37`
- `04_누락_충돌_감사!A122:H128`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A13:J13`
- `15_조작_게임규칙!A16:J16`
- `40_핵심시스템_메인콘텐츠!A16:J16`
- `41_성장_경제!A26:I26`
- `50_메인콘텐츠!A23:J23`
- `60_UX_UI_접근성!A24:J24`
- `99_변경이력!A39:H39`

bounded read-back:

```text
SAME_DECISION_ID = PASS
GRILL_ME_COUNT = 2_OF_10
SOURCE_PROFILE_INHERITANCE = PASS
ONE_RELATED_COMPENSATION_AXIS = PASS
PRODUCT_STATUS = NOT_IMPLEMENTED
```

## 4. 후보 HEAD 검증

후보 증거 HEAD:

`b34dd6179af8d1ad7fe4b16fba88db2125c6c1f9`

```text
Validate Project Core Documentation: PASS / run 663
Validate Omenward GDD Sheet Adoption: PASS / run 383
Validate Base v9 adoption: PASS / run 364
SHEET_READBACK = PASS
```

이 Workbook 마감 커밋으로 PR HEAD가 이동하므로 최종 exact HEAD에서 필수 CI·latest main compare·Sheet SHA를 다시 확인한다.

## 5. 감사 기준

```text
SIGNATURE_DELTA_COUNT = 1
COMPENSATION_AXIS_COUNT = 1
COMPENSATION_MUST_BE_CAUSALLY_RELATED = TRUE
ALL_OTHER_SOURCE_AXES_INHERITED = TRUE
FULL_STAT_REDESIGN = FORBIDDEN
FREE_SIGNATURE_POWER = FORBIDDEN
PRODUCT_IMPLEMENTED = FALSE
```

## 6. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`

## 7. 구현·검증 경계

```text
PROJECT_SHEET_CONFIGURED
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_HERO_VARIANTS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영·다음 Gate

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 현재 카운터는 `2/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 제품 코드 PR은 별도 계약 대상이다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
```
