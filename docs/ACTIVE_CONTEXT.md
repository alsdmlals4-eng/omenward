# [현행] Active Context

```yaml
updated_at: 2026-08-05
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_count: 5_OF_10
current_status: PR_CANON_TARGET / NOT_IMPLEMENTED
current_working_pr: 140
next_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: HUMAN_QA_NOT_RUN
image_generation: STOPPED_BY_USER
```

## 현재 작업

마력탑 연구·마력 수급·수동 전술 시전과 4·3·3 전술 목록을 5/10 책임 원본으로 정리하고 PR #140의 최종 exact-head 검증을 수행한다.

책임 원본:

- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/OMENWARD_GDD_CURRENT_CANON.md`
- `docs/design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- `docs/reviews/ADVERSARIAL_TACTICAL_SKILLS_MANA_AND_RESEARCH_REVIEW_2026-08-05.md`
- `docs/superpowers/specs/2026-08-05-tactical-skills-and-mana-design.md`
- `docs/superpowers/plans/2026-08-05-tactical-skills-and-mana.md`

## 현행 계약

```text
마력탑 최대 활성 수 = 1
마력탑 = T1 → T2 → T3
분기 = FORBIDDEN
동시 연구 = 1
연구 = 골드 + 시간
시전 = 마력
Stage 전 편성 = 없음
자동 시전 = 금지
Reset = NEW_MAPRUN
```

```text
T1 4종 = 속박진 / 수호장 / 집중 명령 / 충격파
T2 3종 = 폭풍 억제 / 파쇄 명령 / 봉쇄 결계
T3 3종 = 결전의 깃발 / 성역 / 시간 왜곡
```

## TDD·Sheet 증거

```text
RED_RUN = 954 / FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 45 PASS
GREEN_CANDIDATE_HEAD = 917445ba9b09260da1f2b7bafb0bbf2f809a834b
PROJECT_CORE_RUN = 976 / SUCCESS
GDD_SHEET_RUN = 682 / SUCCESS
OMENWARD_CORE_RUN = 150 / SUCCESS
BASE_V9_RUN = 665 / SUCCESS
SHEET_CANDIDATE_READBACK = PASS
REFACTOR = COMPLETE
```

REFACTOR 이후 최종 SHA를 문서에 고정하면 다시 self-reference가 생기므로 final exact-head 증거는 PR #140과 Sheet의 현재 상태 셀이 소유한다.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
```

마력 수급량·보유 상한·연구비·연구시간·시전비·쿨다운·범위·지속시간은 아직 확정하지 않는다.

## 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
LEGACY_C1_C2_C3_PROVEN
```

다음 Gate는 Stage 종료 상인 6/10이다.
