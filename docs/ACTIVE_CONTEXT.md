# [현행] Active Context

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: CORE_FUN_AND_CONTENT_DEEPENING
current_planning_decision: OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-core-fun-canon-lifecycle-cleanup-20260804
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
codex_execution: BLOCKED_UNTIL_SEPARATE_IMPLEMENTATION_HANDOFF
last_merged_planning_pr: 134
last_merged_planning_commit: 3dc91102607b2e3d184897fb1fd7531f8a3327b3
current_grill_me_count: 1
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`과 `context_baseline_commit`은 실행 시점 저장소 기본 브랜치에서 해석한다. 과거 병합 SHA는 `last_merged_*` 증거 필드에만 보존한다.

## 1. 프로젝트 코어

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
공세 예고
→ 건설·TokenSource 구성
→ 세 원형 릴 회전
→ 3×3 노출창 이동·확정
→ 보관·판매·한 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

세 원형 릴은 3×3 노출창의 세 열이다.

## 2. 현재 핵심 재미 Decision

책임 원본:

`design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`

핵심 4축:

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과
```

Stage 콘텐츠 압력 분류:

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

정확 Stage·적·수치는 후속 Decision이다.

## 3. 현행 자원·건물·HUD

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
상인 = Stage 종료 정비시간
지휘소 = 현재 MapRun 전체 아군 병력 오라
```

- 식량은 현행 핵심 HUD 자원이 아니다.
- 토큰 초당 공급·건물 지속 유지비 없음.
- 금화·병종 토큰은 인게임 금화·T1/T2 병종 이미지를 재사용.
- T3 병종 이미지는 룰렛 병종 토큰에 사용하지 않음.

## 4. 최종 아트 방향

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
```

추가 이미지·실제 아트 제작은 사용자 별도 지시 전 중단한다.

## 5. 문서 수명주기

권위:

- `DOCUMENTATION_MAP.md`
- `DOCUMENT_LIFECYCLE_REGISTRY.md`
- `process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md`

```text
[현행] = 사용 허용
[대체됨] = 후속 정본 사용
[보류] = 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 사실 근거만 허용
```

현재 `[보류]`:

- 구형 첫 10분 벨루 흐름.
- Meta·Hub 문서.
- Hero·Legendary family.

## 6. 적대적 검토 결과

책임 원본:

`reviews/ADVERSARIAL_CORE_FUN_CANON_AND_LEGACY_CONFLICT_REVIEW_2026-08-04.md`

주요 수정:

- PROJECT_CORE 구형 식량·5종 건물 제거.
- 구형 master GDD `[대체됨]` 처리.
- README·AGENTS·Roadmap 최신화.
- fixed current-main 회귀 방지.
- 고아 APPROVED 문서 lifecycle 격리.

## 7. 현재 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = CORE_FUN_AND_CONTENT_GUARDRAILS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 Gate

```text
GRILL_ME_COUNT = 1/10
NEXT_DECISION = STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX
THEN = SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS
NEXT_IMPLEMENTATION = SEPARATELY_AUTHORIZED_CODEX_HANDOFF
```
