# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: GAMEPLAY_HERO_EXIT_REPLACEMENT_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
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
current_grill_me_count: 4
future_merge_cadence: 10
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`current_branch: main`과 `context_baseline_commit`은 현재 정본 기준선이다. 승인 Decision 작성은 `working_branch`에서 진행한다.

## 1. 현재 방향

- 세계관 노출은 `균열에서 넘어온 이계 생물종` 수준으로 제한한다.
- 우선순위는 실제 게임플레이·콘텐츠 구조다.
- 영웅은 사전 편성 캐릭터가 아니라 영웅 등급 보관 토큰의 선택형 변환 후보다.
- 전장 전체의 출전 중 영웅 유닛은 동시에 최대 1명이다.

## 2. 프로젝트 약속

> 공개된 세 전선의 공세를 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 3. 영웅 해금·사용·활성 제한

```text
주점에서 병종별 영웅 영구 해금
→ Profile 명부 등록
→ 룰렛에서 동병종 [영웅] 등급 토큰 획득
→ 보관함에서 원본 유지 또는 해금 영웅 선택
→ active hero가 없으면 1토큰을 1영웅으로 변환
→ 한 전선에 비가역 배치
```

- 하나의 병종에 해금 영웅이 여러 명 존재할 수 있다.
- 별도의 런 시작 전 영웅 등록·계약 단계는 없다.
- 병종이 일치하는 해금 영웅만 변환 후보로 표시한다.
- 변환하지 않아도 원본 영웅 등급 병종을 배치할 수 있다.
- 상·중·하를 합쳐 이름 지정 영웅은 동시에 최대 1명만 출전한다.
- active hero가 있으면 새 토큰은 보관하거나 원본 병종으로 사용할 수 있다.
- 같은 영웅도 이전 인스턴스가 더 이상 출전 중이 아니면 새 토큰으로 다시 배치할 수 있다.
- 반복 출전마다 별도의 영웅 등급 토큰을 소비한다.
- 변환은 추가 병력·전역 패시브·릴 odds 변경을 만들지 않는다.
- 확정 전 취소 가능, 배치 확정 뒤 undo·회수·판매·라인 변경 불가다.

## 4. 최소 세계 배경

- MapRun은 별개의 실제 경계 공세다.
- 베일종은 사용자에게 균열에서 넘어온 다양한 이계 생물로 설명한다.
- 적은 군집·돌격·원거리·방호·교란·공성 역할로 제작한다.
- 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다.
- 오멘워드는 루메른 왕실 인가 자율 경계대응단이며 플레이어는 현장 지휘관이다.

## 5. 메인 허브·영구 성장

```text
1순위 = 이어하기·새 MapRun
2순위 = Profile·영구재화·준비 상태
3순위 = 주점·병영·연구
```

- 주점: 병종별 복수 영웅 후보 해금·명부 관리.
- 허브 병영: 병사·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 랜덤 유료 영입·중복 합성·무한 레벨·전 구간 배율·숨은 릴 확률 조작 금지.

## 6. 보호할 게임 시스템

- 20 Stage·4막·약 35분 목표.
- 위험 Stage 5·10·15·20.
- 상·중·하 세 라인.
- 세 물리 원형 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 future reel structure에 영구 반영하며 undo 없음.
- immutable SpinSnapshot과 명시적 한 번 확정.
- PendingReward 보관·판매·한 라인 비가역 배치.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 접전지 0, 총 30노드.
- MapRun 건물: 금고·농장·타워·전장 병영·지휘소.
- 고정시간 점령·paid Retry 원칙·벨루 비모달 안내자.

## 7. 실제 구현 경계

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
- profile/checkpoint/journal/backup and paid Retry
- minimal extradimensional-creature background
- Tavern/Barracks/Research auxiliary hub
- multi-hero-per-unit unlock roster
- stored Hero-grade token conversion and irreversible deployment
- one active Hero across all lanes; same Hero repeat deployment after slot clears
```

`APPROVED_PLAN != IMPLEMENTED != VALIDATED`.

## 8. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

## 9. Grill Me·병합 규칙

- 승인 Grill Me Decision ID만 카운트한다.
- 현재 카운터는 `4/10`이다.
- 10번째 승인 시 GitHub·Sheet·PR·CI·review·authority path 적대적 preflight를 실행한다.
- blocker가 있으면 병합하지 않는다.

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1
= 현재 영웅이 살아 있을 때 수동 교대·퇴각을 허용하는가, 어떤 사건에서 active 상태가 종료되는가
```

## 11. 경계

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
CURRENT_MERGE_PENDING: NO
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
