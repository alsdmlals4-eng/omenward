# OMENWARD / 오멘워드

**룰렛을 설계해 군대를 만드는 로그라이트 전략 오토배틀러.**

```yaml
updated_at: 2026-08-20
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
implementation_authorized: false
current_chat_runtime: NOT_RUN
human_player_evidence: NOT_RUN
visual_generation: PAUSED_PENDING_USER_REFERENCE_FILES
```

## Current product promise

```text
징조 관측
→ 건설 / 동원 인장 / 미래 병력 분포 설계
→ 세 징조륜에서 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 결정적 순간의 수동 전술
→ 인과 복기
→ 다음 설계
```

플레이어는 **징조수호관(Omen Warden)** 이며, 룰렛은 카지노/가챠 장치가 아니라 플레이어가 건물과 TokenSource로 구성하는 **군사적 확률·동원 장치**다.

## Current confirmed replan decisions

현재 2026-08-20 재기획에서 다음 6개 Decision이 승인됐다.

1. `OMW-PLAN-20260820-WORLD-ROLE-01` · 징조수호관(Omen Warden)
2. `OMW-PLAN-20260820-MAPRUN-WORLD-01` · 한 Run = 한 수호성의 20 Stage Omen Cycle
3. `OMW-PLAN-20260820-PRESSURE-LANGUAGE-01` · 5 Pressure = 복합 가능한 Omen Signature
4. `OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01` · 자동생산과 TokenSource를 분리한 동원 인장망
5. `OMW-PLAN-20260820-FIRST5-FTUE-01` · 첫 5 Stage 숙련 사다리
6. `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01` · PREPARE → COMMIT → BATTLE → REVIEW Focus Mode

상세 owner는 `docs/CURRENT_CONFIRMED_DECISIONS.md`를 먼저 읽는다.

## Current Stage cadence

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
```

- 모든 Stage 마지막 Wave에 Elite가 존재한다.
- 5/10/15/20은 Boss Stage다.
- `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`는 적 종족명이 아니라 전장에서 해결해야 하는 Omen Signature다.
- Forecast는 대응 가능한 정보를 주되 정답 카운터를 직접 지시하지 않는다.

## Current planning gate

이미지 생성은 사용자가 보유한 기존 시안/레퍼런스 파일을 받을 때까지 보류한다.

이미지 외 현재 기획 우선순위:

```text
1. Decision 1~6 adversarial review / canon reconciliation
2. world conflict + core story
3. 20 Stage content / boss structure
4. balance budget
5. text UX / state-transition specification
6. visual work resumes only after user reference files arrive
```

## Current GitHub work-item truth

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

- PR #175의 unmerged runtime 변경은 현재 `main` 제품 truth가 아니다.
- Issue #176은 과거 PR175 package의 follow-up이므로 미래 구현 전에 당시 내용과 현재 main/재기획 Decision을 다시 대조한다.
- PR #197은 진행 중 별도 workstream이며 이 기획 채팅에서 수정·retarget·merge하지 않는다.

## Runtime / evidence boundary

2026-08-20 재기획 채팅에서는 현재 `main` Godot runtime을 실행하지 않았다.

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

2026-08-11~12의 signal11/HiGodot 기록은 **historical evidence**이며 현재 crash 재현을 뜻하지 않는다.

## Current owners

- [Confirmed Decisions](docs/CURRENT_CONFIRMED_DECISIONS.md)
- [Active Context](docs/ACTIVE_CONTEXT.md)
- [Project Core](docs/PROJECT_CORE.md)
- [Current GDD](docs/OMENWARD_GDD_CURRENT_CANON.md)
- [Current Implementation Status](docs/CURRENT_IMPLEMENTATION_STATUS.md)
- [Pending Decisions / Gates](docs/DECISIONS_PENDING.md)
- [Onboarding Authority](docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md)
- [Visual Requirement Inventory](docs/design/OMENWARD_VISUAL_REQUIREMENT_INVENTORY_2026-08-20.md)

## Work-entry rule

Fresh Base + fresh OMENWARD main/open PR + current Notion owner를 먼저 읽고, 중요한 Decision은 benchmark / 여러 대안 / 적대적 검토를 거친다. 진행 중 다른 workstream PR은 읽기 전용으로 보호한다.

## Historical compatibility markers

아래 문자열은 2026-08-11~12 자동 검증/문서 소비자의 역사 lineage를 위해 보존하는 **ALLOWED_LEGACY**다. 현재 상태를 뜻하지 않는다.

```text
MAIN_CANONICAL_APPROVED_10_OF_10 = HISTORICAL_2026_08_11
PHASE_B_FINAL_PLANNING_REVIEW = HISTORICAL_PASS
PHASE_C_C0_OVERALL = HISTORICAL_PASS
PR175 = OPEN_DRAFT = HISTORICAL_LABEL_ONLY
PR175_CURRENT_MAIN_REVALIDATION_NEXT = HISTORICAL_LABEL_ONLY
LEGACY_C1_C2_C3_PROVEN
HUMAN_QA_NOT_RUN
```
