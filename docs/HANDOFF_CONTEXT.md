# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_GRADE_SLOT_AND_UNIQUE_SKILL_2_PLANNING
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
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
current_grill_me_count: 6
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 최신 사용자 결정

Decision ID:

`OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1`

```text
[영웅]·[전설] 등급 유닛을 표준/해금·병종·전선과 관계없이 전장 전체에 최대 1명만 활성화
```

```text
표준 [영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
표준 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 고유 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
HIGH_GRADE_ACTIVE_CAP = 1
COUNTED_GRADES = HERO | LEGENDARY
NAMED_HERO_UNIQUE_SKILL_SLOT = 2
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

## 2. 기존 결정과 달라진 점

- 과거 `이름 지정 해금 영웅만 전역 1명` 규칙은 폐기됐다.
- 표준 영웅·해금 영웅·표준 전설·향후 해금 전설 모두 같은 전역 슬롯을 공유한다.
- 과거 `표준 영웅 키트에 고유 스킬 하나 추가` 구조는 폐기됐다.
- 해금 영웅은 표준 2스킬을 고유 2스킬로 교체하며 추가 3번째 스킬을 얻지 않는다.
- 향후 해금 전설은 표준 3스킬을 고유 3스킬로 교체하지만 현재 구현하지 않는다.
- 해금 후 표준 영웅이 합리적 선택이 아닌 것은 의도된 수직 성장이다.

## 3. 전역 슬롯 처리

```text
영웅 이상 토큰 획득
→ 슬롯 비어 있음: 합법 표준/해금 후보 선택 후 한 전선 비가역 배치
→ 슬롯 차 있음: 보관 또는 판매
```

- 제한은 룰렛 획득이 아니라 전장 배치에 적용한다.
- 슬롯 충돌로 결과를 소멸시키지 않는다.
- 자동 삭제·자동 교체·수동 퇴각·수동 교대·판매·재보관으로 활성 슬롯을 비우지 않는다.
- 살아 있는 고등급 유닛은 Stage·Act·정비시간을 넘어 지속한다.

## 4. 초기 5명

```text
shield_guard / 방패병 → 고유 2스킬
archer / 궁병         → 고유 2스킬
priest / 사제         → 고유 2스킬
mage / 마법사         → 고유 2스킬
assassin / 암살자     → 고유 2스킬
```

정확 영웅 이름과 고유 2스킬 효과는 pending이다.

## 5. 공통 자동 발동

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 유효 조건·대상·priority·tie-break
→ 발동 직전 재검증
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

- 유효 조건이 없으면 준비 상태를 보존한다.
- 수동 버튼·수동 타깃·수동 보류·Retry 재굴림은 금지한다.

## 6. 코어 적합성

핵심 재미:

> 건물을 지어 룰렛의 미래를 바꾸고, 예고된 위기에 맞는 희귀 병력을 얻어 어느 전선에 비가역 커밋할지 결정한 뒤 전황을 뒤집는다.

전역 고등급 슬롯은 영웅·전설을 누적 전력으로 만들지 않고 세 전선 중 하나에 최고 전력을 투입하는 기회비용을 만든다.

주요 위험:

- 영웅 생존 중 전설 당첨을 즉시 배치하지 못하는 좌절.
- 영웅 결과 빈도와 슬롯 점유로 인한 보관함 압력.
- 해금 고유 2스킬이 전설 전체 키트를 침범하는 파워 역전.
- 고등급 한 명이 세 전선의 유일한 승리 조건이 되는 현상.

상세 검토: `docs/reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md`.

## 7. 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md`
- `docs/design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`

## 8. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILL_2 = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

다음 우선 결정:

```text
OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
```

검토 주제는 초기 다섯 해금 영웅 각각의 전장 임팩트형 고유 2스킬 콘셉트다.
