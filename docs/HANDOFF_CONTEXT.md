# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_SINGLE_DELTA_VARIANT_PLANNING
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
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
current_grill_me_count: 1
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 현재 승인 결정

Decision ID:

`OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1`

```text
원본 병종 [영웅] 등급 유닛
+ 영웅 전용 스킨·이름·최소 식별 연출
+ 패시브 1개 또는 자동 [사용스킬] 1개
= 이름 지정 영웅
```

- 이름 지정 영웅은 완전 신규 유닛이 아니라 기존 `[영웅]` 등급 병종의 스킨형 전술 변주다.
- 영웅 전용 차이는 정확히 하나다.
- `PASSIVE XOR AUTOMATIC_ACTIVE_SKILL`이며 두 유형을 동시에 제공하지 않는다.
- `[사용스킬]`은 기존 자동 발동 계약을 따르며 수동 버튼·수동 타깃이 아니다.
- 원본 병종의 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 기본적으로 고유 자원·궁극기·새 AI·새 전체 애니메이션 세트를 요구하지 않는다.
- 외형 제작량은 스킨 수준을 목표로 하되 단일 차이는 실제 전술 선택을 바꿔야 한다.

## 2. 전투 예산 경계

- 이름 지정 영웅은 원본 `[영웅]` 등급 병종의 순수 상위호환이 아니다.
- 패시브 또는 사용스킬의 가치는 기본 스탯·안정성·범용성에서 상쇄한다.
- 원본 병종이 더 좋은 대표 상황을 최소 하나 유지한다.
- 장식 전용 스킨과 신규 병종 수준의 과도한 차이를 모두 금지한다.

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
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`

## 5. 적대적 검토 핵심

- 패시브 안에 여러 독립 효과를 숨겨 제작량이 다시 증가하지 않는지 확인한다.
- 사용스킬이 수동 조작으로 변질되지 않는지 확인한다.
- 스킨형이라는 이유로 무료 능력 추가가 되지 않는지 확인한다.
- 색상만 바꾼 장식 전용 영웅이 되지 않도록 실루엣·장비·VFX 식별성을 확보한다.
- 단일 차이가 원본 역할을 파괴해 새 병종처럼 작동하지 않는지 확인한다.

## 6. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_HERO_VARIANTS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

다음 우선 결정:

```text
OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
```

검토 주제는 `단일 패시브/사용스킬의 전투 가치와 원본 병종 보상 조정 방식`이다.
