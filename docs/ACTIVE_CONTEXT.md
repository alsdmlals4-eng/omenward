# [현행] Active Context

```yaml
updated_at: 2026-08-05
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: CORE_FUN_AND_CONTENT_DEEPENING
current_planning_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
lifecycle_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-building-branches-20260805
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
codex_execution: BLOCKED_UNTIL_SEPARATE_IMPLEMENTATION_HANDOFF
last_merged_planning_pr: 136
last_merged_planning_commit: b1b1f5ff4af9b7e53df12f282415daf7fde30a9b
last_maintenance_recovery_pr: 137
last_maintenance_recovery_commit: a426aef7738a2d9aa8c40cf1eddbe97601e22f80
current_grill_me_count: 3_OF_10
max_approval_batch: 10
early_checkpoint: HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
tdd: RED → GREEN → REFACTOR
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`과 `context_baseline_commit`은 실행 시점 저장소 기본 브랜치에서 해석한다. 과거 SHA는 `last_merged_*` 증거 필드에만 보존한다.

## 1. 프로젝트 코어

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
Stage 압력·Wave 순서 확인
→ 건설·TokenSource 구성
→ 룰렛 회전·3×3 이동·확정
→ 보관·판매·한 전선 비가역 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

## 2. 현재 Decision — 건물 6종 전문화

책임 원본:

`design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
```

- 선택은 건물 인스턴스별이다.
- 다른 인스턴스는 서로 다른 분기를 선택할 수 있다.
- 모든 분기는 얻는 것과 포기하는 것을 함께 표시한다.
- T3는 결과 곡선·표적 우선순위·전선 교리·Route 대응·자원 사용 시점을 바꾼다.
- 정확한 비용·배율·범위·쿨다운은 시뮬레이션 전 미확정이다.

```text
금고 = 안정/행운
농장 = 징집/예비
병영 = 전열/기동
방어탑 = 연사/포격
지휘소 = 돌격/수비
마력탑 = 유량/저장
```

## 3. Stage 압력 의존성

```text
MapRun = 20 Stage
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

건물만으로 카운터를 완성하지 않는다. Decision 4/10 병종과 Decision 5/10 전술이 압력별 최소 두 대응 경로를 채워야 한다.

## 4. 자원·HUD·아트

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
상인 = Stage 종료 정비시간
STYLE = PIXEL_ILLUSTRATION_HYBRID
```

- 식량·토큰 초당 공급·건물 유지비는 현행 규칙이 아니다.
- 룰렛은 인게임 금화·T1/T2 병종 이미지를 재사용한다.
- T3 병종 이미지는 룰렛 토큰에 사용하지 않는다.
- 추가 이미지와 실제 아트 제작은 중단 상태를 유지한다.

## 5. 작업 운영

책임 원본:

`process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md`

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = 고위험 충돌 / 세션 종료 / 대규모 정본 영향
TDD = RED → GREEN → REFACTOR
GITHUB_WRITE = EXPLICIT_NON_DEFAULT_BRANCH_ONLY
```

이번 작업의 RED 증거는 Project Core Documentation run 888이다. 기존 검증은 통과했고 새 건물 정본·운영 정책·3/10 라우팅 부재 때문에만 실패했다.

## 6. 현재 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = BUILDING_BRANCH_CANON_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 다음 Gate

```text
GRILL_ME_COUNT = 3/10
NEXT_DECISION = OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
THEN = OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-STONE-V1
NEXT_IMPLEMENTATION = SEPARATELY_AUTHORIZED_CODEX_HANDOFF
```
