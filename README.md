# OMENWARD / 오멘워드

**오멘워드**는 예고된 세 전선 공세를 읽고, 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 판타지 전략 오토배틀 게임입니다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
updated_at: 2026-08-05
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_planning_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_planning: TACTICAL_SKILLS_AND_MANA / NOT_IMPLEMENTED
current_grill_me_count: 5_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
human_validation: HUMAN_QA_NOT_RUN
```

## 핵심 루프

```text
Stage 압력·Wave 순서 확인
→ 건설·TokenSource·연구 방향 설계
→ 세 원형 릴 회전과 결과 조작
→ 병력 보관·판매·비가역 전선 배치
→ 해금 전술을 마력으로 수동 시전
→ 결과 원인 복기
→ 다음 Stage 설계
```

## 현재 정본

- Stage: 20 Stage, 기본 3 Wave Beat, Danger `4/9/14/19`, Boss `5/10/15/20`.
- 압력: `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`.
- 자원: 골드·마력·배치 병력/병력 한도·룰렛 이동권.
- 건물: 금고·농장·병영·방어탑·지휘소·마력탑.
- 마력탑: MapRun당 1개, 분기 없는 `T1 → T2 → T3`, Tier 상승 시 마력 수급·연구 Tier 상승.
- 전술 연구: 골드+시간, 동시 연구 1개, 현재 MapRun 동안 해금.
- 전술 시전: 수동 대상 지정, 시전 확정 시 마력 소비, 자동 시전 금지.
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
7. `docs/design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
8. `docs/reviews/ADVERSARIAL_TACTICAL_SKILLS_MANA_AND_RESEARCH_REVIEW_2026-08-05.md`
9. `docs/CURRENT_IMPLEMENTATION_STATUS.md`

`[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않습니다.

## Planning Batch

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
[완료 2/10] Stage·Wave·Danger·Boss 압력
[완료 3/10] 건물 분기·카운터
[완료 4/10] 병종 역할·시너지·카운터
[현행 5/10] 전술스킬·마력
[다음 6/10] Stage 종료 상인
```

완료 이력:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
```

## 운영·Legacy 증거

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH: 10
TDD_MANDATORY
RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE: FORBIDDEN
V2_SPEC_APPROVED
LEGACY_C1_C2_C3_PROVEN
```

제품 코드·런타임·수치 데이터·실제 아트 자산은 별도 승인 전 변경하지 않습니다.
