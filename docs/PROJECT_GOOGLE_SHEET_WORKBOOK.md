# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
current_operating_gate: OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-SIGNATURE-CONCEPTS-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3
last_merged_planning_pr: 127
current_planning_pr: 129
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PASS / CANDIDATE_CI_GREEN / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED
current_grill_me_count: 4
preflight: NEXT_AT_10_OF_10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
last_full_audit: 2026-08-02
```

Google Sheet는 사용자 계획 작업면이며 GitHub가 기획 정본이다. 같은 Decision ID·PR SHA·구현 경계를 함께 표시한다.

## 1. 현재 동기화 Decision

`OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1`

```text
shield_guard / 방패병   → PASSIVE
archer / 궁병           → PASSIVE
assassin / 암살자       → PASSIVE
priest / 사제           → AUTOMATIC_ACTIVE_SKILL
mage / 마법사           → AUTOMATIC_ACTIVE_SKILL
```

```text
INITIAL_HERO_COUNT = 5
UNIQUE_SOURCE_ARCHETYPE_COUNT = 5
PASSIVE_COUNT = 3
AUTOMATIC_ACTIVE_COUNT = 2
INITIAL_ROSTER_IS_FINAL_CAP = FALSE
```

- 최신 사용자 직접 선택이 이전 4명·2:2 수량을 대체한다.
- 구체 영웅 이름·효과·상쇄 축·수치는 pending이다.
- 거인·기병은 초기 5명에서 제외한다.
- 초기 5명은 완전 신규 유닛이 아니라 원본 병종 자산을 재사용하는 스킨형 변주다.

## 2. 검증 역할

| 병종 | 검증 역할 |
|---|---|
| 방패병 | frontline·nearest·ranged defense |
| 궁병 | ranged·flying priority·anti-air |
| 암살자 | bypass·backline priority |
| 사제 | support·lowest-health ally |
| 마법사 | ranged control·cluster priority |

궁병과 마법사의 중복은 지속 대공과 군집 광역 자동 스킬로 분리한다.

## 3. Sheet 동기화 범위

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A30:N31`
- `02_현재_확정결정!A38:M39`
- `04_누락_충돌_감사!A137:H144`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A15:J15`
- `15_조작_게임규칙!A18:J18`
- `40_핵심시스템_메인콘텐츠!A18:J18`
- `41_성장_경제!A28:I28`
- `50_메인콘텐츠!A25:J25`
- `60_UX_UI_접근성!A26:J26`
- `70_아트_오디오_에셋!A9:J9`
- `99_변경이력!A41:H41`

bounded read-back:

```text
SAME_DECISION_ID = PASS
GRILL_ME_COUNT = 4_OF_10
INITIAL_HERO_COUNT = 5
EXACT_ARCHETYPES = PASS
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
STALE_FOUR_COUNT_MARKED_REFINED = PASS
INITIAL_ROSTER_IS_FINAL_CAP = FALSE
PRODUCT_STATUS = NOT_IMPLEMENTED
```

## 4. 후보 HEAD 검증

후보 증거 HEAD:

`e8bdec8cd20022f9afc2e86468da103359a794f7`

```text
Validate Project Core Documentation: PASS / run 679
Validate Omenward GDD Sheet Adoption: PASS / run 399
Validate Base v9 adoption: PASS / run 380
SHEET_READBACK = PASS
```

이 Workbook 마감 커밋으로 PR HEAD가 이동하므로 최종 exact HEAD에서 필수 CI·latest main compare·Sheet SHA·review surface·blocker를 다시 확인한다.

## 5. 감사 기준

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
FIVE_FULL_NEW_UNITS = FORBIDDEN
PRODUCT_IMPLEMENTED = FALSE
```

## 6. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`

## 7. 구현·검증 경계

```text
PROJECT_SHEET_CONFIGURED
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
INITIAL_HERO_COUNT = 5
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
EXACT_HERO_IDENTITIES = PENDING
EXACT_SIGNATURE_EFFECTS = PENDING
EXACT_COMPENSATION_AXES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영·다음 Gate

- 현재 카운터는 `4/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-SIGNATURE-CONCEPTS-V1
```
