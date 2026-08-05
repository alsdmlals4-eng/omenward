# [검토] 첫 10~15분 온보딩 형식·노출 순서 적대적 검토

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: CHECKPOINT_2_REVIEWED
planning_count: 7_OF_10_IN_PROGRESS
review_range: OMW-AUD-492~511
```

## 검토 결론

실제 MapRun 안에서 핵심 인과 사슬을 먼저 완성하고, 룰렛 통제·전술·Danger·Boss를 단계적으로 추가하는 순서는 OMENWARD의 핵심 재미와 가장 잘 맞는다. 다만 Stage 1 과밀, 사용 이유 없는 조기 개방, 첫 상인 과설명, Danger/Boss의 신규 시스템 덤프를 막지 못하면 형식상 단계 노출이어도 실제 경험은 과부하가 된다.

## 감사 항목

| Audit | Risk | Severity | Required control |
|---|---|---:|---|
| OMW-AUD-492 | `TUTORIAL_MAIN_RULE_DRIFT` | P0 | 첫 세션도 실제 경제·전투·저장 규칙 사용 |
| OMW-AUD-493 | `MODAL_OVERLOAD` | P1 | 목표와 직접 관련된 안내만 단계 노출 |
| OMW-AUD-494 | `ANSWER_FOLLOWING_ONBOARDING` | P0 | 벨루가 정답 행동을 대신 선택하지 않음 |
| OMW-AUD-495 | `SCRIPTED_VICTORY_MASKING` | P0 | 승패는 실제 선택과 전투 규칙의 결과 |
| OMW-AUD-496 | `PREMATURE_SYSTEM_EXPOSURE` | P1 | Stage 1 전체 시스템 동시 개방 금지 |
| OMW-AUD-497 | 핵심 재미보다 메뉴 암기를 먼저 요구 | P1 | 압력→선택→결과 인과를 먼저 체험 |
| OMW-AUD-498 | 안내를 닫으면 정보를 다시 찾을 수 없음 | P1 | HUD·툴팁 재확인 경로 필요 |
| OMW-AUD-499 | 튜토리얼 보정이 본편 경제를 왜곡 | P0 | 가짜 자원·가짜 비용 금지 |
| OMW-AUD-500 | 실패 불가능 구조로 원인 학습 차단 | P1 | scripted victory 금지, 실패 피드백은 후속 결정 |
| OMW-AUD-501 | 후속 노출 순서를 승인 없이 고정 | P0 | 승인 전 `SYSTEM_EXPOSURE_ORDER = PENDING_GRILLME` 유지, 승인 뒤 동일 ID로 갱신 |
| OMW-AUD-502 | 이미지·HX 제작을 조기 착수 | P1 | 검토 완료 전 제작 금지 |
| OMW-AUD-503 | 문서 체크포인트를 제품 승인으로 오해 | P0 | 제품·데이터·아트 경계 반복 표기 |
| OMW-AUD-504 | `STAGE_ONE_OVERLOAD` | P0 | Stage 1은 핵심 인과 한 줄과 상인 선택성만 교육 |
| OMW-AUD-505 | `SYSTEM_UNLOCK_WITHOUT_DECISION_USE` | P1 | 새 시스템은 즉시 의미 있는 선택에 사용될 때만 강조 |
| OMW-AUD-506 | 첫 상인에서 4개 슬롯 전략을 모두 강의 | P1 | 선택 사항·골드 기회비용만 교육 |
| OMW-AUD-507 | Stage 2가 이동 조작 연습으로 축소 | P1 | 이동 전후 결과와 두 전선 이상 판단을 함께 요구 |
| OMW-AUD-508 | Stage 3에서 마력탑·연구·전술이 분리된 메뉴 암기 | P1 | 하나의 해금·시전·결과 인과 사슬로 교육 |
| OMW-AUD-509 | Stage 4 Danger가 미학습 신규 시스템을 추가 | P0 | 학습한 시스템 조합+공개 규칙 변형 하나만 허용 |
| OMW-AUD-510 | Stage 5 Boss가 튜토리얼 전용 패턴을 사용 | P0 | 본편 Boss 정보 공개·전투 규칙과 동일 |
| OMW-AUD-511 | 승인된 순서를 정확 시간·강제 클릭 순서로 오독 | P1 | exact timings·입력 강제·후보 수는 후속 승인·사람 QA 전 보류 |

## 채택 이유

- 첫 전투 전에 OMENWARD의 건설→룰렛→배치 인과를 경험해 일반 자동전투 게임으로 오인할 가능성을 줄인다.
- Stage 2와 Stage 3는 이전 단계의 인과를 확장하며 새로운 별도 루프를 만들지 않는다.
- Stage 4와 Stage 5는 신규 시스템 설명이 아니라 조합 판단과 숙련 확인에 집중한다.
- 상인은 정본상 Stage 1 종료 뒤 등장하되, 첫 방문의 교육 범위를 최소화할 수 있다.

## 비채택안

### 전투 우선형

첫 전투는 빠르지만 건물로 룰렛을 설계한다는 핵심 정체성이 늦게 나타나 일반 자동전투 게임처럼 보일 위험 때문에 비채택했다.

### 준비 시스템 선개방형

전투 결과를 보기 전에 건설·룰렛·이동권·마력탑·연구·전술을 모두 학습시켜 `FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN`과 충돌하므로 비채택했다.

## 승인된 순서

```text
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
STAGE_1 = CORE_CAUSAL_CHAIN_AND_FIRST_MERCHANT
STAGE_2 = ROULETTE_CONTROL_AND_MULTI_FRONT
STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC
STAGE_4 = FIRST_DANGER_INTEGRATION
STAGE_5 = FIRST_BOSS_MASTERY_CHECK
MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE
MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST
```

## 남은 검증

```text
FIRST_BUILD_CANDIDATES = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
FIRST_MEANINGFUL_RULER_CHOICE = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
HUMAN_QA_STOP_SHIP = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

## 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
IMAGE_GENERATION = NOT_AUTHORIZED
ANIMATION_HX = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

현재 판정:

```text
CORE_FIT = STRONG
FORMAT_DECISION = PASS
SYSTEM_EXPOSURE_ORDER = PASS
FULL_7_OF_10_COMPLETION = NOT_READY
IMPLEMENTATION_READINESS = BLOCKED_BY_REMAINING_GRILLME_AND_RUNTIME_PLAN
```
