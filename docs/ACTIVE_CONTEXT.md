# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_UNIQUE_SKILL_UPGRADE_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
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
current_grill_me_count: 5
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 승인 기획은 Draft PR #129에 누적하며 제품 구현 권한은 없다.

## 1. 현재 제품·계보

- 제품 핵심은 세 물리 릴을 건물과 TokenSource로 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 공식 진행은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- 현재 제품은 Legacy 프로토타입이며 최신 승인 기획은 미구현이다.
- 현행 전체 시스템 권위는 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다.
- 현행 적대적 검토 계보는 `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`다.
- 룰렛 Evidence Pilot `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 `PILOT_RECOMMENDATION / NOT_CANON`이다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 2. 영웅 생명주기 정본

```text
기존 UnitArchetype
→ 이름 지정 영웅 영구 해금·Profile 등록
→ 룰렛 동병종 [영웅] 등급 토큰
→ 원본 병종 또는 이름 지정 영웅 선택
→ 전역 active slot 검사
→ 1토큰을 1유닛으로 변환·한 전선 비가역 배치
→ 공개 규칙 기반 자동 전투
```

- 세 전선 전체 활성 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 생존 상태는 기존 Stage 지속 계약을 따른다.
- 사망 후 재출전에는 사망 이후 새 동병종 `[영웅]` 결과가 필요하다.

## 3. 해금 영웅 현행 모델

```text
원본 병종 [영웅] 등급 유닛
+ 이름·초상·스킨·식별 연출
+ 고유 자동 사용스킬 1개
= 제한형 상위호환 이름 지정 영웅
```

```text
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1_PER_HERO
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
MANDATORY_COMPENSATION_AXIS_COUNT = 0
SOURCE_BASELINE_STATS = INHERITED
GLOBAL_ACTIVE_NAMED_HERO_CAP = 1
```

- 이전 `패시브 XOR 자동 사용스킬` 구조는 폐기했다.
- 이전 `단일 차이 + 관련 상쇄 축 1개`와 평균 예산 동등 sidegrade 의무도 폐기했다.
- 이름 지정 영웅은 원본보다 조금 더 강하고 임팩트 있는 해금 보상이다.
- 기본 능력치를 의무적으로 낮추지 않는다.
- 전역 활성 1명·해금·적격 `[영웅]` 토큰·비가역 배치·스킬 cooldown/charge로 통제한다.
- 미해금 상태와 다른 이름 지정 영웅 활성 중에는 원본 `[영웅]` 등급 유닛이 계속 필요하다.

## 4. 초기 검증 로스터 5명

```text
shield_guard / 방패병 → 고유 자동 사용스킬
archer / 궁병         → 고유 자동 사용스킬
priest / 사제         → 고유 자동 사용스킬
mage / 마법사         → 고유 자동 사용스킬
assassin / 암살자     → 고유 자동 사용스킬
```

```text
INITIAL_HERO_COUNT = 5
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

- 5명은 최종 출시 상한이 아니라 첫 제작·밸런스·UX·자동 타기팅·자산 재사용 검증 범위다.
- 정확 영웅 이름·스킬·발동 조건·cooldown·VFX/SFX·수치는 아직 확정하지 않는다.

## 5. 고유 스킬 자동 발동

```text
공개 trigger
→ 공개 target filter·priority·tie-break
→ 대상·cooldown/charge 재검증
→ 자동 발동
→ 상태·로그 기록
```

- 수동 스킬 버튼·수동 타깃·수동 보류는 없다.
- 동일 저장 상태와 입력 순서에서는 같은 결과를 낸다.
- 저장·Retry 재굴림은 금지다.
- 스킬 발동은 전투 결과와 VFX/SFX에서 즉시 식별돼야 한다.

## 6. 현재 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` — `SUPERSEDED_HISTORY`

## 7. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILLS = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영 규칙·다음 Gate

- 현재 카운터는 `5/10`이다.
- 승인된 중요 결정은 GitHub와 Sheet에 같은 Decision ID로 즉시 반영한다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- Green preflight와 blocker 0인 문서·기획 PR은 standing authorization에 따라 병합한다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-CONCEPTS-V1
```
