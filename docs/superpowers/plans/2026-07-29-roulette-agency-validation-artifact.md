# OMENWARD 룰렛 통제감 사람 검증 Artifact 실행 계획 — Governance 교정판

```yaml
session_packet_id: OMENWARD-HV-001
project: OMENWARD
baseline_branch: main
baseline_commit: 495bb3628f4cccb971c8875adc01cf947133f8b6
base_governance_commit: dd6ae48225da58088045733e8fdc3de5784bdeff
base_governance_path: docs/knowledge/game-development/HUMAN_VALIDATION_ARTIFACT_GOVERNANCE.md
base_template_path: templates/research/HUMAN_VALIDATION_SESSION_PACKET.md
artifact_status: READY_FOR_LOW_FIDELITY_HUMAN_SESSION
human_validation: NOT_RUN
implementation_authority: NONE
```

> 이 문서는 전체 Vertical Slice 내부 룰렛 UX의 저충실도 방향을 검증한다. 별도 Core PoC, Godot 코드, Scene, Resource, 최종 병종·밸런스를 만들지 않는다.

## 1. 결정 질문

> 같은 릴 구조에서 결과가 좋거나 나빠도 플레이어가 자신이 통제한 구조·출처·커밋과 잔여 무작위성을 분리하고 다음 구조 수정안을 설명하는가?

## 2. Artifact fidelity와 주장 상한

```yaml
artifact_fidelity: CARD
simulated_components:
  - RESEARCH_ONLY_ROLE_TOKEN
  - 카드로 표현한 TokenSource·릴 구조
scripted_components:
  - 전투 인과 카드
fixed_outcomes:
  - 같은 구조의 FAVORABLE 결과
  - 같은 구조의 UNFAVORABLE_OR_MIXED 결과
claim_ceiling:
  can_claim:
    - 구조 변경과 잔여 RNG를 개념적으로 구분하는지
    - TokenSource 출처를 추적하는지
    - 비가역 커밋의 장점·포기 비용을 설명하는지
    - 좋은 결과와 나쁜 결과에서 귀인이 달라지는지
  cannot_claim:
    - 실제 RNG 분포·확률·밸런스
    - 실제 룰렛 조작감·애니메이션·정보 위계 통과
    - Godot Vertical Slice 구현·성능·접근성 통과
    - 최종 병종·건물·전선 수치
```

고정 결과 카드 하나로 통제감을 증명하지 않는다.

## 3. 보호 계약

- 최신 권한: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`.
- 목표: `FULL_SYSTEM_VERTICAL_SLICE / MINIMUM_CONTENT_BREADTH`.
- 별도 Core PoC를 재도입하지 않는다.
- 가로 이동은 TokenInstance와 출처를 함께 이동시키고 사용 즉시 확정한다.
- 정지 결과는 immutable SpinSnapshot 관점으로 취급한다.
- 배치 뒤 라인 변경·회수·판매를 허용하지 않는다.
- 정확 정지 index는 사전에 공개하지 않는다.
- `DEFENDER / CONTROL / BREAKER`는 `RESEARCH_ONLY_ROLE_TOKEN`이다.

## 4. 세션 패킷과 결과 교차 배정

1. 공세 브리핑.
2. 세 릴과 TokenSource 출처.
3. 구조 변경 또는 영구 가로 이동.
4. 회전 전 요약: 통제·확정·잔여 RNG·비가역 결정.
5. 동일 구조의 결과 A/B.
6. 전선 커밋.
7. 장점과 포기 비용이 있는 전투 인과.
8. 관찰·진행자 개입 기록.

```yaml
variant_A: FAVORABLE
variant_B: UNFAVORABLE_OR_MIXED
assignment:
  participant_1_3: [A, B, A]
  participant_4_6: [B, A, B]
```

좋은 결과에서만 설계 덕분이라고 하고 나쁜 결과를 순수 운으로 처리하는지 본다.

## 5. 시나리오

### 1 — 단일 위협과 TokenSource 변화

```yaml
scenario_id: OW-AGENCY-1
threat: "상단 강한 단일 돌파 — DEFENDER 필요"
player_change: "BARRACKS-A가 각 릴 지정 위치에 DEFENDER 공급"
variant_A: [DEFENDER@BARRACKS-A, DEFENDER@BARRACKS-A, DEFENDER@BARRACKS-A]
variant_B: [GOLD@VAULT-A, DEFENDER@BARRACKS-A, BREAKER@BASELINE]
```

### 2 — 두 전선과 영구 가로 이동

```yaml
scenario_id: OW-AGENCY-2
threats:
  top: "다수 진격 — CONTROL"
  middle: "중장갑 핵심 — BREAKER"
move: "CONTROL과 BREAKER를 한 번 교환, undo 없음"
variant_A: [CONTROL@BARRACKS-A, BREAKER@BARRACKS-B, CONTROL@BARRACKS-A]
variant_B: [GOLD@VAULT-A, CONTROL@BARRACKS-A, BREAKER@BARRACKS-B]
commit_options: [top, middle]
```

### 3 — 세 전선과 이전 구조 회수

```yaml
scenario_id: OW-AGENCY-3
prior_history: ["BREAKER 비중 유지", "상단 CONTROL 부족 기록"]
threats: {top: CONTROL, middle: DEFENDER, bottom: BREAKER}
variant_A: [CONTROL@BARRACKS-A, DEFENDER@BARRACKS-A, BREAKER@BARRACKS-B]
variant_B: [GOLD@VAULT-A, DEFENDER@BARRACKS-A, BREAKER@BARRACKS-B]
commit_rule: "한 전선에만 비가역 커밋"
```

모든 결과에는 지킨 것과 포기한 것을 함께 표시한다.

## 6. 진행자 스크립트

> 슬롯 운이 좋았는지를 평가하는 테스트가 아닙니다. 어떤 구조를 바꿨고 무엇이 아직 무작위인지, 나온 결과를 어느 전선에 왜 배치했는지 설명해 주세요.

1. 공세·릴·출처 공개.
2. 참가자가 구조 변경 수행.
3. `first_attempt`로 통제·확정·잔여 RNG·비가역 결정을 작성.
4. 배정된 A/B 결과 공개.
5. 공개 시점·문구를 `facilitator_intervention`에 기록.
6. 출처 추적 후 전선 커밋.
7. 장점·포기 비용 카드 공개.
8. `post_feedback_attempt`로 결과 귀인과 다음 구조 수정 기록.
9. 행동 기록 뒤 자기보고.

진행자는 가장 좋은 전선이나 구조를 추천하지 않는다.

## 7. 참가자와 기록

```yaml
pilot_purpose: DIRECTIONAL_FINDING_AND_ATTRIBUTION_DEFECT_DISCOVERY
minimum_participants: 6
segments:
  low_strategy_experience: 3
  deckbuilding_or_autobattle_experienced: 3
scenario_order:
  group_1: [1, 2, 3]
  group_2: [3, 2, 1]
result_variant: COUNTERBALANCED_A_B
session_minutes: 30-40
```

기록 필드:

- 참가자·경험군·시나리오·결과 Variant.
- 최초 구조 변화·통제/RNG 설명·출처 예상.
- 결과 카드 공개에 대한 진행자 개입.
- 결과 뒤 귀인·출처 추적·커밋 이유·포기 대안.
- 다음 구조 수정안.
- undo/reroll 요청·시간·정보 누락 행동.
- 통제감·불공정감·과밀 자기보고.
- 좋은 결과만 자기 공로로 보는 critical incident.

## 8. 판정

비율은 `n/N` 참고값으로만 기록한다.

```yaml
PROMISING_DIRECTION:
  required_patterns:
    - "서로 다른 참가자 2명 이상이 A/B 결과 모두에서 통제 요소와 잔여 RNG를 구분"
    - "출처와 전선 커밋의 장점·포기 비용을 설명"
    - "결과가 달라도 다음 구조 수정안이 릴·TokenSource·역할 비중과 연결"
  claim: "Vertical Slice UX에서 구조·RNG·출처·커밋 인과를 계속 검증할 방향을 지지"
ADAPT:
  condition: "구조 인과는 읽히지만 출처·비가역성·전선 비교 중 한 층에서 반복 혼란"
REWORK:
  condition: "결과 Variant와 무관하게 릴을 계산표 또는 순수 운으로만 읽음"
REJECT:
  condition: "좋은 결과에서만 통제감을 느끼고 나쁜 결과에서 구조 영향을 설명하지 못함"
STOP:
  condition: "정본 충돌, 별도 Core PoC 오인, 진행자 정답 전선 추천"
```

이 fidelity에서는 제품 UX `ADOPT`, 실제 RNG 검증, `CORE_LOCK`을 선언하지 않는다.

## 9. 현재 상태

```yaml
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
next_gate: RUN_COUNTERBALANCED_LOW_FIDELITY_PILOT_AND_WRITE_REPORT
```
