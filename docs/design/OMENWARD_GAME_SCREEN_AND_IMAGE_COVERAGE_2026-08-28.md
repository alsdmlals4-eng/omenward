# OMENWARD · Game Screen and Image Coverage

```yaml
coverage_id: OMW-SCREEN-IMAGE-COVERAGE-20260828-01
github_issue: 231
status: CURRENT_TARGET_BUILD_AUDITED
scope: ACTUAL_GODOT_CONSUMERS_PLUS_PLANNED_PRODUCT_SURFACES
decision_owner: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
planned_map_topology: ONE_WARD_CITADEL_ROOT__THREE_DIVERGING_FRONT_ROUTES
runtime_evidence_ceiling: PARTIAL_TECHNICAL_HERA_CAPTURE_PLUS_HEADLESS_NATURAL_REVIEW__HUMAN_NOT_RUN
image_generation_policy: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
```

## Operating rule

필수 이미지는 서로 대체하지 않는 세 범주로 관리한다.

| Category | Purpose | Completion evidence |
|---|---|---|
| `RUNTIME_IMAGE` | 실제 Godot 화면의 캐릭터·배경·아이콘·UI·FX | consumer 연결 + 실행 화면 검증 |
| `PRODUCTION_VISUAL` | Visual Bible·규격·시트·플로우·관계·스타일 기준 | Notion과 repository 정본 등록 |
| `RELEASE_IMAGE` | logo·capsule·store screenshot·key art | 확정 플랫폼 규격의 제출 가능 파일 |

**판정식:** `목표 화면 × 실제 소비처 × 오브젝트 × 상태 × 변형 × 표현 방법`.
실제 소비처가 없는 제목 화면·상점·설정·출시물은 필요한 미래 표면으로 기록하지만, 허구의 규격이나 게임 안에서 쓰이지 않는 이미지를 자동 제작하지 않는다. 상태의 목적을 Godot theme, modulation, shader, primitive drawing이 더 정확히 수행하면 그 표현을 runtime coverage로 인정한다.

## A. Current runtime screen surfaces

| screen_id | family / priority | player goal and question | runtime consumer | asset coverage | status |
|---|---|---|---|---|---|
| `SCR-BOOT-01` | Boot / P0 | 빠르게 튜토리얼 전장으로 들어간다. | `project.godot` → `scenes/main/main.tscn` → `GameSession` | 엔진 boot; 별도 splash 미구현 | `COVERED_BY_IMPLEMENTED_SCOPE` |
| `SCR-RUN-PREPARE-01` | Run Command / P0 | “다가오는 징조에 무엇을 준비할까?” | `RunCommandScreen/TopBar`, `Fronts`, `PreparePanel` | battlefield backdrop, top HUD, 3 building thumbnails, Godot theme | `COVERED_RUNTIME` |
| `SCR-RUN-ROULETTE-01` | Run Command / P0 | “어떤 징조를 조사하고 조정할까?” | `RoulettePanel`, `StageRun` | board, device, arrows, gold/X/token frame/state, unit idle textures, Godot selection | `COVERED_RUNTIME` |
| `SCR-RUN-COMMIT-01` | Run Command / P0 | “얻은 병력을 어느 전선에 비가역 커밋할까?” | `CommitPanel`, `StageRun.confirm_pending_deployment()` | shared unit idle/token images; `OptionButton` and theme states | `COVERED_BY_SHARED_RUNTIME_ASSETS` |
| `SCR-RUN-BATTLE-01` | Battle / P0 | 세 전선의 교전·전진기지·접전지·우회로를 읽는다. | `Battlefield`, `BattlefieldView`, `UnitView`, `Fronts` | `OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1`, 20 faction/archetype idle cells, procedural clash/outpost/bypass overlays | `PARTIAL_TECHNICAL_RUNTIME` |
| `SCR-RUN-REVIEW-01` | Run Command / P0 | 결과와 재시도를 이해한다. | `ReviewPanel`, `StageRun` | Godot text/button/themed panel; no raster requirement | `COVERED_BY_GODOT_UI` |
| `SCR-STAGE-SELECT-01` | Alternate dev surface / P1 | 튜토리얼·일반 스테이지를 고른다. | `StageSelect` exists but is hidden from `main.tscn` | Godot text/button | `NOT_IN_DEFAULT_PLAYER_FLOW` |
| `SCR-STAGE-HUD-01` | Alternate dev surface / P1 | 자원·건설·전술 정보를 본다. | `StageHud` exists but is hidden from `main.tscn` | gold/capacity/building runtime images + Godot controls | `NOT_IN_DEFAULT_PLAYER_FLOW` |

## B. Runtime asset-family coverage

| family | state / variant | consumer and expression method | disposition |
|---|---|---|---|
| Three-front battlefield | forward base, clash zone, bypass routes, Ward/Veil territory | `Battlefield/Backdrop` raster plus `BattlefieldView._draw()` overlays | `RUNTIME_CONNECTED__HERA_CAPTURED` |
| Units | Lumern + Veil × shield, greatsword, assassin, spear, archer, cavalry, priest, mage, flier, giant idle identity | `FactionVisualProfile.idle_texture` → `UnitView/IdleSprite` | `20_OF_20_RUNTIME_TEXTURES_CONNECTED` |
| Unit state feedback | move, attack preparation/hit/recovery, hit, death, bypass, capture, victory | `UnitView._draw()` state silhouette, line/arc/alpha treatment; no duplicate PNG demanded by the actual runtime | `COVERED_BY_PROCEDURAL_RUNTIME_EXPRESSION` |
| Roulette | normal, inspected, moved, result confirmation | 3×3 source textures plus `Button`, modulation, tooltip, and result-list UI | `RUNTIME_CONNECTED__INSPECTABLE` |
| Prepare/HUD resources | gold, troop capacity, barracks, tower, farm | `StageHud` and `RunCommandScreen` | `RUNTIME_CONNECTED` |
| Button/selection/disabled/warning | normal, hover, pressed, focus, selected, disabled | `StyleBoxFlat`, Godot `Button`/`OptionButton`, text and modulation | `COVERED_BY_THEME_NOT_NEW_RASTER` |
| Tactical telegraph | clash ring, bypass warning, faction direction | `BattlefieldView._draw()` | `COVERED_BY_PROCEDURAL_RUNTIME_EXPRESSION` |

No current direct runtime consumer is missing a required raster asset after the battlefield backdrop addition. The deterministic no-unit tutorial path now proves actual `BATTLE → REVIEW` defeat through wave, objective, gate, and base rules; a live Hera REVIEW capture, long-session readability, and human player evaluation remain `NOT_RUN`.

Machine readback owners: `tools/audit_runtime_image_coverage.py` with `tests/python/test_runtime_image_coverage_audit.py`, and `tests/headless/natural_tutorial_resolution_test.gd` for natural result-to-review regression.

## C. Production visuals

| visual_id | intended use | repository owner | Notion destination | status |
|---|---|---|---|---|
| `PV-STYLE-01` | current visual north star and faction language | `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md` | `02 · 비주얼 바이블` | `REGISTERED` |
| `PV-BATTLEFIELD-01` | close battlefield composition / routes / forward bases | `docs/images/approved/OMENWARD_BATTLEFIELD_BACKDROP_V1.md` | `02 · 비주얼 바이블` | `LOCAL_AND_NOTION_STORED` |
| `PV-SCREEN-01` | current screen × consumer × state matrix; one-base/three-branch planning topology with per-branch forward base and clash-zone anchors | this file | Notion coverage page update in the next audit task | `REPOSITORY_REGISTERED__PLANNED_ROUTE_STATES_NOT_RUNTIME_APPLIED` |
| `PV-UNIT-01` | idle/unit geometry and faction identity | `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md` | Visual Bible / asset records | `REGISTERED` |

## D. Release / external surfaces

| screen_id | needed deliverables | actual consumer | status / blocker |
|---|---|---|---|
| `REL-LOGO-01` | title logo and application icon | no title/menu or package presentation route | `DEFERRED_BY_NO_PRODUCT_CONSUMER` |
| `REL-STORE-01` | Steam/Google Play capsule, screenshot, key art | platform release authority exists; exact current store specification must be fresh-read before generation | `REQUIRES_PLATFORM_SPEC` |
| `REL-TRAILER-01` | gameplay capture/key art/banner | no final product loop or capture brief | `REQUIRES_PLAYABLE_VERTICAL_SLICE` |

## E. Planned game surfaces (not yet runtime consumers)

Title/menu, save/load, pause/settings, game over, ending/credits, event/dialogue, codex/archive, upgrade/shop/forge, full route map, and separate result/reward surfaces are recorded as planned product surfaces. They become production/image work only when a Godot scene/route and player interaction contract are added. Their omission from current asset files is **not** a runtime image defect.

## Evidence and next actions

1. Capture an actual COMMIT assignment state and a live Hera REVIEW frame using the current main scene when a bounded player-flow scenario is available.
2. If a capture identifies a clarity failure, add the smallest consumer-bound image, shader, or Godot theme asset and validate it in the same resolution.
3. Before a title, settings, save/load, or release-art production pass, establish that surface’s actual Godot consumer and platform dimensions.
