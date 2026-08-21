# [현행] OMENWARD Handoff Context

```yaml
updated_at: 2026-08-21
status: CURRENT_V4_7_HANDOFF
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
current_project_core: docs/PROJECT_CORE.md
implementation_authorized: false
visual_generation: USER_REQUEST_ONLY
```

## 1. 새 세션에서 가장 먼저 복원할 것

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 18
CURRENT_NEXT = REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
VISUAL_GENERATION = USER_REQUEST_ONLY
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
```

## 2. Current read order

1. fresh Base current authority.
2. fresh OMENWARD `main`, PR, Issue inventory.
3. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
4. `docs/ACTIVE_CONTEXT.md`.
5. `docs/OMENWARD_GDD_CURRENT_CANON.md`.
6. `docs/PROJECT_CORE.md`.
7. relevant current Decision owner.
8. Project Notion Home + relevant human-facing page.
9. runtime scope가 열렸을 때 actual code/data/scene/test/runtime.

## 3. Product core

```text
건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.

징조 관측
→ 건설 / 미래 확률 설계
→ 3×3 징조륜 / 제한된 행·열 조작
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한 전술
→ 인과 Review
```

## 4. Current world / stage truth

```text
PLAYER_ROLE = Omen Warden / 징조수호관
VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
RUN_HISTORY_RESET = FALSE
PRESSURE = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
DANGER_STAGE_TYPE = REMOVED
```

## 5. Current UI / visual truth

```text
RUN_COMMAND_SCREEN = PREPARE -> COMMIT -> BATTLE -> REVIEW
CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART
BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART
DEFAULT_CAMERA = FULL_THREE_LANES_VISIBLE
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
ROULETTE_EXPOSURE = 3×3
LOWER_CONTROL_DECK = FOCUS_ADAPTIVE_COMPACT
```

Latest visual owners:
- `docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md`

## 6. Current work gate

```text
TOPDOWN_BATTLEFIELD_LAYOUT = COMPLETE
TOPDOWN_UNIT_SILHOUETTE = COMPLETE
CURRENT = REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
THEN = COMPONENT_SHEET
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
THEN = IMPLEMENTATION_AUTHORITY_REQUIRED
```

이미지 생성은 사용자가 명시적으로 요청한 경우에만 수행한다.

## 7. Balance / implementation boundary

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
IMPLEMENTATION_AUTHORITY = NONE
```

## 8. Historical evidence boundary

```text
LEGACY_C1_C2_C3_PROVEN
HUMAN_QA_NOT_RUN
```

Historical exact proof owner:
- `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`
- `docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`
- `docs/C3_CORE_UX_AUDIT_2026-07-23.md`
- `docs/archive/2026-07/pre-v2-canon/CURRENT_IMPLEMENTATION_STATUS_PRE_V2.md`

과거 signal11 / HiGodot / GUT / Hera / Issue176 execution evidence는 history다. fresh current-main execution 없이 current blocker나 next step으로 사용하지 않는다.

## 9. GitHub work-item rule

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
PR197 = CLOSED_UNMERGED_SUPERSEDED_BY_198
```

## 10. Notion / repository sync

- Notion = human-facing current workspace.
- Repository = structured/runtime current canon.
- Google Sheet = compatibility/history only.
- current meaning 변경 후 destination readback 필수.

## 11. Do not infer

- 과거 technical PASS → current v4.7 player-experience PASS.
- closed-unmerged PR → current main implementation.
- existing prototype UI → approved current UX implementation.
- normalized balance envelope → final product numerics.

## 12. Next-session stopping rule

새 기획 결정이 필요하거나 current canon과 충돌하거나 범위/권한이 바뀌는 경우만 사용자 결정으로 올린다. 저장소에서 확인 가능한 stale reference·validator drift·historical/current 분리 문제는 기술 교정 대상으로 처리한다.
