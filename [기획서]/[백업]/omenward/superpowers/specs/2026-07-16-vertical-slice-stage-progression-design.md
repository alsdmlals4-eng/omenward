# Vertical Slice and Stage Progression Design

## Goal

Deliver a playable OMENWARD proof of concept with one scripted tutorial and one regular stage that runs W1 through W20, then merge the validated work into `main`.

## Scope

The tutorial contains four deterministic waves and teaches construction, the 3×3 roulette, lane deployment, one defensive building, and the first archetype choice. Completion unlocks the regular stage.

The regular stage shares the same systems and has twenty deterministic waves: baseline pressure in W1–W4, elite at W5, hero at W10, legendary boss and standard victory target at W15, overtime pressure at W16–W19, and a mythic boss at W20. A player may win through the W15 objective or enemy-base destruction; surviving beyond W15 enables the overtime sequence.

## Architecture

`GameSession` remains the composition root and owns a `StageRun` state machine. A `StageManifest` defines tutorial and regular-stage data, including economy, unlocked actions, omen schedule, wave compositions, lane assignments, and victory rules. A single shared `Unit` scene is instantiated from the existing public archetype, tier, rank, team, and visual-faction contract; enemies differ only by team, visual set, and wave spawn instruction.

The battle scene owns three isolated lane simulators. Each lane contains its own gates, middle outposts, clash zone, unit spatial list, and assassin bypass route. It exposes observable state to HUD/debug controls but has no cross-lane movement graph. Economy, building nodes, roulette results, deploy queue, wave clock, combat results, stage result, and deterministic input log are independent services coordinated by `StageRun`.

## Playable Loop

```text
stage selection
→ omen
→ build / roulette / deploy
→ three-lane simulation
→ capture / bypass / gate siege
→ wave result and next omen
→ stage victory or defeat
→ retry or next stage
```

## Representative Content

Implement shield guard, archer, assassin, priest, and giant as playable shared archetypes. Use geometric placeholder presentation and the existing faction visual identities; no final art, audio, save system, multiplayer, procedural campaign, or enemy-specific combat profile is introduced.

## Invariants

- Preserve the common ten-archetype contract; never create enemy-only unit resources, scenes, statistics, skills, targeting, or animation contracts.
- Keep the three lanes disconnected for ordinary units; only the assassin can use its own same-lane bypass route.
- Keep each side's three gates independent and each middle outpost at two forward plus one rear build node.
- Do not add a minimap or gate repair/rebuild.
- Treat W1–W20 as waves inside one regular stage, not as twenty separate stages.

## Validation

Headless tests must validate stage manifest loading, deterministic W1–W20 scheduling, tutorial completion/unlock, shared-unit faction invariance, isolated lanes, outpost transitions, gate modifiers, assassin timing, and reproducible stage result from the same seed/input log. Manual QA covers an actual complete tutorial and normal-stage run, plus 1920×1080 and 1280×720 readability.

## Risks and Controls

The full set of systems is broad, so scene presentation stays graybox and the wave database remains declarative. W16–W20 are implemented as data-driven pressure escalation rather than new parallel combat code. Tests exercise each state-machine boundary before UI integration.
