---
name: omenward-core-loop-human-playtest
description: 오멘워드의 첫 10분 건설→룰렛→배치→3라인 역전 루프를 실제 플레이 관찰로 검증한다. C1U·C3 UX, 인간 플레이, 튜토리얼, HUD, 룰렛·전장·건설의 연결 또는 코어 루프 증명 상태를 계획·실행·판정할 때 사용한다.
---

# Omenward Core Loop Human Playtest

자동 테스트는 룰렛·전투 계약이 작동함을 보여도, 플레이어가 전선을 읽고 건물로 확률을 설계한 뒤 획득 유닛을 배치해 역전했다고 이해했음을 증명하지 않는다. 이 Skill은 그 차이를 관찰 가능한 플레이 증거로 바꾼다.

## Read first

`AGENTS.md` → `docs/PROJECT_CORE.md` → `docs/CURRENT_IMPLEMENTATION_STATUS.md` → `docs/HANDOFF_CONTEXT.md` → 관련 APPROVED 룰렛·전장·UX 문서 → 현재 build·Scene·test.

## Test question

첫 10분 안에 신규 플레이어가 다음 사슬을 두 번 스스로 연결하는가?

`전조·라인 위협 인식 → 건물/토큰 또는 전술 선택 → 룰렛 결과 이해 → 보관 유닛 배치 → 접전지·거점·성문 결과 확인 → 다음 공세를 위한 설계 변경`

각 세션에서 한 가지 가설만 우선 검증한다. 예: 건물이 룰렛 확률을 바꾼다는 인식, 3라인 중 우선 대응의 이유, 이동권/상위 등급 보상의 이해, 암살자 우회로의 위험 읽기.

## Session contract

| Field | Define |
|---|---|
| Build and seed | exact branch, build, StageManifest, seed, known issue |
| Participant | prior genre exposure and prior project exposure |
| Task | player goal stated without solution language |
| Expected decision | one observable choice that tests the hypothesis |
| Evidence | screen recording, event log, action timing, short think-aloud or post-task explanation |
| Guardrail | frustration, inaccessible input, unreadable HUD, bug, or facilitator leakage |
| Pass rule | behavior and explanation that must both occur |
| Stop rule | when a bug or missing prerequisite invalidates the observation |

Do not use a scripted win, a facilitator’s instruction, or a one-time lucky roulette result as core-loop proof.

## Observation protocol

1. Show the normal strategy view with no mini-map replacement or hidden developer tags.
2. Ask the player to identify the most urgent lane and explain the next action before clicking.
3. Observe whether the player connects a building or token change to the next roulette result.
4. Observe whether the player can choose a lane for the acquired unit and predict the intended effect.
5. At a contested point, ask why the result changed; compare the explanation with authoritative combat and ownership events.
6. At the next warning, check whether the player changes the plan using the previous result rather than repeating a memorized action.
7. Record a short post-session explanation of the loop and a single point of confusion.

## Interpretation

Classify each finding as:

- `LOOP_PROVEN`: behavior and explanation show the required causal link.
- `UX_GAP`: the underlying rule works, but information hierarchy, feedback, or input prevents correct understanding.
- `RULE_GAP`: the player understands the UI but cannot make a meaningful decision.
- `CONTENT_GAP`: the scenario fails to create a readable contrast or consequence.
- `TECHNICAL_BLOCKED`: build, performance, input, or bug invalidates the session.
- `NOT_RUN`: no human evidence exists.

Never promote C1/C2 automated verification to `CORE_LOOP_PROVEN` without human-play evidence.

## Output

Report the hypothesis, participant context, build/seed, observed choices, explanation evidence, failures, result classification, exact document/status updates, and the smallest follow-up change. Keep untested values and unobserved accessibility or performance claims as `NOT_RUN`.

## Failure conditions

- Treating a successful test script as player comprehension.
- Guiding the player to the correct building, roulette move, or lane.
- Replacing the three-line strategy view with a mini-map or exposing developer threat labels.
- Changing several rules and UI elements before the next observation.
