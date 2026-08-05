# [검토] 첫 10~15분 온보딩 형식·노출 순서 적대적 검토

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: CHECKPOINT_4_REVIEWED
planning_count: 7_OF_10_IN_PROGRESS
review_range: OMW-AUD-492~523
```

## 검토 결론

사용자 교정에 따라 이전의 `T1 기본 배치`를 폐기한다. 첫 판 1스테이지에서 여섯 T1을 각각 한 개씩 직접 설치하고 짧은 역할 설명을 제공한다. 2스테이지에서는 현재 압력과 관련된 유효 T2 후보 두 개를 비교하고 하나를 지을 수 있는 골드를 지급한다.

이 구조는 건설 조작을 실제 행동으로 익히게 하지만 Stage 1이 체크리스트 노동으로 변하거나, 마력탑 설치가 전술 연구 전체 설명으로 번지는 위험이 있다. 따라서 T1 설치는 기초 세팅, 첫 전투 판단은 비가역 배치, 첫 건물 전략 판단은 Stage 2의 T2 분기로 책임을 분리한다.

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
| OMW-AUD-515 | 기본 건물 수·위치를 승인 없이 고정 | P1 | 수는 6으로 승인, 위치는 후속 GrillMe |
| OMW-AUD-516 | `T1_BUILD_CHECKLIST_FATIGUE` | P0 | 여섯 설치를 짧은 단계로 처리하고 장문 모달 금지 |
| OMW-AUD-517 | `TUTORIAL_GOLD_ECONOMY_DRIFT` | P0 | 실제 골드·실제 비용 사용, 가짜 자원 금지 |
| OMW-AUD-518 | `MANA_TOWER_EARLY_RESEARCH_DUMP` | P0 | Stage 1은 자원 역할만, 연구 설명은 Stage 3 |
| OMW-AUD-519 | 필수 여섯 건물 비용 부족으로 진행 불가 | P0 | Stage 1 지급 골드는 필수 세트 비용을 보장 |
| OMW-AUD-520 | 잘못된 지출·위치로 기초 구축 softlock | P0 | 정확 복구·지출 제한 규칙은 후속 승인 전 구현 금지 |
| OMW-AUD-521 | Stage 2 T2 후보가 정답/오답으로 구성 | P0 | 두 후보 모두 현재 압력에 유효해야 함 |
| OMW-AUD-522 | T2 지급 골드가 본편 경제와 분리 | P0 | 실제 골드로 후보 하나의 실제 비용을 지불 |
| OMW-AUD-523 | 여섯 T1 설치로 첫 전투가 지나치게 지연 | P1 | 정확 시간은 사람 QA로 검증, 한 시점 한 설치 목표 |

## 채택 이유

- 건설 조작을 설명만 듣지 않고 실제로 한 번씩 수행한다.
- 모든 T1의 존재와 기본 역할을 빠르게 익힌 뒤 Stage 2에서 전략 분기를 시작한다.
- Stage 1의 비가역 배치와 Stage 2의 T2 선택을 분리해 전투 판단과 건물 전략 판단을 각각 명확하게 만든다.
- 실제 골드와 실제 비용을 사용해 본편 규칙과 튜토리얼의 경제 드리프트를 막는다.
- 두 T2 후보를 모두 유효하게 만들어 강제 정답형 온보딩을 피한다.

## 대체된 이전안

### T1 기본 배치형

설명 부담은 작지만 플레이어가 건설 조작을 직접 익히지 못한다. 사용자 교정으로 폐기하며 `SUPERSEDED_PREBUILT_T1_START / IMPLEMENTATION_INPUT_FORBIDDEN`으로 격리한다.

### Stage 1 T2 선택형

여섯 T1 설치와 T2 분기까지 같은 Stage에 넣으면 판단 층위가 과밀해진다. T2 선택은 Stage 2로 이동한다.

## 승인된 순서와 경계

```text
SYSTEM_EXPOSURE_ORDER = APPROVED_FOUNDATION_THEN_BRANCH_CHOICE
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_BUILDING_BRANCH_CHOICE = NONE
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
MANA_TOWER_STAGE_1_EXPLANATION = BRIEF_RESOURCE_ROLE_ONLY
TACTICAL_RESEARCH_EXPLANATION_BEFORE_STAGE_3 = FORBIDDEN
```

## 남은 검증

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
T1_DIRECT_BUILD_BOUNDARY = PASS
STAGE2_T2_CHOICE_BOUNDARY = PASS
FULL_7_OF_10_COMPLETION = NOT_READY
IMPLEMENTATION_READINESS = BLOCKED_BY_REMAINING_GRILLME_AND_RUNTIME_PLAN
```
