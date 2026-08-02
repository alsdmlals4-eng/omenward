# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: GAMEPLAY_HERO_EXIT_REPLACEMENT_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
baseline_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
current_grill_me_count: 4
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
| 영웅 해금·병종 바인딩·복수 동병종 영웅 명부 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | `USER_APPROVED_HERO_ROSTER_STRUCTURE` |
| 영웅 등급 보관 토큰·영웅 변환·비가역 배치 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | `USER_APPROVED_HERO_ACTIVATION_STRUCTURE` |
| 영웅 동시 활성 1명·동일 영웅 반복 출전 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | `USER_APPROVED_SINGLE_ACTIVE_LIMIT` |
| 세계·MapRun 반복·승패·징조 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | `USER_APPROVED_WORLD_PRINCIPLE` |
| 베일 본질·법칙·균열·상흔 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | `USER_APPROVED_WORLD_ONTOLOGY` |
| 이계 생물종·경계파쇄자 게임플레이 범위 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | `USER_APPROVED_MINIMAL_LORE_GAMEPLAY_SCOPE` |
| 오멘워드·루메른·지휘관 정치 역할 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | `USER_APPROVED_WORLD_ORGANIZATION` |
| Profile 영구 성장 철학·Readiness | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | `USER_APPROVED_ROLE / VALUES_PENDING` |
| 주점·허브 병영·연구 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | `USER_APPROVED_STRUCTURE / VALUES_PENDING` |
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

## 4. 영웅 라우팅

### 확정

```text
병종별 영웅 후보 1명 이상
→ 주점에서 영구 해금·명부 등록
→ 룰렛에서 동병종 [영웅] 등급 토큰 획득
→ 보관함에서 원본 유지 또는 해금 영웅 선택
→ active hero가 없으면 1토큰을 1유닛으로 변환
→ 한 전선에 비가역 배치
```

- 각 영웅은 하나의 기존 `UnitArchetype`에 고정 연결된다.
- 같은 병종에 서로 다른 해금 영웅이 여러 명 존재할 수 있다.
- 런 시작 전 별도 영웅 등록·계약은 없다.
- 병종 불일치·미해금 영웅은 변환 후보가 아니다.
- 원본 영웅 등급 병종 토큰도 정상 배치 가능하다.
- 상·중·하를 합쳐 출전 중인 이름 지정 영웅은 동시에 최대 1명이다.
- active hero가 있으면 새 토큰은 보관하거나 원본 병종으로 사용한다.
- 같은 영웅도 이전 인스턴스가 종료된 뒤 새 토큰으로 반복 출전할 수 있다.
- 반복 출전마다 별도의 영웅 등급 토큰이 필요하다.
- 확정 전 취소 가능, 전선 배치 뒤 undo·회수·판매·라인 변경 불가다.

### 다음 결정

```text
OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1
= 현재 영웅이 살아 있을 때 수동 교대·퇴각을 허용하는가, 어떤 사건에서 active 상태가 종료되는가
```

정확 명단·능력·수치는 별도 결정이다.

## 5. 세계관 라우팅

- MapRun은 별개의 실제 경계 공세다.
- 베일종은 균열에서 넘어온 다양한 이계 생물의 통칭이다.
- 단일 제국·통일 종족·상세 정치·외교는 현재 제품 범위가 아니다.
- 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다.
- 사용자에게는 적의 역사보다 행동·위협 대상·대응법을 전달한다.

## 6. 게임플레이·콘텐츠 라우팅

| 분야 | 먼저 읽을 원본 | 다음 검증·결정 |
|---|---|---|
| 핵심 컨셉·뾰족한 재미 | `PROJECT_CORE.md`, Decision Ledger | 룰렛 통제감·사람 검증 |
| 영웅 해금·명부 | Hero Unlock Registration | 병종별 정확 명단·비용 |
| 영웅 토큰 변환·배치 | Hero Token Conversion | 단일 활성 상태 검증 |
| 영웅 활성·반복 출전 | Hero Single Active | 퇴각·교대·Stage 유지 |
| 적 역할·경계파쇄자 | Veilspecies Gameplay Scope | Act별 도입·정확 명단·행동 |
| 룰렛·TokenSource·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | latest Red·runtime |
| 전장·노드·점령 | Project Core | Legacy battle code·tests |
| 경제·Retry·저장 | Meta + Auxiliary Hub + inherited economy lineage | simulator·fault test |
| 화면·UX | Screen Board V2 | active hero 표시·보관함 차단 피드백 |
| 콘텐츠·위험 Stage·미션 | Decision Ledger inherited lineage | exact content breadth review |

## 7. 메인 허브·성장 라우팅

- 주점: 병종별 복수 영웅 후보의 결정론적 영구 해금과 명부.
- 보관함: 영웅 등급 토큰의 원본 유지 또는 동병종 해금 영웅 변환.
- 전장: 이름 지정 영웅 active slot 1개를 세 전선이 공유.
- 허브 병영: 병사 훈련·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 랜덤 유료 영입·무한 레벨·전 구간 배율·숨은 릴 확률·자동 플레이 금지.

## 8. 실제 구현 경계

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
- Tavern/Barracks/Research hub
- multi-hero-per-unit unlock roster
- stored Hero-grade token conversion and irreversible deployment
- one active Hero across all lanes; repeat deployment after slot clears
```

## 9. Grill Me·병합 규칙

- 자료에서 확인 가능한 사실과 이미 승인된 결정은 재질문하지 않는다.
- 프로젝트 방향을 바꾸는 충돌만 한 번에 하나씩 질문한다.
- 승인 뒤 GitHub·Sheet가 같은 Decision ID로 동기화되기 전 다음 중요 질문으로 넘어가지 않는다.
- 승인 Grill Me Decision ID만 카운트한다.
- 현재 카운터는 `4/10`이다.
- 10건은 preflight trigger이며 blocker가 있으면 병합하지 않는다.

## 10. 현재 Gate

```text
Grill Me: OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
CURRENT_MERGE_PENDING: NO
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
