# [승인] OMENWARD Whole-Project Content Closure

```yaml
updated_at: 2026-08-11
decision_id: OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1
status: APPROVED_CURRENT_PRODUCT_AUTHORITY
approval_source: USER_EXPLICIT_APPROVAL_OF_RECOMMENDED_NINE_DECISIONS
work_phase: PHASE_A_GPT_CHAT_PLANNING
product_code_authority: NONE
phase_b: NOT_RUN
phase_c: BLOCKED
```

## 1. 장르 분류

현재 OMENWARD의 제품 장르 정본은 다음과 같다.

```text
PRIMARY_GENRE = ROGUELITE_STRATEGY_AUTO_BATTLER
MECHANICAL_SUBGENRE = ROULETTE_PROBABILITY_BUILDER
SUPPORTING_DESCRIPTORS = TACTICAL_LANE_DEPLOYMENT / ENGINE_BUILDING / RESOURCE_MANAGEMENT / MANUAL_TACTICAL_SKILL_TIMING
MARKETING_SHORT = 룰렛을 설계해 군대를 만드는 로그라이트 전략 오토배틀러
PURE_SLOT_GAME = AVOID_POSITIONING
PURE_TOWER_DEFENSE = AVOID_POSITIONING
PURE_RTS = AVOID_POSITIONING
STANDARD_CARD_DECKBUILDER = AVOID_POSITIONING
```

핵심 차별점은 **건물이 확률 Source를 만들고 → 플레이어가 룰렛을 설계하며 → 룰렛 결과가 병력 획득으로 이어지고 → 비가역 전선 배치와 수동 전술 타이밍이 그 확률 설계를 전투 인과로 변환한다**는 점이다.

## 2. 작업 전 벤치마킹 결과

2026-08-11 현재 공식 상점/제품 설명을 기준으로 비교했다. 비교는 정본을 대체하지 않고 현재 결정의 검증 근거로만 사용한다.

| 비교작 | 관찰 | 처분 | OMENWARD 적용 |
|---|---|---|---|
| Mechabellum | 병력 draft·formation·counter와 손속도보다 판단을 강조하는 auto-battler | ADAPT | 전선 배치·카운터·결과 설명 가능성을 강화하되 PvP 구조는 복제하지 않는다. |
| The Last Flame | run 기반의 roguelike auto-battler, build·synergy·decision 중심 | ADAPT | run identity와 build causality를 참고하되 party-RPG 구조는 복제하지 않는다. |
| Spin Hero | reel을 돌리고 symbol pool을 구축하는 roguelike deckbuilder | ADAPT | reel이 운만 소비하는 장치가 아니라 플레이어가 구축하는 확률 엔진이어야 한다. |
| Luck be a Landlord | slot machine 자체의 symbol composition을 구축하는 roguelike deckbuilder | ADAPT | 확률 구성 agency를 참고하되 slot 자체가 최종 목적이 되는 제품 포지셔닝은 피한다. |
| Backpack Battles | 전투 전 구매·제작·배치가 승부를 만드는 inventory auto-battler | ADAPT | 전투 전 설계와 공간/배치의 인과를 강화한다. |
| CloverPit | 확률·slot 규칙 조작과 meta progression | TEST / AVOID | 확률 조작의 가독성은 실험하되 gambling/horror identity와 무제한 snowball은 제품 정체성으로 채택하지 않는다. |

```text
BENCHMARK_COPY_COMPETITOR_RULES = FORBIDDEN
BENCHMARK_PURPOSE = DECISION_STRESS_TEST_AND_DIFFERENTIATION
```

## 3. 승인 결정 1 — Building T3 공통 문법

```text
BUILDING_T3_GRAMMAR = SINGLE_CAPSTONE_DEEPENS_SELECTED_T2_IDENTITY
BUILDING_T3_REBRANCH = FORBIDDEN
```

T3는 T2에서 선택한 전략 정체성을 한 단계 깊게 만드는 최종 capstone이다. T3에서 다시 A/B 분기를 만들지 않는다. T2를 핵심 발전 선택으로 유지하고 설명·밸런스·콘텐츠 조합 폭발을 방지한다.

## 4. 승인 결정 2 — 일반병 병영 T3

```text
GENERAL_BARRACKS_T3 = ONE_ROLE_DEEPENING_CAPSTONE_PER_SELECTED_T2_ROLE
GENERAL_BARRACKS_T3_NEW_TROOP_BRANCH = FORBIDDEN
GENERAL_BARRACKS_T3_NEW_TOKEN_SOURCE_GRAMMAR = FORBIDDEN
ARCHER_T3 = CROSSBOW_ARCHER / RAPID_FIRE_ARCHER
```

방패·대검·창·궁병·기병은 각각 기존 역할을 강화하는 capstone을 갖는다. 새 병종 계열이나 새 TokenSource 문법을 T3에서 도입하지 않는다. 궁병은 후속 승인 계보 `CROSSBOW_ARCHER / RAPID_FIRE_ARCHER`를 보존한다. 정확 수치와 일부 역할별 세부 scalar는 runtime/balance evidence에서 확정한다.

## 5. 승인 결정 3 — 방어탑 T3

```text
DEFENSE_TOWER_T2 = ARTILLERY / DEFENSE_ENHANCEMENT / SNIPER
DEFENSE_TOWER_T3 = ONE_DETERMINISTIC_CAPSTONE_PER_T2_IDENTITY
DEFENSE_TOWER_T3_REBRANCH = FORBIDDEN
```

포격은 광역 압력, 방어강화는 버티기/전선 유지, 저격은 고가치 단일 제거의 정체성을 끝까지 유지한다.

## 6. 승인 결정 4 — 직선 강화 건물 T3

```text
LINEAR_T3_BUILDINGS = VAULT / FARM / COMMAND_POST / MANA_TOWER
LINEAR_T3_NEW_SUBSYSTEM = FORBIDDEN
LINEAR_T3_EFFECT = DEEPEN_EXISTING_PRIMARY_FUNCTION
```

금고·농장·지휘소·마력탑 T3는 기존 주기능을 강화한다. T3 하나 때문에 별도 신규 subsystem을 학습하게 만들지 않는다.

## 7. 승인 결정 5 — 방어강화 계열 최종 표시명

```text
DEFENSE_T2_DISPLAY_NAMES = 포격탑 / 요새탑 / 저격탑
DEFENSE_ENHANCEMENT_DISPLAY_NAME = 요새탑
```

카드·HUD에서 역할을 즉시 읽을 수 있도록 방어강화 계열 최종 표시명은 `요새탑`으로 확정한다.

## 8. 승인 결정 6 — Hero 전략 역할

```text
HERO_STRATEGIC_ROLE = CONTEXTUAL_AMPLIFIER
HERO_ERASE_BAD_ROULETTE_OR_FRONTLINE_COMMIT = FORBIDDEN
HERO_UNIVERSAL_ANSWER_BUTTON = FORBIDDEN
```

Hero는 잘 설계한 룰렛·전선·전술 타이밍을 상황에 맞게 증폭한다. 잘못된 편성이나 비가역 전선 선택을 무효화하는 리셋/정답 버튼이 아니다.

## 9. 승인 결정 7 — Hero 투입 규칙

```text
HERO_SELECTION_PER_MAPRUN = 1
HERO_SELECTION = BOUNDED_MAPRUN_COMMITMENT
HERO_STAGE_BY_STAGE_FREE_SWAP = FORBIDDEN
```

한 MapRun에서 Hero 한 명을 선택해 run identity로 커밋한다. Stage마다 자유롭게 바꾸며 하드카운터를 맞추는 구조는 금지한다.

## 10. 승인 결정 8 — Legendary 문법

```text
LEGENDARY_GRAMMAR = RARE_CONSTRAINED_SIDEGRADE
LEGENDARY_REQUIRES_EXPLICIT_ADVANTAGE_AND_COST_OR_CONSTRAINT = TRUE
LEGENDARY_PLAIN_RAW_STAT_SUPERIOR_TIER = FORBIDDEN
```

Legendary는 강한 장점과 명확한 비용·조건을 동시에 가진 희귀 sidegrade다. 존재만으로 일반 시스템과 기존 선택을 무효화하는 단순 상위 스탯 등급으로 만들지 않는다.

## 11. 승인 결정 9 — Meta·Hub 철학

```text
META_HUB_PROGRESSION = HORIZONTAL_CONTEXTUAL
META_PRIORITY = INFORMATION_UNLOCK / CHOICE_BREADTH / CHALLENGE_VARIANTS / RECORDS_COLLECTION / CONVENIENCE
PERMANENT_PURE_COMBAT_STAT_ACCUMULATION = FORBIDDEN
MANDATORY_GRIND_CURRENCY = FORBIDDEN
HUB_REPLACES_IN_RUN_DECISION = FORBIDDEN
```

Hub는 다음 Run을 더 잘 이해하고 더 다양한 선택을 하게 하는 레이어다. 영구 전투력 누적이나 반복 노동형 필수 재화를 통해 Run 내부 의사결정을 대체하지 않는다.

## 12. 기존 HELD 문서 처리

Hero/Legendary 및 Meta/Hub의 과거 상세 문서는 역사·아이디어·검토 근거로 보존한다. 이 Decision은 **제품 수준의 현재 high-level grammar를 승인**하지만 과거 상세 kit, exact 숫자, 과거 meta power 값 전체를 자동 재활성화하지 않는다.

```text
HELD_REFERENCE_LINEAGE_NOT_CURRENT_EXACT_IMPLEMENTATION_AUTHORITY
OLD_HERO_EXACT_KITS_AUTO_REACTIVATION = FORBIDDEN
OLD_META_EXACT_POWER_VALUES_AUTO_REACTIVATION = FORBIDDEN
```

## 13. Phase A 상태

세 genuine semantic decision group은 이 Decision으로 닫힌다.

```text
WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0
WHOLE_PROJECT_CONTENT_DECISIONS = CLOSED_PENDING_USER_PLANNING_COMPLETE_DECLARATION
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN
PHASE_C_BLOCKED
```

다음 항목은 제품 의미 미정으로 재분류하지 않는다.

```text
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
FINAL_FV_AND_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
```

이 Decision의 승인은 별도 literal `기획 완료` 선언이 아니다.
