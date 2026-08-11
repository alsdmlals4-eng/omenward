# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-11
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
phase_b: PASS
phase_c_c0: PASS
phase_c_gate: OPEN
current_phase_decision: OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1
preceding_phase_b_decision: OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1
```

## Current milestone

```text
PHASE_A_GPT_CHAT_PLANNING = COMPLETE_BY_USER_DECLARATION
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = PASS
IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED
PHASE_C_GATE = OPEN
PHASE_C_C0_REPOSITORY_TOOLCHAIN_GATE = PASS
PHASE_C_C0_LOCAL_HIGODOT_GATE = PASS
PHASE_C_C0_OVERALL = PASS
PHASE_C_STATUS = PR175_CURRENT_MAIN_REVALIDATION_NEXT
PR175_CURRENT_MAIN_REVALIDATION_NEXT
```

## Phase C order

### C0 — fresh execution preflight — COMPLETE
- Base/project/Sheet current truth: verified and synchronized
- Godot 4.7.1 + Godot AI plugin/server 3.1.4: verified
- self-contained OMENWARD editor + HTTP8002/WS9502: verified
- shared Codex + project-specific `CODEX_HOME`: verified
- exact OMENWARD session registry: verified at closure; future session fresh-resolve required
- repository/toolchain and local HiGodot C0 gates: PASS

### Current transition — PR175 current-main revalidation
Before C1 persistent authoring, rebase/update PR175 against fresh current main and re-run exact-head validation. Historical PR175 Green is not current evidence.

### C1 — Issue176 implementation completeness
Seven approved runtime gaps via GUT RED → HiGodot/Godot AI authoring → parse/import → GUT Green → existing regressions.

### C2 — deterministic FV evidence
`FV-PRIEST / FV-MAGE / FV-FLIER / FV-GIANT / FV-COMMON`, repeat determinism, raw output preservation.

### C3 — functional-value review / live QA
Role-specific vectors, Hera after Green only, tracked-source delta NONE, human-readable causal review.

### C4 — evidence-based tuning
Only after runtime evidence propose final parameter vectors/scalars/numerics.

## Current Godot AI execution route

Phase B historical provenance:

```text
USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4
GODOT_AI_3_1_4_PHASE_B_STATUS = USER_REPORTED_PENDING_C0_FRESH_VERIFY
```

Current verified route:

```text
GODOT_AI_3_1_4_C0_STATUS = VERIFIED_PLUGIN_SERVER_SESSION
OMENWARD_EDITOR_SETTINGS = SELF_CONTAINED_ISOLATED
OMENWARD_GODOT_AI_HTTP_PORT = 8002
OMENWARD_GODOT_AI_WS_PORT = 9502
OMENWARD_CODEX_HOME = C:/Users/user/.codex-omenward
SESSION_ID_FRESH_RESOLVE_EACH_EXECUTION_BLOCK = REQUIRED
```

C0 closure session/PID values are evidence only and are never reused as future selectors.

## Current Stage roadmap

```text
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
```

Stage 1–4 are normal Stage cadence with a final-wave Elite learning check; Stage 5 is the first Boss + Elite synthesis check. The same 5-Stage Boss rhythm continues through Stage 20.

## Historical Vertical Slice automated evidence

```text
기존 기술 기준선·C1·C2·C3 자동 증거 확보
C1 승인 룰렛 핵심 계약 원격 검증·병합 완료
**REMOTE_PROVEN**
제품 구현: `NOT_STARTED`
```

These markers preserve the durable historical C1/C2/C3 proof and the Vertical Slice's own implementation boundary. They do not mean the current PR175 runtime package or full product is complete.

## Release-deferred

```text
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
SHARED_SAVE_SCHEMA = NOT_STARTED
EXPORT_PRESETS = ABSENT
```

## Planning lineage — historical checkpoints only

These markers preserve provenance; they are not the current planning percentage.

```text
OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1 = 3_OF_10 / SUPERSEDED_LINEAGE
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1 = 4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1 = 5_OF_10
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1 = 6_OF_10
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1 = 7_OF_10_LINEAGE
```

Current whole-project product closure owner:
`docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md`.

Current C0 execution closure owner:
`docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md`.
