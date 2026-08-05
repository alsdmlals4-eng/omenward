# [현행] 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
status: CURRENT_DOCUMENTATION_ROUTER
```

## 1. 최상위 읽기 순서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/ACTIVE_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
6. `docs/OMENWARD_GDD_CURRENT_CANON.md`
7. 주제별 `[현행]` 책임 원본
8. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
9. `docs/DECISIONS_PENDING.md`

## 2. 현재 시스템 연결·증거

- Vertical Slice 계보: `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- Vertical Slice 적대적 검토: `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- 핵심 재미 적대적 검토: `ADVERSARIAL_CORE_FUN_CANON_AND_LEGACY_CONFLICT_REVIEW_2026-08-04.md`
- 룰렛 Evidence Pilot: `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`
- Pilot 경계: `PILOT_RECOMMENDATION / NOT_CANON`
- 현행 GDD: `OMENWARD_GDD_CURRENT_CANON.md`
- 수명주기: `DOCUMENT_LIFECYCLE_REGISTRY.md`

## 3. 현재 Planning Batch

| 순서 | 상태 | 책임 원본 |
|---|---|---|
| 1/10 | 완료 | `APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md` |
| 2/10 | 완료 | `APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md` |
| 3/10 | 완료 | `APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md` |
| 4/10 | 현행 | `APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md` |
| 5/10 | 다음 | `OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1` |

병종 설계 근거와 실행 계획:

- `docs/superpowers/specs/2026-08-05-troop-roles-synergies-counters-design.md`
- `docs/superpowers/plans/2026-08-05-troop-roles-synergies-counters.md`
- `docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md`

## 4. 현행 병종 권위

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
```

- 열 종 기준선은 방패수호병·대검병·창병·궁수·마도사·사제·암살자·기병·비행병·거인이다.
- 압력별 최소 두 병종 대응 경로를 둔다.
- 시너지는 행동 기반이며 단순 세트 보너스는 금지한다.
- 병영은 전열/기동 가중을 바꾸되 반대 계열을 영구 삭제하지 않는다.
- T1/T2 실제 병종 이미지를 룰렛에 재사용하며 T3 토큰은 금지한다.
- `data/units/*.tres`는 최신 정본 구현 입력이 아닌 Legacy Prototype 증거다.

## 5. 수명주기 해석

- `[현행]`: 신규 기획·구현 입력 허용.
- `[대체됨]`: 후속 책임 원본이 승계. 역사 근거만 허용.
- `[보류]`: 최신 정본과 재검증 전 사용 금지.
- `[폐기]`: 채택하지 않음. 사용 금지.
- `[증거]`: 과거 사실만 증명.

파일명보다 `DOCUMENT_LIFECYCLE_REGISTRY.md`의 상태를 우선한다.

## 6. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 완료 이력 보존

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

4/10 문서 병합은 병종 `.tres`, AI, Scene, 수치 구현 승인이 아니다.