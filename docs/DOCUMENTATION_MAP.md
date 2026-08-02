# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: PR121_TEN_DECISION_ADVERSARIAL_PREFLIGHT
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
baseline_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_pr: 120
current_pr: 121
current_grill_me_count: 10
preflight: REQUIRED_IN_PROGRESS
merge_authorization: NOT_GRANTED
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
| 승인 Decision·상태·10건 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| 맵·MapRun·Stage·Wave·정산·정비시간·Stage 중 운영 기능 | `design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` | `USER_APPROVED_GAME_FLOW_TERMINOLOGY` |
| 영웅 해금·병종 바인딩·복수 동병종 영웅 명부 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | `USER_APPROVED_HERO_ROSTER_STRUCTURE` |
| 영웅 등급 보관 토큰·영웅 변환·비가역 배치 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | `USER_APPROVED_HERO_ACTIVATION_STRUCTURE` |
| 영웅 동시 활성 1명·동일 영웅 반복 출전 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | `USER_APPROVED_SINGLE_ACTIVE_LIMIT` |
| 영웅 수동 퇴각·교대 금지·Stage/Act/정비시간 유지·active 종료 | `design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md` | `USER_APPROVED_NO_MANUAL_EXIT` |
| 영웅 Stage 경계 HP·쿨다운·충전·고유 자원 지속과 전투 잔여 상태 정리 | `design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md` | `USER_APPROVED_HERO_LONG_TERM_STATE_PERSISTENCE` |
| 영웅 사망 무회수·사망 이후 새 룰렛 결과·새 인스턴스 초기 상태 | `design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` | `USER_APPROVED_POST_DEATH_RESULT_AND_FRESH_INSTANCE` |
| 영웅 총 전투 예산·조건부 고점·전문화·약점·원본 선택 사유 | `design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` | `USER_APPROVED_CONDITIONAL_PEAK_SPECIALIZED_SIDEGRADE` |
| 영웅 능력 자동 발동·trigger·능력/대상 우선순위·결정론 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | `USER_APPROVED_AUTOMATIC_RULE_BASED_ACTIVATION` |
| 세계·MapRun 반복·승패·징조 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | `USER_APPROVED_WORLD_PRINCIPLE` |
| 베일 본질·법칙·균열·상흔 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | `USER_APPROVED_WORLD_ONTOLOGY` |
| 이계 생물종·경계파쇄자 게임플레이 범위 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | `USER_APPROVED_MINIMAL_LORE_GAMEPLAY_SCOPE` |
| 오멘워드·루메른·지휘관 정치 역할 | `design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | `USER_APPROVED_WORLD_ORGANIZATION` |
| Profile 영구 성장 철학·Readiness | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | `USER_APPROVED_ROLE / VALUES_PENDING` |
| 주점·허브 병영·연구 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | `USER_APPROVED_STRUCTURE / VALUES_PENDING` |
| 제품 화면·메인 작전 허브 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | `TEXT_SPEC_CURRENT / IMAGE_NOT_GENERATED` |
| Grill Me 10건 병합 주기·preflight | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | `CURRENT_OPERATING_RULE` |
| PR #121 10건 적대적 preflight 결과 | `reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md` | `CREATED_AFTER_PREFLIGHT / MERGE_NOT_AUTHORIZED` |
| 실제 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 역할·동기화 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. MapRun 라우팅

```text
맵 선택
→ MapRun 생성·RunState 초기화
→ Stage
→ Wave 1...N
   ↔ 건설·업그레이드·수리
   ↔ 룰렛 조작과 병력 확보
   ↔ 보관함 관리
   ↔ 병력 배치
→ Stage 정산·checkpoint
→ 정비시간
→ 다음 Stage
```

- `라운드`는 별도 상태가 아니며 공식 용어는 `Wave / 웨이브`다.
- Wave 사이에는 기본 정비시간이 없고 Stage 종료 뒤 한 번만 발생한다.
- 네 가지 런 운영 기능은 Stage와 정비시간 모두 사용할 수 있다.
- MapRun 초기화는 RunState만 초기화하고 Profile은 유지한다.

## 4. 영웅 라우팅

```text
영웅 영구 해금·명부 등록
→ 룰렛 동병종 [영웅] 등급 토큰
→ 원본 병종 또는 해금 영웅 선택
→ active slot 검사
→ 1토큰을 1유닛으로 변환·한 전선 배치
→ 공개된 규칙 기반 자동 능력 운용
→ 생존 시 장기 상태 유지
→ 사망 시 무회수·slot clear
→ 사망 이후 새 적격 룰렛 결과로만 이름 지정 영웅 재출전
```

- 같은 병종에 복수 영웅이 존재할 수 있다.
- 모든 영웅은 해당 기존 `UnitArchetype`에 고정 연결된다.
- 세 전선 전체 active 이름 지정 영웅은 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 영웅은 원본 `[영웅]` 등급 병종의 순수 상위호환이 아니다.
- 전투 예산은 피해·생존·사거리·제어·지원·기동·운용 조건을 함께 평가한다.
- 모든 영웅은 조건부 고점과 실제 약점을 가진다.
- 모든 영웅 전투 능력은 규칙 기반 자동 발동이며 수동 스킬 버튼과 수동 타깃 지정은 없다.
- trigger·ability priority·target priority·tie-break를 공개한다.
- 동일 저장 상태·입력 순서에서는 같은 자동 판단 결과를 유지한다.

## 5. 분야별 다음 검증

| 분야 | 먼저 읽을 원본 | 다음 검증·결정 |
|---|---|---|
| 핵심 컨셉·뾰족한 재미 | `PROJECT_CORE.md`, Decision Ledger | 룰렛 통제감·사람 검증 |
| MapRun·Stage·Wave·정비시간 | MapRun Stage Wave Maintenance | 일반 clock matrix·맵별 Wave 편성 |
| 영웅 해금·명부 | Hero Unlock Registration | 병종별 명단·비용 |
| 영웅 토큰 변환·배치 | Hero Token Conversion | UI·transaction runtime |
| 영웅 활성·반복 출전 | Hero Single Active | 토큰 빈도·반복 편중 simulation |
| 영웅 퇴각·종료 | Hero Exit and Replacement | 사망·유지 UX |
| 영웅 Stage 상태 | Hero Stage State Persistence | 영속 동반자 예외 |
| 영웅 사망·재출전 | Hero Redeployment Initial State | provenance fault test |
| 영웅 전투 예산 | Hero Power Budget and Sidegrade | encounter matrix·선택률·조합 simulation |
| 영웅 능력 발동 | Hero Ability Activation Mode | trigger/priority 명세·결정론·save reload test |
| 적 역할·경계파쇄자 | Veilspecies Gameplay Scope | Stage·Wave별 도입·명단·행동 |
| 룰렛·TokenSource·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | runtime·사람 검증 |
| 전장·노드·점령 | Project Core | Legacy battle code·tests |
| 경제·Retry·저장 | Meta + Auxiliary Hub + Hero lifecycle | maintenance clock matrix·save fault test |
| 화면·UX | Screen Board V2 + Hero authorities | 자동 발동·조건·약점·post-death 안내 usability |

## 6. 실제 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
```

## 7. Grill Me·병합 규칙

- 자료에서 확인 가능한 사실과 이미 승인된 결정은 재질문하지 않는다.
- 승인 뒤 GitHub·Sheet가 같은 Decision ID로 동기화되기 전 다음 중요 질문으로 넘어가지 않는다.
- 승인 Grill Me Decision ID만 카운트한다.
- 현재 카운터는 `10/10`이며 preflight trigger에 도달했다.
- 10건은 병합 명령이 아니다.
- P0/P1 blocker가 있으면 병합하지 않는다.
- blocker 0이어도 사용자의 명시적 병합 승인 전에는 Draft를 유지한다.

## 8. 현재 Gate

```text
OMW-OPS-20260802-PR121-TEN-DECISION-PREFLIGHT-V1
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
PREFLIGHT: REQUIRED_IN_PROGRESS
MERGE_AUTHORIZATION: NOT_GRANTED
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
