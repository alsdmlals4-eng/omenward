# [현행] OMENWARD · Text UX와 상태전이 계약

```yaml
decision_id: OMW-PLAN-20260820-TEXT-UX-STATE-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
  - OMW-PLAN-20260820-FIRST5-FTUE-01
  - OMW-PLAN-20260820-BALANCE-BUDGET-01
runtime_mutation: NONE
product_data_mutation: NONE
visual_asset_approval: NONE
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD의 player-facing Run UX는 **Question-first + Staged Commit**을 사용한다.

```text
PREPARE = 다가오는 문제를 보고 무엇을 바꿀 것인가?
COMMIT  = 얻은 병력을 어느 전선에 확정할 것인가?
BATTLE  = 지금 직접 개입해야 하는가?
REVIEW  = 왜 이런 결과가 나왔는가?
```

각 top-level Focus Mode는 하나의 주 질문과 하나의 Primary CTA를 우선한다.

```text
STAGE ENTER
→ PREPARE
→ COMMIT
→ BATTLE
→ REVIEW.RESULT
→ REVIEW.MAINTENANCE
→ NEXT PREPARE
```

Stage 20은 `REVIEW.FINAL → MAPRUN_FINAL_SETTLEMENT`로 종료하며 Merchant를 열지 않는다.

## 2. PREPARE

Player question:

> 다가오는 문제를 보고, 무엇을 바꿀 것인가?

항상 우선 표시:

```text
주 Omen Signature
부 Omen Signature
강도
Route 징후
Gold / Mana / 병력 한도
현재 동원 분포
선택 전후 변화 방향
```

Primary CTA:

`배치 단계로`

건물/업그레이드 UI는 `현재 → 선택 후`의 방향을 보여주되 정답 빌드를 지시하지 않는다.

금지:

- `추천: 궁병을 선택하세요` 같은 prescriptive answer.
- raw internal ID / source ID / exact debug weight의 상시 player 노출.

진행 차단은 일반 문구 대신 부족 항목을 직접 말한다.

예:

```text
필수 준비 2개 남음
금고 · 농장 건설 필요
```

## 3. COMMIT · Staged deployment

현재 프로토타입처럼 전선 버튼 클릭 즉시 영구 배치하지 않는다.

```text
보관 병력 선택
→ 전선 선택
→ PENDING 배치안에 추가
→ COMMIT 내부에서는 취소/수정 가능
→ `배치 확정 · 전투 시작`
→ 원자적으로 실제 비가역 배치 적용
```

`PENDING_COMMIT`은 player plan state이며 실제 deployed troop truth가 아니다.

최종 확정 뒤:

```text
RECALL = FORBIDDEN
SELL_DEPLOYED = FORBIDDEN
CROSS_LANE_MOVE = FORBIDDEN
```

Primary CTA:

- pending 병력이 있을 때: `배치 확정 · 전투 시작`
- 새 배치가 없을 때: `현재 배치로 전투 시작`

상시 경고:

> 확정한 병력은 회수·판매하거나 다른 전선으로 이동할 수 없습니다.

최초 Stage 1 Commit에서만 비가역 설명을 한 번 더 명시한다. 매 병력마다 modal confirmation을 띄우지 않는다.

첫 설명:

> **전선 배치는 비가역입니다.** 확정한 병력은 이번 Run에서 회수·판매하거나 다른 전선으로 이동할 수 없습니다.

재검토 조건:

- staged deployment가 `배치했는데 왜 아직 전장에 없지?` 혼란을 유발한다.
- 사람 플레이에서 accidental irreversible commit이 의미 있게 반복된다.

## 4. BATTLE

Player question:

> 지금 직접 개입해야 하는가?

표시 우선순위:

```text
세 전선 현재 상태
현재 주요 위협
Boss / Elite 핵심 예고
Mana
사용 가능한 전술
Cooldown
Target validity / block reason
```

PREPARE의 Forecast는 사라지지 않고 요약 맥락으로 축소한다.

전투 중에는 건설·새 Spin·새 병력 Commit 편집을 닫는다.

전술은 준비를 대체하는 자동 정답 버튼이 아니다.

## 5. Player-facing block reason language

Internal reason code와 player copy를 분리한다.

예시 mapping:

| Internal / state | Player-facing |
|---|---|
| `insufficient_gold` | `Gold {amount} 부족` |
| `service_not_ready` | `징조륜을 아직 사용할 수 없습니다` |
| mana insufficient | `마력 {amount} 부족` |
| research incomplete | `연구 완료 후 사용할 수 있습니다` |
| invalid target | `이 전술의 대상 조건과 맞지 않습니다` |
| undisclosed route | `공개된 우회 경로에만 사용할 수 있습니다` |
| capacity full | `병력 한도가 부족합니다` |

Player-facing 문구는 반드시 다음 중 하나 이상을 답해야 한다.

```text
무엇이 부족한가
무엇이 아직 준비되지 않았는가
어떤 조건이 맞지 않는가
무엇이 비가역인가
```

Raw reason code는 Debug/Inspector에서만 유지한다.

## 6. REVIEW

Player question:

> 왜 이런 결과가 나왔는가?

Player-facing REVIEW는 5개 인과 블록으로 제한한다.

```text
1. 예고
2. 준비
3. 배치
4. 주요 사건
5. 결과
```

예:

```text
예고
MASS ★★★ + SIEGE ★

준비
대검병 동원 비중 증가
방어탑 유지

배치
중앙 +4
하단 +2

주요 사건
Wave 2 중앙 포화 억제 성공
Wave 3 공성 준비 차단 지연

결과
방어 성공
중앙 성문 피해 28
```

원인 요약은 사실과 인과만 보여준다.

```text
MASS 대응: 안정
SIEGE 대응: 지연
후열 피해: 낮음
```

금지:

`다음에는 창병을 지으세요` 같은 prescriptive next-build command.

## 7. REVIEW substate

Stage 1~19:

```text
REVIEW.RESULT
→ 결과 확인
→ REVIEW.MAINTENANCE
→ Merchant / 수리 / 보상 / 제한 서비스
→ 다음 Stage Forecast 요약
→ NEXT PREPARE
```

Merchant와 정비는 다섯 번째 top-level Mode가 아니라 REVIEW의 후처리 substate다.

Stage 20:

```text
REVIEW.FINAL
→ MAPRUN_FINAL_SETTLEMENT
```

## 8. FTUE Stage 1~5 player copy baseline

| 순간 | 기준 문구 |
|---|---|
| Stage 1-A | `금고와 농장을 세워 수호성을 유지할 기반을 마련하세요.` |
| Stage 1-B | `병영과 방어탑을 세워 병력과 전선을 준비하세요.` |
| Stage 1-C | `지휘소와 마력탑을 세워 지휘 체계를 완성하세요.` |
| Stage 1-D | `징조륜이 열렸습니다. 건물이 등록한 동원 인장을 확인하고 첫 동원을 실행하세요.` |
| Stage 1 Commit | `새 병력의 전선을 정하세요. 확정한 뒤에는 회수하거나 옮길 수 없습니다.` |
| Stage 2 | `T2 전문화는 현재 전력과 이후 동원 분포를 함께 바꿉니다. 선택 전후를 비교하세요.` |
| Stage 3 | `전술 하나를 연구했습니다. 전투 중 필요한 순간에 직접 사용하세요.` |
| Stage 4 | `새로운 규칙은 없습니다. 징조를 읽고 직접 방어 계획을 완성하세요.` |
| Stage 5 | `첫 수렴이 시작됩니다. Boss의 핵심 위협과 마지막 Wave의 Elite를 먼저 확인하세요.` |

문구는 최종 로컬라이징 전 CHANGEABLE이지만 의미 계약은 보호한다.

## 9. Debug vs Player surface

Player surface에서 제거/상세로 숨김:

```text
raw Token Ledger weights
source_building_ids
reward_archetype_ids
unit IDs
raw target IDs
internal cause codes
internal failure reason codes
exact diagnostic counters
```

Player surface에서 유지:

```text
확률/분포 변화의 이해 가능한 요약
현재 자원
현재/예고 전선 위협
사용 가능 행동
차단 이유
결과 인과
```

## 10. 장기 fast path

숙련 플레이어를 위해 모드를 없애지 않고 같은 state contract 위에 단축 경로를 추가할 수 있다.

허용:

```text
keyboard/controller shortcuts
last-focused panel restore
quick lane assignment within COMMIT
one-action jump to detailed Forecast
```

금지:

- 비가역 commit 경계를 숨기는 fast path.
- Battle 중 Prepare/Commit mutation.
- raw debug UI를 숙련자 기본 UI로 승격.

## 11. 검증 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_MUTATION = NONE
CURRENT_RUNTIME = NOT_RUN
HUMAN_VALIDATION = NOT_RUN
STAGED_COMMIT_USABILITY = NOT_RUN
PLAYER_COPY_READABILITY = NOT_RUN
```

사람 플레이에서 staged commit 혼란, confirmation fatigue, block reason 이해 실패를 실제 관찰한 뒤 fast path나 확인 강도를 조정한다.

## 12. 다음 Gate

```text
NEXT_PRODUCT_DECISION = VISUAL_REFERENCE_RECONCILIATION
VISUAL_REFERENCE_FILES = RECEIVED_REFERENCE_ONLY_NOT_CANON
IMAGE_GENERATION = PAUSED_UNTIL_VISUAL_DIRECTION_REAPPROVAL
IMPLEMENTATION_START = NOT_AUTHORIZED
```
