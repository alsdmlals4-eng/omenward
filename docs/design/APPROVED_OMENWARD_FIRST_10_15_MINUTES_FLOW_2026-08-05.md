# [부분 승인] OMENWARD 첫 10~15분 플레이 흐름

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
decision_status: PARTIAL_APPROVAL_2_OF_10
planning_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: SYSTEM_EXPOSURE_ORDER
product_code_authority: NONE
art_asset_production_authority: NONE
```

## 1. 승인된 결론

```text
DECISION_STATUS = PARTIAL_APPROVAL_2_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
CORE_FUN_FIRST = REQUIRED
```

첫 플레이는 별도 연습장이 아니라 실제 MapRun이다. 건설·룰렛·배치·마력탑·전술 연구·상인을 한꺼번에 설명하지 않고, 실제 목표와 선택에 필요한 순서로 단계적으로 노출한다.

## 2. 승인된 시스템 노출 순서

```text
STAGE_1 = CORE_CAUSAL_CHAIN_AND_FIRST_MERCHANT
STAGE_2 = ROULETTE_CONTROL_AND_MULTI_FRONT
STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC
STAGE_4 = FIRST_DANGER_INTEGRATION
STAGE_5 = FIRST_BOSS_MASTERY_CHECK
```

### Stage 1 — 핵심 인과 사슬과 첫 상인

```text
OMEN_FORECAST
→ BUILD_PREVIEW_AND_CHOICE
→ FIRST_ROULETTE
→ TROOP_RESULT
→ IRREVERSIBLE_DEPLOYMENT
→ REAL_COMBAT
→ CAUSAL_REVIEW
→ FIRST_MERCHANT
```

```text
FIRST_BUILD_CHOICE = REQUIRED
FIRST_BUILD_CANDIDATES = PENDING_GRILLME
MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE
MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST
```

Stage 1은 “건설 선택이 룰렛 결과를 바꾸고, 그 결과를 어느 전선에 커밋했는지가 전투 결과를 만든다”는 한 문장을 실제 행동으로 이해시키는 단계다. 첫 건설의 정확한 후보·가격·수치·효율은 아직 확정하지 않는다.

첫 상인에서는 네 슬롯의 고급 활용법을 모두 강의하지 않는다. 상인이 선택 사항이며, 구매하지 않는 것도 정상이고, 구매 시 다음 Stage의 다른 골드 사용 기회를 포기한다는 사실만 가르친다.

### Stage 2 — 룰렛 통제와 다전선 판단

```text
MOVE_TICKET_EXPOSURE
→ ROW_COLUMN_MOVE_PREVIEW
→ BEFORE_AFTER_RESULT_COMPARISON
→ MULTI_FRONT_PRESSURE_COMPARISON
→ IRREVERSIBLE_DEPLOYMENT
```

Stage 1의 “룰렛 결과를 받는다”에서 Stage 2의 “비용을 들여 결과를 통제한다”로 확장한다. 정확 입력 순서·이동권 지급량·무료 이동 조건은 후속 수치·UX 검증 전 확정하지 않는다.

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

Stage 1~3에서 배운 건설·룰렛 통제·배치·전술을 조합한다. 새 핵심 시스템을 추가하지 않고 공개된 규칙 변형 하나를 통해 조합 판단을 시험한다.

### Stage 5 — 첫 Boss 숙련 확인

새 시스템을 추가하기보다 기존 시스템 이해를 시험한다. Boss의 정확 패턴·압력·실패 허용 범위는 후속 GrillMe 전 구현 입력으로 사용할 수 없다.

## 3. 핵심 재미 전달 계약

첫 10~15분은 기능 목록 암기가 아니라 다음 인과를 직접 체험하게 해야 한다.

```text
예고된 압력
→ 제한된 골드로 건설·룰렛 선택
→ 병력 결과 확인
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

벨루는 현재 목표·사용 가능한 행동·결과 원인을 설명할 수 있지만, 구매·건설·룰렛 이동·전선 배치를 대신 결정하지 않는다.

## 4. 점진 노출 원칙

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
FIRST_BUILD_CANDIDATES = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
FIRST_MEANINGFUL_RULER_CHOICE = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
HUMAN_VALIDATION_STOP_SHIP = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

이번 체크포인트는 위 항목을 자동 확정하지 않는다. 특히 첫 건설 후보, 최소 유효 경로 수, 정확한 Danger/Boss 내용과 실패·재시도 규칙은 후속 GrillMe 승인 전 구현 입력으로 사용할 수 없다.

## 6. 벤치마킹 채택 원칙

- 복잡한 전략 시스템은 목표 단위로 단계 노출한다.
- 적의 의도와 위협은 행동 전에 읽을 수 있어야 한다.
- 설명 직후 실제 핵심 선택을 수행하게 한다.
- 튜토리얼과 본편의 규칙을 일치시킨다.
- 새로운 시스템은 이전 단계의 인과를 이해한 뒤 추가한다.

특정 게임의 UI나 단계 구성을 그대로 복제하지 않고 OMENWARD의 `예고된 압력 → 제작한 확률 → 비가역 전선 커밋 → 설명 가능한 결과`에 맞춰 채택한다.

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

다음 결정은 **Stage 1의 첫 의미 있는 건설·룰렛 선택 구조**다. 승인 전에는 정확한 건물 후보·보정값·최소 유효 경로 수를 정본으로 간주하지 않는다.
