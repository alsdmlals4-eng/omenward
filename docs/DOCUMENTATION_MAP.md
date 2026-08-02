# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: WORLD_VEILSPECIES_PURPOSE_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
baseline_main: 26b0a39fbf576557f2658723dee8405c2ea07a6f
active_base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_MAIN_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_pr: 119
last_merge_commit: 26b0a39fbf576557f2658723dee8405c2ea07a6f
superseded_pr: 116_CLOSED_NOT_MERGED
current_grill_me_count: 0
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
| 승인 Decision·상태·대체·병합 카운트 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| 세계·MapRun 반복·승패·징조 역할 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | `USER_APPROVED_WORLD_PRINCIPLE` |
| 베일 본질·법칙·균열·상흔 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | `USER_APPROVED_WORLD_ONTOLOGY` |
| 오멘워드·루메른·지휘관 정치 역할 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | `USER_APPROVED_WORLD_ORGANIZATION` |
| Profile 영구 성장 철학·Readiness | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | `USER_APPROVED_ROLE / VALUES_PENDING` |
| 주점·허브 병영·연구·영웅 영입·영구 노드 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | `USER_APPROVED_STRUCTURE / VALUES_PENDING` |
| 8개 제품 화면·메인 작전 허브 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | `TEXT_SPEC_CURRENT / IMAGE_NOT_GENERATED` |
| Grill Me 10건 병합 주기·preflight | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | `CURRENT_OPERATING_RULE` |
| PR #119 병합 직전 적대적 검토 | `reviews/OMENWARD_PR119_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md` | `MERGED_BATCH_EVIDENCE` |
| 전체 Vertical Slice 시스템 관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `APPROVED_SYSTEM_CONTRACT / LATER_DECISIONS_OVERRIDE` |
| 현행 Vertical Slice 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_REVIEW_LINEAGE / LATER_REVIEWS_OVERRIDE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 실제 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 역할·동기화 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |
| 미확정 수치·콘텐츠 | `DECISIONS_PENDING.md` | `PENDING_REFERENCE / LEDGER_OVERRIDES` |
| 통합 게임 설명 | `OMENWARD_GAME_DESIGN.md` | `REFERENCE_SUMMARY / CURRENT_DECISIONS_OVERRIDE` |

## 3. current와 history 구분

- PR #119는 squash 병합되어 승인 묶음의 main 정본이 됐다.
- 병합 commit은 `26b0a39fbf576557f2658723dee8405c2ea07a6f`이다.
- PR #116은 승인 대화와 세부 문서의 역사 증거다.
- PR #116은 닫혔고 병합되지 않았으며 current local authority가 아니다.
- PR #116 경로를 current authority로 사용하려면 현재 Base v9.4와 최신 Decision을 대조해 새 PR에 선별 복구해야 한다.
- `APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`는 PR #119에서 current local authority로 복구·확장됐다.

## 4. 검토·증거 경계

- `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`는 전체 시스템 Vertical Slice 계보의 적대적 검토다.
- 이후 사용자 승인·분야 정본·새 premerge review가 충돌하면 최신 사용자 승인과 최신 분야 정본이 우선한다.
- `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 룰렛 통제감 가설의 Evidence Pilot이다.
- Evidence Pilot 상태는 반드시 `PILOT_RECOMMENDATION / NOT_CANON`으로 유지한다.
- Pilot은 제품 구현·사람 검증·세계관 정본·CORE_LOCK 권한을 갖지 않는다.

## 5. 세계관 라우팅

### 확정

- MapRun은 별개의 실제 경계 공세.
- 징조는 위협 구조의 제한된 선행 관측.
- 베일은 비의지적 경계 겹침.
- 봉쇄는 국소 접촉면을 닫고 상흔을 남김.
- 오멘워드는 루메른 왕실 인가 자율 경계대응단.
- 플레이어는 활성 작전 지휘관, 통치자 아님.
- Profile은 조직의 교리·보급·기록·인재·연구 축적.

### 다음 결정

```text
OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
= 베일종·경계파쇄자의 발생·지성·사회·침공 목적
```

이 결정 전에는 베일종 전체가 한 제국·군체·자연재해·악신의 하수인 중 하나라고 임의 확정하지 않는다.

## 6. 메인 허브·성장 라우팅

- 주점: 영웅 이상 전문 인재의 영구 명부와 결정론적 공개 영입 노드. 랜덤 뽑기·유료 재굴림·중복 합성 금지.
- 허브 병영: 병사 훈련·병종·전문화·교리 sidegrade. MapRun TokenSource 병영과 구분.
- 연구: 대체 건물·TokenSource·미션·징조 분석·편의 sidegrade. 숨은 odds·전 구간 생산 배율·자동 플레이 금지.
- 기본 Profile로 모든 콘텐츠 완료 가능.
- balance는 노드·Retry 소비, total은 비감소 milestone 판정.
- 비용·노드 수·영웅 목록·능력·환불은 exact-value approval 전 제품값이 아니다.

## 7. 분야별 라우팅

| 분야 | 먼저 읽을 원본 | 보조·검증 |
|---|---|---|
| 핵심 컨셉·뾰족한 재미 | `PROJECT_CORE.md`, Decision Ledger | 룰렛 Evidence·사람 검증 |
| 세계·MapRun·징조·승패 | World Run Motivation | Sheet `11_세계관` |
| 베일·법칙·상흔 | Veil Ontology | 후속 적·지리 Decision |
| 왕국·오멘워드·지휘관 | Political Role | Sheet `11·13·14` |
| 벨루 | Project Core·Screen Board·World Run | Sheet `13_주요인물` |
| Profile 철학·Readiness | Meta Progression Role | P0/P1/P2 simulation |
| 주점·병영·연구·영웅 | Auxiliary Hub Progression | Sheet `41·60`, hero content decision |
| 화면·UX | Screen Board V2 | runtime·해상도·사람 검증 |
| 룰렛·TokenSource·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | Legacy code·latest Red lineage |
| 전장·노드·점령 | Project Core | Legacy battle code·tests |
| 경제·Retry·저장 | Meta + Auxiliary Hub + inherited economy lineage | simulator/fault test NOT_RUN |
| 콘텐츠·위험 Stage·미션 | Decision Ledger inherited lineage | exact content pending |
| 병합·정본 동기화 | Merge Cadence Protocol | GitHub PR·Sheet exact read-back |

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
- world/Veil/political canon
- Tavern/Barracks/Research hub and Hero+ roster
```

## 9. Grill Me·병합 규칙

- 자료에서 확인 가능한 사실은 묻지 않는다.
- 이미 승인된 결정을 재질문하지 않는다.
- 프로젝트 방향을 바꾸는 충돌만 한 번에 하나씩 질문한다.
- 답변 후 GitHub·Sheet가 같은 Decision ID로 동기화되기 전 다음 중요 질문으로 넘어가지 않는다.
- 승인 Grill Me Decision ID만 병합 카운트에 포함한다.
- 현재 카운터는 `0/10`이다.
- 매 10건은 preflight trigger이며 blocker가 있으면 병합하지 않는다.
- 다음 Decision은 새 branch·새 Draft PR에서 시작한다.

## 10. 현재 Gate

```text
Grill Me: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
CURRENT_MERGE_PENDING: NO
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
