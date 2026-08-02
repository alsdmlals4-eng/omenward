# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: FIRST_FIVE_HERO_UNIQUE_SKILL_2_CONCEPTS_APPROVED
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
last_merged_planning_pr: 127
base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 7
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 최신 사용자 결정

Decision ID:

`OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1`

```text
방패병 → 불퇴의 성벽
궁병   → 천공 소거
사제   → 생명의 서약
마법사 → 메테오
암살자 → 그림자 분신
```

사용자 직접 수정:

- 사제는 회복이 아니라 `최소 체력 이하로 떨어지지 않게 하는 효과`다.
- 마법사는 밀집 폭발 일반형이 아니라 `메테오`다.
- 암살자는 고가치 표적 처형 단발기가 아니라 `분신 생성`이다.
- 앞으로 Grill Me 질문·작업은 상용 게임 벤치마크와 현업 제작 비교·권장안을 포함한다.

## 2. 고유 2스킬 핵심 계약

### 불퇴의 성벽

- 같은 전선의 붕괴 직전 전열을 짧게 유지한다.
- 새 지형·건물·navmesh 없이 방벽 효과가 정해진 피해 예산을 흡수한다.
- 영구 경로 변경·전선 전체 무적은 금지한다.

### 천공 소거

- 같은 전선의 유효 비행 표적이 임계치를 넘으면 동시 일제사격한다.
- 지상·건물·다른 전선을 공격하지 않는다.
- 표적이 없으면 cooldown을 소비하지 않고 READY를 유지한다.

### 생명의 서약

```text
effective_floor_per_target
= min(current_hp_at_cast, configured_floor_percent * max_hp)
```

- 짧은 지속시간 동안 같은 전선의 생존 아군 전투 유닛이 유효 하한 아래로 떨어지지 않는다.
- 발동 시 체력을 올리지 않는다.
- 회복·부활·건물/성문/타워 보호·적 보호·종료 시 저장 피해 적용은 없다.

### 메테오

- 같은 전선에서 deterministic 적 밀집 중심을 선택한다.
- 지면 경고와 낙하 예고 후 메테오 1개가 확정 지점에 떨어진다.
- `CAST_COMMIT` 뒤 적 이동으로 회피할 수 있다.
- 즉발·전역·다중 메테오·기본 지속 장판은 금지한다.

### 그림자 분신

- 같은 전선에 유효한 후열 고가치 표적이 있을 때 종속 분신 1체를 생성한다.
- 분신은 원본 암살자의 현재 표적과 기본 공격 일부만 복제한다.
- 독립 target selection·pathfinding·스킬·패시브·CC·보상 생성·body blocking·전선 이동은 없다.
- 전역 영웅 이상 슬롯을 점유하지 않는 owner-bound non-targetable combat proxy가 기본안이다.

## 3. 공통 발동·파워 경계

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 유효 조건·대상·priority·tie-break
→ 발동 직전 재검증
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

```text
ONE_LANE
ONE_PRIMARY_TACTICAL_PURPOSE
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
```

- 다섯 능력은 표준 영웅의 2스킬 슬롯을 교체한다.
- 추가 세 번째 스킬·패시브·숨은 보너스는 없다.
- 정확 cooldown·trigger·duration·damage·floor·clone coefficient는 pending이다.

## 4. 기존 등급·전역 슬롯 결정

```text
표준 [영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
표준 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 고유 3스킬
```

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 표준 영웅·해금 영웅·표준 전설·향후 해금 전설 모두 같은 전역 슬롯을 공유한다.
- 제한은 룰렛 획득이 아니라 전장 배치에 적용한다.
- 슬롯 충돌 토큰은 보관·판매하며 자동 삭제·강제 교체하지 않는다.
- 같은 Stage의 재전설 결과는 동일 계열 영웅 등급 보상 토큰 2개이며 즉시 유닛 2명을 만들지 않는다.

## 5. 벤치마크·현업 비교 정책

Process ID:

`OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1`

앞으로 모든 Grill Me에는 다음을 포함한다.

1. 현행 Project Core·정본 근거.
2. 공식 상용 게임·개발 자료 중심 직접 사례 2~4개.
3. 장르·조작·전투 규모·세션 구조 차이.
4. 구현·데이터·AI·pathfinding·animation·VFX/SFX·UI·save/load·determinism·QA 비교.
5. 적대적 검토와 복제 금지 경계.
6. 2~4개 선택지·제작비·검증비·권장안.

이번 Decision의 비교 사례는 Braum 방패 역할, Diablo III 광역 화살 사건, Kindred 체력 하한, Wild Rift Meteor, Zed의 제한된 그림자 proxy와 Riot의 clarity/counterplay 원칙이다. 이는 설계 복제가 아니라 실패 경계와 제작 방법을 비교하기 위한 자료다.

## 6. 코어 적합성

핵심 재미:

> 건물을 지어 룰렛의 미래를 바꾸고, 예고된 위기에 맞는 희귀 병력을 얻어 어느 전선에 비가역 커밋할지 결정한 뒤 전황을 뒤집는다.

전역 고등급 슬롯은 영웅·전설을 누적 전력으로 만들지 않고 세 전선 중 하나에 최고 전력을 투입하는 기회비용을 만든다. 초기 다섯 고유 2스킬은 각 병종 역할을 한 전선에서 확대하고, 별도 독립 시스템을 만들지 않는다.

주요 위험:

- 생명의 서약이 광역 무적이나 숨은 회복으로 변하는 것.
- 메테오가 즉발로 대응 불가능하거나 지나치게 빗나가 보상감이 사라지는 것.
- 그림자 분신이 신규 AI·유닛·저장 시스템으로 팽창하거나 스킬·CC를 복제하는 것.
- 방벽이 navmesh를 변경하는 것.
- 천공 소거가 비행 Wave를 혼자 무조건 삭제하는 것.
- 고유 2스킬이 표준 전설 전체 키트보다 강해지는 것.

상세 검토: `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`.

## 7. 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md`
- `docs/design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_REPEAT_LEGENDARY_RESULT_HIGH_GRADE_SLOT_RESOLUTION_2026-08-02.md`
- `docs/process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`
- `docs/reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`

## 8. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_HERO_IDENTITIES = PENDING
UNIQUE_SKILL_2_CONCEPTS = APPROVED
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_COOLDOWNS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
FINAL_DISPLAY_NAMES = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
REPEAT_LEGENDARY_STORAGE_OVERFLOW_POLICY = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

다음 우선 결정:

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
```

검토 주제는 초기 다섯 고유 2스킬의 공통 cooldown·충전 방식·READY 유지·발동 실패와 재예약 정책이다. 벤치마크·현업 비교 정책을 적용해 질문한다.
