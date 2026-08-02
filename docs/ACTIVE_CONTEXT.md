# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: GAMEPLAY_HERO_RUN_ROLE_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_branch: main
context_baseline_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base_version: 9.4.0
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
last_merged_pr: 120
last_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
current_grill_me_count: 1
future_merge_cadence: 10
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`current_branch: main`과 `context_baseline_commit`은 현재 정본 기준선이다. 승인 Decision 작성은 `working_branch`에서 진행한다.

## 1. 현재 방향

사용자는 세계관을 제품 전면에 공개하지 않고 게임 기획을 우선하기로 했다.

```text
WORLD_LORE_EXPOSURE = MINIMAL
PLAYER_EXPLANATION = 균열에서 넘어온 이계 생물종
NEXT_PRIORITY = GAMEPLAY_AND_CONTENT_DESIGN
```

## 2. 프로젝트 약속

> 공개된 세 전선의 공세를 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 3. 최소 세계 배경

### MapRun

- 하나의 MapRun은 별개의 실제 경계 공세다.
- 20 Stage·4막은 한 공세의 고조 과정이다.
- 승리는 한 균열·침공로 봉쇄, 패배는 실제 방어선 붕괴다.
- paid Retry는 시간 되감기가 아닌 같은 공세의 비상 재투입이다.

### 베일·이계 생물

- 베일은 현실과 이질적인 외부 법칙 영역의 비의지적 경계 겹침이다.
- 베일종은 사용자에게 `균열에서 넘어온 이계 생물종` 정도로 설명한다.
- 단일 제국·통일 종족·외교 정본을 현재 제품에 요구하지 않는다.
- 적은 군집·돌격·원거리·방호·교란·공성 역할로 설계한다.
- 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다.
- 적의 역사보다 관측 행동·위협 대상·대응법을 전달한다.

### 오멘워드

- 루메른 왕실 인가 자율 경계대응단.
- 플레이어는 활성 작전 지휘관이며 통치자가 아니다.
- 상세 정치·법률·왕실 인물은 현재 게임플레이 설계 우선순위가 아니다.

## 4. 메인 허브·영구 성장

```text
1순위 = 이어하기·새 MapRun
2순위 = Profile·영구재화·준비 상태
3순위 = 주점·병영·연구
```

- 주점: 영웅 이상 전문 인재의 공개 결정론적 영입.
- 허브 병영: 병사·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 영구 노드는 유한하고 비용·선행·결과를 구매 전에 공개한다.
- 기본 Profile로 모든 콘텐츠 완료 가능.
- 랜덤 유료 영입·무한 레벨·전 구간 배율·숨은 릴 확률 조작 금지.
- 영웅의 정확한 MapRun 참여 방식은 아직 미확정이다.

## 5. 보호할 게임 시스템

- 20 Stage·4막·약 35분 목표.
- 위험 Stage 5·10·15·20.
- 상·중·하 세 라인.
- 세 물리 원형 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 future reel structure에 영구 반영하며 undo 없음.
- immutable SpinSnapshot과 명시적 한 번 확정.
- PendingReward 보관·판매·한 라인 비가역 배치.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 접전지 0, 총 30노드.
- MapRun 건물: 금고·농장·타워·전장 병영·지휘소.
- 고정시간 점령.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 벨루 비모달 안내자.

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
- real-incursion and minimal extradimensional-creature background
- Tavern/Barracks/Research auxiliary hub
- deterministic Hero+ recruitment
```

`APPROVED_PLAN != IMPLEMENTED != VALIDATED`.

## 7. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

## 8. Grill Me·병합 규칙

- 승인 Grill Me Decision ID만 카운트한다.
- 현재 카운터는 `1/10`이다.
- 10번째 승인 시 GitHub·Sheet·PR·CI·review·authority path 적대적 preflight를 실행한다.
- blocker가 있으면 병합하지 않는다.
- 직접 사용자 병합·보류 지시는 주기보다 우선한다.

## 9. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1
= 영입한 영웅이 한 MapRun에서 어떤 방식으로 플레이에 참여하는가
```

## 10. 경계

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
CURRENT_MERGE_PENDING: NO
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
