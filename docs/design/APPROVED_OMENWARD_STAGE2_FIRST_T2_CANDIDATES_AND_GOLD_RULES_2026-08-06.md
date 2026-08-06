# OMENWARD Stage 2 최초 T2 후보·골드 규칙 승인 계약

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-STAGE2-FIRST-T2-CANDIDATES-AND-GOLD-RULES-V1
parent_decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
approval: USER_APPROVED_RECOMMENDED_OPTION
status: USER_APPROVED_PLANNING_CANON / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 목적

이 문서는 첫 실제 MapRun의 Stage 2에서 플레이어에게 처음 제시할 T2 후보 두 개와, 해당 선택에 사용하는 실제 골드·예약·잔여 골드 규칙을 소유한다.

```text
DECISION_STATUS = PARTIAL_APPROVAL_7_OF_10
APPROVAL_CHECKPOINT = FIRST_STAGE2_T2_CANDIDATES_AND_GOLD_RULES
```

건물 Tier·자동생산·TokenSource의 기반은 다음 책임 원본을 따른다.

- `docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`
- `docs/design/APPROVED_OMENWARD_UNIT_BUILDING_TIER_MATRIX_AND_ARCHER_T3_CORRECTION_2026-08-06.md`

## 2. 최초 T2 후보

```text
FIRST_STAGE2_T2_CANDIDATES = GENERAL_BARRACKS_T2_SHIELD / GENERAL_BARRACKS_T2_ARCHER
FIRST_STAGE2_CANDIDATE_BUILDING = STAGE1_GENERAL_BARRACKS
FIRST_STAGE2_CHOICE_SCOPE = SAME_BUILDING_TWO_BRANCHES
```

Stage 1에서 설치한 일반병 병영 한 채를 다음 둘 중 하나로 전문화한다.

### 2.1 방패병 분기

```text
SHIELD_ROLE = FRONTLINE_DURABILITY_AND_STALL
SHIELD_AUTO_PRODUCTION = SHIELD_UNIT
SHIELD_TOKEN_SOURCE = SHIELD_UNIT
```

- 기본 보병 자동생산과 TokenSource를 방패병 계열로 교체한다.
- 전열 생존·적 진입 지연·후열 보호에 강점을 둔다.
- 직접적인 처치 속도보다 전선 유지시간을 늘리는 선택이다.

### 2.2 궁병 분기

```text
ARCHER_ROLE = SUSTAINED_RANGED_DAMAGE_AND_FLYING_PRIORITY
ARCHER_AUTO_PRODUCTION = ARCHER
ARCHER_TOKEN_SOURCE = ARCHER
```

- 기본 보병 자동생산과 TokenSource를 궁병 계열로 교체한다.
- 지속 원거리 화력과 후열 기여도를 높인다.
- 기본 비행 적 우선 타기팅은 유지하되, 첫 Stage 2 전투가 궁병을 강제하는 비행 하드키가 되어서는 안 된다.

## 3. 후보 선정 근거

```text
FIRST_STAGE2_LESSON = ROULETTE_SOURCE_AND_FRONTLINE_TRADEOFF
```

두 후보를 같은 일반병 병영의 분기로 묶는 이유는 다음과 같다.

1. 어느 쪽을 선택해도 자동생산 병종과 TokenSource가 실제로 바뀌므로 룰렛 통제 학습이 누락되지 않는다.
2. 방패병은 버티기, 궁병은 지속 화력이라는 직관적인 대비를 제공한다.
3. 다른 건물 유형을 섞는 방식보다 비교 축이 적어 첫 T2 선택의 인지 부담이 낮다.
4. 동적 후보 생성보다 첫 플레이 검증과 원인 복기가 쉽다.

방어탑·경제·지원 건물 T2는 후속 Run 선택으로 남긴다.

## 4. 선택과 되돌림 규칙

```text
FIRST_STAGE2_CHOICE_CONFIRMATION = REQUIRED
FIRST_STAGE2_BRANCH_CHANGE_AFTER_CONFIRMATION = FORBIDDEN
FIRST_STAGE2_UPGRADE_COUNT_BEFORE_ROULETTE = EXACTLY_ONE
SECOND_T2_UPGRADE_BEFORE_FIRST_STAGE2_ROULETTE = FORBIDDEN
UNCHOSEN_BRANCH_GLOBAL_LOCK = FALSE
OTHER_GENERAL_BARRACKS_CAN_SELECT_UNCHOSEN_BRANCH = TRUE
```

- 선택 확인 전에는 두 후보를 자유롭게 비교할 수 있다.
- 확인 뒤에는 해당 병영의 분기를 무료 변경하거나 되돌릴 수 없다.
- 첫 Stage 2 룰렛 전에는 정확히 한 번의 T2 업그레이드만 허용한다.
- 선택하지 않은 분기는 계정·Run 전체에서 영구 폐기되지 않는다.
- 이후 다른 일반병 병영을 건설·업그레이드할 기회가 생기면 미선택 분기를 고를 수 있다.

## 5. 선택 전 미리보기

```text
FIRST_STAGE2_PREVIEW = REQUIRED
PREVIEW_AUTO_PRODUCTION_CHANGE = REQUIRED
PREVIEW_TOKEN_SOURCE_CHANGE = REQUIRED
PREVIEW_ROLE_TRADEOFF = REQUIRED
PREVIEW_NEXT_PRESSURE_RELEVANCE = REQUIRED
PREVIEW_UNCHOSEN_BRANCH_ACCESS = REQUIRED
PREVIEW_COST_AND_REMAINING_GOLD = REQUIRED
```

미리보기는 두 후보 각각에 대해 다음을 한 화면에서 비교한다.

- 자동생산 병종의 전후 변화.
- 룰렛 TokenSource의 전후 변화.
- 버티기와 지속 화력의 차이.
- 다음 압력에 대응하는 방식.
- 선택하지 않은 분기가 이후 다른 병영에서 다시 열릴 수 있다는 사실.
- 비용과 선택 뒤 예상 잔여 골드.

## 6. Stage 2 골드 계약

```text
FIRST_STAGE2_PAIR_COST_CLASS = SAME
STAGE_2_REAL_GOLD_GRANT = EXACTLY_ONE_CANDIDATE_EFFECTIVE_COST
STAGE_2_REQUIRED_COST_RESERVE = ONE_FIRST_T2_UPGRADE
STAGE_2_NON_CANDIDATE_SPENDING_BEFORE_CHOICE = BLOCKED
STAGE_2_GRANT_SURPLUS = FORBIDDEN
STAGE_2_PREEXISTING_GOLD = PRESERVED
STAGE_2_LEFTOVER_GOLD_AFTER_CHOICE = NORMAL_WALLET
TUTORIAL_ONLY_DISCOUNT = FORBIDDEN
T2_EXACT_COST = PENDING_SIMULATION
```

- 방패병과 궁병의 첫 T2 후보는 같은 비용 등급을 사용한다.
- Stage 2 지급액은 실제 골드 지갑에 들어가며 후보 하나의 실효 비용과 정확히 같다.
- 선택 전에는 첫 T2 비용을 예약하고 후보 외 소비를 차단한다.
- 지급액에 의도적인 잉여를 포함하지 않는다.
- Stage 1에서 남은 기존 골드는 삭제·흡수하지 않는다.
- 업그레이드 뒤 기존 잔여 골드는 정상 지갑으로 사용한다.
- 최종 밸런스에서 두 분기의 기본 비용을 다르게 해야 한다면 튜토리얼 전용 할인으로 억지 보정하지 않고, 같은 비용 등급의 첫 후보 조합을 다시 검토한다.

## 7. 다음 전투 압력 계약

```text
FIRST_STAGE2_NEXT_PRESSURE = MIXED_SOFT_COUNTER
FIRST_STAGE2_NEXT_PRESSURE_PROFILE = SUSTAINED_MIXED_GROUND_PRESSURE
FIRST_STAGE2_HARD_COUNTER_REQUIREMENT = FORBIDDEN
FLYING_HARD_REQUIREMENT = FALSE
SCRIPTED_OUTCOME = FORBIDDEN
BOTH_FIRST_STAGE2_PATHS_MUST_BE_VALID = REQUIRED
```

- 다음 압력은 방패병의 전선 유지와 궁병의 지속 화력이 모두 의미 있게 작동하는 혼합 지상 압력으로 설계한다.
- 방패병은 시간을 벌고, 궁병은 처치 속도를 높이는 서로 다른 해결 방식을 제공한다.
- 어느 한 후보 없이는 통과할 수 없는 하드 카운터를 배치하지 않는다.
- 승리를 각본으로 고정하지 않으며 배치·룰렛 결과·전투 판단이 실제 결과에 영향을 준다.
- 정확 적 조합·수량·승률·시간은 시뮬레이션과 사람 플레이 검증 전 확정하지 않는다.

## 8. 룰렛 학습 흐름

```text
STAGE_2_REAL_GOLD_GRANT
→ SHIELD_VS_ARCHER_PREVIEW
→ PLAYER_CONFIRMATION
→ ONE_GENERAL_BARRACKS_T2_UPGRADE
→ AUTO_PRODUCTION_AND_TOKEN_SOURCE_CHANGE
→ FIRST_STAGE2_ROULETTE
→ BEFORE_AFTER_RESULT_COMPARISON
→ MOVE_TICKET_EXPOSURE
→ MULTI_FRONT_DEPLOYMENT
```

선택 직후 첫 룰렛에서 선택한 병종 TokenSource가 실제 후보 구성에 영향을 주는 모습을 보여준다. 단, 정확 토큰 수·가중치·등장률은 별도 시뮬레이션 대상으로 남긴다.

```text
TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION
```

## 9. 금지 규칙

```text
FIRST_STAGE2_DEFENSE_TOWER_CANDIDATE = FORBIDDEN
FIRST_STAGE2_DYNAMIC_CANDIDATE_GENERATION = DEFERRED
FIRST_STAGE2_ONE_PATH_HARD_COUNTER = FORBIDDEN
FIRST_STAGE2_FREE_DUAL_UPGRADE = FORBIDDEN
FIRST_STAGE2_GLOBAL_BRANCH_LOCK = FORBIDDEN
FIRST_STAGE2_TUTORIAL_ONLY_PRICE = FORBIDDEN
FIRST_STAGE2_AUTO_CONFIRMATION = FORBIDDEN
```

이 금지는 첫 Stage 2 온보딩 후보에만 적용한다. 이후 일반 Run에서 방어탑 T2, 다른 일반병 분기, 동적 보상·후보 생성 자체를 금지하지 않는다.

## 10. 제품·수치 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 결정은 기획 정본만 승인한다. 실제 제품 구현은 별도 구현 계획·RED 제품 테스트·데이터 마이그레이션·사람 플레이 Gate를 요구한다.

## 11. 다음 GrillMe

다음 결정은 **특수병 병영 T1이 무작위 특수병을 언제 선정하고, 결과를 생산 전·후 어느 시점에 공개할지**다.
