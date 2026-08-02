# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
canonical_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 2
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
```

이 문서는 현재 승인 Decision과 상태를 소유한다. 제품 정체성과 불변 조건은 `PROJECT_CORE.md`, 실제 구현은 `CURRENT_IMPLEMENTATION_STATUS.md`, 질문별 책임 원본은 `DOCUMENTATION_MAP.md`가 소유한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY

REGISTRATION
!= IMMEDIATE_DEPLOYMENT
!= PASSIVE_GLOBAL_BUFF
!= REEL_ODDS_CHANGE
```

## 2. 현재 승인 Decision

| Decision ID | 상태 | 결정 | 현재 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 기존 병종마다 고정 대응 영웅을 두고, 주점에서 영구 해금한 뒤 런 전 대응 병종에 등록해야 사용할 수 있다 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | 등록 슬롯 수·전장 발동·명단·능력·수치 pending |
| `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1` | `USER_APPROVED / CURRENT_BRANCH_SYNCED` | 베일종은 균열을 통해 유입된 다양한 이계 생물의 통칭이며 사용자에게 상세 문명·정치 설명을 제공하지 않는다. 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | 적 명단·Act 배치·정확 행동·수치 pending |
| `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1` | `USER_APPROVED / MAIN_SYNCED` | 오멘워드는 루메른 왕실 인가 자율 경계대응단이며 활성 작전에서 제한된 비상 지휘권을 갖는다 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | 정치 인물·법률명 상세 pending |
| `OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1` | `USER_APPROVED / MAIN_SYNCED` | 메인 허브에 주점·허브 병영·연구를 두고 정산 영구재화로 유한 공개 노드를 개방한다 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | 비용·노드·영웅 능력 pending |
| `OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1` | `CURRENT_OPERATING_RULE / MAIN_SYNCED` | 승인 Grill Me 10건마다 적대적 병합 preflight를 실행하고 blocker 0일 때만 병합한다 | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | 현재 카운터 `2/10` |
| `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1` | `USER_APPROVED / MAIN_SYNCED` | 베일은 현실과 이질적인 외부 법칙 영역의 비의지적 경계 겹침이다 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | 기원·우주론은 제품 범위 밖 |
| `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` | `USER_APPROVED / MAIN_SYNCED` | 각 MapRun은 별개의 실제 경계 공세이며 승리는 한 침공로 봉쇄다 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | 지역·콘텐츠 상세 pending |
| `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` | `USER_APPROVED / MAIN_SYNCED` | 수평 해금·제한 편의를 주축으로 하고 상한형 준비 보정을 보조축으로 둔다 | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | exact values·simulation pending |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `INHERITED_APPROVED / MAIN_SYNCED_LOCAL_AUTHORITY` | 메인 허브부터 Retry까지 제품 화면과 정보 위계 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | image·runtime·human validation pending |

## 3. 영웅 해금·등록 정본

```text
기존 병종
→ 병종별 고정 대응 영웅
→ 주점 공개 노드에서 영구 해금
→ 런 전 대응 병종에 등록
→ 등록 영웅만 해당 런에서 사용 가능
```

- 각 영웅은 하나의 기존 `UnitArchetype`에 고정 연결된다.
- 해금은 영구 소유권이며 등록은 런별 사용 자격이다.
- 해금만으로 모든 런에 자동 장착되지 않는다.
- 등록 상태는 런 시작 시 `RunLoadoutSnapshot`으로 고정한다.
- 런 도중 등록 변경·교체·해제는 허용하지 않는다.
- 등록은 즉시 전장 배치·전 구간 능력치 배율·릴 확률 변경을 뜻하지 않는다.
- 기본 병종은 영웅 미해금 상태에서도 완전하며 전체 콘텐츠 완료가 가능해야 한다.

## 4. 이계 생물종 게임플레이 정본

```text
PLAYER_EXPLANATION = 균열에서 넘어온 이계 생물종
INTERNAL_TERM = 베일종
SINGLE_RACE_OR_EMPIRE = NO
DETAILED_POLITICS_AND_DIPLOMACY = OUT_OF_SCOPE
BOUNDARY_BREAKER = BREACH_STABILIZING_BOSS_ORGANISM
```

적 제작 역할 분류는 `군집형 / 돌격형 / 원거리형 / 방호형 / 교란형 / 공성형 / 경계파쇄자`다. 이는 정확한 최종 적 명단이 아니라 Act·Stage 콘텐츠 제작 규칙이다.

## 5. 보호된 제품 코어

> 공개된 세 전선의 위험을 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

- PC-primary, 20 Stage·4막·약 35분 목표.
- 위험 Stage 5·10·15·20.
- 세 물리 릴·TokenInstance·cursor·3×3 노출.
- immutable SpinSnapshot·명시적 확정·한 라인 비가역 배치.
- 상·중·하 3라인·고정시간 점령·전체 30 건설 노드.
- MapRun 건물: 금고·농장·타워·전장 병영·지휘소.
- 실제 경계 공세·국소 봉쇄·벨루 비모달 안내자.

## 6. 메인 허브·Profile 정본

```text
PRIMARY_ACTION = MAPRUN_ENTRY
AUXILIARY = TAVERN + HUB_BARRACKS + RESEARCH
CURRENCY = SETTLED_PERMANENT_CURRENCY_BALANCE
NODE_GRAPH = FINITE / VISIBLE / DETERMINISTIC
```

- 주점: 병종별 고정 영웅의 영구 해금과 명부 관리.
- 허브 병영: 병사·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 랜덤 뽑기·유료 재굴림·중복 합성·무한 레벨·숨은 릴 확률 조작 금지.

## 7. 실제 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED_NOT_IMPLEMENTED
- three physical reels and permanent horizontal movement
- 30-node topology and five MapRun buildings
- fixed-time capture
- paid Retry and Profile save
- minimal Veil-species gameplay scope
- Tavern/Barracks/Research permanent-node hub
- fixed unit-hero unlock and pre-run registration
```

## 8. 남은 검증·결정

### TEST_REQUIRED

- 영웅이 일반 병사와 룰렛 코어를 무력화하는지.
- 영웅 등록 슬롯이 사실상 고정 정답 조합으로 수렴하는지.
- 미등록·미해금 병종도 완전한 선택지인지.
- 적 교란과 경계파쇄자의 전조·대응·실패 인과가 읽히는지.

### USER_DECISION_REQUIRED

- 등록된 병종 영웅의 전장 등장·발동 방식.
- 동시에 등록 가능한 영웅 수.
- 병종별 영웅 명단·능력·등급·수치.
- Act별 적 역할 조합과 정확 명단.
- 노드 수·비용·환불·영구재화 최종명.

## 9. Grill Me·병합 상태

```text
LAST_MERGED_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
CURRENT_COUNT_SINCE_MERGE = 2_OF_10
NEXT_PREFLIGHT_TRIGGER = 10_APPROVED_GRILL_ME_DECISIONS
CURRENT_MERGE_PENDING = NO
```

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
= 등록된 병종 영웅이 해당 병종의 룰렛 결과·전선 배치와 어떤 방식으로 연결되어 등장하는가
```

## 11. 상태 경계

```text
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
```
