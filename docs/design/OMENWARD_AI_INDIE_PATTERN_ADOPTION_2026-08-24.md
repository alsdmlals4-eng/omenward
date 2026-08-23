# OMENWARD · AI Indie Pattern Adoption — 2026-08-24

```yaml
status: USER_DIRECTED_ADAPTATION
work_mode: PLAN
runtime_mutation: NONE
balance_mutation: NONE
source_base_merge: dff09d83c3892a70ba5fee86a59d36086889a6c5
source_radar: docs/knowledge/game-development/AI_GAME_AND_AI_ASSISTED_INDIE_RADAR.md
source_pattern_pack: docs/knowledge/game-development/reuse/AI_ASSISTED_INDIE_PATTERN_PACK_2026-08-24.md
project_authority: docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md
human_validation: NOT_RUN
player_experience_validation: NOT_RUN
```

## 1. 목적

AI-assisted 1인 개발 사례와 Slotbound 계열 확률 설계 사례에서 확인한 패턴을 OMENWARD의 현재 정체성에 맞게 흡수한다. 외부 게임의 룰렛 표현이나 기능을 복제하지 않는다.

OMENWARD의 현재 인과는 다음이 우선한다.

```text
Forecast / Omen Signature
→ 건물 선택
→ 미래 Mobilization Distribution 변화
→ Triple Omen Wheels 병력 획득
→ 전선 선택
→ 비가역 배치
→ 전투 결과
→ 다음 Stage 판단
```

## 2. 판정표

| Base pattern | OMENWARD 판정 | 적용 |
|---|---|---|
| HUMAN_DIRECTED_AI_BUILD_LOOP | ADOPT | 구현은 bounded change → changed-surface review → test/run → accept/revise/revert 순서 |
| SILENT_OMISSION_GATE | ADOPT | 건물/TokenSource/Forecast/UI 소비자 누락을 변경 후 별도 공격 |
| CONTEXT_SCOPE_AND_ARCHITECTURE_BUDGET | ADOPT | Building / TokenSource / Roulette / Lane / Result owner를 섞지 않음 |
| BREADTH_AFTER_CORE_IDENTITY_LOCK | ADOPT | Stage 1~5 causality가 Human QA되기 전 추가 룰렛 변형/콘텐츠 breadth 확대 금지 |
| PLAYER_FEEDBACK_REBUILD_LOOP | ADOPT | 첫 세션 Human evidence가 핵심 인과를 못 전달하면 숫자보다 구조/설명 재검토 |
| AI_VISIBLE_OUTPUT_QUALITY_GATE | ADOPT | 추후 생성형 시각물도 기존 아트/권리/가독성 Gate 동일 적용 |
| RNG_AGENCY_AND_RECOVERY | ADAPT | `PROBABILITY_AGENCY_AND_COMMITMENT`로 변형 |
| runtime generative AI | REJECT_CURRENT | 현재 플레이어 가치에 필수 아님 |

## 3. 핵심 변형 · PROBABILITY_AGENCY_AND_COMMITMENT

Slotbound에서 재사용할 것은 슬롯 UI가 아니라 `불확실성을 선택으로 바꾸는 구조`다. OMENWARD에서는 그 선택이 **결과 후 되돌리기**가 아니라 **결과 전 확률 설계와 결과 후 책임 있는 커밋**이어야 한다.

```text
Forecast를 읽음
→ 현재 Mobilization Structure 이해
→ 건물/T2 후보 비교
→ 미래 분포 방향을 의도적으로 편집
→ 룰렛 결과 획득
→ 획득 병력을 현재 세 전선 맥락에서 해석
→ 하나의 전선에 비가역 커밋
→ 결과를 causal review에서 복기
→ 다음 Stage의 확률 설계에 학습 반영
```

### 명시적 금지

다음을 이번 패턴 흡수의 명목으로 추가하지 않는다.

- 무료 reroll
- 결과 후 unit lock으로 룰렛 결과 취소
- 획득 병력의 무비용 재추첨/교환
- 비가역 전선 배치 취소
- 세 Omen Wheel을 세 Lane과 동일시
- AI가 다음 최적 건물/전선을 자동 추천
- AI가 authoritative probability/state를 직접 수정

`SPECIAL_T1_FREE_REROLL = FORBIDDEN`과 기존 irreversible deployment를 유지한다.

## 4. 선택 가독성 Gate

### Stage 2 전 확률 변경

T2 Preview는 현재 계약을 유지하면서 다음 질문에 답할 수 있어야 한다.

```text
지금 무엇이 나올 수 있는가?
이 후보를 선택하면 어떤 방향이 상대적으로 늘거나 줄어드는가?
왜 이 변화가 현재 Forecast에 의미가 있는가?
어떤 결과까지는 여전히 불확실한가?
```

정확한 최종 퍼센트가 아직 승인되지 않았다면 가짜 숫자를 만들지 않는다. 상대 방향·TokenSource 변화·획득 경로만 정직하게 표현한다.

### 룰렛 결과 후

결과가 나쁘게 느껴져도 즉시 삭제/재추첨 버튼으로 없애지 않는다. 대신 플레이어에게 다음 판단을 준다.

```text
무엇을 얻었는가
→ 어느 Lane에서 가장 덜 나쁜/가장 의미 있는가
→ 지금 커밋하면 어떤 위험을 감수하는가
→ 다음 Stage에서 어떤 확률 설계를 바꿀 것인가
```

즉 OMENWARD의 recovery는 `undo`가 아니라 `learning → next-distribution adjustment`다.

## 5. PLAYER_FEEDBACK_REBUILD_LOOP 적용

Release-near 첫 세션에서 다음을 구분한다.

```text
BUG
CLARITY
BALANCE
CORE_CAUSALITY_FAILURE
```

- BUG → local fix.
- CLARITY → Forecast/Preview/Result causal feedback 개선.
- BALANCE → simulation + same-seed comparison.
- CORE_CAUSALITY_FAILURE → 건물 수치 미세조정보다 `build → distribution → obtain → commit → result` 전달 구조 자체를 다시 검토.

Stage 1의 여섯 T1 건물은 현재 유지한다. Human evidence에서 첫 룰렛 전 인과 이해 실패가 반복될 때만 기존 revisit condition을 연다.

## 6. 구현 후보 · 다음 Codex 범위

현재 이 문서는 런타임 변경을 승인하지 않는다. 다음 제품 Task가 열릴 때 아래 순서로만 소비한다.

1. Stage 2 T2 Preview의 causal information audit.
2. Roulette result → lane commitment 화면의 decision-information audit.
3. Post-stage review가 `forecast → distribution → commitment → decisive event → response → outcome`을 복원하는지 확인.
4. 확률 관련 변경은 deterministic seed/replay + Balance Scenario 비교.
5. Human first-contact에서 플레이어가 “운빨”이 아니라 “내가 확률을 설계했다”고 설명하는지 검증.

## 7. 성공/폐기 조건

### 유지

플레이어가 다음을 자기 말로 설명할 수 있으면 유지한다.

> Forecast를 보고 건물을 골라 앞으로 나올 병력 분포를 바꿨고, 나온 병력을 어느 전선에 쓸지 책임지고 결정했다.

### 재검토

- 건물 선택과 룰렛 결과의 인과를 연결하지 못함.
- 룰렛을 완전한 운으로만 인식함.
- 결과 후 취소/재추첨이 없어서가 아니라 정보 부족 때문에 억울함을 느낌.
- Stage 2 Preview가 사실상 정답 추천으로 작동함.
- 세 Wheel과 세 Lane을 반복 혼동함.

## 8. Implementation Reality Gate

현재 주장 가능:

- Base 패턴이 OMENWARD 현재 정본에 맞게 변형되어 문서화됨.
- 기존 무료 reroll 금지와 irreversible commitment를 보존함.
- 다음 구현/QA에서 검사할 decision-quality 계약이 정의됨.

현재 주장 불가:

- 확률 UI가 실제로 이해되기 쉬움.
- 룰렛이 더 재미있어짐.
- Stage 1~5 Human QA 통과.
- 최종 확률/비용/간격 승인.
- runtime generative AI 도입.

## 9. 적대적 검토 5회

1. **복사 공격** — Slotbound reroll/lock을 그대로 가져오지 않고 OMENWARD의 사전 확률 설계와 비가역 커밋으로 변형: PASS.
2. **정체성 공격** — 룰렛을 카지노 보상 장치로 만들지 않고 player-constructed probability의 결과 확인 장치로 유지: PASS.
3. **인과 공격** — 인기 사례를 성공 원인으로 간주하지 않고 선택 구조만 흡수: PASS.
4. **구현 공격** — exact probability/UI/Human evidence가 아직 없으므로 runtime PASS 주장 금지: PASS.
5. **과잉기능 공격** — 새 화폐, reroll, AI 추천, 별도 확률 엔진 추가 없음: PASS.

`CLEAN_REVIEW_EXIT`.
