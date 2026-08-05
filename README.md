# OMENWARD / 오멘워드

**오멘워드**는 예고된 세 전선 공세를 읽고, 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 판타지 전략 오토배틀 게임입니다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
updated_at: 2026-08-06
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_planning_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_planning: FIRST_10_15_MINUTES_FLOW / NOT_IMPLEMENTED
current_grill_me_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_5_OF_10
working_pr: 142
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: NOT_AUTHORIZED
human_validation: HUMAN_QA_NOT_RUN
```

## 핵심 루프

```text
Stage 압력·Wave 순서 확인
→ T1 기초 구축과 T2 발전 방향 선택
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
- 마력탑: MapRun당 1개, 분기 없는 `T1 → T2 → T3`.
- 전술 연구: 골드+시간, 동시 연구 1개, 현재 MapRun 동안 해금.
- 전술 시전: 수동 대상 지정, 시전 확정 시 마력 소비, 자동 시전 금지.
- 상인: Stage 1~19 종료 정비시간에만 방문, Stage 20 뒤에는 최종 정산.
- 상인 재고: 룰렛 제어·복구·성장 보조·가변 기회의 유한 4칸.
- 전술 기준선: T1 4종·T2 3종·T3 3종, 총 10종.
- 병종 기준선: 10종이지만 역할 근거와 별도 승인에 따라 증감 가능.

## 7/10 첫 10~15분 — 부분 승인 5/10

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10_IN_PROGRESS
PARTIAL_APPROVAL_5_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_FOUNDATION_THEN_BRANCH_CHOICE
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_PLACEMENT_POLICY = CATEGORY_COMPATIBLE_SAFE_NODES
T1_BUILD_ORDER = PLAYER_SELECTED
FOUNDATION_SETUP_RELOCATION = FREE_BEFORE_CONFIRMATION
FOUNDATION_SETUP_CONFIRMATION = REQUIRED
POST_CONFIRMATION_PLACEMENT_RULES = STANDARD_RUN_RULES
FREE_RELOCATION_AFTER_CONFIRMATION = FORBIDDEN
STAGE_1_REQUIRED_COST_RESERVE = SUM_OF_UNBUILT_REQUIRED_T1_COSTS
STAGE_1_NON_T1_SPENDING_BEFORE_REQUIRED_SET_COMPLETE = BLOCKED
STAGE_1_LEFTOVER_GOLD_POLICY = NORMAL_WALLET_AFTER_REQUIRED_SET_COMPLETE
FOUNDATION_GRANT_SURPLUS = FORBIDDEN
T1_INVALID_PLACEMENT_TRANSACTION = ATOMIC_ROLLBACK_FULL_REFUND
FIRST_ROULETTE_UNLOCK = AFTER_ALL_SIX_T1_AND_SETUP_CONFIRMATION
EXACT_T1_COSTS = PENDING_SIMULATION
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
SCRIPTED_VICTORY = FORBIDDEN
```

첫 판 Stage 1에서 실제 골드로 여섯 T1을 각각 한 개씩 직접 설치합니다. 건물 유형에 맞고 첫 전투 진행을 보장하는 안전 노드만 후보로 보여주며, 설치 순서는 플레이어가 정합니다.

세팅 확인 전에는 안전 노드 사이의 무료 이동·교환을 허용합니다. 확인 뒤에는 무료 이동을 종료하고 표준 Run 규칙으로 전환합니다. 아직 설치하지 않은 필수 T1 비용 합계를 실제 골드 지갑에 예약하고, 필수 세트 완료 전 비필수 소비를 차단합니다.

잘못된 건설 거래는 생성·노드 점유·골드 차감을 원자적으로 취소하고 전액 복구합니다. 여섯 T1과 세팅 확인 전에는 첫 룰렛을 열지 않습니다.

```text
Stage 1 = 예고→실제 골드→여섯 T1 설치→세팅 확인→룰렛→병력 결과→비가역 배치→실전 전투→복기→첫 상인
Stage 2 = T2 골드→두 유효 후보 비교→하나 업그레이드→룰렛 통제→다전선 비교
Stage 3 = Stage 1에 설치한 마력탑의 연구 기능→첫 T1 전술→수동 시전
Stage 4 = 학습 시스템을 조합하는 첫 Danger
Stage 5 = 새 시스템 없이 숙련을 확인하는 첫 Boss
```

정확 T1 좌표·비용과 두 T2 후보의 정체는 아직 확정하지 않습니다.

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
[진행 7/10] 첫 10~15분 흐름 — PARTIAL_APPROVAL_5_OF_10
```

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

## 플랫폼 범위

```text
OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1
APPROVED_DUAL_PLATFORM
PC / Steam = COMMITTED
Android / Google Play = COMMITTED
STOVE = SECONDARY_RELEASE_CANDIDATE
iOS = NOT_CURRENT_SCOPE
COMMON_PLATFORM_GATE / PC_RELEASE_GATE / MOBILE_RELEASE_GATE = NOT_RUN
RELEASE_BLOCKED_UNVERIFIED
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
