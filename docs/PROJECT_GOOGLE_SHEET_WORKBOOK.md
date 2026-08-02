# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
current_operating_gate: OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-CONCEPTS-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3
last_merged_planning_pr: 127
current_planning_pr: 129
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PASS / CANDIDATE_CI_GREEN / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED
current_grill_me_count: 5
preflight: NEXT_AT_10_OF_10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. GitHub가 기획 정본이며 Sheet는 같은 Decision ID와 PR SHA를 표시한다.

## 1. 현재 동기화 Decision

`OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1`

```text
원본 병종 [영웅] 등급 기본 전투 성능
+ 이름·초상·스킨·식별 연출
+ 고유 자동 사용스킬 1개
= 제한형 상위호환 이름 지정 영웅
```

```text
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1_PER_HERO
MANDATORY_COMPENSATION_AXIS_COUNT = 0
SOURCE_BASELINE_STATS = INHERITED
GLOBAL_ACTIVE_NAMED_HERO_CAP = 1
```

- 이름 지정 영웅은 원본보다 조금 더 강하고 임팩트 있는 해금 보상이다.
- 이전 패시브 선택 구조·강제 상쇄 축·평균 예산 동등 sidegrade는 현행 정본이 아니다.
- 스킬은 규칙 기반 자동 발동하며 수동 버튼·수동 타깃은 없다.
- 정확 영웅·스킬·cooldown·VFX/SFX·수치는 pending이다.

## 2. 초기 5명

```text
shield_guard / archer / priest / mage / assassin
→ 각 병종 이름 지정 영웅 1명
→ 고유 자동 사용스킬 1개씩
```

```text
INITIAL_HERO_COUNT = 5
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
FINAL_RELEASE_CAP = FALSE
```

## 3. Sheet 동기화 범위

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A32:N32`
- `02_현재_확정결정!A40:M40`
- `04_누락_충돌_감사!A145:H152`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A16:J16`
- `15_조작_게임규칙!A19:J19`
- `40_핵심시스템_메인콘텐츠!A19:J19`
- `41_성장_경제!A29:I29`
- `50_메인콘텐츠!A26:J26`
- `60_UX_UI_접근성!A27:J27`
- `70_아트_오디오_에셋!A10:J10`
- `99_변경이력!A42:H42`

bounded read-back:

```text
SAME_DECISION_ID = PASS
GRILL_ME_COUNT = 5_OF_10
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 5_INITIAL
MANDATORY_COMPENSATION_AXIS_COUNT = 0
GLOBAL_ACTIVE_NAMED_HERO_CAP = 1
PRODUCT_STATUS = NOT_IMPLEMENTED
```

## 4. 후보 HEAD 검증

후보 증거 HEAD:

`e32d4c7cf0a88ff2d275764b4ef3a9dea77aee97`

```text
Validate Project Core Documentation: PASS / run 692
Validate Omenward GDD Sheet Adoption: PASS / run 412
Validate Base v9 adoption: PASS / run 393
SHEET_READBACK = PASS
```

이 Workbook 마감 커밋으로 PR HEAD가 이동하므로 최종 exact HEAD에서 필수 CI·latest main compare·Sheet SHA를 다시 확인한다.

## 5. 감사 기준

```text
EVERY_NAMED_HERO_HAS_UNIQUE_ACTIVE_SKILL = TRUE
UNIQUE_ACTIVE_SKILL_COUNT_PER_HERO = 1
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
MANDATORY_COMPENSATION_AXIS_COUNT = 0
SOURCE_BASELINE_INHERITED = TRUE
NAMED_HERO_GLOBAL_ACTIVE_CAP = 1
PRODUCT_IMPLEMENTED = FALSE
```

## 6. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` — `SUPERSEDED_HISTORY`

## 7. 구현·검증 경계

```text
PROJECT_SHEET_CONFIGURED
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILLS = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영·다음 Gate

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 현재 카운터는 `5/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 제품 코드 PR은 별도 계약 대상이다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-CONCEPTS-V1
```
