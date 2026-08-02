# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: WORLD_VEILSPECIES_PURPOSE_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
current_world_decision: OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_branch: main
context_baseline_commit: 26b0a39fbf576557f2658723dee8405c2ea07a6f
working_branch: NEW_BRANCH_REQUIRED_FOR_NEXT_DECISION
active_base_version: 9.4.0
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / MAIN_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
last_merged_pr: 119
last_planning_merge_commit: 26b0a39fbf576557f2658723dee8405c2ea07a6f
current_grill_me_count: 0
future_merge_cadence: 10
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`current_branch: main`과 `context_baseline_commit`은 현재 정본 기준선을 뜻한다. 다음 Decision은 새 branch·새 Draft PR에서 시작한다.

## 1. 현재 상태

PR #119가 검증된 HEAD `230b250a21d87b7f37a644d227d2a459ba1fddc4`에서 squash 병합됐다.

```text
PR #119: CLOSED / MERGED
MERGE COMMIT: 26b0a39fbf576557f2658723dee8405c2ea07a6f
PREMERGE P0/P1 BLOCKER: 0
REQUIRED CI: 3 GREEN
PRODUCT PATH CHANGES: 0
GRILL ME COUNTER: 0/10
```

## 2. 프로젝트 약속

> 공개된 세 전선의 공세를 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 3. 현재 세계 정본

### MapRun

- 하나의 MapRun은 징조로 감지된 별개의 실제 경계 공세다.
- 20 Stage·4막은 한 공세가 고조되는 과정이다.
- 승리는 하나의 균열·침공로 봉쇄, 패배는 실제 전진 방어선 붕괴다.
- paid Retry는 시간 되감기가 아닌 같은 공세의 비상 재투입이다.

### 베일

- 현실과 이질적인 외부 법칙 영역의 비의지적 경계 겹침.
- 균사·혈관·결정형 증식은 법칙 충돌의 물질 패턴.
- 공세별 베일 법칙은 유한·관측·반복 가능해야 한다.
- 베일종은 별도 지성·목적을 가질 수 있으며 다음 세계관 Decision에서 확정한다.

### 오멘워드

- 루메른 왕실의 법적 인가를 받은 전문 경계대응단.
- 평시에는 감독·예산 감사·지방 협조.
- 활성 작전에서는 지정 구역·기간·배속 전력에 한정된 현장 자율권.
- 영구 통치·무제한 징발·상시 왕국군 지휘·일반 사법권은 없음.
- 플레이어는 작전 지휘관이며 통치자가 아니다.

## 4. 메인 허브·영구 성장

```text
1순위 = 이어하기·새 MapRun
2순위 = Profile·영구재화·현재 준비 상태
3순위 = 주점·병영·연구
```

- 주점: 영웅 이상 전문 인재의 공개 결정론적 영입·명부.
- 허브 병영: 병사 훈련·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·징조 분석·편의 sidegrade.
- 영구 노드는 유한하고 비용·선행·결과를 구매 전에 공개한다.
- 기본 Profile로 모든 콘텐츠 완료 가능.
- 랜덤 유료 영입·무한 레벨·전 구간 전투 배율·숨은 릴 확률 조작 금지.
- 영구재화 balance는 노드·Retry 소비, total은 비감소 milestone 판정.

정확 비용·노드 수·영웅 목록·등급·능력·출전 상한은 pending이다.

## 5. 보호할 게임 시스템

- 20 Stage·4막·약 35분 목표.
- 위험 Stage 5·10·15·20.
- 상·중·하 세 라인.
- 세 물리 원형 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 future reel structure에 영구 반영, undo 없음.
- immutable SpinSnapshot과 명시적 한 번 확정.
- PendingReward 보관·판매·한 라인 비가역 배치.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 접전지 0, 총 30노드.
- MapRun 건물: 금고·농장·타워·전장 병영·지휘소.
- 고정시간 점령.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 정본 안내자 벨루.

## 6. 실제 구현 경계

```text
CURRENT_LEGACY
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- three physical reels and permanent movement
- 30-node topology and five MapRun buildings
- fixed-time capture
- profile/checkpoint/journal/backup
- paid Retry
- real-incursion world and Veil ontology
- royal-chartered Omenward organization
- Tavern/Barracks/Research auxiliary hub
- deterministic Hero+ roster recruitment
```

`APPROVED_PLAN != IMPLEMENTED != VALIDATED`.

## 7. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

PR #116은 역사 승인 증거이며 current local authority가 아니다.

## 8. Grill Me·병합 규칙

- 승인 Grill Me Decision ID만 카운트한다.
- 현재 카운터는 `0/10`이다.
- 10번째 승인 시 GitHub·Sheet·PR·CI·review·authority path 적대적 preflight를 실행한다.
- P0/P1 blocker가 있으면 병합하지 않는다.
- 직접 사용자 병합·보류 지시는 10건 주기보다 우선한다.

## 9. 다음 Gate

```text
OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
= 베일종·경계파쇄자의 발생·지성·사회·침공 목적
```

## 10. 경계

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
CURRENT_MERGE_PENDING: NO
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
