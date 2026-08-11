# [현행] OMENWARD Phase B 최종 기획 검토

```yaml
updated_at: 2026-08-11
reviewed_at_kst: 2026-08-11T12:01:00+09:00
decision_id: OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1
review_type: PHASE_B_FINAL_PLANNING_REVIEW
review_result: PASS
product_decision_created: false
product_mutation: NONE
godot_mutation: NONE
base_main_observed: 069f0c9654a6cde7cea6f3343dd2fa81c6248d5d
project_main_observed_at_entry: 113f00bbddb22033bfadd2086ff8b5661815fb86
runtime_pr: 175
runtime_issue: 176
handoff_pr: 177
```

## 1. Gate

사용자는 2026-08-11 KST에 literal `기획 완료`를 명시적으로 선언했다.

```text
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = PASS
NEW_PRODUCT_DECISION_REQUIRED = FALSE
IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED
PHASE_C_GATE = OPEN
PHASE_C_STATUS = READY_TO_ENTER
```

`PHASE_C_GATE = OPEN`은 제품 구현 완료를 뜻하지 않는다. 이후 작업부터 Phase C 절차를 시작할 수 있다는 뜻이다.

## 2. Fresh authority recovery

Phase B 진입 시 다음을 다시 읽었다.

- Base `main`: `069f0c9654a6cde7cea6f3343dd2fa81c6248d5d`
- Base open PR: 0
- OMENWARD `main`: `113f00bbddb22033bfadd2086ff8b5661815fb86`
- OMENWARD open runtime/handoff PR: #175 / #177
- Google Sheet current hub, work order, current decisions, audit, main-content, history ranges
- `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md`
- whole-project content closure, quality guardrail, Elite/Boss cadence owners
- Phase A readiness dependency classification and PR175 runtime package

Base가 이전 관찰 SHA `315c66e...`에서 전진한 최신 변경은 serial-fiction integrity audit 계열이며, OMENWARD 게임 제품 의미와 직접 충돌하는 active game-design rule은 발견하지 못했다.

## 3. Feature-unit decomposition and status

| Feature unit | Current owner / evidence | Phase B classification |
|---|---|---|
| Core causality / pressure readability | Core Fun + current GDD | ALREADY_REFLECTED_STILL_VALID |
| Roulette / TokenSource physical grammar | Barracks amendment + physical remediation | ALREADY_REFLECTED_STILL_VALID |
| General/Special barracks roles | role/synergy canon + runtime package | ALREADY_REFLECTED_STILL_VALID |
| Building T2/T3 grammar | Building Tier + whole-project closure | ALREADY_REFLECTED_STILL_VALID |
| Defense names | whole-project closure | ALREADY_REFLECTED_STILL_VALID |
| Hero strategic role / commitment | whole-project closure | ALREADY_REFLECTED_STILL_VALID |
| Legendary grammar | whole-project closure | ALREADY_REFLECTED_STILL_VALID |
| Meta/Hub | whole-project closure | ALREADY_REFLECTED_STILL_VALID |
| RNG fairness / dead-run prevention | quality guardrail owner | ALREADY_REFLECTED_STILL_VALID |
| Run variation / seeded challenge | quality guardrail owner | ALREADY_REFLECTED_STILL_VALID |
| Causal review UX | quality guardrail owner | ALREADY_REFLECTED_STILL_VALID |
| Stage cadence | Elite/Boss cadence owner | ALREADY_REFLECTED_STILL_VALID |
| old Danger 4/9/14/19 cadence | older pressure matrix/current-consumer remnants | CONFLICT_OLD / SUPERSEDED |
| PR175 Issue176 seven gaps | approved runtime package | IMPLEMENTATION_COMPLETENESS |
| exact FV / combat / Elite/Boss numerics | runtime evidence dependency | POST_RUNTIME_EVIDENCE_TUNING |
| save/export/store/release adapters | platform/release owners | RELEASE_PHASE_DEFERRED |

결론:

```text
WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS_AUTHORITY = NOT_APPROVED
```

미선정 수치는 기획 누락이 아니라 측정 의존 항목이다. 런타임 증거 없이 Phase B에서 임의 확정하지 않는다.

## 4. Current-consumer conflict audit

Phase B fresh-read에서 다음 stale current-facing 표현을 발견했다.

- current GDD: `Danger 4/9/14/19`
- current GDD / Project Core / README 계열: Stage 4 Danger 통합 표현
- lifecycle/documentation routing: Aug-4 pressure matrix를 cadence 최신 owner보다 앞에 두는 잔여 표현
- current phase consumers: user gate `NOT_RECEIVED`, Phase B `NOT_RUN`, Phase C `BLOCKED`

이것은 **새 제품 결정 부족이 아니라 current-router drift**다.

최신 적용값:

```text
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
LEGACY_DANGER_CADENCE_AUTHORITY = NONE
```

과거 4/9/14/19 문서는 삭제하지 않는다. history/evidence로 보존하며 current implementation input 권위만 제거한다.

## 5. Benchmark / industry research packet

조사일: 2026-08-11 KST. 제품 사례는 공식 Steam 제품 페이지를 우선했다. 외부 사례는 자동 authority가 아니다.

| Source | Checked | Relevance | Disposition | OMENWARD consequence |
|---|---|---|---|---|
| Mechabellum — official Steam product page | 2026-08-11 | troop drafting, customization, formations, strategy-over-clicking | ADAPT | 전투 결과의 핵심은 APM보다 사전 구성·배치 판단으로 유지 |
| The Last Flame — official Steam product page | 2026-08-11 | roguelike auto-battler, build creation, strategy/decision, ascension/endless | ADAPT | soft synergy와 반복-run build causality, horizontal challenge 방향 유지 |
| Balatro — official Steam product page | 2026-08-11 | varied synergies, 8 difficulties, challenge and seeded runs | ADAPT | seeded/challenge 확장은 수평 난이도 grammar로 유지; poker economy는 복제하지 않음 |
| Luck be a Landlord — official Steam product description, prior packet reconfirmed conceptually | 2026-08-11 | slot composition without real-money gambling identity | ADAPT | 룰렛을 player-constructed probability engine으로 유지, 도박 fantasy/paid spin 금지 |
| hi-godot/godot-ai official GitHub README | 2026-08-11 | live Godot MCP, current prerequisites Godot 4.5+ / 4.7+ recommended | ADOPT_FOR_PHASE_C_PREFLIGHT | Phase C 시작 전에 실제 local/plugin/server/session truth fresh verify |
| Godot Asset Store Godot AI listing | 2026-08-11 | Asset Store may lag source; surfaced v2.9.0 | TEST / IGNORE_FOR_EXACT_VERSION | 사용자 제보 3.1.4를 자동 공식 authority로 승격하지 않음 |

공식 source 확인에서는 `Godot AI 3.1.4` exact release를 독립 확인하지 못했다. 따라서:

```text
USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4
GODOT_AI_3_1_4_EXACT_UPSTREAM_VERIFICATION = NOT_CONFIRMED_IN_PHASE_B_WEB_CHECK
GODOT_AI_3_1_4_CANON_AUTHORITY_RECONCILIATION = DEFER_TO_PHASE_C_FRESH_VERIFY
```

이는 제품 기획 blocker가 아니라 Phase C execution preflight 항목이다.

## 6. Adversarial review

### P0 — obsolete Danger cadence leakage

위험: 구현자가 `4/9/14/19 Danger + 5/10/15/20 Boss`를 다시 구현할 수 있음.

처리: latest cadence owner를 current router에 직접 연결하고 old cadence를 `SUPERSEDED / IMPLEMENTATION_INPUT_FORBIDDEN`으로 분류한다.

### P0 — Phase B가 runtime 완료를 가장하는 오류

위험: Gate가 열렸다는 이유로 PR175/Issue176을 완료 처리하거나 final 수치를 임의 선택.

처리:

```text
PR175 = OPEN_DRAFT
PR175_MERGE = FORBIDDEN_UNTIL_RUNTIME_ACCEPTANCE
ISSUE176_APPROVED_RUNTIME_GAPS = 7
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

### P1 — Godot AI version assumption

위험: 사용자 제보 3.1.4를 local installation/session verification 없이 사용.

처리: Phase C C0에서 exact local plugin/server/launcher/session을 fresh verify한다.

### P1 — benchmark imitation

위험: competitor structure를 제품 정답으로 가져오기.

처리: `ADOPT / ADAPT / AVOID / TEST / IGNORE`만 사용하고 기존 OMENWARD core causality와 충돌하면 거부한다.

적대적 검토 결과, Phase C 진입을 막는 **새 product-semantic blocker는 없음**.

## 7. Definition of Ready

```text
PLANNING_CANON_RECOVERED = TRUE
WHOLE_PRODUCT_SEMANTIC_GROUPS_CLOSED = TRUE
LATEST_STAGE_CADENCE_ROUTED = TRUE
QUALITY_GUARDRAILS_ROUTED = TRUE
USER_GATE_RECEIVED = TRUE
FEATURE_UNIT_CLASSIFICATION_COMPLETE = TRUE
DEPENDENCY_DIRECTION_DEFINED = TRUE
PROTECTED_PRODUCT_BOUNDARIES_DEFINED = TRUE
RUNTIME_PACKAGE_ALREADY_APPROVED = TRUE
ISSUE176_SCOPE_TRACEABLE = TRUE
FINAL_NUMERICS_CORRECTLY_DEFERRED = TRUE
PLATFORM_RELEASE_SCOPE_CORRECTLY_DEFERRED = TRUE
NEW_PRODUCT_DECISION_REQUIRED = FALSE
IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED
```

## 8. Phase C work order

### C0 — execution preflight

1. fresh Base/project/Sheet read + current branch/open PR/latest SHA.
2. current industry/tool verification for the concrete runtime task.
3. local Godot 4.7.1 project and Godot AI exact installed version/session/transport fresh verify.
4. reconcile user-reported 3.1.4 with actual local/plugin/upstream state.
5. revalidate/rebase PR175 against current `main`; old 11/11 is historical evidence only.
6. do not kill unrelated Godot editors/shared Godot-AI server; root cause first.

### C1 — Issue176 implementation completeness

`GUT RED -> HiGodot/Godot AI persistent authoring -> Godot parse/import -> GUT GREEN -> existing regressions GREEN`

Complete the seven approved gaps only; no unrelated subsystem expansion.

### C2 — deterministic FV evidence

Run `FV-PRIEST/MAGE/FLIER/GIANT/COMMON`, require repeat determinism, preserve raw events, and never serialize blocked outputs as fake numeric zero.

### C3 — functional-value comparison + live QA

Role-specific vector comparison, Hera live QA after Green only, tracked-source delta `NONE`, human-readable causal review.

### C4 — evidence-based tuning

Only after runtime evidence may final parameter vectors/scalars/numerics be proposed/approved. No Phase-B preselection.

### Later release phase

Shared save schema, export presets, store SDK and release gates remain separate release-phase work and are not PR175 prebuild blockers.

## 9. Phase transition

```text
PHASE_A_GPT_CHAT_PLANNING = COMPLETE_BY_USER_DECLARATION
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = PASS
PHASE_C_GATE = OPEN
PHASE_C_STATUS = READY_TO_ENTER
PRODUCT_IMPLEMENTATION_COMPLETION = FALSE
```

Phase C의 첫 행동은 C0 fresh preflight이며, 이 Phase B PR 자체는 `data/`, `scripts/`, `scenes/`, `assets/`, `addons/`, `project.godot`을 변경하지 않는다.
