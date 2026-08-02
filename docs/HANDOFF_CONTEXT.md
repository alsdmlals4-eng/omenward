# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: POST_MERGE_MAIN_CANONICAL
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
pr121_merge_commit: 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
working_branch: NONE
current_planning_pr: NONE
last_merged_planning_pr: 121
base: 9.4.2_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: MERGED_TO_MAIN_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 0
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: PR121_PASS_AND_MERGED
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. `pr121_merge_commit`은 최근 승인 10건을 정본화한 역사적 증거다.

## 1. 최근 완료 작업

- PR #121을 exact HEAD `79cb43b71d0072374a9586bb66dd4a24c3b069a9`에서 최종 검증했다.
- Project Core run 630, GDD Sheet run 347, Base v9 run 324가 통과했다.
- latest main 대비 `ahead 117 / behind 0`, 문서 21개, 제품 경로 0개였다.
- 댓글·리뷰·미해결 스레드는 모두 0이었다.
- Sheet `OPEN_P0`, `OPEN_P1`, `MERGE_BLOCKER` 검색 결과는 모두 0이었다.
- PR #121은 squash 병합됐고 merge commit은 `8337a3eba5ff065b2a7c06c6a6256e5b4951c055`다.

## 2. 현재 제품·기획 경계

- 현재 제품은 Legacy 프로토타입이다.
- 최신 승인 기획은 main 정본이지만 아직 구현되지 않았다.
- 제품 코드·데이터·Scene·Resource는 PR #121에서 변경되지 않았다.
- `APPROVED_PLAN != IMPLEMENTED != VALIDATED`를 유지한다.

## 3. MapRun·영웅 정본

```text
맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간
```

- Stage와 정비시간 모두 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치가 가능하다.
- 이름 지정 영웅은 기존 UnitArchetype에 고정 연결된다.
- 동병종 `[영웅]` 등급 토큰을 원본 병종 또는 해금 영웅으로 1:1 변환한다.
- 세 전선 전체 active 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지한다.
- 생존 영웅은 HP·쿨다운·충전·고유 자원을 Stage 경계 너머로 유지한다.
- 사망은 회수 보상을 제공하지 않으며 사망 이후 새 적격 토큰으로만 재출전한다.
- 이름 지정 영웅은 원본 병종의 순수 상위호환이 아닌 조건부 고점형 전문화 sidegrade다.

## 4. 자동 능력 정본

```text
공개 trigger
→ 고정 ability priority
→ 공개 target priority·tie-break
→ 유효성 재검증
→ 자동 발동
```

- 수동 스킬 버튼·수동 타깃 지정은 없다.
- 동일 저장 상태와 입력 순서는 동일한 능력·대상 결과를 만든다.
- 저장·Retry를 통한 자동 판단 재굴림은 금지한다.

## 5. 현재 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`
- `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md`

## 6. 앞으로의 동일 작업 규칙

- 중요 결정 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 승인 10건마다 적대적 preflight를 실행한다.
- 문서·기획 PR은 blocker 0·필수 CI Green·latest main 동기화·제품 경로 0이면 별도 승인 대기 없이 직접 병합한다.
- blocker가 있으면 수정하고 다시 검증한다.
- GitHub auto-merge는 사용하지 않는다.
- 제품 코드 구현과 제품 코드 PR 병합은 이 standing authorization 범위 밖이다.

## 7. 다음 작업

```text
NEXT_PLANNING_BATCH_SELECTION
```

우선순위 후보:

- HeroAbilitySpec의 첫 영웅 능력 계약.
- 일반 MaintenancePhase clock matrix.
- 병종별 영웅 명단·해금 비용.
- 영웅 토큰 빈도·선택률 simulation 계약.

## 8. 미완료 검증

```text
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_IMPLEMENTATION = NOT_STARTED
```
