# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_ABILITY_KIT_PLANNING_BATCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
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
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 1
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`context_baseline_commit`과 `current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 승인 기획은 Draft PR #129에 누적하며 제품 구현 권한은 없다.

## 1. 현재 제품 방향

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 공식 흐름은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- 현재 제품은 Legacy 프로토타입이고 최신 승인 기획은 미구현이다.
- 전체 시스템 Vertical Slice 책임 원본은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다.
- 현행 적대적 검토 계보는 `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`다.
- 룰렛 Evidence Pilot은 `PILOT_RECOMMENDATION / NOT_CANON`이다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 2. 영웅 생명주기 정본

```text
기존 UnitArchetype
→ 이름 지정 영웅 결정론적 해금·Profile 등록
→ 룰렛 동병종 [영웅] 등급 토큰
→ 원본 병종 또는 해금 영웅 선택
→ 전역 active slot 검사
→ 1토큰을 1유닛으로 변환·한 전선 비가역 배치
→ 공개 규칙 기반 자동 능력 운용
```

- 세 전선 전체 active 이름 지정 영웅은 동시에 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 생존 영웅의 HP·쿨다운·충전·고유 자원은 Stage를 넘어 유지한다.
- 영웅 사망은 회수 보상·부활권·보장·pity를 제공하지 않는다.
- 사망 이후 새 동병종 `[영웅]` 결과로만 이름 지정 영웅을 재출전한다.
- 이름 지정 영웅은 원본 병종의 순수 상위호환이 아닌 조건부 고점형 전문화 sidegrade다.

## 3. 현재 승인 영웅 키트

```text
병종 기반 기본 공격
+ 고유 특성 1개
+ 규칙 기반 자동 전투 능력 1개
+ 명시적 약점·대응법 1개 이상
```

- 정규 능력 슬롯은 `HERO_COMBAT_ABILITY` 하나다.
- `HERO_TRAIT`는 기본 공격 변화, 조건부 패시브, 위치·전선·조합 규칙 중 하나를 주 역할로 가진다.
- 고유 자원은 필요한 영웅만 최대 1종 사용하며 별도 능력 슬롯으로 계산하지 않는다.
- 공통 궁극기 슬롯·수동 궁극기 버튼·수동 타깃 지정은 금지다.
- 기본 공격 변형이나 특성 안에 독립 능력을 숨겨 사실상 3개 이상 능력 키트를 만드는 것을 금지한다.
- 정확 영웅 키트·수치·HeroAbilitySpec 구현은 pending이다.

## 4. 자동 발동·결정론

```text
공개 trigger
→ 고정 ability priority
→ 공개 target filter·priority·tie-break
→ 유효성 재검증
→ 자동 발동
→ 상태 기록
```

- 동일 저장 상태와 입력 순서에서는 같은 능력과 대상을 선택한다.
- 저장·Retry로 자동 판단을 재굴림할 수 없다.
- 대상 상실·중단·비용 소비 정책은 후속 공통 계약에서 확정한다.

## 5. 현재 책임 원본

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

## 6. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
EXACT_HERO_KITS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 운영 규칙

- 승인된 중요 결정은 GitHub 정본과 Sheet에 같은 Decision ID로 즉시 반영한다.
- 현재 카운터는 `1/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 문서·기획 PR은 Green preflight와 blocker 0이면 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 standing authorization 범위 밖이다.

## 8. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-TRAIT-PATTERN-BOUNDARY-V1
```
