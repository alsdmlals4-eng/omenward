# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: GAMEPLAY_HERO_RUN_ROLE_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
baseline_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
current_grill_me_count: 1
```

이 문서는 질문별 현행 책임 원본을 선택하는 라우터다. 한 질문에 하나의 주 책임 원본을 두고 다른 문서는 계보·보조·검증으로만 사용한다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ PROJECT_CANON_DECISION_LEDGER.md
→ 현재 질문의 APPROVED 분야 문서
→ CURRENT_IMPLEMENTATION_STATUS.md
→ ACTIVE_CONTEXT.md
→ HANDOFF_CONTEXT.md
→ 실제 code/data/Scene/Resource/tests
→ 연결 Google Sheet
```

## 2. 현재 책임 원본

| 질문 | 현행 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·플레이어 약속·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 승인 Decision·상태·병합 카운트 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| 세계·MapRun 반복·승패·징조 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | `USER_APPROVED_WORLD_PRINCIPLE` |
| 베일 본질·법칙·균열·상흔 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | `USER_APPROVED_WORLD_ONTOLOGY` |
| 이계 생물종·경계파쇄자 게임플레이 범위 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | `USER_APPROVED_MINIMAL_LORE_GAMEPLAY_SCOPE` |
| 오멘워드·루메른·지휘관 정치 역할 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | `USER_APPROVED_WORLD_ORGANIZATION` |
| Profile 영구 성장 철학·Readiness | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | `USER_APPROVED_ROLE / VALUES_PENDING` |
| 주점·허브 병영·연구·영웅 영입 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | `USER_APPROVED_STRUCTURE / VALUES_PENDING` |
| 제품 화면·메인 작전 허브 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | `TEXT_SPEC_CURRENT / IMAGE_NOT_GENERATED` |
| Grill Me 10건 병합 주기·preflight | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | `CURRENT_OPERATING_RULE` |
| 실제 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 역할·동기화 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. 필수 계보·검토 호환 경로

- `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`
- 룰렛 Evidence Pilot 상태: `PILOT_RECOMMENDATION / NOT_CANON`

후속 사용자 승인·분야 정본·새 premerge review가 충돌하면 최신 사용자 승인과 최신 분야 정본이 우선한다.

## 4. 세계관 라우팅

### 제품에 필요한 최소 정본

- MapRun은 별개의 실제 경계 공세다.
- 징조는 제한된 위협 구조 예고다.
- 베일은 비의지적 경계 겹침이다.
- 베일종은 균열에서 넘어온 다양한 이계 생물의 통칭이다.
- 단일 제국·통일 종족·상세 정치·외교는 현재 제품 범위가 아니다.
- 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다.
- 사용자에게는 적의 역사보다 행동·위협 대상·대응법을 전달한다.

### 세계관 확장 제한

다음은 사용자가 다시 요청하기 전 자동 확정하지 않는다.

- 이계 문명의 정치·종교·왕조.
- 비적대 이계 종족과의 외교.
- 다중우주 구조와 최초 기원.
- 적 언어·문화 중심의 장문 서사.

## 5. 게임플레이·콘텐츠 라우팅

| 분야 | 먼저 읽을 원본 | 다음 검증·결정 |
|---|---|---|
| 핵심 컨셉·뾰족한 재미 | `PROJECT_CORE.md`, Decision Ledger | 룰렛 통제감·사람 검증 |
| 영웅 런 참여 방식 | Auxiliary Hub + Meta Progression | `OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1` |
| 적 역할·경계파쇄자 | Veilspecies Gameplay Scope | Act별 도입·정확 명단·행동 |
| 룰렛·TokenSource·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | latest Red·runtime |
| 전장·노드·점령 | Project Core | Legacy battle code·tests |
| 경제·Retry·저장 | Meta + Auxiliary Hub + inherited economy lineage | simulator·fault test |
| 화면·UX | Screen Board V2 | runtime·해상도·사람 검증 |
| 콘텐츠·위험 Stage·미션 | Decision Ledger inherited lineage | exact content breadth review |

## 6. 메인 허브·성장 라우팅

- 주점: 영웅 이상 전문 인재의 영구 명부와 결정론적 공개 영입 노드.
- 허브 병영: 병사 훈련·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 기본 Profile로 모든 콘텐츠 완료 가능.
- 영웅의 정확한 런 참여 방식·출전 상한·능력은 다음 Decision에서 확정한다.
- 랜덤 유료 영입·무한 레벨·전 구간 배율·숨은 릴 확률·자동 플레이 금지.

## 7. 실제 구현 경계

```text
CURRENT_PRODUCT
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- physical reels and permanent move
- 30-node topology and five MapRun buildings
- paid Retry and Profile save
- minimal extradimensional-creature gameplay background
- Tavern/Barracks/Research hub and Hero+ roster
```

## 8. Grill Me·병합 규칙

- 자료에서 확인 가능한 사실과 이미 승인된 결정은 재질문하지 않는다.
- 프로젝트 방향을 바꾸는 충돌만 한 번에 하나씩 질문한다.
- 승인 뒤 GitHub·Sheet가 같은 Decision ID로 동기화되기 전 다음 중요 질문으로 넘어가지 않는다.
- 승인 Grill Me Decision ID만 카운트한다.
- 현재 카운터는 `1/10`이다.
- 10건은 preflight trigger이며 blocker가 있으면 병합하지 않는다.

## 9. 현재 Gate

```text
Grill Me: OMW-DEC-20260802-GAMEPLAY-HERO-RUN-ROLE-V1
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
CURRENT_MERGE_PENDING: NO
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
