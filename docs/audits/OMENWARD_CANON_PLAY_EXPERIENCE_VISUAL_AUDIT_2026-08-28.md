# OMENWARD 정본·핵심 경험·시각 이해 감사 · 2026-08-28

> **Historical snapshot boundary — 2026-08-28:** 이 감사는 Storybook 전략 지도 전환 이전의 정본·기술 증거를 기록한다. `OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01`이 current visual owner/status만 supersede하며, 캡처된 legacy-build 증거 자체는 무효화하지 않는다.

```yaml
audit_id: OMW-AUDIT-20260828-CANON-PLAY-VISUAL-01
issue: 236
mode: REVIEW
repository_main: b2f1fc6b1605047140cc68febbadbaa6f017112d
base_main: 7cfc75d607d1ed4d0f8323d4389e64da93df00c8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
notion_home: 3c41b237-eb1c-816f-bbc8-e2dddc18b6eb
status: CANON_RECONCILED__HUMAN_PLAYTEST_REMAINS
```

## 1. Source classification

| Class | Current owner or evidence | Audit disposition |
|---|---|---|
| `CURRENT` | Decision index, Active Context, current GDD, Project Core, Run Command implementation, 2026-08-28 screen/image coverage, Notion Home | Current truth |
| `HISTORICAL` | 2026-08-24 final planning review, 2026-08-25 visual receiver acknowledgement, legacy C1/C2/C3 evidence | Preserve with explicit historical label |
| `SUPERSEDED` | standalone Anime Pixel / Clean Pixel, full-road default, minimap-not-required wording | Do not restore as current |
| `CONFLICT` | several active routers and Python checks still showed the 21-decision / `OM-IMG-023` / natural-capture next-gate state | Corrected in Issue #236 |
| `UNKNOWN_UNVERIFIED` | human usability, player experience, sustained battlefield/minimap readability, visual rights review, final economy numerics | No PASS claim |

## 2. Reconciled current state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 22
CURRENT_VISUAL_DECISION = OMW-VISUAL-20260828-BATTLEFIELD-MAP-ROULETTE-PICKER-01
APPROVED_VISUAL = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
APPROVED_PARENT_VISUAL = OM-IMG-023
IMPLEMENTATION_EXECUTION = IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN
CURRENT_NEXT = HUMAN_PLAYTEST_FOR_BATTLEFIELD_READABILITY_AND_ROULETTE_INSPECTION
```

The 2026-08-25 front-state/minimap decision and `OM-IMG-023` remain the protected visual parent/reference. The 2026-08-28 presentation decision and backdrop are the current slice-level presentation owner. This does not promote a technical capture to human/player validation.

## 3. Player experience understanding

```text
Forecasted three-front pressure
→ construct/choose TokenSource to change future unit probability
→ inspect and make limited row/column changes to a 3×3 omen board
→ receive a unit result
→ commit that unit irrevocably to one front
→ observe automatic battle and limited tactical intervention
→ review the causal chain and adapt the next stage's design
```

The player promise is strategic authorship under visible future pressure, not gambling or direct-hero action. The risky hypothesis is whether a new player can independently connect forecast → probability design → roulette result → irreversible front commitment → observed outcome.

## 4. Evidence ceiling

| Claim | Evidence status |
|---|---|
| Run Command state contracts, roulette selection inspection, visual asset links, scene contracts | Verified by fresh headless tests |
| Tutorial BATTLE → REVIEW defeat path | Verified headlessly through existing natural rules |
| 960×540 / 1280×720 / 1920×1080 technical capture | Historical/current documented partial technical evidence |
| Human battlefield/minimap readability and roulette understanding | `NOT_RUN` |
| Player fun, first-session memory, and retention motivation | `NOT_RUN` |

## 5. Incident / lesson

**Incident:** a later current Decision and runtime evidence update did not propagate to every current router and its tests.

**Solution:** corrected active projection documents and their contract tests; preserved earlier visual material as a parent/historical reference rather than deleting it.

**Lesson:** any current Decision that changes `current_visual_decision`, decision count, or `CURRENT_NEXT` must update all active router projections and their validator expectations in the same change.

**Base promotion:** `NO_BASE_PROMOTION` for now. The finding has one project-specific visual lineage and no demonstrated second-project consumer.

## 6. Separate follow-up

Issue #237 owns the unrelated full-suite environment/hygiene failures: absent local `numpy`, CI-only Base checkout assumption, and tracked generated Godot import artifacts. They are not resolved or hidden by this audit.
