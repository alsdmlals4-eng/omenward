# 오멘워드 경제·메타·유료 Retry 100,000-seed 시뮬레이션 계약

- 결정 ID: `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1`
- 작성일: `2026-08-01`
- 상태: `CURRENT_SIMULATION_CONTRACT / NOT_IMPLEMENTED / NOT_RUN`
- 상위 정본: `docs/design/APPROVED_OMENWARD_ECONOMY_RETRY_SAVE_CHECKPOINT_PLANNING_CONTRACT_2026-08-01.md`
- Parameter Registry: `docs/design/OMENWARD_ECONOMY_RETRY_SAVE_PARAMETER_REGISTRY_V1.json`
- 제품 코드 권한: `NONE`

이 계약은 정확한 경제값을 승인하기 전에 실행할 재현 가능한 대량 시뮬레이션을 정의한다. 시뮬레이터가 존재한다는 사실이나 평균값 하나만으로 제품 밸런스가 검증됐다고 주장하지 않는다.

---

## 1. 질문

1. 건물·릴·이동·판매·보관·배치 중 하나가 항상 우월한가?
2. 일반적인 플레이에서 공세 대응에 필요한 최소 선택권이 유지되는가?
3. 접전지·금고·금화 결과가 복구 불가능한 스노우볼을 만드는가?
4. 판매·취소·수리·철거에 무한 차익거래가 있는가?
5. Retry 비용이 후반 피로 완화와 패배 긴장 사이에서 실제 선택이 되는가?
6. 동일 seed·입력은 동일 경제·checkpoint·Retry 결과를 만드는가?

---

## 2. 실행 묶음

### Suite A — 단일 MapRun 경제

- Candidate set마다 최소 `100,000`개 고정 seed.
- 20 Stage 전체 또는 조기 패배까지 실행.
- Normal을 기준으로 하고 난이도 multiplier는 별도 층으로 분리한다.
- 같은 seed set을 모든 Candidate와 policy에 재사용한다.

### Suite B — 메타·Retry 장기 궤적

- Candidate set마다 최소 `100,000`개 profile trajectory.
- 각 trajectory는 여러 MapRun의 정산·소비·Retry 선택을 포함한다.
- 첫 런·초기 사용자와 반복 플레이 사용자를 분리한다.
- 현재 런 미정산 영구재화는 모든 경우 비용 잔액에서 제외한다.

### Suite C — 거래·저장 fault injection

대량 확률 실행과 별개로 다음 fault point를 전수 검사한다.

```text
journal PREPARED 뒤 중단
checkpoint temporary write 뒤 중단
profile 차감 준비 뒤 중단
checkpoint validation 실패
atomic replace 실패
current checksum 실패
backup checksum 실패
schema migration 실패
동일 idempotency key 재호출
```

Suite C는 `100,000` 무작위 실행으로 대체하지 않는다. 각 fault point와 transaction type을 결정론적으로 커버한다.

---

## 3. Candidate set

최소 세 후보군을 비교한다.

```text
H0 = Legacy 수치에서 현재 구조로 직접 옮길 수 있는 값만 참조한 역사 기준 후보
H1 = 전선 안정과 구조 투자 균형 후보
H2 = 릴 조작과 보관·판매 선택을 더 자주 허용하는 후보
```

규칙:

- H0는 제품 승인 수치가 아니라 비교 기준이다.
- Candidate 차이는 Parameter Registry override 파일 하나로 표현한다.
- Candidate마다 config hash를 생성한다.
- 한 번에 너무 많은 축을 변경하지 않는다. 변경 축과 가설을 기록한다.
- 실패 후보도 삭제하지 않고 결과 artifact와 rejection reason을 보존한다.

---

## 4. 플레이 정책 모델

최소 다음 deterministic policy를 사용한다.

### P0 — 안전 우선

- 현재 가장 위험한 라인의 즉시 전투력과 식량 안정 우선.
- 고위험 경제 투자와 과도한 보관을 회피.

### P1 — 균형

- 공개 공세를 충족한 뒤 건물·릴·보관을 분산.
- 제품 기본 비교 정책.

### P2 — 건물·TokenSource 투자

- 금고·병영·농장·타워·지휘소의 중장기 구조 효과 우선.
- 초기 전선 부족 위험을 감수.

### P3 — 릴·이동 집중

- 유료 회전과 `n×P` 이동을 적극 사용.
- 건물은 TokenSource와 최소 방어 중심.

### P4 — 보관·선택 지연

- PendingReward 보관을 적극 사용하고 확실한 공세 대응 때 배치.
- 저장 용량·기회비용을 검증.

### P5 — 판매·현금화

- 낮은 적합도 결과를 판매해 건물·회전에 재투자.
- 차익거래와 판매 우월성을 검증.

### P6 — 무작위 합법 행동

- 합법 행동 중 seed 기반 무작위 선택.
- 사람이 선택하지 않을 경계 조합과 상태 공간 탐색.

Policy는 정답 AI가 아니다. 경제 구조의 민감도와 지배 전략을 찾는 테스트 모델이다.

---

## 5. 공통 입력

```yaml
simulation_input:
  candidate_id
  candidate_config_hash
  seed_set_id
  seed
  policy_id
  difficulty_id
  stage_manifest_version
  content_manifest_version
  rng_algorithm_version
  parameter_registry_version
  initial_profile_state_id
  retry_behavior_policy
```

동일 입력은 동일 ordered event log와 final state hash를 생성해야 한다.

---

## 6. 이벤트 기록

최소 이벤트:

```text
RUN_STARTED
STAGE_PREPARATION_ENTERED
INCOME_GRANTED
CONSTRUCTION_QUOTED/STARTED/COMPLETED/CANCELED
UPGRADE_QUOTED/STARTED/COMPLETED/CANCELED
REPAIR_STARTED/TICKED/STOPPED
DEMOLITION_STARTED/COMPLETED
TOKEN_SOURCE_ACTIVATED/BLOCKED/REMOVED
SPIN_PAID/SPIN_FREE/SPIN_STOPPED/SPIN_CONFIRMED
REEL_MOVE_PREVIEWED/EXECUTED
PENDING_REWARD_CREATED/STORED/SOLD/DEPLOYED
FOOD_RESERVED/RELEASED/DEPLOY_BLOCKED
CLASH_CAPTURED/LOST
STAGE_SETTLED
CHECKPOINT_COMMITTED
RUN_DEFEATED/RUN_CLEARED/RUN_ENDED
PERMANENT_CURRENCY_SETTLED
PAID_RETRY_OFFERED/DECLINED/PREPARED/COMMITTED/FAILED
SAVE_RECOVERED_FROM_BACKUP
```

각 경제 event는 transaction ID·idempotency key·before/after balance·reason을 가진다.

---

## 7. MapRun 지표

Stage `1, 5, 10, 15, 20` checkpoint에서 최소 다음 분포를 기록한다.

- gold `p01/p05/p10/p25/p50/p75/p90/p95/p99`.
- food cap·reserved·free capacity.
- free spin 잔액.
- 유료 회전 누적 횟수와 지불액.
- 세로·가로 이동 횟수와 지불액.
- 건물 가족별 수·Tier·투자액.
- TokenSource 수·활성/BLOCKED 상태.
- stored reward 수·overflow/block 횟수.
- 판매 횟수·수입·source/grade 분포.
- 라인별 배치 병력·HP·식량.
- 접전지 소유 시간·수입.
- 수리·철거·취소 비용과 환불.
- 합법 행동이 하나도 없는 상태 수.
- 패배·승리·Stage 도달률.

전체 평균만 보고하지 않는다. 꼬리 분포와 policy별 결과를 함께 제공한다.

---

## 8. 경제 불변 조건

다음은 허용 오차 없이 `0`이어야 한다.

```text
NEGATIVE_GOLD_WITHOUT_EXPLICIT_DEBT_RULE
NEGATIVE_FOOD_RESERVED
FOOD_RESERVED_ABOVE_CAP_CAUSING_EXISTING_UNIT_DELETION
DUPLICATE_SPIN_REWARD
DUPLICATE_SELL_PROCEEDS
DUPLICATE_REFUND
REFUND_ABOVE_ACTUAL_PAID
ENEMY_DESTRUCTION_REFUND
MOVE_EXECUTED_WITHOUT_COST_OR_ITEM
MOVE_UNDO_AFTER_EXECUTION
DEPLOYED_REWARD_STILL_STORED_OR_SELLABLE
SAME_REWARD_DEPLOYED_TWICE
TOKEN_SOURCE_DUPLICATE_SUPPLY
FREE_SPIN_GOLD_CALCULATED_FROM_ZERO_REFERENCE
CURRENT_RUN_PENDING_META_USED_FOR_RETRY
PAID_RETRY_MORE_THAN_ONCE
STAGE_1_TO_4_PAID_RETRY
RETRY_CHANGED_SEED_OR_MANIFEST
PROFILE_DOUBLE_CHARGE
FREE_RESTORE_AFTER_FAILED_CHARGE
```

발생 시 Candidate는 즉시 `REJECTED_INVARIANT_FAILURE`다.

---

## 9. 구조적 비교 지표

정확한 통과 band는 첫 결과 보고 후 확정하지만, 다음 방향을 만족해야 한다.

### 9.1 선택 가능성

- 정상 policy가 반복적으로 `건물만`, `회전만`, `판매만`으로 수렴하지 않는다.
- 최소 둘 이상의 유효한 대응 경로가 주요 공세 구간에 존재한다.
- 한 행동을 쓰지 않으면 자동 패배하는 hidden tax를 만들지 않는다.

### 9.2 복구 가능성

- Stage 초반의 합법적 한 번의 실수가 남은 런 전체를 결정적으로 봉쇄하지 않는다.
- 접전지 선취가 통제 불가능한 골드 복리를 만들지 않는다.
- cap 감소가 새 배치를 제한하더라도 기존 병력을 삭제하지 않는다.

### 9.3 RNG와 통제

- 릴 집중 policy가 구조 투자 없이 항상 우월하지 않는다.
- 건물 집중 policy가 회전·이동을 무의미하게 만들지 않는다.
- 이동권은 결과 가능성을 바꾸지만 확정 승리를 구매하는 도구가 아니다.

### 9.4 보관·판매

- 보관 용량은 무작위 결과를 무제한 연기하지 못한다.
- 판매는 실패 완충 장치지만 지속 차익거래가 아니다.
- 판매 집중 policy가 다른 policy를 위험·보상 양쪽에서 지배하지 않는다.

---

## 10. Retry·메타 지표

- Stage Tier별 Retry offer 수·선택률·성공률·재실패율.
- Retry 전후 clear probability 변화.
- 프로필 잔액 `p05/p50/p95`.
- 첫 Retry 가능까지 필요한 정산 런 수.
- Retry 구매 뒤 다른 메타 소비까지의 지연.
- 영구재화가 0인 상태의 후반 패배 비율.
- Retry가 가능하지만 거절한 비율과 이후 행동.
- Retry 사용이 사실상 자동 선택되는 profile 비율.
- 비용이 잔액을 초과해 항상 비활성인 profile 비율.
- 반복 clear·실패 정산이 영구재화를 무한 팽창시키는지.

### 비용 후보 판정

후보는 다음 세 결과 중 하나로 분류한다.

```text
TOO_CHEAP
- 대부분의 자격 profile이 고민 없이 사용
- 다른 메타 소비를 사실상 제거
- 패배가 추가 생명으로 변함

TOO_EXPENSIVE
- 자격 Stage에서도 실제 사용 가능 profile이 희소
- 후반 피로 완화 역할을 수행하지 못함

DECISION_RELEVANT
- 잔액·런 진행·다른 메타 목표에 따라 사용/거절이 모두 발생
- 같은 문제 재도전의 가치가 Stage Tier와 함께 증가
```

최종 통과 band는 사람 플레이와 첫 100K 결과를 근거로 별도 exact-value Decision에서 확정한다.

---

## 11. Save·Retry fault 지표

허용 오차 0:

- 유효 checkpoint 없이 비용 차감.
- 차감 후 복원 실패로 영구재화 손실.
- journal replay 이중 차감.
- journal replay 무료 복원.
- current와 backup 동시 덮어쓰기.
- checksum 실패 파일을 정상 load.
- future schema를 추정 load.
- migration 실패 뒤 원본 변경.
- Retry 뒤 seed·공세·미션·룰렛 lineage 변경.
- `retry_used` rollback으로 두 번째 제품 Retry 가능.

각 fault test는 before state hash·journal·current/backup hash·recovery receipt를 보존한다.

---

## 12. 통계·재현성

- 고정된 seed list를 저장소 artifact로 보존한다.
- Candidate와 policy는 같은 seed list를 사용한다.
- config·code·manifest·registry hash를 결과에 기록한다.
- 핵심 비율은 95% confidence interval을 제공한다.
- 평균 차이뿐 아니라 분포와 effect size를 제공한다.
- 실패 seed를 최소 재현 입력으로 축소한다.
- 실행 순서·병렬화가 결과를 바꾸지 않아야 한다.

---

## 13. 산출물

```text
artifacts/simulation/economy/<run_id>/
  manifest.json
  candidate_configs/
  seed_set.json
  summary.json
  stage_distributions.csv
  policy_comparison.csv
  retry_meta_trajectories.csv
  invariant_failures.jsonl
  fault_injection_results.json
  rejected_candidates.json
  reproducibility_report.md
```

저장소에 모든 원시 100K event log를 영구 commit하지 않는다. 압축 artifact·요약·실패 재현 seed·hash를 보존한다.

---

## 14. Gate 판정

```text
SIMULATOR_COMPILES
+ SAME_INPUT_SAME_HASH
+ INVARIANT_FAILURES_ZERO
+ FAULT_INJECTION_FAILURES_ZERO
+ ALL_POLICIES_REPORTED
+ TAIL_DISTRIBUTIONS_REPORTED
+ RETRY_META_TRAJECTORIES_REPORTED
+ HUMAN_PLAYTEST_CANDIDATES_SELECTED
= READY_FOR_EXACT_VALUE_REVIEW
```

다음은 통과가 아니다.

- 100K 실행 횟수만 채움.
- 평균 골드만 보고.
- 정상 정책 하나만 실행.
- 실패 seed를 삭제.
- Legacy Candidate H0가 익숙하다는 이유로 자동 채택.
- Runtime·사람 플레이 없이 exact 값을 `PROVEN`으로 승격.

---

## 15. 현재 상태

```text
SIMULATION_CONTRACT: CURRENT
SIMULATOR: NOT_CREATED
SEED_SET: NOT_CREATED
CANDIDATE_CONFIGS: NOT_CREATED
100K_RUN: NOT_RUN
FAULT_INJECTION: NOT_RUN
EXACT_VALUES: NOT_APPROVED
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
```
