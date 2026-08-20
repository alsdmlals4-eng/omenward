# [현행] OMENWARD · Lower Control Deck Spec

```yaml
decision_id: OMW-PLAN-20260820-LOWER-CONTROL-DECK-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_BATTLEFIELD_PRIMARY_LOWER_SECONDARY_DIRECTION
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
  - OMW-PLAN-20260820-TEXT-UX-STATE-01
  - OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01
  - OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01
runtime_mutation: NONE
scene_mutation: NONE
human_validation: NOT_RUN
```

## 1. 결정

하단은 **Focus-adaptive Compact Control Deck**를 사용한다.

```text
BATTLEFIELD = primary
LOWER_CONTROL_DECK = secondary
ONE_ACTIVE_WORK_SURFACE_AT_A_TIME = TRUE
DUPLICATE_TOP_RESOURCES = FORBIDDEN
```

하단에 모든 메뉴를 동시에 펼쳐놓지 않는다. 현재 Focus Mode와 현재 선택 Tab에 필요한 조작면 하나만 전개한다.

## 2. 대안 검토

### A · Focus-adaptive Compact Deck — 채택

- 전장 높이를 유지한다.
- 하단 shell은 일관되지만 내부 panel만 바뀐다.
- 3×3 Roulette Focus에서는 Board/Arrows가 중심.
- COMMIT/BATTLE/REVIEW에서는 해당 질문에 필요한 요소만 보인다.

### B · Persistent Dashboard — 비채택

자원, 룰렛, Tier, 결과, 건설, 전술, Bellu를 모두 상시 표시하면 전장을 침범하고 Decision 6/10의 Focus hierarchy를 무너뜨린다.

### C · Mostly Hidden Drawer — 비채택

전장은 가장 넓게 보이지만 핵심 룰렛 조작과 현재 행동 상태가 숨겨져 반복적인 열기/닫기 조작이 생긴다.

## 3. 높이 planning envelope

```text
REFERENCE = 960×540
GLOBAL_LOWER_DECK = 25~32% exploration
ROULETTE_FOCUS = 28~32%
OTHER_FOCUS_BASELINE = 25~28%
```

- 이전 대형 하단 시안 대비 약 절반 수준의 세로 점유를 목표로 한다.
- exact pixels는 North Star/Vertical Slice에서 검증한다.
- 하단이 커져 아군/Veil 본진이나 전선 하나가 잘리면 실패다.

## 4. 상단 HUD 단일 소유

상단/전장 overlay가 소유:

```text
Gold
Mana / current tactical resource
Deployed Troops / Troop Limit
Stage / Wave
Prepare / Maintenance timer
Speed / Pause / Settings
Forecast summary when relevant
```

하단에서 같은 숫자를 다시 표시하지 않는다.

```text
LOWER_GOLD_DUPLICATE = FORBIDDEN
LOWER_MANA_DUPLICATE = FORBIDDEN
LOWER_TROOP_LIMIT_DUPLICATE = FORBIDDEN
```

예외:

- Spin cost, building cost, tactical cost처럼 **현재 행동의 비용**은 CTA 옆에 로컬 표시할 수 있다.
- 이는 현재 보유 총량을 복제하는 것이 아니다.

## 5. Shell 구조

하단 shell의 기본 층:

```text
TOP EDGE = current focus label / optional compact status
MAIN WORK AREA = active tab / mode surface
BOTTOM OR SIDE STRIP = compact tab navigation
PRIMARY CTA = current mode/action only
CONTEXT GUIDE = optional / collapsible
```

불필요한 빈 공간을 새 정보로 채우지 않는다.

## 6. Tab 계약

기본 기능 접근:

```text
ROULETTE
STORAGE
BUILD
TACTICAL
```

Bellu는 독립적인 fifth management menu가 아니라 **context guide panel**이다.

- Bellu는 FTUE/설명/상태 피드백에서 열릴 수 있다.
- 평상시에는 작은 portrait/cue 또는 접힌 상태를 허용한다.
- 정답 빌드를 대신 추천하지 않는다.

## 7. PREPARE / Roulette surface

우선순위:

```text
LEFT COMPACT = Lucky / Stored Move Ticket
CENTER DOMINANT = 3×3 board + 12 arrows
RIGHT ACTION = Spin / Result Preview / Confirm
```

권장 planning widths @ 960 reference:

```text
MOVE_RESOURCE_COMPACT = 88~108 px exploration
BOARD_AND_ARROWS = 168~188 px exploration
ACTION_RESULT = 150~180 px exploration
CONTEXT_GUIDE = 80~110 px optional exploration
```

남는 폭은 padding/breathing space로 남길 수 있다. Dashboard처럼 모든 공간을 채우지 않는다.

## 8. PREPARE / Build surface

룰렛 보드를 숨기고 Build 선택에 필요한 것만 표시한다.

```text
building choices
current → after change summary
local cost
construction / upgrade CTA
```

- 상단 Gold 총량은 그대로 사용하고 하단에 전체 자원 표를 복제하지 않는다.
- 선택한 건물의 Roulette/TokenSource 영향이 있으면 한 줄 요약/preview로 연결한다.

## 9. COMMIT surface

```text
stored / newly acquired units
pending lane assignment
three-lane comparison cue
irreversible warning
PRIMARY CTA = 배치 확정 · 전투 시작
```

- 3×3 board는 기본적으로 닫는다.
- Pending assignment는 editable plan이며 final confirm 전에는 실제 배치가 아니다.
- 병력마다 반복 modal을 띄우지 않는다.

## 10. BATTLE surface

```text
TACTICAL quick access
Mana cost per selected skill as local cost
cooldown / target validity
current lane / target cue
```

- Build/Spin/Commit mutation은 닫는다.
- 전술을 쓰지 않을 때 하단을 정보 대시보드로 채우지 않는다.
- 전장 전투가 시각적으로 가장 큰 면적과 주의를 유지한다.

## 11. REVIEW surface

```text
Forecast → Prepare → Commit → Key Event → Result
maintenance / merchant entry
next-stage transition CTA
```

- raw battle log는 기본 surface에서 숨긴다.
- Review result가 충분히 길면 하단 내부 pagination/step 전환은 허용하지만 전장을 완전히 가리는 full modal은 기본값이 아니다.

## 12. Primary CTA ownership

같은 순간에 동급 Primary CTA를 여러 개 두지 않는다.

예:

```text
Roulette READY = 룰렛 돌리기
Roulette STOPPED = 결과 확정
COMMIT = 배치 확정 · 전투 시작
BATTLE = no forced global CTA; tactical action is contextual
REVIEW = 정비 / 다음 Stage 준비
```

## 13. Controller / keyboard focus

- tab strip → active work area → primary CTA 순의 예측 가능한 focus route를 사용한다.
- Roulette Focus 안에서는 3×3 주변 화살표를 local navigation group으로 묶는다.
- hover-only 정보는 금지하며 focus에도 동일 preview/tooltip을 제공한다.
- disabled control은 이유를 player-facing copy로 설명한다.

## 14. Visual density guardrail

금지:

```text
ALL_TABS_CONTENT_VISIBLE_AT_ONCE
DUPLICATE_RESOURCE_TABLE
ALWAYS_EXPANDED_TIER_LEGEND
ALWAYS_EXPANDED_BELLU_DIALOGUE
RAW_TOKEN_LEDGER
RAW_TARGET_IDS
```

허용:

```text
contextual help
collapsed tier/line rule legend
short result summary
local action cost
small state badges
```

## 15. Benchmark adaptation

- Thronefall의 streamlined defense UI 원리: 전투/방어 핵심을 장식보다 우선한다.
- Into the Breach의 minimal tactical information 원리: 판단에 필요한 정보만 전투 공간과 함께 읽힌다.
- 타 게임의 실제 HUD layout은 복제하지 않는다.

## 16. 검증

```text
960×540
1280×720
1920×1080
mouse / keyboard / controller focus route
```

PASS 후보:

- 세 전선 전체가 하단 open 상태에서도 보임.
- 현재 질문과 Primary CTA를 1~2초 내 찾을 수 있음.
- 자원 숫자가 상/하단에 중복되지 않음.
- Roulette Focus에서 3×3/Arrows가 하단의 가장 중요한 조작으로 보임.
- Build/Commit/Battle/Review에서 불필요한 Roulette panel이 전장을 침범하지 않음.

## 17. 다음 작업 순서

```text
COMPLETE = LOWER_CONTROL_DECK_SPEC
CURRENT_NEXT = ROULETTE_DDD_FEEDBACK_SPEC
THEN = NEW_NORTH_STAR_ONE_IMAGE
THEN = COMPONENT_SHEET
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
THEN = IMPLEMENTATION_HANDOFF_AFTER_USER_AUTHORITY
```

## 18. 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE = UNCHANGED
RUNTIME = NOT_RUN
HUMAN_VALIDATION = NOT_RUN
FINAL_LOWER_DECK_GEOMETRY = NOT_APPROVED_AS_RUNTIME_NUMERICS
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```
