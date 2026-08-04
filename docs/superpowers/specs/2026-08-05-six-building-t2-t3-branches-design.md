# OMENWARD Six-Building T2/T3 Branches Design

```yaml
decision_id: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
status: USER_APPROVED_DESIGN / NOT_IMPLEMENTED
planning_counter: 3_OF_10
product_code_authority: NONE
simulation: NOT_RUN
human_validation: NOT_RUN
```

## 1. Goal

Define a consistent specialization grammar for the six current buildings so each upgrade changes how the player prepares the roulette or commits to battlefield pressure instead of merely increasing numbers.

```text
T1 base building
├─ T2 branch A → T3 specialization A
└─ T2 branch B → T3 specialization B
```

A building chooses one T2 branch. Only that branch can advance to T3. Cross-branch acquisition and dual-T3 completion are not allowed in the current MapRun.

## 2. Design principles

1. Every branch must state what it gains and what it gives up.
2. Every branch must affect at least two core-fun axes: forecast, reel/TokenSource design, result handling, battlefield commitment, or post-result review.
3. Every pressure must have at least two response routes across buildings, troops, tactics, or roulette preparation.
4. No building branch may solve all five pressures.
5. T3 changes decision logic or targeting priority; a pure numeric increase is insufficient.
6. Upgrade choices are permanent for the current MapRun unless a later approved reset system explicitly overrides this rule.
7. Exact costs, percentages, cooldowns, ranges, spawn values, and Threat Budgets remain simulation-owned.

## 3. Benchmark-derived guardrails

- Specialized upgrades should be readable as distinct strategic roles rather than incremental stat ladders.
- The player must lose access to an alternative strength when committing to a branch.
- Upgrade breadth must stay small enough that the player can compare choices at Stage maintenance without opening a separate encyclopedia.
- Visual evolution should communicate the chosen branch without creating a separate building identity unrelated to the T1 silhouette.

## 4. Branch matrix

### 4.1 Vault / 금고

**T2 A — Stable Treasury / 안정 금고**
- Gain: reduces gold-income volatility and improves reliability of future construction and rerolls.
- Core link: forecast and economy planning.
- Gives up: lower peak payout potential than the speculative branch.
- Pressure fit: `MASS`, `ARMORED` through reliable preparation across multiple waves.

**T3 A — Reserve Treasury / 비축 금고**
- Changes decision logic: converts part of excess Stage-end gold into a protected next-Stage reserve instead of a larger immediate jackpot.
- Does not duplicate merchant stock or create infinite carry growth.

**T2 B — Fortune Vault / 행운 금고**
- Gain: makes gold TokenSource outcomes more swingy but creates stronger high-line payout opportunities.
- Core link: reel design and result handling.
- Gives up: less stable construction timing and greater failure variance.
- Pressure fit: `SIEGE`, `ARMORED` when a high-cost counter must be funded quickly.

**T3 B — Omen Jackpot / 징조 대박**
- Changes decision logic: a disclosed high-line condition can amplify one confirmed gold result, after which the effect enters a non-repeatable Stage cooldown.
- No hidden independent rarity roll.

### 4.2 Farm / 농장

**T2 A — Muster Farm / 징집 농장**
- Gain: higher deployable troop-cap growth.
- Core link: battlefield commitment and multi-lane coverage.
- Gives up: no emergency reserve protection.
- Pressure fit: `MASS`, `INFILTRATION`.

**T3 A — War Levy / 전시 징집령**
- Changes decision logic: reserves a disclosed portion of new capacity for the currently least-defended lane until the player commits it; it does not move already deployed troops.

**T2 B — Reserve Farm / 예비 농장**
- Gain: smaller cap increase plus protection against temporary cap loss or blocked deployment states.
- Core link: forecast and recovery planning.
- Gives up: lower maximum army size.
- Pressure fit: `SIEGE`, `INFILTRATION`.

**T3 B — Last Granary / 최후의 곡창**
- Changes decision logic: once per Stage, a disclosed reserve slot can accept one stored troop even when ordinary capacity is full; it cannot exceed the hard post-Stage cap.

### 4.3 Barracks / 병영

**T2 A — Line Barracks / 전열 병영**
- Gain: specializes the selected T1 troop family toward ground holding, armor breaking, or mass control according to the later troop-role canon.
- Core link: TokenSource identity and battlefield commitment.
- Gives up: reduced access to route/layer-flexible troop outcomes.
- Pressure fit: `MASS`, `ARMORED`, `SIEGE` depending on troop family.

**T3 A — Veteran Line / 정예 전열**
- Changes decision logic: improves the selected family’s committed role and its result-preview explanation; T3 art is not added to roulette tokens.

**T2 B — Route Barracks / 기동 병영**
- Gain: specializes the selected family toward air, bypass, rear-guard, or rapid-response coverage.
- Core link: TokenSource identity and route forecasting.
- Gives up: weaker direct front-line efficiency.
- Pressure fit: `FLYING`, `INFILTRATION`.

**T3 B — Omen Response Corps / 징조 대응대**
- Changes decision logic: the family gains one explicit route-response rule shown before deployment, never free cross-lane movement after commitment.

The exact troop families and combat modifiers remain owned by Decision 4/10.

### 4.4 Defense Tower / 방어탑

**T2 A — Volley Tower / 연사탑**
- Gain: rapid target cycling and crowd suppression.
- Core link: battlefield pressure handling.
- Gives up: poor efficiency against heavy armor and structures.
- Pressure fit: `MASS`, `FLYING` only if the selected tower variant is explicitly anti-air capable.

**T3 A — Interception Battery / 요격 포대**
- Changes decision logic: prioritizes disclosed leak, flyer, or infiltrator threats according to one selected targeting doctrine.
- It may not cover every route simultaneously.

**T2 B — Bombard Tower / 포격탑**
- Gain: slow heavy impact, armor break, and siege interruption.
- Core link: target priority and commitment timing.
- Gives up: poor response to dispersed fast targets.
- Pressure fit: `ARMORED`, `SIEGE`.

**T3 B — Breach Cannon / 파성포**
- Changes decision logic: creates a visible focus window against a marked heavy or siege target instead of passively increasing all damage.

### 4.5 Command Post / 지휘소

**T2 A — Assault Command / 돌격 지휘소**
- Gain: MapRun-wide offensive doctrine for already committed troops.
- Core link: commitment payoff and Stage pressure prioritization.
- Gives up: weaker recovery and hold stability.
- Pressure fit: `ARMORED`, `SIEGE`.

**T3 A — Decisive Front / 결전 전선**
- Changes decision logic: before a Stage begins, the player marks one disclosed decisive lane for the doctrine bonus. The mark cannot move mid-Stage.

**T2 B — Bastion Command / 수비 지휘소**
- Gain: MapRun-wide defensive doctrine and better survival of spread commitments.
- Core link: multi-lane planning and failure prevention.
- Gives up: lower burst conversion.
- Pressure fit: `MASS`, `INFILTRATION`.

**T3 B — Layered Defense / 종심 방어**
- Changes decision logic: the player assigns one disclosed rear-guard priority before Stage start; it does not recall or relocate troops.

Assault and Bastion families may coexist only through separate Command Posts. Same-family effects use the highest active Tier and do not stack.

### 4.6 Magic Tower / 마력탑

**T2 A — Flow Tower / 유량 마력탑**
- Gain: steadier mana-stone generation during the MapRun.
- Core link: tactical-skill cadence and forecast.
- Gives up: lower emergency storage ceiling.
- Pressure fit: `MASS`, `INFILTRATION` through frequent low-cost tactical responses.

**T3 A — Pulse Conduit / 맥동 도관**
- Changes decision logic: provides a disclosed timing pulse that rewards planned skill cadence; it does not auto-cast skills.

**T2 B — Reservoir Tower / 저장 마력탑**
- Gain: larger mana-stone capacity and stronger preparation for rare high-cost responses.
- Core link: Stage-to-Stage planning and boss preparation.
- Gives up: slower routine generation.
- Pressure fit: `ARMORED`, `SIEGE`, `FLYING` depending on later tactical-skill canon.

**T3 B — Omen Reservoir / 징조 저장고**
- Changes decision logic: protects a disclosed reserve amount for the next Boss or Danger Stage, but reserved mana cannot be spent on ordinary Waves until released.

## 5. Pressure coverage

The building matrix alone must not hard-counter every pressure, but it must create at least two meaningful preparation routes when combined with later troop and tactical decisions.

| Pressure | Building preparation routes |
|---|---|
| MASS | Muster Farm, Volley Tower, Bastion Command, Flow Tower |
| ARMORED | Fortune Vault, Line Barracks, Bombard Tower, Assault Command, Reservoir Tower |
| FLYING | Route Barracks, explicit anti-air Volley doctrine, Reservoir Tower for later anti-air tactics |
| INFILTRATION | Muster/Reserve Farm, Route Barracks, Interception doctrine, Bastion Command, Flow Tower |
| SIEGE | Reserve Farm, Line Barracks, Bombard Tower, Assault Command, Reservoir Tower |

No row is an implementation guarantee before troop roles and tactical skills are approved. It is a dependency map for Decisions 4/10 and 5/10.

## 6. UX contract

- The maintenance screen shows both T2 branches side by side.
- Each card must show: `gain`, `give-up`, `best pressure fit`, `core-loop impact`, and `T3 preview`.
- Locked opposite branches remain visible after selection so the opportunity cost stays understandable.
- Exact numeric deltas are not shown in planning canon until simulation values exist.
- A branch icon and silhouette accent may change, but the T1 building remains visually recognizable.

## 7. Failure conditions

The design fails if any of the following becomes true:

1. A branch is only a larger percentage with no changed decision.
2. Both branches can be completed in one MapRun without an explicit later reset decision.
3. One branch is the best answer to all five pressures.
4. A building silently changes the required counter after Stage start.
5. A building grants free troop recall, free cross-lane movement, automatic tactical casting, infinite gold, or infinite mana.
6. Barracks T3 introduces roulette T3 troop images.
7. Exact balance values are treated as approved before simulation.
8. The upgrade UI hides the foregone branch or its trade-off.

## 8. TDD acceptance contract

Repository validation must fail before canon implementation when:

- the 3/10 design/spec or current authority document is missing;
- the common `T1 → one of two T2 → matching T3` grammar is absent;
- cross-branch or dual-T3 acquisition is allowed;
- any of the six buildings lacks two named branches and a stated give-up;
- pressure coverage omits any of the five pressure tags;
- the process policy omits benchmarking, 10-approval batch limit, early checkpoint conditions, or mandatory TDD;
- current central docs and Google Sheet do not point to the same Decision ID and counter.

## 9. Scope boundaries

Included:
- player-visible branch roles and trade-offs;
- pressure-response dependency map;
- upgrade comparison UX;
- documentation lifecycle and validation rules.

Excluded:
- exact costs and percentages;
- combat stats, targeting algorithms, coordinates, timers, persistence schema;
- troop-family roster and tactical-skill effects;
- product code, scenes, resources, game data, and actual art assets.
