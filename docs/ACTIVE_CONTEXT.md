# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 4
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`context_baseline_commit`과 `current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 승인 기획은 Draft PR #129에 누적하며 제품 구현 권한은 없다.

## 1. 영웅 공통 제작 모델

```text
기존 병종 [영웅] 등급 유닛
+ 영웅 전용 스킨·이름·최소 식별 연출
+ 패시브 1개 또는 자동 [사용스킬] 1개
- 직접 관련된 상쇄 축 1개
= 이름 지정 영웅
```

- 원본 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- `PASSIVE XOR AUTOMATIC_ACTIVE_SKILL`이다.
- 상쇄 축 외의 원본 데이터는 유지한다.
- 무료 능력·다축 하향·전체 스탯 재설계는 금지한다.

## 2. 초기 검증 로스터 5명

사용자의 최신 직접 선택으로 이전 4명 권장 범위를 다음 5명으로 확장했다.

```text
shield_guard / 방패병   → PASSIVE
archer / 궁병           → PASSIVE
assassin / 암살자       → PASSIVE
priest / 사제           → AUTOMATIC_ACTIVE_SKILL
mage / 마법사           → AUTOMATIC_ACTIVE_SKILL
```

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

검증 역할:

- 방패병: 전열·점령·원거리 방어·최근접 대상.
- 궁병: 지속 원거리·대공·비행 우선 대상.
- 암살자: 우회·후열 우선 대상.
- 사제: 아군 지원·최저 체력 아군 대상.
- 마법사: 군집·광역·제어·적 군집 대상.

구체 영웅 이름·외형 콘셉트·단일 차이 효과·상쇄 축·수치는 아직 확정하지 않는다.

## 3. 생명주기·자동 발동 연결

- 영웅은 기존 UnitArchetype에 고정 연결된다.
- 동병종 `[영웅]` 토큰을 원본 병종 또는 이름 지정 영웅으로 1:1 변환한다.
- 세 전선 전체 active 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 사제와 마법사의 사용스킬은 수동 버튼이 아닌 공개 규칙 기반 자동 발동이다.
- 동일 저장 상태와 입력 순서에서는 같은 결과를 내며 save reroll은 금지다.

## 4. 적대적 경계

- 이전 4명·2:2 표현은 현행 5명·3:2보다 우선할 수 없다.
- 궁병과 마법사는 모두 ranged지만 지속 대공과 군집 광역으로 판단을 분리한다.
- 암살자 패시브는 기존 backline 타기팅을 반복하는 장식 효과가 아니어야 한다.
- 사제·마법사 자동 스킬은 ally-lowest-health와 enemy-cluster 테스트를 분리한다.
- 다섯 영웅을 완전 신규 유닛으로 제작하지 않는다.
- 5명은 최종 출시 전체 로스터 상한이 아니다.

## 5. 현재 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`

## 6. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
INITIAL_HERO_COUNT = 5
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
EXACT_HERO_IDENTITIES = PENDING
EXACT_SIGNATURE_EFFECTS = PENDING
EXACT_COMPENSATION_AXES = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 운영 규칙·다음 Gate

- 현재 카운터는 `4/10`이다.
- 승인 결정은 GitHub와 Sheet에 같은 Decision ID로 즉시 반영한다.
- 10번째 승인에서 적대적 preflight를 실행한다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-SIGNATURE-CONCEPTS-V1
```
