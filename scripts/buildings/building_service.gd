class_name BuildingService
extends RefCounted

const BASE_SLOT_CAPACITY := 6
const BuildingDefinitionScript = preload("res://scripts/data/building_definition.gd")
const BuildingStateScript = preload("res://scripts/buildings/building_state.gd")

var economy: Variant
var manifest: Variant
var definitions := {}
var _buildings: Array[BuildingState] = []
var _unlocked_slot_capacity := BASE_SLOT_CAPACITY
var _roster_mutation_allowed := false


func _init(assigned_economy: Variant, assigned_manifest: Variant) -> void:
	economy = assigned_economy
	manifest = assigned_manifest
	definitions = {
		&"barracks": _definition(&"barracks", "일반병 병영", 40, 0, &"warrior", &"shield_guard", 3, &"tier_1", 1, true),
		&"tower": _definition(&"tower", "방어탑", 35, 0, &"", &"", 0, &"tier_1", 0, true),
		&"farm": _definition(&"farm", "농장", 35, 6, &"", &"", 0, &"tier_1", 0, true),
		&"vault": _definition(&"vault", "금고", 0, 0, &"", &"", 0, &"tier_1", 0, false),
		&"special_barracks": _definition(&"special_barracks", "특수병 병영", 0, 0, &"", &"", 0, &"tier_1", 0, false),
		&"command_post": _definition(&"command_post", "지휘소", 0, 0, &"", &"", 0, &"tier_1", 0, false),
		&"mana_tower": _definition(&"mana_tower", "마력탑", 0, 0, &"", &"", 0, &"tier_1", 0, false),
	}


func set_roster_mutation_allowed(allowed: bool) -> void:
	_roster_mutation_allowed = allowed


func roster_mutation_allowed() -> bool:
	return _roster_mutation_allowed


func sync_occupation_capacity(stable_forward_base_count: int, stable_clash_zone_count: int) -> void:
	_unlocked_slot_capacity = BASE_SLOT_CAPACITY + maxi(0, stable_forward_base_count) + maxi(0, stable_clash_zone_count)
	_apply_slot_activity()


func move_roster_entry(from_slot_index: int, to_slot_index: int) -> bool:
	if not _roster_mutation_allowed or from_slot_index < 0 or to_slot_index < 0 or from_slot_index == to_slot_index:
		return false
	if to_slot_index >= _visible_slot_count():
		return false
	var source: BuildingState = _building_at_slot(from_slot_index)
	if source == null:
		return false
	var target: BuildingState = _building_at_slot(to_slot_index)
	source.slot_index = to_slot_index
	if target != null:
		target.slot_index = from_slot_index
	_buildings.sort_custom(func(a: BuildingState, b: BuildingState) -> bool: return a.slot_index < b.slot_index)
	_apply_slot_activity()
	manifest.input_log.append({
		"action": "move_building_roster_entry",
		"from_slot_index": from_slot_index,
		"to_slot_index": to_slot_index,
	})
	return true


func _apply_slot_activity() -> void:
	for state in _buildings:
		var should_be_active := state.slot_index < _unlocked_slot_capacity
		state.state = state.ACTIVE if should_be_active else state.INACTIVE_LOCKED
		_set_effect_active(state, should_be_active)


func unlocked_slot_capacity() -> int:
	return _unlocked_slot_capacity


func try_install(building_id: StringName) -> bool:
	if install_block_reason(building_id) != &"":
		return false
	var definition: BuildingDefinition = definitions[building_id]
	if not economy.try_spend_gold(definition.gold_cost):
		return false
	var state: BuildingState = BuildingStateScript.new(_first_empty_active_slot(), definition)
	_buildings.append(state)
	_buildings.sort_custom(func(a: BuildingState, b: BuildingState) -> bool: return a.slot_index < b.slot_index)
	_set_effect_active(state, true)
	manifest.input_log.append({
		"action": "install_building",
		"slot_index": state.slot_index,
		"building_id": str(building_id),
		"tier_id": str(state.tier_id),
	})
	return true


func install_block_reason(building_id: StringName) -> StringName:
	if not _roster_mutation_allowed:
		return &"stage_locked"
	if not definitions.has(building_id):
		return &"unknown_building"
	var definition: BuildingDefinition = definitions[building_id]
	if not definition.runtime_available:
		return &"research_pending"
	if _first_empty_active_slot() < 0:
		return &"slot_capacity_reached"
	if economy == null or int(economy.gold) < int(definition.gold_cost):
		return &"insufficient_gold"
	return &""


func roster_snapshot() -> Array[Dictionary]:
	var by_slot := {}
	var highest_owned_slot := -1
	for state in _buildings:
		by_slot[state.slot_index] = state
		highest_owned_slot = maxi(highest_owned_slot, state.slot_index)
	var visible_slot_count := maxi(_unlocked_slot_capacity, highest_owned_slot + 1)
	var snapshot: Array[Dictionary] = []
	for slot_index in visible_slot_count:
		var state: Variant = by_slot.get(slot_index)
		if state == null:
			snapshot.append({
				"slot_index": slot_index,
				"state": "empty" if slot_index < _unlocked_slot_capacity else "inactive_locked",
				"building_id": "",
				"display_name": "빈 슬롯",
				"tier_id": "",
				"effect_active": false,
				"locked_reason": "" if slot_index < _unlocked_slot_capacity else "occupation_capacity",
			})
			continue
		var building_state: BuildingState = state
		snapshot.append({
			"slot_index": building_state.slot_index,
			"state": str(building_state.state),
			"building_id": str(building_state.definition.building_id),
			"display_name": building_state.definition.display_name,
			"tier_id": str(building_state.tier_id),
			"effect_active": building_state.effect_active,
			"locked_reason": "" if building_state.state == building_state.ACTIVE else "occupation_capacity",
		})
	return snapshot


func available_definitions_snapshot() -> Array[Dictionary]:
	var building_ids: Array = definitions.keys()
	building_ids.sort_custom(func(a: Variant, b: Variant) -> bool: return str(a) < str(b))
	var result: Array[Dictionary] = []
	for building_id_value in building_ids:
		var definition: BuildingDefinition = definitions[building_id_value]
		result.append({
			"building_id": str(definition.building_id),
			"display_name": definition.display_name,
			"gold_cost": definition.gold_cost,
			"food_cap_bonus": definition.food_cap_bonus,
			"runtime_available": definition.runtime_available,
			"install_block_reason": str(install_block_reason(definition.building_id)),
			"roulette_symbol_id": str(definition.roulette_symbol_id),
			"roulette_board_weight": definition.roulette_board_weight,
			"reward_archetype_id": str(definition.roulette_reward_archetype_id),
		})
	return result


func roulette_token_sources() -> Array[Dictionary]:
	return roulette_token_sources_snapshot()


func roulette_token_sources_snapshot() -> Array[Dictionary]:
	var sources: Array[Dictionary] = []
	for state in _buildings:
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
			"source_building_id": StringName("slot_%d:%s" % [state.slot_index, definition.building_id]),
		})
	return sources


func active_building_count() -> int:
	var count := 0
	for state in _buildings:
		if state.state == state.ACTIVE:
			count += 1
	return count


func _first_empty_active_slot() -> int:
	var occupied := {}
	for state in _buildings:
		occupied[state.slot_index] = true
	for slot_index in _unlocked_slot_capacity:
		if not occupied.has(slot_index):
			return slot_index
	return -1


func _building_at_slot(slot_index: int) -> BuildingState:
	for state in _buildings:
		if state.slot_index == slot_index:
			return state
	return null


func _visible_slot_count() -> int:
	var highest_owned_slot := -1
	for state in _buildings:
		highest_owned_slot = maxi(highest_owned_slot, state.slot_index)
	return maxi(_unlocked_slot_capacity, highest_owned_slot + 1)


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


func _definition(
	building_id: StringName,
	display_name: String,
	gold_cost: int,
	food_cap_bonus: int,
	symbol_id: StringName,
	reward_archetype_id: StringName,
	board_weight: int,
	source_tier_id: StringName,
	source_weight: int,
	runtime_available: bool,
) -> BuildingDefinition:
	var definition := BuildingDefinitionScript.new() as BuildingDefinition
	definition.building_id = building_id
	definition.display_name = display_name
	definition.gold_cost = gold_cost
	definition.food_cap_bonus = food_cap_bonus
	definition.roulette_symbol_id = symbol_id
	definition.roulette_reward_archetype_id = reward_archetype_id
	definition.roulette_board_weight = board_weight
	definition.roulette_source_tier_id = source_tier_id
	definition.roulette_source_weight = source_weight
	definition.runtime_available = runtime_available
	return definition
