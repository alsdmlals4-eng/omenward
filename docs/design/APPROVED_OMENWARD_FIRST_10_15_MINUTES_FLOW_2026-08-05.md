# [부분 승인] OMENWARD 첫 10~15분 플레이 흐름

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
decision_status: PARTIAL_APPROVAL_4_OF_10
planning_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: STAGE1_T1_SETUP_AND_STAGE2_T2_CHOICE
product_code_authority: NONE
art_asset_production_authority: NONE
```

## 1. 승인된 결론

```text
DECISION_STATUS = PARTIAL_APPROVAL_4_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_FOUNDATION_THEN_BRANCH_CHOICE
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_BUILDING_BRANCH_CHOICE = NONE
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
T2_UPGRADE_PREVIEW = REQUIRED
IRREVERSIBLE_DEPLOYMENT = REQUIRED
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
CORE_FUN_FIRST = REQUIRED
```

첫 판은 실제 MapRun이다. 1스테이지에서 플레이어는 금고·농장·병영·방어탑·지휘소·마력탑 T1을 각각 한 개씩 직접 설치한다. 각 건물은 이름·핵심 역할 한 문장·아이콘 수준으로만 설명하며 장문 기능 강의를 하지 않는다.

1스테이지 지급 골드는 여섯 T1의 실제 비용을 지불할 수 있을 만큼 보장한다. 튜토리얼 전용 가짜 자원이나 무료 가짜 건설 규칙을 만들지 않는다. T1 설치는 분기 선택이 아니라 이후 시스템을 이해하기 위한 기초 세팅이다.

첫 전투 판단은 1스테이지에서 룰렛으로 얻은 병력을 어느 전선에 비가역 배치할지 결정하는 것이다. 첫 건물 전략 판단은 2스테이지에서 현재 압력과 관련된 유효 T2 후보 두 개를 비교하고 하나를 선택해 업그레이드하는 것이다.

## 2. 승인된 시스템 노출 순서

```text
STAGE_1 = BUILD_ONE_EACH_T1_AND_FIRST_DEPLOYMENT
STAGE_2 = FIRST_T2_UPGRADE_CHOICE_AND_ROULETTE_CONTROL
STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC
STAGE_4 = FIRST_DANGER_INTEGRATION
STAGE_5 = FIRST_BOSS_MASTERY_CHECK
```

### Stage 1 — 여섯 T1 설치와 첫 비가역 배치

```text
OMEN_FORECAST
→ STAGE_1_REAL_GOLD_GRANT
→ BUILD_ONE_EACH_ALL_T1
→ FIRST_ROULETTE
→ TROOP_RESULT
→ IRREVERSIBLE_DEPLOYMENT
→ REAL_COMBAT
→ CAUSAL_REVIEW
→ FIRST_MERCHANT
```

```text
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_BUILDING_BRANCH_CHOICE = NONE
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE
MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST
```

여섯 T1은 모두 직접 설치하지만 한 건물마다 긴 모달을 띄우지 않는다. 건설 직전 또는 직후 짧은 역할 라벨을 보여주고 상세 내용은 HUD·툴팁에서 다시 확인할 수 있게 한다.

마력탑도 Stage 1의 여섯 T1에 포함한다. 다만 이때는 “마력을 생산하고 이후 전술 연구에 연결된다”는 짧은 자원 역할만 설명한다. 연구 대상·연구 시간·전술 시전 설명은 Stage 3 전까지 열지 않는다.

```text
MANA_TOWER_T1_INCLUDED_IN_STAGE_1_SET = REQUIRED
MANA_TOWER_STAGE_1_EXPLANATION = BRIEF_RESOURCE_ROLE_ONLY
TACTICAL_RESEARCH_EXPLANATION_BEFORE_STAGE_3 = FORBIDDEN
```

첫 상인에서는 네 슬롯의 고급 활용법을 모두 강의하지 않는다. 구매하지 않는 것도 정상이며, 구매 시 다음 Stage의 다른 골드 사용 기회를 포기한다는 사실만 가르친다.

### Stage 2 — 첫 T2 선택과 룰렛 통제

```text
STAGE_2_T2_GOLD_GRANT
→ T2_CANDIDATE_PREVIEW_AND_CHOICE
→ T2_UPGRADE_CONSTRUCTION
→ MOVE_TICKET_EXPOSURE
→ ROW_COLUMN_MOVE_PREVIEW
→ BEFORE_AFTER_RESULT_COMPARISON
→ MULTI_FRONT_PRESSURE_COMPARISON
→ IRREVERSIBLE_DEPLOYMENT
```

```text
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
T2_UPGRADE_PREVIEW = REQUIRED
```

두 T2 후보는 모두 현재 압력에 대응 가능한 실제 선택이어야 한다. 선택 전 다음을 비교해서 보여준다.

```text
얻는 것
포기하는 것
현재 압력과의 관계
룰렛 또는 전투 결과에 미치는 영향
```

정답 후보와 오답 후보를 연출하지 않으며 벨루는 어느 쪽을 고르라고 대신 결정하지 않는다.

### Stage 3 — 마력탑·연구·수동 전술

```text
MANA_TOWER_RESEARCH_PANEL_EXPOSURE
→ RESEARCH_RELATION_EXPLANATION
→ FIRST_T1_TACTIC_UNLOCK
→ MANUAL_TARGET_LANE_TIMING_SELECTION
→ BEFORE_AFTER_TACTICAL_RESULT_REVIEW
```

Stage 1에서 설치한 마력탑의 연구 기능을 이 시점에 처음 본격적으로 설명한다. 마력탑·연구·전술을 분리된 메뉴 암기가 아니라 하나의 해금·시전·결과 인과로 가르친다.

### Stage 4 — 첫 Danger 통합 시험

Stage 1~3에서 배운 T1 기반·T2 발전·룰렛 통제·배치·전술을 조합한다. 새 핵심 시스템을 추가하지 않고 공개된 규칙 변형 하나로 조합 판단을 시험한다.

### Stage 5 — 첫 Boss 숙련 확인

새 시스템을 추가하기보다 기존 시스템 이해를 시험한다. Boss의 정확 패턴·압력·실패 허용 범위는 후속 GrillMe 전 구현 입력으로 사용할 수 없다.

## 3. 핵심 재미 전달 계약

```text
예고된 압력
→ 실제 골드로 여섯 T1 기초 구축
→ 룰렛 병력 획득
→ 비가역 전선 배치
→ 실제 전투 결과와 복기
→ 다음 Stage의 두 T2 발전안 비교
→ 하나의 발전 방향 선택
→ 룰렛 통제와 전선 판단 확장
```

```text
REAL_ECONOMY_RULES = REQUIRED
REAL_COMBAT_RESULT_RULES = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
BELU_REPLACES_PLAYER_CHOICE = FORBIDDEN
TUTORIAL_ONLY_FAKE_RESOURCE = FORBIDDEN
TUTORIAL_ONLY_FAKE_COMBAT_RULE = FORBIDDEN
```

벨루는 건물의 짧은 역할·현재 목표·사용 가능한 행동·결과 원인을 설명할 수 있다. T1 위치, T2 분기, 룰렛 이동, 전선 배치, 상인 구매를 대신 결정하지 않는다.

## 4. 점진 노출 원칙

- 여섯 T1은 모두 직접 설치하되 설명은 짧게 유지한다.
- T1 설치를 전략적 분기 선택처럼 과장하지 않는다.
- 한 시점의 활성 목표는 하나다.
- 설명 직후 실제 설치 또는 배치를 수행하게 한다.
- 마력탑 설치와 전술 연구 교육을 분리한다.
- 새로운 패널을 열 때 기존 핵심 행동을 가리지 않는다.
- 모달 설명을 연속으로 쌓지 않는다.
- 안내를 닫은 뒤 같은 정보를 HUD·툴팁에서 다시 확인할 수 있어야 한다.
- 첫 승리는 보장된 연출이 아니라 플레이어 배치와 현행 전투 규칙의 결과여야 한다.

## 5. 아직 승인되지 않은 항목

```text
T1_PLACEMENT_LAYOUT = PENDING_GRILLME
T1_BUILD_ORDER = PENDING_GRILLME
STAGE_1_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
STAGE_1_NON_T1_SPENDING_RULE = PENDING_GRILLME
FIRST_T2_UPGRADE_CANDIDATE_IDENTITIES = PENDING_GRILLME
STAGE_2_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
HUMAN_VALIDATION_STOP_SHIP = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

이번 체크포인트는 여섯 T1의 정확 위치·건설 순서·잔여 골드 처리, 두 T2 후보의 정확한 건물·분기 정체, 비용 수치와 시간 배분을 자동 확정하지 않는다.

## 6. 벤치마킹 채택 원칙

- 기초 조작은 짧은 실제 행동으로 익히고 전략 분기는 별도 단계에서 비교한다.
- 실제 자원과 실제 비용을 사용해 본편 경제와 규칙을 일치시킨다.
- 모든 필수 T1을 직접 설치하되 기능 설명을 한꺼번에 쏟아붓지 않는다.
- 선택 전 대가와 결과를 읽게 하고 두 후보 모두 유효하게 만든다.
- 새로운 시스템은 이전 단계의 인과를 이해한 뒤 추가한다.

특정 게임의 UI를 복제하지 않고 OMENWARD의 `기초 구축 → 제작한 확률 → 비가역 배치 → T2 발전 선택 → 설명 가능한 결과`에 맞춰 채택한다.

## 7. 제품·아트 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
IMAGE_GENERATION = NOT_AUTHORIZED
ANIMATION_HX = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

기획 체크포인트 병합은 제품 구현·튜토리얼 UI 제작·이미지·애니메이션·HX 생성을 승인하지 않는다.

## 8. 다음 GrillMe

다음 결정은 **Stage 1 T1 설치 순서·위치 자유도와 실수/잔여 골드 처리 방식**이다. 두 T2 후보의 수는 승인했지만 정확한 후보 정체는 아직 확정하지 않는다.
