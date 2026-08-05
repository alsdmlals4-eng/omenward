# [현행] 오멘워드 미확정 결정 목록

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
next_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
product_code_authority: NONE
```

시스템 연결 기준선은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. 최신 병종 기획은 아직 제품에 구현되지 않았다.

## 확정된 범위

- 열 종 병종 기준선.
- 병종 수는 불변 조건이 아니며 사전 고정 최소·최대 없음.
- 다섯 압력 각각에 최소 두 병종 대응 경로.
- 행동 기반 시너지와 단순 세트 보너스 금지.
- 전열/기동 병영 가중과 공통 지원 계열.
- T1/T2 실제 인게임 이미지 재사용, T3 룰렛 토큰 금지.
- 제품 데이터·정확 수치 변경 없음.

책임 원본:

- `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- `docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md`

## 다음 5/10 — 전술스킬·마석

확정해야 할 항목:

1. 전술스킬 슬롯·획득·교체 규칙.
2. 마석 수급·보유·사용 시점.
3. MASS·ARMORED·FLYING·INFILTRATION·SIEGE별 전술 대응.
4. 자동 시전 금지와 플레이어 의도 입력.
5. 건물·병종과 중복되지 않는 전술 역할.
6. 정확 수치 시뮬레이션 Gate.

## 후속 미확정

- 6/10 Stage 종료 상인.
- 7/10 첫 10~15분 흐름.
- 8/10 Hero·Legendary 재조정.
- 9/10 Meta·Hub 재조정.
- 10/10 전체 Run 콘텐츠·UX·아트 종합 검토.
- 병종 체력·공격력·관통·회복·속도·확률·비용.
- 병영 가중치와 승급 비용.
- 병종 수 증감이 필요한 경우 별도 Decision.

## 구현 차단

```text
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_TACTICAL_AND_NUMERIC_DECISIONS
DATA_MIGRATION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
HUMAN_QA = NOT_RUN
```

`data/units/*.tres`는 Legacy Prototype 증거이며 구현 입력으로 사용하지 않는다.

## 완료 이력 보존

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```