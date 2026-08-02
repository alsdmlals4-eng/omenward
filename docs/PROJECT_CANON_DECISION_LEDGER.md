# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
canonical_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 1
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1
```

이 문서는 현재 승인 Decision과 상태를 소유한다. 제품 정체성과 불변 조건은 `PROJECT_CORE.md`, 실제 구현은 `CURRENT_IMPLEMENTATION_STATUS.md`, 질문별 책임 원본은 `DOCUMENTATION_MAP.md`가 소유한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY

RECOMMENDED_DEFAULT
!= USER_APPROVED_VALUE
!= IMPLEMENTED_VALUE
!= VALIDATED_VALUE

PLAYER_FACING_MINIMAL_LORE
!= INTERNAL_GAMEPLAY_RULE_ABSENT
```

## 2. 현재 승인 Decision

| Decision ID | 상태 | 결정 | 현재 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 베일종은 균열을 통해 유입된 다양한 이계 생물의 통칭이며 사용자에게 상세 문명·정치 설명을 제공하지 않는다. 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | 적 명단·Act 배치·정확 행동·수치 pending |
| `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1` | `USER_APPROVED / MAIN_SYNCED` | 오멘워드는 루메른 왕실 인가 자율 경계대응단이며 활성 작전에서 제한된 비상 지휘권을 갖는다 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | 정치 인물·법률명 상세 pending |
| `OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1` | `USER_APPROVED / MAIN_SYNCED` | 메인 허브에 주점·허브 병영·연구를 두고 정산 영구재화로 유한 공개 노드를 개방한다 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | 비용·노드·영웅·능력 pending |
| `OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1` | `CURRENT_OPERATING_RULE / MAIN_SYNCED` | 승인 Grill Me 10건마다 적대적 병합 preflight를 실행하고 blocker 0일 때만 병합한다 | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | 현재 카운터 `1/10` |
| `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1` | `USER_APPROVED / MAIN_SYNCED` | 베일은 현실과 이질적인 외부 법칙 영역의 비의지적 경계 겹침이다 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | 기원·우주론은 제품 범위 밖 |
| `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` | `USER_APPROVED / MAIN_SYNCED` | 각 MapRun은 별개의 실제 경계 공세이며 승리는 한 침공로 봉쇄다 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | 지역·콘텐츠 상세 pending |
| `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` | `USER_APPROVED / MAIN_SYNCED` | 수평 해금·제한 편의를 주축으로 하고 상한형 준비 보정을 보조축으로 둔다 | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | exact values·simulation pending |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `INHERITED_APPROVED / MAIN_SYNCED_LOCAL_AUTHORITY` | 메인 허브부터 Retry까지 제품 화면과 정보 위계 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | image·runtime·human validation pending |

## 3. 이계 생물종 게임플레이 정본

```text
PLAYER_EXPLANATION = 균열에서 넘어온 이계 생물종
INTERNAL_TERM = 베일종
SINGLE_RACE_OR_EMPIRE = NO
DETAILED_POLITICS_AND_DIPLOMACY = OUT_OF_SCOPE
BOUNDARY_BREAKER = BREACH_STABILIZING_BOSS_ORGANISM
```

- 베일종은 하나의 문명이나 통일 종족이 아니라 다양한 이계 생물의 통칭이다.
- 사용자에게 필요한 것은 기원 강의가 아니라 관측 가능한 행동·위협 대상·대응법이다.
- 공세 집결은 군체 행동·포식 본능·우두머리 신호·균열 반응으로 설명할 수 있다.
- 고등 지성 존재 가능성은 닫지 않지만 현재 제품에 외교·정치 콘텐츠를 요구하지 않는다.
- 경계파쇄자는 균열을 고정·확장하고 공세 규칙을 바꾸는 보스급 공성 생물이다.
- 장문의 세계관 도감 없이 전조·행동·결과 로그로 기능을 전달한다.

### 적 제작 역할 분류

```text
군집형 / 돌격형 / 원거리형 / 방호형 / 교란형 / 공성형 / 경계파쇄자
```

이는 정확한 최종 적 명단이 아니라 Act·Stage 콘텐츠를 설계하기 위한 역할 분류다.

## 4. 보호된 제품 코어

> 공개된 세 전선의 위험을 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

- PC-primary.
- 20 Stage·4막·약 35분 목표.
- 위험 Stage 5·10·15·20.
- 세 물리 릴·TokenInstance·cursor·3×3 노출.
- immutable SpinSnapshot과 명시적 확정.
- 보관·판매·한 라인 비가역 배치.
- 상·중·하 3라인·고정시간 점령.
- 건설 노드 1종·전체 30개.
- 금고·농장·타워·전장 병영·지휘소.
- 실제 경계 공세·국소 봉쇄·상흔.
- 벨루 비모달 안내자.

## 5. 메인 허브·Profile 정본

```text
PRIMARY_ACTION = MAPRUN_ENTRY
AUXILIARY = TAVERN + HUB_BARRACKS + RESEARCH
CURRENCY = SETTLED_PERMANENT_CURRENCY_BALANCE
NODE_GRAPH = FINITE / VISIBLE / DETERMINISTIC
```

- 주점: 영웅 이상 전문 인재의 영구 영입. 랜덤 뽑기·유료 재굴림·중복 합성 금지.
- 허브 병영: 병사·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 기본 Profile로 모든 콘텐츠 완료 가능.
- exact cost·node count·hero roster·ability·deployment cap은 pending.

## 6. 실제 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage restart

LATEST_APPROVED_NOT_IMPLEMENTED
- three physical reels and permanent horizontal movement
- 30-node topology and five MapRun buildings
- fixed-time capture
- paid Retry and Profile save
- real-incursion world and minimal Veil-species gameplay scope
- Tavern/Barracks/Research permanent-node hub
- deterministic Hero+ roster recruitment
```

## 7. 남은 검증·결정

### TEST_REQUIRED

- 영웅이 일반 병사와 룰렛 코어를 무력화하는지.
- 주점·병영·연구 중 지배 시설이 생기는지.
- 적 교란이 플레이어 통제감과 실패 원인 가독성을 훼손하는지.
- 경계파쇄자가 단순 체력 보스가 아닌 규칙 보스로 읽히는지.

### USER_DECISION_REQUIRED

- 영입 영웅의 MapRun 참여 방식.
- 영웅 등급·명단·출전 상한·능력.
- Act별 적 역할 조합과 신규 도입 순서.
- 일반 적·위험 적·경계파쇄자 정확 명단.
- 노드 수·비용·환불·영구재화 최종명.

## 8. Grill Me·병합 상태

```text
LAST_MERGED_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
CURRENT_COUNT_SINCE_MERGE = 1_OF_10
NEXT_PREFLIGHT_TRIGGER = 10_APPROVED_GRILL_ME_DECISIONS
CURRENT_MERGE_PENDING = NO
```

## 9. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1
= 영입한 영웅이 한 MapRun에서 어떤 방식으로 플레이에 참여하는가
```

## 10. 상태 경계

```text
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
```
