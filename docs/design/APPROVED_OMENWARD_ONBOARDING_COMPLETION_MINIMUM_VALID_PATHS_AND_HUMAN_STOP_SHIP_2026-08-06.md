# [최종 승인] OMENWARD 온보딩 완료·최소 유효 경로·사람 검증 Stop-ship

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-ONBOARDING-COMPLETION-MINIMUM-VALID-PATHS-HUMAN-STOP-SHIP-V1
parent_decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
approval: USER_APPROVED_PROCEED_WITH_RECOMMENDED_FINAL_GATE
status: APPROVED_PLANNING_CANON / NOT_IMPLEMENTED
product_code_authority: NONE
```

```text
DECISION_STATUS = APPROVED_10_OF_10
PARENT_FIRST_10_15_MINUTES_FLOW = PLANNING_COMPLETE
APPROVAL_CHECKPOINT = ONBOARDING_COMPLETION_MINIMUM_VALID_PATHS_AND_HUMAN_STOP_SHIP
```

이 문서는 첫 10~15분 흐름의 마지막 체크포인트다. 보스 처치만으로 온보딩을 완료 처리하지 않고, Stage 1~5의 핵심 행동을 플레이어가 직접 수행했는지와 보상·저장·재시도 상태가 원자적으로 확정됐는지를 함께 검사한다.

## 1. 완료 판정

```text
ONBOARDING_COMPLETE_TRIGGER = ALL_REQUIRED_MILESTONES_PLUS_FIRST_BOSS_CLEAR_PLUS_SUMMARY_ACK
ONBOARDING_FIRST_CLEAR_FLAG_COMMIT = ATOMIC_AFTER_COMPLETION_TRIGGER
EARLY_COMPLETION_FLAG_COMMIT = FORBIDDEN
FIRST_CLEAR_REWARD_COMMIT = EXACTLY_ONCE
STANDARD_RUN_UNLOCK = AFTER_FIRST_CLEAR_FLAG_COMMIT
POST_FIRST_CLEAR_FULL_SKIP_UNLOCK = AFTER_FIRST_CLEAR_FLAG_COMMIT
COMPLETION_FLAG_AND_REWARD_PARTIAL_COMMIT = FORBIDDEN
```

온보딩 완료는 다음 세 조건이 모두 충족된 뒤 확정한다.

1. Stage 1~5의 필수 마일스톤이 모두 기록됐다.
2. 첫 Boss를 본편 전투 규칙으로 처치했다.
3. 전투 후 요약에서 플레이어가 예고·건물·룰렛·배치·전술의 결과 연결을 확인했다.

완료 플래그, 첫 클리어 보상, 표준 Run 해금, 전체 스킵 해금은 하나의 원자적 완료 거래로 처리한다. 일부만 저장하거나 보상을 중복 지급해서는 안 된다.

## 2. Stage별 필수 마일스톤

```text
STAGE1_REQUIRED_MILESTONE = FOUNDATION_ROULETTE_DEPLOYMENT_COMBAT_REVIEW_MERCHANT
STAGE2_REQUIRED_MILESTONE = SHIELD_OR_ARCHER_T2_TOKEN_CHANGE_ROULETTE_CONTROL_DEPLOYMENT
STAGE3_REQUIRED_MILESTONE = MANA_RESEARCH_AND_VALID_MANUAL_TACTIC_CAST
STAGE4_REQUIRED_MILESTONE = DANGER_FORECAST_AND_PLAYER_MITIGATION_DECISION
STAGE5_REQUIRED_MILESTONE = UNSCRIPTED_FIRST_BOSS_CLEAR
```

### Stage 1

- 금고·농장·일반병 병영·방어탑·지휘소·마력탑 T1을 직접 설치한다.
- 기초 세팅을 확인하고 첫 룰렛을 확인한다.
- 병력을 직접 비가역 배치한다.
- 실제 전투 결과와 인과 복기를 확인한다.
- 첫 상인을 확인한다.

### Stage 2

- 방패병 또는 궁병 T2를 실제 골드로 직접 선택한다.
- 자동생산 병종과 TokenSource 변화 전후를 확인한다.
- 룰렛 통제 기능을 최소 한 번 직접 사용한다.
- 선택한 병력으로 직접 전선을 판단하고 배치한다.

### Stage 3

- 마력탑에서 전술 하나를 직접 연구한다.
- 유효한 전투 상황에서 수동으로 한 번 시전한다.
- 마력 비용과 결과를 확인한다.

### Stage 4

- 첫 Danger 예고를 확인한다.
- 건물·병력·배치·전술 중 최소 하나를 직접 조정한다.
- 조정 결과가 전투에 반영되는 것을 확인한다.

### Stage 5

- 새로운 시스템 추가 없이 앞에서 배운 수단을 조합한다.
- Boss는 각본 승리·무적 보정·자동 처치 없이 실제 규칙으로 상대한다.
- 처치 뒤 결과 요약을 확인한다.

## 3. 플레이어 최소 유효 경로

```text
MINIMUM_VALID_PLAYER_PATH_COUNT = TWO
MINIMUM_VALID_PLAYER_PATHS = SHIELD_WITHOUT_SPECIAL / ARCHER_WITHOUT_SPECIAL
SPECIAL_BARRACKS_REQUIRED_FOR_ONBOARDING_COMPLETION = FALSE
ONE_PATH_HARD_COUNTER = FORBIDDEN
SHIELD_PATH_MUST_BE_COMPLETEABLE = REQUIRED
ARCHER_PATH_MUST_BE_COMPLETEABLE = REQUIRED
FACILITATOR_INTERVENTION_FOR_VALID_PATH = FORBIDDEN
DEBUG_OR_CHEAT_FOR_VALID_PATH = FORBIDDEN
```

첫 클리어의 최소 유효 경로는 두 개다.

1. **방패병 경로:** 특수병 병영 없이 방패병 T2를 선택해 Stage 5까지 완료한다.
2. **궁병 경로:** 특수병 병영 없이 궁병 T2를 선택해 Stage 5까지 완료한다.

특수병 병영은 선택 투자이므로 온보딩 완료의 필수 조건이 아니다. 두 기본 경로 모두 진행 가능해야 하며, 한 경로만 통과시키는 적 구성·보스 패턴·강제 힌트·숨은 보정은 금지한다.

## 4. 내부 QA 경로 행렬

```text
INTERNAL_QA_REQUIRED_SCENARIO_COUNT = TWELVE
INTERNAL_QA_BASELINE_SCENARIOS = TWO_NO_SPECIAL_PATHS
INTERNAL_QA_SPECIAL_MATRIX = TWO_T2_PATHS_X_FIVE_SPECIAL_RESULTS
ALL_TWELVE_SCENARIOS_PROGRESSABLE_WITHOUT_DEBUG = REQUIRED
ALL_SPECIAL_T1_RESULTS_HAVE_VALID_USE = REQUIRED
SPECIAL_RESULT_REQUIRED_FOR_CLEAR = FORBIDDEN
SPECIAL_RESULT_SCRIPTED_FOR_QA_PASS = FORBIDDEN
```

출시 전 내부 QA는 다음 12개 시나리오를 모두 통과해야 한다.

- 방패병·특수병 없음
- 궁병·특수병 없음
- 방패병 × 마도사·사제·암살자·비행병·거인
- 궁병 × 마도사·사제·암살자·비행병·거인

이는 플레이어에게 12회 플레이를 요구하는 규칙이 아니라, 무작위 결과와 T2 선택의 조합 중 진행 불가능한 죽은 경로가 없는지 검증하는 내부 행렬이다.

## 5. 사람 검증 표본과 합격선

```text
FIRST_TIME_HUMAN_SAMPLE_MINIMUM = TWENTY
PER_T2_PATH_SAMPLE_MINIMUM = TEN
OVERALL_UNASSISTED_COMPLETION_RATE_MINIMUM = 0.85
PER_PATH_UNASSISTED_COMPLETION_RATE_MINIMUM = 0.80
PATH_COMPLETION_RATE_GAP_MAXIMUM = 0.20
TARGET_MEDIAN_DURATION_MINUTES = 10_TO_15
DURATION_P90_MAXIMUM_MINUTES = 20
CORE_CAUSAL_UNDERSTANDING_RATE_MINIMUM = 0.80
FACILITATOR_GAMEPLAY_INSTRUCTION = FORBIDDEN
OBSERVATION_AND_POST_SESSION_INTERVIEW = ALLOWED
```

최소 20명의 첫 플레이어를 방패병 경로와 궁병 경로에 각각 10명 이상 배정한다. 플레이 중 진행자가 정답·배치·건설·전술을 알려주지 않는다.

### 완료율

- 전체 무개입 완료율 85% 이상.
- 각 T2 경로 무개입 완료율 80% 이상.
- 두 경로 완료율 차이 20%p 이하.

### 시간

- 중앙값은 10~15분 목표.
- 90백분위는 20분 이하여야 한다.
- 빠른 완료를 위해 필수 행동을 자동 처리하거나 전투를 각본화해서는 안 된다.

### 핵심 인과 이해

세션 후 질문에서 80% 이상이 다음 세 관계를 자기 말로 설명해야 한다.

1. 건물과 TokenSource가 룰렛 후보를 어떻게 바꾸는가.
2. 예고와 병력 역할이 배치 판단에 어떻게 연결되는가.
3. T2 선택과 수동 전술이 다음 전투 계획을 어떻게 바꾸는가.

## 6. 절대 Stop-ship

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

다음 중 하나라도 재현되면 출시·구현 승인을 중단한다.

1. 정상 조작으로 진행할 수 없는 막힘이 발생한다.
2. 저장·불러오기·Stage 복구 뒤 건물·골드·생산 타이머·확정 무작위 결과가 손상된다.
3. 완료 전 플래그가 켜지거나 보상·해금이 중복 지급된다.
4. 실패 재시도로 골드·아이템·상점 갱신·무작위 재추첨 이득을 얻는다.
5. 첫 클리어 전 필수 행동·Stage·결정을 건너뛸 수 있다.
6. 벨루가 선택·건설·배치·전술을 대신하거나 정답 절차를 완성해 준다.
7. 방패병·궁병 또는 특수병 5종 중 하나가 진행 불가능한 죽은 경로가 된다.
8. Boss가 각본상 자동 패배하거나 자동 승리한다.
9. 온보딩 전용 재시도 안전 규칙이 표준 Run에 남는다.

## 7. 정량 Hold 기준

다음은 단일 버그가 아니라 표본 결과에 따른 출시 보류 기준이다.

```text
HOLD_IF_OVERALL_COMPLETION_BELOW_0_85 = TRUE
HOLD_IF_ANY_PATH_COMPLETION_BELOW_0_80 = TRUE
HOLD_IF_PATH_GAP_ABOVE_0_20 = TRUE
HOLD_IF_DURATION_P90_ABOVE_20_MINUTES = TRUE
HOLD_IF_CAUSAL_UNDERSTANDING_BELOW_0_80 = TRUE
```

기준 미달 시 힌트만 늘리는 방식으로 덮지 않는다. 먼저 적 압력, 경제 여유, UI 가시성, 선택 가치, 룰렛 인과 표시 중 실제 원인을 진단한다.

## 8. 완료 후 상태

```text
POST_CLEAR_STANDARD_RUN_AVAILABLE = TRUE
POST_CLEAR_FULL_ONBOARDING_SKIP_AVAILABLE = TRUE
POST_CLEAR_REWARDLESS_TUTORIAL_REPLAY_AVAILABLE = TRUE
POST_CLEAR_FIRST_REWARD_REGRANT = FORBIDDEN
POST_CLEAR_TUTORIAL_GRANT_REGRANT = FORBIDDEN
POST_CLEAR_STANDARD_RUN_FAILURE_RULES = REQUIRED
```

첫 클리어 뒤에는 표준 Run과 전체 온보딩 스킵을 해금한다. 설정에서 보상 없는 재학습은 허용하되 첫 클리어 보상과 튜토리얼 지급을 다시 제공하지 않는다.

## 9. 제품 경계와 후속 단계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
FULL_PLANNING_SUITE = NOT_RUN
GITHUB_ACTIONS_GREEN = NOT_PROVEN
```

이 결정으로 첫 10~15분 **기획 승인 10/10**은 완료된다. 그러나 제품 구현, 수치 시뮬레이션, Godot 테스트, 20명 사람 검증, 12개 내부 경로 행렬은 아직 실행되지 않았다.

PR #142는 최신 main과 다시 동기화하고 전체 기획 계약을 실행하기 전까지 Draft를 유지한다.
