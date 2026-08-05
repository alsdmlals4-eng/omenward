# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-06
current_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_4_OF_10
current_working_pr: 142
work_mode: TOTAL_PLANNING
product_code_authority: NONE
image_generation: NOT_AUTHORIZED
```

## 1. 작업 시작 순서

1. `docs/PROJECT_CORE.md`
2. `docs/ACTIVE_CONTEXT.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
5. `docs/OMENWARD_GDD_CURRENT_CANON.md`
6. 현재 Decision 책임 원본과 적대적 검토
7. `docs/CURRENT_IMPLEMENTATION_STATUS.md`

대상 파일이 `[현행]`인지 확인하지 않고 구현 입력으로 사용하지 않는다.

## 2. 완료된 5/10·6/10 계약

5/10 전술스킬·마력 계보는 단일 선형 마력탑, 골드+시간 연구, 수동 마력 시전 계약을 유지한다.

Stage 종료 상인은 Stage 1~19 종료 정비시간에만 방문하고 Stage 20 뒤에는 MapRun 최종 정산으로 이동한다. 재고는 룰렛 제어·복구·성장 보조·가변 기회의 유한 4칸이며 구매 통화는 골드다.

```text
ALWAYS_AVAILABLE_HUD_SHOP = FORBIDDEN
INFINITE_PURCHASE = FORBIDDEN
INFINITE_REROLL = FORBIDDEN
DIRECT_CORE_REWARD_SALE = FORBIDDEN
EXACT_NUMERICS = PENDING_SIMULATION
```

## 3. 현행 7/10 부분 승인 계약

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10_IN_PROGRESS
PARTIAL_APPROVAL_4_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_FOUNDATION_THEN_BRANCH_CHOICE
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_BUILDING_BRANCH_CHOICE = NONE
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
T2_UPGRADE_PREVIEW = REQUIRED
MANA_TOWER_T1_INCLUDED_IN_STAGE_1_SET = REQUIRED
MANA_TOWER_STAGE_1_EXPLANATION = BRIEF_RESOURCE_ROLE_ONLY
TACTICAL_RESEARCH_EXPLANATION_BEFORE_STAGE_3 = FORBIDDEN
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
BELU_REPLACES_PLAYER_CHOICE = FORBIDDEN
```

- 첫 판 1스테이지에서 금고·농장·병영·방어탑·지휘소·마력탑 T1을 각각 한 개씩 직접 설치한다.
- Stage 1 지급 골드는 여섯 T1의 실제 비용을 감당할 수 있어야 한다.
- 각 T1 설명은 이름·역할 한 문장·아이콘으로 제한하며 상세는 툴팁에서 재확인한다.
- T1 설치는 기초 세팅이지 분기 선택이 아니다.
- 첫 전투 판단은 Stage 1의 비가역 병력 배치다.
- 첫 건물 전략 판단은 Stage 2의 T2 업그레이드다.
- Stage 2는 현재 압력에 유효한 T2 후보 두 개를 보여주고 하나를 지을 실제 골드를 지급한다.
- T2 선택 전 이득·포기·현재 압력 관계·룰렛/전투 영향을 비교한다.
- 마력탑은 Stage 1에 설치하지만 전술 연구 설명은 Stage 3까지 금지한다.
- 첫 상인은 선택 사항과 골드 기회비용만 설명한다.
- 벨루는 목표·선택지·결과 원인을 설명할 수 있지만 플레이어 결정을 대신하지 않는다.

미승인 범위:

```text
T1_PLACEMENT_LAYOUT = PENDING_GRILLME
T1_BUILD_ORDER = PENDING_GRILLME
STAGE_1_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
STAGE_1_NON_T1_SPENDING_RULE = PENDING_GRILLME
FIRST_T2_UPGRADE_CANDIDATE_IDENTITIES = PENDING_GRILLME
STAGE_2_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

## 4. 작업 방식

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH: 10
EARLY_CHECKPOINT = HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
TDD_MANDATORY
RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE: FORBIDDEN
```

- 기획 변경도 실패 조건을 먼저 테스트로 기록한다.
- 승인된 내용은 같은 Decision ID로 GitHub와 Google Sheet에 동기화한다.
- 제품 변경은 별도 구현 계획과 제품 RED 테스트 전 금지한다.
- 사용자가 승인하지 않은 건물 위치·정확 비용·잔여 골드 처리·T2 후보 정체를 추가하지 않는다.
- 구형 `PREBUILT T1` 시작과 장문 T1 설명을 구현 입력으로 사용하지 않는다.
- PR 병합 전 fresh CI·Sheet read-back·review thread·차단 표식을 다시 확인한다.

## 5. 역할 분리

- GPT: 핵심 재미·콘텐츠·플레이어 경험·UX·아트 방향·정본 동기화.
- Codex: 자료구조·알고리즘·좌표·경로·성능·제품 코드·제품 테스트.
- Google Sheet: GitHub Decision의 운영 미러이며 독립 권위가 아니다.

## 6. 완료 이력

```text
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
LEGACY_C1_C2_C3_PROVEN
```

제품 코드·Scene·Resource·게임 데이터·실제 아트 자산은 현행 문서 체크포인트로 자동 승인되지 않는다.

## 7. 플랫폼 출시·에셋 권리

출시 플랫폼, 외부 자산, AI·외주·참조 기반 독립 제작 작업은 다음 프로젝트 증거를 읽는다.

- `docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md`
- `docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md`
- `docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md`
- `docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md`

플랫폼 운영 Decision은 `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`이다.

```text
platform_decision = APPROVED_DUAL_PLATFORM
release_strategy = STAGED_CROSS_PLATFORM
PC = COMMITTED
Steam = COMMITTED_PRIMARY_STORE
STOVE = SECONDARY_RELEASE_CANDIDATE
Android = COMMITTED
Google Play = COMMITTED_PRIMARY_STORE
iOS = NOT_CURRENT_SCOPE
simultaneous release = NOT_COMMITTED
```

PC·Steam과 Android·Google Play 지원 범위는 승인됐지만, 플랫폼별 PASS는 독립이다. `COMMON_PLATFORM_GATE`, `PC_RELEASE_GATE`, `MOBILE_RELEASE_GATE`를 각각 판정하며 한 Gate의 PASS를 다른 Gate에 전이하지 않는다. STOVE는 별도 상점 Gate 전 출시 확정이 아니다.

원본을 조금 수정하거나 AI로 변환했다는 이유만으로 독립 자산으로 보지 않고 `reference_brief`, `forbidden_expression`, 별도 `final_asset_record`, 유사성 검토를 요구한다.

필수 권리·계약·약관 버전·설문·build/store 일치·플랫폼별 구현과 검증 중 하나라도 미확인이면 `RELEASE_BLOCKED_UNVERIFIED`다. 자산 감사, 런타임 검증, 상점 제출, 최종 등급, 법률 검토는 현재 `NOT_RUN / NOT_ASSIGNED`다. 현재 기획 7/10 부분 승인과 제품 코드 권한 없음 상태를 변경하지 않는다.
