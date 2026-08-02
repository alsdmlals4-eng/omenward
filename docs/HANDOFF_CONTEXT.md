# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_INITIAL_ROSTER_SCOPE_PLANNING
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
last_merged_planning_pr: 127
base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 3
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 현재 승인 결정 3건

### 1.1 스킨형 단일 차이

`OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1`

- 이름 지정 영웅은 기존 `[영웅]` 등급 병종의 스킨형 전술 변주다.
- 영웅 전용 차이는 패시브 1개 또는 자동 `[사용스킬]` 1개 중 정확히 하나다.
- 원본 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.

### 1.2 단일 상쇄 축

`OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1`

- 단일 차이 가치와 직접 관련된 상쇄 축 하나만 하향·조건화한다.
- 상쇄 축 외의 원본 데이터를 유지한다.
- 여러 스탯 동시 조정·공통 고정 세금·전체 성장 곡선 재설계는 금지다.

### 1.3 초기 로스터 4명

`OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1`

```text
서로 다른 UnitArchetype 4종
→ 병종마다 이름 지정 영웅 1명
→ 패시브형 2명
→ 자동 사용스킬형 2명
→ 초기 검증 로스터 총 4명
```

- 동일 병종 복수 영웅은 초기 로스터에서 금지한다.
- 역할·전투 판단 중복을 최소화한다.
- 정확 병종·영웅 이름·능력·상쇄 축은 pending이다.
- 4명은 최종 출시 전체 로스터 상한이 아니다.
- 병종 후보는 원본 완성도·자산 재사용성·검증 가치·상쇄 가독성·콘텐츠 노출성을 기준으로 선정한다.

## 2. 초기 로스터 적대적 경계

- 2:2 할당을 위해 병종 정체성에 맞지 않는 능력을 억지로 넣지 않는다.
- 서로 다른 병종이어도 기능이 겹치면 후보를 교체한다.
- 인기·설정 매력보다 제작 가능성과 시스템 검증 가치를 우선한다.
- 네 영웅 모두 같은 단일 차이 또는 상쇄 패턴에 편중되지 않도록 검토한다.
- 새 리그·전체 애니메이션·별도 AI를 요구하는 병종은 스킨형 후보 적합성을 재검토한다.
- 초기 4명을 완전 신규 유닛으로 제작하지 않는다.

## 3. 기존 생명주기 연결

- 영웅은 기존 UnitArchetype에 고정 연결된다.
- 동병종 `[영웅]` 토큰을 원본 병종 또는 이름 지정 영웅으로 1:1 변환한다.
- 세 전선 전체 active 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 사망 후 재출전에는 사망 이후 새 적격 토큰이 필요하다.
- 생존 상태·Stage 경계·정비시간·저장 규칙은 기존 승인 계약을 따른다.

## 4. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`

## 5. 구현 경계·다음 작업

```text
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

다음 우선 결정:

```text
OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
```

검토 주제는 `실제 저장소 병종 명단에서 초기 검증 가치가 가장 높은 서로 다른 병종 4종을 선정하는 것`이다.
