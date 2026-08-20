# [현행] OMENWARD Run Command Screen · Focus Mode 구조

```yaml
decision_id: OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-WORLD-ROLE-01
  - OMW-PLAN-20260820-MAPRUN-WORLD-01
  - OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
  - OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
  - OMW-PLAN-20260820-FIRST5-FTUE-01
scope: PLAYER_FACING_RUN_COMMAND_SCREEN_INFORMATION_ARCHITECTURE
runtime_mutation: NONE
balance_mutation: NONE
visual_asset_approval: NONE
```

## 1. 결정

OMENWARD의 한 Run은 완전히 분리된 여러 전체화면을 반복 전환하는 구조보다, 하나의 **Run Command Screen**을 지속 맥락으로 사용하고 현재 플레이어 질문에 따라 정보 우선순위를 바꾸는 Focus Mode 구조를 기본안으로 한다.

```text
RUN COMMAND SCREEN
→ PREPARE
→ COMMIT
→ BATTLE
→ REVIEW
→ next Stage PREPARE
```

화면은 수호성·세 전선·현재 Stage라는 공간적 맥락을 유지하되, 각 단계에서 필요하지 않은 조작과 상세 정보는 뒤로 물린다.

## 2. 지속 맥락

Focus Mode가 바뀌어도 다음 정보는 플레이어가 맥락을 잃지 않도록 지속적으로 접근 가능해야 한다.

```text
CURRENT_STAGE / WAVE
CORE_RESOURCES
THREE_LANE_SPATIAL_CONTEXT
FORECAST_SUMMARY
```

세 전선의 공간적 위치와 현재 Omen Signature 요약은 준비→배치→전투→복기 사이에서 서로 다른 장소로 재해석되지 않는다.

## 3. PREPARE Focus Mode

핵심 질문:

> 다가오는 문제를 보고 무엇을 바꿀 것인가?

권장 정보 흐름:

```text
Forecast
→ Building / Upgrade choice
→ current mobilization distribution vs expected directional change
→ Omen Wheels focus layer
→ acquired troops
```

- 건설과 징조륜을 서로 독립된 미니게임처럼 분리하지 않는다.
- 건물 선택 시 `직접 생산`과 `동원 인장/TokenSource 기여`의 차이를 읽을 수 있어야 한다.
- 정확한 Token Ledger·내부 weight는 필요 시 상세로 열며 player-facing 상시 정보로 강제하지 않는다.

## 4. COMMIT Focus Mode

핵심 질문:

> 지금 얻은 병력을 어느 전선에 되돌릴 수 없게 투입할 것인가?

룰렛 결과 뒤에는 건설 UI의 시각 우선순위를 낮추고 세 전선과 획득 병력을 전면에 둔다.

```text
ACQUIRED_TROOP
→ compare lane forecast / current friendly state
→ choose one lane
→ irreversible deployment
```

`Top / Middle / Bottom` 같은 추상 버튼만으로 끝내기보다 실제 전장 공간에서 전선을 선택하는 행위로 읽히는 UX를 우선한다.

세 징조륜과 세 전선은 1:1 대응하지 않는다. 징조륜 결과를 어느 전선에 배치할지는 별도 플레이어 결정이다.

## 5. BATTLE Focus Mode

핵심 질문:

> 지금 전술적으로 개입할 가치가 있는 순간인가?

전투가 시작되면 건설과 룰렛 편집 조작은 기본 player-facing 우선순위에서 물러난다.

상시 핵심:

```text
THREE_LANE_STATUS
KEY_THREAT / OMEN CONTEXT
MANA
AVAILABLE_TACTICAL_ACTIONS
```

자동전투의 전략성을 유지하기 위해 전투 중 반복 클릭 노동이나 다수의 상시 버튼을 핵심으로 만들지 않는다. 수동 전술은 준비를 대체하는 자동 승리 도구가 아니라 결정적 순간 보정이다.

## 6. REVIEW Focus Mode

핵심 질문:

> 내 설계와 배치가 왜 이런 결과를 만들었는가?

현재 기술 프로토타입의 `WAVE CAUSE REPORT` 계열 evidence는 최종 player UI에서 raw debug text 그대로 노출하지 않고 다음 인과 구조로 재표현한다.

```text
Forecast
→ player preparation / mobilization structure
→ major lane commitment
→ key battle events
→ tactical response
→ outcome
```

허용:
- 사실 기반 원인 요약
- 어떤 Signature 대응이 충분/부족했는지 설명
- 전선별 주요 손실·성문/거점 변화

금지:
- `다음에는 X를 지으세요` 식 처방형 정답
- 실패 이유를 하나의 단일 hard-counter 부족으로 단정
- runtime에서 관측되지 않은 원인을 추정해 사실처럼 표시

## 7. 정보 계층

player-facing 정보는 기본적으로 세 계층으로 관리한다.

```text
ALWAYS_VISIBLE
→ Stage/Wave, 핵심 자원, 세 전선 Forecast 요약

CURRENT_FOCUS
→ 현재 Mode에서 결정에 필요한 핵심 정보와 조작

ON_DEMAND_DETAIL
→ 병종 상세, 정확한 Token Ledger, 수치 비교, 상세 전투 로그
```

기술 디버그/Inspector 용도의 Token Ledger, target priority, raw cause report, internal IDs를 최종 player HUD에 상시 노출하지 않는다.

## 8. 현행 프로토타입과의 관계

현재 `scenes/ui/stage_hud.tscn`과 `scripts/ui/stage_hud.gd`는 Omen, Token Ledger, 건설 비교, Tactical Overlay, Wave Report, Spin, 건설, 배치 등을 하나의 기술 HUD에서 노출한다.

이 상태는 구현·evidence 관찰용 기술 프로토타입으로 보존 가능하지만 최종 player-facing 정보 구조의 North Star는 아니다.

```text
CURRENT_STAGE_HUD = TECHNICAL_PROTOTYPE / DEBUG-capable surface
FINAL_PLAYER_UI_NORTH_STAR = RUN_COMMAND_SCREEN_WITH_FOCUS_MODES
```

이 Decision만으로 현재 Scene/Script를 수정하지 않는다.

## 9. 대안과 재검토

### 대안 B · 전체 화면 분리

Prepare / Roulette / Battle을 완전히 다른 전체 화면으로 분리하면 각 화면은 단순해지지만 `건설 → 확률 → 배치 → 결과` 인과와 공간 기억이 끊길 위험이 있어 기본안으로 채택하지 않는다.

### 대안 C · 모든 정보 상시 대시보드

숙련자와 디버그 관점에서는 정보 접근이 빠르지만 첫 세션 정보 과부하와 작은 화면 확장 문제가 커 player-facing 기본안에서 제외한다. Debug/Inspector surface에서는 허용한다.

재검토 조건:
- Focus Mode 전환 때문에 필요한 비교 정보가 숨겨져 왕복 탐색이 반복됨
- 동일 Command Screen 유지가 전장 가독성을 오히려 낮춤
- 작은 해상도/Android에서 지속 맥락과 현재 Focus를 동시에 보이기 어려움
- release-near Vertical Slice에서 플레이어가 현재 Phase와 다음 행동을 반복적으로 혼동함

## 10. 검증 상태

```yaml
TECH_EVIDENCE: EXISTING_STAGE_HUD_FOUND_AS_PROTOTYPE_ONLY
UI_EVIDENCE: NOT_RUN
HUMAN_USABILITY_EVIDENCE: NOT_RUN
PLAYER_EXPERIENCE_EVIDENCE: NOT_RUN
VISUAL_NORTH_STAR_ASSET: NOT_CREATED
```

실제 시각 계층과 사용성은 승인 Visual North Star를 만든 뒤 release-near Vertical Slice에서 검증한다.
