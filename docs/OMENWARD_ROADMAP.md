# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_3_OF_10
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
[진행 7/10] 첫 10~15분 흐름 — PARTIAL_APPROVAL_3_OF_10
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
PARTIAL_APPROVAL_3_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
INITIAL_T1_BUILDINGS = PREBUILT
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_CONSTRUCTION_TUTORIAL = FORBIDDEN
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
FIRST_MEANINGFUL_RULER_CHOICE = T2_UPGRADE_AND_IRREVERSIBLE_DEPLOYMENT
T2_UPGRADE_PREVIEW = REQUIRED
STAGE_1 = PREBUILT_T1_TO_T2_AND_DEPLOYMENT_CAUSAL_CHAIN
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

첫 세션은 실제 MapRun이다. T1 건물은 기본 배치·짧은 역할 설명으로 처리하고, 첫 중요한 판단은 T2 업그레이드 방향과 병력의 비가역 배치다. 이후 Stage 2 룰렛 통제, Stage 3 마력탑·연구·전술, Stage 4 Danger 통합, Stage 5 Boss 숙련으로 확장한다.

## 7/10 남은 목표

- 첫 세션에 보여줄 T1 인스턴스 수·위치와 첫 T2 후보.
- 초반 최소 유효 경로 수.
- 벨루 개입 범위.
- Stage 4 Danger와 Stage 5 Boss의 정확 압력·패턴.
- 첫 실패 원인과 다음 선택을 설명하는 피드백.
- 첫 5 Stage의 강제 정답·필수 구매 방지.
- 실패·재시도·스킵·재학습 규칙.
- 사람 플레이 검증 시나리오와 Stop-ship 기준.

```text
INITIAL_T1_INSTANCE_COUNT = PENDING_GRILLME
FIRST_T2_UPGRADE_CANDIDATES = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
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
CHECKPOINT_2_RED_RUN = 1022
CHECKPOINT_2_GREEN_RUNS = 1040 / 742 / 214 / 728 / 9
CHECKPOINT_3_RED_COMMIT = 6004f3fd3bfef75281aaaa4e59e79567de4abdb3
CHECKPOINT_3_RED_RUN = 1041
CHECKPOINT_3_RED_RESULT = FAILURE_AS_EXPECTED
CHECKPOINT_3_GREEN = IN_PROGRESS
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
LEGACY_C1_C2_C3_PROVEN
```
