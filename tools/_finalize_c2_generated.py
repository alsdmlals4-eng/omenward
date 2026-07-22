from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one replacement, found {count}: {old[:120]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


replace_once(
    "scripts/battle/unit_instance.gd",
    '''func move_toward_position(position: float, delta: float) -> void:
\tstate = "move"
\tvar direction := signf(position - lane_position)
\tlane_position += direction * float(_stats.get("move_speed", 0.0)) * delta
''',
    '''func move_toward_position(position: float, delta: float) -> void:
\tstate = "move"
\tvar distance := position - lane_position
\tvar step := float(_stats.get("move_speed", 0.0)) * delta
\tif absf(distance) <= step:
\t\tlane_position = position
\telse:
\t\tlane_position += signf(distance) * step
''',
)

replace_once(
    "scripts/buildings/building_service.gd",
    '''\t\tvar should_be_active := outpost.owner_team_id == PLAYER_TEAM_ID
''',
    '''\t\tvar should_be_active: bool = outpost.owner_team_id == PLAYER_TEAM_ID
''',
)

replace_once(
    "scripts/battle/outpost_state.gd",
    '''func set_contested() -> void:
\tif state != NEUTRALIZING and state != CAPTURING:
\t\treturn
\tcapture_power = 0.0
\tcontested = true
\t_hold_remaining = 0.0
\t_is_reverting = false
''',
    '''func set_contested() -> void:
\tif state == STABILIZING:
\t\treturn
\tcapture_power = 0.0
\tcontested = true
\t_hold_remaining = 0.0
\t_is_reverting = false
''',
)

replace_once(
    "scripts/battle/battle_simulator.gd",
    '''\tif state.is_stable_for(team_id):
\t\treturn
''',
    '''\tif state.is_stable_for(team_id):
\t\tstate.contested = false
\t\treturn
''',
)

replace_once(
    "tests/headless/c2_battle_objective_test.gd",
    '''func _test_objective_sequence_and_lane_gate_isolation(failures: PackedStringArray) -> void:
\tvar battle := BattleSimulator.new(_registry(), 101)
\tvar giant: Variant = battle.spawn_unit(_spawn(&"lumern", &"top", &"giant"))
\tgiant.lane_position = battle.CLASH_POSITION
\tbattle.advance(20.0)
\t_expect(battle.clash_zones[&"top"].outpost.is_stable_for(&"lumern"), "an uncontested giant captures the top clash", failures)
\tgiant.lane_position = float(battle.OUTPOST_POSITIONS[&"veil"])
\tbattle.advance(10.0)
\t_expect(battle.outposts[&"veil"][&"top"].is_stable_for(&"lumern"), "the same lane force captures the enemy top outpost", failures)
\tgiant.lane_position = float(battle.GATE_POSITIONS[&"veil"])
''',
    '''func _test_objective_sequence_and_lane_gate_isolation(failures: PackedStringArray) -> void:
\tvar battle := BattleSimulator.new(_registry(), 101)
\tvar giants: Array = []
\tfor _index in 4:
\t\tvar giant: Variant = battle.spawn_unit(_spawn(&"lumern", &"top", &"giant"))
\t\tgiant.lane_position = battle.CLASH_POSITION
\t\tgiants.append(giant)
\tbattle.advance(10.0)
\t_expect(battle.clash_zones[&"top"].outpost.is_stable_for(&"lumern"), "an uncontested giant squad captures the top clash", failures)
\tfor giant in giants:
\t\tgiant.lane_position = float(battle.OUTPOST_POSITIONS[&"veil"])
\tbattle.advance(15.0)
\t_expect(battle.outposts[&"veil"][&"top"].is_stable_for(&"lumern"), "the same lane force captures the enemy top outpost", failures)
\tfor giant in giants:
\t\tgiant.lane_position = float(battle.GATE_POSITIONS[&"veil"])
\tvar giant: Variant = giants[0]
''',
)

replace_once(
    "tests/headless/c2_battle_objective_test.gd",
    '''\tgiant.lane_position = float(battle.BASE_POSITIONS[&"veil"])
\tbattle.bases[&"veil"].apply_damage(100000.0, true)
''',
    '''\tfor attacker in giants:
\t\tattacker.lane_position = float(battle.BASE_POSITIONS[&"veil"])
\tbattle.bases[&"veil"].apply_damage(100000.0, true)
''',
)

replace_once(
    "tests/headless/c2_battle_objective_test.gd",
    '''\t_test_natural_base_result(failures)
\t_finish(failures)
''',
    '''\t_test_natural_base_result(failures)
\t_test_stage_natural_results(failures)
\t_finish(failures)
''',
)

replace_once(
    "tests/headless/c2_battle_objective_test.gd",
    '''const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
''',
    '''const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"
''',
)

replace_once(
    "tests/headless/c2_battle_objective_test.gd",
    '''func _registry() -> Variant:
''',
    '''func _test_stage_natural_results(failures: PackedStringArray) -> void:
\tvar tutorial: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
\tvar victory_progression := StageProgression.new()
\tvar victory_run := StageRun.new(victory_progression)
\tvictory_run.start(tutorial, 505)
\tvictory_run.battle.bases[&"veil"].apply_damage(100000.0, true)
\tvictory_run.advance(0.1)
\t_expect(victory_run.result_state == victory_run.VICTORY and victory_progression.regular_unlocked, "enemy base destruction closes StageRun as victory", failures)
\tvar defeat_run := StageRun.new(StageProgression.new())
\tdefeat_run.start(tutorial, 506)
\tdefeat_run.battle.bases[&"lumern"].apply_damage(100000.0, true)
\tdefeat_run.advance(0.1)
\t_expect(defeat_run.result_state == defeat_run.DEFEAT, "player base destruction closes StageRun as defeat", failures)
\tvar progression := StageProgression.new()
\tprogression.regular_unlocked = true
\tvar regular: Resource = ResourceLoader.load(REGULAR_STAGE_PATH)
\tvar boss_run := StageRun.new(progression)
\tboss_run.start(regular, 507)
\tboss_run.battle.objectives_enabled = false
\twhile boss_run.current_wave < 15:
\t\tboss_run.advance(60.0)
\t_expect(boss_run.legendary_boss_unit_id > 0, "W15 records the legendary boss runtime identity", failures)
\tvar boss: Variant = boss_run.battle.get_unit_by_id(boss_run.legendary_boss_unit_id)
\tif boss != null:
\t\tboss.health = 0.0
\tboss_run.advance(0.1)
\t_expect(boss_run.result_state == boss_run.VICTORY, "W15 legendary boss defeat produces standard victory", failures)


func _registry() -> Variant:
''',
)

replace_once(
    "tools/validate_c2_battle_objective.py",
    '''        "an uncontested giant captures the top clash",
''',
    '''        "an uncontested giant squad captures the top clash",
''',
)

replace_once(
    "tools/validate_c2_battle_objective.py",
    '''        "enemy base destruction produces a natural battle victory",
        "player base destruction produces a natural battle defeat",
''',
    '''        "enemy base destruction produces a natural battle victory",
        "player base destruction produces a natural battle defeat",
        "enemy base destruction closes StageRun as victory",
        "W15 legendary boss defeat produces standard victory",
''',
)

failure_log = ROOT / "docs/_C2_RUNTIME_FAILURE.log"
if failure_log.exists():
    failure_log.unlink()
self_path = ROOT / "tools/_finalize_c2_generated.py"
if self_path.exists():
    self_path.unlink()
