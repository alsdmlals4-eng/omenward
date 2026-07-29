# OMENWARD 룰렛 통제감 사람 검증 Artifact 실행 계획 — 합성 위험 교정판

```yaml
session_packet_id: OMENWARD-HV-001
project: OMENWARD
baseline_branch: main
baseline_commit: f3ef315e8cd4493ebc6a2e6513dcec222510ee5a
base_governance_commit: 9c4071c5ecefe28769b512d426442338ceb7acdd
base_governance_path: docs/knowledge/game-development/HUMAN_VALIDATION_ARTIFACT_GOVERNANCE.md
base_synthetic_governance_path: docs/knowledge/game-development/SYNTHETIC_TESTER_SIMULATION_GOVERNANCE.md
synthetic_review_source: docs/research/OMENWARD_ROULETTE_AGENCY_SYNTHETIC_TESTER_REPORT_2026-07-29.md
artifact_status: READY_AFTER_SYNTHETIC_REMEDIATION
human_validation: NOT_RUN
vertical_slice_implementation: NOT_STARTED
implementation_authority: NONE
```

> 이 문서는 전체 Vertical Slice 내부 룰렛 UX의 저충실도 방향을 검증한다. 별도 Core PoC, Godot 코드, Scene, Resource, 최종 병종·밸런스를 만들지 않는다.

## 1. 결정 질문

> 결과의 총 연구 utility가 같아도 플레이어가 자신이 통제한 릴 구조·TokenSource·위치 적합도와 잔여 무작위성을 분리하고, 결과 공개 전 예상과 공개 후 귀인의 차이를 설명하는가?

## 2. Artifact fidelity와 주장 상한

```yaml
artifact_fidelity: CARD
simulated_components:
  - RESEARCH_ONLY_ROLE_TOKEN
  - 카드로 표현한 TokenSource·릴 구조
  - RESEARCH_MATCHED_UTILITY 결과 쌍
scripted_components:
  - 전투 인과 카드
fixed_outcomes:
  - 동일 token multiset·동일 source multiset의 MATCHED_PAIR_LEFT
  - 동일 token multiset·동일 source multiset의 MATCHED_PAIR_RIGHT
claim_ceiling:
  can_claim:
    - 구조 변경과 잔여 RNG를 개념적으로 구분하는지
    - TokenSource가 결과 보장이 아니라 가능성 출처임을 이해하는지
    - 결과 전 예상과 결과 후 귀인이 달라지는지
    - 비가역 이동·커밋의 장점과 포기 비용을 단계별로 설명하는지
  cannot_claim:
    - 실제 RNG 분포·확률·밸런스
    - 실제 룰렛 조작감·애니메이션·정보 위계 통과
    - Godot Vertical Slice 구현·성능·접근성 통과
    - 최종 병종·건물·전선 수치
    - 카드의 RESEARCH_MATCHED_UTILITY가 제품 밸런스 수치라는 주장
```

`MATCHED_PAIR_LEFT/RIGHT`는 좋음·나쁨 결과가 아니다. 같은 token·source 구성에서 위치·배치 관계만 달라지도록 만든 연구 카드이며 실제 전투 가치 동일성을 증명하지 않는다.

## 3. 보호 계약

- 최신 권한: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`.
- 목표: `FULL_SYSTEM_VERTICAL_SLICE / MINIMUM_CONTENT_BREADTH`.
- 별도 Core PoC를 재도입하지 않는다.
- 가로 이동은 TokenInstance와 출처를 함께 이동시키고 사용 즉시 확정한다.
- 정지 결과는 immutable SpinSnapshot 관점으로 취급한다.
- 배치 뒤 라인 변경·회수·판매를 허용하지 않는다.
- 정확 정지 index는 사전에 공개하지 않는다.
- `DEFENDER / CONTROL / BREAKER`는 `RESEARCH_ONLY_ROLE_TOKEN`이다.
- `RESEARCH_MATCHED_UTILITY`는 제품 수치가 아니라 변수 분리를 위한 카드 표식이다.

## 4. TokenSource 카드 문법

모든 TokenSource 카드는 아래 문장을 포함한다.

```text
이 출처는 릴에 들어갈 수 있는 후보와 상대적 비중에 영향을 줍니다.
특정 토큰이나 정지 위치를 보장하지 않습니다.
정확한 정지 결과는 회전 전 알 수 없습니다.
```

카드에는 다음을 분리 표시한다.

```yaml
token_source_card:
  possible_token_categories: VISIBLE
  relative_weight_language: QUALITATIVE_RESEARCH_ONLY
  guaranteed_result: NONE
  exact_stop_index: HIDDEN
  product_probability: NOT_DEFINED
```

## 5. 세션 패킷과 단계형 비가역 결정

1. 공세 브리핑.
2. 세 릴과 TokenSource 출처.
3. 현재 시나리오에서 허용된 구조 행동 수행.
4. 결과 전 기록: 통제 요소·비통제 요소·예상 가능한 결과 범위.
5. 배정된 matched pair 결과 공개.
6. 출처와 위치 적합도 추적.
7. 현재 시나리오에서 허용된 경우에만 전선 커밋.
8. 장점과 포기 비용이 있는 전투 인과 카드.
9. 관찰·진행자 개입 기록.

```yaml
irreversible_learning_sequence:
  scenario_1: STRUCTURE_CHANGE_ONLY
  scenario_2: PERMANENT_HORIZONTAL_MOVE_ADDED
  scenario_3: FRONTLINE_COMMIT_ADDED
```

한 시나리오에서 처음 배우는 비가역 결정을 두 개 이상 추가하지 않는다.

## 6. matched-utility 시나리오

공개된 `token_multiset`, `source_multiset`, `research_utility_total`은 쌍 안에서 동일하다. 위치·릴 index·전선 적합 관계만 다르다.

### 1 — 단일 위협과 구조 변화만

```yaml
scenario_id: OW-AGENCY-1
threat: "상단 강한 단일 돌파 — DEFENDER 필요"
allowed_action: "BARRACKS-A의 공급 위치를 릴별로 설정"
irreversible_action: NONE
common_contract:
  token_multiset: [DEFENDER, CONTROL, GOLD]
  source_multiset: [BARRACKS-A, BASELINE, VAULT-A]
  research_utility_total: MATCHED_NOT_PRODUCT_BALANCE
pair_left: [DEFENDER@BARRACKS-A, CONTROL@BASELINE, GOLD@VAULT-A]
pair_right: [GOLD@VAULT-A, DEFENDER@BARRACKS-A, CONTROL@BASELINE]
```

이 단계에서는 전선 커밋을 요구하지 않는다. 구조가 어떤 결과 범위를 만들었다고 예상했는지만 비교한다.

### 2 — 두 전선과 영구 가로 이동

```yaml
scenario_id: OW-AGENCY-2
threats:
  top: "다수 진격 — CONTROL"
  middle: "중장갑 핵심 — BREAKER"
allowed_action: "CONTROL과 BREAKER TokenInstance를 한 번 교환"
irreversible_action: PERMANENT_HORIZONTAL_MOVE
frontline_commit: NOT_USED_IN_THIS_SCENARIO
common_contract:
  token_multiset: [CONTROL, BREAKER, GOLD]
  source_multiset: [BARRACKS-A, BARRACKS-B, VAULT-A]
  research_utility_total: MATCHED_NOT_PRODUCT_BALANCE
pair_left: [CONTROL@BARRACKS-A, BREAKER@BARRACKS-B, GOLD@VAULT-A]
pair_right: [GOLD@VAULT-A, CONTROL@BARRACKS-A, BREAKER@BARRACKS-B]
```

이 단계는 영구 이동의 장점·포기 비용만 본다. 전선 커밋 판단은 시나리오 3으로 미룬다.

### 3 — 세 전선과 비가역 커밋

```yaml
scenario_id: OW-AGENCY-3
prior_history: ["BREAKER 비중 유지", "상단 CONTROL 부족 기록"]
threats: {top: CONTROL, middle: DEFENDER, bottom: BREAKER}
allowed_action: "SpinSnapshot 결과를 확인한 뒤 한 전선 선택"
irreversible_action: FRONTLINE_COMMIT
common_contract:
  token_multiset: [CONTROL, DEFENDER, BREAKER]
  source_multiset: [BARRACKS-A, BARRACKS-A, BARRACKS-B]
  research_utility_total: MATCHED_NOT_PRODUCT_BALANCE
pair_left: [CONTROL@BARRACKS-A, DEFENDER@BARRACKS-A, BREAKER@BARRACKS-B]
pair_right: [BREAKER@BARRACKS-B, CONTROL@BARRACKS-A, DEFENDER@BARRACKS-A]
commit_options: [top, middle, bottom]
commit_rule: "한 전선에만 비가역 커밋"
```

모든 결과에는 지킨 것과 포기한 것을 함께 표시한다. pair 명칭에는 `FAVORABLE`, `UNFAVORABLE`, `GOOD`, `BAD`를 사용하지 않는다.

## 7. 결과 교차 배정

```yaml
assignment:
  participant_1_3: [PAIR_LEFT, PAIR_RIGHT, PAIR_LEFT]
  participant_4_6: [PAIR_RIGHT, PAIR_LEFT, PAIR_RIGHT]
```

쌍의 token·source 구성은 같으므로 결과 만족도보다 위치·출처·커밋 귀인 언어의 차이를 본다.

## 8. 진행자 스크립트

> 슬롯 운이 좋았는지를 평가하는 테스트가 아닙니다. 결과를 보기 전에 내 구조가 영향을 주는 부분, 주지 못하는 부분, 나올 수 있다고 예상한 범위를 적어 주세요. 결과가 나온 뒤에는 출처·위치·커밋 중 무엇이 영향을 줬는지 설명해 주세요.

1. 공세·릴·TokenSource 카드 공개.
2. 참가자가 해당 시나리오의 구조 행동을 수행.
3. 결과 공개 전 아래를 기록한다.
   - `pre_result_controlled_elements`
   - `pre_result_uncontrolled_elements`
   - `pre_result_expected_range`
   - `pre_result_failure_possibility`
4. 배정된 `PAIR_LEFT/PAIR_RIGHT` 결과를 공개한다.
5. 공개 시점·문구를 `facilitator_intervention`에 기록한다.
6. 출처와 위치 적합도를 추적한다.
7. 시나리오 3에서만 전선 커밋을 수행한다.
8. 장점·포기 비용 카드를 공개한다.
9. `post_result_attribution`, `prediction_delta`, `next_structure_change`를 기록한다.
10. 행동 기록 뒤 자기보고.

진행자는 가장 좋은 전선이나 구조를 추천하지 않으며 pair를 좋음·나쁨으로 평가하지 않는다.

## 9. 참가자와 기록

```yaml
pilot_purpose: DIRECTIONAL_FINDING_AND_ATTRIBUTION_DEFECT_DISCOVERY
minimum_participants: 6
segments:
  low_strategy_experience: 3
  deckbuilding_or_autobattle_experienced: 3
scenario_order:
  group_1: [1, 2, 3]
  group_2: [3, 2, 1]
result_variant: COUNTERBALANCED_MATCHED_PAIR
session_minutes: 30-40
```

기록 필드:

- 참가자·경험군·시나리오·pair.
- 최초 구조 변화와 irreversible 단계.
- `pre_result_controlled_elements`, `pre_result_uncontrolled_elements`.
- `pre_result_expected_range`, `pre_result_failure_possibility`.
- TokenSource를 보장으로 설명했는지.
- 결과 카드 공개에 대한 진행자 개입.
- `post_result_attribution`, 출처 추적, 위치 적합도.
- 시나리오 3의 커밋 이유와 포기 대안.
- `prediction_delta`, `next_structure_change`.
- undo/reroll 요청·시간·정보 누락 행동.
- 통제감·불공정감·과밀 자기보고.
- pair를 좋음·나쁨으로만 평가하거나 단일 전선 몰빵을 반복하는 critical incident.

## 10. 판정

비율은 `n/N` 참고값으로만 기록한다.

```yaml
PROMISING_DIRECTION:
  required_patterns:
    - "서로 다른 참가자 2명 이상이 결과 전 통제 요소와 잔여 RNG를 구분"
    - "matched pair가 달라도 출처·위치·비가역 결정의 영향을 설명"
    - "TokenSource를 특정 결과 보장으로 취급하지 않음"
    - "결과 뒤 수정안이 릴 구조·출처·역할 비중과 연결"
  claim: "Vertical Slice UX에서 구조·RNG·출처·커밋 인과를 계속 검증할 방향을 지지"
ADAPT:
  condition: "구조 인과는 읽히지만 출처·비가역성·예상 범위 중 한 층에서 반복 혼란"
REWORK:
  condition: "matched pair와 무관하게 릴을 계산표·보장 상자·순수 운으로만 읽음"
REJECT:
  condition: "결과 만족도만 말하고 구조 영향·잔여 RNG·포기 비용을 설명하지 못함"
STOP:
  condition: "정본 충돌, 별도 Core PoC 오인, 진행자 정답 전선 추천, pair utility를 제품 밸런스로 주장"
```

이 fidelity에서는 제품 UX `ADOPT`, 실제 RNG 검증, `LOOP_PROVEN`, `CORE_LOCK`을 선언하지 않는다.

## 11. 현재 상태

```yaml
synthetic_must_fix_applied:
  matched_utility_pairs_added: true
  pre_result_prediction_added: true
  irreversible_decisions_staged: true
  token_source_non_guarantee_copy_added: true
human_session_executed: false
product_code_changed: false
vertical_slice_implementation_started: false
separate_core_poc_created: false
canon_changed: false
true_rng_distribution: NOT_RUN
product_ui: NOT_RUN
accessibility: NOT_RUN
performance: NOT_RUN
human_validation: NOT_RUN
implementation_authority: NONE
next_gate: RUN_REVISED_MATCHED_PAIR_PILOT_THEN_VALIDATE_IN_VERTICAL_SLICE_WHEN_IMPLEMENTED
```
