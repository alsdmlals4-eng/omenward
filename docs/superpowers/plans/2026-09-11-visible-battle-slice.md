# Visible battle and construction implementation plan

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
