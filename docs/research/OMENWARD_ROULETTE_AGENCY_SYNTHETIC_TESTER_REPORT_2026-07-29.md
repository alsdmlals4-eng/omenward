# OMENWARD 룰렛 통제감 합성 테스터 보고서

```yaml
simulation_id: OMENWARD-SYNTH-001
validation_method: SYNTHETIC_TESTER_SIMULATION
evidence_tier: T6_AI_INFERENCE
baseline_commit: 5404fdc61c973696b6334d9726602e646f8749ac
base_governance_commit: 9c4071c5ecefe28769b512d426442338ceb7acdd
structure_analysis: docs/research/OMENWARD_SYNTHETIC_TESTER_STRUCTURE_ANALYSIS_2026-07-29.md
result_state: SYNTHETIC_RISK_REVIEW
human_validation: NOT_RUN
vertical_slice_implementation: NOT_STARTED
implementation_authority: NONE
assumption_not_observation: true
```

## 1. 결정 질문

> 같은 릴 구조에서 결과가 좋거나 나빠도 플레이어가 자신이 통제한 구조·출처·커밋과 잔여 무작위성을 분리하고 다음 구조 수정안을 설명할 수 있는가?

실제 RNG 체감·조작감·재미·전투 가독성은 판정하지 않는다.

## 2. 페르소나별 가정

### ROGUELIKE_NOVICE

```yaml
assumed_first_attempt:
  - TokenSource를 확률에 영향을 주는 출처가 아니라 특정 토큰을 보장하는 상자로 해석
  - unfavorable 결과가 나오면 구조 설명과 결과가 모순됐다고 판단
reasoning_basis: source라는 명칭과 카드형 표시가 결과 보장을 연상시킬 수 있음
confidence: HIGH
counterexample: 분포·가능 결과를 시각적으로 먼저 보여주면 보장 해석이 감소함
adversarial_question: 출처가 가능성을 만든다는 점이 보이는가?
assumption_not_observation: true
```

### BUILDCRAFT_EXPERT

```yaml
assumed_first_attempt:
  - 결과 카드의 총 유용 토큰 수와 역할 적합도를 먼저 계산
  - favorable/unfavorable 조건이 동일 구조의 귀인 실험이 아니라 단순 결과 품질 비교라고 판단
reasoning_basis: 두 결과가 utility와 role alignment를 동시에 바꿈
confidence: HIGH
counterexample: 동일 총 utility를 유지하고 위치·출처 적합도만 바꾸면 구조 귀인을 더 잘 분리할 수 있음
adversarial_question: 통제감인가, 좋은 보상 만족도인가?
assumption_not_observation: true
```

### RESULTS_BIASED

```yaml
assumed_first_attempt:
  - favorable 결과에서는 자신의 이동·배치 덕분이라고 설명
  - unfavorable 결과에서는 정지 index가 나빴다고 설명하며 구조 책임을 축소
reasoning_basis: 결과 편향과 사후 귀인
confidence: HIGH
counterexample: 결과 공개 전에 예상 범위와 실패 가능성을 기록하면 사후 귀인이 줄어듦
adversarial_question: 결과 전에도 같은 인과를 설명했는가?
assumption_not_observation: true
```

### RNG_SKEPTIC

```yaml
assumed_first_attempt:
  - 모든 scripted 결과를 진행자 조작으로 보고 구조 설계 의미를 인정하지 않음
  - 다음 수정도 확률을 높이는 방향보다 결과 재굴림 요구로 귀결
reasoning_basis: 실제 분포·spin·반복 결과가 없는 카드 세션의 한계
confidence: HIGH
counterexample: 카드 세션 목적을 attribution comprehension으로 제한하면 실제 RNG 신뢰 문제와 분리 가능
adversarial_question: 이 세션은 룰렛 신뢰를 검증하는가, 인과 문법만 검증하는가?
assumption_not_observation: true
```

### COMMIT_AVERSE

```yaml
assumed_first_attempt:
  - 룰렛 이해보다 비가역 가로 이동과 전선 커밋의 후회 비용에 집중
  - 안전한 중앙 선택 또는 변경하지 않기를 선호
reasoning_basis: 한 세션에 두 종류의 비가역 결정이 연속됨
confidence: HIGH
counterexample: 첫 시나리오에서는 이동 또는 커밋 중 하나만 비가역로 두면 인과 학습을 분리할 수 있음
adversarial_question: 통제감을 측정하는가, 후회 회피를 측정하는가?
assumption_not_observation: true
```

### OPTIMIZER

```yaml
assumed_first_attempt:
  - 가장 높은 보상 전선 하나에 Token을 몰아주는 전략을 선택
  - 포기 비용을 명시적으로 최소화하기보다 성공 확률 집중을 지배 전략으로 사용
reasoning_basis: 다전선 분산의 보상·패널티 계약이 카드 수준에서 충분히 고정되지 않음
confidence: MEDIUM
counterexample: 전선별 실패 연쇄와 상한이 명확하면 분산 전략이 합리적일 수 있음
adversarial_question: 전선 선택이 전략인가, 몰빵 기대값 문제인가?
assumption_not_observation: true
```

## 3. Finding

| ID | 상태 | 내용 | 최소 조치 |
|---|---|---|---|
| `OM-SYN-F01` | `MUST_FIX_BEFORE_TEST` | favorable/unfavorable 카드가 총 utility·역할 적합도·위치를 함께 바꿔 attribution 변수를 혼합 | matched-utility 결과 쌍 추가 |
| `OM-SYN-F02` | `SHOULD_ADAPT` | 결과 공개 전 예상 범위를 기록하지 않아 사후 합리화 분리 불가 | pre-result prediction과 구조 영향 설명 선기록 |
| `OM-SYN-F03` | `MUST_FIX_BEFORE_TEST` | 비가역 가로 이동과 비가역 전선 커밋이 같은 초반 시나리오에 겹쳐 학습 부담 혼합 | 첫 시나리오에서 한 비가역 결정만 사용 |
| `OM-SYN-F04` | `SHOULD_ADAPT` | TokenSource가 보장 출처로 오해될 수 있음 | 가능 토큰·가중 범위·비보장 표기 후보 추가 |
| `OM-SYN-F05` | `TEST_REQUIRED` | 실제 RNG 분포·반복 spin에서 통제감이 유지되는지 카드로 판정 불가 | Vertical Slice runtime에서 반복 결과 필요 |
| `OM-SYN-F06` | `TEST_REQUIRED` | 전선 몰빵이 지배 전략인지 실제 보상·실패 연쇄 수치 필요 | 전선 utility 민감도 분석 |
| `OM-SYN-F07` | `COUNTEREXAMPLE` | 잔여 RNG를 너무 강조하면 구조 설계가 무의미하게 느껴질 수 있음 | 통제 가능한 범위와 비통제 범위를 동시에 표시 |

## 4. 권장 수정

1. **matched-utility 결과 쌍**: 유리/불리 대신 총 utility는 같고 출처·위치 적합도만 다른 결과를 추가한다.
2. **pre-result 기록**: 결과 공개 전 “내 구조가 영향을 주는 부분 / 주지 못하는 부분 / 예상 범위”를 기록한다.
3. **비가역 결정 단계화**: 시나리오 1은 구조 변경만, 시나리오 2부터 전선 커밋을 추가한다.
4. **TokenSource 비보장 표기**: source가 guarantee가 아님을 분포 문법으로 표현한다.
5. **카드 세션 주장 축소**: 실제 RNG 신뢰·재미·밸런스가 아니라 인과 언어와 책임 구분만 본다.
6. **몰빵 TEST**: 전선별 가치·실패 연쇄·상한이 고정된 뒤 수치 분석으로 분리한다.

## 5. 적대적 검토

```yaml
strongest_case_for_current_direction: 구조 변경과 출처·커밋을 결과 복기에 연결하는 흐름은 룰렛을 순수 운보다 설계 결과로 설명할 가능성이 있음
strongest_case_against_current_direction: fixed outcome 품질과 비가역 후회가 통제감보다 결과 만족도·손실 회피를 측정할 수 있음
hidden_assumption: 같은 총 utility에서도 위치·출처 관계를 플레이어가 의미 있게 구분한다는 가정
dominant_strategy_risk: 단일 전선 몰빵
facilitator_or_copy_bias: favorable/unfavorable 명칭 자체가 결과 평가를 유도
fidelity_confound: 실제 RNG 없이 scripted 카드만 사용
canon_conflict_check: NO_CONFLICT
product_path_intrusion_check: NONE
verdict: ADAPT
```

## 6. 판정

```yaml
decision: ADAPT
reason: 룰렛 인과 문법 방향은 유지하지만 결과 utility 혼합·사후 귀인·비가역 결정 중첩을 먼저 교정해야 함
human_validation: NOT_RUN
actual_rng_feel: NOT_RUN
actual_fun: NOT_RUN
vertical_slice_runtime: NOT_STARTED
implementation_authority: NONE
canon_changed: false
next_gate: REVISE_CARD_STIMULI_THEN_VALIDATE_IN_VERTICAL_SLICE_WHEN_IMPLEMENTED
```

`discipline.omenward-core-ux`의 실제 사람 결과 상태는 변경하지 않는다.
