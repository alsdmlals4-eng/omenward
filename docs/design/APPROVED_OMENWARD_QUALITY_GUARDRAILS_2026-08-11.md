# [현행] OMENWARD 확률 공정성·반복성·복기·난이도·제품표현 Quality Guardrails

```yaml
decision_id: OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1
approved_at: 2026-08-11 KST
approval: USER_DIRECT_PROCEED_AUTHORIZATION
status: USER_APPROVED / CURRENT_PLANNING_CANON / NOT_IMPLEMENTED
work_phase: PHASE_A_GPT_CHAT_PLANNING
benchmark_process: OMW-DEC-20260811-OPS-BENCHMARK-INDUSTRY-RESEARCH-FIRST-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 목적

이 Decision은 새 독립 미니게임이나 수치 성장 시스템을 추가하지 않는다. OMENWARD의 핵심 인과인 다음 구조가 확률 때문에 억울해지거나 반복 플레이에서 암기·정답화되지 않도록 횡단 품질 규칙을 고정한다.

```text
예고된 압력
→ 건물·TokenSource로 제작한 확률
→ 룰렛 조작·결과 확정
→ 비가역 전선 커밋
→ 전투 결과
→ 원인 복기와 다음 설계
```

## 2. RNG 공정성 / Dead-run 방지

```text
RNG_CAN_CHANGE_OPTIMAL_RESPONSE_COST = TRUE
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
SINGLE_UNIT_OR_SINGLE_ROLL_HARD_KEY = FORBIDDEN
FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE
```

- 예고된 핵심 압력에는 최소 두 개 이상의 실질 대응축이 존재해야 한다.
- 대응축은 병종·건물·전술스킬·룰렛/보관 운영 등 현재 코어 시스템 안에서 구성한다.
- 특정 단일 병종 또는 특정 단일 룰렛 결과가 나오지 않았다는 이유만으로 Stage가 사실상 자동 패배가 되면 안 된다.
- RNG는 최적 대응의 효율·비용·경로를 흔들 수 있지만 대응 가능성 자체를 삭제해서는 안 된다.
- 특수병 T1 무작위 선정은 다른 해결법을 요구할 수 있으나 `망한 건설 결과 = 복구 불가능한 런 사망`이 되어서는 안 된다.

## 3. Run variation / Seed 문법

```text
BOSS_CADENCE_FIXED = 5 / 10 / 15 / 20
ELITE_CADENCE_FIXED = EVERY_STAGE_FINAL_WAVE
SEED_VARIATION_MAY_CHANGE = PRESSURE_COMPOSITION / ROUTE / ENEMY_VARIANT / AUTHORED_RULE_VARIATION
FORECAST_AFTER_SEED_RESOLUTION = REQUIRED
HIDDEN_REQUIRED_COUNTER_MUTATION_AFTER_STAGE_START = FORBIDDEN
```

- 고정 landmark는 Boss cadence와 매 Stage 최종 Wave Elite cadence다.
- seed는 압력 조합·Route·적 변형·authored rule variation을 바꿀 수 있다.
- seed가 문제를 바꾸더라도 플레이어에게 필요한 치명적 정보는 Stage 시작 전에 공개한다.
- `랜덤한 문제 / 비랜덤한 핵심 정보`를 기본 원칙으로 사용한다.
- 이미 공개한 요구 대응축을 Stage 시작 뒤 숨은 랜덤으로 바꾸지 않는다.

## 4. Build identity / Soft synergy

```text
BUILD_IDENTITY = BUILDING_DIRECTION + TOKEN_SOURCE_COMPOSITION + TROOP_ROLES + TACTICAL_STYLE + HERO
HARD_SET_BONUS_AS_DEFAULT = FORBIDDEN
SOFT_SYNERGY_DISCOVERY = PREFERRED
```

- 별도의 기본 세트 보너스 시스템을 추가하지 않는다.
- 한 MapRun의 빌드 정체성은 건물 발전 방향, TokenSource 구성, 주요 병종 역할, 전술 사용 성향, 선택 Hero의 결합에서 자연스럽게 드러나야 한다.
- 플레이어가 상호작용을 발견하는 soft synergy를 우선한다.
- `3개 모으면 +30%`처럼 게임이 정답 조합을 직접 지정하는 hard set은 기본 문법으로 사용하지 않는다.
- 단일 빌드가 모든 압력에 항상 우월하면 실패다.

## 5. Causal Review UX

```text
POST_STAGE_CAUSAL_REVIEW = FORECAST -> KEY_EVENTS -> PLAYER_RESPONSE_OUTCOME
PRESCRIPTIVE_NEXT_BUILD_COMMAND = FORBIDDEN
CAUSE_VISIBILITY = REQUIRED
```

Stage 후 복기는 최소 다음 인과를 읽을 수 있어야 한다.

```text
무엇이 예고됐는가
→ 실제 전투에서 어떤 주요 사건이 발생했는가
→ 내 건설·룰렛·전선 커밋·전술 대응이 어떤 결과를 만들었는가
```

- 복기는 원인을 설명하되 다음 정답 빌드를 명령하지 않는다.
- `다음엔 궁병을 지으세요` 같은 처방형 자동 지시를 기본 UX로 사용하지 않는다.
- 실패를 단순 DPS 숫자 하나로 축약하지 않는다.
- 플레이어가 다음 Stage에서 스스로 다른 설계를 선택할 근거를 제공한다.

## 6. Difficulty / Challenge / Seeded Run 확장

```text
META_DIFFICULTY_POWER_STAIRCASE = FORBIDDEN
HORIZONTAL_CHALLENGE_EXPANSION = ALLOWED
SEEDED_RUN = ALLOWED
CHALLENGE_RULES = ALLOWED
RECORDS_AND_HISTORY = ALLOWED
DIFFICULTY_HP_ONLY_SCALING = AVOID
```

- Meta·Hub의 `HORIZONTAL_CONTEXTUAL` 원칙을 유지한다.
- 상위 난이도·Challenge는 압력 조합, 자원 기회비용, Route 해석, 예고된 정보에 대한 대응 난도를 우선 강화한다.
- 단순 적 HP/공격력 배율만으로 상위 난이도를 정의하지 않는다.
- Seeded Run·Challenge Rule·기록/히스토리는 수평 확장 후보로 허용한다.
- 영구 순수 전투력 누적을 난이도 해금의 필수 조건으로 만들지 않는다.

## 7. Non-gambling 제품·UX 가드레일

```text
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
PAID_SPIN = FORBIDDEN
REAL_MONEY_PROBABILITY_PURCHASE = FORBIDDEN
CASINO_CHIP_PRIMARY_FANTASY = AVOID
JACKPOT_EQUALS_VICTORY = FORBIDDEN
```

- 룰렛의 주인공은 `당첨`이 아니라 플레이어가 건물과 TokenSource로 미래 확률을 설계했다는 전략적 인과다.
- 유료 스핀, 현금성 확률 구매, 카지노 칩 중심 제품 판타지, 잭팟이 곧 승리인 구조를 사용하지 않는다.
- 룰렛 비주얼이 있어도 제품 분류는 `ROGUELITE_STRATEGY_AUTO_BATTLER / ROULETTE_PROBABILITY_BUILDER`를 유지한다.

## 8. Benchmark / 현업 조사 판정

2026-08-11 fresh-read work item에서 공식 제품 설명과 현재 유사 장르 사례를 비교했다.

- `Mechabellum` — `ADAPT`: 전략·formation·counter readability를 참고하되 PvP 구조는 복제하지 않는다.
- `The Last Flame` — `ADAPT`: 반복 런의 build causality와 난이도/도전 확장을 참고하되 party-RPG 구조는 복제하지 않는다.
- `Spin Hero` — `ADAPT`: reel이 player-built build engine이 되는 점을 참고하되 deck 구조는 복제하지 않는다.
- `Luck be a Landlord` — `ADAPT`: slot symbol composition과 probability agency를 참고하되 slot 자체를 최종 목적화하지 않는다.
- `Backpack Battles` — `ADAPT`: 전투 전 구성·배치 agency를 참고하되 PvP inventory 문법은 복제하지 않는다.
- `CloverPit` — `TEST / AVOID`: probability manipulation 가독성은 시험 가치가 있으나 gambling/slot/horror identity와 unrestricted snowball을 OMENWARD 정체성으로 채택하지 않는다.
- Elite/Boss 계층 사례 — `ADAPT`: Elite는 일반 적보다 Stage의 전술적 대응을 강화하는 시험, Boss는 별도 패턴과 선택 구조의 상위 시험으로 분리하는 역할 계층만 참고한다.

```text
BENCHMARK_COPY_COMPETITOR_RULES = FORBIDDEN
BENCHMARK_PURPOSE = DECISION_STRESS_TEST_AND_DIFFERENTIATION
```

## 9. 다른 승인안과의 정합성

이 Decision은 다음을 뒤집지 않는다.

- `OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1`
- Hero = contextual amplifier / one Hero per MapRun.
- Legendary = rare constrained sidegrade.
- Meta·Hub = horizontal contextual.
- final product numerics = not approved.
- runtime FV = post-runtime evidence tuning.

Elite/Boss cadence의 정확한 Stage 규칙은 별도 sibling Decision `OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1`가 소유한다.

## 10. 상태 경계

```text
QUALITY_GUARDRAILS = APPROVED
PRODUCT_CODE = UNCHANGED
GODOT_MUTATION = NONE
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PHASE_A = ACTIVE
PHASE_C = BLOCKED
```
