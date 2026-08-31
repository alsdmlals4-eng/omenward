# OMENWARD · Global Building Roster and Occupation Slot Design

```yaml
spec_id: OMW-DRAFT-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01
captured_at: 2026-08-30 KST
source: USER_DIRECTION_IN_CHAT
status: USER_DIRECTION_CAPTURED__PLANNING_REVIEW_REQUIRED
work_mode: PLAN
scope: BUILDING_ROSTER / OCCUPATION_SLOT_CAPACITY / FIXED_TOWER_OWNERSHIP / STRATEGIC_MAP_VISUAL_GRAMMAR
product_code_authority: NONE
runtime_asset: NOT_CREATED
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
supersession_candidate:
  - OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01__CONSTRUCTION_PAD_SCOPE_ONLY
  - OMW-VISUAL-LOCK-20260829-OPEN-BATTLEFIELD-V6-01__DISCOVERABLE_PAD_SCOPE_ONLY
```

## 1. User-directed result

The battlefield contains **terrain, fixed defense towers, units, ownership state, and combat effects only**. It contains no construction pad, production building, building-selection pop-up, or map-placement interaction.

Buildings live in a player-only **global building roster**. In `PREPARE`, the player uses the compact lower work surface to install, prioritize, and upgrade buildings; no building chooses a battlefield coordinate or a forward-base node.

```text
BATTLEFIELD_VISIBLE = TERRAIN + FIXED_TOWERS + UNITS + OWNERSHIP_STATE + COMBAT_EFFECTS
BATTLEFIELD_VISIBLE_EXCLUDES = CONSTRUCTION_PADS + PRODUCTION_BUILDINGS + MAP_BUILDING_POPUPS
BUILDING_INTERACTION_SURFACE = PREPARE__GLOBAL_BUILDING_ROSTER
BUILDING_MAP_PLACEMENT = FORBIDDEN
```

This retains the protected product identity:

```text
BUILDINGS -> PLAYER_CONSTRUCTED_PROBABILITY_ENGINE -> 3x3 OMEN WHEEL -> UNIT ACQUISITION -> IRREVERSIBLE_FRONT_COMMIT
```

It does not introduce free-form defense construction, a fixed reel-to-front mapping, automatic deployment, or a gambling presentation.

## 2. Selected model and alternatives considered

| Model | Result | Reason |
|---|---|---|
| **Global roster; capacity from base six plus stable player-held objectives** | **SELECTED** | Keeps the map readable, makes occupation improve strategic capacity, and preserves a single player-owned building surface. |
| Separate building rows for each front | REJECTED | Reintroduces implied map placement and creates three competing inventories; this obscures the global probability-engine decision. |
| Construction pads or free map placement | REJECTED | Conflicts directly with the user direction and turns the battlefield into a base-building board. |

The reference research supports treating a building roster as a strategic choice surface, but it does **not** license copying another game’s UI or construction system. Free-form fortress construction is explicitly rejected because it would make building placement the dominant game loop rather than the roulette and irreversible three-front commitment. [Against the Storm Building reference](https://wiki.hoodedhorse.com/Against_the_Storm/Buildings); [Cataclismo official product description](https://store.steampowered.com/app/1422440/Cataclismo/).

## 3. Global roster and slot contract

### 3.1 Capacity

```text
BASE_BUILDING_SLOT_CAPACITY = 6
OCCUPATION_SLOT_BONUS = 1_PER_STABLE_PLAYER_HELD_CAPTURE_OBJECTIVE
CAPTURE_OBJECTIVE_TYPES = FORWARD_BASE + CLASH_ZONE
UNLOCKED_SLOT_CAPACITY = 6
  + STABLE_PLAYER_OWNED_FORWARD_BASE_COUNT
  + STABLE_PLAYER_OWNED_CLASH_ZONE_COUNT
```

The current combat model represents three initially Lumern-owned forward bases, three Veil forward bases, and three clash zones. With that current model, a newly started Lumern run has `6 + 3 = 9` unlocked slots. If Lumern stably holds every forward base and clash zone, the conceptual ceiling is `6 + 9 = 15` slots. This is a **capacity rule**, not a final economy or balance value; it needs simulation before product numerics are locked.

`STABLE` is required. A neutralizing, capturing, stabilizing, or contested objective contributes zero capacity immediately. A home Citadel is not a capture objective and never grants a slot.

### 3.2 Order, activation, and ownership loss

```text
ROSTER_ORDER = EXPLICIT_PLAYER_PRIORITY_ORDER__TOP_TO_BOTTOM
ACTIVE_BUILDING_SLOTS = [1..UNLOCKED_SLOT_CAPACITY]
INACTIVE_BUILDING_SLOTS = [UNLOCKED_SLOT_CAPACITY + 1..OWNED_BUILDING_COUNT]
```

- A player installs a building into the next empty roster slot or replaces an explicitly selected empty/ruined slot in `PREPARE`.
- The player can reorder owned building cards in `PREPARE`; top-to-bottom order determines the survival priority when capacity changes.
- A building in an unlocked slot is `ACTIVE` and applies its approved effect, including any valid TokenSource contribution.
- When an objective is lost and its slot bonus disappears, every building below the new capacity becomes `INACTIVE_LOCKED`. It remains owned, retains its tier and upgrade history, occupies its roster slot, and receives no refund.
- `INACTIVE_LOCKED` buildings contribute **no** food-cap bonus, auto-production benefit, global modifier, mana benefit, gold modifier, or Roulette TokenSource. Their card states the exact missing capacity and the objective(s) that would reopen it.
- When enough objectives return to stable player ownership, slots reactivate deterministically from the top down. The reactivated building restores its existing state; it does not require another purchase.

No occupied map node, node ruin, or per-outpost building state exists in the target model. A player-owned building is a MapRun roster object, not a physical battlefield structure.

### 3.3 Building roster content

The current long-term planning lineage remains:

```text
VAULT / FARM / GENERAL_BARRACKS / SPECIAL_BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
```

The current runnable implementation only contains `BARRACKS / TOWER / FARM`. The target roster UI must never imply that the other four are implemented. The actual available roster is data-driven, with locked/research-pending entries visibly distinct from usable entries.

`DEFENSE_TOWER` in the building roster is a probability/economy/upgrading object. It is distinct from a **fixed battlefield defense tower**, never creates a physical building on the map, and does not consume or grant a capture objective.

### 3.4 First-session boundary

```text
STAGE_1_DIRECT_BUILD_OR_UPGRADE = FORBIDDEN
STAGE_1_ROSTER_VISIBILITY = OPTIONAL_READONLY_PREVIEW
FIRST_MEANINGFUL_ROSTER_ACTION = STAGE_2
```

Stage 1 may show the roster’s locked capacity/read-only explanation, but cannot permit purchase, upgrade, reorder-for-benefit, or a prescriptive construction prompt. The three-front forecast, 3×3 wheel, and irreversible commitment remain its teaching sequence.

## 4. Capturable objective and fixed tower contract

### 4.1 Ownership and tower state

Every visible forward base owns one **fixed defense tower** that is separate from the building roster.

```text
FIXED_TOWER_OWNER = CURRENT_STABLE_OBJECTIVE_OWNER
FIXED_TOWER_ACTIVE = OBJECTIVE_STATE_STABLE_ONLY
FIXED_TOWER_CAPTURE_POWER = 0
FIXED_TOWER_SOLO_CLEAR = FORBIDDEN
FIXED_TOWER_DOES_NOT_CONSUME_ROSTER_SLOT = TRUE
```

| Objective state | Tower | Slot bonus | Gold benefit |
|---|---|---:|---:|
| Lumern stable owner | Lumern-controlled local support fire | +1 for a forward base | eligible for stable-occupation income |
| Veil stable owner | Veil-controlled local support fire | 0 | 0 for Lumern |
| Neutralizing / capturing / stabilizing / contested | disabled; no team fires it | 0 | 0 |

A clash zone is a capturable objective and grants one roster slot on stable Lumern control, but it does **not** create a tower. It changes the nearby forward-base pressure and provides its own current front-state marker only.

### 4.2 Economy direction

Each stable Lumern-held forward base also increases gold income. The implementation must replace or reconcile the existing generic stable-outpost income so one objective cannot be paid twice.

```text
STABLE_FORWARD_BASE_GOLD_BONUS = REQUIRED
STABLE_CLASH_ZONE_GOLD_BONUS = RETAIN_OR_RECONCILE_WITH_CURRENT_CONTROL_INCOME
EXACT_GOLD_AMOUNT_AND_INTERVAL = PENDING_SIMULATION
DOUBLE_COUNTING = FORBIDDEN
```

The existing runtime has separate control income and stable-outpost income paths. Their final relationship is deliberately not selected here; the required future simulation will select one auditable formula.

## 5. Player-facing flow

```text
FORECAST
→ PREPARE: see roster capacity, active/inactive cards, and occupation-linked slot state
→ install / prioritize / upgrade a global building without placing it on the map
→ 3×3 omen-wheel distribution and limited manipulation
→ choose a front and atomic irreversible unit commitment
→ BATTLE: read terrain, units, fixed towers, ownership, and pressure only
→ REVIEW: see which held/lost objectives changed tower allegiance, income, and roster activation
```

The `PREPARE` lower deck has one active surface. The roster must not compete visually with the 3×3 wheel: opening the wheel replaces the roster surface rather than overlaying it.

Required player-visible feedback:

1. `Slots 9 / 9 unlocked` or an equivalent accessible, localizable representation.
2. A clear top-to-bottom priority marker on active cards and a locked-state reason on inactive cards.
3. Stable forward-base ownership changes the local tower’s banner/faction language and its gold feedback.
4. Capture transition disables the tower and immediately explains the lost slot and deactivated building, without deleting the player’s building card.
5. Review maps forecast, objective transition, roster activation change, and combat outcome without prescribing a “correct” next build.

## 6. Visual-candidate brief

Three planning-only images are required before the visual direction is promoted:

| Candidate | Purpose | Required contents | Exclusions |
|---|---|---|---|
| `MAP-V8` | strategic battlefield grammar | open terrain, a single Ward root, a single Veil root, three shared fronts, fixed towers, small unit groups, ownership flags | construction pads, barracks, farms, building pop-ups, UI text |
| `ROSTER-V1` | player-only building management surface | six base slots plus occupation-unlocked rows, top-priority convention, inactive-lock convention, upgrade affordances | map-coordinate placement, pseudo-localized gameplay text, implementation claim |
| `OWNERSHIP-V1` | front-state comparison | stable Lumern / contested / stable Veil forward-base tower states and their roster/income consequence | a second battlefield, permanent barricades, production buildings on terrain |

All three are `PLANNING_REFERENCE_ONLY`, created with built-in ImageGen, and are not runtime assets, release assets, or proof of human usability.

## 7. Implementation and migration boundary

No code, scene, resource, data, runtime asset, or existing planning board is changed by this document. After user review of the three candidates, an approved packet must supersede only the construction-pad scope of the v6 documents and then open a separate Phase 2 implementation issue with RED tests.

The future migration must:

1. replace per-outpost construction-node keys with global roster slot entries;
2. preserve owned building tier/upgrade state across temporary capacity loss;
3. derive capacity from stable objective snapshots rather than map nodes;
4. route fixed towers from stable objective ownership without capture contribution or solo clear;
5. reconcile current gold paths without double counting;
6. remove battlefield node drawing and map-building UI only after the approved replacement roster surface exists.

## 8. Required future RED tests and review gates

```text
TEST_BASE_CAPACITY_IS_SIX_PLUS_STABLE_FORWARD_BASE_AND_CLASH_COUNTS
TEST_STARTING_LUMERN_FORWARD_BASES_CONTRIBUTE_CAPACITY
TEST_CONTESTED_OR_STABILIZING_OBJECTIVE_REMOVES_CAPACITY_IMMEDIATELY
TEST_BUILDINGS_ABOVE_CAPACITY_BECOME_INACTIVE_WITHOUT_DELETION_OR_REFUND
TEST_REACTIVATION_RESTORES_TOP_DOWN_ORDER_AND_PRIOR_TIER
TEST_INACTIVE_BUILDING_REMOVES_TOKEN_SOURCE_AND_ALL_PASSIVE_EFFECTS
TEST_FIXED_TOWER_TRANSFERS_ONLY_ON_STABLE_OBJECTIVE_OWNER
TEST_FIXED_TOWER_DISABLED_DURING_ALL_CAPTURE_STATES
TEST_FIXED_TOWER_HAS_ZERO_CAPTURE_POWER_AND_CANNOT_SOLO_CLEAR
TEST_GOLD_INCOME_COUNTS_EACH_STABLE_OBJECTIVE_EXACTLY_ONCE
TEST_BATTLEFIELD_HAS_NO_CONSTRUCTION_PAD_OR_MAP_BUILDING_CONSUMER
TEST_STAGE1_REJECTS_ROSTER_MUTATION
```

Before implementation, perform the project Phase 2 readiness review: fresh `main` and work-item readback, explicit Issue, RED tests, implementation packet, provenance review, target-resolution runtime QA plan, and a five-loop adversarial review. Human UX and player-experience status remain `NOT_RUN` until recorded observation exists.

## 9. Risks and rollback

| Risk | Guardrail | Rollback boundary |
|---|---|---|
| A lost objective silently changes roulette odds | immediate roster lock event and token-ledger diff in the review | preserve roster object; only restore capacity when objective is stable again |
| Too many starting slots make construction trivial | exact output/economy values stay simulation-pending; capacity is independent from free purchases | tune costs/output, not the user-directed capacity formula, unless a new user decision changes it |
| Tower ownership hides the player’s required unit commitment | tower contributes no capture power and cannot clear a front alone | disable tower support first, retaining objective ownership state |
| Roster and roulette compete for attention | one active lower-deck surface; no overlay | close roster when opening wheel |
| Legacy per-outpost state causes a partial migration | new global roster data must be introduced behind RED tests before node code is removed | retain legacy state only until an approved migration pass has verified parity |

