# [현행] OMENWARD · 20 Stage 콘텐츠와 Boss Arc

```yaml
decision_id: OMW-PLAN-20260820-CONTENT-BOSS-ARC-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-WORLD-ROLE-01
  - OMW-PLAN-20260820-MAPRUN-WORLD-01
  - OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
  - OMW-PLAN-20260820-FIRST5-FTUE-01
  - OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01
supersedes_for_current_content_routing:
  - OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
preserves_cadence_owner:
  - OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1
runtime_mutation: NONE
balance_mutation: NONE
simulation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

20 Stage는 완전 고정 스크립트도, 완전 랜덤 Pressure deck도 아니다.

**4개의 5-Stage 수렴막이라는 authored learning spine을 고정하고, 각 Stage 역할을 해치지 않는 범위에서 bounded variation을 허용한다.**

```text
Stage 1~5   = I막 · 징조 문해 / PRESSURE LITERACY
Stage 6~10  = II막 · 복합 징조 / COMBINATION
Stage 11~15 = III막 · 대가와 선택 / OPPORTUNITY COST
Stage 16~20 = IV막 · 대수렴 / SYNTHESIS
```

Boss landmark:

```text
Stage 5  = Priority Test
Stage 10 = Route Test
Stage 15 = Stance Test
Stage 20 = Sequential Synthesis Test
```

공통 Stage 문법:

```text
BASELINE_WAVE_BEATS = 3
Wave 1 = pressure introduction / opening test
Wave 2 = complication / secondary pressure / route variation
Final Wave = commitment test + Elite
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
```

## 2. Danger Stage 폐기와 재사용 규칙

별도 `Danger Stage` 타입은 존재하지 않는다.

```text
DANGER_STAGE_TYPE = REMOVED
DANGER_STAGES_4_9_14_19 = FORBIDDEN_AS_CURRENT_CADENCE
```

구형 4/9/14/19에서 가치가 있던 아이디어는 **일반 Stage authored variation**으로만 흡수한다.

```text
Stage 4  variation = 공개된 우회 Route
Stage 9  variation = 공개된 Wave overlap timetable
Stage 14 variation = 공개된 주 전선 이동 순서
Stage 19 variation = 공개된 Route convergence
```

이 변주는 Stage 시작 전에 핵심 정보를 공개하며, 특별 보상/별도 Stage type 권한을 갖지 않는다.

## 3. 현행 20 Stage 콘텐츠 매트릭스

정확한 적 수량, spawn 초, Threat Budget, HP/Damage multiplier는 이 문서에서 확정하지 않는다.

| Stage | Act | Working Name | Omen Signature / Pressure | Authored Variation | Final Wave | 핵심 학습/시험 |
|---:|---|---|---|---|---|---|
| 1 | I · 징조 문해 | 범람 전조 | `MASS` | 단일 전선 → 시간차 두 전선 | Elite | 처리량·병력 한도·분산의 의미를 처음 읽는다. |
| 2 | I · 징조 문해 | 철갑 행렬 | `ARMORED` | 소수 장갑 Anchor + 일반 호위 | Elite | 값싼 다수와 집중 화력의 차이를 읽는다. |
| 3 | I · 징조 문해 | 성벽 위의 날개 | `FLYING` | 지상 압력과 공중 후열 압박 분리 | Elite | 지상 전열만 강화해서는 안 된다는 Layer 문제를 배운다. |
| 4 | I · 징조 문해 | 열린 우회로 | `INFILTRATION` | **공개 우회 Route**; 입구·출구·예상 목표 사전 표시 | Elite | 전방 올인 대신 후열/예비대를 남기는 이유를 배운다. |
| 5 | I · 징조 문해 | 제1 수렴 · 공성추 | `SIEGE + MASS` | Boss의 구조물 파괴 준비 동작과 취약창 공개 | **Boss + Elite** | **Priority:** 공성 위협·Boss·다른 전선 중 무엇을 먼저 끊을지 판단한다. |
| 6 | II · 복합 징조 | 방패 뒤의 군세 | `MASS + ARMORED` | 한 전선에서 처리량·집중화력 요구를 겹치고 다음 Wave에서 역할 반전 | Elite | 한 빌드 안에서 광역과 단일 대응을 분배한다. |
| 7 | II · 복합 징조 | 하늘의 칼날 | `FLYING + INFILTRATION` | 공중 대응을 끌어낸 뒤 다른 Route로 후열 압박 | Elite | 대공과 후방 방어를 하나의 병종/위치에 의존하지 않는다. |
| 8 | II · 복합 징조 | 폐허의 행진 | `SIEGE + MASS` | 한 전선은 범람, 다른 전선은 구조물 목표 | Elite | 가장 가까운 적과 가장 위험한 적을 구분한다. |
| 9 | II · 복합 징조 | 교차 공세 시계 | `ARMORED + FLYING` | **Wave overlap timetable 전체 공개** | Elite | 현재 Wave에 전부 쓰지 않고 보관·룰렛·배치 타이밍을 계획한다. |
| 10 | II · 복합 징조 | 제2 수렴 · 사냥지휘관 | `FLYING + INFILTRATION` + 제한 호위 | Boss가 공중/우회 Route를 교대하고 다음 Route 사전 표시 | **Boss + Elite** | **Route:** 현재 위치보다 다음 진입 Route를 보고 후속 병력을 커밋한다. |
| 11 | III · 대가와 선택 | 철갑의 하늘 | `ARMORED + FLYING` | 장갑 요구 전선과 대공 요구 전선을 분리 | Elite | 전문 대응을 한 전선에 몰아 넣을 때 생기는 기회비용을 느낀다. |
| 12 | III · 대가와 선택 | 침묵의 포격 | `INFILTRATION + SIEGE` | 후열 목표와 구조물 목표를 서로 다른 전선에 배치 | Elite | 전열 승리와 구조물 생존을 별도 문제로 본다. |
| 13 | III · 대가와 선택 | 세 전선 포화 | `MASS + FLYING` | 세 전선 모두 의미 있는 압력, 역할은 서로 다름 | Elite | 병력 한도와 전선 전문화의 비용을 판단한다. |
| 14 | III · 대가와 선택 | 이동하는 징조 | `INFILTRATION + ARMORED + FLYING` | **Wave 1/2/3의 주 전선 이동 순서 전체 공개** | Elite | 첫 Wave에 고급 병력을 전부 비가역 배치하지 않고 Run 앞을 계획한다. |
| 15 | III · 대가와 선택 | 대수렴 · 검은 성채 | `ARMORED + SIEGE` + 제한 측면 압력 | Boss `행군 태세 ↔ 포격 태세`; 포격 때 구조물 목표·취약창 공개 | **Boss + Elite** | **Stance:** 방어·구조물 보호·집중 화력 우선순위를 태세에 맞춰 바꾼다. |
| 16 | IV · 대수렴 | 삼중 공세 | `MASS + FLYING + SIEGE` | 각 Pressure를 다른 전선에 나누고 이후 호위로 결합 | Elite | 세 전선을 동일 복제하지 않고 역할별로 구성한다. |
| 17 | IV · 대수렴 | 지휘망 절단 | `ARMORED + INFILTRATION + MASS` | 장갑 전열과 후열 침투를 시간차로 중첩 | Elite | 전방 반응과 후방 예비대를 동시에 유지한다. |
| 18 | IV · 대수렴 | 재의 강하 | `FLYING + SIEGE + INFILTRATION` | 공중/우회/공성 Route가 서로 다른 목표를 압박 | Elite | 다중 Layer와 Target priority를 전역적으로 재조정한다. |
| 19 | IV · 대수렴 | 수렴하는 징조 | **핵심 Signature 최대 3개** | **두 Route가 하나의 결정 전선으로 수렴; 전체 순서 사전 공개** | Elite | 출발 전선이 아니라 실제 종착지·결정 전선을 보고 준비한다. |
| 20 | IV · 대수렴 | 최종 수렴 · 수렴핵 | `FIVE-PRESSURE CAPSTONE`을 순차 Pattern으로 분리 | Pattern 1 `MASS+FLYING` → Pattern 2 `ARMORED+SIEGE` → Pattern 3 `INFILTRATION + 잔존 압력`; 모두 사전 예고 | **Final Boss + Elite** | **Sequential Synthesis:** 20 Stage 동안 만든 전체 빌드를 세 패턴에 어떤 순서로 사용할지 시험한다. |

## 4. I막 · 징조 문해 / Stage 1~5

목표는 각 Pressure의 행동 언어를 처음 이해시키는 것이다.

```text
Stage 1 MASS
→ Stage 2 ARMORED
→ Stage 3 FLYING
→ Stage 4 INFILTRATION
→ Stage 5 SIEGE 중심 Boss
```

이는 Decision `OMW-PLAN-20260820-FIRST5-FTUE-01`과 결합한다.

```text
Stage 1 = 인과 이해
Stage 2 = 미래 수정
Stage 3 = 순간 개입
Stage 4 = 응용 시험 / 새 핵심 시스템 없음
Stage 5 = 첫 Boss + 첫 빌드 결산
```

Stage 4의 우회로 공개는 **새 시스템 소개가 아니라 기존 INFILTRATION/Route를 실제로 응용하는 시험**으로 처리한다.

## 5. II막 · 복합 징조 / Stage 6~10

두 Pressure가 단순히 적 숫자를 합산하는 게 아니라 **서로의 대응을 방해하는 방식**으로 조합돼야 한다.

예:

```text
MASS + ARMORED = 처리량과 집중화력 예산 충돌
FLYING + INFILTRATION = 후열 보호 자원 충돌
SIEGE + MASS = 가까운 적과 위험한 목표의 우선순위 충돌
```

Stage 10 Boss는 Route 자체가 공격 패턴이다. 숨은 전환은 금지한다.

## 6. III막 · 대가와 선택 / Stage 11~15

이 막의 난이도는 주로 **기회비용**에서 발생한다.

```text
모든 Pressure에 최고 대응을 동시에 가질 수 없음
→ Forecast 전체를 보고 어디까지 커버할지 선택
→ 비가역 커밋의 비용이 커짐
→ Stage 15에서 태세 전환 Boss로 우선순위 재평가
```

Stage 14는 전체 주 전선 순서를 미리 보여주므로 정보가 부족해서 어려운 것이 아니라 **정보는 충분하지만 자원이 부족해서 어려운** Stage여야 한다.

## 7. IV막 · 대수렴 / Stage 16~20

새 핵심 시스템을 추가하지 않는다.

Stage 16~20은 이미 만든 다음 구조를 종합 시험한다.

```text
건물 Tier / 전문화
+ TokenSource / 동원 분포
+ 보관 병력
+ 비가역 전선 커밋
+ 마력 전술
+ Forecast 해석
```

Stage 19에서도 한 Wave의 **핵심 Signature는 최대 3개**를 기본 상한으로 두고, 모든 Pressure를 같은 비중으로 한꺼번에 쏟아 가독성을 파괴하지 않는다.

이 `최대 3개`는 콘텐츠 가독성 guardrail이며 exact Threat Budget 숫자를 확정하는 것이 아니다. 실제 human validation에서 더 적거나 다른 조합이 필요하면 조정 가능하다.

## 8. Boss 4종 기능 계약

Boss의 정확한 고유명·외형·수치는 후속 콘텐츠/Visual/Balance에서 조정 가능하지만, **플레이 질문**은 서로 달라야 한다.

| Boss Stage | Boss Function | 플레이어 질문 | 금지 |
|---:|---|---|---|
| 5 | `PRIORITY` | 무엇부터 끊어야 하는가? | 큰 HP만 가진 공성몹 |
| 10 | `ROUTE` | 다음 공격은 어디로 오는가? | 예고 없는 순간이동/랜덤 Route |
| 15 | `STANCE` | 언제 지키고 언제 집중 공격할 것인가? | HP %만 바뀌는 가짜 Phase |
| 20 | `SEQUENTIAL_SYNTHESIS` | 내 전체 빌드를 세 Pattern에 어떤 순서로 배분할 것인가? | 다섯 Pressure 동시 난사 |

Boss는 Elite를 대체하지 않는다.

```text
BOSS_IS_NOT_ELITE_REPLACEMENT = TRUE
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
```

Boss+Elite를 단순 합산해 대응 불가능 burst로 만들지 않는다. Boss Stage 전체 Threat Budget은 Balance 단계에서 별도 검증한다.

## 9. Stage 20 Final Boss Pattern

Stage 20은 `Veil Convergence Front` Decision의 수렴핵/정박체 결산과 연결한다.

### Pattern I · 범람의 징조

```text
MASS + FLYING
```

- 전열 포화와 후열 압박.
- 빌드의 처리량·대공 폭을 시험.

### Pattern II · 붕괴의 징조

```text
ARMORED + SIEGE
```

- 장갑 행군과 구조물 파괴 우선순위.
- 집중 화력과 구조물 보호 판단을 시험.

### Pattern III · 사냥의 징조

```text
INFILTRATION + 이전 Pattern 잔존 압력
```

- 최종 Route와 목표를 완전히 공개.
- 남은 병력·전술·보관 자원을 어디에 마지막으로 커밋할지 시험.

Pattern 전환은 숨은 랜덤이 아니다.

```text
FINAL_BOSS_HIDDEN_PATTERN_SWAP = FORBIDDEN
FINAL_BOSS_NEXT_PATTERN_FORECAST = REQUIRED
```

## 10. Bounded Variation 계약

### Vertical Slice / 첫 콘텐츠 기준선

초기 검증에서는 위 20 Stage authored spine을 가능한 한 안정적으로 유지한다.

목적:

- Pressure/Route 학습 확인.
- FTUE 원인 추적.
- Balance regression 비교.
- 사람 테스트에서 실패 이유를 재현 가능하게 유지.

### 장기 Run 변동 허용

다음은 Stage 역할을 해치지 않는 범위에서 seed/content pack으로 달라질 수 있다.

```text
PRIMARY_LANE
SECONDARY_LANE
allowed secondary Signature
Route variant
Elite identity
Escort package
limited Wave overlap timing
cosmetic/faction presentation
```

### 변동 금지

```text
Stage learning role를 랜덤 교체
Boss Stage 5/10/15/20 이동
Final-wave Elite cadence 삭제
치명 Pressure/Route의 전투 중 무예고 교체
특정 seed가 모든 유효 대응을 제거
```

## 11. 일반 Stage authored variation library

구형 Danger 아이디어를 재사용 가능한 Stage modifier library로 보존한다.

1. `REVEALED_BYPASS_ROUTE`
   - 활성 우회 Route 입구/출구/예상 목표를 사전 공개.
2. `REVEALED_WAVE_OVERLAP_TIMETABLE`
   - Wave 시작 시간과 중첩 가능 구간을 사전 공개.
3. `REVEALED_PRIMARY_LANE_ROTATION`
   - Wave별 주 전선 이동 순서를 사전 공개.
4. `REVEALED_ROUTE_CONVERGENCE`
   - 여러 Route가 어느 결정 전선으로 수렴하는지 사전 공개.

한 Stage에 이런 전역 변주를 여러 개 겹쳐 복잡성을 만들지 않는다.

```text
GLOBAL_AUTHORED_VARIATION_MAX_PER_STAGE = 1 default
```

정확한 예외 허용은 후속 콘텐츠 검증이 필요하다.

## 12. 반복성과 공정성 Guardrail

- Stage 시작 전 주 Pressure, 보조 Pressure, 강도, Route 징후를 읽을 수 있어야 한다.
- Elite 존재는 학습 가능한 고정 landmark다.
- Boss 핵심 행동과 치명적 Route/목표는 사전 읽기가 가능해야 한다.
- 한 Stage가 특정 병종/건물 단 하나를 필수 정답으로 만들지 않는다.
- 높은 난이도는 조합·타이밍·자원 압박을 강화할 수 있지만 대응 수단 자체를 삭제하지 않는다.
- 같은 주 전선을 반복하는 정확한 제한 횟수는 콘텐츠 생성기/데이터 설계 단계에서 결정한다.
- `FLYING` 세계관 의미를 이유로 기존 targeting 권한을 새로 금지하지 않는다.

## 13. Balance / evidence로 넘기는 값

다음은 현재 **미확정**이다.

```text
ELITE_EXACT_COUNT
ELITE_HP_MULTIPLIER
ELITE_DAMAGE_MULTIPLIER
ELITE_MODIFIER_POOL
BOSS_HP
BOSS_DAMAGE
BOSS_EXACT_ENTRY_WAVE
BOSS_EXACT_ENTRY_SECOND
STAGE_THREAT_BUDGET
WAVE_THREAT_BUDGET
PRESSURE_COST
GOLD_INCOME_CURVE
MANA_INCOME_CURVE
TROOP_LIMIT_CURVE
```

이 값들은 다음 `BALANCE_BUDGET` Decision과 deterministic simulation/runtime/human evidence에서 결정한다.

## 14. 대체/보존 관계

구형:

`docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`

처리:

```text
STAGE_TYPE_AND_CADENCE = SUPERSEDED
DANGER_STAGE_TYPE = REJECTED_FOR_CURRENT
4_ACT_LEARNING_CURVE = ABSORBED_AND_REFINED
INDIVIDUAL_STAGE_PRESSURE_IDEAS = ABSORBED_WHERE_COMPATIBLE
DANGER_RULE_IDEAS = REUSED_AS_OPTIONAL_NORMAL_STAGE_VARIATIONS
OLD_EXACT_NAMES = WORKING_LINEAGE_ONLY
```

최신 cadence owner:

`docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md`

이 문서는 2026-08-20 현재 **콘텐츠 매트릭스 owner**이며 cadence owner의 고정 Elite/Boss 규칙을 변경하지 않는다.

## 15. 다음 Gate

```text
NEXT_PRODUCT_DECISION = BALANCE_BUDGET
IMAGE_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
IMPLEMENTATION_START = NOT_AUTHORIZED
CURRENT_RUNTIME = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
```
