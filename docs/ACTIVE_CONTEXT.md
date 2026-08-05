# [현행] Active Context

```yaml
updated_at: 2026-08-05
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_count: 6_OF_10
current_status: PR_CANON_TARGET / NOT_IMPLEMENTED
current_working_pr: 141
next_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: HUMAN_QA_NOT_RUN
image_generation: STOPPED_BY_USER
```

## 현재 작업

Stage 1~19 종료 정비시간의 4칸 유한 재고 상인을 6/10 책임 원본으로 정리하고 PR #141의 최종 exact-head 검증을 수행한다.

책임 원본:

- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/OMENWARD_GDD_CURRENT_CANON.md`
- `docs/design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- `docs/design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- `docs/reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md`
- `docs/superpowers/specs/2026-08-05-stage-end-merchant-design.md`
- `docs/superpowers/specs/2026-08-05-stage-end-merchant-design-amendment.md`
- `docs/superpowers/plans/2026-08-05-stage-end-merchant.md`

## 현행 상인 계약

```text
MERCHANT_VISIT_STAGES = 1_TO_19
STAGE_20_MERCHANT = FORBIDDEN
TOTAL_MERCHANT_SLOTS = 4
SLOT_A = ROULETTE_CONTROL
SLOT_B = RECOVERY_SERVICE
SLOT_C = DEVELOPMENT_SERVICE
SLOT_D = VARIABLE_OPPORTUNITY
VISIT_STOCK = FINITE
PURCHASE_CURRENCY = GOLD_ONLY
```

- 이동권이 3 미만이면 이동권, 3/3이면 다음 룰렛 1회 할인을 제시한다.
- 상시 HUD 상점·전투 중 재진입·무한 구매·무한 reroll·할인 중첩은 금지한다.
- 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기를 직접 판매하지 않는다.

## TDD·Sheet 증거

```text
RED_RUN = 986 / FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 55 PASS
RED_NEW_MERCHANT_CONTRACTS = 10 FAIL_OR_ERROR
RED_CAUSE = CANON / REVIEW / 6_OF_10_ROUTING / LIFECYCLE_MISSING

GREEN_CANDIDATE_HEAD = 83c1dc0e241c4fd8b04a0e9a5680562f9469bd01
PROJECT_CORE_RUN = 1002 / SUCCESS
GDD_SHEET_RUN = 707 / SUCCESS
OMENWARD_CORE_RUN = 174 / SUCCESS
BASE_V9_RUN = 690 / SUCCESS
SHEET_BOUNDED_READBACK = PASS
REFACTOR = COMPLETE
```

REFACTOR와 증거 갱신으로 HEAD가 변경됐으므로 final exact-head CI와 Sheet read-back을 한 번 더 수행한다.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
```

가격·재고 수·등장률·할인율·거래 상태머신은 아직 확정하거나 구현하지 않는다.

## 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
LEGACY_C1_C2_C3_PROVEN
```

다음 Gate는 첫 10~15분 흐름 7/10이다.
