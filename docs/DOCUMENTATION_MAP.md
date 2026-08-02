# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: HERO_UNIQUE_SKILL_UPGRADE_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 5
preflight: NEXT_AT_10_OF_10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
```

이 문서는 질문별 현행 책임 원본을 선택하는 라우터다. `current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

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
| 승인 Decision·5/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| 전체 시스템 Vertical Slice | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| Vertical Slice 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 영웅 해금·병종 등록 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | `MERGED_USER_APPROVED_ROSTER` |
| 영웅 토큰 변환·배치 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | `MERGED_USER_APPROVED_ACTIVATION` |
| 영웅 단일 활성·반복 출전 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | `MERGED_USER_APPROVED_ACTIVE_LIMIT` |
| 영웅 Stage 상태·사망·재출전 | `design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`, `design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` | `MERGED_USER_APPROVED_LIFECYCLE` |
| 해금 영웅 상위호환·고유 스킬 모델 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | `USER_APPROVED_CURRENT_HERO_POWER_AND_KIT_AUTHORITY` |
| 영웅 자동 발동·결정론 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | `USER_APPROVED_ALL_HEROES_AUTO_ACTIVE` |
| 초기 영웅 병종 5종 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | `USER_APPROVED_FIVE_ARCHETYPE_ROSTER` |
| 초기 영웅 검증 범위 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | `USER_APPROVED_FIVE_UNIQUE_SKILL_HEROES` |
| 영웅 스킨형 자산·단일 스킬 구조 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | `REFINED_TO_UNIQUE_ACTIVE_ONLY` |
| 영웅 전투 예산 | `design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` | `REFINED_TO_CONSTRAINED_UPGRADE` |
| 과거 강제 상쇄 축 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | `SUPERSEDED_HISTORY / NOT_CURRENT` |
| 이계 생물종·경계파쇄자 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | `MERGED_USER_APPROVED_GAMEPLAY_SCOPE` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. 현행 영웅 라우팅

```text
원본 병종 [영웅] 등급 기본 성능
+ 스킨·이름·식별 연출
+ 고유 자동 사용스킬 1개
= 제한형 상위호환 이름 지정 영웅
```

- 모든 이름 지정 영웅은 자동 사용스킬형이다.
- 영웅 전용 패시브는 없다.
- 의무 능력치 하향·강제 상쇄 축은 없다.
- 전역 활성 이름 지정 영웅 최대 1명 제한을 유지한다.
- 원본 역할·기본 공격·사거리·이동·기본 AI·리그·공통 애니메이션을 재사용한다.
- 수동 스킬·수동 타깃·저장 재굴림은 금지한다.

## 4. 초기 5명 라우팅

```text
shield_guard / archer / priest / mage / assassin
→ 각 병종 이름 지정 영웅 1명
→ 자동 고유 사용스킬 1개씩
```

```text
INITIAL_HERO_COUNT = 5
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
FINAL_RELEASE_CAP = FALSE
```

## 5. 계보·증거 경계

- `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 전체 시스템 기획 권위지만 구현 완료 증거가 아니다.
- `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`는 현행 적대적 검토 계보다.
- `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 `PILOT_RECOMMENDATION / NOT_CANON`이며 별도 승인 전 정본·구현 권한이 없다.
- 강제 상쇄 축 문서는 계보 보존용이며 현행 설계에 적용하지 않는다.

## 6. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILLS = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 운영·다음 Gate

- 현재 카운터는 `5/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 문서·기획 PR은 latest main 동기화·필수 CI Green·Sheet read-back·blocker 0·제품 경로 0이면 standing authorization에 따라 병합한다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-CONCEPTS-V1
```
