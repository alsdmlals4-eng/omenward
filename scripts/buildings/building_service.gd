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
		&"tower": _definition(&"tower", 35, 0, &"shield_guard"),
		&"farm": _definition(&"farm", 35, 6, &"archer"),
	}


func register_outpost(outpost_id: StringName, outpost: Variant, node_ids: Array) -> void:
	_outposts[outpost_id] = outpost
	_nodes[outpost_id] = node_ids.duplicate()


func try_construct(outpost_id: StringName, node_id: StringName, building_id: StringName) -> bool:
	if not definitions.has(building_id) or not _node_is_available(outpost_id, node_id):
		return false
	var definition: Variant = definitions[building_id]
	if not economy.try_spend_gold(definition.gold_cost):
		return false
	var outpost: Variant = _outposts[outpost_id]
	var state: Variant = BuildingStateScript.new(outpost_id, node_id, definition, outpost.capture_revision)
	_buildings[_key(outpost_id, node_id)] = state
	if definition.food_cap_bonus > 0:
		economy.add_food_cap(definition.food_cap_bonus)
	manifest.input_log.append({
		"action": "build",
		"outpost_id": str(outpost_id),
		"node_id": str(node_id),
		"building_id": str(building_id),
	})
	return true


func roulette_archetype_ids() -> Array[StringName]:
	var tokens: Array[StringName] = []
	for key in _buildings:
		var state: Variant = _buildings[key]
		if _outpost_is_active_for_player(state.outpost_id) and _building_matches_current_capture(state):
			tokens.append(state.definition.roulette_archetype_id)
	if tokens.is_empty():
		tokens.append(&"shield_guard")
	return tokens


func _node_is_available(outpost_id: StringName, node_id: StringName) -> bool:
	if not _nodes.has(outpost_id) or not (_nodes[outpost_id] as Array).has(node_id):
		return false
	var key := _key(outpost_id, node_id)
	if _buildings.has(key):
		var state: Variant = _buildings[key]
		if _building_matches_current_capture(state):
			return false
		_buildings.erase(key)
	return _outpost_is_active_for_player(outpost_id)


func _outpost_is_active_for_player(outpost_id: StringName) -> bool:
	if not _outposts.has(outpost_id):
		return false
	var outpost: Variant = _outposts[outpost_id]
	return outpost.owner_team_id == PLAYER_TEAM_ID and outpost.state == outpost.STABLE and not outpost.construction_locked


func _building_matches_current_capture(state: Variant) -> bool:
	if not _outposts.has(state.outpost_id):
		return false
	var outpost: Variant = _outposts[state.outpost_id]
	return state.capture_revision == outpost.capture_revision


func _definition(building_id: StringName, gold_cost: int, food_cap_bonus: int, token_id: StringName) -> Variant:
	var definition: Variant = BuildingDefinitionScript.new()
	definition.building_id = building_id
	definition.gold_cost = gold_cost
	definition.food_cap_bonus = food_cap_bonus
	definition.roulette_archetype_id = token_id
	return definition


func _key(outpost_id: StringName, node_id: StringName) -> String:
	return "%s:%s" % [outpost_id, node_id]
