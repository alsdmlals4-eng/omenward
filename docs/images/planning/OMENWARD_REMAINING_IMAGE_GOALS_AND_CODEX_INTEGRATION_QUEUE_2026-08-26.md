# OMENWARD · Remaining Image Goals + Codex Integration Queue

```yaml
work_package_id: OMW-IMG-GOALS-20260826-RUNTIME-CONSUMER-COVERAGE-01
status: USER_APPROVED_B_CURRENT
created_at: 2026-08-26
scope: PROJECT_IMAGE_GAP_AUDIT_AND_FUTURE_CODEX_INTEGRATION_HANDOFF
current_user_order: REQUIRED_GAME_IMAGES_FIRST_THEN_CODEX
image_generation_this_work_package: P0_REMAINDER_CANDIDATE_BATCH_GENERATED_AWAITING_USER_REVIEW
codex_godot_execution: BLOCKED_UNTIL_APPROVED_P0_AND_CURRENT_CONSUMER_P1_IMPLEMENTATION_READY
runtime_validation: NOT_RUN
base_main_fresh_read: 05d44bba978f4cff0fc94ade8e54825f5d6c80f0
omenward_main_fresh_read: 43f37e2bf25ec4f38a42936c3fea367d9c826370
google_sheet_role: COMPATIBILITY_HISTORY_ONLY_STALE
```

## 1. 목적과 완료 경계

이 문서는 이미지를 많이 만드는 목록이 아니다. **실제 게임 또는 실제 제품 배포면이 소비하는 이미지 중 현재 부족한 것만** Image Goal로 묶고, 사용자 승인 뒤에만 제작하며, 승인 완료 뒤 Codex가 실제 Godot 소비처에 연결할 수 있도록 Integration Goal을 준비한다.

```text
CURRENT CANON / IMPLEMENTATION
→ EXISTING VISUAL INVENTORY
→ REUSE DECISION
→ ACTUAL CONSUMER GAP
→ IMAGE GOAL
→ USER REVIEW / APPROVAL
→ GPT IMAGE PRODUCTION
→ NOTION APPROVED ASSET REGISTRATION
→ CODEX INTEGRATION GOAL
→ GODOT IMPORT / CONNECTION
→ RUNTIME SCREENSHOT / PLAY VALIDATION
```

상태는 반드시 분리한다.

```text
REFERENCE_ONLY
DRAFT
NEEDS_REVISION
APPROVED
IMPLEMENTATION_READY
IMPLEMENTED
RUNTIME_VERIFIED
REJECTED
SUPERSEDED
```

`APPROVED != IMPLEMENTATION_READY != IMPLEMENTED != RUNTIME_VERIFIED`.

## 1.1 User decision · B approval

- Decision ID: `OMW-IMG-QUEUE-APPROVAL-20260826-B-01`
- User input: `B안 승인`
- Status: `USER_APPROVED_CURRENT`
- Approved scope: P0 + current-consumer P1 assets → cleanup/export → Implementation Ready → Codex integration.
- Deferred scope: P2/P3 preproduction.
- IMG-01 Shield Guard pair: cleanup master pair and the animation-production contract are completed and user-approved.
- Codex/Godot: blocked until the approved scope is Implementation Ready.

Decision record: `docs/images/approved/OMENWARD_IMAGE_GOAL_QUEUE_B_APPROVAL_2026-08-26.md`.

## 2. Fresh-read authority / drift

- Base `main`: `05d44bba978f4cff0fc94ade8e54825f5d6c80f0`.
- OMENWARD `main`: `43f37e2bf25ec4f38a42936c3fea367d9c826370`.
- Open PR #205/#209/#212 are unrelated/read-only to this package.
- `docs/ACTIVE_CONTEXT.md` and `docs/CURRENT_CONFIRMED_DECISIONS.md` still carry the 2026-08-25 closeout router and do not yet describe the merged 2026-08-26 runtime-consumer asset work. Live image status therefore comes from merged image planning/approval records + Notion current image pages.
- Google Sheet `00_프로젝트_허브` still points to OMENWARD `b51bb294...`, Base `ee8227...`, PR175/Issue176 runtime handoff. It is stale compatibility/history, not current image authority.

## 3. Existing visual inventory and lifecycle

| Visual | Current role | Lifecycle | Reuse |
|---|---|---|---|
| `OM-IMG-023` | Front-State/minimap/SD fantasy visual north-star | `REFERENCE_ONLY` (user-approved reference) | `REUSE_AS_IS` as style/composition reference only |
| `ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1` | actual Lumern Shield Guard identity source | `APPROVED` | `REUSE_WITH_EDIT` for cleanup, runtime-scale export, animation expansion, token crop |
| `ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1` | actual Veil Shield Guard identity source | `APPROVED` | `REUSE_WITH_EDIT` for cleanup, runtime-scale export, animation expansion, token crop |
| historical `OMW-VIS-001~012` sheets/mockups | composition/UX history | `REFERENCE_ONLY` or `SUPERSEDED` | layout/style reference only; not runtime pixels |
| historical VR-001/VR-002 and old image-generation candidates | older visual lineage | `REFERENCE_ONLY` / `SUPERSEDED` | selective reference only |
| unregistered second blue-knight generation after Lumern approval | conflicts with Veil brief and has no approval | `REJECTED` | `REJECT` |
| GUT/addon/editor PNG/SVG files | tooling assets | not OMENWARD product art | `REJECT` for game content |

Durable approved Lumern source:

```text
FILE = OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1.png
SIZE = 1254x1254 RGBA
SHA256 = 3e98fb83f5ac9169c387e6669c8ba545375700fc2346fc004781754884b2a50a
DRIVE_ID = 1ZiVrA2mxO8sfzzct6uuPAk_b0NDMK8b8
PIXEL_CLEANUP = USER_APPROVED_CLEANUP_MASTER_PAIR_V1
RUNTIME_IMPORT = NOT_RUN
RUNTIME_READABILITY = NOT_RUN
```

## 4. Implementation reality

Current player-facing product remains graybox:

- `scripts/units/unit_view.gd`: circles/polygons/lines via `_draw()`, no product sprite texture.
- `scripts/battle/battlefield_view.gd`: procedural lane rectangles/lines/outpost circles, no world texture/minimap art.
- `scenes/ui/stage_hud.tscn`: Labels and Buttons, no OMENWARD HUD/image assets.

Therefore:

```text
PROJECT_PRODUCT_IMAGE_ASSETS_IMPLEMENTED = 0
PROJECT_PRODUCT_IMAGE_ASSETS_RUNTIME_VERIFIED = 0
APPROVED_VISUAL_REFERENCE_COUNT = 1
APPROVED_ACTUAL_GAME_ASSET_SOURCE_COUNT = 2
```

## 5. Existing Solution First disposition

| Need | Decision | Rule |
|---|---|---|
| approved Lumern Shield Guard | `REUSE_WITH_EDIT` | never redraw from zero unless revision is explicitly requested |
| Roulette unit tokens | `REUSE_WITH_EDIT` | crop approved actual unit art; token-only character art forbidden |
| Gold | `REUSE_AS_IS` once produced | one shared Gold asset for HUD/reward/Roulette |
| token frame | `REUSE_AS_IS` | shared across Roulette/Result/Storage/COMMIT |
| 12 manipulation arrows | `REUSE_AS_IS` | one arrow source rotated/flipped |
| building thumbnails | `REUSE_WITH_EDIT` | crop/reframe world building sprite |
| common panels/buttons | `ADAPT` | prefer Godot Theme/NinePatch/primitive; do not generate decorative raster by default |
| minimap background | `ADAPT` | runtime data + primitive route/progress; generate only marker atlas |
| selection/valid/invalid tint | `ADAPT` | shader/theme/outline before separate images |
| other-project/Base title-specific art | `REJECT` for direct pixel reuse | Base supplies process/reference, not OMENWARD identity pixels |

---

# 6. Remaining Image Goals

## P0 — Codex 시작 전 현재 플레이 가능한 핵심 범위에 필요한 자산

### IMG-01 — Shield Guard Faction Pair Runtime Set

#### 1. Player / Product Goal
전열 방어 병종과 Ally↔Veil 차이를 전략 줌에서 즉시 읽고, 같은 병종이 Roulette→COMMIT→Battle에서 동일한 시각 정체성을 유지한다.

#### 2. Actual Consumer
- Scene: `scenes/units/unit.tscn`
- Script: `scripts/units/unit_view.gd`
- Secondary: 3×3 token crop / Result / Storage / COMMIT.

#### 3. Existing References
- `ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1`: `REUSE_WITH_EDIT`, character identity source.
- `OM-IMG-023`: style/scale reference.
- Veil brief: shape/palette contract.

#### 4. Required Assets
- Lumern Shield Guard runtime state source/atlas: transparent; final atlas geometry TBD; approved idle reused.
- Veil Shield Guard idle V1: transparent; user-approved source.
- Veil Shield Guard runtime state source/atlas after the animation-production contract and cleanup/export.
- State family: `deploy / idle / move / attack_basic / skill_1 / hit_light / death / victory` only after the non-image Animation Production Contract locks exact frame/FPS and missing choreography.

#### 5. Must Preserve
Shield-first role; Lumern navy/ivory/cool-gray/restrained-gold; Veil carapace/rift language; 2.5–3-head tactical SD; same archetype/pivot logic.

#### 6. Must Not Introduce
Veil recolored human knight; spear/greatsword role drift; boss-scale weight; new skill mechanics.

#### 7. Quality Target
Transparent pixel-clean masters; readable around the current 34–40 px humanoid display exploration envelope; token crop remains readable at 32–34 px tile reference.

#### 8. Acceptance Criteria
Both factions read as Shield Guard without text; faction identity is shape-based, not color-only; no baked UI/background/shadow; same state arrangement can be implemented.

#### 9. Verification
`Generated → Reviewed → Approved → Notion Registered → Pixel Cleanup → Implementation Ready → Codex Import → Runtime 960/1280/1920 check`.

### IMG-02 — Greatsword + Spear Frontline Runtime Set

#### 1. Player / Product Goal
전열에서 `large sweeping damage`와 `long spear line` 역할을 즉시 구분한다.
#### 2. Actual Consumer
`unit.tscn` / `unit_view.gd`; token/result/storage/commit derivatives.
#### 3. Existing References
Shield pair style lock; current silhouette rules; OM-IMG-023.
#### 4. Required Assets
Lumern/Veil Greatsword + Lumern/Veil Spear = 4 faction-archetype runtime sources/atlases; transparent; state family follows the locked Animation Production Contract.
#### 5. Must Preserve
Greatsword = long heavy two-hand attack mass; Spear = longest forward line; faction grammar consistent.
#### 6. Must Not Introduce
Spear tip reversed; Veil as simple recolor; hero-scale ornamentation.
#### 7. Quality Target
Role readable before face/detail at tactical scale.
#### 8. Acceptance Criteria
Names hidden: Greatsword and Spear remain distinguishable in both factions; state layout compatible with runtime.
#### 9. Verification
Same lifecycle as IMG-01 plus cross-unit silhouette check.

### IMG-03 — Archer + Cavalry Runtime Set

#### 1. Player / Product Goal
원거리 화력과 기동/돌진 병종을 전선 혼전에서도 빠르게 구분한다.
#### 2. Actual Consumer
Battlefield unit renderer + derived token/commit surfaces.
#### 3. Existing References
Current silhouette/art guide + approved faction/style references.
#### 4. Required Assets
Lumern/Veil Archer + Lumern/Veil Cavalry = 4 runtime sources/atlases.
#### 5. Must Preserve
Archer bow/launcher silhouette; Cavalry mount + rider/Veil functional equivalent; role-first readability.
#### 6. Must Not Introduce
Archer melee-heavy silhouette; Cavalry giant/boss scale; new mount mechanics.
#### 7. Quality Target
Clear body/mount/weapon mass at current tactical zoom.
#### 8. Acceptance Criteria
Archer/Cavalry read correctly without label and both factions fit common state/pivot contract.
#### 9. Verification
Generated through runtime evidence lifecycle.

### IMG-04 — Priest + Mage Runtime Set

#### 1. Player / Product Goal
지원과 마법 피해 역할을 작은 전투 화면에서도 구별한다.
#### 2. Actual Consumer
Battlefield renderer + derived token/result/storage/commit.
#### 3. Existing References
Faction style, silhouette rules, current unit archetypes.
#### 4. Required Assets
Lumern/Veil Priest + Lumern/Veil Mage = 4 runtime sources/atlases.
#### 5. Must Preserve
Priest support relic/staff language; Mage catalyst/core language; limited ambient magic.
#### 6. Must Not Introduce
Constant bloom, giant spell effects baked into sprite, new spell mechanics.
#### 7. Quality Target
Weapon/catalyst silhouette survives tactical downscale.
#### 8. Acceptance Criteria
Support vs caster role distinguishable by silhouette; no VFX occlusion in base frames.
#### 9. Verification
Standard asset lifecycle + combat-scale pair check.

### IMG-05 — Assassin + Flier Runtime Set

#### 1. Player / Product Goal
침투와 공중 위협/아군 역할을 전선 상태에서 즉시 식별한다.
#### 2. Actual Consumer
Battlefield renderer; infiltration/air contextual surfaces use same identities.
#### 3. Existing References
Silhouette contract + faction visual language.
#### 4. Required Assets
Lumern/Veil Assassin + Lumern/Veil Flier = 4 runtime sources/atlases. Extra assassin bypass/flier flight states are `STATE_RECHECK`, not invented here.
#### 5. Must Preserve
Assassin narrow/dual-weapon read; Flier wingspan/height read.
#### 6. Must Not Introduce
Hidden-route revelation through art; boss-scale wings; new movement rules.
#### 7. Quality Target
Strong silhouette and direction read without excessive VFX.
#### 8. Acceptance Criteria
Assassin/Flier/faction each readable without color-only dependence; any extra states backed by current system contract.
#### 9. Verification
Standard lifecycle + infiltration/air readability test after implementation.

### IMG-06 — Giant Faction Pair Runtime Set

#### 1. Player / Product Goal
거인이 일반 유닛보다 명확히 큰 공성/중량 역할로 보이되 Boss와 혼동되지 않는다.
#### 2. Actual Consumer
Battlefield unit renderer; structure-attack feedback when actual state contract requires it.
#### 3. Existing References
Current Giant archetype; historical 72–96 px display envelope is exploration only.
#### 4. Required Assets
Lumern Giant + Veil Giant = 2 runtime sources/atlases; `structure_attack/heavy_stagger` only after current state-contract recheck.
#### 5. Must Preserve
Scale difference, heavy weapon/body, faction language.
#### 6. Must Not Introduce
Boss phase identity, new siege mechanics, unsupported extra states.
#### 7. Quality Target
Large but information-efficient silhouette that fits three-front simultaneous view.
#### 8. Acceptance Criteria
Giant ≠ normal humanoid ≠ Boss; collision/ground baseline can share runtime pivot conventions.
#### 9. Verification
Standard lifecycle + three-front crowding/readability check.

### IMG-07 — Roulette / Result / Storage / COMMIT Token Core

#### 1. Player / Product Goal
플레이어가 3×3 결과와 획득 병력을 같은 시각 언어로 추적한다.
#### 2. Actual Consumer
3×3 Roulette, Result Preview, Storage, COMMIT, HUD Gold.
#### 3. Existing References
Approved Token Component Spec; approved unit art is source of unit crops.
#### 4. Required Assets
1) derived unit Role-Anchor crops, 2) shared Gold texture, 3) X/non-reward rune, 4) common token frame, 5) token state overlay atlas. Token tile reference 32–34 px; source masters may be larger.
#### 5. Must Preserve
Actual unit continuity; T1/T2 token rules; reward rarity separate from token tier.
#### 6. Must Not Introduce
Gacha rarity frames, premium-currency styling, token-only character illustrations.
#### 7. Quality Target
All token roles readable at 32–34 px reference tile.
#### 8. Acceptance Criteria
Unit/Gold/X instantly distinct; overlays do not obscure role anchor; same unit recognized in Battle/Commit.
#### 9. Verification
3×3 full-view downscale + implemented token-state screenshots.

### IMG-08 — Five Omen Signature Icons

#### 1. Player / Product Goal
Forecast/Battle/Review에서 현재 위협 유형을 텍스트 없이 빠르게 구분한다.
#### 2. Actual Consumer
Forecast, BATTLE, REVIEW; FLYING/INFILTRATION/SIEGE may also appear in minimap context.
#### 3. Existing References
`MASS / ARMORED / FLYING / INFILTRATION / SIEGE` current pressure canon.
#### 4. Required Assets
5 transparent icons: MASS, ARMORED, FLYING, INFILTRATION, SIEGE. Master size TBD; must survive ~24–32 px HUD display exploration.
#### 5. Must Preserve
Pressure meanings; iconography consistent with fantasy ward/rift language.
#### 6. Must Not Introduce
New pressure type, text baked into icon, color-only distinction.
#### 7. Quality Target
Monochrome silhouette remains distinguishable.
#### 8. Acceptance Criteria
5-way blind-shape recognition is plausible at HUD size and no icon implies hidden route knowledge.
#### 9. Verification
Forecast/Battle/Review implementation screenshots at target resolutions.

### IMG-09 — HUD Resource + Minimap Utility Atlas

#### 1. Player / Product Goal
현재 마력/병력 한도와 전선 공간 문맥을 빠르게 읽는다.
#### 2. Actual Consumer
Top HUD + per-front minimap.
#### 3. Existing References
Current HUD contract; per-front minimap visual Decision; Gold reused from IMG-07.
#### 4. Required Assets
1) Mana icon, 2) Troop Capacity icon, 3) minimap marker atlas containing stronghold/clash/route/Boss/Siege. Minimap background is not a painted duplicate battlefield.
#### 5. Must Preserve
Minimap = context only; no unit-by-unit replication.
#### 6. Must Not Introduce
New resource, permanent unseen-route marker, duplicated battle VFX.
#### 7. Quality Target
Readable small glyphs with shape redundancy.
#### 8. Acceptance Criteria
Markers remain distinct at minimap size; Gold is not duplicated as a new asset.
#### 9. Verification
Three minimaps simultaneously readable at 960×540, 1280×720, 1920×1080.

### IMG-10 — 3×3 Omen Workbench Runtime Textures

#### 1. Player / Product Goal
3×3 결과와 행/열 조작 가능성을 슬롯머신이 아니라 지휘 장치로 이해한다.
#### 2. Actual Consumer
PREPARE Roulette Focus; system data from `scripts/roulette/roulette_service.gd`, UI surface currently graybox/planned.
#### 3. Existing References
3×3 component spec, Roulette DDD feedback spec, OM-IMG-023 lower-deck hierarchy.
#### 4. Required Assets
1) board/frame texture only if Theme/NinePatch is insufficient, 2) one manipulation arrow icon reused by rotate/flip, 3) Omen/reel/seal device texture family.
#### 5. Must Preserve
3×3; exactly 12 directional controls via reuse; central judging cue; battlefield remains primary.
#### 6. Must Not Introduce
Cherry/7/jackpot/lever/casino language, baked text, redundant resource HUD.
#### 7. Quality Target
Crisp tactical UI at 960×540 base composition.
#### 8. Acceptance Criteria
Arrow direction is unambiguous; generated textures are only those Theme/primitive cannot replace.
#### 9. Verification
PREPARE interaction screenshots + state transition readback after Codex.

### IMG-11 — Stage-1 Foundation Buildings A

#### 1. Player / Product Goal
기초 경제/병력/방어 시설을 Ward에서 즉시 구분하고 건설 선택과 세계 오브젝트를 연결한다.
#### 2. Actual Consumer
Ward/building world representation; Build thumbnail derived from world art; building system owner `scripts/buildings/building_service.gd`.
#### 3. Existing References
Current Building Tier authority; current visual style.
#### 4. Required Assets
Vault T1, Farm T1, General Barracks T1, Defense Tower T1 = 4 transparent/world-compatible sprites. Historical 100–128 px building display range is exploration only.
#### 5. Must Preserve
Facility roles and Ally shape/material language.
#### 6. Must Not Introduce
Obsolete A/B branches, new resources, text baked into buildings.
#### 7. Quality Target
Silhouette readable in Ward view; thumbnails can be cropped from same source.
#### 8. Acceptance Criteria
4 buildings distinguishable without labels; no duplicate thumbnail-only illustrations.
#### 9. Verification
World + build-selection screenshots after implementation.

### IMG-12 — Stage-1 Foundation Buildings B

#### 1. Player / Product Goal
지휘소와 마력탑을 경제/병영/방어 시설과 명확히 구분한다.
#### 2. Actual Consumer
Ward world + Build selection; Mana/research context.
#### 3. Existing References
Current Building Tier + Tactical Skills/Mana canon.
#### 4. Required Assets
Command Post T1 + Mana Tower T1 = 2 world sprites; Build crops derived.
#### 5. Must Preserve
Command Post = command/ward authority; Mana Tower = arcane research/mana, single linear family.
#### 6. Must Not Introduce
Mana Tower branching, new research currency, independent minigame.
#### 7. Quality Target
Distinct vertical silhouettes; magic presence restrained but obvious.
#### 8. Acceptance Criteria
Command vs mana function visually separable at Ward scale.
#### 9. Verification
Build/Ward screenshots and HUD linkage after implementation.

### IMG-13 — Three Front-State Environment Core

#### 1. Player / Product Goal
세 전선이 동일 세계에 속하면서도 현재 교전 위치/거점/경로를 읽을 수 있다.
#### 2. Actual Consumer
`battlefield_view.gd` replacement/augmentation for three Front-State views.
#### 3. Existing References
OM-IMG-023; current Front-State/minimap Decision.
#### 4. Required Assets
1) combat terrain tile/plate family, 2) allied Ward stronghold/defense-line asset, 3) Veil rift/front anchor, 4) outpost/route prop atlas. Exact tile geometry awaits implementation-layout envelope, but no full-screen baked battle screenshot.
#### 5. Must Preserve
Battlefield primary; Ward fantasy/magic; Ally↔Veil shape contrast; minimap handles long-distance context.
#### 6. Must Not Introduce
Old long-road whole-map composition as default, decorative clutter that hides units.
#### 7. Quality Target
Supports dense unit readability and restrained lighting.
#### 8. Acceptance Criteria
Units remain readable over terrain; stronghold/rift/outpost roles distinct; tiles/plates can assemble without obvious seams.
#### 9. Verification
Three simultaneous front screenshots at target resolutions.

## P1 — Vertical Slice / Demo 품질과 상태 완결성

### IMG-14 — Omen Warden Command Representation

#### 1. Player / Product Goal
플레이어가 직접 싸우는 영웅이 아니라 징조를 읽고 병력을 보내는 지휘관임을 시각적으로 이해한다.
#### 2. Actual Consumer
PREPARE / COMMIT / Ward command context; exact scene target will be named in Codex handoff.
#### 3. Existing References
OM-IMG-023 commander silhouette; current world-role Decision.
#### 4. Required Assets
One transparent command sprite/half-body master with long command flag; UI crop derived from same source, not separate character art.
#### 5. Must Preserve
Long flag, command coat/armor, high-ground/command posture.
#### 6. Must Not Introduce
Frontline melee protagonist, oversized persistent battle portrait, new named hero identity.
#### 7. Quality Target
Strong silhouette and same Ally material language.
#### 8. Acceptance Criteria
Role reads as commander without explanatory text; crop reuse works in PREPARE/COMMIT.
#### 9. Verification
Implemented command surfaces and battle non-occlusion check.

### IMG-15 — Combat Feedback VFX Core

#### 1. Player / Product Goal
배치, 피격, 공성 경고, 거점 피해/점령 사건을 전투 혼잡 속에서도 인지한다.
#### 2. Actual Consumer
Battlefield deploy/hit/siege/stronghold state transitions.
#### 3. Existing References
Combat readability + front-state/minimap Decision.
#### 4. Required Assets
Deploy/reinforcement, hit feedback, siege warning, stronghold damage/capture = up to 4 VFX sources/flipbooks **only where shader/primitive is insufficient**.
#### 5. Must Preserve
Event clarity > spectacle.
#### 6. Must Not Introduce
Persistent bloom, hidden game-state information, VFX that masks unit role.
#### 7. Quality Target
Short, readable, low visual-noise effects.
#### 8. Acceptance Criteria
Each event has a unique cue and no effect obscures combat state.
#### 9. Verification
Runtime event capture/screenshots; remove any raster VFX solved better by shader/primitive.

### IMG-16 — Roulette Feedback VFX Core

#### 1. Player / Product Goal
행/열 이동, 판정선 확정, 보상 획득의 인과를 즉시 이해한다.
#### 2. Actual Consumer
PREPARE 3×3 manipulation/result transition.
#### 3. Existing References
Roulette DDD feedback spec.
#### 4. Required Assets
Move snap, judging/line-lock, reward reveal = up to 3 VFX sources; shader/primitive first.
#### 5. Must Preserve
Agency-first tactical crescendo.
#### 6. Must Not Introduce
Jackpot/gacha celebration language, fake near-miss cues.
#### 7. Quality Target
Fast, controlled, token readability preserved.
#### 8. Acceptance Criteria
Player can distinguish manipulate→judge→reward without text-only dependence.
#### 9. Verification
Recorded PREPARE state sequence after implementation.

### IMG-17 — Building T2 Specialization Runtime Set

#### 1. Player / Product Goal
플레이어가 건물 업그레이드 선택의 역할 차이를 외형만으로도 추적한다.
#### 2. Actual Consumer
Ward world + specialization preview/build UI.
#### 3. Existing References
Current `OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1`; obsolete universal A/B branch doc is `SUPERSEDED`.
#### 4. Required Assets
- General Barracks T2: Shield/Greatsword/Spear/Archer/Cavalry = 5.
- Special Barracks T1 + T2 Mage/Priest/Assassin/Flier/Giant = 6.
- Defense Tower T2 Artillery/Defense-enhancement/Sniper = 3.
- Linear T2 Vault/Farm/Command Post/Mana Tower = 4.
This Goal is executed as 3–5-image subpackets, never one giant batch.
#### 5. Must Preserve
Only current branch structure; T3 identities remain unresolved where canon says pending.
#### 6. Must Not Introduce
Old `안정/행운 금고`, `전열/기동 병영`, universal A/B branches, unapproved T3 mechanics.
#### 7. Quality Target
Parent building lineage obvious; specialization role visible via silhouette/function props.
#### 8. Acceptance Criteria
All current T2 branches identifiable; obsolete branch imagery absent.
#### 9. Verification
Specialization UI + Ward world runtime screenshots after implementation.

### IMG-18 — Ten Tactical Skill Icons

#### 1. Player / Product Goal
전투 중 해금된 전술을 빠르게 식별하고 마력/대상/쿨다운 판단을 할 수 있다.
#### 2. Actual Consumer
Tactical skill panel / BATTLE quick access; current canon has 10 skills.
#### 3. Existing References
`OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1`.
#### 4. Required Assets
T1 4: 속박진/수호장/집중 명령/충격파; T2 3: 폭풍 억제/파쇄 명령/봉쇄 결계; T3 3: 결전의 깃발/성역/시간 왜곡. Produce as tier subpackets 4/3/3. Ready/selected/disabled/cooldown should normally be UI state overlays, not separate painted icons.
#### 5. Must Preserve
Skill role/target meaning; T1/T2/T3 hierarchy; Mana as cast resource.
#### 6. Must Not Introduce
New skill, auto-cast implication, hidden target discovery, text baked into icons.
#### 7. Quality Target
Each icon recognizable at tactical-panel size; coherent family with distinct silhouettes.
#### 8. Acceptance Criteria
10 icons are non-ambiguous at small size and state variants can be produced with UI effects rather than duplicate art.
#### 9. Verification
Implemented panel at target resolutions + disabled/cooldown state checks.

### IMG-19 — Unit Tier / Rank Visual Variant Gate

#### 1. Player / Product Goal
필요한 경우 Tier/Rank 차이를 전장에서 읽되 병종 역할 실루엣을 해치지 않는다.
#### 2. Actual Consumer
Battlefield / Result / Storage; Roulette Token allows T1/T2 actual art, T3 token is forbidden.
#### 3. Existing References
Tier/Rank data and Token Component Spec.
#### 4. Required Assets
`TBD_AFTER_DATA_CONTRACT_RECHECK`. Current faction visual profile does not yet expose a tier-specific sprite asset seam, so exact variant count is not responsibly fixed here.
#### 5. Must Preserve
Role silhouette > tier detail; rarity != token tier.
#### 6. Must Not Introduce
Rarity gacha frames, arbitrary T3 token art, unsupported data dimensions.
#### 7. Quality Target
Only generate variants that have a named runtime consumer/data mapping.
#### 8. Acceptance Criteria
A current data/visual contract exists before generation and exact count is traceable.
#### 9. Verification
`CANON_RECHECK → brief → generation → integration → runtime`.

## P2 — 콘텐츠 확장 단계, 현재 Codex 시작 Gate 비차단

### IMG-20 — Stage Boss Runtime Visuals

#### 1. Player / Product Goal
Stage 5/10/15/20 Boss가 일반/Elite보다 높은 위협과 고유 패턴 주체로 읽힌다.
#### 2. Actual Consumer
Boss battle stages and related telegraphs.
#### 3. Existing References
20-stage Boss arc; current Veil/fantasy style.
#### 4. Required Assets
Four actual Boss battle sprite/effect families after each Boss behavior/phase visual contract is rechecked.
#### 5. Must Preserve
Boss stages 5/10/15/20; pressure language and public telegraph rules.
#### 6. Must Not Introduce
New boss mechanics or names without canon.
#### 7. Quality Target
Boss-scale identity without obscuring front-state readability.
#### 8. Acceptance Criteria
Each Boss asset corresponds to an authored behavior/phase consumer.
#### 9. Verification
Boss-stage runtime capture and readability tests.

### IMG-21 — REVIEW.MAINTENANCE Merchant Visual

#### 1. Player / Product Goal
Stage 후처리에서 상인/보상/정비 상태를 전투 상태와 구분한다.
#### 2. Actual Consumer
`REVIEW.MAINTENANCE` merchant surface.
#### 3. Existing References
Current Text UX state transition / merchant canon.
#### 4. Required Assets
Actual merchant portrait/sprite only after current surface confirms it is shown; UI panels remain semantic.
#### 5. Must Preserve
Merchant as REVIEW substate, not fifth top-level mode.
#### 6. Must Not Introduce
New shop currency or gacha presentation.
#### 7. Quality Target
Readable NPC identity consistent with Ward fantasy.
#### 8. Acceptance Criteria
Concrete scene/UI consumer exists before generation.
#### 9. Verification
Merchant screen runtime evidence.

### IMG-22 — Bellu Player-Facing Guide Asset

#### 1. Player / Product Goal
FTUE에서 실제 가이드 캐릭터가 노출되는 경우 설명 주체를 일관되게 인식한다.
#### 2. Actual Consumer
Only a re-confirmed player-facing tutorial/guide surface.
#### 3. Existing References
Historical Bellu guide contract; current FTUE.
#### 4. Required Assets
Portrait/sprite only after current surface recheck.
#### 5. Must Preserve
Single-guide role if still current.
#### 6. Must Not Introduce
A second mascot/guide or tutorial system.
#### 7. Quality Target
UI-scale readable, non-intrusive.
#### 8. Acceptance Criteria
Current consumer is proven first; otherwise `DEFERRED_BY_DECISION`.
#### 9. Verification
FTUE runtime screenshot.

### IMG-23 — Additional Biome / Environment Sets

#### 1. Player / Product Goal
추가 Stage/MapRun 환경이 세계관을 확장하면서 전투 가독성을 유지한다.
#### 2. Actual Consumer
Future biome-specific Front-State environment surfaces.
#### 3. Existing References
IMG-13 environment grammar + Ward/Veil style.
#### 4. Required Assets
Only biome sets explicitly required by authored stage content; exact count TBD.
#### 5. Must Preserve
Unit contrast and front-state hierarchy.
#### 6. Must Not Introduce
Decorative biome art with no stage consumer.
#### 7. Quality Target
Same tile/material grammar across biomes.
#### 8. Acceptance Criteria
Each set maps to an authored stage/biome.
#### 9. Verification
Runtime stage screenshots.

### IMG-24 — T3 Buildings / Named High-Rank Unit Variants

#### 1. Player / Product Goal
후반 성장의 시각적 위계를 실제 gameplay state와 맞춘다.
#### 2. Actual Consumer
Late MapRun building/unit states when current canon/data supports them.
#### 3. Existing References
Current tier/rank rules.
#### 4. Required Assets
TBD; current Building authority explicitly leaves multiple T3 identities/effects unresolved.
#### 5. Must Preserve
Parent role and silhouette.
#### 6. Must Not Introduce
Premature T3 mechanics or unsupported named variants.
#### 7. Quality Target
Runtime-mapped variants only.
#### 8. Acceptance Criteria
Exact gameplay/data consumer exists before image brief.
#### 9. Verification
Late-stage runtime evidence.

## P3 — Release / Marketing, 현재 제작 금지

### IMG-25 — Title / Main Menu Product Art

#### 1. Player / Product Goal
게임 시작 전 OMENWARD의 command/ward/omen identity를 전달한다.
#### 2. Actual Consumer
Concrete title/main-menu scene only after that scene contract exists.
#### 3. Existing References
OM-IMG-023 and approved runtime assets as identity references.
#### 4. Required Assets
Logo/title art/background only when a real menu consumer is named.
#### 5. Must Preserve
Commander/ward/omen identity; no fake gameplay.
#### 6. Must Not Introduce
Unimplemented systems or misleading battle composition.
#### 7. Quality Target
Release-quality, localization-aware layers.
#### 8. Acceptance Criteria
Menu scene and aspect targets are current.
#### 9. Verification
Packaged build menu screenshot.

### IMG-26 — Steam / Distribution Marketing Set

#### 1. Player / Product Goal
Store visitor에게 실제 게임 정체성과 플레이를 정확히 전달한다.
#### 2. Actual Consumer
Steam/store capsule, screenshots, trailer thumbnail when release work begins.
#### 3. Existing References
Runtime-verified screenshots and approved title assets only.
#### 4. Required Assets
Exact set/size/count rechecked from platform official specs at release time.
#### 5. Must Preserve
Truthful gameplay representation and asset rights/provenance.
#### 6. Must Not Introduce
Fake UI/gameplay or stale platform sizes.
#### 7. Quality Target
Platform-current release quality.
#### 8. Acceptance Criteria
Official specs fresh-read; rights record complete; screenshots from actual runtime where required.
#### 9. Verification
Store submission evidence, not game runtime evidence.

---

# 7. Non-image prerequisites that block specific Image Goals

These are **production information**, not generated images.

1. `UNIT_ANIMATION_PRODUCTION_CONTRACT`: **COMPLETE** — `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md` locks the pair invariants and reserves exact frame/FPS/pivot/atlas geometry for the cleaned-pair addendum before mass atlas production.
2. `UNIT_TIER_VISUAL_DATA_CONTRACT`: exact tier/rank visual mapping before IMG-19.
3. `BUILDING_T3_CANON_RECHECK`: before IMG-24.
4. `BOSS_BEHAVIOR_VISUAL_RECHECK`: before IMG-20.
5. `BELLU_CURRENT_SURFACE_RECHECK`: before IMG-22.
6. `PLATFORM_SPEC_RECHECK`: before IMG-26.

Do not turn these information gaps into explanation-sheet image tasks.

# 8. Adversarial review A–F

### Loop A — Missing assets
Finding: prior tracker omitted the 10 player-facing tactical skill icons and did not separate late building specialization/tier gaps.
Correction: added IMG-18 and gated tier/building expansions.

### Loop B — Excess production
Finding: panel/button/minimap-background/placement-state art could be generated despite Theme/shader/primitive being better.
Correction: semantic UI/primitive first; generated image only where an actual raster asset is necessary.

### Loop C — Reuse
Finding: approved Lumern idle and actual unit→token continuity could be duplicated.
Correction: Lumern = `REUSE_WITH_EDIT`; token art derives from approved unit art; shared Gold/frame/arrow/build crops are reused.

### Loop D — Canon conflict
Finding: old six-building A/B branch document is explicitly superseded; current building authority has 7 base types and specific T2 structure.
Correction: only current Tier authority feeds IMG-17; T3 stays gated.

### Loop E — Godot feasibility
Finding: image atlases cannot be implementation-ready while exact frame/FPS/pivot/skill choreography is unresolved.
Correction: added non-image Animation Production Contract Gate before bulk unit atlas production.

### Loop F — Player experience
Finding: producing every possible visual variant before the core pair/style/interaction is proven would spend effort without improving current playability.
Correction: P0 queue locks Shield pair first, then core unit/roulette/HUD/building/environment assets; P2/P3 remain nonblocking.

```text
ADVERSARIAL_REVIEW = CLEAN_6_OF_6_AFTER_CORRECTIONS
IMAGE_GENERATION = NOT_RUN_FOR_THIS_AUDIT
PRODUCT_IMPLEMENTATION = NOT_RUN
RUNTIME_VERIFICATION = NOT_RUN
```

# 9. Final Image Goal Queue

| Order | Goal | Priority | Consumer | Existing usable source | New production | Precondition |
|---:|---|---|---|---|---|---|
| 1 | IMG-01 Shield Guard pair | P0 | Battlefield + token derivatives | Lumern + Veil idle APPROVED | pair state sets | cleanup/export; animation contract before mass states |
| 2 | IMG-02 Greatsword+Spear | P0 | Battlefield/token | style lock only | 4 unit families | IMG-01 + animation contract |
| 3 | IMG-03 Archer+Cavalry | P0 | Battlefield/token | style lock only | 4 unit families | IMG-01 + animation contract |
| 4 | IMG-04 Priest+Mage | P0 | Battlefield/token | style lock only | 4 unit families | IMG-01 + animation contract |
| 5 | IMG-05 Assassin+Flier | P0 | Battlefield/token | style lock only | 4 unit families | state recheck for extras |
| 6 | IMG-06 Giant pair | P0 | Battlefield | style lock only | 2 unit families | giant state recheck |
| 7 | IMG-07 Token core | P0 | Roulette/Result/Storage/COMMIT | unit art reuse | Gold/X/frame/overlay + crops | approved unit sources |
| 8 | IMG-08 Omen Signature icons | P0 | Forecast/Battle/Review | canon names | 5 icons | none |
| 9 | IMG-09 HUD/minimap utility | P0 | HUD/minimaps | Gold reused | 2 icons + marker atlas | minimap contract |
| 10 | IMG-10 Omen workbench | P0 | PREPARE | composition refs | up to 3 textures | semantic-UI delete test |
| 11 | IMG-11 Foundation Buildings A | P0 | Ward/Build | none | 4 sprites | current building authority |
| 12 | IMG-12 Foundation Buildings B | P0 | Ward/Build | none | 2 sprites | current building authority |
| 13 | IMG-13 Front environment | P0 | Battlefield | OM-IMG-023 reference | 4 environment families | front-state contract |
| 14 | IMG-14 Omen Warden | P1 | PREPARE/COMMIT/Ward | OM-IMG-023 identity | 1 master + derived crops | consumer scene confirmation |
| 15 | IMG-15 Combat VFX | P1 | Battlefield | none | up to 4 | shader/primitive delete test |
| 16 | IMG-16 Roulette VFX | P1 | PREPARE | DDD spec | up to 3 | shader/primitive delete test |
| 17 | IMG-17 Building T2 | P1 | Ward/specialization | T1 parents | 18 images in subpackets | current T2 authority |
| 18 | IMG-18 Tactical skill icons | P1 | Tactical panel | skill canon | 10 icons in 4/3/3 packs | none |
| 19 | IMG-19 Unit tier/rank variants | P1 | Battle/Result/Storage | unit base art | TBD | visual data contract |
| 20 | IMG-20 Boss visuals | P2 | Boss stages | faction/style | 4 behavior-linked families | boss visual recheck |
| 21 | IMG-21 Merchant | P2 | REVIEW.MAINTENANCE | world style | TBD | concrete merchant surface |
| 22 | IMG-22 Bellu guide | P2 | FTUE | historical contract | TBD | current guide surface recheck |
| 23 | IMG-23 Additional biomes | P2 | later stages | IMG-13 grammar | authored-set dependent | stage/biome mapping |
| 24 | IMG-24 T3/high-rank variants | P2 | late MapRun | parent art | TBD | current T3 canon/data |
| 25 | IMG-25 Title/menu art | P3 | title/menu | approved identity refs | TBD | concrete menu contract |
| 26 | IMG-26 Store marketing | P3 | Steam/distribution | runtime screenshots | platform-dependent | official spec recheck |

**Current next production gate after IMG-01 idle approval:**

```text
CURRENT_GATE = P0_REMAINDER_CANDIDATE_BATCH_REVIEW
NEXT_REQUIRED_ACTION = AWAIT_USER_BATCH_REVIEW_OF_P0_REMAINDER_CANDIDATES
NEXT_IMAGE_GENERATION = REQUIRES_ITS_OWN_EXPLICIT_USER_APPROVAL
```

The Veil idle was generated only after its separate explicit user approval and then user-approved. No future image is authorized by that approval.

# 10. Codex Integration Goal Queue

Codex does not create the art. It receives only approved/implementation-ready assets and current Notion/GitHub references.

```text
CODEX_EXECUTION_GATE = ALL_B_SCOPE_P0_AND_CURRENT_CONSUMER_P1_ASSETS_USER_APPROVED_CLEANED_EXPORTED_AND_IMPLEMENTATION_READY
```

## CODEX-IMG-01 — Unit Rendering Foundation + Shield Pair
### Start gate
Do not begin until `CODEX_EXECUTION_GATE` is satisfied. This B approval does not authorize Codex/Godot execution before that gate.

### Goal
Replace procedural unit graybox for the approved Shield pair and establish reusable sprite/animation import/mapping conventions.
### Inputs
Approved Shield assets; Notion approved pages; `unit.tscn`; `unit_view.gd`; faction visual profiles; animation contract.
### Scope
Import/filter/pivot/SpriteFrames or equivalent, Lumern/Veil mapping, shield pair states, token-crop source linkage, target-resolution checks.
### Non-Scope
Create/redesign art; alter stats or skills; other archetypes.
### Tasks
1 existing implementation audit; 2 reuse check; 3 import; 4 resource settings; 5 scene connection; 6 state connection; 7 animation events; 8 run; 9 960/1280/1920 verify; 10 screenshots/evidence; 11 regression fixes.
### Acceptance Criteria
Approved pixels appear in correct faction/archetype; no placeholder circle for Shield Guard; scale/pivot/filter correct; state transitions work; evidence exists; no gameplay regression.

## CODEX-IMG-02 — Remaining Base Unit Library
Integrate approved IMG-02~06 assets across 10 archetypes × 2 factions using the foundation from CODEX-IMG-01. Same acceptance plus complete mapping and missing-asset fail-closed behavior.

## CODEX-IMG-03 — Roulette / Result / Storage / COMMIT Visual Continuity
Integrate IMG-07 token crops/Gold/X/frame/overlays and guarantee the same unit identity flows from token to deployed unit.

## CODEX-IMG-04 — Omen / HUD / Per-Front Minimap Icons
Integrate IMG-08/09 into Forecast/Battle/Review/HUD/minimaps; implement marker context without unit-by-unit minimap replication.

## CODEX-IMG-05 — 3×3 Omen Workbench
Integrate IMG-10; one arrow texture rotated/flipped for 12 controls; preserve 3×3 and current state machine; use Theme/primitive for non-image UI.

## CODEX-IMG-06 — Foundation Buildings
Integrate IMG-11/12 world sprites and derived build thumbnails; preserve current building roles; no obsolete A/B branches.

## CODEX-IMG-07 — Front-State Environment
Integrate IMG-13 terrain/stronghold/rift/outposts into three simultaneous fronts; preserve unit readability and minimap context.

## CODEX-IMG-08 — Omen Warden Command Presence
Integrate IMG-14 only in approved command contexts; ensure BATTLE is not occluded or converted into hero-action presentation.

## CODEX-IMG-09 — VFX + Tactical Icons
Integrate IMG-15/16/18; state/target/cooldown feedback must work with real input; raster effects replaced by shader/primitive when superior.

## CODEX-IMG-10 — Building Specialization / Tier Variants
Integrate IMG-17 and later IMG-19/24 only after their data contracts are current and assets approved.

## CODEX-IMG-11 — Content Expansion Visuals
Integrate approved P2 assets into their exact stages/substates; cannot start from placeholder briefs.

## CODEX-IMG-12 — Release Visual Surfaces
Integrate title/menu assets where applicable; store marketing remains distribution work rather than Godot runtime unless the same asset is actually used in-game.

### Common Codex Integration acceptance

- approved asset hash/source can be traced;
- exact consumer Scene/UI/System is named;
- placeholder removed only where replacement is approved;
- nearest/filter/stretch/scale/pivot/crop correct;
- actual input/state transitions function;
- target resolution screenshots exist;
- tests/run evidence exists;
- runtime/human evidence is not inferred from static approval;
- unrelated PRs/workstreams are untouched.

# 11. Codex start gate under current user order

```text
CODEX_PRODUCT_IMAGE_INTEGRATION = BLOCKED_UNTIL_ALL_B_SCOPE_ASSETS_USER_APPROVED_CLEANED_EXPORTED_AND_IMPLEMENTATION_READY
CODEX_EXECUTION_GATE = ALL_B_SCOPE_P0_AND_CURRENT_CONSUMER_P1_ASSETS_USER_APPROVED_CLEANED_EXPORTED_AND_IMPLEMENTATION_READY
UNBLOCK_WHEN = ALL_B_SCOPE_P0_AND_CURRENT_CONSUMER_P1_ASSETS_USER_APPROVED_CLEANED_EXPORTED_AND_IMPLEMENTATION_READY
CURRENT_BLOCKING_PRIORITIES = P0 + P1 THAT_HAVE_CURRENT_CONSUMERS
P2_P3 = DEFERRED_NONBLOCKING_UNTIL_THEIR_PROJECT_STAGE
```

This interprets “make the actual-use images first, then Codex” without forcing future Boss/biome/store assets that do not yet have a current implementation surface to block the present playable-scope Codex handoff.
