class_name BuildingService
extends RefCounted

const PLAYER_TEAM_ID := &"lumern"
const BuildingDefinitionScript = preload("res://scripts/data/building_definition.gd")
const BuildingStateScript = preload("res://scripts/buildings/building_state.gd")

var economy: Variant
var manifest: Variant
var definitions := {}
var _outposts := {}
var _nodes := {}
var _buildings := {}


func _init(assigned_economy: Variant, assigned_manifest: Variant) -> void:
	economy = assigned_economy
	manifest = assigned_manifest
	definitions = {
		&"barracks": _definition(&"barracks", 40, 0, &"warrior", &"shield_guard", 3, &"tier_1", 1),
		&"tower": _definition(&"tower", 35, 0, &"", &"", 0, &"tier_1", 0),
		&"farm": _definition(&"farm", 35, 6, &"", &"", 0, &"tier_1", 0),
	}


func register_outpost(outpost_id: StringName, outpost: Variant, node_ids: Array) -> void:
	_outposts[outpost_id] = outpost
	_nodes[outpost_id] = node_ids.duplicate()


func try_construct(outpost_id: StringName, node_id: StringName, building_id: StringName) -> bool:
	sync_outpost_states()
	if not definitions.has(building_id) or not _node_is_available(outpost_id, node_id):
		return false
	var definition: BuildingDefinition = definitions[building_id]
	if not economy.try_spend_gold(definition.gold_cost):
		return false
	var outpost: Variant = _outposts[outpost_id]
	var state: BuildingState = BuildingStateScript.new(outpost_id, node_id, definition, outpost.capture_revision)
	_buildings[_key(outpost_id, node_id)] = state
	_set_effect_active(state, true)
	manifest.input_log.append({
		"action": "build",
		"outpost_id": str(outpost_id),
		"node_id": str(node_id),
		"building_id": str(building_id),
	})
	return true


func sync_outpost_states() -> void:
	var keys: Array = _buildings.keys()
	keys.sort()
	for key in keys:
		var state: BuildingState = _buildings[key]
		if not _outposts.has(state.outpost_id):
			_ruin(state)
			continue
		var outpost: Variant = _outposts[state.outpost_id]
		if state.capture_revision != outpost.capture_revision:
			_ruin(state)
			continue
		var should_be_active: bool = outpost.owner_team_id == PLAYER_TEAM_ID
		state.state = state.ACTIVE if should_be_active else state.DISABLED
		_set_effect_active(state, should_be_active)


func roulette_token_sources() -> Array[Dictionary]:
	sync_outpost_states()
	return roulette_token_sources_snapshot()


func roulette_token_sources_snapshot() -> Array[Dictionary]:
	var sources: Array[Dictionary] = []
	var keys: Array = _buildings.keys()
	keys.sort()
	for key in keys:
		var state: BuildingState = _buildings[key]
		var definition: BuildingDefinition = state.definition
		if state.state != state.ACTIVE or not state.effect_active:
			continue
		if definition.roulette_symbol_id == &"" or definition.roulette_board_weight <= 0:
			continue
		sources.append({
			"symbol_id": definition.roulette_symbol_id,
			"reward_archetype_id": definition.roulette_reward_archetype_id,
			"board_weight": definition.roulette_board_weight,
			"source_tier_id": definition.roulette_source_tier_id,
			"source_weight": definition.roulette_source_weight,
			"source_building_id": StringName(str(key)),
		})
	return sources


func building_state(outpost_id: StringName, node_id: StringName) -> Variant:
	sync_outpost_states()
	return building_state_snapshot(outpost_id, node_id)


func building_state_snapshot(outpost_id: StringName, node_id: StringName) -> Variant:
	return _buildings.get(_key(outpost_id, node_id))


func active_building_count() -> int:
	sync_outpost_states()
	var count := 0
	for state: BuildingState in _buildings.values():
		if state.state == state.ACTIVE:
			count += 1
	return count


func _node_is_available(outpost_id: StringName, node_id: StringName) -> bool:
	if not _nodes.has(outpost_id) or not (_nodes[outpost_id] as Array).has(node_id):
		return false
	var key := _key(outpost_id, node_id)
	if _buildings.has(key):
		var state: BuildingState = _buildings[key]
		if state.state != state.RUINED:
			return false
		_buildings.erase(key)
	return _outpost_is_buildable_for_player(outpost_id)


func _outpost_is_buildable_for_player(outpost_id: StringName) -> bool:
	if not _outposts.has(outpost_id):
		return false
	var outpost: Variant = _outposts[outpost_id]
	return outpost.owner_team_id == PLAYER_TEAM_ID and outpost.state == outpost.STABLE and not outpost.construction_locked


func _set_effect_active(state: BuildingState, active: bool) -> void:
	if state.effect_active == active:
		return
	state.effect_active = active
	if state.definition.food_cap_bonus <= 0:
		return
	if active:
		economy.add_food_cap(state.definition.food_cap_bonus)
	else:
		economy.remove_food_cap(state.definition.food_cap_bonus)


func _ruin(state: BuildingState) -> void:
	_set_effect_active(state, false)
	state.state = state.RUINED


func _definition(
	building_id: StringName,
	gold_cost: int,
	food_cap_bonus: int,
	symbol_id: StringName,
	reward_archetype_id: StringName,
	board_weight: int,
	source_tier_id: StringName,
	source_weight: int,
) -> BuildingDefinition:
	var definition := BuildingDefinitionScript.new() as BuildingDefinition
	definition.building_id = building_id
	definition.gold_cost = gold_cost
	definition.food_cap_bonus = food_cap_bonus
	definition.roulette_symbol_id = symbol_id
	definition.roulette_reward_archetype_id = reward_archetype_id
	definition.roulette_board_weight = board_weight
	definition.roulette_source_tier_id = source_tier_id
	definition.roulette_source_weight = source_weight
	return definition


func _key(outpost_id: StringName, node_id: StringName) -> String:
	return "%s:%s" % [outpost_id, node_id]
