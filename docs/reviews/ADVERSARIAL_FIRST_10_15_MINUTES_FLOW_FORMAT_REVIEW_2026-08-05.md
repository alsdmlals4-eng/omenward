# [검토] 첫 10~15분 온보딩 형식 적대적 검토

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: CHECKPOINT_1_REVIEWED
planning_count: 7_OF_10_IN_PROGRESS
review_range: OMW-AUD-492~503
```

## 검토 결론

실제 MapRun 안에서 시스템을 단계적으로 노출하는 방식은 OMENWARD의 핵심 재미와 가장 잘 맞는다. 다만 아래 실패 조건을 제품 설계와 사람 QA에서 닫기 전에는 7/10 전체 완료로 판정할 수 없다.

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
| OMW-AUD-501 | 후속 노출 순서를 승인 없이 고정 | P0 | `SYSTEM_EXPOSURE_ORDER = PENDING_GRILLME` |
| OMW-AUD-502 | 이미지·HX 제작을 조기 착수 | P1 | 검토 완료 전 제작 금지 |
| OMW-AUD-503 | 문서 체크포인트를 제품 승인으로 오해 | P0 | 제품·데이터·아트 경계 반복 표기 |

## 채택 이유

- 별도 프롤로그보다 튜토리얼과 본편의 규칙 일치성이 높다.
- 모든 시스템 동시 개방보다 인지 부하가 낮다.
- 실제 핵심 선택을 빠르게 수행해 OMENWARD의 정체성을 전달할 수 있다.

## 비채택안

### 별도 프롤로그 튜토리얼

규칙·경제·승패 조건이 실제 MapRun과 달라질 위험과 반복 학습 비용 때문에 비채택했다.

### Stage 1 전체 시스템 개방

선택 원인과 결과가 섞이고 첫 실패를 설명하기 어려워 비채택했다.

## 남은 검증

```text
SYSTEM_EXPOSURE_ORDER = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
DANGER_ONBOARDING = PENDING_GRILLME
BOSS_ONBOARDING = PENDING_GRILLME
MERCHANT_FIRST_EXPOSURE = PENDING_GRILLME
HUMAN_QA_STOP_SHIP = PENDING_GRILLME
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
FULL_7_OF_10_COMPLETION = NOT_READY
IMPLEMENTATION_READINESS = BLOCKED_BY_REMAINING_GRILLME_AND_RUNTIME_PLAN
```
