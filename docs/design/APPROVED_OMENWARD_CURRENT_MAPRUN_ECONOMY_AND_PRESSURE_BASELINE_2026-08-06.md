# [승인] OMENWARD 현재 MapRun 경제·압력 시뮬레이션 기준선

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1
parent_decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SIMULATION-INPUT-PROVENANCE-AND-ROULETTE-AXIS-CORRECTION-V1
status: APPROVED_SIMULATION_BASELINE
approval: USER_DIRECT_PROCEED_AUTHORIZATION
approval_count: 3_OF_10
approach: HYBRID_ABSOLUTE_ONBOARDING_AND_NORMALIZED_THREAT_BASELINE
scope: SMOKE_SIMULATION_INPUT_ONLY
product_code_authority: NONE
```

## 1. 결정

첫 5 Stage에는 실제 골드·초 단위를 사용하고, 적 압력과 기회비용은 Threat Unit과 다차원 벡터로 정규화한다. 구형 15분 단일 Stage 수치를 그대로 복원하지 않으며, 이 값은 제품 최종 밸런스가 아니다.

```text
SIMULATION_RUNNABLE = TRUE_FOR_SMOKE_ONLY
SMOKE_SWEEP = READY_NOT_RUN
DECISION_SWEEP = BLOCKED_UNTIL_SMOKE_PASS
CONFIRMATION_SWEEP = BLOCKED_UNTIL_DECISION_PASS
FINAL_PARAMETER_VECTOR = NOT_SELECTED
ABSOLUTE_PRODUCT_NUMERICS = NOT_FINAL
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

기계 판독 입력:

- `docs/analysis/barracks_simulation/current_maprun_economy_pressure_baseline.v1.json`

## 2. Stage 1 기초 경제

필수 T1 비용:

| 건물 | 골드 | 건설시간 |
|---|---:|---:|
| 금고 | 50 | 25초 |
| 농장 | 35 | 20초 |
| 일반병 병영 | 40 | 20초 |
| 방어탑 | 35 | 22초 |
| 지휘소 | 45 | 25초 |
| 마력탑 | 45 | 25초 |
| **합계** | **250** | 병렬 최대 25초 |

```text
MAPRUN_STARTING_FOUNDATION_GOLD = 250
FOUNDATION_REQUIRED_COST_SUM = 250
FOUNDATION_GRANT_SURPLUS = 0
FOUNDATION_SETUP_CLOCKS = OFF_UNTIL_CONFIRMATION
FOUNDATION_CONSTRUCTION = PARALLEL_AFTER_CONFIRMATION
STAGE1_OPERATIONAL_GOLD_GRANT_AFTER_FOUNDATION = 20
BASE_SPIN_COST = 20
```

20골드는 여섯 건물 완공 뒤 정상 가격 첫 회전을 위한 실제 지갑 지급이다. Foundation 비용 예약과 분리하며, 첫 세트 완료 전 다른 소비는 계속 차단한다.

## 3. 지속 골드

```text
BASE_INCOME = 3 GOLD / 20 ACTIVE_COMBAT_SECONDS
VAULT_T1_INCOME = 3 GOLD / 20 ACTIVE_COMBAT_SECONDS
MIDPOINT_CONTROL_INCOME = 4 GOLD / CONTROLLED_POINT / 60 ACTIVE_COMBAT_SECONDS
KILL_GOLD = 0
WAVE_CLEAR_GOLD = 0
STAGE_CLEAR_FIXED_GOLD = 0
INCOME_TIMER_SCOPE = MAPRUN_PERSISTENT_PAUSED_OUTSIDE_ACTIVE_COMBAT
```

20초·60초 타이머는 Stage 전환에서 초기화하지 않는다. 정비시간과 Foundation 세팅 중에는 멈춘다.

## 4. Stage 2와 선택 투자

```text
SHIELD_T2_COST = 50
ARCHER_T2_COST = 50
SHIELD_T2_UPGRADE_SECONDS = 25
ARCHER_T2_UPGRADE_SECONDS = 25
STAGE2_RESERVED_GOLD_GRANT = 50
SPECIAL_BARRACKS_T1_COST = 60
SPECIAL_BARRACKS_T1_CONSTRUCTION_SECONDS = 30
```

Stage 2 지급액은 기존 승인처럼 후보 하나의 비용과 정확히 같고 선택 전 다른 소비에 사용할 수 없다.

## 5. 정비시간 Clock Matrix

기준 정비시간은 30 active decision seconds다. 플레이어는 일찍 확정할 수 있다.

| Clock | 정비시간 |
|---|---|
| 적·점령 진행 | OFF |
| 기본·금고·접전지 골드 | OFF |
| 유닛 자동생산 | OFF |
| 건설·업그레이드·수리 진행 | ON |
| 마석 회복·전술 쿨다운 | OFF |
| 피해·회복·상태이상 틱 | OFF |

접근성 일시정지는 정비시간의 모든 Clock을 멈춘다. 정비 중 특수병 병영이 완공되면 결과는 즉시 공개하지만 자동생산 타이머는 다음 active combat부터 시작한다.

## 6. 자동생산 간격

| 병종 | active combat seconds |
|---|---:|
| 기본 보병 | 50 |
| 방패병 | 65 |
| 궁병 | 65 |
| 암살자 | 75 |
| 사제 | 80 |
| 마도사 | 90 |
| 비행병 | 100 |
| 거인 | 110 |

특수병 T1 추첨은 smoke baseline에서 각 20%다. 저장·복구·철거를 통한 무료 재추첨 금지는 유지한다.

## 7. 식량·노드 기회비용

```text
STARTING_FOOD_CAP = 12
FARM_T1_FOOD_CAP_BONUS = 6
POST_FOUNDATION_OPTIONAL_NODE_BUDGET_BASELINE = 2
NODE_STRESS = 1 / 2 / 3
```

식량 후보:

```text
BASIC_INFANTRY 1
SHIELD 2
ARCHER 2
ASSASSIN 2
PRIEST 3
MAGE 3
FLYING_UNIT 4
GIANT 6
```

비교는 단일 가중합이 아니라 벡터로 수행한다.

```text
GOLD_EQ = investment_gold / 40
TIME_EQ = first_unit_wait_seconds / 50
FOOD_EQ = unit_food_cost / 6
NODE_EQ = occupied_optional_nodes / 2
OPPORTUNITY_COST = VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE
```

`optional node = 2`는 시뮬레이션 기준이며 최종 레벨 좌표·노드 수 권위가 아니다.

## 8. Threat Unit

```text
1 TU = ONE_STAGE1_BASELINE_LIGHT_GROUND_ENEMY_EQUIVALENT
LIGHT_GROUND = 1.0 TU
ARMORED_ANCHOR = 2.5 TU
FLYING_RAIDER = 1.5 TU
INFILTRATOR = 1.5 TU
SIEGE_UNIT = 3.0 TU
STAGE5_BOSS_CORE = 12.0 TU
```

TU는 조합 예산이며 최종 HP·DPS·Spawn 수가 아니다.

## 9. Stage 1~5 기준선

| Stage | 유형·압력 | 목표 Wave 시작초 | Wave TU | 예상 active combat |
|---:|---|---|---|---:|
| 1 | Normal · MASS | 0 / 35 / 75 | 8 / 12 / 16 | 110초 |
| 2 | Normal · ARMORED | 0 / 40 / 80 | 7 / 12 / 17 | 120초 |
| 3 | Normal · FLYING | 0 / 40 / 85 | 6 / 11 / 16 | 130초 |
| 4 | Danger · INFILTRATION | 0 / 45 / 95 | 7 / 13 / 19 | 140초 |
| 5 | Boss · SIEGE | 0 / 50 / 105 | 10 / 18 / 28 | 160초 |

```text
WAVE_START_RULE = MAX_TARGET_OFFSET_OR_PREVIOUS_CLEAR_PLUS_8_SECONDS
FORCED_OVERLAP_BEFORE_STAGE9 = FALSE
ACTIVE_COMBAT_STAGE1_TO_5 = 660_SECONDS
FOUNDATION_SETUP_EXPECTED = 50_SECONDS
FOUR_MAINTENANCE_BASELINES = 120_SECONDS
FIRST_FIVE_EXPECTED_TOTAL = 830_SECONDS / 13_MINUTES_50_SECONDS
TARGET_ONBOARDING_WINDOW = 600..900_SECONDS
```

Stage 2의 장갑 압력은 방패병의 stall과 궁병의 sustained damage가 모두 유효한 soft-counter 구성이다. Stage 3의 비행 압력은 궁병을 강제 정답으로 만들지 않으며, 기존 다른 공격 가능 Layer와 전술 경로도 유효해야 한다.

## 10. Gate 해제와 경계

2/10에서 확인한 여섯 blocker는 이 smoke baseline으로 해소한다. 다만 통과 결과가 아직 없으므로 decision·confirmation sweep는 열지 않는다.

```text
GENERAL_PRODUCTION_INTERVAL_SECONDS = RESOLVED_FOR_SMOKE
ASSASSIN_PRODUCTION_INTERVAL_SECONDS = RESOLVED_FOR_SMOKE
FOOD_SLOT_AND_NODE_OPPORTUNITY_COST = RESOLVED_FOR_SMOKE
CURRENT_MAPRUN_GOLD_TIMELINE = RESOLVED_FOR_SMOKE
ENEMY_THREAT_BUDGET_AND_TIMELINE = RESOLVED_FOR_SMOKE
MAINTENANCE_CLOCK_MATRIX = RESOLVED_FOR_SMOKE
NEXT_GATE = BARRACKS_SMOKE_SWEEP_EXECUTION
```
