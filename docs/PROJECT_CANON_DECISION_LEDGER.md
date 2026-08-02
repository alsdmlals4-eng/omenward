# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / MAIN_CANONICAL
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
pr121_merge_commit: 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
working_branch: NONE
active_base: 9.4.3
last_merged_planning_pr: 121
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 0
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: PR121_PASS_AND_MERGED
next_gate: NEXT_PLANNING_BATCH_SELECTION
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. `pr121_merge_commit`은 아래 승인 10건을 main 정본으로 만든 역사적 증거다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY

MERGED_TO_MAIN
= CURRENT_PLANNING_CANON
!= PRODUCT_IMPLEMENTED

TEN_APPROVED_GRILL_ME_DECISIONS
= PREFLIGHT_TRIGGER
```

## 2. PR #121에서 main에 병합된 Decision 10건

| Decision ID | 상태 | 결정 | 현재 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 이름 지정 영웅의 기본 공격과 전투 능력은 공개 trigger·고정 ability priority·target priority·결정론적 tie-break에 따라 자동 발동하며 수동 스킬 버튼·수동 타깃 지정은 없다 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | 정확 능력·trigger·priority·tick·수치·runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 이름 지정 영웅은 원본 `[영웅]` 등급 병종과 유사 평균 총 전투 예산, 조건부 고점, 고유 전술 정체성, 명시적 약점을 가진 전문화 sidegrade다 | `design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` | 예산식·가중치·허용 편차·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 영웅 사망은 회수 보상을 제공하지 않으며 사망 이후 새 동병종 `[영웅]` 룰렛 결과로만 새 인스턴스를 재출전한다 | `design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` | provenance fault test·정확 초기값 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 생존 영웅의 HP·쿨다운·충전·고유 자원은 Stage를 넘어 유지하고 일시 전투 상태는 정산에서 제거한다 | `design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md` | 영속 동반자 예외·runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | `맵 → MapRun → Stage → Wave → 정산 → 정비시간` 계층과 Stage/정비시간 운영 기능을 사용한다 | `design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` | clock matrix·정확 길이·Wave 편성 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 배치 영웅은 수동 퇴각·교대할 수 없고 생존 시 같은 인스턴스로 유지된다 | `design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md` | 사망 연출·로그 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 세 전선 전체 active 이름 지정 영웅은 최대 1명이며 종료 뒤 같은 영웅도 새 적격 토큰으로 반복 출전 가능하다 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | 능력·토큰 빈도 simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 동병종 `[영웅]` 토큰을 원본 병종 또는 해금 영웅 하나로 1:1 변환해 한 전선에 비가역 배치한다 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | UI·transaction runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 각 영웅은 기존 병종 하나에 고정 연결되며 같은 병종에 복수 영웅을 영구 해금·등록할 수 있다 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | 영웅 명단·비용 pending |
| `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1` | `MERGED_TO_MAIN / NOT_IMPLEMENTED` | 베일종은 균열을 통해 유입된 다양한 이계 생물의 통칭이며 상세 문명·정치 설명을 제품 범위로 요구하지 않는다 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | 적 명단·행동·Act 배치 pending |

## 3. 병합 증거

```text
PR = 121
PR_HEAD = 79cb43b71d0072374a9586bb66dd4a24c3b069a9
MERGE_METHOD = SQUASH
PR121_MERGE_COMMIT = 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
PREMERGE_PROJECT_CORE_RUN = 630_PASS
PREMERGE_GDD_SHEET_RUN = 347_PASS
PREMERGE_BASE_V9_RUN = 324_PASS
PREMERGE_BEHIND_MAIN = 0
PREMERGE_PRODUCT_PATHS = 0
PREMERGE_OPEN_P0 = 0
PREMERGE_OPEN_P1 = 0
PREMERGE_MERGE_BLOCKER = 0
```

## 4. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 5. 카운터와 향후 병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 0_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 중요 결정은 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 문서·기획 PR은 10건 preflight가 Green이고 blocker 0이면 standing user authorization에 따라 별도 승인 대기 없이 병합한다.
- GitHub auto-merge 기능은 사용하지 않는다.
- 제품 코드 구현·병합은 이 standing authorization의 범위가 아니다.
