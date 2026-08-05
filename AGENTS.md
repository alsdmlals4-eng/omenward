# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_count: 6_OF_10
next_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
work_mode: TOTAL_PLANNING
product_code_authority: NONE
image_generation: STOPPED_BY_USER
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

## 2. 현재 6/10 계약

전술·마력 5/10 완료 계약:

```text
자원 = 골드 / 마력 / 배치 병력·병력 한도 / 이동권
마력탑 최대 활성 수 = 1
마력탑 = T1 → T2 → T3
마력탑 분기 = FORBIDDEN
연구 = 골드 + 시간
시전 = 마력
동시 연구 = 1
Stage 전 편성 = 없음
자동 시전 = 금지
새 MapRun = 마력탑 Tier·연구·해금·보유 마력 초기화
```

Stage 종료 상인 6/10 현행 계약:

```text
Stage 1~19 종료 정비시간 방문
Stage 20 상인 = FORBIDDEN
재고 = 룰렛 제어 / 복구 / 성장 보조 / 가변 기회
재고 = 방문별 유한
구매 통화 = 골드
상시 HUD 상점 = FORBIDDEN
무한 구매·무한 reroll = FORBIDDEN
```

- 이동권이 3 미만이면 이동권, 3/3이면 다음 룰렛 1회 할인을 제시한다.
- 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기를 직접 판매하지 않는다.
- 상인은 기존 시스템을 보정하지만 우회하지 않는다.
- 정확 가격·재고·등장률·할인율은 `PENDING_SIMULATION`이다.

## 3. 작업 방식

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
- 제품 변경은 별도 구현 계획과 제품 RED 테스트 전 금지한다.
- 사용자가 승인하지 않은 자동화·편성·하드카운터·직접 판매를 추가하지 않는다.
- PR 병합 전 fresh CI·Sheet read-back·리뷰 thread·차단 표식을 다시 확인한다.

## 4. 역할 분리

- GPT: 핵심 재미·콘텐츠·플레이어 경험·UX·아트 방향·정본 동기화.
- Codex: 자료구조·알고리즘·좌표·경로·성능·제품 코드·제품 테스트.
- Google Sheet: GitHub Decision의 운영 미러이며 독립 권위가 아니다.

## 5. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
LEGACY_C1_C2_C3_PROVEN
```

제품 코드·Scene·Resource·게임 데이터·실제 아트 자산은 현행 6/10 문서 병합으로 자동 승인되지 않는다.
