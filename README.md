# OMENWARD / 오멘워드

**오멘워드**는 예고된 세 전선 공세를 읽고, 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 판타지 전략 오토배틀 게임입니다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
updated_at: 2026-08-06
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
work_mode: TOTAL_PLANNING
current_planning_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_planning: STAGE_END_MERCHANT / NOT_IMPLEMENTED
current_grill_me_count: 6_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
human_validation: HUMAN_QA_NOT_RUN
platform_phase2: MAIN_CANONICAL
```

공통 작업·검증·PR·승인 배치 규칙은 Base에서만 관리한다. 이 README는 OMENWARD의 제품 정본과 프로젝트별 구현·검증 경계만 요약한다.

## 핵심 루프

```text
Stage 압력·Wave 순서 확인
→ 건설·TokenSource·연구 방향 설계
→ 세 원형 릴 회전과 결과 조작
→ 병력 보관·판매·비가역 전선 배치
→ 해금 전술을 마력으로 수동 시전
→ Stage 종료 정비시간의 제한 상인 선택
→ 결과 원인 복기와 다음 Stage 설계
```

## 현재 정본

- Stage: 20 Stage, 기본 3 Wave Beat, Danger `4/9/14/19`, Boss `5/10/15/20`.
- 압력: `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`.
- 자원: 골드·마력·배치 병력/병력 한도·룰렛 이동권.
- 건물: 금고·농장·병영·방어탑·지휘소·마력탑.
- 마력탑: MapRun당 1개, 분기 없는 `T1 → T2 → T3`, Tier 상승 시 마력 수급·연구 Tier 상승.
- 전술 연구: 골드+시간, 동시 연구 1개, 현재 MapRun 동안 해금.
- 전술 시전: 수동 대상 지정, 시전 확정 시 마력 소비, 자동 시전 금지.
- 상인: Stage 1~19 종료 정비시간에만 방문, Stage 20 뒤에는 최종 정산.
- 상인 재고: 룰렛 제어·복구·성장 보조·가변 기회의 유한 4칸.
- 상인은 병종·전술·마력·건물 분기를 직접 판매하지 않는다.
- 전술 기준선: T1 4종·T2 3종·T3 3종, 총 10종.
- 병종 기준선: 10종이지만 역할 근거와 별도 승인에 따라 증감 가능.
- 룰렛 자산: 실제 T1/T2 병종 이미지를 재사용하고 T3 병종 토큰은 금지.

## 먼저 읽을 문서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/ACTIVE_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
6. `docs/OMENWARD_GDD_CURRENT_CANON.md`
7. `docs/design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
8. `docs/reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md`
9. `docs/CURRENT_IMPLEMENTATION_STATUS.md`

`[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않습니다.

## Planning Batch

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
[완료 2/10] Stage·Wave·Danger·Boss 압력
[완료 3/10] 건물 분기·카운터
[완료 4/10] 병종 역할·시너지·카운터
[완료 5/10] 전술스킬·마력
[현행 6/10] Stage 종료 상인
[다음 7/10] 첫 10~15분 흐름
```

완료 이력:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
```

## 구현·검증 경계

```text
V2_SPEC_APPROVED
LEGACY_C1_C2_C3_PROVEN
PLATFORM_PHASE0_MAIN_CANONICAL_LOCAL_PASS
PLATFORM_PHASE1_MAIN_CANONICAL_LOCAL_PASS
PLATFORM_PHASE2_MAIN_CANONICAL_LOCAL_PASS
FULL_PROJECT_RUNTIME = NOT_RUN
REPRESENTATIVE_PC_BUILD = NOT_RUN
REPRESENTATIVE_ANDROID_BUILD = NOT_RUN
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
```

제품 코드·런타임·수치 데이터·실제 아트 자산은 별도 승인 전 변경하지 않습니다.