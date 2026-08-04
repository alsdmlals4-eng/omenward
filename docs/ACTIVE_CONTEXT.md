# [현행] Active Context

```yaml
updated_at: 2026-08-05
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
current_status: MAIN_CANON_TARGET / NOT_IMPLEMENTED
next_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: HUMAN_QA_NOT_RUN
image_generation: STOPPED_BY_USER
```

## 현재 작업

병종 역할·시너지·압력 카운터를 Stage·건물 정본과 연결한다.

책임 원본:

- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/OMENWARD_GDD_CURRENT_CANON.md`
- `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- `docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md`

## 현재 병종 기준선

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
```

```text
방패수호병 / 대검병 / 창병 / 궁수 / 마도사
사제 / 암살자 / 기병 / 비행병 / 거인
```

- MASS: 대검병·마도사, 보조 방패수호병.
- ARMORED: 마도사·창병, 보조 거인.
- FLYING: 궁수·비행병.
- INFILTRATION: 암살자·기병, 보조 후방 방패수호병.
- SIEGE: 창병·기병/암살자, 보조 거인 역공.
- 시너지는 행동 기반이며 단순 세트 보너스는 금지.
- 병영은 전열/기동 가중을 바꾸지만 반대 계열을 삭제하지 않음.
- T3 병종 룰렛 토큰은 금지.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
```

`data/units/*.tres`는 Legacy Prototype 증거이며 최신 구현 입력이 아니다.

## TDD 상태

- RED: Validate Project Core Documentation run 922.
- 예상 실패: 병종 정본·적대적 검토·4/10 중앙 라우팅·Legacy 데이터 격리 부재.
- GREEN/REFACTOR: 현재 PR exact head에서 재검증 예정.

## 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

다음 Gate는 전술스킬·마석 5/10이다.