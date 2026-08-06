# [적대적 검토] OMENWARD 병영 2,000-seed Smoke Sweep

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
status: ADVERSARIAL_REVIEW_COMPLETE / CONDITIONAL_FAIL
scope: ANALYSIS_AND_DECISION_QUALITY
```

## 총평

Smoke 실행 자체는 재현 가능하고 입력 해시·공통 seed·9개 벡터·9개 KPI를 남겼다. 그러나 현재 모델은 제품 전투력을 식별할 수 없다. countable KPI 8/9 통과를 근거로 기준 벡터를 추천하면 과대 주장이다.

```text
MODEL_IDENTIFIABILITY_FAIL
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.500000 > 0.45
SMOKE_PASS_ESCALATION_WITHOUT_REVIEW = FORBIDDEN
DECISION_SWEEP = BLOCKED
```

## 1. 일반 경로 유효성의 가정 지배

```text
LOW  = 0.195417
MID  = 1.000000
HIGH = 1.000000
DELTA = 0.804583
```

**공격:** 일반병 경로가 통과한다는 결론은 병영 수치가 아니라 임의로 둔 방어탑·지휘소·전술·기본 전선 지원값에 의해 결정된다.

**판정:** `GENERAL_PATH_VALIDITY_RATE = 1.0`을 제품 결론으로 인용 금지. MID proxy 안에서만 통과한 분석 결과다.

**Stop-ship:** 승인된 player-capability budget 없이 decision sweep 금지.

## 2. 특수병 결과 5종 100% 유효의 허위 안정성

모든 특수병 결과가 `1.0`인 것은 현재 MID 지원이 최소 경로를 이미 거의 해결하고 있기 때문일 수 있다. 특수병 역할 차이가 잘 균형 잡혔다는 독립 증거가 아니다.

**Stop-ship:** 실제 또는 승인 proxy에서 각 특수병이 만드는 marginal clear margin과 실패 압력을 분리하지 못하면 5종 유효성 PASS를 승격하지 않는다.

## 3. 물리 릴 TokenSource burst

```text
SPECIAL_TOKEN_SHARE_10_MIN = 0.296259 / PASS
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.500000 / FAIL
```

**공격:** 평균만 보면 통과하지만 복수 특수병 병영 순간에는 네 출처 중 두 출처가 특수병이 되어 구조적으로 50%를 차지한다.

**판정:** 비용·생산간격 벡터를 조절해도 토큰 출처 수가 같아 모든 9개 벡터가 동일하게 실패했다.

**금지:** 구형 fractional weight를 되살리거나 TokenInstance를 분수화해서 KPI를 맞추지 않는다.

**후속 비교:** 두 번째 TokenSource 활성 지연, 다른 실제 출처에 의한 희석, 복수 특수병 접근 제약, 상한 재설계.

## 4. 두 번째 특수병 한계가치 0의 censoring

`SECOND_SPECIAL_MARGINAL_VALUE_RATIO = 0`은 강한 체감수익 체감의 증거가 아니다. 다수 시나리오에서 10분 전에 두 번째 특수병 생산물이 도착하지 않았기 때문에 관측값이 0이 될 수 있다.

**필수 추가 지표:** 두 번째 병영 구매율, 완공률, 첫 생산 도착률, 10/15분 도착 시각, 미지출 골드와 optional node 점유.

## 5. 비싼·느린 벡터의 낮은 regret 착시

V07/V08의 regret `0.0065`는 다섯 특수병이 균형 잡혔다는 뜻보다 특수병 영향 자체가 늦게 나타나 점수 차이가 축소된 결과일 수 있다.

**판정:** regret만 최소화하는 벡터 선택 금지. 접근률·도착률과 함께 해석한다.

## 6. 룰렛 모델 축소

모델은 자연 중앙줄과 일반 등급만 계산한다. 럭키, 이동권, 가로·세로 이동, 등급 상승, 금화 다중 완성선은 포함하지 않는다.

**영향:** 실제 플레이어 조작은 낮은 자연 당첨률을 개선하고 특정 TokenSource의 가치를 바꿀 수 있다. 현재 결과는 조작 없는 하한 screening이다.

**Stop-ship:** 룰렛 조작 가치를 포함하지 않은 결과를 최종 TokenSource 밸런스로 사용 금지.

## 7. 전투 지속·사상자·비가역 배치 누락

유닛은 죽지 않고 모든 압력에 누적 기여한다. 실제 OMENWARD의 비가역 전선 커밋과 Route 분산 비용이 제거되어 있다.

**영향:** 후반 Stage 유효성, 지원형 병종, 거인·비행병의 포기 비용이 낙관적으로 계산될 수 있다.

**후속:** 제품 수치 확정 전에는 최소한 Stage별 소모·전선 잠금의 무차원 budget을 승인해야 한다.

## 8. 15분 창 censoring

현행 Stage 1~5 기준선은 830초에 종료되므로 900초 결과는 Stage 6을 모델링하지 않고 830초 상태를 유지한다.

**판정:** `15분 KPI`가 실제 15분 활동 결과라고 표현 금지. `STAGE5_END_CENSORED_SNAPSHOT`으로 명시한다.

## 9. 검증 경계

```text
RED = AUTHORITY_AND_RESULT_MISSING
2,000_SEED_EXECUTION = PASS
REPEAT_RUN_BYTE_IDENTICAL = PASS
100_SEED_SCALAR_NUMPY_PARITY = PASS
FOCUSED_UNITTEST = PENDING_FINAL_ROUTER_SYNC
FULL_PRIVATE_REPOSITORY_SUITE = NOT_RUN
GODOT = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

## 최종 판정

```text
SMOKE_EXECUTION_QUALITY = PASS_WITH_CAVEATS
BALANCE_DECISION_READINESS = FAIL
MODEL_IDENTIFIABILITY = FAIL
TOKEN_BURST_GUARDRAIL = FAIL
NEXT_GATE = PLAYER_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION
```
