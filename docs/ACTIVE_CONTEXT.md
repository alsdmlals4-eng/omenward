# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_INITIAL_ROSTER_SCOPE_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
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
current_grill_me_count: 3
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`context_baseline_commit`과 `current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 승인 기획은 Draft PR #129에 누적하며 제품 구현 권한은 없다.

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

- 세 전선 전체 active 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 생존 상태는 기존 Stage 지속 계약을 따른다.
- 사망은 회수 보상을 제공하지 않고 사망 이후 새 동병종 `[영웅]` 결과로만 재출전한다.
- 이름 지정 영웅은 원본 병종의 순수 상위호환이 아닌 전문화 sidegrade다.

## 3. 이름 지정 영웅 제작·밸런스 모델

```text
기존 병종 [영웅] 등급 유닛
+ 영웅 전용 스킨·이름·최소 식별 연출
+ 패시브 1개 또는 자동 [사용스킬] 1개
- 직접 관련된 상쇄 축 1개
= 이름 지정 영웅
```

```text
SIGNATURE_DELTA_COUNT = 1
SIGNATURE_DELTA = PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
COMPENSATION_AXIS_COUNT = 1
COMPENSATION_MUST_BE_CAUSALLY_RELATED = TRUE
ALL_OTHER_SOURCE_AXES_INHERITED = TRUE
```

- 원본 병종의 핵심 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 패시브형과 사용스킬형 중 하나만 선택하며 둘을 동시에 제공하지 않는다.
- `[사용스킬]`은 수동 버튼이 아니라 기존 자동 발동 정본을 따르는 규칙 기반 자동 능력이다.
- 고유 자원·공통 궁극기·새 AI 구조·전체 신규 애니메이션 세트는 기본 금지다.
- 단일 차이의 가치와 직접 연결된 능력치·효율·조건 축 하나만 조정한다.
- 상쇄 축 외의 원본 데이터는 유지하고 원본 병종이 더 나은 대표 상황을 최소 하나 유지한다.

## 4. 초기 검증 로스터 범위

```text
서로 다른 기존 UnitArchetype 4종
→ 병종마다 이름 지정 영웅 1명
→ 패시브형 2명
→ 자동 사용스킬형 2명
→ 초기 검증 로스터 총 4명
```

```text
INITIAL_NAMED_HERO_COUNT = 4
INITIAL_SOURCE_ARCHETYPE_COUNT = 4
HEROES_PER_SOURCE_ARCHETYPE = 1
PASSIVE_VARIANT_COUNT = 2
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
```

- 초기 4명은 서로 다른 원본 병종에 연결하며 역할·전투 판단 중복을 최소화한다.
- 정확 병종·영웅 이름·능력·상쇄 축은 아직 확정하지 않는다.
- 4명은 최종 출시 전체 로스터 상한이 아니라 첫 제작·밸런스·UX·자산 재사용 검증 범위다.
- 패시브형과 자동 사용스킬형을 각각 2명씩 검증한다.
- 후보 병종은 원본 완성도·자산 재사용성·전술 차별성·상쇄 가독성·콘텐츠 노출성을 기준으로 선정한다.
- 초기 4명을 모두 완전 신규 유닛으로 제작하는 것은 금지한다.

## 5. 자동 발동·결정론

사용스킬형 영웅은 다음을 따른다.

```text
공개 trigger
→ 공개 target filter·priority·tie-break
→ 대상·비용·cooldown 재검증
→ 자동 발동
→ 상태 기록
```

- 수동 스킬 버튼·수동 타깃·수동 보류는 없다.
- 동일 저장 상태와 입력 순서에서는 같은 결과를 낸다.
- 저장·Retry 재굴림은 금지다.

## 6. 현재 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`

## 7. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
INITIAL_HERO_COUNT = 4
EXACT_ARCHETYPES = PENDING
EXACT_HEROES = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영 규칙·다음 Gate

- 현재 카운터는 `3/10`이다.
- 승인된 중요 결정은 GitHub와 Sheet에 같은 Decision ID로 즉시 반영한다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- Green preflight와 blocker 0인 문서·기획 PR은 standing authorization에 따라 병합한다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
```
