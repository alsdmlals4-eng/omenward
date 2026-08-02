# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_UNIQUE_SKILL_2_COOLDOWN_POLICY_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 8
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 승인 기획은 Draft PR #129에 누적하며 제품 구현 권한은 없다.

## 1. 제품 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 세 전선 공세 읽기
→ 건물·TokenSource로 릴 설계
→ 룰렛 조작·확정
→ 희귀 병력 획득
→ 어느 전선에 비가역 배치할지 판단
→ 자동전투·점령·건물 운영으로 전황 역전
→ 다음 Stage 설계에 환류
```

현재 제품은 Legacy 프로토타입이며 최신 승인 기획은 미구현이다.

## 2. 등급·전역 슬롯

```text
[일반] = 1스킬
[엘리트] = 강화된 1스킬
[영웅] = 강화된 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화된 1스킬 + 고유 2스킬
[전설] = 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 표준 영웅·해금 영웅·표준 전설·향후 해금 전설은 전장 전체 슬롯 하나를 공유한다.
- 제한은 획득이 아니라 배치에 적용한다.
- 슬롯 충돌 토큰은 보관·판매한다.
- 같은 Stage의 재전설 결과는 동일 계열 영웅 등급 보상 토큰 2개다.

## 3. 초기 해금 영웅 5명

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

- 불퇴의 성벽: 새 지형 없이 피해 예산을 흡수하는 짧은 전열 방벽.
- 천공 소거: 같은 전선의 유효 비행 표적 동시 일제사격.
- 생명의 서약: 발동 시 회복 없이 짧은 체력 하한 보호.
- 메테오: 적 밀집 지점에 예고 후 단발 지연 낙하.
- 그림자 분신: 독립 AI 없이 기본 공격 일부를 복제하는 owner-bound proxy 1체.

## 4. 승인된 공통 cooldown·charge·실패 정책

```text
INITIAL_WARMUP
→ READY_WAITING_FOR_VALID_CONDITION
→ CAST_PRECHECK
→ CAST_COMMIT
→ RESOLUTION_OR_ACTIVE_EFFECT
→ COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
```

```text
MAX_STORED_READY_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
COOLDOWN_DURING_ACTIVE_EFFECT = FALSE
```

- 새 전장 배치 뒤 첫 사용 전에 initial warmup을 거친다.
- 유효 조건이 없으면 READY를 보존한다.
- READY 상태에서 두 번째 사용권을 비축하지 않는다.
- `CAST_COMMIT` 전 trigger·target 무효화는 READY 복귀·cooldown 소비 0이다.
- 천공 소거·메테오는 commit 뒤 단발 사건을 한 번 해결한다.
- 불퇴의 성벽·생명의 서약·그림자 분신은 owner-bound 지속형이며 시전자 제거 시 종료한다.
- cooldown은 일제사격 판정, 메테오 폭발, 또는 지속효과 종료 뒤 시작한다.
- save/load·Retry로 warmup·cooldown·target·READY를 재굴림하거나 복제할 수 없다.

상세 책임 원본:

`design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md`

## 5. UX·저장 계약

표시 대상:

- `INITIAL_WARMUP`과 남은 시간.
- `READY`와 유효 조건 대기 이유.
- `CAST_COMMIT` 대상·범위·예고.
- active effect 남은 시간 또는 예산.
- cooldown 남은 시간.

저장 대상:

- 상태 enum.
- warmup·cooldown 남은 시간.
- deterministic target snapshot.
- 메테오 commit 위치·낙하 시간.
- 방벽 예산·체력 하한·분신 owner link 등 active payload.

## 6. 벤치마크·현업 비교 운영 정책

모든 Grill Me 질문과 승인 작업은 다음을 포함한다.

- Project Core·현행 정본.
- 직접 관련 공식 상용 사례 2~4개.
- OMENWARD와의 장르·조작·전투 규모 차이.
- 데이터·AI·pathfinding·animation·VFX/SFX·UI·save/load·determinism·QA 비용.
- 적대적 검토·복제 금지 경계.
- 선택지·제작비·검증비·권장안.

## 7. 적대적 검토 핵심

- warmup이 너무 짧으면 배치 즉시 폭발, 너무 길면 해금 보상이 죽는다.
- active effect 중 cooldown이 흐르면 지속형 스킬이 상시 유지될 수 있다.
- charge 누적은 전역 고등급 슬롯 하나의 순간 지배력을 과도하게 높인다.
- precommit 대상 소멸로 사용권을 잃으면 자동전투가 불공정하게 느껴진다.
- save/load·Retry·Stage 전환이 timer를 초기화하면 재굴림 exploit이 된다.
- commit 뒤 시전자 사망은 단발 해결형과 owner-bound 지속형을 구분해야 한다.
- Stage·정비시간 timer 진행 규칙은 아직 pending이다.

## 8. 구현 경계·다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
COMMON_STATE_MACHINE = APPROVED
SINGLE_READY_STORAGE = APPROVED
CHARGE_ACCUMULATION = FORBIDDEN
INITIAL_WARMUP = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWNS = PENDING
STAGE_AND_MAINTENANCE_TIMER_POLICY = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

- 현재 카운터는 `8/10`이다.
- 10번째 승인에서 fresh adversarial preflight를 실행한다.

```text
NEXT_GATE = OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
```
