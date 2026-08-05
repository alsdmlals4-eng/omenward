# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_2_OF_10
current_working_pr: 142
product_code_authority: NONE
```

## Planning Batch

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
[완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
[완료 3/10] 건물 6종 분기·카운터
[완료 4/10] 병종 역할·시너지·카운터
[완료 5/10] 전술스킬·마력
[완료 6/10] Stage 종료 상인
[진행 7/10] 첫 10~15분 흐름 — PARTIAL_APPROVAL_2_OF_10
[8/10] Hero·Legendary 재조정
[9/10] Meta·Hub 재조정
[10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```

## 6/10 Stage 종료 상인 결과

- Stage 1~19 종료 정비시간에만 상인이 방문한다.
- Stage 20 종료 뒤에는 상인이 아니라 MapRun 최종 정산으로 이동한다.
- 재고는 룰렛 제어·복구·성장 보조·가변 기회의 유한 4칸이다.
- 이동권이 3개 미만이면 이동권, 3/3이면 다음 룰렛 1회 할인을 제시한다.
- 구매 통화는 골드 하나다.
- 상인은 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기를 직접 판매하지 않는다.
- 상시 HUD 상점·전투 중 재진입·무한 구매·무한 reroll·할인 중첩은 금지한다.
- 정확 가격·재고 수·등장률·할인율과 거래 상태머신은 후속 시뮬레이션·Codex 계획 대상이다.

## 7/10 승인된 체크포인트

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10_IN_PROGRESS
PARTIAL_APPROVAL_2_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
STAGE_1 = CORE_CAUSAL_CHAIN_AND_FIRST_MERCHANT
STAGE_2 = ROULETTE_CONTROL_AND_MULTI_FRONT
STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC
STAGE_4 = FIRST_DANGER_INTEGRATION
STAGE_5 = FIRST_BOSS_MASTERY_CHECK
MERCHANT_FIRST_EXPOSURE = STAGE_1_MAINTENANCE
MERCHANT_FIRST_LESSON = OPTIONAL_GOLD_OPPORTUNITY_COST
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
```

첫 세션은 실제 MapRun이며 Stage 1에서 핵심 인과를 완성한 뒤 Stage 2 룰렛 통제, Stage 3 마력탑·연구·전술, Stage 4 Danger 통합, Stage 5 Boss 숙련으로 확장한다. 벨루는 설명자이며 플레이어의 핵심 선택을 대신하지 않는다.

## 7/10 남은 목표

- 첫 의미 있는 통치자 선택과 첫 건설 후보.
- 초반 최소 유효 경로 수.
- 벨루 개입 범위.
- Stage 4 Danger와 Stage 5 Boss의 정확 압력·패턴.
- 첫 실패 원인과 다음 선택을 설명하는 피드백.
- 첫 5 Stage의 강제 정답·필수 구매 방지.
- 실패·재시도·스킵·재학습 규칙.
- 사람 플레이 검증 시나리오와 Stop-ship 기준.

```text
FIRST_BUILD_CANDIDATES = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
FIRST_MEANINGFUL_RULER_CHOICE = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

## 구현 순서

```text
6/10 Stage 종료 상인 정본 완료
→ 7/10 첫 10~15분 흐름 승인 배치
→ 7/10 적대적 검토·사람 QA 계획 완료
→ Hero·Legendary / Meta·Hub 재조정
→ 전체 Run 종합 검토
→ 필요한 이미지·애니메이션·HX 승인 및 제작
→ 경제·수치 시뮬레이션
→ 별도 Codex 구현 계획
→ 제품 RED 테스트
→ 최소 구현
→ 런타임·사람 QA
```

제품 코드·Scene·Resource·게임 데이터·실제 아트 자산은 별도 승인 전 변경하지 않는다.

제품 구현: `NOT_STARTED`

## 7/10 TDD 상태

```text
CHECKPOINT_1_RED_RUN = 1009
CHECKPOINT_1_GREEN_RUNS = 1016 / 719 / 190 / 705
CHECKPOINT_2_RED_COMMIT = 540b821253a9819a51707e7e6294601889306ab0
CHECKPOINT_2_RED_RUN = 1022
CHECKPOINT_2_RED_RESULT = FAILURE_AS_EXPECTED
CHECKPOINT_2_GREEN = IN_PROGRESS
```

## 완료 Decision 계보

```text
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

## Legacy 자동 검증 증거

기존 기술 기준선·C1·C2·C3 자동 증거 확보

C1 승인 룰렛 핵심 계약 원격 검증·병합 완료

상태: **REMOTE_PROVEN**

```text
LEGACY_C1_C2_C3_PROVEN
```

위 증거는 과거 계약 검증만 의미하며 최신 7/10 기획의 제품 구현을 의미하지 않는다.
