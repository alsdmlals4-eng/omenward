# OMENWARD 룰렛 통제감 사람 검증 Artifact 실행 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans only after a separate product-build approval. This document authorizes low-fidelity research preparation and human observation only.

**Goal:** 전체 Vertical Slice의 룰렛 설계→정지 결과→전선 커밋→전투 결과 인과를 세 개 대표 상황으로 축소해, 플레이어가 결과를 자신의 구조 설계와 잔여 무작위성으로 구분하는지 검증한다.

**Architecture:** 최신 Vertical Slice 구현은 시작하지 않는다. 세 원형 릴을 카드 스트립, TokenSource를 출처 카드, 공세를 전선 브리핑 카드, 정지와 전투를 숨김 결과 카드로 표현한다. 참가자는 구조 변경과 커밋을 직접 수행하지만 정확 정지 index는 결과 공개 전 알 수 없다.

**Tech Stack:** Markdown 인쇄 카드 또는 읽기 전용 클릭 순서, 수기 토큰, 타이머, 관찰 기록표. Godot·Scene·Resource·제품 데이터는 사용하거나 변경하지 않는다.

## Global Constraints

- 기준 `main`: `f36192293c8ea163b8e19fe749adcc122404f6c5`.
- 상위 Evidence Pack: `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`.
- 최신 권한: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`.
- 목표는 `FULL_SYSTEM_VERTICAL_SLICE / MINIMUM_CONTENT_BREADTH`다.
- 별도 Core PoC를 재도입하지 않는다.
- 가로 이동은 TokenInstance와 출처를 이동시키며 실행 즉시 확정되고 되돌릴 수 없다.
- stopped 결과는 immutable SpinSnapshot 관점으로 취급한다.
- 배치 후 라인 변경·회수·판매를 허용하지 않는다.
- 정확 정지 index를 사전에 공개하지 않는다.
- 이 Artifact의 역할 토큰은 `RESEARCH_ONLY_ROLE_TOKEN`이며 최종 병종·아트·밸런스 정본이 아니다.
- 사람 테스트 결과는 전체 Vertical Slice 구현·검증 완료를 의미하지 않는다.

---

## 1. Artifact 구성

세션 패킷은 다음 여섯 장의 화면 역할로 구성한다.

1. **공세 브리핑:** 상·중·하 전선 위협과 필요한 역할.
2. **현재 구조:** 세 릴의 토큰 순서와 각 TokenSource 출처.
3. **조작 카드:** TokenSource 변화 또는 한 번의 영구 가로 이동.
4. **회전 전 요약:** 플레이어가 통제한 요소와 남은 무작위성.
5. **정지·커밋 카드:** 정지 결과 출처 확인과 세 전선 중 한 곳에 비가역 배치.
6. **전투 인과 카드:** 배치가 방어·점령·본진 결과에 기여한 내용과 다음 수정 질문.

## 2. 연구 전용 표기 규칙

### 역할 토큰

| 표기 | 의미 | 제품 정본 여부 |
|---|---|---|
| `DEFENDER` | 피해를 버티거나 전선 붕괴를 늦추는 역할 | 연구 전용 |
| `CONTROL` | 적 진격·점령을 저지하는 역할 | 연구 전용 |
| `BREAKER` | 방어선을 밀거나 핵심 적을 돌파하는 역할 | 연구 전용 |
| `[금화]` | 현재 정본의 금고 TokenSource 보상 | 승인 개념 사용 |
| `X` | source lifecycle로 공급 불가 상태를 나타내는 연구 표식 | `SOURCE_BOUND_X` 개념 참고 |

역할 토큰은 특정 T2·T3 병종을 확정하지 않는다.

### 출처 태그

모든 토큰 뒷면에 다음 중 하나를 표시한다.

- `VAULT-A`
- `BARRACKS-A`
- `BARRACKS-B`
- `BASELINE`

참가자는 정지 뒤 토큰을 뒤집어 출처를 확인한다.

## 3. 시나리오 1 — 단일 위협과 한 TokenSource 변화

```yaml
scenario_id: OW-AGENCY-1
purpose: "건설 선택이 다음 결과 분포를 바꿨다고 이해하는가"
threats:
  top: "강한 단일 돌파 — DEFENDER 필요"
  middle: "낮은 압박"
  bottom: "낮은 압박"
reels_before:
  reel_1: [CONTROL@BASELINE, GOLD@VAULT-A, BREAKER@BASELINE]
  reel_2: [BREAKER@BASELINE, CONTROL@BASELINE, GOLD@VAULT-A]
  reel_3: [CONTROL@BASELINE, BREAKER@BASELINE, GOLD@VAULT-A]
player_change:
  action: "BARRACKS-A를 선택해 각 릴의 지정 공급 위치에 DEFENDER를 하나씩 공급"
reels_after:
  reel_1: [DEFENDER@BARRACKS-A, GOLD@VAULT-A, BREAKER@BASELINE]
  reel_2: [BREAKER@BASELINE, DEFENDER@BARRACKS-A, GOLD@VAULT-A]
  reel_3: [CONTROL@BASELINE, BREAKER@BASELINE, DEFENDER@BARRACKS-A]
hidden_stop_result:
  center_row: [DEFENDER@BARRACKS-A, DEFENDER@BARRACKS-A, DEFENDER@BARRACKS-A]
commit_target: top
battle_result: "상단 돌파를 지연해 본진 피해를 막았지만 중단의 점령 진전은 얻지 못함"
```

질문:

1. 회전 전 무엇을 바꿨는가?
2. 결과 중 무엇이 설계 영향이고 무엇이 아직 무작위인가?
3. 정지 뒤 세 토큰이 어디서 왔는가?
4. 상단 커밋 외 대안은 무엇이었는가?

## 4. 시나리오 2 — 두 전선 경쟁과 한 번의 영구 가로 이동

```yaml
scenario_id: OW-AGENCY-2
purpose: "가로 이동의 현재·미래 동시 영향과 비가역성을 이해하는가"
threats:
  top: "다수 진격 — CONTROL 필요"
  middle: "중장갑 핵심 — BREAKER 필요"
  bottom: "안정"
reels_before:
  reel_1: [CONTROL@BARRACKS-A, GOLD@VAULT-A, BREAKER@BARRACKS-B]
  reel_2: [BREAKER@BARRACKS-B, CONTROL@BARRACKS-A, GOLD@VAULT-A]
  reel_3: [GOLD@VAULT-A, BREAKER@BARRACKS-B, CONTROL@BARRACKS-A]
player_information:
  - "세로 조사로 현재 노출 위치를 확인함"
  - "정확 정지 index는 알 수 없음"
allowed_move:
  action: "현재 보드의 가로 한 줄에서 CONTROL과 BREAKER 위치를 한 번 교환"
  cost: "사용 즉시 확정, undo 없음"
hidden_stop_result:
  center_row: [CONTROL@BARRACKS-A, BREAKER@BARRACKS-B, CONTROL@BARRACKS-A]
commit_options:
  - top
  - middle
facilitator_battle_results:
  top: "다수 진격은 막았으나 중단 핵심 적이 중간 거점을 압박함"
  middle: "핵심 적을 제거했으나 상단 점령 진행이 일부 후퇴함"
```

참가자는 실제로 토큰 두 개를 교환한다. 진행자는 이동 뒤 원래 순서를 다시 보여주지 않는다. 변경 전 카드는 별도 비교판으로만 남겨 기억 시험을 방지한다.

## 5. 시나리오 3 — 세 전선 압박과 이전 구조 결과 회수

```yaml
scenario_id: OW-AGENCY-3
purpose: "이전 설계가 다음 스테이지 판단으로 환류하는가"
prior_history:
  - "시나리오 2에서 BARRACKS-B BREAKER 비중을 유지함"
  - "상단 CONTROL 부족이 기록됨"
threats:
  top: "점령 회복 직전 — CONTROL 필요"
  middle: "중간 거점 방어 — DEFENDER 필요"
  bottom: "적 본진 돌파 기회 — BREAKER 필요"
reels:
  reel_1: [CONTROL@BARRACKS-A, DEFENDER@BARRACKS-A, BREAKER@BARRACKS-B]
  reel_2: [BREAKER@BARRACKS-B, GOLD@VAULT-A, DEFENDER@BARRACKS-A]
  reel_3: [CONTROL@BARRACKS-A, BREAKER@BARRACKS-B, GOLD@VAULT-A]
hidden_stop_result:
  center_row: [CONTROL@BARRACKS-A, DEFENDER@BARRACKS-A, BREAKER@BARRACKS-B]
commit_rule: "세 결과를 한 전선에만 커밋하고 이후 회수·판매·라인 변경 불가"
facilitator_battle_results:
  top: "점령 회복을 막았지만 중단 건물 피해와 하단 돌파 기회를 포기함"
  middle: "거점을 지켰지만 상단 점령 진행과 하단 돌파가 악화됨"
  bottom: "적 본진에 피해를 주지만 상단 점령과 중단 수리비가 증가함"
```

참가자는 선택 뒤 포기한 두 전선의 결과도 말해야 한다.

## 6. 회전 전 요약 카드

각 시나리오에서 참가자가 직접 다음 네 칸을 채운다.

| 칸 | 기록 예시 |
|---|---|
| 내가 바꾼 구조 | TokenSource 추가 또는 가로 이동 |
| 이미 확정된 것 | 공세 정보, 현재 릴 순서, 이동 소비 |
| 남은 무작위성 | 정확 정지 index와 완성선 |
| 비가역 결정 | 이동 소비, 정지 후 전선 커밋 |

진행자는 칸을 대신 채우지 않는다. 비어 있으면 그대로 관찰 결과로 기록한다.

## 7. 진행자 스크립트

### 시작 안내

> "이 테스트는 슬롯에서 운이 좋았는지를 평가하지 않습니다. 어떤 구조를 바꿨고, 무엇이 아직 무작위이며, 나온 결과를 어느 전선에 왜 배치했는지 확인합니다. 정확 정지 위치는 회전 전에는 공개하지 않습니다."

### 시나리오당 순서

1. 공세 브리핑을 15초 동안 읽게 한다.
2. 현재 세 릴과 출처 태그를 보여준다.
3. 허용된 건설 또는 가로 이동을 참가자가 직접 수행한다.
4. 회전 전 요약 카드 네 칸을 채우게 한다.
5. 숨김 결과 카드를 뒤집는다.
6. 정지 토큰의 출처를 참가자가 찾게 한다.
7. 한 전선에 결과를 커밋한다.
8. 해당 전투 인과 카드를 공개한다.
9. 다음 구조 수정안을 말하게 한다.

진행자는 가장 좋은 전선을 추천하지 않는다.

## 8. 참가자 구성

```yaml
minimum_participants: 6
segments:
  low_strategy_experience: 3
  deckbuilding_or_autobattle_experienced: 3
session_minutes: 30-40
order:
  participant_1_3: [1, 2, 3]
  participant_4_6: [3, 2, 1]
```

시나리오 3을 먼저 받는 참가자에게는 `prior_history` 카드만 제공하고 시나리오 2의 정답이나 추천을 설명하지 않는다.

## 9. 관찰 기록지

| 필드 | 기록 규칙 |
|---|---|
| `participant_id` | 개인 식별정보 없는 코드 |
| `segment` | `LOW` 또는 `EXPERIENCED` |
| `scenario_id` | 1/2/3 |
| `structure_change_explained` | 0/1 |
| `controlled_vs_random_explained` | 0/1 |
| `source_trace_correct` | 0/1 |
| `commit_reason_uses_threat` | 0/1 |
| `foregone_alternative_explained` | 0/1 |
| `next_structure_adjustment` | 참가자 원문 요약 |
| `decision_seconds` | 조작 시작부터 커밋까지 |
| `structure_review_seconds` | 릴·출처 확인 시간 |
| `attribution` | `OWN_STRUCTURE / RESIDUAL_RNG / BOTH / PURE_LUCK / UI_CONFUSION` |
| `undo_requested` | 0/1 |
| `reroll_requested` | 0/1 |
| `separate_poc_confusion` | 0/1 |
| `observer_note` | 정보 과밀·출처 미확인·색상 의존 등 |

## 10. 계산과 판정

- 구조 변화 설명률: `structure_change_explained=1` 비율.
- 잔여 무작위성 구분률: `controlled_vs_random_explained=1` 비율.
- 출처 추적률: `source_trace_correct=1` 비율.
- 전선 커밋 인과율: 위협과 포기 대안을 모두 설명한 비율.
- 순수 운 귀인률: `attribution=PURE_LUCK` 비율.
- 다음 수정안 제시율: 구체 TokenSource·릴 순서·역할 비중 중 하나를 언급한 비율.

```yaml
ADOPT_FOR_VERTICAL_SLICE_UX_BLUEPRINT:
  structure_change_rate: ">= 0.75"
  controlled_randomness_rate: ">= 0.67"
  source_trace_rate: ">= 0.67"
  commit_causality_rate: ">= 0.67"
  next_adjustment_rate: ">= 0.67"
  pure_luck_attribution_rate: "<= 0.25"
ADAPT:
  condition: "구조 인과는 읽히지만 출처·비가역성·전선 비교 중 한 층에서 반복 혼란 발생"
REWORK:
  condition: "대부분이 릴을 계산표로만 읽거나 전투 결과와 커밋을 연결하지 못함"
REJECT:
  condition: "결과를 순수 운으로 소비하고 다음 구조 수정안이 나오지 않음"
STOP:
  condition: "Artifact가 최신 Vertical Slice 계약과 충돌하거나 별도 Core PoC로 해석됨"
```

## 11. 증거 저장 계약

사람 테스트 뒤에만 다음 문서를 별도 PR로 만든다.

```text
docs/validation/OMENWARD_ROULETTE_AGENCY_HUMAN_VALIDATION_REPORT_2026-XX-XX.md
```

필수 내용:

- 실행 `main` SHA와 사용한 Artifact 버전.
- 참가자 수·경험 구분.
- 시나리오별 원자료.
- 구조·RNG·출처·커밋·전투 인과 계산.
- `ADOPT / ADAPT / REWORK / REJECT` 판정.
- 전체 Vertical Slice UX 청사진에 반영할 원칙.
- 제품 구현·사람 전체 Slice 검증·CORE_LOCK 상태는 계속 별도라고 명시.

## 12. 실행 작업

### Task 1: 정본 대조

- [ ] `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`의 룰렛·전선·커밋 불변 조건과 이 문서를 비교한다.
- [ ] 가로 이동 undo 금지, 정확 정지 비공개, 배치 후 회수 금지가 유지되는지 확인한다.
- [ ] 충돌이 있으면 세션을 시작하지 않는다.

### Task 2: 카드 제작

- [ ] 세 릴 카드를 같은 크기로 인쇄하거나 읽기 전용 화면으로 만든다.
- [ ] 토큰 앞면에는 역할, 뒷면에는 출처를 표시한다.
- [ ] 변경 전·후 비교판을 애니메이션 없이도 볼 수 있게 한다.
- [ ] 정지 결과와 전투 인과 카드는 참가자 응답 전 숨긴다.

### Task 3: 사람 세션

- [ ] 두 경험군 각 3명 이상을 실행한다.
- [ ] 시나리오 순서를 역전 배정한다.
- [ ] 행동과 자기보고를 분리 기록한다.
- [ ] reroll·undo 요청이 나와도 기능을 추가하지 않고 이유만 묻는다.

### Task 4: 판정

- [ ] 확률 계산 능력이 아니라 인과 설명을 우선한다.
- [ ] 시나리오 성공을 전체 Vertical Slice 검증으로 확대하지 않는다.
- [ ] 보고서 판정 전 제품 구현 PR을 만들지 않는다.

## 13. 적대적 셀프 리뷰

- 역할 토큰이 최종 병종으로 오인될 수 있음 → 모든 역할에 `RESEARCH_ONLY_ROLE_TOKEN` 표시.
- 결과 카드가 정답 전선 강의가 될 수 있음 → 모든 커밋에 장점과 포기 비용을 동시에 기록.
- 시나리오 1의 좋은 결과가 통제감 과대평가를 만들 수 있음 → 시나리오 2·3에서 트레이드오프 결과 사용.
- 표본이 작아 수치가 과대해석될 수 있음 → 방향성 Pilot이며 통계적 유의성 주장 금지.
- 저충실도 카드 통과가 UI 통과로 오인될 수 있음 → 실제 Godot·접근성·성능은 계속 `NOT_RUN`.

## 14. 현재 상태

```yaml
artifact_status: READY_FOR_LOW_FIDELITY_HUMAN_SESSION
product_code_changed: false
vertical_slice_implementation_started: false
separate_core_poc_created: false
canon_changed: false
human_validation: NOT_RUN
implementation_authority: NONE
next_gate: RUN_SIX_PARTICIPANT_THREE_SCENARIO_MICROTEST
rollback: remove this document only
```
