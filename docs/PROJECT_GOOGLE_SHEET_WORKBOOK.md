# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
current_operating_gate: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3
last_merged_planning_pr: 127
current_planning_pr: 129
sheet_status: PROJECT_SHEET_CONFIGURED / SYNC_TO_PR_129_IN_PROGRESS
current_grill_me_count: 3
preflight: NEXT_AT_10_OF_10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. GitHub가 기획 정본이며 Sheet는 같은 Decision ID와 PR SHA를 표시한다.

## 1. 현재 동기화 Decision

Decision:

`OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1`

```text
서로 다른 기존 UnitArchetype 4종
→ 병종마다 이름 지정 영웅 1명
→ 패시브형 2명
→ 자동 사용스킬형 2명
→ 초기 검증 로스터 총 4명
```

- 동일 병종 복수 영웅은 초기 로스터에서 금지한다.
- 네 병종의 역할·전투 판단 중복을 최소화한다.
- 정확 병종·영웅·능력·상쇄 축은 pending이다.
- 4명은 최종 출시 전체 로스터 상한이 아니라 첫 제작·밸런스·UX·자산 재사용 검증 범위다.
- 후보 병종은 원본 완성도·자산 재사용성·전술 차별성·상쇄 가독성·콘텐츠 노출성을 기준으로 선정한다.
- 초기 로스터는 패시브형 2명과 자동 사용스킬형 2명을 모두 검증한다.

## 2. 이전 승인 연결

```text
원본 병종 [영웅] 등급 유닛
+ 스킨·이름·최소 식별 연출
+ PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
- ONE_RELATED_COMPENSATION_AXIS
= 이름 지정 영웅
```

- 원본 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- `[사용스킬]`은 수동 버튼이 아닌 규칙 기반 자동 발동이다.
- 상쇄 축 외의 원본 데이터는 유지한다.
- 무료 능력·다축 하향·전체 스탯 재설계는 금지다.

## 3. 주요 탭 동기화 목적

| 탭 | 이번 Decision 반영 내용 |
|---|---|
| `00_프로젝트_허브` | PR #129·Decision·3/10·다음 Gate |
| `01_작업순서` | 초기 로스터 4명 승인과 실제 병종 선정 후속 |
| `02_현재_확정결정` | 서로 다른 병종 4종·패시브 2·자동 스킬 2 승인 |
| `04_누락_충돌_감사` | 최종 로스터 상한 오해·2:2 강제·역할 중복·제작량 폭증 위험 |
| `05_GDD_요약` | 초기 검증 로스터 범위 요약 |
| `12_핵심루프` | 네 병종 원본/영웅 선택 비교 검증 |
| `15_조작_게임규칙` | 초기 로스터 수·병종 중복 금지·2:2 유형 불변식 |
| `40_핵심시스템_메인콘텐츠` | `InitialNamedHeroRosterSpec` 방향 |
| `41_성장_경제` | 초기 4명 해금 범위와 원본 완주 가능성 |
| `50_메인콘텐츠` | 네 병종의 장점·약점을 드러내는 encounter 매트릭스 |
| `60_UX_UI_접근성` | 4명 카드의 원본 대비 한 쌍 교환 비교 |
| `70_아트_오디오_에셋` | 4개 스킨형 변주 제작량·재사용 기준 |
| `99_변경이력` | GitHub path·PR SHA·read-back 상태 |

## 4. 감사 기준

```text
INITIAL_NAMED_HERO_COUNT = 4
INITIAL_SOURCE_ARCHETYPE_COUNT = 4
HEROES_PER_SOURCE_ARCHETYPE = 1
PASSIVE_VARIANT_COUNT = 2
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
FOUR_FULL_NEW_UNITS = FORBIDDEN
PRODUCT_IMPLEMENTED = FALSE
```

## 5. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`

## 6. 구현·검증 경계

```text
PROJECT_SHEET_CONFIGURED
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
INITIAL_HERO_COUNT = 4
EXACT_ARCHETYPES = PENDING
EXACT_HEROES = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 운영·다음 Gate

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 현재 카운터는 `3/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 제품 코드 PR은 별도 계약 대상이다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
```
