# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: GAMEPLAY_HERO_RUN_ROLE_GRILL_ME_READY
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
baseline_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 1
future_merge_cadence: 10
```

## 1. 현재 정본

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 현재 제품은 Legacy 프로토타입이고 최신 기획은 미구현이다.
- 각 MapRun은 별개의 실제 경계 공세다.
- 사용자에게 세계관을 장문으로 공개하지 않는다.
- 베일종은 제품에서 `균열을 통해 넘어온 이계 생물종` 정도로만 설명한다.
- 단일 이계 제국·통일 종족·외교·정치 상세는 현재 범위가 아니다.
- 경계파쇄자는 균열을 고정·확장하고 공세 규칙을 바꾸는 보스급 생물이다.
- 적 콘텐츠는 군집·돌격·원거리·방호·교란·공성 역할로 구분한다.
- 적의 역사보다 행동·위협 대상·대응법을 우선 전달한다.
- 오멘워드는 루메른 왕실 인가 자율 경계대응단이며 플레이어는 현장 지휘관이다.
- 메인 허브 보조 콘텐츠는 주점·허브 병영·연구다.
- 정산 영구재화로 유한 공개 노드를 개방한다.
- 주점 영웅 영입은 랜덤 뽑기가 아닌 결정론적 공개 노드다.

## 2. 보호할 코어

- PC-primary.
- 20 Stage·4막·약 35분.
- 위험 Stage 5·10·15·20.
- 세 물리 릴·비가역 가로 이동·SpinSnapshot.
- 보관·판매·한 라인 비가역 배치.
- 전장 3라인, 건설 노드 1종, 전체 30개.
- MapRun 건물 5종: 금고·농장·타워·전장 병영·지휘소.
- fixed-time capture.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 벨루 비모달 안내자.
- 기본 Profile로 모든 콘텐츠 완료 가능.

## 3. 보조 허브 경계

```text
메인 1순위 = 이어하기·새 작전
보조 시설 = 주점·병영·연구
노드 = 유한·비용/선행/결과 공개
```

- 주점: 영웅 이상 전문 인재 명부·영구 영입.
- 허브 병영: 병사·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 금지: 랜덤 유료 영입, 무한 레벨, 전 구간 배율, 숨은 릴 확률, 자동 플레이.
- 영웅의 정확한 MapRun 참여 방식·능력·출전 상한은 미확정이다.

## 4. current authority

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

## 5. 실제 구현 경계

```text
CURRENT_PRODUCT
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- physical reels and permanent movement
- 30-node topology and five buildings
- paid Retry and Profile save
- minimal extradimensional-creature gameplay scope
- Tavern/Barracks/Research permanent-node hub
- deterministic Hero+ roster
```

## 6. Grill Me 운영

- 현재 승인 카운터는 `1/10`이다.
- 10번째 승인 시 병합 preflight를 실행한다.
- blocker가 있으면 병합하지 않는다.
- 다음 질문부터 세계관 확장이 아니라 실제 플레이 구조를 결정한다.

## 7. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1
= 영입한 영웅이 한 MapRun에서 어떤 방식으로 플레이에 참여하는가
```

```text
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
