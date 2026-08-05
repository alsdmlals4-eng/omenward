# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_1_OF_10
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

## 2. 완료된 6/10 계약

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
PARTIAL_APPROVAL_1_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
BELU_REPLACES_PLAYER_CHOICE = FORBIDDEN
```

- 첫 플레이는 실제 MapRun이다.
- 시스템은 현재 목표와 직접 관련된 시점에 단계적으로 노출한다.
- 실제 경제·전투 결과 규칙을 사용한다.
- 벨루는 목표·선택지·결과 원인을 설명할 수 있지만 플레이어 결정을 대신하지 않는다.
- 시스템 노출 순서·최소 유효 경로·Danger/Boss/상인 노출·실패 규칙·정확 시간은 `PENDING_GRILLME`다.

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
- 사용자가 승인하지 않은 자동화·편성·하드카운터·직접 판매·노출 순서를 추가하지 않는다.
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
