# OMENWARD / 오멘워드

**룰렛을 설계해 군대를 만드는 로그라이트 전략 오토배틀러.**

```yaml
updated_at: 2026-08-11
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
phase_b: PASS
phase_c_gate: OPEN
phase_c_c0: PASS
current_phase_decision: OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1
preceding_phase_b_decision: OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1
```

## Current product loop

```text
예고된 압력
→ 건물 / TokenSource / 룰렛 확률 설계
→ 병력 획득
→ 비가역 전선 배치
→ 수동 전술 타이밍
→ 설명 가능한 결과 / 다음 설계
```

## Current Stage cadence

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
LEGACY_DANGER_CADENCE_AUTHORITY = NONE
```

모든 Stage 마지막 Wave에는 Elite가 존재한다. 5/10/15/20은 Boss Stage이며 Boss + final-wave Elite 규칙이 함께 적용된다. 예전 별도 Danger Stage cadence는 current implementation input이 아니다.

## Current planning / implementation gate

사용자가 literal `기획 완료`를 선언했고 Phase B final planning review와 Phase C C0 repository/local gate를 통과했다.

```text
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = PASS
NEW_PRODUCT_DECISION_REQUIRED = FALSE
IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED
PHASE_C_GATE = OPEN
PHASE_C_C0_REPOSITORY_TOOLCHAIN_GATE = PASS
PHASE_C_C0_LOCAL_HIGODOT_GATE = PASS
PHASE_C_C0_OVERALL = PASS
PHASE_C_STATUS = PR175_CURRENT_MAIN_REVALIDATION_NEXT
PR175_CURRENT_MAIN_REVALIDATION_NEXT
```

Gate open과 C0 PASS는 gameplay implementation 완료를 뜻하지 않는다. 현재 다음 작업은 PR175를 fresh current main에 rebase/update하고 exact-head 검증을 다시 수행하는 것이다.

## Runtime package

```text
PR175 = OPEN_DRAFT
PR175_CURRENT_MAIN_REBASE_REVALIDATION_REQUIRED = TRUE
ISSUE176 = OPEN
ISSUE176_APPROVED_RUNTIME_GAPS = 7
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
PR175_MERGE = FORBIDDEN_UNTIL_RUNTIME_ACCEPTANCE
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

## Current owners

- [Project Core](docs/PROJECT_CORE.md)
- [Current GDD](docs/OMENWARD_GDD_CURRENT_CANON.md)
- [Documentation Map](docs/DOCUMENTATION_MAP.md)
- [Lifecycle Registry](docs/DOCUMENT_LIFECYCLE_REGISTRY.md)
- [Whole-project content closure](docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md)
- [Quality guardrails](docs/design/APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md)
- [Elite/Boss cadence](docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md)
- [Phase B final planning review](docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md)
- [Phase C C0 local HiGodot closure](docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md)
- [Vertical Slice foundation](docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md)

## Work-entry rule

Every non-trivial task starts with fresh Base/project/Sheet recovery, targeted current benchmark/industry/tool research, `ADOPT / ADAPT / AVOID / TEST / IGNORE` classification, then canon-conflict check.

```text
BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_WORK = TRUE
COMPETITOR_BEHAVIOR_AUTOMATIC_AUTHORITY = FORBIDDEN
POST_CHANGE_ADVERSARIAL_MONITORING = REQUIRED
```

## Godot AI note

Phase B historical provenance:

```text
USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4
GODOT_AI_3_1_4_PHASE_B_STATUS = USER_REPORTED_PENDING_C0_FRESH_VERIFY
```

C0 current execution truth:

```text
GODOT_VERSION = 4.7.1-stable
GODOT_AI_PLUGIN_VERSION = 3.1.4
GODOT_AI_SERVER_VERSION = 3.1.4
GODOT_AI_3_1_4_C0_STATUS = VERIFIED_PLUGIN_SERVER_SESSION
OMENWARD_EDITOR_SETTINGS = SELF_CONTAINED_ISOLATED
OMENWARD_GODOT_AI_HTTP_PORT = 8002
OMENWARD_GODOT_AI_WS_PORT = 9502
CODEX_INSTALLATION = SHARED
OMENWARD_CODEX_HOME = C:/Users/user/.codex-omenward
SESSION_ID_FRESH_RESOLVE_EACH_EXECUTION_BLOCK = REQUIRED
```

C0 closure의 session ID/PID는 증거일 뿐 future selector가 아니다. persistent Godot authoring 전에는 exact OMENWARD project path로 세션을 fresh-resolve한다.

## Historical Vertical Slice evidence boundary

```text
V2_SPEC_APPROVED
LEGACY_C1_C2_C3_PROVEN
HUMAN_QA_NOT_RUN
```

These durable proof markers preserve the previously validated Vertical Slice C1/C2/C3 evidence. They do not assert that the current PR175 package or full product implementation is complete.
