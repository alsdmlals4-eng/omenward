# [검토] 첫 10~15분 온보딩 형식·노출 순서 적대적 검토

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: CHECKPOINT_3_REVIEWED
planning_count: 7_OF_10_IN_PROGRESS
review_range: OMW-AUD-492~515
```

## 검토 결론

실제 MapRun 안에서 단계적으로 노출한다는 방향은 유지한다. 다만 기존 권장안처럼 Stage 1에서 T1 건설 선택부터 길게 가르치면 OMENWARD의 중요한 판단인 T2 발전과 비가역 배치가 늦어진다. 따라서 기초 T1 건물은 이미 배치된 상태로 제공하고 역할은 짧게 확인하며, 첫 실제 판단을 T2 업그레이드와 병력 배치에 둔다.

이 수정은 단순 편의가 아니라 핵심 재미 우선순위 교정이다. T1은 용어와 출발 상태, T2는 전략적 발전 방향, 배치는 되돌릴 수 없는 전선 커밋으로 책임을 분리한다.

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
| OMW-AUD-500 | 실패 불가능 구조로 원인 학습 차단 | P1 | scripted victory 금지 |
| OMW-AUD-501 | 후속 노출 순서를 승인 없이 고정 | P0 | 동일 Decision ID와 GrillMe 승인 필요 |
| OMW-AUD-502 | 이미지·HX 제작을 조기 착수 | P1 | 검토 완료 전 제작 금지 |
| OMW-AUD-503 | 문서 체크포인트를 제품 승인으로 오해 | P0 | 제품·데이터·아트 경계 반복 표기 |
| OMW-AUD-504 | `STAGE_ONE_OVERLOAD` | P0 | Stage 1은 핵심 인과와 상인 선택성만 교육 |
| OMW-AUD-505 | `SYSTEM_UNLOCK_WITHOUT_DECISION_USE` | P1 | 즉시 의미 있는 선택에 쓰일 때만 강조 |
| OMW-AUD-506 | 첫 상인에서 4개 슬롯 전략을 모두 강의 | P1 | 선택 사항·골드 기회비용만 교육 |
| OMW-AUD-507 | Stage 2가 이동 조작 연습으로 축소 | P1 | 이동 전후 결과와 다전선 판단 연결 |
| OMW-AUD-508 | Stage 3가 분리된 메뉴 암기 | P1 | 해금·시전·결과의 단일 인과로 교육 |
| OMW-AUD-509 | Danger가 미학습 시스템을 추가 | P0 | 학습 시스템 조합+공개 변형 하나만 허용 |
| OMW-AUD-510 | Boss가 튜토리얼 전용 패턴 사용 | P0 | 본편 Boss 규칙과 동일 |
| OMW-AUD-511 | 승인 순서를 정확 시간·강제 클릭으로 오독 | P1 | 시간·입력·후보 수는 보류 |
| OMW-AUD-512 | `T1_EXPLANATION_OVERLOAD` | P0 | T1 역할은 이름·한 문장·아이콘 수준으로 제한 |
| OMW-AUD-513 | `T1_CONSTRUCTION_FALSE_PRIORITY` | P0 | T1 건설 튜토리얼 금지, T1은 기본 배치 |
| OMW-AUD-514 | T2 선택 전에 차이를 읽을 수 없음 | P0 | 얻는 것·포기하는 것·현재 압력 관계 Preview 필수 |
| OMW-AUD-515 | 기본 건물 수·위치를 승인 없이 고정 | P1 | 정확 인스턴스 수와 위치는 `PENDING_GRILLME` |

## 채택 이유

- 기초건물 설명 시간을 줄이고 실제 전략 차이가 생기는 T2부터 주의를 집중한다.
- 플레이어는 기본 구조를 외우는 대신 현재 압력에 맞는 발전 방향을 읽는다.
- T2 선택과 비가역 배치를 같은 Stage 인과에 연결해 “발전 방향→룰렛 결과→전선 결과”를 빠르게 이해한다.
- Stage 2와 Stage 3는 이전 단계의 인과를 확장하며 별도 루프를 만들지 않는다.
- Stage 4와 Stage 5는 신규 시스템 설명이 아니라 조합 판단과 숙련 확인에 집중한다.

## 비채택안

### T1 직접 건설 선택형

기초 시스템을 직접 조작한다는 장점은 있으나, 단순한 기본 건물 선택이 핵심 전략처럼 과대 강조되고 T2·배치 학습이 늦어진다. `T1_CONSTRUCTION_FALSE_PRIORITY` 때문에 비채택한다.

### T1 장문 설명형

건물별 기능을 먼저 완전히 설명하면 정보는 많아지지만 플레이어가 아직 사용할 판단이 없어 기억 부담만 커진다. 역할 라벨과 재확인 툴팁으로 대체한다.

## 승인된 순서와 경계

```text
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
INITIAL_T1_BUILDINGS = PREBUILT
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_CONSTRUCTION_TUTORIAL = FORBIDDEN
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
FIRST_MEANINGFUL_RULER_CHOICE = T2_UPGRADE_AND_IRREVERSIBLE_DEPLOYMENT
STAGE_1 = PREBUILT_T1_TO_T2_AND_DEPLOYMENT_CAUSAL_CHAIN
STAGE_2 = ROULETTE_CONTROL_AND_MULTI_FRONT
STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC
STAGE_4 = FIRST_DANGER_INTEGRATION
STAGE_5 = FIRST_BOSS_MASTERY_CHECK
MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE
MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST
```

## 남은 검증

```text
INITIAL_T1_INSTANCE_COUNT = PENDING_GRILLME
FIRST_T2_UPGRADE_CANDIDATES = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
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
PREBUILT_T1_BOUNDARY = PASS
FIRST_MEANINGFUL_CHOICE_BOUNDARY = PASS
FULL_7_OF_10_COMPLETION = NOT_READY
IMPLEMENTATION_READINESS = BLOCKED_BY_REMAINING_GRILLME_AND_RUNTIME_PLAN
```
