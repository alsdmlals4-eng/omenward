# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_SIGNATURE_DELTA_BALANCE_PLANNING
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
last_merged_planning_pr: 127
base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 2
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 현재 승인 결정 2건

### 1.1 스킨형 단일 차이

Decision ID:

`OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1`

```text
원본 병종 [영웅] 등급 유닛
+ 영웅 전용 스킨·이름·최소 식별 연출
+ 패시브 1개 또는 자동 [사용스킬] 1개
= 이름 지정 영웅
```

- 이름 지정 영웅은 완전 신규 유닛이 아니라 기존 `[영웅]` 등급 병종의 스킨형 전술 변주다.
- `PASSIVE XOR AUTOMATIC_ACTIVE_SKILL`이며 두 유형을 동시에 제공하지 않는다.
- `[사용스킬]`은 기존 자동 발동 계약을 따르며 수동 버튼·수동 타깃이 아니다.
- 원본 병종의 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 고유 자원·궁극기·새 AI·전체 신규 애니메이션은 기본 금지다.

### 1.2 단일 상쇄 축

Decision ID:

`OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1`

```text
원본 전투 데이터 복사
→ 패시브 또는 자동 사용스킬 하나 적용
→ 직접 관련된 상쇄 축 하나만 하향·조건화
→ 나머지 원본 데이터 유지
```

- 상쇄 축은 단일 차이의 가치와 직접 연결돼야 한다.
- 여러 스탯을 동시에 낮추거나 영웅별 전체 성장 곡선을 새로 만들지 않는다.
- 조건 의존도를 상쇄로 쓰면 조건 미충족 구간에서 실제 저점이 발생해야 한다.
- 모든 영웅에게 동일한 고정 능력치 세금을 적용하지 않는다.
- 원본 병종이 더 좋은 대표 상황을 최소 하나 유지한다.

## 2. 전투 예산 경계

```text
SIGNATURE_DELTA_COUNT = 1
COMPENSATION_AXIS_COUNT = 1
COMPENSATION_MUST_BE_CAUSALLY_RELATED = TRUE
ALL_OTHER_SOURCE_AXES_INHERITED = TRUE
```

- 무료 패시브·사용스킬 추가는 금지다.
- 형식적인 무관 능력치 하향으로 비용을 회피하지 않는다.
- 상쇄 축 하나가 여러 파생 결과를 바꾸면 총 전투 예산에서 함께 검증한다.
- 원본/영웅 선택률·조건 충족률·고점/저점·대표 encounter를 simulation에서 비교한다.

## 3. 기존 생명주기 연결

- 영웅은 기존 UnitArchetype에 고정 연결된다.
- 동병종 `[영웅]` 토큰을 원본 병종 또는 이름 지정 영웅으로 1:1 변환한다.
- 세 전선 전체 active 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 사망 후 재출전에는 사망 이후 새 적격 토큰이 필요하다.
- 생존 상태·Stage 경계·정비시간·저장 규칙은 기존 승인 계약을 따른다.

## 4. 책임 원본

- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`

## 5. 적대적 검토 핵심

- 상쇄가 너무 작아 무료 능력과 동일해지지 않는지 확인한다.
- 능력과 무관한 축을 낮춰 실질 비용을 회피하지 않는지 확인한다.
- 여러 스탯을 조금씩 조정해 전체 재설계로 돌아가지 않는지 확인한다.
- 조건부 상쇄가 대부분 충족돼 실질 약점이 사라지지 않는지 확인한다.
- 단일 축 하향이 지나쳐 영웅이 함정 선택이 되지 않는지 확인한다.
- 스킨형이라는 이유로 장식 전용 또는 순수 상위호환이 되지 않는지 확인한다.

## 6. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_HERO_VARIANTS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

다음 우선 결정:

```text
OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
```

검토 주제는 `초기 제작 범위에서 몇 개 병종·몇 명의 이름 지정 영웅을 먼저 제공할지`다.
