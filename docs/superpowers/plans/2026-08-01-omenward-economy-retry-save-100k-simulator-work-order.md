# 오멘워드 경제·Retry·Save 100K 시뮬레이터 Work Order

- Work Order Decision ID: `OMW-DEC-20260801-ECONOMY-SIMULATOR-WORK-ORDER-V1`
- 상위 Decision ID: `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1`
- 작성일: `2026-08-01`
- 상태: `IMPLEMENTATION_PLAN_CURRENT / EXECUTION_NOT_AUTHORIZED / PLANNING_ONLY`
- Work Mode: `PLAN`
- 실행 주체: 후속 승인된 도구·테스트 package
- 제품 Godot 코드: `OUT_OF_SCOPE`
- Codex 실행: `BLOCKED_PENDING_SEPARATE_BUILD_APPROVAL`
- 정확 제품 수치 승인: `OUT_OF_SCOPE`

## 1. 목적

결정론적 독립 시뮬레이터를 만들어 다음을 증명한다.

1. Parameter Registry를 기계적으로 읽고 `null=미승인`, legacy H0=역사 비교 후보 경계를 지킨다.
2. H0/H1/H2 Candidate와 P0~P6 정책을 같은 seed 집합에서 비교한다.
3. 20 Stage MapRun 경제의 지배 전략·복구 불가 스노우볼·판매/환불 차익거래를 찾는다.
4. 여러 MapRun의 Profile 영구재화·Retry 기회비용을 비교한다.
5. save/checkpoint/Retry transaction 중단점에서 이중 차감·무료 복원·동시 손상을 찾는다.
6. 실패 seed·config hash·event log를 재현 가능한 artifact로 남긴다.

이 Work Order는 시뮬레이터와 테스트를 만들기 위한 계획이다. H1/H2의 숫자를 여기서 발명하거나 제품값으로 승인하지 않는다.

---

## 2. 선행 책임 원본

반드시 다음 순서로 읽는다.

1. `docs/PROJECT_CORE.md`
2. `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
3. `docs/design/APPROVED_OMENWARD_ECONOMY_RETRY_SAVE_CHECKPOINT_PLANNING_CONTRACT_2026-08-01.md`
4. `docs/design/OMENWARD_ECONOMY_RETRY_SAVE_PARAMETER_REGISTRY_V1.json`
5. `docs/testing/OMENWARD_ECONOMY_META_RETRY_100K_SIMULATION_CONTRACT_2026-08-01.md`
6. `docs/testing/OMENWARD_ECONOMY_RETRY_SAVE_RED_TEST_EXTENSION_2026-08-01.md`
7. `docs/testing/OMENWARD_ECONOMY_SIMULATION_CANDIDATE_CONFIG_SCHEMA_V1.json`
8. `docs/testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md`
9. `docs/testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md`
10. 실제 Legacy economy/roulette/building/retry tests와 code seam

---

## 3. 범위

### 포함

- Python 3.12 독립 결정론 시뮬레이터.
- Registry·Candidate·seed·policy schema와 validator.
- H0 역사 후보 생성기.
- 값 없는 H1/H2 template 생성기.
- 고정 seed set 생성기와 hash.
- P0~P6 정책 모델.
- MapRun 경제·Profile trajectory 모델.
- transaction/save fault-injection model.
- pytest 또는 unittest 기반 Red/Green 테스트.
- artifact writer와 reproducibility report.
- CI에서 작은 smoke set과 수동/dispatch full 100K 분리.

### 제외

- Godot `scripts/`, `scenes/`, `data/`, `.tres`, `.tscn` 변경.
- 실제 제품 balance data 생성.
- H1/H2 정확 숫자 임의 입력.
- Retry 영구재화 이름 결정.
- 제품 save 파일 경로·암호화·플랫폼 cloud save 구현.
- 화면·이미지·UI 생성.
- Base Adapter migration.
- PR 병합.

---

## 4. 제안 파일 구조

```text
tools/economy_sim/
  __init__.py
  cli.py
  models.py
  parameter_registry.py
  candidate_config.py
  seed_set.py
  rng.py
  event_log.py
  policies/
    __init__.py
    base.py
    safety_first.py
    balanced.py
    building_investment.py
    reel_agency.py
    storage_delay.py
    sell_cashout.py
    random_legal.py
  simulation/
    __init__.py
    maprun.py
    profile_trajectory.py
    economy_transactions.py
    checkpoint.py
    retry.py
    fault_injection.py
  reports/
    __init__.py
    aggregate.py
    distributions.py
    reproducibility.py

configs/economy_sim/
  candidate_schema.json
  candidates/
    H0.generated.json
    H1.template.json
    H2.template.json
  policies.json
  smoke_seed_set.json
  full_seed_set.manifest.json

tests/python/economy_sim/
  test_parameter_registry_contract.py
  test_candidate_schema.py
  test_seed_set_determinism.py
  test_policy_legality.py
  test_transaction_invariants.py
  test_checkpoint_retry_faults.py
  test_reproducibility.py
  test_smoke_simulation.py

artifacts/simulation/economy/
  .gitkeep

docs/reports/economy-simulation/
  README.md
```

`artifacts/simulation/economy/<run_id>/`의 대용량 결과는 CI artifact 또는 외부 실행 artifact로 보관한다. 전체 원시 event log 100K를 Git에 commit하지 않는다.

---

## 5. 구현 패키지

### Package S0 — Repository·환경 preflight

**결과:** 시뮬레이터가 수정해도 되는 경계와 실행 환경이 확정된다.

입력:

- 현재 PR base/head.
- Python version·의존성 관리 방식.
- 기존 `tests/python`, workflow, artifact policy.

작업:

1. dirty/diverged 상태와 동일 Goal 작업을 확인한다.
2. Python 3.12 또는 저장소 현재 표준을 실제 workflow에서 확인한다.
3. 표준 라이브러리만으로 가능한지 먼저 판정한다.
4. 외부 패키지가 필요하면 최소 패키지·version·license·CI cost를 제안하고 승인 전 추가하지 않는다.
5. 제품 경로 보호 목록을 고정한다.

완료 기준:

```text
ENVIRONMENT_VERIFIED
+ PROTECTED_PRODUCT_PATHS_DEFINED
+ DUPLICATE_WORK_NONE
+ TOOL_PACKAGE_BOUNDARY_CONFIRMED
```

검증:

- 현재 Python tests discovery.
- workflow trigger·timeout·artifact 보존 정책.

롤백:

- 읽기 전용이므로 변경 없음.

---

### Package S1 — Registry·Candidate Red Gate

**결과:** 현재 Registry와 Candidate schema를 검사하는 테스트가 먼저 실패 또는 통과 이유를 명확히 보고한다.

먼저 작성할 테스트:

```text
RED-PARAM-001 JSON parse
RED-PARAM-002 unique parameter IDs
RED-PARAM-003 null cannot become product default
RED-PARAM-004 legacy H0 authority restricted
RED-PARAM-005 compatibility alias only
RED-PARAM-006 Retry tier constraints present
RED-PARAM-007 exact value promotion evidence required
```

작업:

1. `parameter_registry.py`를 쓰기 전에 위 테스트를 작성한다.
2. 현재 Registry raw bytes SHA-256을 계산한다.
3. ID 집합·alias·approved/null·legacy provenance를 읽는 최소 parser를 구현한다.
4. constraint 문자열을 전부 해석하는 범용 언어를 만들지 않는다. 현재 필요한 교차 관계만 명시적으로 검증한다.
5. Candidate JSON Schema를 정적 검증한다.

완료 기준:

```text
REGISTRY_PARSE_PASS
UNIQUE_IDS_PASS
NULL_POLICY_PASS
LEGACY_AUTHORITY_PASS
CANDIDATE_SCHEMA_PASS
```

금지:

- null에 임의 default 주입.
- H0를 CURRENT로 승격.
- 알 수 없는 Parameter ID 무시.

롤백:

- `tools/economy_sim/parameter_registry.py`, 관련 tests만 제거하면 원상 복구.

---

### Package S2 — Seed·RNG·Event 기반

**결과:** 입력·RNG·event log의 결정론적 기반이 고정된다.

테스트 우선:

- 같은 seed spec은 같은 seed list/hash.
- seed 순서·worker 수가 개별 run 결과를 바꾸지 않음.
- 같은 candidate/policy/seed는 같은 ordered event log와 final state hash.
- 다른 RNG version은 manifest에서 명시적으로 구분.

작업:

1. seed 생성 사양을 정의한다.
2. smoke seed set은 작고 Git에 저장 가능한 manifest로 만든다.
3. full 100K는 생성 규칙·첫/마지막 seed·count·hash만 Git에 보존한다.
4. RNG stream을 combat/economy/roulette/mission/retry로 분리한다.
5. 모든 event에 sequence·tick·transaction ID·before/after·reason을 기록한다.

완료 기준:

```text
SEED_MANIFEST_DETERMINISTIC
RNG_STREAMS_VERSIONED
EVENT_LOG_ORDER_STABLE
SAME_INPUT_SAME_HASH
```

---

### Package S3 — H0 생성·H1/H2 template

**결과:** 과거값은 자동 추출된 비교 후보로만 생성되고, H1/H2는 숫자 없는 가설 template으로 남는다.

H0:

- Registry의 `legacy_h0` 항목만 수집.
- 누락된 필수 Parameter는 `MISSING_H0_VALUE`로 명시.
- 누락값을 0이나 현재 Legacy runtime default로 자동 채우지 않는다.
- status=`SIMULATION_INPUT_ONLY`.

H1:

- role=`BALANCED_STRUCTURE_INVESTMENT`.
- 질문·tradeoff·rejection condition만 채운 template.
- values는 빈 객체.

H2:

- role=`FREQUENT_REEL_AND_REWARD_AGENCY`.
- 질문·tradeoff·rejection condition만 채운 template.
- values는 빈 객체.

테스트:

- H0 source가 전부 `HISTORICAL_ONLY/LEGACY_PROVEN_ONLY`인지.
- H1/H2 values가 승인 전 비어 있는지.
- config hash가 canonical serialization에서 안정적인지.
- Registry에 없는 ID가 Candidate에 있으면 실패하는지.

완료 기준:

```text
H0_GENERATED_WITH_GAPS_EXPLICIT
H1_TEMPLATE_NO_VALUES
H2_TEMPLATE_NO_VALUES
CONFIG_HASH_STABLE
NO_PRODUCT_PROMOTION
```

---

### Package S4 — Domain transaction model

**결과:** 실제 제품 코드와 독립된 최소 domain model이 경제 불변 조건을 재현한다.

모델:

```text
MapRunEconomyState
ProfileEconomyState
PhysicalReelState abstraction
PendingRewardState
BuildingProjectState
LineDeploymentState
StageState
RunCheckpointState
TransactionJournalState
```

테스트 우선:

- 중복 spin confirm·sale·deployment·refund 0.
- preview mutation 0.
- `n×P`와 shared session counter.
- stored food 0 / deployed food reserve.
- cap loss does not delete units.
- actual-paid floor refund.
- enemy destruction refund 0.
- pause/defeat income 0.

범위 절제:

- 실제 전투 damage/AI를 재구현하지 않는다.
- Stage outcome은 versioned stochastic/deterministic outcome interface를 사용한다.
- physical reel은 최신 계약의 상태·비용·reward 발생 경계만 모델링한다.

완료 기준:

```text
ECONOMY_INVARIANTS_GREEN
TRANSACTION_IDEMPOTENCY_GREEN
PRODUCT_CODE_IMPORTS_ZERO
```

---

### Package S5 — Policy P0~P6

**결과:** 모든 policy가 합법 행동만 선택하고 동일 상태에서 결정론적이다.

공통 interface:

```python
choose_action(state_snapshot, legal_actions, policy_context) -> ActionDecision
```

규칙:

- policy는 state를 직접 mutate하지 않는다.
- 선택 이유와 고려 candidate를 event에 기록한다.
- 합법 행동 0이면 명시적 `NO_LEGAL_ACTION`을 반환한다.
- policy마다 숨은 정보 접근 금지.

테스트:

- P0~P6가 illegal action을 반환하지 않음.
- P6 random legal은 지정 RNG stream만 사용.
- policy 순서나 worker 수가 결과를 바꾸지 않음.
- 특정 policy가 특정 Parameter를 하드코딩하지 않음.

완료 기준:

```text
ALL_POLICIES_LEGAL
ALL_POLICIES_DETERMINISTIC
NO_HIDDEN_INFORMATION
NO_STATE_MUTATION_IN_POLICY
```

---

### Package S6 — MapRun simulation

**결과:** smoke set에서 20 Stage 또는 조기 패배까지 재현 가능한 실행과 분포가 나온다.

작업:

1. Stage/Act 진행 interface를 구현한다.
2. 공개 공세·건설·릴·reward·전투 결과·정산 event를 연결한다.
3. Stage 1/5/10/15/20 checkpoint 지표를 수집한다.
4. 조기 패배와 clear를 모두 지원한다.
5. 무한 loop·행동 없는 상태에 watchdog과 진단을 둔다.

테스트:

- 작은 fixed seed set golden hash.
- 모든 불변 위반 0.
- 각 policy 결과가 존재.
- p01~p99 계산의 입력 count·missing 처리.
- 실패 seed 최소 재현 명령 생성.

완료 기준:

```text
SMOKE_MAPRUN_PASS
ALL_POLICIES_REPORTED
TAIL_DISTRIBUTIONS_REPORTED
FAILURE_REPRO_COMMAND_PRESENT
```

---

### Package S7 — Profile trajectory·paid Retry

**결과:** 여러 런의 정산 잔액·메타 소비·Retry 선택을 재현한다.

추가 policy:

```text
RETRY_NEVER
RETRY_WHEN_AFFORDABLE
RETRY_STAGE_VALUE_AWARE
RETRY_PRESERVE_FOR_META
```

테스트 우선:

- Stage 1~4 offer 0.
- MapRun당 최대 1회.
- T1/T2/T3 mapping.
- 미정산 현재 런 meta 제외.
- 같은 idempotency key 동일 receipt.
- Retry 뒤 seed/manifest/RNG lineage 유지.

지표:

- 첫 Retry 가능까지의 정산 런 수.
- offer/선택/거절/성공/재패배.
- balance p05/p50/p95.
- 다른 meta 소비와의 지연.
- TOO_CHEAP/TOO_EXPENSIVE/DECISION_RELEVANT 분류 입력.

완료 기준:

```text
PROFILE_TRAJECTORY_SMOKE_PASS
RETRY_INVARIANTS_GREEN
RETRY_METRICS_COMPLETE
```

---

### Package S8 — Save/checkpoint fault injection

**결과:** transaction type × 중단점 전체 조합이 복구 가능하다.

대상 transaction:

- SPIN_CONFIRM
- STORE/SELL/DEPLOY
- CONSTRUCTION/UPGRADE CANCEL
- REPAIR SETTLEMENT
- DEMOLITION COMPLETE
- STAGE SETTLEMENT
- PAID_RETRY
- PROFILE_UNLOCK

중단점:

```text
BEFORE_PREPARED
AFTER_PREPARED
AFTER_DOMAIN_APPLY
BEFORE_ATOMIC_REPLACE
AFTER_ATOMIC_REPLACE_BEFORE_RECEIPT
AFTER_COMMITTED
```

테스트 결과:

- 정확히 한 번 commit 또는 완전 rollback.
- current와 backup 동시 손상 0.
- charge-without-restore 0.
- free restore 0.
- future schema load 0.
- migration failure changes original 0.

완료 기준:

```text
ALL_TRANSACTION_FAULT_POINTS_COVERED
FAULT_FAILURES_ZERO
CURRENT_BACKUP_CONSISTENT
JOURNAL_RECOVERY_DETERMINISTIC
```

---

### Package S9 — Full 100K runner·artifact report

**결과:** Candidate별 100K MapRun과 100K Profile trajectory를 재현 가능한 artifact로 생성한다.

실행 정책:

- PR push마다 full 100K를 강제하지 않는다.
- PR CI: parser/unit/smoke seed set.
- 수동 workflow_dispatch 또는 승인된 scheduled run: full 100K.
- concurrency·timeout·artifact retention을 명시한다.
- worker별 partial을 deterministic reduce한다.

필수 출력:

```text
manifest.json
candidate configs + hashes
seed set manifest + hash
policy comparison
stage distributions
retry trajectories
invariant failures
fault injection results
reproducibility report
rejected candidate record
```

완료 기준:

```text
100K_MAPRUN_PER_CANDIDATE_COMPLETE
100K_PROFILE_TRAJECTORY_PER_CANDIDATE_COMPLETE
INVARIANT_FAILURES_ZERO
FAULT_FAILURES_ZERO
REPRODUCIBILITY_SECOND_RUN_MATCH
```

단, H1/H2 values가 승인되지 않은 상태에서는 full 실행을 `BLOCKED_MISSING_CANDIDATE_VALUES`로 정상 차단한다. 빈 template을 0값으로 실행하지 않는다.

---

### Package S10 — 결과 검수·exact-value handoff

**결과:** 수치 승격이 아니라 사람 검토용 후보와 실패 근거가 만들어진다.

산출:

- Candidate별 장점·실패·지배 전략.
- policy별 꼬리 분포.
- Retry 비용 판단 입력.
- 실패 seed 최소 재현.
- H0/H1/H2 `REJECT / REVISE / SHORTLIST`.
- 사람 플레이용 최대 2개 candidate 추천.

금지:

- 평균 승률 하나로 선택.
- simulator 결과만으로 exact values CURRENT 승격.
- 실패 candidate 삭제.
- H0 자동 채택.

후속 Gate:

```text
READY_FOR_EXACT_VALUE_REVIEW
→ 사용자 Approval Bundle
→ exact value Decision ID
→ Parameter Registry approved_value 갱신
→ Sheet 동기화
→ 최신 Red tests
→ 제품 구현 Plan
```

---

## 6. 의존성

```text
S0 BLOCKS S1
S1 BLOCKS S2,S3
S2 BLOCKS S4,S5
S3 USES_OUTPUT S1,S2
S4 BLOCKS S6,S7,S8
S5 BLOCKS S6,S7
S6 BLOCKS S9
S7 BLOCKS S9
S8 VALIDATES S9
S9 BLOCKS S10
```

병렬 가능:

- S3 H0/template 생성과 S5 policy interface 설계는 S1·S2 계약 후 병렬 가능.
- S7 Profile trajectory와 S8 fault harness는 S4 interface 고정 후 별도 파일 경계에서 병렬 가능.

병렬 금지:

- Registry parser와 Candidate schema 소비자가 동시에 서로 다른 ID 정책을 수정.
- transaction state schema를 S4/S8에서 경쟁적으로 수정.
- aggregate output schema를 S6/S7/S9가 독립 변경.

---

## 7. CI 계획

제안 workflow:

```text
.github/workflows/validate-omenward-economy-simulator.yml
```

PR fast path:

- compile.
- Registry/Candidate schema tests.
- unit tests.
- smoke seeds.
- fault-injection reduced matrix.
- timeout 상한.

Manual full path:

- 100K MapRun/candidate.
- 100K Profile trajectory/candidate.
- complete fault matrix.
- artifacts upload.
- deterministic rerun sample.

기존 `validate-omenward-core.yml`에 처음부터 대량 job을 합치지 않는다. 기존 CI 실패를 이 package의 실패로 숨기거나 반대로 무시하지 않는다.

---

## 8. 승인·실행 Gate

이 문서 작성 후 상태:

```text
WORK_ORDER: CURRENT
CANDIDATE_SCHEMA: CURRENT
REGISTRY_PARSER_TESTS: NOT_CREATED
SIMULATOR_CODE: NOT_CREATED
H0_CONFIG: NOT_GENERATED
H1_H2_VALUES: NOT_APPROVED
SEED_SET: NOT_CREATED
100K_RUN: NOT_RUN
FAULT_INJECTION: NOT_RUN
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
```

실행 승인 전 필요한 것:

```text
WORK_ORDER_USER_REVIEW: SATISFIED_BY_RECOMMENDED_DEFAULT_APPROVAL
PACKAGE_SCOPE_CONFIRMATION: REQUIRED_BEFORE_BUILD
BRANCH_AND_OWNER: REQUIRED
DEPENDENCY_POLICY: REQUIRED
EXPECTED_RED_REASON: REQUIRED
ROLLBACK_PATH: REQUIRED
```

별도 Build 승인 없이 이 계획을 실행하거나 H1/H2 수치를 채우지 않는다.

---

## 9. 최종 완료 기준

시뮬레이터 package 완료는 다음을 모두 요구한다.

```text
REGISTRY_AND_SCHEMA_TESTS_GREEN
SAME_INPUT_SAME_HASH
SMOKE_MAPRUN_GREEN
PROFILE_TRAJECTORY_GREEN
FAULT_INJECTION_FAILURES_ZERO
FULL_100K_ARTIFACTS_PRESENT_FOR_NONEMPTY_CANDIDATES
REPRODUCIBILITY_REPORT_PASS
PRODUCT_PATH_DIFF_ZERO
EXACT_VALUES_NOT_AUTO_PROMOTED
CI_EVIDENCE_LINKED
```

이 완료는 제품 경제·save·Retry 구현 완료가 아니다.