# OMENWARD / 오멘워드

**오멘워드**는 예고된 세 전선 공세를 읽고, 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 판타지 전략 오토배틀 게임입니다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
updated_at: 2026-08-05
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_planning_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_planning: TROOP_ROLES_SYNERGIES_AND_COUNTERS / NOT_IMPLEMENTED
current_grill_me_count: 4_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
human_validation: HUMAN_QA_NOT_RUN
```

## 핵심 루프

```text
Stage 압력·Wave 순서 확인
→ 건설·TokenSource 구성
→ 세 원형 릴 회전
→ 3×3 노출창에서 열·행 이동
→ 결과 확정
→ 보관·판매·한 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

## 현재 정본

- Stage: 20 Stage, 기본 3 Wave Beat, Danger `4/9/14/19`, Boss `5/10/15/20`.
- 압력: `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`.
- 자원: 골드·마석·배치 병력/병력 한도·룰렛 이동권.
- 건물: 금고·농장·병영·방어탑·지휘소·마력탑.
- 건물 분기: 인스턴스별 `T1 → T2 A/B → matching T3`; 교차 분기·양쪽 T3 금지.
- 병종 기준선: 방패수호병·대검병·창병·궁수·마도사·사제·암살자·기병·비행병·거인.
- 병종 수: 기준선 10종이지만 불변 조건이 아니며 역할 공백·중복과 제작비를 근거로 별도 승인 후 증감 가능.
- 시너지: 숨은 세트 보너스가 아니라 관찰 가능한 전장 행동 연결.
- 룰렛 자산: 실제 T1/T2 병종 이미지를 재사용하고 T3 병종 토큰은 금지.

## 작업 운영 정책

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH: 10
TDD_MANDATORY
RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE: FORBIDDEN
```

## 먼저 읽을 문서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/ACTIVE_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
6. `docs/OMENWARD_GDD_CURRENT_CANON.md`
7. `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
8. `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
9. `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
10. `docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md`
11. `docs/CURRENT_IMPLEMENTATION_STATUS.md`

`[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않습니다.

## 현재 배치

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
→ [완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
→ [완료 3/10] 건물 6종 T2/T3 분기·카운터
→ [현행 4/10] 병종 역할·시너지·카운터
→ [다음 5/10] 전술스킬·마석
→ [6/10] Stage 종료 상인
→ [7/10] 첫 10~15분 흐름
→ [8/10] Hero·Legendary
→ [9/10] Meta·Hub
→ [10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```

완료 이력 보존:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

제품 코드, 런타임, 실제 아트 자산은 별도 승인 전 변경하지 않습니다.