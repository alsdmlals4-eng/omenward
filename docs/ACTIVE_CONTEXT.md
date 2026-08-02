# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_GRADE_SLOT_AND_UNIQUE_SKILL_2_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 6
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
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ 세로·가로 이동과 확정으로 결과 조작
→ 병력 보관·판매·획득
→ 어느 전선에 비가역 배치할지 판단
→ 자동전투·점령·건물 운영으로 전황 역전
→ 결과를 다음 Stage 설계에 환류
```

핵심 시스템:

- 공세 예측.
- 건물·병영·금고에 결속된 룰렛 토큰 구조 설계.
- 영구 가로 이동과 SpinSnapshot 기반 결과 조작.
- 보관·판매·비가역 전선 배치.
- 세 전선 자동전투·점령·거점·건물 운영.

보조 시스템:

- 골드·식량·보관함·판매.
- 건설·업그레이드·수리·파괴·BLOCKED.
- 병영 Tier 패시브와 룰렛 등급 스킬 성장.
- 20 Stage MapRun·Wave·정비시간·checkpoint.
- 미션·메타 해금·벨루·UI·아트·오디오.

현재 제품은 Legacy 프로토타입이며 최신 승인 기획은 미구현이다. 전체 시스템 권위는 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`, 현행 적대적 검토 계보는 `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`다. 룰렛 Evidence Pilot `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 `PILOT_RECOMMENDATION / NOT_CANON`이다.

## 2. 표준 병종 등급 정본

```text
[일반] = 1스킬
[엘리트] = 강화된 1스킬
[영웅] = 강화된 1스킬 + 표준 2스킬
[전설] = 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬
```

- 등급은 룰렛 완성선으로 결정하고 병영 Tier와 독립한다.
- 병영 Tier는 핵심 패시브 해금·강화와 실제 병종 출처를 결정한다.
- 표준 등급 책임 원본은 `APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md`다.

## 3. 해금 이름 지정 영웅 현행 모델

```text
표준 [영웅]
= 강화된 1스킬 + 표준 2스킬

해금 이름 지정 [영웅]
= 강화된 1스킬 + 고유 2스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
NAMED_HERO_UNIQUE_SKILL_SLOT = 2
STANDARD_SKILL_2 = REPLACED
EXTRA_SKILL_ADDED = FALSE
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
```

- 해금 영웅은 표준 영웅보다 강하고 전설보다 약하다.
- 고유 2스킬은 표준 2스킬을 교체하며 추가 3번째 스킬이 아니다.
- 패시브·숨은 상시 보너스·의무 능력치 하향은 없다.
- 정확 영웅 이름·고유 2스킬·수치는 아직 확정하지 않는다.

## 4. 영웅 이상 등급 전역 단일 활성

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

다음을 상·중·하 전선 전체에서 모두 합쳐 최대 1명만 활성화한다.

- 표준 `[영웅]`.
- 해금 이름 지정 `[영웅]`.
- 표준 `[전설]`.
- 향후 해금 이름 지정 `[전설]`.

- 이름 지정 여부·병종·전선을 바꾸어 제한을 우회할 수 없다.
- 제한은 획득이 아니라 전장 배치에 적용한다.
- 슬롯이 차 있을 때 새 영웅·전설 토큰은 정상 생성하며 보관·판매할 수 있다.
- 자동 삭제·자동 교체·수동 퇴각·수동 교대는 금지한다.
- 살아 있는 영웅 이상 유닛은 Stage·Act·정비시간을 넘어 동일 인스턴스로 지속한다.

## 5. 초기 해금 영웅 5명

```text
shield_guard / 방패병 → UNIQUE_SKILL_2
archer / 궁병         → UNIQUE_SKILL_2
priest / 사제         → UNIQUE_SKILL_2
mage / 마법사         → UNIQUE_SKILL_2
assassin / 암살자     → UNIQUE_SKILL_2
```

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_UNIQUE_SKILL_SLOT = 2
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

다섯 고유 2스킬은 한 번의 발동으로 배치 전선의 국면을 바꾸는 전장 사건이어야 하지만 표준 전설 전체 키트를 넘지 않는다.

## 6. 자동 발동 공통 프레임

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 병종별 유효 조건·대상 확인
→ deterministic priority·tie-break
→ 발동 직전 재검증
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

- 유효 조건이 없으면 준비 상태를 보존한다.
- 수동 스킬·수동 타깃·수동 보류는 없다.
- 동일 저장 상태와 입력 순서는 동일 결과를 만든다.

## 7. 향후 해금 전설 방향

```text
표준 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬

향후 해금 이름 지정 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 고유 3스킬
```

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

현재는 슬롯 방향만 승인하며 로스터·획득·수치·자산·구현은 후속 범위다.

## 8. 적대적 검토 핵심

- named-only 1명 제한은 폐기됐으며 영웅 이상 등급 전체가 슬롯을 공유한다.
- 표준 2스킬과 고유 2스킬을 동시에 주면 전설 계층을 침범하므로 교체 구조만 허용한다.
- 영웅이 오래 생존할 때 후속 전설 잭팟을 즉시 배치하지 못하는 좌절을 보관·판매·UI·경제로 검증한다.
- 영웅 결과 빈도와 슬롯 점유시간이 보관함 압력을 과도하게 만들 수 있어 simulation이 필요하다.
- 해금 후 표준 영웅이 선택되지 않는 것은 의도된 수직 성장이다. 미해금 상태에서도 기본 진행 가능해야 한다.
- 영웅 이상 한 명이 세 전선 전체의 유일한 승리 조건이 되면 실패다.

상세 검토: `reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md`.

## 9. 현재 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`
- `docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md`
- `docs/design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md`

## 10. 구현 경계·다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILL_2 = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

- 현재 카운터는 `6/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- Green preflight와 blocker 0인 문서·기획 PR은 standing authorization에 따라 병합한다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
```
