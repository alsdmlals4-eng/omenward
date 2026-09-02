# Five Sequential Front Maps · Blueprint V1

```yaml
blueprint_id: OMW-BLUEPRINT-20260902-FIVE-SEQUENTIAL-FRONT-MAPS-V1
status: USER_CONFIRMED__RESEARCHED__FEASIBLE__SPECIFIED__IMPLEMENTATION_AUTHORIZED
product_owner: docs/design/APPROVED_OMENWARD_FIVE_SEQUENTIAL_FRONT_MAPS_2026-09-02.md
predecessor: OMW-BLUEPRINT-20260902-BATTLE-PRIMARY-HIERARCHY-RECOVERY-V2
visual_style: STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
runtime_evidence: NOT_RUN
human_evidence: NOT_RUN
```

## Intent

The upper five-cell ribbon becomes the progress map for five sequential, independently
loaded battlefields. It remains context, never a second battlefield. The screen still
has one active combat map and one fixed tower.

## State model

```text
front_map_state[index] = LOCKED | CURRENT | CLEARED

start regular Stage:
  [CURRENT, LOCKED, LOCKED, LOCKED, LOCKED]

map 1–4 win:
  [CLEARED, CURRENT, LOCKED, LOCKED, LOCKED]   # only after explicit next CTA

map 5 win:
  [CLEARED, CLEARED, CLEARED, CLEARED, CLEARED]
  -> StageRun.VICTORY
```

## Flow map

```text
                           ┌───────────────────────────┐
                           │  top ribbon: 5 map states │
                           │ cleared / current / lock  │
                           └─────────────┬─────────────┘
                                         │ read-only
PREPARE ──> ROULETTE ──> COMMIT ──> BATTLE(current terrain / 4 waves)
   ^                                     │
   │                                     ├── map 1–4 victory ──> REVIEW ──> next CTA ──┐
   │                                     │                                                │
   └─────────────────────────────────────┴────────────────────────────────────────────────┘
                                         │
                                         └── map 5 victory ──> FINAL REVIEW / Stage victory
```

## Wireframe

```text
16,12 ┌───────────────────────────────── TopBar: 내정 | 룰렛 | 전선 ─────────────────────────────────┐
16,62 ├─ 전진 ─ [완료 수호 성채]─[현재 수호 전진]─[잠김 접전]─[잠김 장막 전진]─[잠김 베일 성채] ─┤
16,110│                                                                                          │
      │     current FrontMapDefinition terrain + one tower + actual units only                  │
      │     wide clear horizontal troop corridor; props are outside it                           │
      │                                                                                          │
16,422├─ context-sensitive lower deck: PREPARE / roulette / commit / battle / review CTA ──────┤
      └──────────────────────────────────────────────────────────────────────────────────────────┘
```

## Asset requirement

Five `Texture2D` foundations are required, one per `FrontMapDefinition`. Each is 16:9
storybook watercolor tactical terrain, without UI/text/units/markers, with a clear
horizontal travel corridor. No building, construction node, fence, barricade, bridge or
river may obstruct travel. Candidate files are not canonical or runtime-bound until their
provenance and user visual confirmation are recorded.

## Rejection criteria

- Showing five battlefield views at once, a selectable map menu, or a return to three fronts.
- Advancing the full Stage after a non-final map victory.
- Resetting the global roster/economy when entering the next map.
- Turning a map change into map-building, tower multiplication, or an obstacle corridor.
- Treating generated candidate PNGs as approved canonical runtime assets without the required record.
