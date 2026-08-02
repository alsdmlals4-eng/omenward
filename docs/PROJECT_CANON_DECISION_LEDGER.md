# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / MERGE_PREFLIGHT
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
current_world_decision: OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
canonical_baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
merge_batch_pr: 119
superseded_planning_pr: 116_CLOSED_NOT_MERGED
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_in_current_batch: 4
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
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

HISTORICAL_APPROVAL_EVIDENCE
!= CURRENT_LOCAL_AUTHORITY
```

## 2. 현재 승인 Decision

| Decision ID | 상태 | 결정 | 현재 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1` | `USER_APPROVED / CURRENT` | 오멘워드는 루메른 왕실 인가 자율 경계대응단이며 활성 작전에서 제한된 비상 지휘권을 갖고 평시·작전 후 감사와 지방 협조를 따른다 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | 왕실 인물·법률명·최종 직함·세력 상세 pending |
| `OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1` | `USER_APPROVED / CURRENT` | 메인 허브 보조 콘텐츠를 주점·병영·연구로 구성하고 정산 영구재화로 유한 노드를 개방한다; 주점은 공개 결정론적 영웅 영입, 병영은 sidegrade 훈련, 연구는 시스템·정보 sidegrade를 담당한다 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | 비용·노드 수·영웅 목록·등급·출전 상한·능력 pending |
| `OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1` | `CURRENT_OPERATING_RULE` | 현재 승인 묶음은 사용자 지시로 즉시 preflight·병합하고 이후 승인 Grill Me 10건마다 사전 검증 후 병합한다 | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | blocker가 있으면 10건이어도 병합 금지 |
| `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1` | `USER_APPROVED / CURRENT` | 베일은 현실과 이질적인 외부 법칙 영역의 비의지적 경계 겹침이며 생태적 증식은 법칙 충돌의 물질 패턴이다 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | 기원·외부 영역 구조·베일종 목적 pending |
| `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` | `USER_APPROVED / CURRENT` | 각 MapRun은 징조로 감지된 별개의 실제 경계 공세이고 승리는 한 침공로 봉쇄, 패배는 실제 방어선 붕괴다 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | 지역·세력·지속 결과 상세 pending |
| `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` | `USER_APPROVED / CURRENT` | 수평 해금·제한 편의를 주축으로 하고 한 런 1개·유한 랭크·초반 한정 준비 보정을 보조축으로 둔다 | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | exact values·simulation·runtime·human validation pending |
| `OMW-DEC-20260802-CANON-RECOVERY-V1` | `USER_APPROVED / MERGE_BATCH` | Base v9.4 main에서 승인 정본을 복구하고 PR #116은 역사 증거로 보존한다 | recovery audit, PR #119, connected Sheet | main merge verification pending |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `INHERITED_APPROVED / CURRENT_LOCAL_AUTHORITY` | 메인 허브부터 Retry까지 8개 화면과 정보 위계; 메인 허브에 주점·병영·연구 확장 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | image·Godot UI·runtime·human validation pending |

## 3. 역사 승인 계보

다음 Decision은 PR #116에서 승인됐으나 PR #116 자체는 병합하지 않는다. 현재 Project Core·이번 원장·새 승인 문서가 상위 의미를 소유하며, 세부 구현 패키지는 후속 계획에서 역사 PR의 해당 파일을 다시 검증해 선별 복구한다.

| Decision ID | 보존된 원칙 | 현재 해석 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | 전장 1·4막·Stage 20·일반 공세 8·위험 4·보스 3·미션 12 | `INHERITED_PLAN / CONTENT_BREADTH_REVIEW_PENDING` |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | Stage 5 이후 MapRun당 최대 1회 paid Retry·동일 RNG checkpoint | `INHERITED_PRINCIPLE / EXACT_COST_PENDING` |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | Stage 5·10·15·20 공개 위험 패키지 | `INHERITED_PLAN / EXACT_CONTENT_PENDING` |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | 노드 1종·본진 6/진영·중간 6곳×3·접전지 0·총 30 | `CURRENT_INVARIANT_IN_PROJECT_CORE` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | 정본명 벨루·자동 결정 금지 | `CURRENT_INVARIANT_IN_CONTEXT_AND_SCREEN_SPEC` |
| `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1` | MapRun/Profile 분리·Journal·Backup·100K/fault Gate | `INHERITED_STRUCTURE / IMPLEMENTATION_PACKAGE_PENDING` |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | 최신 3릴·30노드·5건물·fixed capture·paid Retry Red 책임 | `INHERITED_GATE / TEST_FILES_NOT_CREATED` |
| `OMW-DEC-20260731-CANON-SYNC-V1` | 승인 Decision의 GitHub·Sheet 즉시 동기화 | 이번 merge cadence protocol이 확장·구체화 |

역사 PR의 파일 경로를 current local authority로 표시하지 않는다. 필요한 세부 정본은 현재 Base·Decision과 대조한 뒤 별도 current file로 복구한다.

## 4. 보호된 제품 코어

> 공개된 세 전선의 위험을 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

- PC-primary, 모바일은 미래 고려.
- 20 Stage·4막·약 35분 목표.
- 위험 Stage 5·10·15·20.
- 세 물리 원형 릴·TokenInstance·cursor·3×3 노출.
- immutable SpinSnapshot과 명시적 한 번 확정.
- 보관·판매·한 라인 배치, 배치 뒤 회수·변경·판매 금지.
- 상·중·하 3라인·고정시간 점령.
- 건설 노드 1종·전체 30개.
- 금고·농장·타워·전장 병영·지휘소.
- 벨루 비모달 안내자.
- 실제 경계 공세·제한된 징조·국소 봉쇄·상흔.

## 5. 세계 조직 정본

```text
루메른 왕실 인가
→ 평시 감독·예산 감사·지방 협조
→ 징조·경계 비상사태
→ 오멘워드 현장 지휘관의 제한된 작전 자율권
→ 균열 봉쇄 또는 철수
→ 권한 반납·피해·재화·명령 인과 감사
```

- 플레이어는 활성 작전 지휘관이며 통치자가 아니다.
- 영구 통치·무제한 징발·상시 왕국군 지휘·일반 사법권·쿠데타 권한은 없다.
- 후보 직함 `경계수호관 / Field Warden`은 아직 `RECOMMENDED_DEFAULT`다.

## 6. 메인 허브·Profile 정본

```text
PRIMARY_ACTION = MAPRUN_ENTRY
AUXILIARY = TAVERN + HUB_BARRACKS + RESEARCH
CURRENCY = SETTLED_PERMANENT_CURRENCY_BALANCE
NODE_GRAPH = FINITE / VISIBLE / DETERMINISTIC
```

### 주점

- 영웅 이상 전문 인재를 공개 노드로 영구 영입한다.
- 랜덤 뽑기·유료 재굴림·중복 합성·프리미엄 파워를 금지한다.
- 영입은 영구, 한 런 출전은 제한한다. 정확 상한은 pending이다.

### 허브 병영

- 병사 훈련·병종·전문화·교리 sidegrade를 해금한다.
- MapRun TokenSource 건물 `병영`과 Profile 시설을 구분한다.
- 무한 레벨·전 구간 전투 배율을 금지한다.

### 연구

- 대체 건물·TokenSource·미션·징조 분석·복기·편의 sidegrade를 해금한다.
- 숨은 릴 확률 조작·전 구간 생산 배율·자동 플레이를 금지한다.

### 공통

- 기본 Profile로 모든 콘텐츠 완료 가능.
- `settled balance`는 노드·Retry 소비, `settled total`은 비감소 milestone 판정.
- 비용·노드 수·영웅 목록·능력·환불·정확 schema는 pending이다.

## 7. 실제 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
- independent weighted 9-cell roulette
- barracks/tower/farm only
- legacy outpost/capture_power
- free same-stage restart
- Label/code-drawn graybox UI

LATEST_APPROVED_NOT_IMPLEMENTED
- three physical reels and permanent horizontal movement
- 30-node topology and five MapRun buildings
- fixed-time capture
- paid Retry and Profile save
- real-incursion world and Veil ontology
- royal-chartered Omenward organization
- Tavern/Barracks/Research permanent-node hub
- Hero+ deterministic roster recruitment
```

## 8. 수치 정책

```text
철학·결과·금지선 승인
→ 관계식·후보 작성
→ 같은 seed simulation
→ 꼬리·지배 전략·softlock·재화 비축 검토
→ 사람 검증
→ 사용자 exact-value 승인
→ 구현값·검증값 분리
```

과거 `20 gold spin`, `160 starting gold`, `70/50/40 refund`는 `LEGACY_H0 / HISTORICAL_ONLY`다.

## 9. 적대적 finding

### 구조적으로 해결

- 반복 MapRun을 시간 루프가 아닌 별개의 실제 공세로 정의.
- 베일 현상과 베일종 행위 주체 분리.
- 왕실 소속과 현장 자율권을 기간·구역·감사로 제한.
- 영웅 영입을 랜덤 가챠가 아닌 공개 결정론적 노드로 제한.
- 훈련·연구를 sidegrade와 유한 노드로 제한.
- 10건 주기를 강제 병합이 아닌 preflight trigger로 정의.

### TEST_REQUIRED

- 영웅 보유가 일반 병사와 기본 Profile을 무력화하는지.
- 주점·병영·연구 중 지배 시설이 생기는지.
- 노드 구매와 Retry의 같은 지갑 경쟁이 과도한 비축·후회를 만드는지.
- 메인 허브가 MapRun 진입보다 더 중요한 메뉴 게임이 되는지.
- 수평 해금이 숨은 상위 호환이 되는지.
- save/journal/fault injection.
- 세계 규모·공세 빈도·상흔 누적.

### USER_DECISION_REQUIRED

- 영웅 등급 체계·명단·출전 상한·능력.
- 노드 수·비용·환불·영구재화 최종명.
- 루메른 왕실·지방 세력 상세.
- 베일종·경계파쇄자의 발생·지성·목적.

## 10. Grill Me·병합 상태

현재 묶음의 Grill Me 승인:

1. Meta progression role.
2. World/MapRun motivation.
3. Veil ontology.
4. Omenward political role.

보조 허브와 merge cadence는 사용자 직접 승인 Decision이며 Grill Me 카운트에는 포함하지 않는다.

```text
CURRENT_BATCH_COUNT = 4
CURRENT_USER_MERGE_AUTHORIZATION = YES
MERGE_REQUIRES_PREFLIGHT = YES
POST_MERGE_COUNTER = 0_OF_10
```

## 11. 다음 Gate

병합 완료 뒤 새 branch·새 Draft PR에서 다음 질문을 진행한다.

```text
OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
= 베일종·경계파쇄자의 발생·지성·사회·침공 목적
```

## 12. 상태 경계

```text
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
CURRENT_PR_MERGE: USER_AUTHORIZED / PREFLIGHT_REQUIRED
```
