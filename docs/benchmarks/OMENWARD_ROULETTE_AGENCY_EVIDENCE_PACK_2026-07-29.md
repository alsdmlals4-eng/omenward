# OMENWARD 룰렛 통제감·인과 Evidence Pack Pilot

```yaml
evidence_pack_id: OMENWARD-EVP-001
project: OMENWARD
baseline_branch: main
baseline_commit: f747b1d4d6b4f40dcd7a003658d6dfdf9cda7c76
created_at: 2026-07-29
work_mode: PLAN
status: PILOT_RECOMMENDATION
implementation_authority: NONE
human_validation: NOT_RUN
method_reference: Base dc9603595155989e13fb92edff347df5c725217e
```

> 최신 권한은 `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. 이 Pilot은 **별도 CORE_POC를 재도입하지 않으며**, 승인된 전체 Vertical Slice 안에서 룰렛 통제감과 전투 인과를 검증할 대표 상황을 좁히는 계획 입력이다. 제품 코드·데이터·Scene 변경을 승인하지 않는다.

## 1. 현재 코어와 보호 경계

- 플레이어 약속: 예고된 세 전선의 공세를 읽고 건물과 영구 가로 이동으로 미래 릴을 설계한 뒤 당첨 병력을 한 전선에 비가역 커밋한다.
- 핵심 문장: **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**
- 기본 난이도의 치명적 공세 정보는 숨기지 않는다.
- 가로 이동은 TokenInstance만 교환하며 길이·cursor를 바꾸지 않는다.
- stopped 보상은 immutable SpinSnapshot을 사용한다.
- 이동 실행 즉시 소비되고 undo하지 않는다.
- 배치 후 회수·라인 변경·판매하지 않는다.
- 최신 목표는 `FULL_SYSTEM_VERTICAL_SLICE / MINIMUM_CONTENT_BREADTH`다.
- 코어 PoC는 `SKIPPED_BY_USER_DECISION`이며 별도 실행 트랙을 만들지 않는다.
- 최신 Vertical Slice 구현은 시작되지 않았고 Legacy C1~C3 증거를 최신 증거로 간주하지 않는다.

## 2. 결정 질문

> 플레이어가 룰렛 결과를 단순히 운으로 소비하지 않고 **내가 미래 구조를 설계한 결과**라고 이해하게 하려면, 회전 전·정지 후·라인 확정 전 화면에서 통제 가능한 요소와 잔여 무작위성을 어떻게 구분해야 하는가?

### 가장 위험한 플레이 가설

> 플레이어는 `TokenSource 건설 → 세로 조사 → 영구 가로 이동 → 회전 → 비가역 라인 커밋`의 인과를 추적할 수 있을 때, 실패한 결과도 다음 구조 설계로 이어지는 자기 판단으로 받아들인다.

### 성공 조건

- 플레이어가 회전 전에 자신이 바꾼 릴 구간과 기대 결과를 설명한다.
- 정지 뒤 결과가 어느 TokenSource와 이동에서 왔는지 찾는다.
- 나쁜 결과 뒤 `무작위라서 졌다`보다 다음 구조 수정안을 말한다.
- 세 전선 중 한 곳에 커밋한 이유와 포기한 대안을 설명한다.
- 룰렛 UI와 자동전투 결과 사이 인과가 끊기지 않는다.
- 대표 상황 검증이 전체 Vertical Slice 범위와 별도 제품 트랙을 만들지 않는다.

### 실패 조건

- 건물·이동이 결과에 미친 영향을 플레이어가 보지 못한다.
- 확률 수치를 많이 보여주지만 어떤 행동을 해야 하는지 모른다.
- reroll·undo·확률 보정이 늘어나 코어의 비가역 판단을 약화한다.
- 전투가 자동으로 흘러가 결과 원인을 룰렛과 연결하지 못한다.
- 대표 상황 Prototype가 별도 Core PoC나 축소 제품 범위로 승격된다.

## 3. 선택 Coverage

| Coverage | 상태 | 이유 |
|---|---|---|
| 프로젝트 코어·게임 기획 | EVIDENCED | 룰렛 설계와 전선 커밋이 코어다. |
| 플레이어 경험·난이도 | EVIDENCED | 통제감·실패 귀인·다음 계획을 검증한다. |
| UX·UI·접근성 | EVIDENCED | 구조 변화·잔여 RNG·인과 설명의 정보 위계가 필요하다. |
| 벤치마킹·GUR | EVIDENCED | 행동과 자기보고를 분리한다. |
| Godot 구현 | NOT_APPLICABLE | 최신 제품 코드와 Vertical Slice 구현을 승인하지 않는다. |

## 4. Evidence

| ID | 층 | 출처 | 확인된 활용점 | 한계 |
|---|---|---|---|---|
| EVD-OW-01 | T2_PROFESSIONAL_PRACTICE | Randy Smith, GDC 2023, Cards, Dice, and RNGs: Using Randomness Intentionally | 무작위성을 목적에 맞게 선택하고 플레이어가 관리할 수 있게 하는 실무 프레임을 제안한다. | OMENWARD의 정확한 릴 정보량을 제시하지 않는다. |
| EVD-OW-02 | T2_PROFESSIONAL_PRACTICE | Geoff Engelstein, GDC 2018, The Flavors of Tabletop Game Randomness | input/output randomness 등 서로 다른 무작위성 유형을 목적에 맞게 구분한다. | 디지털 3라인 자동전투와 직접 동일하지 않다. |
| EVD-OW-03 | T2_PROFESSIONAL_PRACTICE | Clint Hocking, GDC 2006, Designing to Promote Intentional Play | 플레이어가 목표와 수단을 구성하려면 시스템 동학을 이해해야 하며 투명성에도 비용이 있다. | 구체 UI를 제공하지 않는다. |
| EVD-OW-04 | T2_PROFESSIONAL_PRACTICE | Matthew Davis, GDC 2019, Into the Breach Design Postmortem | 난이도·RNG·기능 제거를 반복 설계 대상으로 다룬다. | 표면 UI나 전투 구조를 복제하지 않는다. |
| EVD-OW-05 | T6_AI_INFERENCE | 본 Pilot 종합 | 확률 숫자보다 `내가 바꾼 구조`, `남은 불확실성`, `정지 결과의 출처`, `전선 커밋 결과`를 연속해서 보여주는 편이 코어 검증에 직접적이다. | 사람 플레이 전 가설이다. |

## 5. 대안 비교

### A. 정확 정지 결과 사전 공개

- 장점: 완전한 계획 가능.
- 위험: 룰렛이 계산표가 되고 회전의 긴장과 잔여 무작위성이 사라진다.
- 판정: `AVOID`.

### B. 구조 변화와 결과 범위 공개, 정확 정지는 비공개

- 플레이어가 만든 세 릴의 배열과 출처를 읽을 수 있다.
- 가로 이동 전후 차이와 영향을 받는 구간을 보여준다.
- 현재 가능한 결과 범위와 전선 수요는 보여주되 정확 정지 index는 숨긴다.
- 정지 후 결과의 출처와 이전 조작을 역추적한다.
- 판정: `ADAPT`.

### C. 낮은 투명성 + reroll·undo 다수 제공

- 장점: 실수를 복구하기 쉽다.
- 위험: 구조 설계보다 사후 확률 소비와 반복 시도가 중심이 된다.
- 판정: `AVOID`.

## 6. Pilot 권장안

최종 판정: **`ADAPT` — B안을 전체 Vertical Slice 내부의 3개 대표 상황 마이크로 테스트로 검증한다.**

### 화면 인과 사슬

1. **공세 브리핑:** 세 전선의 정확한 위협과 필요한 역할.
2. **구조 설계:** TokenSource별 토큰 공급과 세 릴의 현재 배열.
3. **조작 미리보기:** 세로 조사에서 확인한 정보, 가로 이동 전후 변경 구간.
4. **회전 전 요약:** 통제한 요소 / 남은 무작위성 / 기대 역할 범위.
5. **정지 결과:** 선택된 TokenInstance, 출처, 어떤 조작의 영향을 받았는지.
6. **라인 커밋:** 세 전선 결과 예측이 아니라 현재 정보에 기반한 장단점 비교.
7. **전투 인과:** 배치 병력이 어떤 파동·접전·본진 결과에 기여했는지.
8. **다음 설계:** 실패 원인을 다음 건설·이동 후보로 연결.

### 정보 표현 원칙

- 확률·출처·라인을 색상만으로 구분하지 않는다.
- 변경 전후는 애니메이션만이 아니라 고정 비교 상태로도 확인한다.
- `통제 가능`, `이미 확정`, `잔여 무작위`, `비가역 결정`을 서로 다른 라벨로 표시한다.
- 자동전투 중 핵심 인과 이벤트를 일시정지 없이 다시 볼 수 있는 요약 후보를 둔다.
- reroll과 undo는 이번 Pilot에 추가하지 않는다.
- 마이크로 테스트 결과가 전체 Vertical Slice의 구현·검증 완료를 의미하지 않는다.

## 7. Vertical Slice 내부 3개 대표 상황 검증 계약

```yaml
build_or_artifact: paper_or_clickable_vertical_slice_embedded_three_scenario_microtest
tester_segment:
  - 전략 게임 경험이 낮은 참가자 3명 이상
  - 덱빌딩·오토배틀 경험자 3명 이상
scenario_1: 단일 명확 위협 + 한 TokenSource 변화 + 한 커밋
scenario_2: 두 전선 경쟁 + 세로 조사 + 한 가로 이동
scenario_3: 세 전선 압박 + 이전 구조 결과 회수 + 비가역 커밋
primary_metrics:
  - 회전 전 구조 변화 설명률
  - 정지 결과 출처 추적률
  - 실패 후 다음 구조 수정안 제시율
  - 라인 커밋 이유 설명률
  - 상황별 의사결정 시간
guardrails:
  - 확률 표를 읽지 못해도 핵심 인과를 이해하는가
  - UI 확인 시간이 플레이 시간 대부분을 차지하지 않는가
  - 자동전투 결과를 룰렛과 연결하지 못하는가
  - 대표 상황이 별도 Core PoC·축소 Slice로 오인되는가
success:
  - 다수 참가자가 결과를 자기 구조 설계와 연결하고 다음 수정안을 제시한다
failure:
  - 결과를 운으로만 귀인하거나 조작 전후 차이를 찾지 못한다
stop:
  - APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md와 표현이 충돌하면 테스트 중단
```

## 8. 적대적 검토

| Finding | 공격 | 판정 | 대응 |
|---|---|---|---|
| ADV-OW-01 | 투명성을 높이다 정확 정답을 공개한다. | MUST_FIX | 결과 범위·구조는 공개하고 정확 정지 index는 잔여 RNG로 유지한다. |
| ADV-OW-02 | 확률 숫자가 통제감으로 오인된다. | MUST_FIX | 조작 전후 구조와 결과 출처 설명을 우선한다. |
| ADV-OW-03 | 나쁜 결과를 보정하려 reroll·undo를 추가한다. | REJECT | 코어의 영구 이동·비가역 커밋을 보호한다. |
| ADV-OW-04 | 3라인 정보가 한 화면에 과밀해진다. | SHOULD_FIX | 공세→구조→정지→커밋의 단계별 정보 위계를 검증한다. |
| ADV-OW-05 | Legacy C1~C3 성공을 최신 Vertical Slice 통과로 간주한다. | MUST_FIX | 최신 사람 증거는 별도 `NOT_RUN` 상태로 유지한다. |
| ADV-OW-06 | 대표 상황 검증을 별도 CORE_POC로 재도입한다. | REJECT | 승인된 Vertical Slice 내부의 마이크로 테스트로만 유지한다. |
| ADV-OW-07 | Pilot 문서와 validator 통과를 제품 구현 증거로 주장한다. | MUST_FIX | 제품 코드·런타임·사람 검증 상태를 `NOT_AUTHORIZED / NOT_RUN`으로 유지한다. |

## 9. 현재 결정에 미치는 영향

- 최신 `FULL_SYSTEM_VERTICAL_SLICE / MINIMUM_CONTENT_BREADTH` 계약: `NO_CHANGE`.
- V2 상세 규칙·F-30·Legacy seam: `NO_CHANGE`.
- 별도 Core PoC: `NOT_REINTRODUCED`.
- Vertical Slice 내부 룰렛 UX·인과 대표 상황: `PILOT_RECOMMENDATION / TEST`.
- 제품 코드·Codex Build: `NOT_AUTHORIZED`.
- 자동·사람·접근성·성능 검증: `NOT_RUN`.
- 사람 검증 뒤에도 전체 Vertical Slice와 제품 게이트는 별도 판정한다.

## 10. 원출처

- https://www.gdcvault.com/play/1028984/Cards-Dice-and-RNGs-Using
- https://www.gdcvault.com/play/1024920/Board-Game-Design-Day-White
- https://www.gdcvault.com/play/1013427/Designing-to-Promote-Intentional
- https://www.gdcvault.com/play/1025772/-Into-the-Breach-Design

게시일·영상 접근 범위·세부 발언은 실제 적용 직전에 다시 확인한다.

## 11. 실행 보고

```yaml
selected_skills:
  - managing-project-intake-and-work-contract
  - analyzing-and-refining-game-concepts
  - governing-game-user-research-coverage
  - designing-vertical-slices
  - running-adversarial-review-and-refinement
work_modes_used: PLAN -> REVIEW
product_paths_changed: false
runtime_validation: NOT_APPLICABLE
human_validation: NOT_RUN
rollback: remove this planning-input document and its Documentation Map link
```