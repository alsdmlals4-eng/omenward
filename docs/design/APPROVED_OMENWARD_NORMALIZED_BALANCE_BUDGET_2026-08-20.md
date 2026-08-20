# [현행] OMENWARD · Normalized Balance Budget

```yaml
decision_id: OMW-PLAN-20260820-BALANCE-BUDGET-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-FIRST5-FTUE-01
  - OMW-PLAN-20260820-CONTENT-BOSS-ARC-01
runtime_mutation: NONE
product_data_mutation: NONE
simulation: NOT_RUN_FOR_THIS_DECISION
human_validation: NOT_RUN
final_product_numerics: NOT_APPROVED
```

## 1. 결정

OMENWARD의 현재 Balance 단계에서는 절대 Gold/HP/DPS/초당 마력 수치를 바로 고정하지 않는다.

**기존 구현·분석 수치는 calibration anchor로 보존하고, 먼저 정규화된 선택 예산과 난도 envelope를 승인한다.**

```text
SE = Spin Equivalent
ME = Major-choice Equivalent
TU = Threat Unit / simulation-only threat unit
Threat Vector = Raw TU + Active Lanes + Signature Count + Route Complexity + Wave Overlap + Elite/Boss Presence
```

이 Decision의 목적은 다음이다.

1. 한 Stage에서 플레이어가 실제로 무엇을 포기하고 무엇을 살 수 있어야 하는지 정의한다.
2. 난도가 적 HP/수량만 상승하는 구조가 되지 않게 한다.
3. 기존 10k robustness와 현행 roulette/economy 값을 버리지 않되 최종 제품 수치로 오인하지 않게 한다.
4. 서로 충돌하는 과거 baseline과 current main runtime 수치를 구현 전에 재대조하도록 fail-closed한다.

## 2. Calibration anchor · 최종값 아님

현재 분석 baseline에서 보존할 기준점:

```text
STAGE1_REQUIRED_T1_TOTAL_GOLD = 250
MAPRUN_STARTING_FOUNDATION_GOLD = 250
STAGE1_OPERATIONAL_GOLD_AFTER_FOUNDATION = 20
BASE_SPIN_COST_GOLD = 20
STAGE2_FIRST_T2_COST_CLASS_GOLD = 50
STARTING_FOOD_CAP = 12
FARM_T1_FOOD_CAP_BONUS = 6
```

현재 `main`의 `RouletteService.SPINE_COST`는 20 Gold이므로 현재 calibration에서:

```text
1 SE = 20 Gold
1 ME = 50 Gold = 2.5 SE
```

를 사용한다.

단, `SE`와 `ME`는 **현재 calibration 단위**다. 후속 simulation/runtime evidence로 Spin 또는 첫 Major 선택 가격이 바뀌면 normalized unit도 함께 재기준화한다.

## 3. 알려진 숫자 drift · 구현 전 필수 reconciliation

현재 분석 baseline과 current main runtime은 동일한 경제를 표현하지 않는다.

분석 baseline:

```text
base income = 3 Gold / 20 active-combat sec
Vault T1 income = 3 Gold / 20 active-combat sec
foundation Gold = 250
```

current main 관찰:

```text
StageEconomy.BASE_INCOME_AMOUNT = 5 / 20 sec
StageEconomy.CONTROL_INCOME_AMOUNT = 4 / 60 sec / controlled clash
StageEconomy.OUTPOST_INCOME_AMOUNT = 2 / 30 sec / stable owned outpost
StageDefinition.starting_gold default = 160
```

따라서:

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
IMPLEMENT_CURRENT_MAIN_NUMERICS_AS_FINAL = FORBIDDEN
PROMOTE_ANALYSIS_BASELINE_TO_RUNTIME_WITHOUT_RETEST = FORBIDDEN
```

Balance planning은 이 drift 위에서 어느 한쪽을 임의의 정답으로 고르지 않는다.

## 4. Gold / 선택 예산

경제의 핵심 목표:

```text
PLAYER_CAN_BUY_EVERY_GOOD_OPTION_EACH_CHECKPOINT = FALSE
PLAYER_HAS_AT_LEAST_ONE_MEANINGFUL_AFFORDABLE_ACTION_AT_NORMAL_CHECKPOINT = TARGET
```

Stage 1 Foundation:

```text
required T1 coverage ratio = 1.00
current foundation anchor = 250 / required 250
post-foundation operational anchor = 1.0 SE
```

Normal Stage 정비 체크포인트의 탐색 목표:

```text
if player prioritizes Roulette:
  affordable Spins ≈ 1~2 SE

if player prioritizes Major development:
  one ME-class choice should compete with Roulette / research / merchant spend
```

Boss 이후 체크포인트:

```text
build correction headroom = higher than normal Stage
full-build reset by Gold = FORBIDDEN
all desirable upgrades + several Spins + research + merchant = FORBIDDEN_AS_DEFAULT
```

경제 빌드가 강할수록 선택 폭은 넓어질 수 있으나, 매 방문 모든 상품과 모든 성장 선택을 독식하는 것이 정답이 되면 Stop-ship이다.

## 5. Roulette spend envelope

현재 Spin anchor:

```text
BASE_SPIN_COST = 1.0 SE = 20 Gold
```

목표:

```text
NORMAL_STAGE_OPTIONAL_SPINS_IF_PRIORITIZED = 1~2
BOSS_RECOVERY_SPINS_IF_PRIORITIZED = approximately 2~3 exploration target
ROULETTE_TOO_EXPENSIVE_TO_ENGAGE_CORE_LOOP = STOP_SHIP
ROULETTE_SPAM_WITHOUT_OPPORTUNITY_COST = STOP_SHIP
```

정확한 spin count는 Stage 시간, income reconciliation, merchant/research price와 함께 simulation한다.

## 6. Threat Budget · 단일 스칼라 금지

TU는 기존 simulation의 상대 위협 단위이며 제품 스탯이 아니다.

현재 calibration 역할비:

```text
light_ground = 1.0 TU
armored_anchor = 2.5 TU
flying_raider = 1.5 TU
infiltrator = 1.5 TU
siege_unit = 3.0 TU
stage5_boss_core = 12.0 TU
```

Stage 난도는 다음 벡터로 본다.

```text
THREAT_VECTOR =
- RAW_TU
- ACTIVE_LANE_COUNT
- SIGNATURE_COUNT
- ROUTE_COMPLEXITY
- WAVE_OVERLAP
- ELITE_PRESENCE
- BOSS_PRESENCE_AND_MECHANIC_COMPLEXITY
```

따라서 `RAW_TU`만 증가시키는 HP/supply inflation은 금지한다.

## 7. 4막 Raw-threat search envelope

Act I의 authored baseline을 1.00으로 정규화한다.

```text
Act I   PRESSURE_LITERACY = 1.00 reference
Act II  COMBINATION       = 1.15 ~ 1.35
Act III OPPORTUNITY_COST  = 1.40 ~ 1.65
Act IV  SYNTHESIS         = 1.70 ~ 2.05
```

이 값은 제품 난이도 배율이 아니라 **simulation search envelope**다.

Signature 수, Route 복잡도, overlap이 크게 늘어난 Stage에서는 Raw TU를 낮추는 것이 허용된다. Complexity와 Raw TU를 동시에 최대화해 난도를 이중 상승시키지 않는다.

## 8. Stage 내부 Wave budget

정규화 Stage budget을 1.00으로 볼 때 탐색 범위:

```text
Wave 1      = 20% ~ 30%
Wave 2      = 25% ~ 35%
Final Wave  = 40% ~ 50% / Elite 포함
```

실제 조합은 합계가 100%가 되도록 normalize한다.

Boss Stage:

```text
relative raw TU search target vs same-Act normal median = +25% ~ +45%
```

단, Route/Stance/Sequential Pattern의 인지·행동 복잡도가 높은 Boss는 Raw TU uplift를 줄일 수 있다.

Boss + Elite를 한 순간에 단순 합산해 대응 불가능 burst로 만드는 것은 금지한다.

## 9. Pressure / Route complexity budget

Pressure 자체를 하나의 고정 TU 비용으로 환산해 숨은 단일 점수로 만들지 않는다.

대신:

```text
Pressure complexity = signature interaction cost
Route complexity = number/clarity of relevant route decisions
Overlap complexity = concurrent decision load
```

을 별도 축으로 기록한다.

가드레일:

- 한 Stage의 핵심 대응축 최소 2개.
- Stage 1~5는 single-signature literacy를 우선하고 복잡도 상승을 제한.
- Stage 11~20에서도 동시에 읽어야 하는 핵심 Signature는 기본 최대 3개.
- Final Boss는 5 Pressure를 순차 Pattern으로만 종합 시험.

## 10. Mana Budget

현재 정확한 수급량/상한/시전비는 미확정이다.

따라서 먼저 **결정 기회 수**를 목표로 둔다.

```text
NORMAL_STAGE_MEANINGFUL_T1_CAST_OPPORTUNITIES = 1~2
MANA_CAP_T1_CAST_EQUIVALENT = approximately 2~3
STAGE_TRANSITION_RESET = FALSE
T3_TACTIC_SPAM = FORBIDDEN
```

전술은 잘못된 병력·건물 구조를 계속 지우는 만능 복구 버튼이 아니다.

T1은 자주 쓰는 상황 보정, T2는 복합 압력 전문 보조, T3는 Boss/결정 순간용으로 유지한다.

## 11. Troop / Food Budget

현재 calibration:

```text
STARTING_FOOD_CAP = 12
FARM_T1_BONUS = +6
```

탐색 목표:

```text
NORMAL_PRE_COMMIT_HEADROOM = 15% ~ 30%
LATE_OR_BOSS_PREP_OCCUPANCY = 80% ~ 95%
PERMANENT_ALWAYS_FULL = REVIEW_REQUIRED
```

병력 한도는 상시 세금이 아니라 `새 병력을 넣기 위해 무엇을 포기할지` 판단을 만들어야 한다.

## 12. Merchant Budget

현재 보호 계약:

```text
SLOTS = 4
CURRENCY = Gold only
INFINITE_REROLL = FORBIDDEN
DIRECT_CORE_POWER_SALE = FORBIDDEN
```

Balance 목표:

```text
AT_LEAST_ONE_VALID_PURCHASE_NORMALLY_AFFORDABLE = TARGET
BUY_ALL_FOUR_AS_DEFAULT = FORBIDDEN
TOTAL_STOCK_PRICE > AVERAGE_DISCRETIONARY_GOLD = TARGET
```

상인은 경제 선택을 집중시키는 기회비용 장치이며, 다음 Stage의 필수 정답을 판매하지 않는다.

## 13. 기존 10k robustness 보존

2026-08-09 병영 robustness evidence:

```text
SEED_COUNT = 10000
SPECIAL_TOKEN_SHARE_10_MIN ≈ 0.296265
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333
ROBUSTNESS_10000 = PASS for approved noncombat robustness gates
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

이 증거는 경제/생산/TokenSource robustness lineage로 보존한다.

금지:

```text
10K_PASS -> ALL_COMBAT_NUMERICS_FINAL
10K_PASS -> CURRENT_RUNTIME_ECONOMY_FINAL
```

## 14. Stage 1~5 forgiveness envelope

First-session은 학습 구간이므로 다음을 우선한다.

```text
HIDDEN_HARD_COUNTER = FORBIDDEN
RNG_REMOVES_ALL_VALID_RESPONSES = FORBIDDEN
MIN_RESPONSE_AXES_PER_FORECASTED_PRESSURE >= 2
STAGE1_FOUNDATION_GOLD_SHORTFALL = FORBIDDEN
```

Stage 1~5의 실패는 `몰랐기 때문에 즉사`보다 읽을 수 있었던 선택의 결과가 되도록 한다.

정확한 승률 목표는 사람 플레이 전 확정하지 않는다.

## 15. Stage 20 mastery envelope

Stage 20은 수치 벽이 아니라 누적 설계 종합 시험이다.

```text
PATTERN_1 = MASS + FLYING
PATTERN_2 = ARMORED + SIEGE
PATTERN_3 = INFILTRATION + residual pressure
NEXT_PATTERN_FORECAST = REQUIRED
```

Balance 목표:

- 하나의 극단 전문화가 모든 Pattern을 자동 해결하지 않는다.
- 반대로 한 특정 병종/건물/전술 미보유만으로 자동 패배하지 않는다.
- Resource reserve, lane commitment, tactical timing이 모두 의미 있는 축으로 남는다.

## 16. Machine-readable owner

`docs/analysis/balance/current_normalized_balance_budget.v1.json`

이 JSON은 planning/simulation input envelope이며 runtime data가 아니다.

## 17. 다음 Gate

```text
NEXT_PRODUCT_DECISION = TEXT_UX_AND_STATE_TRANSITION_SPEC
IMAGE_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
IMPLEMENTATION_START = NOT_AUTHORIZED
CURRENT_RUNTIME = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
```
