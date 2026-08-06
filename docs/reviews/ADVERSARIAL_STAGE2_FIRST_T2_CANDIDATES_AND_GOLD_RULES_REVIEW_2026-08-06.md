# 적대적 검토 — Stage 2 최초 T2 후보·골드 규칙

```yaml
decision_id: OMW-DEC-20260806-PLANNING-STAGE2-FIRST-T2-CANDIDATES-AND-GOLD-RULES-V1
reviewed_at: 2026-08-06 KST
scope: FIRST_STAGE2_SHIELD_VS_ARCHER_AND_REAL_GOLD
result: CONDITIONALLY_ACCEPTABLE / SIMULATION_AND_HUMAN_QA_PENDING
product_code_authority: NONE
```

## 1. 검토 대상

```text
FIRST_STAGE2_T2_CANDIDATES
= 일반병 병영 T2 방패병 / 궁병

GOLD
= 같은 비용 등급
+ 실제 골드로 후보 하나만 구매 가능
+ 선택 전 후보 외 소비 차단
+ 기존 골드 보존
```

## 2. 대안 비교

### A. 같은 병영의 방패병·궁병 — 채택

- 두 선택 모두 자동생산과 TokenSource를 바꾸므로 룰렛 통제 학습이 보장된다.
- 버티기와 지속 화력의 차이가 직관적이다.
- 비교 축이 한 건물 안에 머물러 첫 T2 선택의 설명 부담이 낮다.

### B. 일반병 병영과 방어탑을 교차 제시 — 기각

- 방어탑을 선택하면 TokenSource 변화가 없어 Stage 2의 룰렛 통제 학습이 경로별로 달라진다.
- 이동 병력과 고정 방어의 차이까지 한 번에 설명해야 하므로 첫 선택의 원인 복기가 복잡해진다.

### C. 예고·전투 결과에 따라 후보를 동적 생성 — 보류

- 재플레이 다양성은 높지만 첫 플레이 검증과 튜토리얼 QA 경우의 수가 크게 증가한다.
- 고정 후보로 핵심 인과를 검증한 뒤 후속 난이도·재학습 모드에서 검토하는 편이 안전하다.

## 3. 주요 위험과 완화

### 위험 A — FALSE_CHOICE_BY_OMEN

다음 예고가 근접 압력만 과도하게 강조하면 방패병이, 비행 압력을 강조하면 궁병이 사실상 정답이 된다.

```text
MITIGATION
= FIRST_STAGE2_NEXT_PRESSURE = MIXED_SOFT_COUNTER
= SUSTAINED_MIXED_GROUND_PRESSURE
= FLYING_HARD_REQUIREMENT = FALSE
= BOTH_PATHS_VALID = REQUIRED
```

어느 한 분기 없이는 정상 통과가 불가능하면 Stop-ship이다.

### 위험 B — SHIELD_ARCHER_VALUE_ASYMMETRY

같은 비용이라도 방패병의 생존시간과 궁병의 처치 속도 중 하나가 자동생산·TokenSource 양쪽에서 지나치게 높은 총가치를 가질 수 있다.

```text
STOP_SHIP
= 동일 배치 역량에서 한 분기가 생존·처치·룰렛 안정성을 모두 우위
```

정확 비용·생산간격·토큰 가중치·전투 시간은 시뮬레이션에서 함께 비교한다.

### 위험 C — TUTORIAL_ONLY_PRICE_DRIFT

두 후보의 본편 비용이 다른데 첫 판만 할인으로 같게 만들면 본편 경제와 온보딩 경제가 분리된다.

```text
MITIGATION
= FIRST_STAGE2_PAIR_COST_CLASS = SAME
= TUTORIAL_ONLY_DISCOUNT = FORBIDDEN
```

최종 비용이 달라져야 한다면 튜토리얼 할인 대신 첫 후보 조합을 다시 선정한다.

### 위험 D — 예약 골드 우회

실제 골드를 지급한 뒤 상점·추가 건설·다른 업그레이드에 먼저 쓰면 첫 T2 선택이 막힐 수 있다.

```text
MITIGATION
= STAGE_2_REQUIRED_COST_RESERVE = ONE_FIRST_T2_UPGRADE
= STAGE_2_NON_CANDIDATE_SPENDING_BEFORE_CHOICE = BLOCKED
= FIRST_STAGE2_UPGRADE_COUNT_BEFORE_ROULETTE = EXACTLY_ONE
```

거래 실패 시 골드 차감·건물 상태 변경·TokenSource 변경을 모두 원자적으로 되돌려야 한다.

### 위험 E — GLOBAL_LOCK_MISREAD

플레이어가 선택하지 않은 분기를 Run 전체 또는 계정 전체에서 잃는다고 오해할 수 있다.

```text
MITIGATION
= UNCHOSEN_BRANCH_GLOBAL_LOCK = FALSE
= PREVIEW_UNCHOSEN_BRANCH_ACCESS = REQUIRED
= OTHER_GENERAL_BARRACKS_CAN_SELECT_UNCHOSEN_BRANCH = TRUE
```

### 위험 F — 룰렛 변화가 체감되지 않음

선택한 병종의 TokenSource가 첫 룰렛에서 보이지 않으면 선택과 결과의 인과가 약해진다. 반대로 확정 등장으로 조작하면 본편 규칙과 어긋날 수 있다.

```text
MITIGATION
= BEFORE_AFTER_RESULT_COMPARISON = REQUIRED
= RULE_PARITY_WITH_MAIN_RUN = REQUIRED
= GUARANTEED_SCRIPTED_TOKEN_RESULT = FORBIDDEN
```

TokenSource 가중치는 실제 본편 규칙을 사용하되 첫 플레이에서 변화가 통계적으로 관찰 가능한지는 시뮬레이션으로 검증한다.

### 위험 G — 궁병의 비행 우선 설명이 현재 전투의 하드키로 오해됨

궁병 미리보기에 비행 우선이 표시되면 플레이어가 다음 전투에 비행이 필수 등장한다고 해석할 수 있다.

```text
MITIGATION
= 현재 강점: 지속 원거리 화력
= 장기 강점: 비행 우선 대응
= FIRST_STAGE2_FLYING_HARD_REQUIREMENT = FALSE
```

## 4. 검증 매트릭스

| 항목 | 방패병 경로 | 궁병 경로 | 필수 판정 |
|---|---|---|---|
| 자동생산 변화 | 기본 보병→방패병 | 기본 보병→궁병 | 둘 다 명확히 표시 |
| TokenSource 변화 | 방패병 | 궁병 | 본편 규칙과 동일 |
| 주 역할 | 전선 유지·지연 | 지속 원거리 화력 | 역할 중복 금지 |
| 다음 압력 대응 | 시간을 벌어 후열 보호 | 빠른 제거로 압력 완화 | 둘 다 정상 진행 가능 |
| 비용 | 동일 비용 등급 | 동일 비용 등급 | 튜토리얼 할인 금지 |
| 미선택 분기 | 다른 병영에서 후속 선택 가능 | 다른 병영에서 후속 선택 가능 | 전역 잠금 금지 |

## 5. 사람 플레이 Stop-ship

다음 중 하나라도 발생하면 구현 승인 전 설계를 재검토한다.

1. 플레이어 다수가 예고만 보고 한 후보를 명백한 정답으로 인식한다.
2. 한 경로가 합리적 배치로도 다음 압력을 정상 통과하지 못한다.
3. 업그레이드 후 룰렛 변화의 원인을 설명하지 못한다.
4. 선택하지 않은 분기가 영구 소실된다고 오해한다.
5. 지급 골드를 다른 소비로 빼내 첫 T2를 구매하지 못한다.
6. 같은 비용을 맞추기 위해 온보딩 전용 할인·환급이 필요해진다.

정확 기준값과 표본 수는 사람 QA 계획에서 정한다.

## 6. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 결론

방패병과 궁병을 같은 일반병 병영의 첫 T2 후보로 제시하는 안은 Stage 2의 핵심 학습인 **건물 전문화 → 자동생산 변화 → TokenSource 변화 → 룰렛 결과 변화 → 전선 판단**을 두 경로 모두에서 유지한다는 점에서 가장 적합하다.

단, 혼합 압력이 실제로 두 경로를 모두 유효하게 만드는지와 같은 비용에서 총가치가 균형을 이루는지는 시뮬레이션·사람 플레이 전까지 미검증 상태로 남긴다.
