# 적대적 검토 — 특수병 병영 T1 무작위 선정·공개 시점

```yaml
decision_id: OMW-DEC-20260806-PLANNING-SPECIAL-T1-RANDOM-SELECTION-AND-PREVIEW-TIMING-V1
reviewed_at: 2026-08-06 KST
scope: SPECIAL_T1_RANDOM_SELECTION_REVEAL_AND_REROLL_GUARDS
result: CONDITIONALLY_ACCEPTABLE / SIMULATION_AND_HUMAN_QA_PENDING
product_code_authority: NONE
```

## 1. 검토 대상

```text
건설 거래 성공
→ 병영별 특수병 1종 독립 추첨
→ 즉시 결과 공개
→ 첫 생산 타이머 시작
→ T1 동안 같은 병종 반복 생산
```

T1은 TokenSource를 제공하지 않으며 T2 전문화에서 플레이어가 원하는 특수병 계열을 선택한다.

## 2. 대안 비교

### A. 건설 전 결과 공개 — 기각

결과가 마음에 들지 않을 때 건설을 취소해 비용 없이 다시 확인할 수 있어 무작위 선택이 사실상 무료 선택으로 변한다. 건설 노드·비용 선택 전에 결과를 아는 것은 투자 불확실성을 제거한다.

### B. 건설 완료 직후 1종 확정·즉시 공개 — 채택

- 투자 결정 뒤 결과가 확정되므로 무작위성의 기회비용이 유지된다.
- 첫 생산 전에 결과를 알 수 있어 배치·상점·후속 건설 계획을 조정할 시간이 있다.
- 병영별 정체성이 생기고 T2의 선택 전문화가 명확한 개선으로 작동한다.

### C. 첫 생산 완료 시까지 결과 비공개 — 기각

긴 특수병 생산시간 동안 플레이어가 전략 계획을 세울 정보가 부족하다. 결과를 기다리는 시간이 긴데도 대응 선택을 할 수 없어 불확실성이 판단이 아니라 답답함으로 바뀐다.

### D. 매 생산마다 재추첨 — 기각

병영의 역할을 예측할 수 없고, T1 결과가 전선 계획에 지속적으로 반영되지 않는다. 생산마다 큰 기능 차이가 발생해 경제·전투 분산이 지나치게 커지고 T2 전문화의 의미도 약해진다.

## 3. 주요 위험과 완화

### 위험 A — SAVE_SCUM_REROLL

저장 직후 건설하거나 결과 공개 뒤 불러오기를 반복해 원하는 병종을 얻을 수 있다.

```text
MITIGATION
= SPECIAL_T1_SELECTION_SAVE_PERSISTENCE = REQUIRED
= SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
```

난수 결과와 생산 타이머를 저장하고 복구 시 그대로 재사용한다. 구현은 Run seed와 건물 인스턴스 식별자를 포함한 결정론적 검증이 필요하다.

### 위험 B — REVEAL_CANCEL_REROLL

결과 공개 뒤 무료 취소·전액 환급·무료 철거가 가능하면 재추첨 비용이 사라진다.

```text
MITIGATION
= SPECIAL_T1_REVEAL_THEN_FREE_CANCEL = FORBIDDEN
= SPECIAL_T1_FREE_REROLL = FORBIDDEN
```

철거·재건설은 본편의 실제 비용과 시간 규칙을 사용한다. 환급률이 지나치게 높아 재추첨이 자동 최적해가 되면 Stop-ship이다.

### 위험 C — DEAD_ROLL_BY_UPCOMING_PRESSURE

다음 전투가 특정 병종만 요구하면 다른 네 결과는 사실상 실패 결과가 된다.

```text
MITIGATION
= SPECIAL_T1_RESULT_HARD_COUNTER_REQUIREMENT = FORBIDDEN
= ALL_SPECIAL_T1_RESULTS_MUST_HAVE_VALID_USE = REQUIRED
```

특수병 병영은 선택 투자이며 어떤 결과도 다음 진행을 막아서는 안 된다. 특정 기능이 필요한 전투는 일반병·방어탑·전술·배치 등 복수 대응 경로를 가져야 한다.

### 위험 D — RANDOM_VALUE_ASYMMETRY

거인·사제·암살자 등 역할 가치가 상황에 따라 크게 달라 동일 확률이 실제 기대가치의 균형을 보장하지 않는다.

```text
MITIGATION
= SPECIAL_T1_SELECTION_WEIGHTS = PENDING_SIMULATION
= SPECIAL_T1_PRODUCTION_INTERVAL = PENDING_SIMULATION
```

병종별 기능가치·생산시간·전투 기여·실패 분산을 함께 시뮬레이션한다. 한 결과가 모든 상황에서 상위이거나 특정 결과가 반복적으로 무가치하면 가중치·생산시간·역할을 재조정한다.

### 위험 E — T2_OVERRIDE_CONFUSION

플레이어가 T1에서 뽑힌 병종 때문에 T2도 같은 계열로만 올릴 수 있다고 오해할 수 있다.

```text
MITIGATION
= SPECIAL_T2_SELECTION = PLAYER_CHOSEN
= SPECIAL_T2_SPECIALIZATION_OVERRIDES_T1_SELECTION = TRUE
```

결과 공개 UI와 T2 미리보기에서 T1 무작위 정체성은 임시이며 T2에서 원하는 계열을 직접 선택할 수 있다고 명시한다.

### 위험 F — 결과 공개 연출이 생산 완료로 오인됨

건설 직후 병종 아이콘을 보여주면 이미 병력이 지급된 것으로 오해할 수 있다.

```text
MITIGATION
= REVEAL_FIRST_PRODUCTION_COUNTDOWN = REQUIRED
= SPECIAL_T1_PRODUCTION_TIMER_START = AFTER_RESULT_REVEAL
```

선정 결과와 실제 생산 완료를 시각적으로 분리하고 첫 생산까지 남은 시간을 함께 표시한다.

### 위험 G — 건설 실패 시 난수 상태 불일치

골드 차감·노드 점유·건물 생성 중 일부만 실패한 상태에서 선정 결과가 남으면 저장·재현·재시도 결과가 흔들릴 수 있다.

```text
MITIGATION
= SPECIAL_T1_FAILED_CONSTRUCTION_SELECTION = NOT_COMMITTED
```

건설과 선정 결과 확정을 하나의 원자적 거래 경계로 다룬다. 정확한 RNG 소비 방식은 제품 설계에서 결정하되 실패한 건물의 결과가 저장 상태에 남아서는 안 된다.

## 4. 검증 매트릭스

| 항목 | 필수 판정 |
|---|---|
| 선정 시점 | 건설 거래 성공 확정 시점 |
| 공개 시점 | 확정 직후, 첫 생산 타이머 전 |
| 선정 횟수 | 병영별 1회 |
| T1 생산 | 선정 병종만 반복 |
| TokenSource | T1 없음 |
| 저장 복구 | 같은 결과·남은 타이머 유지 |
| 무료 재추첨 | 불가 |
| T2 | 플레이어 선택 병종으로 대체 + TokenSource 해금 |
| 다음 전투 | 다섯 결과 모두 진행 가능 |

## 5. 사람 플레이 Stop-ship

다음 중 하나라도 발생하면 구현 승인 전 재검토한다.

1. 플레이어가 건설 전 결과를 알 수 있다고 오해한다.
2. 결과 공개를 즉시 병력 획득으로 오해한다.
3. 저장·불러오기나 취소·재건설로 사실상 무료 재추첨이 가능하다.
4. 특정 결과가 나오면 다음 전투의 정상 진행이 현저히 어려워진다.
5. 플레이어가 T2 선택이 T1 결과에 종속된다고 오해한다.
6. 한 병종의 기대가치가 다른 결과를 지속적으로 압도한다.

## 6. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 결론

건설 완료 직후 결과를 한 번 확정하고 즉시 공개하는 방식은 무작위 투자의 기회비용을 유지하면서도 첫 생산 전 전략 조정 시간을 제공한다. 다만 저장 재추첨 방지, 철거·환급 경제, 병종별 기대가치 균형과 모든 결과의 유효성은 제품 구현·시뮬레이션·사람 플레이 전까지 미검증 상태다.
