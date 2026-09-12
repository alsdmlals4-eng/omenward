# Visible battle and construction implementation plan

## Current completion loop: research -> specification -> connected implementation -> playtest

Latest execution evidence (supersedes the single-policy 79-check sample below): 81 model checks, UI/save/default scene PASS. Three actual-resource policies at seed1947 and 0.1-second steps: reinforcement/ranged/mixed all DEFEAT in round2; first refit allied0, enemy12/12/13, gold22/101/25, home HP1000; recovery spend0. No resource injection. These are reproducible policy diagnostics, not proof of optimal-play impossibility. Next investigate production, surviving enemy carryover and unimplemented acquisition decisions before tuning numbers. Independent five-perspective read-only review found no P0-P2 blocker; execution evidence remains separately owned by local test output and GPU capture. Recovery dialog first had overlapping direct children; fixed with one VBox content owner and visually rechecked.

Latest user correction: the loop is whole-game completion through comparable-game research, specification, integration and testing, not cosmetic-only iteration. Each unit starts with an implementation plan and covers model/data/UI/assets/save/tests as applicable. Do not stop merely because one screenshot improves; identify the next gameplay gap. Routine technical decisions are delegated; core user rules, protected Git and final art/Human boundaries remain.

Current gap map: (1) first-map preparation/combat/refit/result and viable initial choices, (2) roulette adjustment/commit/reserved capacity, (3) remaining troop abilities/T3/grades, (4) heroes, (5) five-map campaign/retention, (6) complete transparent art/motion, (7) front door/settings/release. Current UI-only next priority is superseded by connected first-map loop; opaque Ward art remains required, not discarded.

### Paid recovery integration

PLAN before code: connect existing Blueprint economics/recovery to refit decisions. ADAPT Thronefall economy-versus-defense preparation (https://store.steampowered.com/app/2239150/Thronefall/), The Last Spell rebuilding between attacks (https://store.steampowered.com/app/1105670/The_Last_Spell/), Commander Quest army composition (https://store.steampowered.com/app/2697930/Commander_Quest/). REJECT adopting kill-all night endings, hero turn control or new resources. Price is our existing Blueprint formula, not a copied game's price.

Spec: heal_cost reads replenishment price units[row12], missingHP/maxHP and economy.heal_coefficient; heal_unit accepts living allied injured units only during PREPARE/REFIT, charges once and restores maxHP. No resurrection/automatic healing/combat-command heal. UI previews each target cost and remaining gold; insufficient funds disables actions. No save-schema change. This creates the concrete choice of recovery versus construction/specialization using the same gold.

Implemented model and real frontline recovery dialog. RED missing transaction/entry -> GREEN 79model checks and UI/save/default gate. Tests include rounding, repeated request, enemy/dead/absent target, affordability, combat rejection, two buttons targeting separate units and save readback. GPU revealed overlapping dialog children: replaced separate auto-fitted children with a vertical content container, re-rendered successfully. Capture output/front-recovery.png is a labeled UI boundary fixture, not proof that the mixed army survived a full round.

Real-resource first-map policy (no HP/gold injections): one general barracks per preparation until two, then archer specialization, free spin, affordable healing, deploy reserves and advance. Result DEFEAT round2, refits1, recovery_spend0. This is a reproducible weak-policy observation, NOT evidence all strategies fail or healing is balanced. Next loop compares multiple initial spend/production policies and identifies missing role/queue rules before tuning numbers. Do not silently tune the blueprint to make one scripted policy win.

## Mixed-role follow-up: plan, implementation, evidence

User approved continuing the mixed-role readability loop. PLAN: reproduce shields/archers/mages/priests/spears on both sides, add bounded read-only hover inspection instead of increasing physical spacing or shrinking art, verify unchanged model and two resolutions. Existing Control tooltip is reused (https://docs.godotengine.org/en/stable/classes/class_control.html#class-control-private-method-get-tooltip); no third-party component or art replacement.

RED missing inspection → GREEN actual faction/role/current-max HP, outside-field blank, dead exclusion, snapshot preservation, maximum6 rows plus overflow. Model68/UI-save/default PASS, scope5 PASS. Natural scenario19damage/16units/shield3poses unchanged. Separate TEST-ONLY mixed fixture spawns5roles per side then runs0.6s actual combat:10units/10damage. Not ordinary acquisition, encounter balance, whole campaign or Human evidence.

GPU720/1080 captures are output/front-mixed.png and front-mixed-1080.png. Added actual InputEventMouseMotion through viewport and waited0.8s;720 capture shows native tooltip with live Ward names/HP. Independent five-pass reviewer found no blocking code issue; hover runtime capture was added after that review and inspected by main agent. Remaining: Ward non-shield cards are opaque (visible white rectangles), some Veil edges remain, mixed units overlap, hover-only is not keyboard/touch accessibility. Next plan prioritizes Ward transparent combat consumers; do not label mixed art complete. Model/save/approved art untouched.

## 2026-09-13 approved bounded combat-readability plan and readback

User approved the preceding plan: reproduce crowding, compare shrink/stagger/status approaches, keep combat rules, verify two resolutions. PLAN was presented before BUILD. REUSE existing atlas/draw consumer; ADAPT stable four-depth stagger (0/24px rear offset); REJECT global shrinking and physical collision changes because those alter readability or combat tuning beyond this unit. Godot custom drawing order supports the final status overlay: https://docs.godotengine.org/en/stable/tutorials/2d/custom_drawing_in_2d.html . Existing Into the Breach threat-readability research remains context, not a claim that this layout replicates that game.

- [x] RED: screen test rejects missing bounded projection.
- [x] BUILD: front_screen.gd owns display-only unit_draw_anchor; depth-sort a copied array, preserve all model coordinates, draw health status after sprites, remove repeated attack text/placeholder unit frames.
- [x] VERIFY: eight co-located consecutive IDs have distinct bounded anchors; projection does not mutate snapshot; 230 simulation steps match control snapshot; existing 68 model checks/UI-save/default gate pass.
- [x] GPU: real natural battle remains19damage/16units and shield3/3poses. 1280x720 and1920x1080 inspected. Extra capture path exact-scoped. No new art generated.
- [x] REVIEW: independent five-pass scope/rules/state/visual/tests review found no blocker. Residual sprite/bar overlap remains; eight-ID pattern repeats. Not collision-free or Human PASS. Current capture is predominantly shields/Veil; full mixed-role visual stress remains pending.

Base remote still d830c0f6; pinned v9.4.3 unchanged, raw protected-path FAIL/scoped BUILD PASS. Parent PR/main remain unmerged. Next plan: mixed-role crowding stress and role/status readability before first-map end-to-end completion. Rollback this display/test change; save schema and simulation need no migration.

## 2026-09-12 continuous improvement: forecast and supply observability

Outcome: RED missing-query/UI checks preceded implementation; GREEN model 68/68, actual UI/save/default-scene gate, 109 selected existing contract tests and 12 scoped/alpha/motion tests. GPU 1280×720 capture: 19 damage events /16 units, shield windup/impact/recovery 3/3. Five-scope independent review found paused/terminal production wording; corrected and tested, including paused+locked substring regression. `git diff --check` clean. Base raw FAIL is the same eight approved runtime paths; project scoped BUILD PASS, not Base raw PASS. Full 559-test suite not rerun in this iteration; the historical `_base_recovery` fixture problem remains unverified. Human/device/accessibility/1920×1080/full-product NOT_RUN. Exact remote CI is checked after commit, not inferred from these local results.

Next continuous unit: reproduce overlapping active soldiers at normal display size and improve combat readability without changing combat rules; then complete missing motion and blueprint/runtime gaps in bounded, researched units. No repeat approval for routine implementation; final art/core semantic decisions and protected integration remain distinct. This is not whole-game completion.

Direction: keep the approved single-front / three-tab / time-limited-round loop; let players read actual incoming pressure and why a selected facility is not supplying units. Approval: latest user requested fresh Base read, benchmarking and implementation/improvement without routine reapproval. This is existing UI/production scope, not approval for unrelated PR absorption, release or core-rule replacement.

Freshness: project implementation source47726ad79e0c49fffbee9b8b9ff2778d44137723; current-task PR259 remains stacked/draft, main and other PRs read-only. Base remote main d830c0f6 was fetched and its AGENTS, intake and continuous-work owners read. Its receipt/HiGodot/2-round-review policies are DRIFT_REFERENCE_ONLY; project v9.4.3 lock, scoped validator and explicit five-pass review are retained. No migration of adapter/generated contracts. Root planning checkout and historical three-front owners are COMPATIBILITY/history; this worktree's current context and actual preview consumer own implementation status. No age-based deletion.

Work modes: PLAN benchmark/alternatives → BUILD existing FrontRun/FrontScreen queries and labels → REVIEW tests/render/readback. Project UX skill supplies the hypothesis: can players identify the next threat and explain why production is paused? Human task/think-aloud remains NOT_RUN; tests establish only correct displayed information.

benchmark_preflight_state: PASS for this bounded UI improvement. Existing 12-game research and current actual consumer were compared before selecting new work. No reusable external system is needed: REUSE FrontRun clocks/catalog and Godot controls, ADAPT presentation. No cross-project code absorption or new plugin/framework.

| Source and evidence (read2026-09-12) | Observed pattern | Project fit / disposition |
|---|---|---|
| https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf, pp13–17 text | Telegraphed attacks shape threat/response decisions | ADAPT actual upcoming wave preview; REJECT replacing real-time combat with fully deterministic grid turns. PDF text inspected, not full talk watched. Official homepage timeout was not substituted for body evidence. |
| https://store.steampowered.com/app/2239150/Thronefall/ About | Build by day, defend by night; economy/defense trade-off | ADAPT clear preparation/production freeze feedback; REJECT kill-all night ending because user requires timed rounds. |
| https://store.steampowered.com/app/2697930/Commander_Quest/ About | Deck/army synergy and covering weaknesses | ADAPT implemented role labels and troop capacity information; no claim to reproduce its proprietary systems. |
| https://store.steampowered.com/app/4906570/Slotbound_Demo/ About | 3×3 summons feed an autobattler; absorption/evolution | REFERENCE_ONLY for summon-to-army readability; REJECT jackpot rescue/absorption as automatic additions. Demo marketing is not measured balance evidence. |
| https://docs.godotengine.org/en/stable/classes/class_progressbar.html | Native percentage control and shared Range/Control behavior | ADOPT native progress bar bound to actual production clock, no bitmap progress decoration. |
| https://www.aseprite.org/docs/frame-duration/ | Frame properties define duration | RETAIN shield native timing checks; static pose reuse is not newly drawn motion. |

Three alternatives: (A) modal next-wave popup, clear but interrupts viewing/input; (B) permanent full army dashboard, rich but crowds1280×720; (C) compact shared two-line forecast plus selected-facility status. ADOPT C for lowest display cost, same game rules, easy removal, and no new save schema. Risk: incorrect future prediction; mitigation: read-only model query and equality test against actual spawned role counts. Risk: masking battlefield; mitigate upper strip outside soldier path. No game assets copied from references.

Acceptance: preview first/next/refit waves and none after victory; queries do not mutate RNG/snapshot; production distinguishes producing/frozen/full/locked/empty; UI reads model each frame without recreating panels every clock tick; locked selected facility cannot appear upgradeable; save/production/combat regressions and native motion remain valid. Existing numeric data is unchanged. Blueprint's more elaborate per-wave variation remains unimplemented; preview intentionally tells the truth about current runtime, not a fictional future implementation.

Learning: reuse existing catalog/clock owner for UI and verify against spawn behavior, rather than a second authored forecast table. Project-only lesson retained here; no Base promotion claimed. Rollback: revert this UI/query commit without touching saves, art, Base locks or other PRs.

**Goal:** 사용자가 병영 건설 → 생산 → 출전 → 단일 전선 전투를 직접 확인한다.
**Authority:** 2026-09-11 최신 사용자 ‘인게임에서 전투하는 거, 병종건설도 볼 수 있게. 이미지 연결’. 기존 기획-only 상태를 이 구간에 한해 supersede한다.
**Spec:** `docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json` 및 사람용 Blueprint v3.
**Architecture:** 기존 3전선 빌드는 보존한다. 별도 `scripts/replan/` 모델과 화면, `scenes/replan/front_slice.tscn`을 추가한다. 검토 JSON을 직접 읽어 병종/가격을 중복 정의하지 않는다. 카드형 후보 이미지를 검토용 실행 장면에서만 사용한다.
**Scope:** 수호 성채 1맵, 60초 라운드, 3웨이브, 재정비, 기본 자동전투, 병영 두 계열/T2 전문화, 생산/출전, 저장. 10라운드 생존/본진 점령 조건. 테스트는 2라운드 경계를 집중 검증한다.
**Excluded:** 영웅, T3/숙련/정예 능력, 전 캠페인, 최종 아트 승인, 출시. 기본형 공격/범위/치료 이외 병종 특수 능력은 미구현 표시.

## Tasks and acceptance

- [ ] `tests/replan_slice_test.gd`: 실 모델의 건설 비용, 계열 경계, 생산, 전투 피해, 라운드 동결, 저장 동일성, 슬롯 잠금 RED → GREEN.
- [ ] `scripts/replan/front_run.gd`: `construct(id)`, `upgrade(slot,id)`, `deploy(id)`, `begin_round()`, `advance(delta)`, `snapshot()`, `restore(data)` 구현. 준비 중 경제/전투 동결, 잘못된 입력은 비용 차감 없이 실패.
- [ ] `scripts/replan/front_screen.gd`, `front_art.gd`, `scenes/replan/front_slice.tscn`: 상단 1줄 지도, 중앙 전투, 하단 내정/징조륜/전선. 이미지 아틀라스는 원본 중복 없이 region으로 소비. 불투명 카드임을 명시.
- [ ] 실제 버튼 경로/전투 화면 캡처와 headless 테스트. 기존 기본 장면 진입은 유지하고 새 장면 직접 실행.
- [ ] Decisions/Active Context/Roadmap에 실행 경로와 증거 한계를 함께 갱신. 기존 v3 PDF는 구현 전 검토판으로 유지.

## Learning map

Blueprint JSON → FrontRun (비용/계열/생산/전투 판정) → FrontScreen (입력/표시)
Candidate atlas → FrontArt (region cache) → 병종 카드 / 내정 카드 / 전장 토큰
FrontRun snapshot → user://replan-front-v1.json → validation → restore

## Sources / choices

- ADOPT Godot AtlasTexture region/filter_clip: https://docs.godotengine.org/en/stable/classes/class_atlastexture.html
- ADAPT Godot saving games: versioned all-or-nothing local snapshot; no arbitrary resource path loading. https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html
- REJECT replacing old three-front services in-place: unrelated open PR overlap and rollback risk.

## Rollback and evidence ceiling

Launch the unchanged `scenes/main/main.tscn` for legacy build. No old saves overwritten. New art remains GENERATED_CANDIDATE; Aseprite NOT_USED for these static atlas sources. A test PASS is not animation/Human/balance approval.

## Actual result / implementation learning map

**PARTIAL / INTEGRATION_BLOCKED**. This worktree now starts at the new preview (1280×720); original scene remains available. The new application name isolates preview saves from the old build. Current source is the three `scripts/replan/` files and the shared Blueprint JSON; the review PDF remains the pre-implementation edition.

| Input / owner | Processing | Visible output / verification |
|---|---|---|
| Build button, Blueprint building_tree | FrontRun.construct/upgrade checks phase, cost, family and slots | List portrait and supply role; model and UI tests |
| Combat time | FrontRun.advance fixed substeps, waves, production, nearest target damage/healing | Single battle area, HP bars, reserve; GPU capture |
| Candidate source PNG | FrontArt caches AtlasTexture region, no new pixel copies | Building cards / allied and Veil tokens; candidates only |
| Save button | JSON snapshot, temporary write then rename; restore validates before mutation | Same economy/units/production; isolated test save round-trip |

### Verification performed

- RED: missing model. GREEN: 39 behavioral checks covering construction, tier/family rejection, affordability, production, damage, refit, capture slots, disk-format restoration and malformed saves.
- UI RED: atlas image escaped allocation at 443×443. GREEN: texture sizing order corrected, real build button/price and file save/load paths pass.
- Default scene headless smoke and live Godot 4.7.1 editor launch. Actual build / roulette / start / pause buttons were exercised with the editor scoped to this worktree. Other projects were not mutated.
- Reproducible GPU capture: `tests/replan_capture.gd`; 23 simulated seconds, 19 damage events, 16 active units. Output `output/front-building.png` and `output/front-battle.png`; no compositing or edited screenshot.
- Local gate: `tools/validate_replan_slice.ps1 -Godot <console executable>`. It fails immediately on a failed test. Remote workflow consumption is not yet established.
- Pinned operating validator: **FAIL** because protected runtime paths changed. New user BUILD authorization is recorded, but the old planning-only policy still prohibits these paths. No policy removal, version-lock replacement or bypass performed.
- Parent planning PR exact head 42498548: fresh read found canon-v45/contract/validate-contract-binding failures. No main merge claimed.

### Five full-scope review passes / corrections

1. Authority + code/data/UI/art/tests: preserve old build, scope new run, reject cross-family upgrades; candidate images not final sprites.
2. Authority + code/data/UI/art/tests: corrupt save checks found negative gold/faction/NaN/facility mismatch acceptance; validate before mutation.
3. Authority + code/data/UI/art/tests: real JSON converts numbers to float; normalize occupation owners to integers to preserve unlocked slots. Round-1 refit now unlocks next-round T2.
4. Authority + code/data/UI/art/tests: GPU/UI inspection found oversized images and stale capacity label; fixed layout and refresh key. Remaining token overlap and static art are not cleared.
5. Authority + code/data/UI/art/tests + Git: rerun gates, retain protected-path failure, parent CI failures and unimplemented requirements. No full-completion claim; worktree remains active for correction.

### Material claims / remaining work

- Visible construction and damage simulation: MACHINE + RENDER evidence, not player approval.
- Image connection: candidate card/atlas consumption only. No Aseprite in these seven source sheets. The historical Aseprite slash pilot is not connected.
- NOT IMPLEMENTED: transparent battle sprites, slash frames, true tower artwork, full body movement/attack, full roulette manipulation/bonus, T3/rank/hero skills, specialized assassin/flying/cavalry effects, five-map campaign.
- Balance, accessibility (full), performance profiling, release rights/compliance, Human: NOT_RUN. Dense tokens overlap; this is not acceptable as final combat art.
- Operating contract and parent PR reconciliation must happen before normal main integration. Automated tests do not override this boundary.

### Use

Open this worktree's `project.godot`, press F5. Build a general barracks in 내정; use the free 징조륜; deploy reserve cards in 전선; start the assault. Production queues more units during combat. At refit, select the barracks to specialize. Save/load keeps this preview run only.
