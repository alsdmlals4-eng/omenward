# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
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
current_grill_me_count: 4
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 승인 결정 4건

1. `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1`
   - 기존 `[영웅]` 등급 병종의 스킨형 변주.
   - 패시브 또는 자동 사용스킬 하나만 보유.
2. `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1`
   - 단일 차이와 직접 관련된 상쇄 축 하나만 조정.
3. `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1`
   - 초기 제작·검증 로스터이며 최종 출시 상한이 아님.
   - 후속 사용자 수정으로 수량은 5명으로 갱신.
4. `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1`
   - 방패병·궁병·사제·마법사·암살자 확정.

## 2. 현행 초기 5명

```text
shield_guard / 방패병   → PASSIVE
archer / 궁병           → PASSIVE
assassin / 암살자       → PASSIVE
priest / 사제           → AUTOMATIC_ACTIVE_SKILL
mage / 마법사           → AUTOMATIC_ACTIVE_SKILL
```

```text
INITIAL_HERO_COUNT = 5
SOURCE_ARCHETYPE_COUNT = 5
PASSIVE_COUNT = 3
AUTOMATIC_ACTIVE_COUNT = 2
```

- 최신 사용자 직접 선택이 이전 4명·2:2 수량을 대체한다.
- 동일 병종 복수 영웅은 초기 범위에서 금지한다.
- 거인과 기병은 초기 5명에 포함되지 않는다.
- 구체 영웅 이름·외형·효과·상쇄 축·수치는 pending이다.

## 3. 병종별 검증 역할

- 방패병: frontline·nearest·ranged defense.
- 궁병: ranged·flying priority·anti-air.
- 암살자: bypass·backline priority.
- 사제: support·lowest-health ally.
- 마법사: ranged control·cluster priority.

궁병과 마법사의 역할 중복은 지속 대공과 군집 광역 자동 스킬로 분리한다.

## 4. 공통 제작·밸런스 경계

```text
원본 [영웅] 등급 병종
+ 스킨·이름·최소 식별 연출
+ PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
- ONE_RELATED_COMPENSATION_AXIS
= 이름 지정 영웅
```

- 원본 역할·공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 무료 능력·여러 스탯 동시 하향·전체 성장 곡선 재설계를 금지한다.
- 병종마다 원본이 더 좋은 대표 상황을 유지한다.
- 사제·마법사 자동 스킬은 수동 버튼이 아니다.

## 5. 적대적 검토 핵심

- 활성 문서와 Sheet에 남은 4명 표현을 현행 5명보다 우선하지 않는다.
- 암살자 패시브가 기존 backline 타기팅의 장식적 반복이 되지 않게 한다.
- 사제 ally-lowest-health와 마법사 enemy-cluster의 결정론 테스트를 분리한다.
- 후열 병종 3개의 콘텐츠 노출과 시각 판독을 별도 검증한다.
- 초기 5명을 완전 신규 유닛으로 만들지 않는다.
- 5명은 최종 출시 전체 로스터 상한이 아니다.

## 6. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`

## 7. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
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

다음 우선 결정:

```text
OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-SIGNATURE-CONCEPTS-V1
```

다섯 영웅의 전술 정체성·단일 차이 방향·원본 우위 상황을 설계한다.
