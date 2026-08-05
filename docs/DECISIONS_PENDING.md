# [현행] 오멘워드 미확정 결정 목록

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_count: 5_OF_10
next_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
product_code_authority: NONE
```

시스템 연결 기준선은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. 최신 5/10 기획은 제품에 구현되지 않았다.

## 확정된 5/10 범위

- 전술 자원명은 마력.
- 마력탑은 MapRun당 최대 1개.
- 마력탑은 분기 없는 `T1 → T2 → T3`.
- Tier 상승 시 초당 마력 수급량과 연구 가능한 전술 Tier 증가.
- 연구 비용은 골드+시간, 동시 연구 1개.
- 연구 완료 스킬은 현재 MapRun 동안 해금.
- Stage 전 편성 없음, 해금된 전술은 모두 사용 가능.
- 플레이어 수동 시전, 유효한 시전 확정 시 마력 소비.
- 새 MapRun에서 마력탑 Tier·연구·해금·보유 마력 초기화.
- 전술 기준선 T1 4종·T2 3종·T3 3종.
- 과거 마력탑 두 분기는 `[대체됨]`.

책임 원본:

- `docs/design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- `docs/reviews/ADVERSARIAL_TACTICAL_SKILLS_MANA_AND_RESEARCH_REVIEW_2026-08-05.md`

## 다음 6/10 — Stage 종료 상인

확정해야 할 항목:

1. Stage 종료 정비시간의 상인 진입·종료 흐름.
2. 상품군과 방문별 유한 재고.
3. 골드 사용의 건설·룰렛·연구·상인 기회비용.
4. 이동권·회복·연구 보조·병종 보상 후보의 역할.
5. 재고 갱신·구매 제한·무한 구매 방지.
6. 마지막 Stage 이후 최종 정산 예외.
7. 정확 가격·재고 수·등장률 시뮬레이션 Gate.

## 후속 미확정

- 7/10 첫 10~15분 흐름.
- 8/10 Hero·Legendary 재조정.
- 9/10 Meta·Hub 재조정.
- 10/10 전체 Run 콘텐츠·UX·아트 종합 검토.
- 병종·전술·건물의 정확 수치.
- 연구 취소 환불·마력 수급 가능 시간·제어 효과 감소 규칙.

## 구현 차단

```text
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_NUMERIC_AND_RUNTIME_PLAN
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
LEGACY_C1_C2_C3_PROVEN
```
