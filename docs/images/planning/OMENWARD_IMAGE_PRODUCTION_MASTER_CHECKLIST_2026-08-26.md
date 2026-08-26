# OMENWARD · Runtime Consumer Image Asset Master Checklist

```yaml
tracker_id: OMW-VIS-TRACKER-20260826-MASTER-01
policy_id: OMW-VIS-POLICY-20260826-RUNTIME-CONSUMER-ASSET-FIRST-01
status: USER_APPROVED_CURRENT
approved_at: 2026-08-26
approval_basis: USER_DIRECT_INSTRUCTION
scope: PLANNING_AND_GAME_CONSUMED_IMAGE_ASSET_TRACKING
current_user_work_mode: PLANNING_PLUS_IMAGE_ONLY
product_code_mutation: NONE
godot_execution: NOT_IN_SCOPE
codex_execution: NOT_IN_SCOPE
image_generation: NOT_STARTED
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
current_reference_asset: OM-IMG-023
current_asset_brief: OMW-ASSET-BRIEF-20260826-LUMERN-SHIELD-GUARD-01
```

## 1. 사용자 승인 제작 원칙

OMENWARD의 이미지 제작 백로그에는 **실제 게임 소비처가 있는 이미지 자산만** 넣는다.

```text
NO_RUNTIME_CONSUMER = NO_IMAGE_PRODUCTION_TASK
EXPLANATION_SHEET = PLANNING_REFERENCE_ONLY
FULL_SCREEN_MOCKUP = PLANNING_REFERENCE_ONLY
COMPARISON_BOARD = PLANNING_REFERENCE_ONLY
RUNTIME_TEXTURE_OR_SPRITE_OR_ICON_OR_VFX = IMAGE_PRODUCTION_CANDIDATE
```

이미지 한 건을 제작 목록에 넣으려면 최소 하나의 실제 소비처를 말할 수 있어야 한다.

허용 소비 형태 예:

```text
Sprite2D / AnimatedSprite2D
TextureRect / NinePatchRect
Button / TextureButton icon
Roulette token texture
HUD / Forecast / Review icon
Minimap marker
Character portrait actually shown by the game
Battlefield / building / environment texture
VFX sprite sheet / flipbook / effect texture
```

기획자가 보기 위한 전체 화면 시안, 규칙 설명 시트, 실루엣 비교판, faction 비교 보드 자체는 이 목록에서 생성하지 않는다.

## 2. 관리 방식 대안 검토

### A · Runtime-consumer asset first — USER APPROVED

각 자산에 `실제 소비처`, `재사용 관계`, `선행 정본`을 붙인다. 게임에서 직접 쓰지 않는 이미지는 생성하지 않는다.

장점:
- 생성 결과가 바로 제품 자산 후보가 된다.
- 설명용 산출물에 이미지 제작 비용을 쓰지 않는다.
- 같은 unit art를 Battlefield → Token → Storage → COMMIT에서 재사용할 수 있다.

### B · Explanation-sheet first — REJECTED

전체 화면 mockup, component sheet, silhouette board를 먼저 이미지로 제작한다.

거부 이유:
- 게임이 직접 소비하지 않는 파일이 쌓인다.
- 실제 sprite/icon 제작과 별개의 시각 계보가 생긴다.
- 승인된 설명 이미지가 구현 자산인 것처럼 오인될 수 있다.

### C · Runtime asset + explanation sheet 한 목록 혼합 — REJECTED FOR PRODUCTION TRACKER

기획용 이미지와 실제 제품 자산을 같은 상태표에서 관리한다.

거부 이유:
- `APPROVED`가 디자인 승인인지 게임 자산 승인인지 모호해진다.
- 우선순위와 완료 정의가 서로 다르다.

기획용 composition 문서는 보존하되 production tracker 밖에서 reference로만 사용한다.

## 3. 현재 Visual LOCK

모든 실제 게임 자산은 다음을 따른다.

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
VEIL_SHAPES = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
ROLE_SILHOUETTE_FIRST = TRUE
CASINO_SLOT_MACHINE_LANGUAGE = FORBIDDEN
```

`OM-IMG-023`은 **방향 reference**다. 그 자체를 게임 화면 background로 사용하거나 재생성 대상으로 보지 않는다.

## 4. 생산 목록에서 제외되는 기존 Visual 항목

다음 ID는 gameplay/UI composition 검증용 계보로 보존하지만 **이미지 생성 production queue에서는 제외**한다.

| ID | 과거 의미 | 현재 처리 |
|---|---|---|
| `OMW-VIS-001` | PREPARE 전체 화면 시안 | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-002` | COMMIT 전체 화면 시안 | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-003` | BATTLE 전체 화면 시안 | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-004` | REVIEW 전체 화면 시안 | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-005` | Battlefield clean plate 설명 시안 | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-006` | Triple Omen Wheels 설명 close-up | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-009` | Building silhouette board | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-010` | Troop silhouette lineup | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-011` | Ally vs Veil comparison board | `PLANNING_REFERENCE_ONLY` |
| `OMW-VIS-012` | FTUE cue sheet | `PLANNING_REFERENCE_ONLY` |

`OMW-VIS-007` Omen Signature와 `OMW-VIS-008` Mobilization Seal은 **설명 시트 자체는 만들지 않지만**, 그 안에서 필요했던 실제 runtime icon/seal 자산은 아래 소비처 기반 목록으로 재정의한다.

---

# 5. P0 · 실제 게임 핵심 소비 자산

## 5.1 전투 유닛 Sprite Sheet · 현재 데이터가 증명하는 20 visual slots

현재 bootstrap data는 10 archetype과 `lumern / veil` 두 visual faction을 갖는다. 따라서 현재 증명 가능한 기본 전투 visual slot은 **10 × 2 = 20개**다.

각 archetype의 현재 animation contract 상태명:

```text
deploy
idle
move
attack_basic
skill_1
hit_light
death
victory
```

정확한 프레임 수, FPS, sheet geometry는 지금 승인하지 않는다.

### 최초 스타일 잠금 Pair

| 순서 | Tracker Key | 실제 자산 | Primary consumer | Secondary consumer | 상태 |
|---:|---|---|---|---|---|
| 1 | `ASSET-UNIT-LUMERN-SHIELD-GUARD` | Lumern Shield Guard sprite sheet | Battlefield UnitView | Roulette token crop / Storage / COMMIT | `BRIEF_READY` · `OMW-ASSET-BRIEF-20260826-LUMERN-SHIELD-GUARD-01` |
| 2 | `ASSET-UNIT-VEIL-SHIELD-GUARD` | Veil Shield Guard sprite sheet | Battlefield UnitView | enemy preview / battle read | `NEXT_AFTER_1_USER_APPROVAL` |

현재 첫 생성 Gate:

```text
ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
→ one isolated runtime-oriented idle sprite
→ user APPROVE / REVISE / REJECT
→ only then Veil pair or additional animation states
```

두 자산으로 **아군/Veil shape language + 2.5~3등신 + 역할 실루엣 + pixel density**를 먼저 잠근다.

### 같은 문법으로 후속 제작할 unit assets

- [ ] `ASSET-UNIT-LUMERN-GREATSWORD`
- [ ] `ASSET-UNIT-VEIL-GREATSWORD`
- [ ] `ASSET-UNIT-LUMERN-SPEAR`
- [ ] `ASSET-UNIT-VEIL-SPEAR`
- [ ] `ASSET-UNIT-LUMERN-ARCHER`
- [ ] `ASSET-UNIT-VEIL-ARCHER`
- [ ] `ASSET-UNIT-LUMERN-CAVALRY`
- [ ] `ASSET-UNIT-VEIL-CAVALRY`
- [ ] `ASSET-UNIT-LUMERN-PRIEST`
- [ ] `ASSET-UNIT-VEIL-PRIEST`
- [ ] `ASSET-UNIT-LUMERN-MAGE`
- [ ] `ASSET-UNIT-VEIL-MAGE`
- [ ] `ASSET-UNIT-LUMERN-ASSASSIN`
- [ ] `ASSET-UNIT-VEIL-ASSASSIN`
- [ ] `ASSET-UNIT-LUMERN-FLIER`
- [ ] `ASSET-UNIT-VEIL-FLIER`
- [ ] `ASSET-UNIT-LUMERN-GIANT`
- [ ] `ASSET-UNIT-VEIL-GIANT`

상태: `WAITING_FIRST_PAIR_STYLE_LOCK`.

### Unit production 완료 정의

- [ ] 실제 Battlefield unit용 full sprite/animation source
- [ ] role silhouette가 작은 전략 줌에서도 읽힘
- [ ] Ally/Veil이 단순 색변경이 아님
- [ ] 승인된 unit art에서 Roulette token crop을 만들 수 있음
- [ ] 별도 token-only 캐릭터를 새로 그리지 않음
- [ ] `OM-IMG-023`의 SD/Fantasy/Magic 방향과 일치

---

## 5.2 Roulette / Storage / COMMIT 실제 Texture 자산

병종 Token은 **실제 unit art 재사용**이 current contract다. 그러므로 병종별 token-only character illustration은 만들지 않는다.

| Tracker Key | 실제 자산 | 소비처 | 제작 방식 | 상태 |
|---|---|---|---|---|
| `ASSET-TOKEN-UNIT-CROPS` | T1/T2 unit Role-Anchor crops | 3×3 Roulette / Result / Storage / COMMIT | approved unit art에서 파생 | `DERIVED_NOT_NEW_CHARACTER_ART` |
| `ASSET-TOKEN-GOLD` | Gold icon/coin texture | HUD / reward / Gold Roulette token | 하나의 shared Gold asset | `NEEDS_BRIEF` |
| `ASSET-TOKEN-X` | empty X / non-reward rune | Roulette 3×3 | 전용 small texture | `NEEDS_BRIEF` |
| `ASSET-TOKEN-FRAME` | common token frame | Roulette / Result / Storage / COMMIT | NinePatch/atlas 후보 | `NEEDS_BRIEF` |
| `ASSET-TOKEN-STATE-OVERLAY` | focus / preview / judging / completed-line overlay | Roulette 3×3 | frame/underlay 기반 | `NEEDS_BRIEF` |

금지:
- rarity마다 별도 gacha frame 생성
- unit token 전용 캐릭터 일러스트
- Gold를 premium currency처럼 제작

---

## 5.3 Omen / HUD / Minimap 실제 Icon 자산

| Tracker Key | 실제 자산 | 실제 소비처 | 상태 |
|---|---|---|---|
| `ASSET-OMEN-MASS` | MASS Signature icon | Forecast / BATTLE / REVIEW | `NEEDS_BRIEF` |
| `ASSET-OMEN-ARMORED` | ARMORED Signature icon | Forecast / BATTLE / REVIEW | `NEEDS_BRIEF` |
| `ASSET-OMEN-FLYING` | FLYING Signature icon | Forecast / BATTLE / REVIEW / minimap context | `NEEDS_BRIEF` |
| `ASSET-OMEN-INFILTRATION` | INFILTRATION Signature icon | Forecast / BATTLE / REVIEW / minimap context | `NEEDS_BRIEF` |
| `ASSET-OMEN-SIEGE` | SIEGE Signature icon | Forecast / BATTLE / REVIEW / minimap context | `NEEDS_BRIEF` |
| `ASSET-HUD-MANA` | Mana icon | top HUD / Tactical cost context | `NEEDS_BRIEF` |
| `ASSET-HUD-TROOP-CAPACITY` | troop capacity icon | top HUD | `NEEDS_BRIEF` |
| `ASSET-MINIMAP-MARKERS` | stronghold / clash / route / Boss / Siege marker atlas | per-front minimap | `NEEDS_BRIEF` |

Gold는 `ASSET-TOKEN-GOLD`를 HUD에서도 재사용한다.

색만으로 상태를 구분하지 않는다.

---

## 5.4 3×3 Omen Workbench 실제 UI Texture

전체 PREPARE 화면을 한 장으로 만들지 않는다. 실제 UI가 소비할 부분만 제작한다.

| Tracker Key | 실제 자산 | 소비처 | 상태 |
|---|---|---|---|
| `ASSET-ROULETTE-BOARD-FRAME` | 3×3 exposure board/frame | Roulette Focus | `NEEDS_BRIEF` |
| `ASSET-ROULETTE-ARROW` | direct manipulation arrow icon | row/column controls; rotation reuse | `NEEDS_BRIEF` |
| `ASSET-OMEN-DEVICE` | Omen/reel/seal command-device textures | PREPARE Roulette Focus | `NEEDS_BRIEF` |

가능하면 한 arrow texture를 회전/flip하여 12개 control에서 재사용한다. UI text는 이미지에 bake하지 않는다.

단순 Panel/Button으로 충분한 영역은 **이미지를 억지로 만들지 않고 Godot Theme/primitive 후보로 남긴다**.

---

## 5.5 실제 건물 Sprite · 현재 FTUE에서 직접 확인되는 6 base families

현행 Text UX Stage 1은 다음 여섯 시설을 실제 플레이어 건설 대상으로 명시한다.

- [ ] `ASSET-BUILDING-VAULT` · 금고
- [ ] `ASSET-BUILDING-FARM` · 농장
- [ ] `ASSET-BUILDING-BARRACKS` · 병영
- [ ] `ASSET-BUILDING-DEFENSE-TOWER` · 방어탑
- [ ] `ASSET-BUILDING-COMMAND-POST` · 지휘소
- [ ] `ASSET-BUILDING-MANA-TOWER` · 마력탑

실제 소비처:
- Ward Citadel/world building sprite
- Build 선택 thumbnail은 가능하면 같은 building art를 crop/reuse
- T2 전문화 preview는 동일 계열 art를 기반으로 후속 확장

현재 `Special Barracks` 등 과거 7-family 표현은 이 목록에 자동 포함하지 않는다. current canon 재확인 전 `NOT_IN_PRODUCTION_QUEUE`.

T2/T3 exact branch sprite 수는 최신 specialization canon fresh-read 후 별도 확장한다.

---

## 5.6 Battlefield / Ward 실제 Environment 자산

전체 BATTLE 화면 스크린샷이 아니라 전장에서 조립해 쓰는 자산을 제작한다.

| Tracker Key | 실제 자산 | 소비처 | 상태 |
|---|---|---|---|
| `ASSET-ENV-FRONT-TERRAIN` | current biome ground / combat-band tiles or plate | three Front-State world views | `NEEDS_BRIEF` |
| `ASSET-ENV-WARD-STRONGHOLD` | allied stronghold / defense-line visual | Front-State / minimap reference | `NEEDS_BRIEF` |
| `ASSET-ENV-VEIL-ANCHOR` | Veil rift/front anchor visual | Front-State world | `NEEDS_BRIEF` |
| `ASSET-ENV-OUTPOST-ROUTE-PROPS` | outpost / route landmark props | Front-State spatial reading | `NEEDS_BRIEF` |

미니맵의 전체 배경을 별도 그림으로 복제하지 않는다. 실제 world state에서 필요한 context marker를 조합하는 방향이 우선이다.

---

## 5.7 Omen Warden 실제 Character 자산

| Tracker Key | 실제 자산 | 소비처 | 상태 |
|---|---|---|---|
| `ASSET-COMMANDER-OMEN-WARDEN` | 긴 지휘 깃발을 든 Omen Warden command sprite/half-body source | PREPARE / COMMIT / Ward command context | `NEEDS_BRIEF` |

대형 상시 전투 초상은 만들지 않는다. 실제 UI/장면에서 필요한 크롭은 이 source에서 파생한다.

---

# 6. P1 · P0 문법 승인 뒤 실제 소비 자산

## Combat / Roulette VFX

- [ ] `ASSET-VFX-DEPLOY` · 병력 배치/증원 VFX → Battlefield deployment
- [ ] `ASSET-VFX-HIT` · hit feedback → Unit battle
- [ ] `ASSET-VFX-MAGIC` · magic/skill effect family → skill runtime, exact skill canon 필요
- [ ] `ASSET-VFX-ROULETTE-SNAP` · row/column move snap → Roulette
- [ ] `ASSET-VFX-LINE-LOCK` · judging / completed line → Roulette
- [ ] `ASSET-VFX-REWARD-REVEAL` · acquired troop reveal → Result/Storage transition
- [ ] `ASSET-VFX-SIEGE-WARNING` · siege urgency → Front-State / minimap context
- [ ] `ASSET-VFX-CAPTURE-GATE-DAMAGE` · stronghold damage/capture feedback → Battlefield

모든 항목은 sprite/flipbook/texture가 실제로 필요한 경우에만 이미지 생성한다. Shader/primitive가 더 적절하면 production asset 목록에서 제거한다.

## Tier / Rank variants

- Unit T2/Tier visual variants
- Building T2/T3 specialization visuals
- Elite / Hero / Legendary visual overlays or unit variants

현재 정확 수량은 `CANON_RECHECK`; 먼저 base unit/building art 문법을 잠근다.

---

# 7. P2 · 실제 소비처가 확정될 때만 추가

- Boss 5/10/15/20 actual battle sprites/effects
- Merchant character/portrait actually shown in REVIEW.MAINTENANCE
- Bellu guide portrait/sprite if current player-facing guide surface is reconfirmed
- additional biome/environment tile sets
- named Hero/Legendary character variants if current canon reconfirms them
- map/settlement/background illustrations only when a concrete game screen consumes them

설명용 `boss hierarchy board`, `faction pair board`, `biome kit sheet`는 만들지 않는다. 필요한 개별 자산만 만든다.

---

# 8. 현재 실제 제작 Queue

```text
REFERENCE
OM-IMG-023 = visual direction only

NOW
1. ASSET-UNIT-LUMERN-SHIELD-GUARD
   BRIEF = OMW-ASSET-BRIEF-20260826-LUMERN-SHIELD-GUARD-01
   FIRST_GENERATION_TARGET = ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
   IMAGE_GENERATION = NOT_STARTED
2. ASSET-UNIT-VEIL-SHIELD-GUARD
   BLOCKED_UNTIL = LUMERN_IDLE_USER_APPROVAL

STYLE_LOCK_AFTER_PAIR
→ faction shape language
→ SD proportion
→ pixel density
→ role silhouette

THEN
3. remaining 18 unit visual slots
4. derived unit-token crops + Gold/X/token frames
5. Omen Signature + resource + minimap icons
6. six current base building sprites
7. Omen workbench component textures
8. battlefield environment assets
9. Omen Warden actual command asset

LATER
P1 VFX / tier variants
P2 content-specific runtime assets
```

## 9. 한 자산 생산 완료 정의

- [ ] named runtime/game consumer가 존재
- [ ] 동일 source art 재사용 가능성 먼저 확인
- [ ] current GitHub + Notion canon fresh-read
- [x] `ASSET-UNIT-LUMERN-SHIELD-GUARD` asset-specific brief 준비
- [ ] 필요한 candidate만 생성
- [ ] 사용자 `APPROVE / REVISE / REJECT`
- [ ] 승인본에 실제 asset identity/file-role 기록
- [ ] Visual Bible / Asset Library에 승인본 등록
- [ ] destination readback
- [ ] 이미지 승인과 runtime/human PASS를 혼동하지 않음

`APPROVED_CURRENT`는 **시각 자산 승인**만 뜻한다. 실제 Godot 소비/크기/animation/성능 검증은 현재 작업 모드에서 `NOT_RUN`이다.

## 10. 5회 전체 적대적 검토

### Loop 1 · 소비처 검사
Finding: 기존 tracker의 Main Battle/PREPARE/COMMIT 전체 화면은 실제 texture consumer가 아니라 composition reference였다.

Correction: production queue에서 제외하고 planning reference로 강등.

### Loop 2 · 중복 자산 검사
Finding: 별도 Roulette unit-token 캐릭터를 만들면 Battlefield unit art와 계보가 갈라진다.

Correction: Token은 approved actual unit art의 Role-Anchor crop으로 파생.

### Loop 3 · 현재 데이터 대조
Finding: runtime bootstrap이 직접 증명하는 기본 unit visual slot은 10 archetype × 2 faction = 20이다.

Correction: 20 unit assets를 실제 전투 소비 자산의 첫 핵심 family로 고정. exact tier variant count는 추정하지 않음.

### Loop 4 · 건물 계보 대조
Finding: 과거 `7 building family` 설명 자료와 current Stage 1의 6 base facilities 사이에 drift 가능성이 있다.

Correction: 현재 FTUE가 명시하는 6 base building sprite만 production queue에 포함. Special Barracks는 재확인 전 제외.

### Loop 5 · 과생산 검사
Finding: UI panel, minimap background, VFX는 Godot Theme/primitive/shader로 충분할 수도 있다.

Correction: `IMAGE_REQUIRED`가 증명되지 않으면 생성하지 않는다. 이미지 생성 자체가 목적이 아니라 실제 게임 소비가 목적이다.

```text
ADVERSARIAL_REVIEW = CLEAN_5_OF_5_AFTER_CORRECTIONS
IMAGE_GENERATION = NOT_STARTED
GODOT_RUNTIME_CONSUMPTION = NOT_RUN
HUMAN_READABILITY = NOT_RUN
```

## 11. Source evidence

- `data/bootstrap_catalog.tres` — 10 archetype × Lumern/Veil visual profiles
- `scripts/data/animation_contract.gd` — unit animation state names
- `scripts/units/unit_view.gd` — current graybox battlefield UnitView consumer seam
- `docs/design/APPROVED_OMENWARD_TOKEN_COMPONENT_SPEC_2026-08-20.md` — actual unit art reuse for Roulette Token
- `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md` — current Stage 1 six base facilities
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md` — current visual style/front/minimap/commander contract
- `docs/images/planning/assets/ASSET_UNIT_LUMERN_SHIELD_GUARD_BRIEF_2026-08-26.md` — first actual runtime asset brief
- `docs/images/planning/OMENWARD_CORE_PLAYER_FLOW_IMAGE_BRIEFS_2026-08-26.md` — composition reference only after this policy

## 12. Boundary

```text
SCREEN_MOCKUP_IMAGE_PRODUCTION = STOPPED
EXPLANATION_SHEET_IMAGE_PRODUCTION = STOPPED
RUNTIME_CONSUMER_ASSET_PLANNING = ACTIVE
FIRST_ACTUAL_ASSET_BRIEF = OMW-ASSET-BRIEF-20260826-LUMERN-SHIELD-GUARD-01
FIRST_ACTUAL_ASSET_BRIEF_STATUS = READY
FIRST_GENERATION_TARGET = ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
IMAGE_GENERATION = NOT_STARTED
PRODUCT_CODE = UNCHANGED
SCENE = UNCHANGED
GODOT_CODEX = OUT_OF_CURRENT_SCOPE
GOOGLE_SHEET = COMPATIBILITY_HISTORY_ONLY
```
