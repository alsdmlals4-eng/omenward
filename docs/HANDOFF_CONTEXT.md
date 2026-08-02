# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_UNIQUE_SKILL_UPGRADE_PLANNING
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
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
current_grill_me_count: 5
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 최신 사용자 결정

Decision ID:

`OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1`

```text
원본 병종 [영웅] 등급 기본 전투 성능
+ 이름·초상·스킨·식별 연출
+ 고유 자동 사용스킬 정확히 1개
= 제한형 상위호환 이름 지정 영웅
```

```text
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1_PER_HERO
MANDATORY_COMPENSATION_AXIS_COUNT = 0
GLOBAL_ACTIVE_NAMED_HERO_CAP = 1
```

- 이름 지정 영웅은 원본보다 조금 더 강하고 임팩트 있는 해금 보상이다.
- 이전 패시브 선택 구조·강제 상쇄 축·평균 예산 동등 sidegrade 의무는 폐기됐다.
- 고유 스킬 추가 대가로 기본 능력치를 의무적으로 낮추지 않는다.
- 원본 역할·기본 공격·기본 스탯·사거리·이동·기본 AI·리그·공통 애니메이션을 계승한다.
- 전역 활성 1명·해금·적격 토큰·비가역 배치·cooldown/charge로 통제한다.

## 2. 초기 5명

```text
shield_guard / 방패병 → 고유 자동 사용스킬
archer / 궁병         → 고유 자동 사용스킬
priest / 사제         → 고유 자동 사용스킬
mage / 마법사         → 고유 자동 사용스킬
assassin / 암살자     → 고유 자동 사용스킬
```

```text
INITIAL_HERO_COUNT = 5
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
FINAL_RELEASE_CAP = FALSE
```

정확 영웅 이름·스킬·발동 조건·cooldown·charge·VFX/SFX·수치는 pending이다.

## 3. 자동 발동·결정론

각 고유 스킬은 다음을 공개한다.

- trigger.
- target filter.
- target priority.
- deterministic tie-break.
- cooldown 또는 charge.
- 유효 대상이 없을 때 처리.
- 발동 직전 재검증.
- VFX/SFX와 로그.

수동 버튼·수동 타깃·수동 보류·저장 재굴림은 금지한다.

## 4. 기존 생명주기 연결

- 영웅은 기존 UnitArchetype에 고정 연결된다.
- 동병종 `[영웅]` 토큰을 원본 병종 또는 이름 지정 영웅으로 1:1 변환한다.
- 세 전선 전체 활성 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 사망 후 재출전에는 사망 이후 새 적격 토큰이 필요하다.
- 생존 상태·Stage 경계·정비시간·저장 규칙은 기존 승인 계약을 따른다.

## 5. 적대적 경계

- 상위호환으로 인해 특정 영웅이 모든 콘텐츠의 유일한 정답이 되지 않는지 검증한다.
- 원본 유닛만으로 기본 진행이 가능한지 검증한다.
- 패시브를 기본 공격 효과나 숨은 상시 보너스로 되살리지 않는다.
- 고유 스킬 하나에 여러 독립 능력을 숨기지 않는다.
- 고유 스킬 5개가 새 AI·새 리그·전체 신규 애니메이션 5세트로 확대되지 않도록 공통 프레임을 사용한다.
- 스킬 임팩트가 약해 해금 보상이 느껴지지 않으면 실패다.

## 6. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` — `SUPERSEDED_HISTORY`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`

## 7. 구현 경계·다음 작업

```text
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

다음 우선 결정:

```text
OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-CONCEPTS-V1
```

검토 주제는 초기 다섯 영웅 각각의 고유 자동 사용스킬 전술 콘셉트다.
