# OMENWARD Quality Guardrails + Elite/Boss Cadence Design

```yaml
date: 2026-08-11
work_phase: PHASE_A_GPT_CHAT_PLANNING
product_runtime_authority: NONE
user_approval:
  quality_guardrails: APPROVED_BY_USER_2026-08-11
  elite_boss_cadence: APPROVED_BY_USER_2026-08-11
base_main_read: 315c66eea9614c284b9c11c4d522141065dfa4b0
omenward_main_read_at_entry: 937d501f6e1fcbad1306dca4b5e8e22fb897af18
omenward_tree_equivalent_current_main_after_accidental_marker_cleanup: 146976b19d53bcc6a3d227288dafd1a5e6efc245
sheet_read: CURRENT_2026-08-11
benchmark_rule: OMW-DEC-20260811-OPS-BENCHMARK-INDUSTRY-RESEARCH-FIRST-V1
```

## 1. 목표

기존 OMENWARD 핵심 인과인 `예고된 압력 → 제작한 확률 → 비가역 전선 커밋 → 결과 복기`를 보호하면서, 확률 기반 게임의 억울한 패배를 줄이고 반복 플레이의 학습·변주를 강화한다. 동시에 구형 `Danger Stage = 4/9/14/19` 구조를 폐기하고, 모든 Stage의 최종 Wave에 Elite 압력을 넣으며 5/10/15/20을 Boss Stage로 고정한다.

## 2. Stage / Elite / Boss cadence

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
ELITE_PRESENCE_REQUIRED = TRUE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_BOSS_PRESENCE_REQUIRED = TRUE
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING
ELITE_EXACT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
BOSS_EXACT_ENTRY_WAVE_AND_NUMERICS = CONTENT_AND_RUNTIME_EVIDENCE_TUNING
```

- Stage 1~20 모두 마지막 Wave에 Elite가 반드시 존재한다.
- Stage 5/10/15/20에는 Boss가 반드시 존재하며, 모든 Stage 공통 규칙 때문에 해당 Stage의 마지막 Wave에도 Elite가 존재한다.
- Boss와 Elite는 서로 다른 위협 계층이다. Elite는 해당 Stage에서 학습한 대응을 강화해 점검하고, Boss는 Act 단위의 선택 구조를 재해석하는 종합시험이다.
- Elite는 단순 HP 배율만 높은 일반 적으로 설계하지 않는다. Stage 압력과 연결되는 역할·행동 차이가 있어야 한다.
- 기존 Stage 4/9/14/19의 authored Route/overlap/pressure 아이디어는 일반 Stage 변주로 재사용할 수 있지만 `Danger Stage`라는 특별 분류나 cadence 권위는 더 이상 갖지 않는다.
- 이미 공개된 위협을 전투 도중 숨은 카운터로 바꾸지 않는다.

## 3. Quality Guardrails

### 3.1 RNG fairness / dead-run prevention

```text
RNG_CAN_CHANGE_OPTIMAL_RESPONSE_COST = TRUE
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
SINGLE_UNIT_OR_SINGLE_ROLL_HARD_KEY = FORBIDDEN
FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE
```

예고된 압력에는 병종·건물·전술·룰렛/보관 운영 중 최소 둘 이상의 실질 대응축이 존재해야 한다. 특정 단일 병종이나 특정 룰렛 결과가 나오지 않았다는 이유만으로 런이 사실상 사망하는 구조를 금지한다.

### 3.2 Run variation / seed grammar

```text
BOSS_CADENCE_FIXED = 5 / 10 / 15 / 20
ELITE_CADENCE_FIXED = EVERY_STAGE_FINAL_WAVE
SEED_VARIATION_MAY_CHANGE = PRESSURE_COMPOSITION / ROUTE / ENEMY_VARIANT / AUTHORED_RULE_VARIATION
FORECAST_AFTER_SEED_RESOLUTION = REQUIRED
HIDDEN_REQUIRED_COUNTER_MUTATION_AFTER_STAGE_START = FORBIDDEN
```

고정 landmark는 유지하되 seed는 문제의 조합을 바꾼다. 랜덤한 문제는 허용하지만 치명적 정보는 Stage 시작 전에 공개한다.

### 3.3 Build identity / soft synergy

```text
BUILD_IDENTITY = BUILDING_DIRECTION + TOKEN_SOURCE_COMPOSITION + TROOP_ROLES + TACTICAL_STYLE + HERO
HARD_SET_BONUS_AS_DEFAULT = FORBIDDEN
SOFT_SYNERGY_DISCOVERY = PREFERRED
```

별도 강제 세트 시스템을 추가하지 않는다. 플레이어가 여러 시스템의 상호작용으로 빌드 정체성을 발견하게 한다.

### 3.4 Causal review UX

```text
POST_STAGE_CAUSAL_REVIEW = FORECAST -> KEY_EVENTS -> PLAYER_RESPONSE_OUTCOME
PRESCRIPTIVE_NEXT_BUILD_COMMAND = FORBIDDEN
CAUSE_VISIBILITY = REQUIRED
```

복기는 원인을 설명하지만 정답을 직접 지시하지 않는다. 플레이어가 다음 설계를 스스로 선택할 여지를 남긴다.

### 3.5 Difficulty / challenge / seeded-run expansion

```text
META_DIFFICULTY_POWER_STAIRCASE = FORBIDDEN
HORIZONTAL_CHALLENGE_EXPANSION = ALLOWED
SEEDED_RUN = ALLOWED
CHALLENGE_RULES = ALLOWED
RECORDS_AND_HISTORY = ALLOWED
DIFFICULTY_HP_ONLY_SCALING = AVOID
```

Meta·Hub의 horizontal-contextual 원칙과 정합화한다. 상위 난이도는 압력 조합·기회비용·예고 후 대응 난도를 우선 강화한다.

### 3.6 Non-gambling product/UX guardrail

```text
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
PAID_SPIN = FORBIDDEN
REAL_MONEY_PROBABILITY_PURCHASE = FORBIDDEN
CASINO_CHIP_PRIMARY_FANTASY = AVOID
JACKPOT_EQUALS_VICTORY = FORBIDDEN
```

룰렛의 주인공은 당첨이 아니라 플레이어가 확률 구조를 만들었다는 전략적 인과다.

## 4. Benchmark packet

Fresh project/Base/Sheet read 뒤 2026-08-11 현재 공식 제품 페이지를 대상으로 재검토했다.

- Ember Knights — `ADAPT`: Elite/Champion을 일반 적보다 더 위험한 변형으로, Boss를 별도 패턴의 상위 시험으로 분리한다. OMENWARD에는 `Elite=Stage 학습 점검`, `Boss=Act 종합시험` 구조만 채택하고 액션 전투 문법은 복제하지 않는다.
- Ravenswatch — `ADAPT`: 반복 런의 고정 목표와 빌드 준비, 난이도/커스텀 모드의 수평 확장 구조를 참고한다. 실시간 액션 타이머 구조는 복제하지 않는다.
- Break Siege — `TEST`: Stage 끝 Boss landmark와 elite/boss roster 분리는 cadence 가독성 참고에 유효하지만, OMENWARD는 매 Stage Boss가 아니라 5-stage 간격 Boss를 유지한다.
- Mega Squad Survivors — `ADAPT`: Elite는 전술적 대응을 요구하고 Boss는 고유 패턴으로 구분하는 역할 계층을 참고한다. 영구 전투력 성장 문법은 OMENWARD Meta 원칙과 충돌하므로 채택하지 않는다.

경쟁작 규칙은 자동 권위가 아니며, 최종 authority는 사용자 승인 OMENWARD Decision이다.

## 5. 대체 관계

이 설계가 정본화되면 다음 구형 current 의미는 대체한다.

```text
DANGER_STAGES = 4 / 9 / 14 / 19
Stage 4 / 9 / 14 / 19 = privileged Danger cadence
Danger Stage = distinct stage type with one global rule mutation
```

다음은 유지한다.

```text
MapRun = 20 Stage
baseline = 3 Wave Beat
Boss stages = 5 / 10 / 15 / 20
forecast-before-commit fairness
irreversible deployment
five pressure taxonomy
final product numerics = not selected
Phase C = blocked until explicit 기획 완료 + Phase B
```

## 6. 검증 기준

- current GDD와 MapRun core에서 `DANGER_STAGE_TYPE = REMOVED`와 `ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE`가 읽혀야 한다.
- old 2026-08-04 pressure matrix는 historical/superseded lineage로 명시되어 current implementation input이 아니어야 한다.
- current documentation router/lifecycle은 새 cadence owner와 quality owner를 가리켜야 한다.
- Stage 5/10/15/20 Boss cadence는 유지되어야 한다.
- Elite/Boss exact count, HP, damage, spawn second는 선택하지 않는다.
- product paths(`data/`, `scripts/`, `scenes/`, `assets/`, `addons/`, `project.godot`)는 변경하지 않는다.
- 같은 Decision IDs를 Google Sheet current/audit/history에 반영한다.

## 7. 상태

```text
DESIGN_APPROVED = TRUE
PRODUCT_CODE = UNCHANGED
GODOT_MUTATION = NONE
FINAL_NUMERICS = NOT_SELECTED
PHASE_A = ACTIVE
PHASE_C = BLOCKED
```
