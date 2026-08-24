# OMENWARD

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
status: ACTIVE_REPLANNING
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
implementation_authorized: false
visual_generation: USER_REQUEST_ONLY
```

## Current product promise

플레이어는 **징조수호관(Omen Warden)** 으로서 세 전선의 Omen Signature를 읽고, 건물·TokenSource로 동원 확률을 설계한 뒤 3×3 징조륜의 결과를 제한적으로 조작하고 병력을 한 전선에 비가역 커밋한다. 전투 뒤에는 인과 Review로 다음 설계를 고친다.

```text
징조 관측
→ 건설 / 확률 설계
→ 3×3 룰렛 / 행·열 조작
→ 병력 획득
→ PREPARE -> COMMIT -> BATTLE -> REVIEW
→ 비가역 전선 커밋
→ 자동전투 + 제한된 전술
→ 인과 복기
```

## Current planning state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 19
TOPDOWN_BATTLEFIELD_LAYOUT = CONFIRMED
TOPDOWN_UNIT_SILHOUETTE = CONFIRMED
NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY
NORTH_STAR_BATTLEFIELD = APPROVED_DIRECTION
NORTH_STAR_ART_MOOD = APPROVED_DIRECTION
NORTH_STAR_LOWER_DECK = NEEDS_CORRECTION
NORTH_STAR_ROULETTE_INTERACTION = NEEDS_CORRECTION
LOWER_DECK_AND_ROULETTE_CORRECTION_BRIEF = COMPLETE
FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5
GITHUB_NOTION_DRIFT_CHECK = PASS
CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED
CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY
VISUAL_GENERATION = USER_REQUEST_ONLY
IMPLEMENTATION_START = NOT_AUTHORIZED
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

Final planning review owner:
- `docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md`

## Evidence boundary

현재 재기획 의미에 대한 runtime·사람 검증은 수행하지 않았다.

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
HUMAN_QA_NOT_RUN
LEGACY_C1_C2_C3_PROVEN
```

`LEGACY_C1_C2_C3_PROVEN`은 2026-07의 정확한 기술 증거가 역사적으로 존재한다는 뜻이며 현재 v4.8 제품 경험 PASS가 아니다. 정확한 head/run은 전용 audit/archive evidence owner에서 검증한다.

## Current authority order

1. fresh Base current authority + 이 저장소 `AGENTS.md`.
2. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
3. `docs/ACTIVE_CONTEXT.md`.
4. `docs/OMENWARD_GDD_CURRENT_CANON.md` / `docs/PROJECT_CORE.md`.
5. 관련 `docs/design/APPROVED_OMENWARD_*` owner.
6. Project Notion Home 및 관련 사람용 page.
7. 실제 code/data/scene/test/runtime evidence.

GitHub PR/Issue 상태는 문서에 고정하지 않고 매 작업 시작 시 fresh 조회한다.

## Visual current contract

```text
CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART
BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART
DEFAULT_CAMERA = FULL_THREE_LANES_VISIBLE
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
ROULETTE_EXPOSURE = 3×3
LOWER_CONTROL_DECK = FOCUS_ADAPTIVE_COMPACT
NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY
```

상세 owner:
- `docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_ROULETTE_DDD_FEEDBACK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md`

## Historical compatibility

- C1/C2/C3 exact proof, July Vertical Slice and old runtime PRs remain historical evidence.
- Open PR/Issue truth is always `FRESH_GITHUB_QUERY_REQUIRED`.

No current document may restore historical states as current implementation authority.
