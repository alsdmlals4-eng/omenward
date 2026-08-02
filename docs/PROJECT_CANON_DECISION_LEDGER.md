# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
canonical_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 10
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
preflight_trigger: REACHED
merge_authorization: NOT_GRANTED
next_gate: OMW-OPS-20260802-PR121-TEN-DECISION-PREFLIGHT-V1
```

이 문서는 현재 승인 Decision과 상태를 소유한다. 제품 정체성과 불변 조건은 `PROJECT_CORE.md`, 실제 구현은 `CURRENT_IMPLEMENTATION_STATUS.md`, 질문별 책임 원본은 `DOCUMENTATION_MAP.md`가 소유한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY

TEN_APPROVED_GRILL_ME_DECISIONS
= PREFLIGHT_REQUIRED
!= AUTO_MERGE

HERO_ABILITY_ACTIVATION
= AUTOMATIC_RULE_BASED
= DISCLOSED_TRIGGER_AND_PRIORITY
= DETERMINISTIC_TARGET_AND_TIE_BREAK
!= MANUAL_SKILL_BUTTON
!= MANUAL_TARGETING
```

## 2. 현재 승인 Decision

| Decision ID | 상태 | 결정 | 현재 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 이름 지정 영웅의 기본 공격과 전투 능력은 공개된 trigger·ability priority·target priority·tie-break에 따라 결정론적으로 자동 발동한다. 수동 스킬 버튼·수동 타깃 지정은 없다 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | 영웅별 정확 능력·trigger·priority·수치·runtime 검증 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 이름 지정 영웅은 원본 `[영웅]` 등급 병종과 유사한 평균 총 전투 예산, 조건부 고점, 고유 전술 정체성, 명시적 약점과 원본 선택 사유를 가진 전문화 sidegrade다 | `design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` | 정확 예산식·가중치·허용 편차·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 영웅 사망은 회수 보상을 제공하지 않는다. 재출전에는 사망 이후 룰렛에서 새로 확정된 동병종 `[영웅]` 등급 토큰이 필요하며 새 인스턴스는 최대 HP·준비 상태로 시작한다 | `design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` | provenance fault test·정확 초기값 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 살아 있는 영웅의 HP·쿨다운·충전·고유 자원은 Stage를 넘어 유지하고 일시 전투 상태는 Stage 정산에서 제거하며 정비시간에는 영웅 clock을 정지한다 | `design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md` | 영속 동반자 예외·runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | `맵 → MapRun → Stage → Wave → 정산 → 정비시간` 계층을 사용하고 네 가지 런 운영 기능은 Stage와 정비시간 모두 사용 가능하다 | `design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` | 일반 clock matrix·정확 길이·Wave 편성 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 배치 영웅은 수동 퇴각·교대할 수 없고 생존 시 Stage·Act·정비시간을 넘어 같은 인스턴스로 유지된다 | `design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md` | 사망 연출·로그 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 세 전선 전체의 active 이름 지정 영웅은 최대 1명이며 이전 인스턴스 종료 뒤 같은 영웅도 새 적격 토큰으로 반복 출전 가능하다 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | 영웅별 능력·토큰 빈도 simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 룰렛의 동병종 `[영웅]` 등급 토큰을 원본 병종으로 유지하거나 해금된 동병종 영웅 하나로 1:1 변환해 한 전선에 비가역 배치한다 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | 정확 UI·입력·runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 각 영웅은 기존 병종 하나에 고정 연결되며 같은 병종에 복수 영웅을 해금할 수 있고 해금 시 Profile 명부에 영구 등록된다 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | 병종별 영웅 명단·비용 pending |
| `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 베일종은 균열을 통해 유입된 다양한 이계 생물의 통칭이며 상세 문명·정치 설명을 제품 범위로 요구하지 않는다 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | 적 명단·행동·Act 배치 pending |
| `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1` | `USER_APPROVED / MAIN_SYNCED` | 오멘워드는 루메른 왕실 인가 자율 경계대응단이며 활성 작전에서 제한된 비상 지휘권을 갖는다 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | 세부 법률·인물 pending |
| `OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1` | `USER_APPROVED / MAIN_SYNCED` | 메인 허브에 주점·허브 병영·연구를 두고 유한 공개 노드를 개방한다 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | 비용·노드·정확 콘텐츠 pending |
| `OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1` | `CURRENT_OPERATING_RULE / MAIN_SYNCED_AND_BRANCH_CORRECTED` | 승인 Grill Me 10건마다 적대적 preflight를 실행하고 blocker 0이며 사용자 병합 승인이 있을 때만 병합한다 | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | PR #121 preflight 진행 중·병합 승인 없음 |
| `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1` | `USER_APPROVED / MAIN_SYNCED` | 베일은 현실과 이질적인 외부 법칙 영역의 비의지적 경계 겹침이다 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | 기원·우주론 제품 범위 밖 |
| `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` | `USER_APPROVED / MAIN_SYNCED` | 각 MapRun은 별개의 실제 경계 공세이며 승리는 한 침공로 봉쇄다 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | 지역·콘텐츠 상세 pending |
| `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` | `USER_APPROVED / MAIN_SYNCED` | 수평 해금·제한 편의를 주축으로 하고 상한형 준비 보정을 보조축으로 둔다 | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | exact values·simulation pending |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `INHERITED_APPROVED / MAIN_SYNCED_LOCAL_AUTHORITY` | 메인 허브부터 Retry까지 제품 화면과 정보 위계 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | image·runtime·human validation pending |

## 3. 현재 10건 Grill Me 묶음

1. `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1`
2. `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1`
3. `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1`
4. `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1`
5. `OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1`
6. `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1`
7. `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1`
8. `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1`
9. `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1`
10. `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1`

## 4. 자동 발동 정본

```text
전투 상태 갱신
→ 공개 trigger 평가
→ 고정 ability priority 평가
→ 공개 target filter·priority·tie-break 적용
→ 유효성 재검증
→ 자동 발동
→ cooldown·charge·resource·결과 기록
```

- 플레이어는 영웅 선택·전선 배치·병력 조합·조건 조성으로 통제한다.
- 수동 스킬 버튼·수동 타깃 지정·수동 발동 보류는 금지다.
- 동일 저장 상태와 입력 순서에서는 같은 능력과 대상을 선택해야 한다.
- 저장·Retry로 발동이나 타깃을 재굴림할 수 없다.
- 자동 비효율은 공개된 조건·우선순위·약점으로 예측 가능해야 한다.

## 5. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

검증 필요:

- 자동 발동 조건·우선순위의 이해 가능성.
- 동일 상태에서 결정론적 능력·대상 선택.
- 저장·Retry 재굴림 차단.
- 원본 병종과 영웅 선택률·조건 충족률·조합 시너지.
- 영웅 사망·post-death token provenance fault test.
- 일반 정비시간 clock matrix.

## 6. preflight 상태

```text
CURRENT_PR = 121
CURRENT_COUNT_SINCE_MERGE = 10_OF_10
PREFLIGHT_TRIGGER = REACHED
PREFLIGHT = REQUIRED_IN_PROGRESS
MERGE_AUTHORIZATION = NOT_GRANTED
AUTO_MERGE = FORBIDDEN
```

- preflight finding은 `RESOLVED`, `ACCEPTED_RISK`, `TEST_REQUIRED`, `USER_DECISION_REQUIRED`, `MERGE_BLOCKER` 중 하나로 분류한다.
- P0/P1 blocker가 있으면 병합하지 않는다.
- blocker 0이어도 사용자의 명시적 병합 승인 전에는 Draft를 유지하고 병합하지 않는다.

## 7. 다음 Gate

```text
OMW-OPS-20260802-PR121-TEN-DECISION-PREFLIGHT-V1
= authority·Sheet·PR·CI·review·changed paths·P0/P1 적대적 검증
```
