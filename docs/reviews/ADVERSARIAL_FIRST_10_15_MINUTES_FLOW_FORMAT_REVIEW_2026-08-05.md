# [검토] 첫 10~15분 온보딩 형식·노출 순서 적대적 검토

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: CHECKPOINT_5_REVIEWED
planning_count: 7_OF_10_IN_PROGRESS
review_range: OMW-AUD-492~529
```

## 검토 결론

Stage 1에서 여섯 T1을 실제 골드로 직접 설치하는 방향은 유지한다. 다만 아무 안전 장치 없이 본편 경제와 배치 규칙을 그대로 노출하면 잘못된 위치·지출·부분 거래로 첫 판이 막힐 수 있다.

권장안은 별도 튜토리얼 화폐나 가짜 무료 건설을 만들지 않고, 실제 골드 지갑에 남은 필수 T1 비용만 예약한다. 설치 확인 전에는 허용된 안전 노드 사이의 무료 재배치를 제공하고, 확인 뒤에는 본편의 표준 규칙으로 전환한다. 이는 규칙 드리프트를 최소화하면서 첫 세션의 회복 불가능한 실수를 차단한다.

## 감사 항목

| Audit | Risk | Severity | Required control |
|---|---|---:|---|
| OMW-AUD-492 | `TUTORIAL_MAIN_RULE_DRIFT` | P0 | 첫 세션도 실제 경제·전투·저장 규칙 사용 |
| OMW-AUD-493 | `MODAL_OVERLOAD` | P1 | 목표와 직접 관련된 안내만 단계 노출 |
| OMW-AUD-494 | `ANSWER_FOLLOWING_ONBOARDING` | P0 | 벨루가 정답 행동을 대신 선택하지 않음 |
| OMW-AUD-495 | `SCRIPTED_VICTORY_MASKING` | P0 | 승패는 실제 선택과 전투 규칙의 결과 |
| OMW-AUD-496 | `PREMATURE_SYSTEM_EXPOSURE` | P1 | Stage 1 전체 시스템 동시 개방 금지 |
| OMW-AUD-497 | 핵심 재미보다 메뉴 암기를 먼저 요구 | P1 | 압력→행동→결과 인과를 먼저 체험 |
| OMW-AUD-498 | 안내를 닫으면 정보를 다시 찾을 수 없음 | P1 | HUD·툴팁 재확인 경로 필요 |
| OMW-AUD-499 | 튜토리얼 보정이 본편 경제를 왜곡 | P0 | 가짜 자원·가짜 비용 금지 |
| OMW-AUD-500 | 실패 불가능 구조로 원인 학습 차단 | P1 | scripted victory 금지 |
| OMW-AUD-501 | 후속 노출 순서를 승인 없이 고정 | P0 | 동일 Decision ID와 GrillMe 승인 필요 |
| OMW-AUD-502 | 이미지·HX 제작을 조기 착수 | P1 | 검토 완료 전 제작 금지 |
| OMW-AUD-503 | 문서 체크포인트를 제품 승인으로 오해 | P0 | 제품·데이터·아트 경계 반복 표기 |
| OMW-AUD-504 | `STAGE_ONE_OVERLOAD` | P0 | Stage 1은 기초 설치·첫 배치·결과 인과로 제한 |
| OMW-AUD-505 | `SYSTEM_UNLOCK_WITHOUT_DECISION_USE` | P1 | 즉시 사용할 기능만 강조 |
| OMW-AUD-506 | 첫 상인에서 4개 슬롯 전략을 모두 강의 | P1 | 선택 사항·골드 기회비용만 교육 |
| OMW-AUD-507 | Stage 2가 이동 조작 연습으로 축소 | P1 | T2 발전·이동 전후 결과·다전선 판단 연결 |
| OMW-AUD-508 | Stage 3가 분리된 메뉴 암기 | P1 | 해금·시전·결과의 단일 인과로 교육 |
| OMW-AUD-509 | Danger가 미학습 시스템을 추가 | P0 | 학습 시스템 조합+공개 변형 하나만 허용 |
| OMW-AUD-510 | Boss가 튜토리얼 전용 패턴 사용 | P0 | 본편 Boss 규칙과 동일 |
| OMW-AUD-511 | 승인 순서를 정확 시간·강제 클릭으로 오독 | P1 | 시간·입력·세부 수치는 보류 |
| OMW-AUD-512 | `T1_EXPLANATION_OVERLOAD` | P0 | 건물별 이름·한 문장·아이콘으로 제한 |
| OMW-AUD-513 | `T1_CONSTRUCTION_FALSE_PRIORITY` | P0 | T1은 기초 세팅이며 전략 분기는 Stage 2 |
| OMW-AUD-514 | T2 선택 전에 차이를 읽을 수 없음 | P0 | 이득·포기·현재 압력 관계 Preview 필수 |
| OMW-AUD-515 | 기본 건물 수·위치를 승인 없이 고정 | P1 | 수는 6으로 승인, 정확 좌표는 레벨 레이아웃 보류 |
| OMW-AUD-516 | `T1_BUILD_CHECKLIST_FATIGUE` | P0 | 여섯 설치를 짧은 단계로 처리하고 장문 모달 금지 |
| OMW-AUD-517 | `TUTORIAL_GOLD_ECONOMY_DRIFT` | P0 | 실제 골드·실제 비용 사용, 가짜 자원 금지 |
| OMW-AUD-518 | `MANA_TOWER_EARLY_RESEARCH_DUMP` | P0 | Stage 1은 자원 역할만, 연구 설명은 Stage 3 |
| OMW-AUD-519 | 필수 여섯 건물 비용 부족으로 진행 불가 | P0 | Stage 1 지급 골드는 필수 세트 비용을 보장 |
| OMW-AUD-520 | `FOUNDATION_SETUP_SOFTLOCK` | P0 | 안전 노드·필수 비용 예약·완료 Gate |
| OMW-AUD-521 | Stage 2 T2 후보가 정답/오답으로 구성 | P0 | 두 후보 모두 현재 압력에 유효해야 함 |
| OMW-AUD-522 | T2 지급 골드가 본편 경제와 분리 | P0 | 실제 골드로 후보 하나의 실제 비용을 지불 |
| OMW-AUD-523 | 여섯 T1 설치로 첫 전투가 지나치게 지연 | P1 | 정확 시간은 사람 QA로 검증 |
| OMW-AUD-524 | `RESERVED_GOLD_ESCAPE` | P0 | 필수 세트 완료 전 비필수 소비 차단, 예약액 재계산 |
| OMW-AUD-525 | `FREE_RELOCATION_RULE_LEAK` | P0 | 무료 재배치는 확인 전만, 확인 뒤 표준 규칙 |
| OMW-AUD-526 | `INVALID_PLACEMENT_PARTIAL_COMMIT` | P0 | 생성·점유·차감을 원자 거래로 처리하고 전액 복구 |
| OMW-AUD-527 | 안전 노드가 사실상 하나의 정답 위치를 강제 | P1 | 유형별 복수의 유효 후보와 첫 전투 진행 가능성 검증 |
| OMW-AUD-528 | Foundation 지급액이 경제 이익으로 전환 | P0 | 지급액은 필수 실제 비용 합계, 의도적 surplus 금지 |
| OMW-AUD-529 | 세팅 확인 없이 룰렛으로 진입 | P0 | 여섯 T1+확인 완료 전 첫 룰렛 잠금 |

## 채택 이유

- 별도 튜토리얼 화폐 없이 실제 골드와 실제 비용을 유지한다.
- 필수 비용 예약은 지갑을 분리하지 않고 소프트락만 차단한다.
- 설치 순서는 플레이어에게 맡기되 잘못된 위치를 확인 전에 수정할 수 있다.
- 확인 뒤 무료 이동을 종료해 본편 규칙과의 드리프트를 막는다.
- 원자적 거래 실패 처리로 골드만 차감되거나 노드만 점유되는 부분 상태를 금지한다.

## 승인 계약

```text
DECISION_STATUS = PARTIAL_APPROVAL_5_OF_10
T1_PLACEMENT_POLICY = CATEGORY_COMPATIBLE_SAFE_NODES
T1_BUILD_ORDER = PLAYER_SELECTED
FOUNDATION_SETUP_RELOCATION = FREE_BEFORE_CONFIRMATION
FOUNDATION_SETUP_CONFIRMATION = REQUIRED
POST_CONFIRMATION_PLACEMENT_RULES = STANDARD_RUN_RULES
FREE_RELOCATION_AFTER_CONFIRMATION = FORBIDDEN
STAGE_1_REQUIRED_COST_RESERVE = SUM_OF_UNBUILT_REQUIRED_T1_COSTS
STAGE_1_NON_T1_SPENDING_BEFORE_REQUIRED_SET_COMPLETE = BLOCKED
STAGE_1_LEFTOVER_GOLD_POLICY = NORMAL_WALLET_AFTER_REQUIRED_SET_COMPLETE
FOUNDATION_GRANT_SURPLUS = FORBIDDEN
T1_INVALID_PLACEMENT_TRANSACTION = ATOMIC_ROLLBACK_FULL_REFUND
FIRST_ROULETTE_UNLOCK = AFTER_ALL_SIX_T1_AND_SETUP_CONFIRMATION
EXACT_T1_COSTS = PENDING_SIMULATION
T1_EXACT_NODE_COORDINATES = PENDING_LEVEL_LAYOUT
```

## 대체·금지

```text
SUPERSEDED_PREBUILT_T1_START = IMPLEMENTATION_INPUT_FORBIDDEN
LEGACY_LONG_T1_BUILDING_EXPLANATION = IMPLEMENTATION_INPUT_FORBIDDEN
UNSAFE_UNRESERVED_STAGE1_SPENDING = IMPLEMENTATION_INPUT_FORBIDDEN
FREE_RELOCATION_AFTER_CONFIRMATION = FORBIDDEN
PARTIAL_BUILD_TRANSACTION_COMMIT = FORBIDDEN
```

## 남은 검증

```text
FIRST_T2_UPGRADE_CANDIDATE_IDENTITIES = PENDING_GRILLME
STAGE_2_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
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
FOUNDATION_THEN_BRANCH_ORDER = PASS
T1_PLACEMENT_AND_GOLD_SAFETY = PASS_AS_PLANNING_CONTRACT
FULL_7_OF_10_COMPLETION = NOT_READY
IMPLEMENTATION_READINESS = BLOCKED_BY_REMAINING_GRILLME_AND_RUNTIME_PLAN
```
