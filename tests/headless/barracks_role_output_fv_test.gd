# 병영 역할 기능가치 시나리오의 원시 이벤트를 수집하는 헤드리스 진단입니다.
extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const BattleSimulator = preload("res://scripts/battle/battle_simulator.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const FV_SCENARIO_CONTRACTS := {
	"FV-COMMON-01": {"greatsword_warrior": 1, "shield_guard": 1, "events": []},
	"FV-PRIEST-01": {"priest": 1, "shield_guard": 1, "events": ["role_buff_start", "role_buff_end"]},
	"FV-MAGE-01": {"mage": 1, "shield_guard": 3, "events": ["role_aoe_hit"]},
	"FV-FLIER-01": {"flier": 1, "archer": 1, "shield_guard": 1, "events": ["role_backline_contact", "role_dive"]},
	"FV-GIANT-01": {"giant": 1, "flier": 1, "shield_guard": 7, "events": ["role_slam"]},
}


func _init() -> void:
	_emit("FV-COMMON-01", _common_battle())
	_emit("FV-PRIEST-01", _priest_battle())
	_emit("FV-MAGE-01", _mage_battle())
	_emit("FV-FLIER-01", _flier_battle())
	_emit("FV-GIANT-01", _giant_battle())
	quit(0)


func _emit(scenario_id: String, battle: BattleSimulator) -> void:
	var events := battle.drain_events()
	var snapshot := battle.snapshot()
	_assert_fixture_contract(scenario_id, snapshot, events)
	print(JSON.stringify({
		"scenario_id": scenario_id,
		"role_metrics": battle.role_output_metrics(),
		"raw_events": events,
		"snapshot": snapshot,
	}))


func _assert_fixture_contract(scenario_id: String, snapshot: Dictionary, events: Array) -> void:
	var contract: Dictionary = FV_SCENARIO_CONTRACTS.get(scenario_id, {})
	if contract.is_empty():
		push_error("Unregistered FV scenario: %s" % scenario_id)
		return
	var counts := {}
	for unit in snapshot.get("units", []):
		var archetype_id := str(unit.get("archetype_id", ""))
		counts[archetype_id] = int(counts.get(archetype_id, 0)) + 1
	for archetype_id in contract:
		if archetype_id == "events":
			continue
		if int(counts.get(archetype_id, 0)) != int(contract[archetype_id]):
			push_error("%s fixture structure mismatch for %s" % [scenario_id, archetype_id])
	for required_event in contract["events"]:
		if not events.any(func(event: Dictionary) -> bool: return event.get("event_type") == required_event):
			push_error("%s fixture missing runtime event %s" % [scenario_id, required_event])


func _common_battle() -> BattleSimulator:
	var battle := _battle(2101)
	battle.objectives_enabled = false
	var attacker = battle.spawn_unit(_spawn(&"lumern", &"middle", &"greatsword_warrior"))
	var defender = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
	attacker.lane_position = 50.0
	defender.lane_position = 52.0
	_advance(battle, 2.0)
	return battle


func _priest_battle() -> BattleSimulator:
	var battle := _battle(2102)
	battle.objectives_enabled = false
	var priest = battle.spawn_unit(_spawn(&"lumern", &"top", &"priest"))
	var ally = battle.spawn_unit(_spawn(&"lumern", &"top", &"shield_guard"))
	_advance(battle, 5.2)
	return battle


func _mage_battle() -> BattleSimulator:
	var battle := _battle(2103)
	battle.objectives_enabled = false
	var mage = battle.spawn_unit(_spawn(&"lumern", &"middle", &"mage"))
	mage.lane_position = 50.0
	for position in [51.0, 52.0, 53.0]:
		var enemy = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
		enemy.lane_position = position
	_advance(battle, 2.0)
	return battle


func _flier_battle() -> BattleSimulator:
	var battle := _battle(2104)
	battle.objectives_enabled = false
	var flier = battle.spawn_unit(_spawn(&"lumern", &"top", &"flier"))
	var frontline = battle.spawn_unit(_spawn(&"veil", &"top", &"shield_guard"))
	var backline = battle.spawn_unit(_spawn(&"veil", &"top", &"archer"))
	flier.lane_position = 0.0
	frontline.lane_position = 25.0
	backline.lane_position = 40.0
	_advance(battle, 40.0)
	return battle


func _giant_battle() -> BattleSimulator:
	var battle := _battle(2105)
	battle.objectives_enabled = false
	var giant = battle.spawn_unit(_spawn(&"lumern", &"bottom", &"giant"))
	giant.lane_position = 50.0
	for position in [51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0]:
		var enemy = battle.spawn_unit(_spawn(&"veil", &"bottom", &"shield_guard"))
		enemy.lane_position = position
	var air = battle.spawn_unit(_spawn(&"veil", &"bottom", &"flier"))
	air.lane_position = 51.5
	_advance(battle, 2.0)
	return battle


func _battle(seed: int) -> BattleSimulator:
	return BattleSimulator.new(_registry(), seed)


func _registry() -> DataRegistry:
	var registry := DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not errors.is_empty():
		push_error("FV registry failed to load: %s" % errors)
	return registry


func _spawn(team_id: StringName, lane_id: StringName, archetype_id: StringName) -> UnitSpawnDefinition:
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = archetype_id
	spawn.owner_team_id = team_id
	spawn.visual_faction_id = team_id
	spawn.lane_id = lane_id
	return spawn


func _advance(battle: BattleSimulator, seconds: float) -> void:
	var steps := int(round(seconds / 0.1))
	for _step in steps:
		battle.advance(0.1)
