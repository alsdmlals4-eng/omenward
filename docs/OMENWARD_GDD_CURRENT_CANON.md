# [현행] OMENWARD GDD 정본

```yaml
updated_at: 2026-08-05
status: CURRENT_GDD_CANON
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_count: 6_OF_10
next_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
product_code_authority: NONE
```

## 1. 게임 정체성

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

플레이어는 공개된 Stage 압력을 읽고 건물·릴·병종·전술 연구를 설계한 뒤, 획득 병력을 한 전선에 비가역 배치하고 적절한 순간에 해금 전술을 수동 시전한다. Stage 종료 뒤에는 제한 상인과 기존 시스템 정비를 통해 다음 Stage의 골드 기회비용을 결정한다.

## 2. 핵심 인과

```text
예고된 압력
→ 건설·TokenSource·연구 투자
→ 제작한 확률과 룰렛 조작
→ 병력 결과·비가역 전선 커밋
→ 마력 기반 수동 전술 타이밍
→ Stage 결과 정산·제한 상인 선택
→ 설명 가능한 결과·다음 설계
```

## 3. MapRun·Stage

```text
MapRun = 20 Stage
Wave Beat = 기본 3개
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
압력 = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

Stage 중 숨은 필수 카운터 변경과 비공개 Route 강제를 금지한다.

## 4. 자원·건물

```text
자원 = 골드 / 마력 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

다섯 건물은 승인된 분기 계보를 사용한다. 마력탑은 유일한 선형 예외다.

```text
마력탑 최대 활성 수 = 1
마력탑 T1 → T2 → T3
BRANCHING = FORBIDDEN
Tier 상승 = 초당 마력 수급 증가 + 연구 가능 전술 Tier 증가
```

## 5. 병종·룰렛

병종 기준선은 10종이며 불변 수량이 아니다. 압력별 최소 두 병종 경로를 유지하고 역할 증감은 별도 승인한다.

- 룰렛에는 실제 T1/T2 병종 이미지를 사용한다.
- T3 병종 룰렛 토큰은 금지한다.
- 병력은 보관·판매 후 한 전선에 배치한다.
- 배치 뒤 자유 회수·판매·Cross-lane 이동은 금지한다.

## 6. 전술 연구·시전

```text
TOTAL_TACTICAL_SKILLS = 10
T1 = 4
T2 = 3
T3 = 3
ONE_CONCURRENT_RESEARCH
STAGE_LOADOUT = NONE
AUTO_CAST = FORBIDDEN
```

```text
T1 = 속박진 / 수호장 / 집중 명령 / 충격파
T2 = 폭풍 억제 / 파쇄 명령 / 봉쇄 결계
T3 = 결전의 깃발 / 성역 / 시간 왜곡
```

- 연구 비용은 골드+시간이다.
- 연구 완료 스킬은 현재 MapRun 동안 해금된다.
- 해금된 모든 스킬은 전술 패널에서 사용 가능하다.
- 플레이어가 대상·전선·시점을 직접 지정한다.
- 유효한 시전 확정 시 마력을 소비한다.
- 대상 무효·취소·Layer 불일치에는 마력을 소비하지 않는다.
- 새 MapRun에서 마력탑 Tier·연구·해금·보유 마력을 초기화한다.

전술은 병종·건물의 지속 역할을 대체하지 않는다.

## 7. Stage 종료 상인

```text
MERCHANT_VISIT_STAGES = 1_TO_19
STAGE_20_MERCHANT = FORBIDDEN
TOTAL_MERCHANT_SLOTS = 4
VISIT_STOCK = FINITE
PURCHASE_CURRENCY = GOLD_ONLY
```

재고:

```text
A = 룰렛 제어
B = 복구 서비스
C = 성장 보조
D = 가변 기회
```

- 이동권이 3 미만이면 보관형 이동권을, 3/3이면 다음 룰렛 1회 비용 할인을 제시한다.
- 복구는 손상 건물 수리, 성장은 전술 연구 가속을 기본 후보로 사용한다.
- 가변 슬롯은 이동권·수리·연구 가속·다음 건설/업그레이드/룰렛 1회 할인을 제공할 수 있다.
- 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기·Stage 정보 직접 판매는 금지한다.
- 상시 HUD 상점·전투 중 재진입·무한 구매·무한 reroll·할인 중첩은 금지한다.
- Stage 20 종료 뒤에는 상인이 아니라 MapRun 최종 정산으로 이동한다.

## 8. UX 정보 계약

HUD는 골드·마력·배치 병력/병력 한도를 상시 표시한다. 마력은 보유량·상한·초당 수급을 읽을 수 있어야 한다.

마력탑 패널은 Tier, 다음 Tier 효과, 연구 가능 Tier, 연구 중 대상·남은 시간·골드 비용을 표시한다.

전술 패널은 Tier·마력 비용·쿨다운·대상 방식·대응 압력·사용 불가 이유를 표시한다. 편성 슬롯은 만들지 않는다.

상인 화면은 현재 골드, 네 슬롯의 상품·가격·재고·대상·소멸 조건·구매 후 잔액과 다음 Stage 압력 요약으로 돌아가는 경로를 표시한다.

## 9. 권위 계보

- `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- `design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- `design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- `design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- `design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- `design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- `reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md`

6/10은 과거 상인 개요의 상시 접근·무한 재고·직접 핵심 보상 판매 가능성을 대체한다.

## 10. 제품 경계

```text
VERTICAL_SLICE_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
LEGACY_C1_C2_C3_PROVEN
```
