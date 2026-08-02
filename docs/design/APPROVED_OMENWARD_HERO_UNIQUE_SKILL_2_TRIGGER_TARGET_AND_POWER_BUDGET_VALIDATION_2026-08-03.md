# OMENWARD 해금 영웅 고유 2스킬 Trigger·대상·파워 예산 검증 승인안

```yaml
decision_id: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
approved_at: 2026-08-03 08:35 KST
approval: USER_APPROVED_RECOMMENDATION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: UNIQUE_SKILL_2_PUBLIC_TRIGGER_TARGET_RESOLVER_AND_POWER_VALIDATION
parent_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
product_code_authority: NONE
exact_thresholds: PENDING
exact_values: PENDING
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

초기 다섯 해금 영웅의 고유 2스킬은 영웅별 숨은 AI가 아니라 하나의 공개 가능한 공통 Resolver를 사용한다.

```text
READY
→ 공개 Trigger 조건 검사
→ 같은 전선 합법 후보 Filter
→ 공개 Priority Score 계산
→ Trigger 안정화 확인
→ Stable ID 기반 tie-break
→ CAST_PRECHECK 재검증
→ CAST_COMMIT Snapshot 고정
```

- Trigger 필터·우선순위·tie-break는 데이터와 UI 설명으로 공개 가능해야 한다.
- 동일 저장 상태와 동일 입력 순서에서는 같은 시점·대상·위치를 선택한다.
- 정확 임계치, 안정화 시간, 피해·지속시간·범위는 simulation 전까지 고정하지 않는다.
- 숨은 미래 전투 종료 예측, 임의 대상 교체, 수동 발동·보류·타깃은 금지한다.
- 전투 종료 직전 commit 손실은 자동 환불하지 않고 취소율과 체감 가치를 측정해 trigger·timer를 조정한다.

## 2. 공통 Resolver 불변식

```text
SAME_LANE_ONLY = TRUE
PUBLIC_TRIGGER_RULE = REQUIRED
PUBLIC_TARGET_PRIORITY = REQUIRED
DETERMINISTIC_TIE_BREAK = REQUIRED
STABLE_ID_FINAL_TIE_BREAK = REQUIRED
CAST_PRECHECK_REVALIDATION = REQUIRED
COMMIT_SNAPSHOT_IMMUTABLE = TRUE
ARBITRARY_FALLBACK_RETARGET = FORBIDDEN
HIDDEN_FUTURE_BATTLE_END_ORACLE = FORBIDDEN
MANUAL_CAST_OR_TARGET = FORBIDDEN
```

### 2.1 Trigger 평가

- Trigger는 고정된 deterministic 평가 주기에서만 검사한다.
- 한 프레임만 조건이 깜빡이는 발동을 막기 위해 data-defined 안정화 창을 사용할 수 있다.
- 안정화 창의 정확 시간은 simulation 항목이다.
- Trigger가 충족되지 않으면 READY를 보존하고 cooldown을 소비하지 않는다.

### 2.2 후보 Filter

- 현재 같은 전선에 존재하는 합법 전투 객체만 후보가 된다.
- 사망·퇴장·비활성·무적 비대상·다른 전선·건물 등 스킬별 금지 대상은 제거한다.
- Filter 규칙은 영웅별 전용 코드가 아니라 공통 schema의 데이터 항목으로 표현한다.

### 2.3 Priority·tie-break

- 스킬별 공개 Priority Score를 계산한다.
- 점수가 같으면 공개된 2차·3차 기준을 적용한다.
- 최종 동률은 stable object ID 또는 stable quantized position key로 해결한다.
- 랜덤 tie-break와 save/load 재굴림은 금지한다.

### 2.4 CAST_PRECHECK·COMMIT

```text
candidate selected
→ CAST_PRECHECK에서 trigger·candidate 재검증
→ 유효하면 CAST_COMMIT
→ target snapshot 또는 committed position 고정
```

- precheck 실패는 READY 복귀·cooldown 0이다.
- commit 후 규칙은 기존 cooldown·Stage 경계 정본을 따른다.

## 3. 초기 다섯 영웅 Trigger·대상 규칙

### 3.1 방패병 — 불퇴의 성벽

**Trigger 약속**

같은 전선의 전열 압력과 보호 가치가 data-defined 기준 이상일 때 발동한다.

**공개 입력 예시**

- 전열 근접 적의 가중 위협도
- 보호 범위 안 생존 아군 수
- 보호 범위 안 아군의 현재 피해 압력
- 방벽이 흡수할 수 있는 유효 전방 피해 존재 여부

**대상·위치**

```text
owner current frontline anchor
→ same-lane legal protection arc
→ barrier orientation fixed at CAST_COMMIT
```

- 별도 지형·건물·collider·navmesh를 생성하지 않는다.
- 유효 전방 피해가 없거나 보호할 아군이 없으면 READY를 보존한다.
- 정확 압력 threshold·흡수 예산·범위·지속시간은 pending이다.

### 3.2 궁병 — 천공 소거

**Trigger 약속**

같은 전선의 합법 비행 적 수 또는 가중 비행 위협도가 기준 이상일 때 발동한다.

**대상 Snapshot**

```text
same-lane living legal flying enemies at CAST_COMMIT
→ deterministic stable-ID ordered snapshot
→ one simultaneous volley resolution
```

- 지상 유닛·건물·다른 전선은 대상이 아니다.
- commit 후 새로 등장한 비행 적은 포함하지 않는다.
- 정확 최소 수·가중치·target cap·피해는 pending이다.

### 3.3 사제 — 생명의 서약

**Trigger 약속**

같은 전선 생존 아군 전투 유닛 중 data-defined 체력 기준 이하 대상이 존재할 때 발동한다.

**대상 Snapshot**

```text
same-lane living allied combat units
+ current HP ratio below trigger threshold
→ qualifying set at CAST_COMMIT
```

각 대상의 유효 체력 하한은 다음 계약을 유지한다.

```text
effective_floor_per_target
= min(current_hp_at_cast, configured_floor_percent * max_hp)
```

- 회복·부활·건물·성문·타워 보호가 아니다.
- 이미 설정 비율보다 낮은 대상에게 숨은 회복을 주지 않는다.
- 정확 trigger 비율·target cap·하한 비율·지속시간은 pending이다.
- target cap이 필요할 경우 낮은 HP 비율 → 높은 현재 위협도 → stable ID 순으로 선택한다.

### 3.4 마법사 — 메테오

**Trigger 약속**

같은 전선의 적 군집 점수가 기준 이상일 때 발동한다.

**후보 지점**

- 합법 적의 현재 위치를 stable quantized battlefield key로 변환한다.
- 각 후보 지점에서 예상 적중 수와 가중 위협도를 계산한다.

**Priority**

```text
1. expected legal enemy hit count descending
2. total weighted threat descending
3. stable quantized position key ascending
```

- 선택 지점은 CAST_COMMIT에서 고정한다.
- 낙하 예고 후 적이 이동해 회피할 수 있다.
- 다음 Stage 적에게 재타깃하지 않는다.
- 즉발·전역·기본 다중 메테오·기본 지속 장판은 금지한다.
- 정확 반경·최소 군집 점수·예고시간·피해는 pending이다.

### 3.5 암살자 — 그림자 분신

**Trigger 약속**

원본 암살자가 같은 전선에서 합법적인 후열 고가치 표적을 현재 공격할 수 있을 때 발동한다.

**공개 대상 Priority**

```text
1. role priority: support / artillery / high-value ranged role
2. backline depth descending
3. current weighted threat descending
4. stable object ID ascending
```

- Trigger 시 원본 암살자의 현재 합법 표적이 위 Filter를 만족해야 한다.
- 분신은 독립 target selection·pathfinding·skill casting을 하지 않는다.
- 분신은 owner의 현재 합법 표적과 기본 공격 일부만 종속 복제한다.
- 표적이 무효화되면 분신은 독립 재탐색하지 않고 owner 상태를 따른다.
- 정확 역할 weight·복제 비율·지속시간은 pending이다.

## 4. 벤치마크·현업 비교

### 4.1 공식 참고 자료

- Riot Games, `Clarity in League` — 플레이어가 전투 사건을 이해하고 대응할 수 있어야 하며 중요도 위계와 시청각 노이즈를 관리해야 한다.
  - https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/
- Teamfight Tactics, `Neon Nights Gameplay Overview` — `largest group`, `lowest health ally`처럼 자동전투의 대상 규칙을 설명 가능한 문장으로 제공하는 사례.
  - https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/neon-nights-gameplay-overview
- Riot Games, `Champion Balance Framework` 및 `Balancing for Pro Play` — 일관된 측정 기준과 특정 선택의 과도한 필수화를 감시하는 production reference.
  - https://www.leagueoflegends.com/en-us/news/dev/dev-champion-balance-framework/
  - https://www.leagueoflegends.com/en-us/news/dev/dev-balancing-for-pro-play/

이 자료는 Trigger 값·피해량·성공 기준의 직접 권위가 아니다. OMENWARD의 세 전선, 비가역 배치, 전역 고등급 슬롯 1개, Stage 지속 구조에 맞춰 조정한다.

### 4.2 비교 결론

| 접근 | 장점 | 비용·위험 | 판정 |
|---|---|---|---|
| 공개 규칙 + 공통 Resolver | 설명 가능·결정론·공통 QA·저장 안정성 | schema와 UI 설명 필요 | 채택 |
| 영웅별 별도 AI | 개성 표현 자유 | 숨은 판단·예외 코드·테스트 폭증 | 금지 기본값 |
| cooldown 완료 즉시 최근접 사용 | 구현 단순 | 낭비·핵심 역할 붕괴·해금 가치 저하 | 기각 |

## 5. 파워 위계 검증 계약

```text
STANDARD_HERO_POWER
< UNLOCKED_NAMED_HERO_POWER
< STANDARD_LEGENDARY_POWER
```

이 위계는 단일 DPS 숫자가 아니라 대표 encounter 묶음과 전체 전선 결과로 검증한다.

### 5.1 비교 Cohort

```text
A = 표준 [영웅]
B = 같은 source archetype의 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

공통 조건:

- 동일 source Tier·핵심 패시브 단계
- 동일 seed·Stage·적 구성·건물·다른 두 전선 상태
- 고등급 슬롯 1명 규칙 유지
- 가능하면 동일 초기 위치와 동일 ordered input
- Hero 차이를 제외한 변수 고정

### 5.2 대표 Encounter family

최소 다음 family를 포함한다.

```text
NEUTRAL_MIXED
FRONTLINE_PRESSURE
FLYING_HEAVY
ALLY_BURST_CRISIS
DENSE_ENEMY_CLUSTER
DISPERSED_ENEMY_FORMATION
HIGH_VALUE_BACKLINE
LONG_ATTRITION
SHORT_STAGE
LATE_COMMIT_BOUNDARY
```

각 영웅은 의도된 강점 encounter와 조건이 맞지 않는 encounter를 모두 포함한다.

### 5.3 측정 지표

```text
lane victory / defense success rate
objective survival and capture result
time to lane collapse or stabilization
damage dealt and prevented
health-floor prevented lethal damage
valid target coverage
cast count and inter-cast interval
READY waiting time
no-cast rate
precheck failure rate
combat-end committed cancellation rate
active-effect uptime
standard Hero / unlocked Hero / Legendary selection value
other-two-lane contribution and failure rate
```

### 5.4 통과 방향

- B는 자신의 의도된 encounter에서 A보다 명확하고 반복 가능한 전투 가치 상승을 보여야 한다.
- C는 대표 encounter 전체 합산 가치와 지속적 키트 완성도에서 B보다 높아야 한다.
- B의 한 번의 고유 사건이 특정 순간 C의 개별 스킬보다 강할 수 있으나 C의 전체 키트 가치를 지속적으로 넘으면 안 된다.
- 어떤 해금 영웅도 모든 encounter family에서 자동 최선이 되어서는 안 된다.
- 고등급 한 명이 없는 다른 두 전선의 건물·일반·엘리트 운영은 여전히 승패에 중요해야 한다.
- 정확 통계 tolerance·sample size·통과 숫자는 simulation 계획에서 고정한다.

## 6. Stop-ship 조건

다음이 확인되면 구현 승인을 중단하고 설계를 재조정한다.

```text
HIDDEN_OR_NONDETERMINISTIC_TARGETING
SAVE_LOAD_OR_RETRY_REROLL
ONE_FRAME_TRIGGER_FLICKER
ARBITRARY_FALLBACK_RETARGET
UNLOCKED_HERO_AGGREGATE_POWER >= STANDARD_LEGENDARY_AGGREGATE_POWER
ONE_UNLOCKED_HERO_DOMINATES_ALL_ENCOUNTER_FAMILIES
OTHER_TWO_LANES_BECOME_NON_DECISIVE
PRIEST_EFFECT_BECOMES_HEAL_OR_RESURRECTION
METEOR_BECOMES_EFFECTIVELY_UNDODGEABLE
CLONE_GAINS_INDEPENDENT_AI_OR_SKILL_COPY
```

## 7. 적대적 감사

- `OMW-AUD-191`: 숨은 AI 판단은 플레이어 설명·재현·QA를 파괴한다. 공개 schema를 강제한다.
- `OMW-AUD-192`: 한 프레임 Trigger 깜빡임은 우연 발동을 만든다. 안정화 창을 data-driven으로 검증한다.
- `OMW-AUD-193`: 동률 대상이 save/load마다 바뀔 수 있다. stable ID·position tie-break를 강제한다.
- `OMW-AUD-194`: 방벽 Trigger가 너무 흔하면 사실상 상시 방어가 된다. 압력 분포와 uptime을 측정한다.
- `OMW-AUD-195`: 천공 소거가 모든 비행 encounter를 제거하면 공세 설계가 무의미해진다. anti-air 승률과 잔존 위협을 측정한다.
- `OMW-AUD-196`: 생명의 서약이 광역 무적·회복으로 변질될 수 있다. 하한·지속시간·대상 scope를 제한한다.
- `OMW-AUD-197`: 메테오가 즉발 또는 항상 최대 군집을 보장하면 counterplay가 사라진다. 예고·회피·miss rate를 측정한다.
- `OMW-AUD-198`: 분신이 독립 AI·스킬·on-hit를 가지면 신규 유닛 시스템과 전설급 파워로 팽창한다. owner-bound proxy를 강제한다.
- `OMW-AUD-199`: 해금 영웅이 표준 전설의 전체 키트보다 강해질 수 있다. A/B/C encounter matrix를 필수화한다.
- `OMW-AUD-200`: 특정 해금 영웅이 모든 공세에서 자동 최선이 될 수 있다. encounter family별 선택 다양성을 검증한다.
- `OMW-AUD-201`: 종료 직전 commit 취소율이 높으면 해금 보상이 불공정하게 느껴진다. 자동 환불 대신 trigger·timer를 조정한다.
- `OMW-AUD-202`: 고등급 한 명이 나머지 두 전선을 무의미하게 만들 수 있다. three-lane contribution을 별도 지표로 검증한다.

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
PUBLIC_RESOLVER = APPROVED_CONCEPT
EXACT_SCHEMA = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_STABILITY_WINDOWS = PENDING
EXACT_POWER_VALUES = PENDING
SIMULATION_PLAN = REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 Decision은 제품 구현 권한을 부여하지 않는다.