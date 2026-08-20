# [현행] OMENWARD · 3×3 Roulette Component Spec

```yaml
decision_id: OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_WORK_ORDER_AND_EXISTING_3X3_ARROW_CORE
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01
  - OMW-PLAN-20260820-BATTLEFIELD-SCALE-READABILITY-01
preserves:
  - APPROVED_ROULETTE_CORE_RULES
  - OMW-AMEND-20260804-HUD-ROULETTE-LAYOUT-AND-BATTLEFIELD-VIEW-V1
runtime_mutation: NONE
scene_mutation: NONE
human_validation: NOT_RUN
```

## 1. 결정

player-facing 룰렛은 **Compact Direct-Arrow 3×3 Workbench**를 사용한다.

```text
3×3 노출 보드 = 중심
각 열 위/아래 화살표 = 해당 릴 세로 이동
각 행 왼쪽/오른쪽 화살표 = 해당 행 가로 순환
Spin → 정지 Snapshot → 이동/예측 → 결과 확정
```

세 징조륜은 세계관/내부 구조이고, player-facing 핵심 조작면은 3×3 노출창이다. 세 릴을 세 전선과 1:1로 대응시키지 않는다.

## 2. 대안 검토

### A · Compact Direct-Arrow 3×3 — 채택

- 3×3 바로 옆에 12개 방향 화살표를 붙인다.
- mouse hover / controller focus가 대상+방향 선택과 preview를 동시에 담당한다.
- 실행 입력 시 이동권을 소비하고 즉시 확정한다.
- 전장을 계속 보면서 조작 가능하다.

### B · Wheel-first Expanded View — 비채택

세 원형 릴 전체를 크게 보여 world diegesis는 강하지만, 하단이 다시 커지고 3×3의 실제 조작 대상과 화살표가 멀어진다. 세 릴 상세는 요청 시 상세 레이어로만 허용한다.

### C · Full-screen Roulette Modal — 비채택

룰렛 뽕맛은 강할 수 있으나 전장/Forecast 맥락을 가리고 `전장이 메인` 계약을 위반한다.

## 3. 하단 점유와 기하

전체 하단 Control Deck contract:

```text
LOWER_DECK = 25~32% screen height exploration
ROULETTE_FOCUS_TARGET = 28~32%
REFERENCE = 960×540
```

3×3 보드 탐색치:

```text
TOKEN_TILE = 32~34 px
TILE_GUTTER = 2~3 px
BOARD_ONLY = 약 100~108 px
ARROW_VISIBLE_CORE = 20~22 px
ARROW_INPUT_TARGET = 24~28 px
BOARD_PLUS_ARROWS_HEIGHT = 약 146~154 px
```

정확 값은 North Star/Vertical Slice에서 재검증하며 runtime final geometry로 승인하지 않는다.

## 4. 화살표 배치

```text
      ↑      ↑      ↑

←  [A]    [B]    [C]  →
←  [D]    [E]    [F]  →
←  [G]    [H]    [I]  →

      ↓      ↓      ↓
```

- 위/아래 화살표는 각 세로 릴 바로 위/아래에 정렬한다.
- 왼/오른쪽 화살표는 각 가로 행 바로 좌/우에 정렬한다.
- 화살표만 보고 조작 대상과 이동 방향을 알 수 있어야 한다.
- 화살표가 토큰보다 작아 시각적으로 사라지지 않게 한다.

## 5. 입력과 preview

기존 `선택 → preview → 실행` 계약을 클릭 수 없이 유지한다.

### Mouse

```text
hover arrow
→ affected column/row 강조
→ ghost preview 표시
→ click
→ 이동 실행 + 자원 소비 + 즉시 확정
```

### Controller / Keyboard

```text
focus arrow
→ affected column/row 강조 + preview
→ confirm input
→ 이동 실행 + 자원 소비 + 즉시 확정
```

```text
UNDO_AFTER_EXECUTION = FORBIDDEN
RESET_SPINSESSION = FORBIDDEN
PREVIEW_DOES_NOT_SPEND = TRUE
```

## 6. 이동권 표시

이동권은 룰렛 전용 자원이며 룰렛 Focus 안에서만 주요 수치로 표시한다.

```text
Lucky Free Move = session-only
Stored Move Ticket = n / 3
CONSUME_LUCKY_FIRST = TRUE
```

표현 예:

```text
무료 이동 1
보관 이동권 2/3
```

- 하단 외의 상단 자원 HUD에 이동권을 중복하지 않는다.
- 이동 자원이 없으면 화살표는 disabled + 이유 표시.
- 구매 유도형 유료 Spin/이동권 UI는 사용하지 않는다.

## 7. SpinSession 시각 상태

### READY

```text
Spin cost
[룰렛 돌리기] = primary CTA
[결과 확정] = disabled
arrows = disabled until stopped snapshot exists
```

### SPINNING

```text
board motion / omen-wheel feedback
all manipulation input locked
```

### STOPPED / MANIPULATE

```text
natural 3×3 board visible
arrows active if move resource available
preview recalculated on focus/hover
result preview recalculated after each executed move
[결과 확정] available
[룰렛 돌리기] disabled until session resolved
```

### CONFIRMED

```text
immutable result / pending reward or confirmed no-reward result
transition to storage/sell/commit flow
```

## 8. 판정 가독성

기존 core 판정을 보존한다.

```text
PRIMARY_JUDGING_LINE = CENTER_HORIZONTAL_ROW
CENTER_ROW_X = no reward
CENTER_ROW_NON_X_MATCH = judging symbol locked
THEN_COUNT = all 8 lines of same judging symbol
```

UI:

- 중앙 가로줄은 평상시부터 **판정 기준선**임을 약하게 표시한다.
- 중앙줄 미완성 시 다른 줄이 우연히 맞아도 reward line처럼 강하게 점등하지 않는다.
- 중앙줄 성공 순간 judging symbol을 고정하고, 그 심벌로 완성된 전체 선을 순차 강조한다.

보상 등급:

```text
1 line = 일반
2 lines = 엘리트
3~7 lines = 영웅
8 lines / 9 cells same = 전설 또는 current cycle rule
```

## 9. Gold Token

Gold Token은 유닛 토큰과 같은 3×3 tile grammar를 사용한다.

```text
CENTER_ROW_GOLD_MATCH = gold judging symbol
line count = same 8-line calculation
1 line = 75% of actual spin cost
2 lines = 200%
3+ lines = 500%
```

금화는 현재 게임 HUD/보상에서 사용하는 동일한 금화 자산을 축소·크롭해 재사용한다. premium currency/gacha chest처럼 표현하지 않는다.

## 10. Token asset boundary

이 Decision은 token visual hierarchy를 상세 확정하지 않는다. 다음 Token Component spec에서 잠근다.

현재 보호:

```text
UNIT_TOKEN_USES_ACTUAL_UNIT_ART = TRUE
T1_T2_TOKEN_ART = ALLOWED_CURRENT_LINEAGE
ABSTRACT_WEAPON_ONLY_REPLACEMENT = NOT_DEFAULT
GOLD_TOKEN_USES_GAME_GOLD_ART = TRUE
X_TOKEN = CLEAR_NON_REWARD_STATE
```

## 11. 좌/중/우 작업대 정보 위계

낮은 하단에서 모든 정보를 계속 펼치지 않는다.

### Left compact

```text
Lucky Free Move
Stored Move Tickets n/3
optional collapse: reward-line rule help
```

### Center dominant

```text
3×3 board
row/column arrows
center judging-line cue
```

### Right action/result

```text
Spin cost
Spin CTA OR Result Confirm CTA
compact result preview
```

Bellu/Tier/rule explanation은 항상 고정 폭을 차지하지 않고 FTUE/도움말/상태에 따라 축소 또는 접을 수 있다.

## 12. Roulette DDD 연결

이 컴포넌트의 핵심 감정은:

```text
내 건물/TokenSource가 확률을 만들었다
→ 돌렸다
→ 거의 맞았다 / 맞았다
→ 내가 행/열을 직접 조작했다
→ 선이 잠겼다
→ 원하는 병력이 실제 획득됐다
```

따라서 화살표 이동과 line lock이 Spin 자체만큼 중요하게 느껴져야 한다.

연출 세부 수치/SFX/VFX는 후속 `ROULETTE_DDD_FEEDBACK_SPEC`가 소유한다.

## 13. 검증

```text
960×540
1280×720
1920×1080
```

PASS 후보:

- 3×3 토큰이 병종 단위로 판독됨.
- 12개 화살표의 대상/방향을 설명 없이 이해 가능.
- hover/focus preview와 실행 상태가 구분됨.
- 중앙 판정줄과 완성선 관계가 이해됨.
- 하단 때문에 세 전선이 잘리지 않음.
- 이동권/Lucky가 상단 자원과 중복되지 않음.
- Spin과 Result Confirm이 다른 행동임이 명확함.

## 14. 다음 작업 순서

```text
COMPLETE = 3X3_ROULETTE_COMPONENT_SPEC
CURRENT_NEXT = TOKEN_COMPONENT_SPEC
THEN = LOWER_CONTROL_DECK_SPEC
THEN = ROULETTE_DDD_FEEDBACK_SPEC
THEN = NEW_NORTH_STAR_ONE_IMAGE
THEN = COMPONENT_SHEET
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
THEN = IMPLEMENTATION_HANDOFF_AFTER_USER_AUTHORITY
```

## 15. 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE = UNCHANGED
RUNTIME = NOT_RUN
HUMAN_VALIDATION = NOT_RUN
FINAL_UI_PIXEL_GEOMETRY = NOT_APPROVED_AS_RUNTIME_NUMERICS
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```
