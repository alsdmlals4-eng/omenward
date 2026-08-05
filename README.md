# OMENWARD / 오멘워드

**오멘워드**는 예고된 세 전선 공세를 읽고, 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 판타지 전략 오토배틀 게임입니다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
updated_at: 2026-08-05
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_planning_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_planning: FIRST_10_15_MINUTES_FLOW / NOT_IMPLEMENTED
current_grill_me_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_3_OF_10
working_pr: 142
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: NOT_AUTHORIZED
human_validation: HUMAN_QA_NOT_RUN
```

## 핵심 루프

```text
Stage 압력·Wave 순서 확인
→ 기본 건물 구조 확인·T2 발전 방향 선택
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

## 7/10 첫 10~15분 — 부분 승인 3/10

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10_IN_PROGRESS
PARTIAL_APPROVAL_3_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
INITIAL_T1_BUILDINGS = PREBUILT
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_CONSTRUCTION_TUTORIAL = FORBIDDEN
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
FIRST_MEANINGFUL_RULER_CHOICE = T2_UPGRADE_AND_IRREVERSIBLE_DEPLOYMENT
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
```

첫 플레이는 실제 MapRun이다. 기초 T1 건물은 이미 지어진 상태로 시작하고 역할은 짧게 확인한다. 중요한 설명과 판단은 T2 업그레이드 방향과 병력의 비가역 배치부터 시작한다. 벨루는 목표·행동·결과 원인을 설명하지만 T2·룰렛·배치·구매 결정을 대신하지 않는다.

```text
Stage 1 = 예고→T1 빠른 확인→T2 업그레이드→룰렛→병력 결과→비가역 배치→실전 전투→복기→첫 상인
Stage 2 = 이동권·행/열 조작→다전선 비교
Stage 3 = 마력탑→연구→첫 T1 전술→수동 시전
Stage 4 = 학습 시스템을 조합하는 첫 Danger
Stage 5 = 새 시스템 없이 숙련을 확인하는 첫 Boss
```

첫 상인은 Stage 1 정비시간에 등장하며 선택 사항과 골드 기회비용만 가르친다. 정확한 T1 인스턴스 수·위치, 첫 T2 후보, 최소 유효 경로, Danger/Boss 세부, 실패 규칙과 정확 시간은 아직 `PENDING_GRILLME`다.

## 먼저 읽을 문서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/ACTIVE_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
6. `docs/OMENWARD_GDD_CURRENT_CANON.md`
7. `docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md`
8. `docs/reviews/ADVERSARIAL_FIRST_10_15_MINUTES_FLOW_FORMAT_REVIEW_2026-08-05.md`
9. `docs/design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
10. `docs/CURRENT_IMPLEMENTATION_STATUS.md`

`[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않습니다.

## Planning Batch

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
[완료 2/10] Stage·Wave·Danger·Boss 압력
[완료 3/10] 건물 분기·카운터
[완료 4/10] 병종 역할·시너지·카운터
[완료 5/10] 전술스킬·마력
[완료 6/10] Stage 종료 상인
[진행 7/10] 첫 10~15분 흐름 — PARTIAL_APPROVAL_3_OF_10
```

완료 이력:

```text
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
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
