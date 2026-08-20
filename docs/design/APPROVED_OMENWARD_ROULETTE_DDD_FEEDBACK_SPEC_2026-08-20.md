# [현행] OMENWARD · Roulette DDD / Feedback Spec

```yaml
decision_id: OMW-PLAN-20260820-ROULETTE-DDD-FEEDBACK-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_ROULETTE_PLEASURE_AS_CORE_DDD_AND_RECOMMENDED_COMPONENT_WORK_ORDER
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01
  - OMW-PLAN-20260820-TOKEN-COMPONENT-01
  - OMW-PLAN-20260820-LOWER-CONTROL-DECK-01
runtime_mutation: NONE
scene_mutation: NONE
asset_production: NOT_STARTED
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD 룰렛의 핵심 DDD는 **Agency-First Tactical Crescendo**를 사용한다.

> 최고점은 `랜덤으로 좋은 게 떴다`가 아니라 **내가 설계한 동원 확률이 정지 보드로 드러나고, 내가 행/열을 조작해 판정선을 잠근 뒤 원하는 병력을 획득했다**는 감정이다.

```text
BUILD / TOKENSOURCE DESIGN
→ PRE-SPIN ANTICIPATION
→ SPIN
→ HONEST NATURAL STOP
→ PLAYER MANIPULATION
→ CENTER-LINE LOCK
→ COMPLETED-LINE CASCADE
→ RESULT REVEAL
→ STORAGE / COMMIT-QUEUE TRANSFER
→ LATER COMMIT CONFIRM
→ BATTLEFIELD DEPLOYMENT FEEDBACK
```

룰렛 획득과 전선 배치를 하나의 연출로 합치지 않는다.

## 2. 대안 검토

### A · Agency-First Tactical Crescendo — 채택

- Spin은 짧게 기대감을 만든다.
- 자연 정지 결과를 숨김없이 보여준다.
- 플레이어의 화살표 조작과 판정선 완성에 가장 강한 촉각/시각 피드백을 준다.
- line count가 늘수록 짧게 escalation한다.
- 전장 시야를 계속 유지한다.

### B · Cinematic Jackpot Burst — 비채택

- 큰 섬광, 장시간 보상 컷, 화면 흔들림, 보상 상자/잭팟 연출은 순간 자극은 강하나 전장을 가리고 카지노 판타지를 강화한다.

### C · Instant Tactical Snap — 비채택

- 조작/판정은 매우 빠르지만 기대→행동→반응의 감정 곡선이 약해 핵심 DDD를 충분히 살리지 못한다.

## 3. 핵심 원칙 · Player agency가 가장 크게 느껴져야 함

피드백 강도 우선순위:

```text
1. PLAYER MOVE THAT CREATES / IMPROVES RESULT
2. CENTER JUDGING-LINE LOCK
3. ADDITIONAL COMPLETED LINES
4. NATURAL SPIN STOP
5. PASSIVE DECORATIVE MOTION
```

- 자연 당첨도 만족스럽게 보여주되, **플레이어가 이동권으로 만든 성공**이 더 분명한 `snap / sigil trail / line lock` 피드백을 받는다.
- 보상 수치에는 숨은 조작 보너스를 추가하지 않는다. 차이는 표현과 agency confirmation에 한정한다.

## 4. 정직한 RNG / Near-miss 가드레일

```text
SCRIPTED_FAKE_NEAR_MISS = FORBIDDEN
RNG_RESULT_VISUAL_REORDER = FORBIDDEN
STOP_TIMING_THAT_CHANGES_PREDETERMINED_RESULT = FORBIDDEN
HIDDEN_PITY_PRESENTED_AS_PURE_LUCK = FORBIDDEN
```

- 실제 SpinSnapshot 정지 보드를 그대로 보여준다.
- `거의 맞았는데 일부러 한 칸 빗나간 것처럼` 연출하기 위해 결과를 재배열하지 않는다.
- Lucky가 발동하면 실제 시스템 상태인 `무료 이동`을 명시적으로 알려준다.

## 5. Timing planning envelope

아래 값은 feel prototype용 탐색 범위이며 final runtime timing이 아니다.

```text
PRE_SPIN_BUILDUP = 0.18~0.32 s
SPIN_VISIBLE_MOTION = 0.55~0.90 s
PER_REEL_STOP_STAGGER = 0.05~0.09 s
POST_STOP_READ = 0.10~0.18 s
ARROW_MOVE_SNAP = 0.10~0.18 s
CENTER_LINE_LOCK = 0.14~0.24 s
EXTRA_LINE_STEP = 0.06~0.10 s each
EXTRA_LINE_CASCADE_CAP = 0.45 s
RESULT_REVEAL = 0.22~0.40 s
RESULT_TO_STORAGE_TRANSFER = 0.18~0.32 s
```

Latency/pace target 후보:

```text
INPUT_PREVIEW_FEEDBACK = immediate / within one rendered frame target
LAST_MOVE_TO_CLEAR_RESULT_STATE = about <= 1.0~1.3 s exploration
NATURAL_SIMPLE_RESULT_TOTAL = about 1.1~1.8 s exploration
```

- 반복 플레이를 위해 모든 핵심 결과가 수초간 입력을 막지 않게 한다.
- rare capstone도 길게 전장을 가리는 cinematic으로 만들지 않는다.

## 6. Pre-spin anticipation

Spin 직전:

```text
Omen-wheel / sigil charge
very short audio rise
3×3 frame tension cue
Spin CTA depress / lock
```

- 전장 전체를 dim하거나 blur하지 않는다.
- 전장을 가리는 full-screen vignette를 기본 사용하지 않는다.
- 현재 TokenSource/확률 설계를 다시 계산하는 척하는 가짜 로딩은 금지한다.

## 7. Spin / stop

Spin 중:

- 세 릴의 수직 motion을 3×3 창에서 읽을 수 있게 한다.
- 릴 정지는 미세하게 stagger되어 각 열의 정지가 읽힌다.
- slot-machine lever/7/cherry/jackpot bell 문법은 사용하지 않는다.

Stop feedback:

```text
soft mechanical / sigil click per reel
brief tile settle
natural board fully readable before next manipulation
```

자연 정지 후 player manipulation이 가능해지는 시점을 명확하게 전환한다.

## 8. Arrow manipulation · DDD의 핵심 손맛

Hover/focus preview:

- 영향 받는 row/column에 `ghost destination`을 표시한다.
- 이동 후 중앙 판정선과 예상 line result를 실제 deterministic preview 범위에서 보여줄 수 있다.
- preview는 자원을 소비하지 않는다.

Execute:

```text
arrow press
→ selected row/column compress cue
→ tokens snap one step
→ origin/destination trail
→ move-ticket consume cue
→ result preview immediate recalc
```

- 전역 화면 흔들림보다 **해당 행/열의 국소적 snap**을 우선한다.
- 실행 후 undo/reset이 없으므로 `실행됨` 상태가 preview와 분명히 달라야 한다.

## 9. Center judging-line lock

중앙 가로줄이 동일 비-X 심벌로 완성되는 순간이 첫 payoff peak다.

연출:

```text
center row frame closes / locks
judging symbol sigil pulse
short low-to-high chord / impact
matching symbol outline stabilizes
```

- 중앙 판정줄 외 다른 줄을 먼저 크게 점등하지 않는다.
- 중앙줄 성공 전에 다른 우연한 match를 jackpot처럼 강조하지 않는다.

## 10. Completed-line cascade

판정 심벌이 고정된 뒤 같은 심벌의 완성선을 실제 line count에 따라 순차적으로 보여준다.

```text
1 line = compact lock / Common
2 lines = second crossing pulse / Elite
3~7 = short escalating cascade / Hero
8 / all 9 same = rare capstone / Legendary-or-current-cycle rule
```

- line count가 많을수록 sound/pulse layer를 추가하되 총 cascade 시간을 제한한다.
- reward grade는 line count 결과이며 hidden rarity roll처럼 연출하지 않는다.

## 11. Result reveal

### Unit

```text
matched token family
→ actual reward unit art expands into Result Preview
→ name / Tier / result grade / role
→ acquired state
```

Token → Result → Storage/Commit card가 같은 병종 시각 계보를 유지한다.

### Gold

- same in-game Gold art를 사용한다.
- payout 숫자는 짧게 강조한 뒤 **상단 Gold HUD로 tracer/number update**를 연결한다.
- 하단에 전체 Gold 총량을 새로 복제하지 않는다.

## 12. 획득과 전장 배치의 시각 분리

중요 계약:

```text
ROULETTE_UNIT_RESULT
→ ACQUIRED / STORAGE_OR_COMMIT_QUEUE
≠ AUTOMATIC_LANE_DEPLOYMENT
```

룰렛 결과 직후 병력을 실제 전장 lane으로 날려 보내지 않는다.

이유:

- 세 전선 중 하나를 고르는 비가역 COMMIT은 별도 player decision이다.
- 룰렛 결과가 자동으로 어느 lane에 들어간다는 오해를 막는다.

후속 COMMIT 확정 시에만:

```text
Commit card / unit marker
→ chosen lane deploy point
→ short reinforcement cue
```

를 사용한다.

## 13. Lucky feedback

Lucky는 자연 중앙줄 미당첨 때 실제 시스템이 제공하는 session 무료 이동이다.

표현:

```text
Omen sigil intervention
`무료 이동 +1` / equivalent player-facing copy
move resource state update
```

- `꽝이 사실 당첨으로 바뀌었다`처럼 표현하지 않는다.
- Lucky는 결과를 직접 지급하지 않고 **플레이어가 한 번 더 조작할 기회**를 준다는 agency를 강조한다.

## 14. Audio layers

후보 레이어:

```text
PRE-SPIN = short omen resonance rise
REEL_STOP = restrained mechanical/sigil tick
ARROW_MOVE = tactile ratchet / stone-metal snap
CENTER_LOCK = concise harmonic lock chord
EXTRA_LINE = additive short tone layers
UNIT_RESULT = role/faction neutral acquisition stinger
GOLD_RESULT = restrained coin / metal resonance
```

금지:

- casino bell / slot jackpot sound imitation.
- 긴 fanfare가 전투 audio를 덮는 구조.
- 반복 Spin마다 높은 피로도를 주는 과도한 고역대 SFX.

## 15. Camera / motion / VFX limits

```text
FULL_SCREEN_SHAKE = AVOID
LOCAL_BOARD_NUDGE = ALLOWED
BATTLEFIELD_AUTO_ZOOM = FORBIDDEN
FULL_SCREEN_WHITE_FLASH = FORBIDDEN
LONG_SCREEN_OBSCURE = FORBIDDEN
```

- board/CTA 영역의 micro-nudge/scale은 허용한다.
- rare capstone도 전장을 완전히 덮지 않는다.
- reduced-motion 옵션과 별개로 핵심 정보 전달은 motion 없이도 outline/line/color/value로 유지 가능해야 한다.

## 16. Repetition / fast-path

반복 플레이에서도 DDD를 유지하되 피로를 줄인다.

허용:

```text
shortened repeated spin buildup option
skip only nonessential tail of result flourish
fast controller/keyboard continuation after result becomes readable
```

금지:

- 결과를 읽기 전에 auto-skip.
- 중앙 판정/line count를 생략해 왜 등급이 나왔는지 알 수 없게 하는 fast mode.

## 17. Benchmark adaptation

채택 원리:

- animation의 `anticipation → action → reaction`: 상호작용을 읽히고 보상감 있게 만든다.
- game feel / rewarding visual / snap / SFX는 player input에 즉시 대응해야 한다.
- 과도한 juice는 context를 해칠 수 있으므로 게임의 군사 동원 장치 맥락에 맞는 피드백만 사용한다.
- tactical clarity가 멋보다 우선한다.

REFERENCE ONLY:

- 카드/스코어 게임의 hover jiggle·scale feedback처럼 작은 조작에도 즉각 반응하는 원리는 참고 가능하나, poker/casino 외형과 reward language는 가져오지 않는다.

## 18. 검증

Prototype 비교:

```text
natural no-reward
natural 1-line Unit
player-move-created 1-line
player-move-created 2-line
Hero multi-line
Gold 1/2/3+ line
Lucky triggered
Legendary/capstone state
reduced-motion mode
```

PASS 후보:

- 플레이어가 `내 조작 때문에 완성됐다`고 느낄 피드백이 존재.
- 중앙 판정선과 line count를 실제로 이해 가능.
- reward grade가 hidden random rarity로 오해되지 않음.
- 전장 시야를 잃지 않음.
- 결과 병력이 자동 lane 배치됐다고 오해하지 않음.
- 반복 Spin에서 피로/지연이 과하지 않음.
- casino/gacha/paid-spin 인상이 강화되지 않음.

## 19. 다음 작업 순서

```text
COMPLETE = ROULETTE_DDD_FEEDBACK_SPEC
CURRENT_NEXT = REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
THEN = COMPONENT_SHEET
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
THEN = IMPLEMENTATION_HANDOFF_AFTER_USER_AUTHORITY
```

## 20. 경계

```text
PRODUCT_CODE = UNCHANGED
SFX_VFX_ASSET_PRODUCTION = NOT_STARTED
SCENE = UNCHANGED
RUNTIME = NOT_RUN
HUMAN_VALIDATION = NOT_RUN
FINAL_FEEDBACK_TIMINGS = NOT_APPROVED_AS_RUNTIME_NUMERICS
IMAGE_GENERATION = USER_REQUEST_ONLY
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```
