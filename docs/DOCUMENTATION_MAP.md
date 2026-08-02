# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: POST_MERGE_MAIN_CANONICAL
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
baseline_main: 8337a3eba5ff065b2a7c06c6a6256e5b4951c055
working_branch: NONE
active_base: 9.4.2_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: MERGED_TO_MAIN_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_pr: 121
current_pr: NONE
current_grill_me_count: 0
preflight: PR121_PASS_AND_MERGED
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
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
| 승인 Decision·상태·10건 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY / MAIN_CANONICAL` |
| 전체 시스템 Vertical Slice 계약 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| Vertical Slice 적대적 검토 계보 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| MapRun·Stage·Wave·정비시간 | `design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` | `MERGED_USER_APPROVED_GAME_FLOW` |
| 영웅 해금·명부 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | `MERGED_USER_APPROVED_ROSTER` |
| 영웅 토큰 변환·배치 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | `MERGED_USER_APPROVED_ACTIVATION` |
| 영웅 단일 활성·반복 출전 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | `MERGED_USER_APPROVED_ACTIVE_LIMIT` |
| 영웅 퇴각·교대·종료 | `design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md` | `MERGED_USER_APPROVED_NO_MANUAL_EXIT` |
| 영웅 Stage 상태 지속 | `design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md` | `MERGED_USER_APPROVED_PERSISTENCE` |
| 영웅 사망·재출전 초기 상태 | `design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` | `MERGED_USER_APPROVED_REDEPLOYMENT` |
| 영웅 전투 예산·sidegrade | `design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` | `MERGED_USER_APPROVED_SIDEGRADE` |
| 영웅 능력 자동 발동·결정론 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | `MERGED_USER_APPROVED_AUTOMATIC_ACTIVATION` |
| 이계 생물종·경계파쇄자 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | `MERGED_USER_APPROVED_GAMEPLAY_SCOPE` |
| 세계·MapRun 반복·승패·징조 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | `USER_APPROVED_WORLD_PRINCIPLE` |
| 베일 본질·법칙·균열·상흔 | `design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md` | `USER_APPROVED_WORLD_ONTOLOGY` |
| Profile 영구 성장 철학 | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | `USER_APPROVED_ROLE / VALUES_PENDING` |
| 주점·허브 병영·연구 | `design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | `USER_APPROVED_STRUCTURE / VALUES_PENDING` |
| PR #121 preflight·병합 증거 | `reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md` | `PREFLIGHT_PASS / MERGED_PR121` |
| Grill Me 병합 주기 | `operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | `CURRENT_OPERATING_RULE` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. 현재 핵심 흐름

```text
맵 선택
→ MapRun 생성·RunState 초기화
→ Stage
→ Wave 1...N
→ Stage 정산·checkpoint
→ 정비시간
→ 다음 Stage
```

```text
영웅 해금·Profile 등록
→ 동병종 [영웅] 등급 토큰
→ 원본 병종 또는 이름 지정 영웅 선택
→ active slot 검사
→ 한 전선 비가역 배치
→ 공개 규칙 기반 자동 능력 운용
→ 생존 시 장기 상태 유지
→ 사망 시 무회수·slot clear
→ 사망 이후 새 적격 결과로만 재출전
```

## 4. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
```

## 5. 향후 동일 작업 운영

- 중요 결정 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 현재 카운터는 `0/10`이다.
- 다음 10번째 승인에서 적대적 preflight를 실행한다.
- 문서·기획 PR은 latest main 동기화·필수 CI Green·Sheet read-back·blocker 0·제품 경로 0이면 별도 승인 대기 없이 병합한다.
- GitHub auto-merge는 사용하지 않는다.
- 제품 코드 PR은 별도 작업 계약 대상이다.

## 6. 다음 Gate

```text
NEXT_PLANNING_BATCH_SELECTION
```
