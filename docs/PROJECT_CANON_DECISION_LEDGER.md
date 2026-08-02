# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
canonical_main: 7c8be1ba47d4159ca3cead6343c20ef068907bcd
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.2
latest_main_sync: PR_125 / f9334f32bd5ac5142860c991a809b6bc911963c4
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 10
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
preflight: CONTENT_PASS / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED_BEFORE_MERGE
preflight_report: reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md
merge_authorization: NOT_GRANTED
next_gate: USER_EXPLICIT_MERGE_DECISION_AFTER_FINAL_EXACT_HEAD_VERIFICATION
```

이 문서는 현재 승인 Decision·상태·병합 카운트를 소유한다. 제품 정체성은 `PROJECT_CORE.md`, 실제 구현은 `CURRENT_IMPLEMENTATION_STATUS.md`, 질문별 책임 원본은 `DOCUMENTATION_MAP.md`가 소유한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY

TEN_APPROVED_GRILL_ME_DECISIONS
= PREFLIGHT_TRIGGER
!= AUTO_MERGE

CONTENT_PREFLIGHT_PASS
= DOCS_ONLY_ELIGIBLE_AFTER_FINAL_HEAD_REVALIDATION
!= MERGE_AUTHORIZED
```

## 2. 현재 승인 Decision 10건

| Decision ID | 상태 | 결정 | 현재 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 이름 지정 영웅의 기본 공격과 전투 능력은 공개 trigger·고정 ability priority·target priority·결정론적 tie-break에 따라 자동 발동하며 수동 스킬 버튼·수동 타깃 지정은 없다 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | 정확 능력·trigger·priority·tick·수치·runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 이름 지정 영웅은 원본 `[영웅]` 등급 병종과 유사한 평균 총 전투 예산, 조건부 고점, 고유 전술 정체성, 명시적 약점과 원본 선택 사유를 가진 전문화 sidegrade다 | `design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` | 정확 예산식·가중치·허용 편차·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 영웅 사망은 회수 보상을 제공하지 않으며 재출전에는 사망 이후 새 동병종 `[영웅]` 등급 룰렛 결과가 필요하고 새 인스턴스는 최대 HP·준비 상태로 시작한다 | `design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` | provenance fault test·정확 초기값 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 생존 영웅의 HP·쿨다운·충전·고유 자원은 Stage를 넘어 유지하고 일시 전투 상태는 정산에서 제거하며 정비시간에는 영웅 clock을 정지한다 | `design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md` | 영속 동반자 예외·runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | `맵 → MapRun → Stage → Wave → 정산 → 정비시간` 계층을 사용하고 네 가지 운영 기능은 Stage와 정비시간 모두 사용 가능하다 | `design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` | 일반 clock matrix·정확 길이·Wave 편성 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 배치 영웅은 수동 퇴각·교대할 수 없고 생존 시 Stage·Act·정비시간을 넘어 같은 인스턴스로 유지된다 | `design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md` | 사망 연출·로그 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 세 전선 전체 active 이름 지정 영웅은 최대 1명이며 이전 인스턴스 종료 뒤 같은 영웅도 새 적격 토큰으로 반복 출전 가능하다 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | 영웅별 능력·토큰 빈도 simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 룰렛의 동병종 `[영웅]` 등급 토큰을 원본 병종으로 유지하거나 해금된 동병종 영웅 하나로 1:1 변환해 한 전선에 비가역 배치한다 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | 정확 UI·transaction runtime pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 각 영웅은 기존 병종 하나에 고정 연결되며 같은 병종에 복수 영웅을 해금할 수 있고 해금 시 Profile 명부에 영구 등록된다 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | 병종별 영웅 명단·비용 pending |
| `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 베일종은 균열을 통해 유입된 다양한 이계 생물의 통칭이며 상세 문명·정치 설명을 제품 범위로 요구하지 않는다 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | 적 명단·행동·Act 배치 pending |

## 3. 기존 main 승인 연결

- `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1`
- `OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1`
- `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1`
- `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1`
- `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1`
- `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2`

## 4. 영웅 자동 발동 정본

```text
전투 상태 갱신
→ 공개 trigger 평가
→ 고정 ability priority 평가
→ 공개 target filter·priority·tie-break 적용
→ 유효성 재검증
→ 자동 발동
→ cooldown·charge·resource·결과 기록
```

- 플레이어는 영웅 선택·전선 배치·조합·조건 조성으로 통제한다.
- 수동 스킬 버튼·수동 타깃 지정·수동 보류는 금지다.
- 동일 저장 상태와 입력 순서에서는 같은 능력과 대상을 선택한다.
- 저장·Retry로 자동 판단을 재굴림할 수 없다.

## 5. preflight 결과

주 책임 원본:

`reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md`

후보 증거 HEAD `be552b54b96a029dfa042675ae002ad21b96af65`:

```text
CONTENT_PREFLIGHT = PASS
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
PRODUCT_PATHS = 0
COMMENTS = 0
REVIEWS = 0
UNRESOLVED_THREADS = 0
Project Core run 615 = PASS
GDD Sheet run 332 = PASS
Base v9 run 308 = PASS
```

- Base v9.4.1은 PR #124, Base v9.4.2 planning-first adoption은 PR #125로 main→feature 동기화했다.
- Documentation Map의 Vertical Slice·review·Evidence Pilot 계보 누락을 복원했다.
- 과거 `OPEN_P1` CI 행은 역사적 해결 상태로 전환했다.
- 제품 구현 전 parser·simulation·fault test는 `TEST_REQUIRED`로 유지하되 문서-only 병합 blocker와 분리했다.
- 최신 main 동기화 이후 최종 exact HEAD 검증이 필요하다.

## 6. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 병합 상태

```text
CURRENT_PR = 121
CURRENT_COUNT_SINCE_MERGE = 10_OF_10
CONTENT_PREFLIGHT = PASS
FINAL_EXACT_HEAD_REVALIDATION = REQUIRED_BEFORE_MERGE
MERGE_AUTHORIZATION = NOT_GRANTED
DRAFT_MUST_REMAIN = TRUE
AUTO_MERGE = FORBIDDEN
```

최종 exact HEAD가 Green이어도 사용자의 별도 병합 승인 전에는 Ready 전환·병합을 수행하지 않는다.
