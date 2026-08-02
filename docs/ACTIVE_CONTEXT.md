# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: POST_MERGE_MAIN_CANONICAL
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_branch: main
context_baseline_commit: 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
working_branch: NONE
active_base_version: 9.4.2
current_product: LEGACY_PROTOTYPE
latest_planning: MERGED_TO_MAIN / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
last_merged_pr: 121
last_merge_commit: 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
current_pr: NONE
current_grill_me_count: 0
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: PR121_PASS_AND_MERGED
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

## 1. 현재 상태

- PR #121은 2026-08-02에 squash 병합됐다.
- 병합 commit은 `8337a3eba5ff065b2a7c06c6a6256e5b4951c055`다.
- 승인 10건은 이제 main 정본이며 Grill Me 카운터는 `0/10`으로 초기화됐다.
- 현재 제품은 여전히 Legacy 프로토타입이고 최신 승인 기획은 미구현이다.
- 제품 코드·데이터·Scene·Resource는 PR #121에서 변경되지 않았다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 2. 현재 제품 방향

- 공식 흐름은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- MapRun 목표는 20 Stage·4막·약 35분이며 위험 Stage는 5·10·15·20이다.
- 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치는 Stage와 정비시간 모두 사용할 수 있다.
- 세 물리 원형 릴·비가역 가로 이동·immutable SpinSnapshot을 보호한다.
- 상·중·하 3전선과 총 30개 건설 노드, 다섯 MapRun 건물을 보호한다.
- 기본 Profile과 원본 병종만으로 모든 콘텐츠 완료 가능성을 유지한다.
- 무한 성장·숨은 릴 확률·전역 multiplier·자동 플레이는 금지한다.

## 3. 영웅 정본

```text
기존 UnitArchetype
→ 이름 지정 영웅 결정론적 해금·Profile 등록
→ 룰렛 동병종 [영웅] 등급 토큰
→ 원본 병종 또는 해금 영웅 선택
→ 전역 active slot 검사
→ 1토큰을 1유닛으로 변환·한 전선 비가역 배치
→ 공개 규칙 기반 자동 능력 운용
```

- 세 전선 전체 active 이름 지정 영웅은 동시에 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 생존 영웅의 HP·쿨다운·충전·사용 횟수·고유 자원은 Stage를 넘어 유지한다.
- 일시 전투 상태와 임시 파생 개체는 Stage 정산에서 제거한다.
- 영웅 사망은 회수 보상·부활권·보장·pity를 제공하지 않는다.
- 이름 지정 영웅 재출전에는 사망 이후 새 동병종 `[영웅]` 룰렛 결과가 필요하다.
- 이름 지정 영웅은 원본 병종과 유사한 평균 전투 예산의 조건부 고점형 전문화 sidegrade다.

## 4. 영웅 자동 능력

```text
전투 상태 갱신
→ 공개 trigger 평가
→ 고정 ability priority 평가
→ 공개 target filter·priority·tie-break 적용
→ 유효성 재검증
→ 자동 발동
→ 결과 상태 기록
```

- 기본 공격과 이름 지정 영웅 전투 능력은 `AUTOMATIC_RULE_BASED`다.
- 수동 스킬 버튼·수동 타깃 지정·숨은 명령 큐는 없다.
- 동일 저장 상태와 입력 순서에서는 같은 능력과 대상을 선택한다.
- 저장·Retry로 자동 판단을 재굴림할 수 없다.

## 5. 현재 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
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

## 6. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MERGED_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 향후 동일 작업 운영

- 승인된 중요 결정은 GitHub 정본과 Sheet에 같은 Decision ID로 즉시 반영한다.
- 승인 10건마다 적대적 preflight를 수행한다.
- 문서·기획 PR이 latest main 동기화, 필수 CI Green, Sheet read-back, `OPEN_P0=0`, `OPEN_P1=0`, `MERGE_BLOCKER=0`, 제품 경로 0을 만족하면 별도 승인 대기 없이 Ready 전환·병합한다.
- blocker가 있으면 먼저 수정하고 같은 preflight를 반복한다.
- GitHub auto-merge 기능은 사용하지 않고 검증 직후 명시적 expected HEAD로 직접 병합한다.
- 이 standing authorization은 제품 코드 구현·병합으로 자동 확장되지 않는다.

## 8. 다음 Gate

```text
NEXT_PLANNING_BATCH_SELECTION
```
