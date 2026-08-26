# OMENWARD · GPT Work Image-Production Handoff · 2026-08-26

```yaml
handoff_id: OMW-HANDOFF-20260826-GPT-WORK-IMAGE-PRODUCTION-01
handoff_state: READY_FOR_GPT_WORK
receiver_surface: CHATGPT_WORK
receiver_role: GPT_NONCODING_PROJECT_OWNER
prepared_at: 2026-08-26
prepared_from_omenward_main: 9aaa12005daf99dfb3bda03fb15884307ab49438
prepared_with_base_main: 06669fe9c6a3ccd6f3b0d19c5757540bfdcc0623
current_user_work_mode: PLANNING_PLUS_IMAGE_ONLY
current_user_order: REQUIRED_GAME_IMAGES_FIRST_THEN_CODEX
current_image_package: OMW-IMG-GOALS-20260826-RUNTIME-CONSUMER-COVERAGE-01
current_image_package_status: P0_REMAINDER_CANDIDATE_BATCH_READY_FOR_USER_REVIEW
current_gate: P0_REMAINDER_CANDIDATE_BATCH_REVIEW
image_generation: USER_REQUEST_ONLY
codex_godot_execution: BLOCKED_UNTIL_ALL_B_SCOPE_ASSETS_USER_APPROVED_CLEANED_EXPORTED_AND_IMPLEMENTATION_READY
runtime_validation: NOT_RUN
human_player_evidence: NOT_RUN
google_sheet_role: COMPATIBILITY_HISTORY_ONLY_STALE
```

## 1. Handoff purpose

This is the durable entry point for continuing OMENWARD in **ChatGPT Work**.

Do not reconstruct current state from this chat, memory, old handoffs, old images, stale Sheet rows, or old PR SHAs. The receiver must fresh-read current Base + OMENWARD + Notion, then use this handoff only as a compressed routing map.

Current owner split:

```text
PLANNING / NOTION / IMAGE NEED / IMAGE GENERATION / IMAGE REVIEW / HANDOFF = GPT / ChatGPT Work
ACTUAL GODOT PRODUCT IMPLEMENTATION = Codex, later only
```

The user explicitly moved ongoing work to GPT Work. This does **not** authorize Codex/Godot product implementation and does **not** approve any pending Image Goal automatically.

## 2. Mandatory fresh-read bootstrap in GPT Work

Read in this order before mutation:

1. fresh Base `main`, `START_HERE.md`, `AGENTS.md`, and only the relevant current Skills;
2. fresh OMENWARD default branch, latest commit, open/draft PRs and relevant Issues;
3. OMENWARD `AGENTS.md`;
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`;
5. `docs/ACTIVE_CONTEXT.md`;
6. `docs/OMENWARD_GDD_CURRENT_CANON.md` + `docs/PROJECT_CORE.md`;
7. current image owners listed below;
8. Project Notion Home + image-production pages;
9. actual code/Scene/Resource/data/tests only for consumer reality checks;
10. Google Sheet only as compatibility/history input unless authority explicitly changes.

Important drift note: `docs/ACTIVE_CONTEXT.md` and `docs/CURRENT_CONFIRMED_DECISIONS.md` still contain the 2026-08-25 visual-closeout router. They are not sufficient by themselves to reconstruct the later 2026-08-26 runtime-consumer image work. For current image status, use the newer merged image planning/approval records + current Notion image pages, while preserving the higher-level gameplay Decisions.

## 3. ChatGPT Work / memory boundary

Fresh Base `main` `06669fe9...` includes the current ChatGPT Project memory guidance for Work/reuse.

For a normal solo project that uses ChatGPT Work and cross-project/Base reuse, Base recommends **Default memory** rather than Project-only isolation. This is a product/workspace preference, not project authority.

```text
MEMORY = CONTEXT AID ONLY
PROJECT CANON = STILL FRESH-READ GITHUB + NOTION + ACTUAL EVIDENCE
```

Do not promote remembered facts, another project's rules, old chat content, or cross-project reuse into OMENWARD canon without current-source confirmation.

If the product UI/memory setting differs from Base's recorded guidance, do not block project work; simply keep canon fresh-read/readback discipline.

## 4. Fresh repository state at sender closeout

```text
BASE_MAIN = 06669fe9c6a3ccd6f3b0d19c5757540bfdcc0623
OMENWARD_MAIN = 9aaa12005daf99dfb3bda03fb15884307ab49438
```

Current known open OMENWARD PRs at sender closeout:

- PR #212 `test: define r5.4 workspace authority reconciliation` — OPEN DRAFT, head `b121c7822a26c26915405fd30ac1c24a6a76a0d2`, unrelated/read-only.
- PR #209 `docs: align front doors with scoped implementation authority` — OPEN DRAFT, stale/diverged, unrelated/read-only.
- PR #205 `docs: approve orchestration-first vertical slice architecture` — OPEN, stale/diverged, unrelated/read-only.

Do not rebase, close, merge, absorb, or mutate these from the image-production lane unless the user explicitly names the PR and action.

## 5. Google Sheet conflict

Fresh Sheet read still shows the historical state:

```text
OMENWARD main = b51bb29471ab802c6241d72a9af1226209934887
Base = ee8227d1aeae8e159ea2f9c4ba71bb0ff9e4349a
PR175 / Issue176 / signal11 runtime handoff
```

This materially conflicts with current GitHub/Notion image work.

Current rule:

```text
GOOGLE_SHEET = COMPATIBILITY / HISTORY ONLY
NO SHEET WRITE FOR THIS HANDOFF
```

Do not use the Sheet's old runtime next-step as the current project next action.

## 6. Protected product identity

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 3×3 징조륜 결과 / 제한된 행·열 조작
→ 병력 획득
→ 세 전선 중 하나에 비가역 COMMIT
→ 자동전투 + 제한된 수동 전술
→ REVIEW 인과 복기
```

Protected visual/game identity:

```text
PLAYER_ROLE = Omen Warden commander
DIRECT_HERO_MELEE_FANTASY = FORBIDDEN_AS_PRIMARY
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
ROULETTE_EXPOSURE = 3x3
CASINO_SLOT_MACHINE_LANGUAGE = FORBIDDEN
```

Faction language:

```text
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
VEIL_SHAPES = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
```

## 7. Current image-production policy

Current policy ID:

`OMW-VIS-POLICY-20260826-RUNTIME-CONSUMER-ASSET-FIRST-01`

```text
NO_RUNTIME_OR_PRODUCT_CONSUMER = NO_IMAGE_PRODUCTION_TASK
EXPLANATION_SHEET = PLANNING_REFERENCE_ONLY
FULL_SCREEN_MOCKUP = PLANNING_REFERENCE_ONLY
COMPARISON_BOARD = PLANNING_REFERENCE_ONLY
```

Generate only assets with concrete game/product consumers: unit sprites/animation sources, unit-derived token crops, Gold/X/token textures, Omen/HUD/minimap icons, real building/world assets, Omen Warden command asset, and VFX only where raster/flipbook is truly required.

Prefer Godot Theme/NinePatch/shader/primitive for panel/button/selected/disabled/valid-invalid states when those do not require bespoke pixels.

## 8. Current visual/asset lifecycle truth

### `OM-IMG-023`

```text
STATUS = REFERENCE_ONLY
ROLE = USER-APPROVED VISUAL NORTH STAR
RUNTIME_ASSET = NO
```

Full-resolution authority:

- Drive ID `1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5`
- 1536×1024 PNG
- SHA-256 `0326b012d1fbefba85b545086b84992051591edff6f3b7e159cf3e083f204224`

Do not use it as a literal battlefield background and do not regenerate it from memory.

### `ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1`

```text
STATUS = APPROVED
IMPLEMENTATION_READY = NO
IMPLEMENTED = NO
RUNTIME_VERIFIED = NO
PIXEL_CLEANUP = NOT_RUN
```

Durable source:

- `OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1.png`
- 1254×1254 RGBA
- SHA-256 `3e98fb83f5ac9169c387e6669c8ba545375700fc2346fc004781754884b2a50a`
- Drive ID `1ZiVrA2mxO8sfzzct6uuPAk_b0NDMK8b8`
- approval record: `docs/images/approved/OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1_APPROVAL_2026-08-26.md`

Disposition: `REUSE_WITH_EDIT`. Never redraw from zero unless the user explicitly requests a revision.

### `ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1`

```text
BRIEF = READY
IMAGE = GENERATED
USER_APPROVAL = APPROVED
PIXEL_CLEANUP = NOT_RUN
IMPLEMENTATION_READY = NO
```

Owner:

`docs/images/approved/OMENWARD_ASSET_UNIT_VEIL_SHIELD_GUARD_IDLE_V1_APPROVAL_2026-08-26.md`

A later unregistered blue-knight generation is **REJECTED / NOT_CANON** and does not satisfy this Veil brief.

## 9. Actual implementation reality

At sender closeout:

```text
PROJECT_PRODUCT_IMAGE_ASSETS_IMPLEMENTED = 0
PROJECT_PRODUCT_IMAGE_ASSETS_RUNTIME_VERIFIED = 0
```

Current consumer seams remain graybox:

- `scripts/units/unit_view.gd` — procedural circle/polygon/line drawing;
- `scripts/battle/battlefield_view.gd` — procedural rect/line/outpost graybox;
- `scenes/ui/stage_hud.tscn` — Label/Button graybox.

Static visual approval is not implementation evidence.

## 10. Current Image Goal package

Primary owner:

`docs/images/planning/OMENWARD_REMAINING_IMAGE_GOALS_AND_CODEX_INTEGRATION_QUEUE_2026-08-26.md`

Tracker/policy owner:

`docs/images/planning/OMENWARD_IMAGE_PRODUCTION_MASTER_CHECKLIST_2026-08-26.md`

Current queue:

```text
P0 = 13 Goal Packets
P1 = 6 Goal Packets
P2 = 5 Goal Packets
P3 = 2 Goal Packets
```

Current approved Codex-start policy is **B**:

```text
B = finish all P0 + current-consumer P1 assets
→ user approval
→ cleanup/export
→ IMPLEMENTATION_READY
→ only then Codex image integration
```

Alternative A (produce all future P2/P3 before Codex) is rejected as premature overproduction.
Alternative C (Codex after each Goal) conflicts with the current user order `images first → Codex`.

**Current decision:** `OMW-IMG-QUEUE-APPROVAL-20260826-B-01` records the user's `B안 승인`. It authorizes the B scope only; it does not auto-generate an image or start Codex.

## 11. Current user gate after B approval

- `GOAL_QUEUE_STATUS = P0_REMAINDER_CANDIDATE_BATCH_READY_FOR_USER_REVIEW`
- `UNIT_ANIMATION_PRODUCTION_CONTRACT = USER_APPROVED_CURRENT` — `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md`
- `CURRENT_GATE = P0_REMAINDER_CANDIDATE_BATCH_REVIEW`
- `NEXT_REQUIRED_ACTION = AWAIT_USER_BATCH_REVIEW_OF_P0_REMAINDER_CANDIDATES`
- `NEXT_IMAGE_GENERATION = REQUIRES_ITS_OWN_EXPLICIT_USER_APPROVAL`
- `CODEX = BLOCKED`

B approval fixes the production sequence: current-consumer P0 plus current-consumer P1 assets must become approved, cleaned/exported, and `IMPLEMENTATION_READY` before Codex integration starts. The Veil idle was generated only after its separate explicit generation approval and is now user-approved; no future asset is auto-authorized.

## 12. Non-image gate before mass unit animation art

Before generating full unit animation atlases at scale, lock a text/data production contract:

`UNIT_ANIMATION_PRODUCTION_CONTRACT`

It must settle at minimum:

- exact frame count per state where needed;
- FPS/timing;
- pivot / ground baseline;
- atlas arrangement / cell geometry;
- facing conventions;
- attack impact timing;
- unresolved `skill_1` choreography.

Do not turn this information gap into an explanation image.

Other deferred information gates:

- `UNIT_TIER_VISUAL_DATA_CONTRACT` before IMG-19;
- `BUILDING_T3_CANON_RECHECK` before IMG-24;
- `BOSS_BEHAVIOR_VISUAL_RECHECK` before IMG-20;
- `BELLU_CURRENT_SURFACE_RECHECK` before IMG-22;
- `PLATFORM_SPEC_RECHECK` before IMG-26.

## 13. Codex boundary

Codex integration queue already exists in the Goal package, but execution is blocked.

```text
CODEX_PRODUCT_IMAGE_INTEGRATION = NOT_STARTED
UNBLOCK = user-approved current-playable P0/P1 assets are IMPLEMENTATION_READY
```

Codex must not generate/redesign art. If a needed visual is missing, return to GPT as `GPT_VISUAL_REQUEST`.

When Codex eventually starts, first implementation Goal is:

`CODEX-IMG-01 — Unit Rendering Foundation + Shield Pair`

Expected later validation includes actual Godot execution and 960×540 / 1280×720 / 1920×1080 screenshot/readability evidence. Until then all runtime/human states remain NOT_RUN.

## 14. Notion entry points

Human Home:

- https://app.notion.com/p/3c41b237eb1c816fbbc8e2dddc18b6eb

Current image production checklist:

- `19 · 이미지 제작 · Runtime Consumer Asset Checklist`
- https://app.notion.com/p/3c81b237eb1c8186ad5cf572abcd53f1

Current Goal Queue:

- `23 · Remaining Image Goals · Codex Handoff Queue`
- https://app.notion.com/p/3c81b237eb1c817db243f44aaa0d741d

Approved Lumern asset:

- `21 · Approved Asset · Lumern Shield Guard Idle V1`
- https://app.notion.com/p/3c81b237eb1c818389edd4a718e7e879

Veil brief:

- `22 · Asset Brief · Veil Shield Guard`
- https://app.notion.com/p/3c81b237eb1c8180b30bc98f8bf067b6

## 15. First actions in GPT Work after B approval

1. Fresh-read Base + OMENWARD + Notion.
2. Confirm the Shield Guard idle pair approval and current main/PR state.
3. Keep P2/P3 deferred and Codex/Godot blocked.
4. Keep `UNIT_ANIMATION_PRODUCTION_CONTRACT` as the pair-pilot owner; no mass atlas without its cleaned-pair geometry addendum.
5. Perform pair pixel cleanup or any future image/edit only after its Goal-specific explicit user approval.

## 16. Suggested first GPT Work prompt

The user should not need to restate project history. A minimal continuation prompt is enough:

```text
오멘워드 인수인계 이어서 진행해.
GitHub/Notion/Base를 fresh-read하고
OMW-HANDOFF-20260826-GPT-WORK-IMAGE-PRODUCTION-01 기준으로 현재 Gate부터 이어가.
과거 대화는 정본으로 쓰지 말고, 이미지 생성과 Codex는 승인 경계를 지켜.
```

## 17. Evidence ceiling at handoff

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_MINIMAP_READABILITY = NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN
CURRENT_GUT_RED = NOT_RUN
CURRENT_GUT_GREEN = NOT_RUN
CURRENT_HERA_LIVE_QA = NOT_RUN
CURRENT_HUMAN_USABILITY = NOT_RUN
CURRENT_PLAYER_EXPERIENCE = NOT_RUN
```

Do not upgrade any of these from static docs, CI, image approval, Notion attachment readback, or memory.

## 18. Transfer acceptance condition

The GPT Work receiver is considered ready when it can state, after fresh-read:

1. current Base and OMENWARD main SHAs;
2. current open workstreams and read-only boundaries;
3. current image Goal package and approval status;
4. approved Lumern source and its non-runtime status;
5. Veil Shield Guard as a user-approved idle source, still not Implementation Ready;
6. the current B approval, its P0/current-consumer P1 boundary, and the separate approval requirement for every future image;
7. stale Google Sheet conflict;
8. runtime/human evidence ceiling.

Until that readback exists:

```text
HANDOFF_PACKET = READY
RECEIVER_FRESH_READ = REQUIRED
NEW_IMAGE_GENERATION = BLOCKED
CODEX = BLOCKED
```
