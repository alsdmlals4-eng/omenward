# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
current_operating_gate: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3
last_merged_planning_pr: 127
current_planning_pr: 129
sheet_status: PROJECT_SHEET_CONFIGURED / SYNC_TO_PR_129_IN_PROGRESS
current_grill_me_count: 1
preflight: NEXT_AT_10_OF_10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. GitHub가 기획 정본이며 Sheet는 같은 Decision ID와 PR SHA를 표시한다.

## 1. 현재 동기화 Decision

Decision:

`OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1`

```text
기존 병종 [영웅] 등급 유닛
+ 영웅 전용 스킨·이름·최소 식별 연출
+ 패시브 1개 또는 자동 [사용스킬] 1개
= 이름 지정 영웅
```

- 영웅 전용 차이는 정확히 하나다.
- `PASSIVE XOR AUTOMATIC_ACTIVE_SKILL`이다.
- `[사용스킬]`은 규칙 기반 자동 발동이며 수동 버튼·수동 타깃은 없다.
- 원본 병종의 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 기본적으로 고유 자원·공통 궁극기·신규 AI·전체 신규 애니메이션을 만들지 않는다.
- 스킨형 제작량을 목표로 하되 단일 차이는 실제 전술 선택을 바꾼다.
- 전투 예산 상쇄와 원본 병종 선택 상황을 유지한다.

## 2. 주요 탭 동기화 목적

| 탭 | 이번 Decision 반영 내용 |
|---|---|
| `00_프로젝트_허브` | PR #129·Decision·1/10·다음 Gate |
| `01_작업순서` | 단일 차이 정본화와 후속 밸런스 결정 |
| `02_현재_확정결정` | 패시브 XOR 자동 사용스킬 승인 |
| `04_누락_충돌_감사` | 복합 키트·무료 강화·수동 스킬·제작량 재증가 위험 |
| `05_GDD_요약` | 스킨형 이름 지정 영웅 요약 |
| `12_핵심루프` | 원본/스킨형 영웅 선택 판단 |
| `15_조작_게임규칙` | 자동 사용스킬·수동 입력 금지 |
| `40_핵심시스템_메인콘텐츠` | `NamedHeroVariantSpec` 구조 |
| `41_성장_경제` | 해금이 무료 전역 강화가 아닌 선택 후보 추가임을 유지 |
| `50_메인콘텐츠` | 단일 차이를 드러내는 encounter 요구 |
| `60_UX_UI_접근성` | 원본 대비 바뀌는 한 가지를 명확히 표시 |
| `99_변경이력` | GitHub path·PR SHA·read-back 상태 |

## 3. 감사 기준

```text
SIGNATURE_DELTA_COUNT = 1
PASSIVE_AND_ACTIVE_TOGETHER = FORBIDDEN
MANUAL_HERO_SKILL = FORBIDDEN
UNIQUE_RESOURCE = FORBIDDEN_BY_DEFAULT
NEW_AI_ARCHITECTURE = FORBIDDEN_BY_DEFAULT
UNIVERSAL_HERO_ULTIMATE = FORBIDDEN
FREE_POWER = FORBIDDEN
PRODUCT_IMPLEMENTED = FALSE
```

## 4. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`

## 5. 구현·검증 경계

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

## 6. 운영·다음 Gate

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 현재 카운터는 `1/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 제품 코드 PR은 별도 계약 대상이다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
```
