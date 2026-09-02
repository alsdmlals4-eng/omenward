# [현행] OMENWARD 전역 건물 로스터와 점령 슬롯 계약

```yaml
decision_id: OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01
approved_at: 2026-08-30 KST
approval_source: USER_CHAT__"확정, 권장안대로 진행해. godot에 기획안들 전부 다 구현될 때까지 멈추지마"
status: USER_CONFIRMED__PHASE2_IMPLEMENTED__MACHINE_VERIFIED__RUNTIME_TARGET_RESOLUTION_REQUIRED
implementation_issue: 255
scope: BUILDING_ROSTER / OCCUPATION_SLOT_CAPACITY / FIXED_TOWER_OWNERSHIP / STRATEGIC_MAP_VISUAL_GRAMMAR
replaces_in_scope:
  - OMW-PLAN-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01__CONSTRUCTION_NODE_MODEL
  - OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01__CONSTRUCTION_PAD_SCOPE_ONLY
product_code_authority: Issue #255 plus this decision and its RED tests
runtime_asset: NOT_CREATED
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. Player-facing result

The battlefield contains only open terrain, the three fixed route towers, units,
objective ownership feedback, and combat effects. Construction pads, map-built
production buildings, and map-placement menus are forbidden.

```text
BATTLEFIELD_VISIBLE = TERRAIN + FIXED_TOWERS + UNITS + OWNERSHIP_STATE + COMBAT_EFFECTS
BATTLEFIELD_VISIBLE_EXCLUDES = CONSTRUCTION_PADS + PRODUCTION_BUILDINGS + MAP_BUILDING_POPUPS
BUILDING_INTERACTION_SURFACE = PREPARE__GLOBAL_BUILDING_ROSTER
BUILDING_MAP_PLACEMENT = FORBIDDEN
```

The player owns buildings as a single ordered roster. A roster entry is a
MapRun object, not a physical battlefield object. Existing building thumbnails
may be reused as UI icons; the new planning images are not runtime assets.

## 2. Capacity, priority, and temporary loss

```text
BASE_BUILDING_SLOT_CAPACITY = 6
OCCUPATION_SLOT_BONUS = 1_PER_STABLE_PLAYER_HELD_FORWARD_BASE_OR_CLASH_ZONE
UNLOCKED_SLOT_CAPACITY = 6
  + STABLE_PLAYER_OWNED_FORWARD_BASE_COUNT
  + STABLE_PLAYER_OWNED_CLASH_ZONE_COUNT
ROSTER_ORDER = EXPLICIT_PLAYER_PRIORITY_ORDER__TOP_TO_BOTTOM
```

- A stable Lumern-held forward base or clash zone contributes one slot.
- Neutralizing, capturing, stabilizing, and contested objectives contribute
  zero immediately. Citadels never contribute a slot.
- At the current opening state, the three stable Lumern forward bases make
  the capacity `9`. This is a capacity fact, not a final economy value.
- Entries in slots `1..capacity` are `ACTIVE`. Entries below capacity become
  `INACTIVE_LOCKED`; they remain owned and retain their tier and history.
- An inactive entry provides no food-cap bonus, passive, income modifier, or
  Roulette TokenSource. There is no refund, deletion, or forced replacement.
- When capacity returns, entries reactivate deterministically top-to-bottom.

`T2` cost, specialization choice, and output remain simulation-pending in the
existing building-tier authority. This migration preserves the tier field and
shows unavailable research entries, but must not invent upgrade numerics.

## 3. Available and planned roster content

```text
RUNTIME_AVAILABLE = BARRACKS / DEFENSE_TOWER / FARM
RESEARCH_VISIBLE_NOT_IMPLEMENTED = VAULT / SPECIAL_BARRACKS / COMMAND_POST / MANA_TOWER
```

`DEFENSE_TOWER` in the roster is an economy/probability/upgrade identity. It
does not create a physical tower and is distinct from the route's fixed tower.
The UI must distinguish unavailable research entries from currently installable
entries rather than implying that all seven buildings already work.

## 4. One fixed tower per shared front

The repeated direct requirement of **one tower per line** wins over older
per-base layout counts.

```text
FIXED_TOWER_COUNT_PER_SHARED_FRONT = 1
FIXED_TOWER_TOTAL = 3
TOWER_BEARING_OBJECTIVE = WARD_SIDE_FORWARD_BASE
FIXED_TOWER_OWNER = CURRENT_STABLE_TOWER_BEARING_OBJECTIVE_OWNER
FIXED_TOWER_ACTIVE = OBJECTIVE_STATE_STABLE_ONLY
FIXED_TOWER_CAPTURE_POWER = 0
FIXED_TOWER_SOLO_CLEAR = FORBIDDEN
```

Each of the top, middle, and bottom fronts has one tower attached to its
Ward-side forward-base objective. It begins Lumern-owned, transfers to Veil
only after that objective becomes stably Veil-owned, and is disabled during any
capture transition. The opposing forward base and each clash zone still matter
for occupation capacity and income, but do not create a second visible tower.

The fixed tower's initial runtime slice is an ownership and presentation state;
it has no invented attack, target-priority, range, or damage value. It cannot
contribute capture power or resolve a front by itself. Those combat numerics
remain a later simulation-gated implementation.

## 5. Income and Stage 1 boundary

Each stable Lumern-held forward base keeps its existing auditable forward-base
income path. Stable clash-zone control keeps its separate control-income path.
The implementation must count each objective through exactly one path; it may
not add a second "tower income" payment.

```text
STABLE_FORWARD_BASE_GOLD_BONUS = EXISTING_AUDITABLE_OUTPOST_PATH
STABLE_CLASH_ZONE_GOLD_BONUS = EXISTING_AUDITABLE_CONTROL_PATH
DOUBLE_COUNTING = FORBIDDEN
STAGE_1_DIRECT_ROSTER_MUTATION = FORBIDDEN
STAGE_1_ROSTER_VISIBILITY = READ_ONLY_ALLOWED
FIRST_MEANINGFUL_ROSTER_ACTION = STAGE_2_INSTALLATION_AND_REORDER
```

## 6. Required implementation evidence

```text
TEST_BASE_CAPACITY_IS_SIX_PLUS_STABLE_FORWARD_BASE_AND_CLASH_COUNTS
TEST_CONTESTED_OR_STABILIZING_OBJECTIVE_REMOVES_CAPACITY_IMMEDIATELY
TEST_BUILDINGS_ABOVE_CAPACITY_BECOME_INACTIVE_WITHOUT_DELETION_OR_REFUND
TEST_REACTIVATION_RESTORES_TOP_DOWN_ORDER_AND_PRIOR_TIER
TEST_INACTIVE_BUILDING_REMOVES_TOKEN_SOURCE_AND_ALL_PASSIVE_EFFECTS
TEST_FIXED_TOWER_TRANSFERS_ONLY_ON_STABLE_TOWER_BEARING_OBJECTIVE
TEST_FIXED_TOWER_DISABLED_DURING_ALL_CAPTURE_STATES
TEST_FIXED_TOWER_HAS_ZERO_CAPTURE_POWER_AND_CANNOT_SOLO_CLEAR
TEST_GOLD_INCOME_COUNTS_EACH_STABLE_OBJECTIVE_EXACTLY_ONCE
TEST_BATTLEFIELD_HAS_NO_CONSTRUCTION_PAD_OR_MAP_BUILDING_CONSUMER
TEST_STAGE1_REJECTS_ROSTER_MUTATION
TEST_PLAYER_REORDER_PRESERVES_OWNERSHIP_AND_DETERMINES_TOP_DOWN_ACTIVITY
```

## 7. Visual and evidence boundary

`ROSTER-V1` is a generated planning candidate only. It validates hierarchy:
dominant strategic map, three route towers, readable unit groups, and one
player-only roster surface. It is neither a shipped UI asset nor a runtime
capture. Any new runtime image requires its own provenance record, user asset
lock, import, and runtime-readability evidence.

Human UX, player comprehension, final balance, and release-rights status stay
`NOT_RUN` or `UNVERIFIED` until separately observed.
