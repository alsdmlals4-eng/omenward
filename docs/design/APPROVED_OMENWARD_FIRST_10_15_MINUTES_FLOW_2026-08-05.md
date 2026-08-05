# [부분 승인] OMENWARD 첫 10~15분 플레이 흐름

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
decision_status: PARTIAL_APPROVAL_1_OF_10
planning_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: ONBOARDING_FORMAT
product_code_authority: NONE
art_asset_production_authority: NONE
```

## 1. 승인된 결론

```text
DECISION_STATUS = PARTIAL_APPROVAL_1_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
CORE_FUN_FIRST = REQUIRED
```

첫 플레이는 별도 연습장이 아니라 실제 MapRun이다. 건설·룰렛·배치·마력탑·전술 연구·상인을 한꺼번에 설명하지 않고, 실제 목표와 선택에 필요한 시점에 단계적으로 노출한다.

## 2. 핵심 재미 전달 계약

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

## 3. 점진 노출 원칙

- 한 단계에서 현재 목표와 직접 관련된 시스템만 강조한다.
- 새로운 패널을 열 때 기존 핵심 행동을 가리지 않는다.
- 모달 설명을 연속으로 쌓지 않는다.
- 안내를 닫은 뒤 같은 정보를 HUD·툴팁에서 다시 확인할 수 있어야 한다.
- 튜토리얼 완료를 위해 실제 MapRun 규칙을 왜곡하지 않는다.
- 첫 승리는 보장된 연출이 아니라 플레이어 선택과 현행 전투 규칙의 결과여야 한다.

## 4. 아직 승인되지 않은 항목

```text
SYSTEM_EXPOSURE_ORDER = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
FIRST_MEANINGFUL_RULER_CHOICE = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_ONBOARDING = PENDING_GRILLME
BOSS_ONBOARDING = PENDING_GRILLME
MERCHANT_FIRST_EXPOSURE = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
HUMAN_VALIDATION_STOP_SHIP = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

이번 체크포인트는 위 항목을 자동 확정하지 않는다. 특히 Stage별 노출 순서, 최소 유효 경로 수, 첫 상인 설명 범위는 후속 GrillMe 승인 전 구현 입력으로 사용할 수 없다.

## 5. 벤치마킹 채택 원칙

- 복잡한 전략 시스템은 목표 단위로 단계 노출한다.
- 적의 의도와 위협은 행동 전에 읽을 수 있어야 한다.
- 설명 직후 실제 핵심 선택을 수행하게 한다.
- 튜토리얼과 본편의 규칙을 일치시킨다.

특정 게임의 UI나 단계 구성을 그대로 복제하지 않고 OMENWARD의 `예고된 압력 → 제작한 확률 → 비가역 전선 커밋 → 설명 가능한 결과`에 맞춰 채택한다.

## 6. 제품·아트 경계

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

## 7. 다음 GrillMe

다음 결정은 **첫 10~15분의 시스템 노출 순서**다. 승인 전에는 단계 번호나 정확 시간을 정본으로 간주하지 않는다.
