# 적대적 검토 — 온보딩 완료·최소 유효 경로·사람 검증 Stop-ship

```yaml
decision_id: OMW-DEC-20260806-PLANNING-ONBOARDING-COMPLETION-MINIMUM-VALID-PATHS-HUMAN-STOP-SHIP-V1
reviewed_at: 2026-08-06 KST
result: CONDITIONALLY_ACCEPTABLE / PRODUCT_AND_HUMAN_VALIDATION_PENDING
product_code_authority: NONE
```

## 검토 결론

첫 Boss 처치만 완료 조건으로 사용하면 핵심 시스템을 건너뛴 채 우연히 승리하거나 각본 보정으로 통과할 수 있다. 따라서 Stage 1~5 필수 마일스톤, 실제 Boss 처치, 결과 요약 확인을 원자적으로 묶는 방식이 타당하다.

방패병·궁병의 두 기본 경로는 특수병 병영 없이도 완료 가능해야 한다. 특수병은 선택 투자이므로 필수화하면 기존 Stage 1 계약과 충돌한다.

## 주요 위험

### BOSS_ONLY_FALSE_COMPLETION

Boss 처치만 확인하면 룰렛 통제·마력 연구·Danger 대응을 수행하지 않아도 완료될 수 있다.

완화: 모든 Stage 마일스톤과 결과 요약 확인을 완료 거래에 포함한다.

### COMPLETION_TRANSACTION_SPLIT

보상은 지급됐지만 완료 플래그가 저장되지 않거나, 완료 플래그만 켜져 보상을 다시 받을 수 있는 상태가 생길 수 있다.

완화: 완료 플래그·보상·표준 Run·스킵 해금을 하나의 원자적 거래로 처리한다.

### ROUTE_DOMINANCE

방패병 또는 궁병 중 한 경로가 현저히 쉽거나 다른 경로가 사실상 실패 경로가 될 수 있다.

완화: 경로별 표본 10명 이상, 각 경로 무개입 완료율 80% 이상, 경로 차이 20%p 이하를 요구한다.

### OPTIONAL_SPECIAL_BECOMES_MANDATORY

특정 Boss 패턴이나 Danger가 특정 특수병 결과를 요구하면 선택 건물이 사실상 필수가 된다.

완화: 특수병 없는 두 기본 경로와 2×5 특수병 조합을 별도로 검증한다.

### TEST_MATRIX_OVERCLAIM

12개 시나리오 문서 계약이 실제 전투 가능성을 증명하는 것으로 오해될 수 있다.

완화: 12개는 제품 내부 QA 행렬이며 현재는 NOT_RUN으로 유지한다.

### METRIC_GAMING

10~15분 목표를 맞추기 위해 전투를 각본화하거나 필수 행동을 자동 처리할 수 있다.

완화: 필수 행동 자동 해결과 각본 승리를 절대 Stop-ship으로 둔다.

### FACILITATOR_CONTAMINATION

진행자가 플레이 중 정답을 알려 완료율을 부풀릴 수 있다.

완화: 관찰과 사후 인터뷰만 허용하고 플레이 중 게임플레이 지시는 금지한다.

### CAUSAL_RECALL_WITHOUT_REAL_UNDERSTANDING

문구를 외운 플레이어가 실제로 계획을 수정하지 못할 수 있다.

완화: 사후 질문은 정의 암기가 아니라 건물→TokenSource→룰렛, 예고→배치, T2·전술→후속 계획의 자기 설명을 요구한다.

### TUTORIAL_SAFETY_RULE_LEAK

온보딩 체크포인트 복구가 표준 Run에 남으면 실패 규칙과 경제가 왜곡된다.

완화: 첫 클리어 플래그 이후 표준 Run 실패 규칙으로 명시적으로 전환한다.

## 절대 Stop-ship 재확인

```text
STOP_SHIP_PROGRESSION_BLOCKER = TRUE
STOP_SHIP_SAVE_OR_CHECKPOINT_CORRUPTION = TRUE
STOP_SHIP_REWARD_DUPLICATION_OR_EARLY_FLAG = TRUE
STOP_SHIP_RETRY_REROLL_OR_RESOURCE_GAIN = TRUE
STOP_SHIP_REQUIRED_ACTION_BYPASS = TRUE
STOP_SHIP_BELU_AUTO_RESOLUTION = TRUE
STOP_SHIP_ANY_T2_OR_SPECIAL_RESULT_DEAD_PATH = TRUE
STOP_SHIP_SCRIPTED_BOSS_VICTORY = TRUE
STOP_SHIP_TUTORIAL_RETRY_LEAKS_TO_STANDARD_RUN = TRUE
```

## 판정 한계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
INTERNAL_QA_TWELVE_SCENARIOS = NOT_RUN
FIRST_TIME_HUMAN_SAMPLE = NOT_RUN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
FULL_PLANNING_SUITE = NOT_RUN
```

## 최종 판정

기획 구조는 조건부 수용 가능하다. 다만 제품 구현 뒤 12개 시나리오와 최소 20명 사람 검증을 통과하기 전에는 온보딩이 실제로 완료됐거나 출시 준비가 끝났다고 주장할 수 없다.
