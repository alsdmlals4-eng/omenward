# [부분 승인] OMENWARD 첫 10~15분 플레이 흐름

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
decision_status: PARTIAL_APPROVAL_3_OF_10
planning_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PREBUILT_T1_AND_FIRST_MEANINGFUL_CHOICE
product_code_authority: NONE
art_asset_production_authority: NONE
```

## 1. 승인된 결론

```text
DECISION_STATUS = PARTIAL_APPROVAL_3_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
INITIAL_T1_BUILDINGS = PREBUILT
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_CONSTRUCTION_TUTORIAL = FORBIDDEN
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
FIRST_MEANINGFUL_RULER_CHOICE = T2_UPGRADE_AND_IRREVERSIBLE_DEPLOYMENT
T2_UPGRADE_PREVIEW = REQUIRED
IRREVERSIBLE_DEPLOYMENT = REQUIRED
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
CORE_FUN_FIRST = REQUIRED
```

첫 플레이는 별도 연습장이 아니라 실제 MapRun이다. 기초 T1 건물은 플레이 시작 시 이미 배치되어 있으며, 각각의 기본 역할은 짧은 이름·한 문장·핵심 아이콘 수준으로만 설명한다. 플레이어에게 T1 건설법이나 장문의 기능 설명을 먼저 학습시키지 않는다.

첫 실제 판단은 공개된 압력에 맞춰 T2 업그레이드 방향을 읽고 선택하는 것과, 룰렛 결과 병력을 어느 전선에 비가역 배치할지 결정하는 것이다.

## 2. 승인된 시스템 노출 순서

```text
STAGE_1 = PREBUILT_T1_TO_T2_AND_DEPLOYMENT_CAUSAL_CHAIN
STAGE_2 = ROULETTE_CONTROL_AND_MULTI_FRONT
STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC
STAGE_4 = FIRST_DANGER_INTEGRATION
STAGE_5 = FIRST_BOSS_MASTERY_CHECK
```

### Stage 1 — 기본 건물 확인, T2 판단, 배치와 첫 상인

```text
OMEN_FORECAST
→ PREBUILT_T1_QUICK_READ
→ T2_UPGRADE_PREVIEW_AND_CHOICE
→ FIRST_ROULETTE
→ TROOP_RESULT
→ IRREVERSIBLE_DEPLOYMENT
→ REAL_COMBAT
→ CAUSAL_REVIEW
→ FIRST_MERCHANT
```

```text
INITIAL_T1_BUILDINGS = PREBUILT
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_CONSTRUCTION_TUTORIAL = FORBIDDEN
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
FIRST_MEANINGFUL_RULER_CHOICE = T2_UPGRADE_AND_IRREVERSIBLE_DEPLOYMENT
T2_UPGRADE_PREVIEW = REQUIRED
MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE
MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST
```

Stage 1은 “이미 존재하는 기본 생산 구조를 어떤 T2 방향으로 발전시키고, 그 결과를 어느 전선에 커밋했는가”가 실제 전투 결과를 만든다는 인과를 체험시키는 단계다. T1 역할은 빠르게 훑고 지나가며, 업그레이드 선택 전에는 얻는 것·포기하는 것·현재 압력과의 관계를 미리 보여준다.

첫 상인에서는 네 슬롯의 고급 활용법을 모두 강의하지 않는다. 상인이 선택 사항이며, 구매하지 않는 것도 정상이고, 구매 시 다음 Stage의 다른 골드 사용 기회를 포기한다는 사실만 가르친다.

### Stage 2 — 룰렛 통제와 다전선 판단

```text
MOVE_TICKET_EXPOSURE
→ ROW_COLUMN_MOVE_PREVIEW
→ BEFORE_AFTER_RESULT_COMPARISON
→ MULTI_FRONT_PRESSURE_COMPARISON
→ IRREVERSIBLE_DEPLOYMENT
```

Stage 1의 “업그레이드 방향과 결과를 받는다”에서 Stage 2의 “비용을 들여 결과를 통제한다”로 확장한다. 정확 입력 순서·이동권 지급량·무료 이동 조건은 후속 수치·UX 검증 전 확정하지 않는다.

### Stage 3 — 마력탑·연구·수동 전술

```text
MANA_TOWER_EXPOSURE
→ RESEARCH_RELATION_EXPLANATION
→ FIRST_T1_TACTIC_UNLOCK
→ MANUAL_TARGET_LANE_TIMING_SELECTION
→ BEFORE_AFTER_TACTICAL_RESULT_REVIEW
```

마력탑·연구·전술을 분리된 메뉴 암기가 아니라 하나의 인과 사슬로 가르친다. 정확 연구시간·해금 전술·마력 수치는 시뮬레이션 전 고정하지 않는다.

### Stage 4 — 첫 Danger 통합 시험

Stage 1~3에서 배운 T2 발전·룰렛 통제·배치·전술을 조합한다. 새 핵심 시스템을 추가하지 않고 공개된 규칙 변형 하나를 통해 조합 판단을 시험한다.

### Stage 5 — 첫 Boss 숙련 확인

새 시스템을 추가하기보다 기존 시스템 이해를 시험한다. Boss의 정확 패턴·압력·실패 허용 범위는 후속 GrillMe 전 구현 입력으로 사용할 수 없다.

## 3. 핵심 재미 전달 계약

첫 10~15분은 기능 목록 암기가 아니라 다음 인과를 직접 체험하게 해야 한다.

```text
예고된 압력
→ 기본 T1 구조 빠른 확인
→ 제한된 골드로 T2 발전 선택
→ 제작된 룰렛 결과 확인
→ 전선 배치와 확정
→ 실제 전투 결과
→ 원인 복기
→ 다음 선택 수정
```

```text
REAL_ECONOMY_RULES = REQUIRED
REAL_COMBAT_RESULT_RULES = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
BELU_REPLACES_PLAYER_CHOICE = FORBIDDEN
TUTORIAL_ONLY_FAKE_RESOURCE = FORBIDDEN
TUTORIAL_ONLY_FAKE_COMBAT_RULE = FORBIDDEN
```

벨루는 T1 건물의 역할을 짧게 요약하고 현재 목표·사용 가능한 행동·결과 원인을 설명할 수 있다. T2 업그레이드 방향·룰렛 이동·전선 배치·상인 구매를 대신 결정하지 않는다.

## 4. 점진 노출 원칙

- T1 건물 설명은 짧은 역할 확인으로 끝낸다.
- T1 건설 절차를 첫 핵심 과제로 만들지 않는다.
- 한 시점의 활성 목표는 하나다.
- 현재 목표와 직접 관련된 시스템만 강조한다.
- 설명 직후 실제 행동을 수행하게 한다.
- 새로운 패널을 열 때 기존 핵심 행동을 가리지 않는다.
- 모달 설명을 연속으로 쌓지 않는다.
- 안내를 닫은 뒤 같은 정보를 HUD·툴팁에서 다시 확인할 수 있어야 한다.
- 튜토리얼 완료를 위해 실제 MapRun 규칙을 왜곡하지 않는다.
- 첫 승리는 보장된 연출이 아니라 플레이어 선택과 현행 전투 규칙의 결과여야 한다.

## 5. 아직 승인되지 않은 항목

```text
INITIAL_T1_INSTANCE_COUNT = PENDING_GRILLME
FIRST_T2_UPGRADE_CANDIDATES = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
HUMAN_VALIDATION_STOP_SHIP = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

이번 체크포인트는 기본 T1 건물의 정확한 수·위치, 첫 T2 후보, 최소 유효 경로 수, 정확한 Danger/Boss 내용과 실패·재시도 규칙을 자동 확정하지 않는다.

## 6. 벤치마킹 채택 원칙

- 이미 이해 가능한 기본 상태는 짧게 확인하고 실제 판단이 시작되는 지점에 교육 비중을 집중한다.
- 복잡한 전략 시스템은 목표 단위로 단계 노출한다.
- 적의 의도와 위협은 행동 전에 읽을 수 있어야 한다.
- 설명 직후 실제 핵심 선택을 수행하게 한다.
- 튜토리얼과 본편의 규칙을 일치시킨다.
- 새로운 시스템은 이전 단계의 인과를 이해한 뒤 추가한다.

특정 게임의 UI나 단계 구성을 그대로 복제하지 않고 OMENWARD의 `예고된 압력 → T2 발전 → 제작한 확률 → 비가역 전선 커밋 → 설명 가능한 결과`에 맞춰 채택한다.

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

다음 결정은 **첫 세션에서 보여줄 T1 건물 범위와 첫 T2 업그레이드 후보 구조**다. 승인 전에는 정확한 건물 수·위치·후보·보정값·최소 유효 경로 수를 정본으로 간주하지 않는다.
