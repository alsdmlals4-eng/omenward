from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.lstrip("\n"), encoding="utf-8", newline="\n")


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one occurrence, found {count}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


write("scripts/data/unit_archetype_profile.gd", r'''
class_name UnitArchetypeProfile
extends Resource

@export var archetype_id: StringName
@export var display_name: String
@export var role: String
@export var base_stats: Dictionary = {}
@export_range(0.0, 2.0, 0.05) var capture_power: float = 1.0
@export var structure_damage_tags: PackedStringArray = PackedStringArray(["normal"])
@export var attack_profile_id: StringName
@export var animation_contract_id: StringName
''')

unit_profiles = {
    "shield_guard": (1.25, "normal"),
    "greatsword_warrior": (1.0, "normal"),
    "assassin": (0.0, "normal"),
    "spear_guard": (1.0, "normal"),
    "archer": (0.5, "normal"),
    "cavalry": (1.0, "normal"),
    "priest": (0.5, "normal"),
    "mage": (0.5, "normal"),
    "flier": (0.0, "normal"),
    "giant": (0.5, "siege"),
}
for archetype_id, (capture_power, damage_tag) in unit_profiles.items():
    path = ROOT / f"data/units/{archetype_id}.tres"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\ncapture_power = [^\n]+", "", text)
    text = re.sub(r"\nstructure_damage_tags = [^\n]+", "", text)
    marker = "\nattack_profile_id = "
    if text.count(marker) != 1:
        raise RuntimeError(f"{path}: attack profile marker mismatch")
    insert = f"\ncapture_power = {capture_power:.2f}\nstructure_damage_tags = PackedStringArray(\"{damage_tag}\")"
    path.write_text(text.replace(marker, insert + marker, 1), encoding="utf-8", newline="\n")

write("scripts/battle/base_state.gd", r'''
class_name BaseState
extends RefCounted

const GateStateScript = preload("res://scripts/battle/gate_state.gd")

const STANDING := &"standing"
const DESTROYED := &"destroyed"

var max_health: float
var health: float
var state: StringName = STANDING
var damage_profile_source: StringName = &"approved_gate_fallback"


func _init(assigned_max_health: float = 0.0) -> void:
	max_health = assigned_max_health if assigned_max_health > 0.0 else GateStateScript.MAX_HP
	health = max_health


func apply_damage(raw_damage: float, is_siege: bool, is_magic: bool = false) -> float:
	if state != STANDING or raw_damage <= 0.0:
		return 0.0
	var resistance: float = GateStateScript.MAGIC_RESISTANCE if is_magic else GateStateScript.ARMOR
	var multiplier: float = GateStateScript.SIEGE_STRUCTURE_MULTIPLIER if is_siege else GateStateScript.NORMAL_STRUCTURE_MULTIPLIER
	var damage: float = raw_damage * multiplier * 100.0 / (100.0 + resistance)
	var applied: float = minf(health, damage)
	health -= applied
	if health <= 0.000001:
		health = 0.0
		state = DESTROYED
	return applied


func is_destroyed() -> bool:
	return state == DESTROYED


func snapshot() -> Dictionary:
	return {
		"max_health": max_health,
		"health": health,
		"state": str(state),
		"damage_profile_source": str(damage_profile_source),
	}
''')

write("scripts/battle/outpost_state.gd", r'''
class_name OutpostState
extends RefCounted

const NEUTRALIZING := "neutralizing"
const CAPTURING := "capturing"
const STABILIZING := "stabilizing"
const STABLE := "stable"
const MAX_CAPTURE_POWER := 2.0
const HOLD_SECONDS := 3.0
const NEUTRALIZE_SECONDS := 10.0
const CAPTURE_SECONDS := 10.0
const STABILIZE_SECONDS := 5.0
const CAPTURE_PROGRESS_REVERT_PER_SECOND := 0.1

var owner_team_id: StringName
var capturing_team_id: StringName
var state := STABLE
var capture_power := 0.0
var capture_progress := 0.0
var construction_locked := false
var existing_buildings_enabled := true
var prior_building_ruined := false
var capture_revision := 0
var contested := false

var _hold_remaining := 0.0
var _phase_remaining := 0.0
var _is_reverting := false
var _previous_owner_team_id: StringName
var _previous_existing_buildings_enabled := true
var _previous_prior_building_ruined := false


func _init(initial_owner_team_id: StringName = &"", has_existing_building: bool = false) -> void:
	owner_team_id = initial_owner_team_id
	existing_buildings_enabled = has_existing_building


func begin_capture(team_id: StringName, power: float) -> bool:
	var normalized_power := _normalize_capture_power(power)
	if team_id == &"" or team_id == owner_team_id or state == STABILIZING or normalized_power <= 0.0:
		return false
	if (state == NEUTRALIZING or state == CAPTURING) and capturing_team_id == team_id:
		set_capture_power(normalized_power)
		return true
	if state != STABLE:
		return false
	capturing_team_id = team_id
	capture_power = normalized_power
	capture_progress = 1.0 if owner_team_id == &"" else 0.0
	_previous_owner_team_id = owner_team_id
	_previous_existing_buildings_enabled = existing_buildings_enabled
	_previous_prior_building_ruined = prior_building_ruined
	construction_locked = true
	contested = false
	_hold_remaining = 0.0
	_is_reverting = false
	_sync_capture_phase()
	return true


func set_capture_power(power: float) -> void:
	if state != NEUTRALIZING and state != CAPTURING:
		return
	var previous_power := capture_power
	capture_power = _normalize_capture_power(power)
	contested = false
	if previous_power > 0.0 and capture_power <= 0.0:
		_hold_remaining = HOLD_SECONDS
		_is_reverting = false
	elif capture_power > 0.0:
		_hold_remaining = 0.0
		_is_reverting = false


func set_contested() -> void:
	if state != NEUTRALIZING and state != CAPTURING:
		return
	capture_power = 0.0
	contested = true
	_hold_remaining = 0.0
	_is_reverting = false


func clear_capture_presence() -> void:
	if state != NEUTRALIZING and state != CAPTURING:
		return
	var had_presence := capture_power > 0.0 or contested
	capture_power = 0.0
	contested = false
	if had_presence:
		_hold_remaining = HOLD_SECONDS
		_is_reverting = false


func advance(delta: float) -> void:
	var remaining := maxf(0.0, delta)
	while remaining > 0.000001:
		if state == STABILIZING:
			var stabilized := minf(remaining, _phase_remaining)
			_phase_remaining -= stabilized
			remaining -= stabilized
			if _phase_remaining <= 0.000001:
				_phase_remaining = 0.0
				state = STABLE
				construction_locked = false
			continue
		if contested:
			return
		if capture_power > 0.0:
			var boundary := 1.0 if capture_progress < 1.0 else 2.0
			var phase_seconds := NEUTRALIZE_SECONDS if capture_progress < 1.0 else CAPTURE_SECONDS
			var seconds_to_boundary := (boundary - capture_progress) * phase_seconds / capture_power
			var progressed := minf(remaining, seconds_to_boundary)
			capture_progress += progressed * capture_power / phase_seconds
			remaining -= progressed
			if capture_progress >= 2.0 - 0.000001:
				_complete_capture()
				continue
			if capture_progress >= boundary - 0.000001:
				capture_progress = boundary
				_sync_capture_phase()
				continue
			_sync_capture_phase()
			continue
		if _hold_remaining > 0.0:
			var held := minf(remaining, _hold_remaining)
			_hold_remaining -= held
			remaining -= held
			if _hold_remaining <= 0.000001:
				_hold_remaining = 0.0
				_is_reverting = true
			continue
		if _is_reverting:
			var reversion_seconds := capture_progress / CAPTURE_PROGRESS_REVERT_PER_SECOND
			var reverted := minf(remaining, reversion_seconds)
			capture_progress -= reverted * CAPTURE_PROGRESS_REVERT_PER_SECOND
			remaining -= reverted
			if capture_progress <= 0.000001:
				_restore_previous_stable_state()
				return
			_sync_capture_phase()
			continue
		return


func is_stable_for(team_id: StringName) -> bool:
	return state == STABLE and owner_team_id == team_id


func previous_owner_team_id() -> StringName:
	return _previous_owner_team_id


func _complete_capture() -> void:
	capture_progress = 2.0
	owner_team_id = capturing_team_id
	capturing_team_id = &""
	capture_power = 0.0
	prior_building_ruined = true
	capture_revision += 1
	existing_buildings_enabled = false
	contested = false
	state = STABILIZING
	_phase_remaining = STABILIZE_SECONDS
	_hold_remaining = 0.0
	_is_reverting = false


func _restore_previous_stable_state() -> void:
	owner_team_id = _previous_owner_team_id
	capturing_team_id = &""
	capture_power = 0.0
	capture_progress = 0.0
	construction_locked = false
	existing_buildings_enabled = _previous_existing_buildings_enabled
	prior_building_ruined = _previous_prior_building_ruined
	contested = false
	state = STABLE
	_hold_remaining = 0.0
	_phase_remaining = 0.0
	_is_reverting = false


func _sync_capture_phase() -> void:
	if capture_progress < 1.0:
		state = NEUTRALIZING
		owner_team_id = _previous_owner_team_id
		existing_buildings_enabled = _previous_existing_buildings_enabled
		_phase_remaining = (1.0 - capture_progress) * NEUTRALIZE_SECONDS
		return
	state = CAPTURING
	owner_team_id = &""
	existing_buildings_enabled = false
	_phase_remaining = (2.0 - capture_progress) * CAPTURE_SECONDS


func _normalize_capture_power(power: float) -> float:
	return clampf(power, 0.0, MAX_CAPTURE_POWER)


func snapshot() -> Dictionary:
	return {
		"owner_team_id": str(owner_team_id),
		"capturing_team_id": str(capturing_team_id),
		"state": state,
		"capture_power": capture_power,
		"capture_progress": capture_progress,
		"construction_locked": construction_locked,
		"existing_buildings_enabled": existing_buildings_enabled,
		"prior_building_ruined": prior_building_ruined,
		"capture_revision": capture_revision,
		"contested": contested,
		"hold_remaining": _hold_remaining,
		"phase_remaining": _phase_remaining,
	}
''')

write("scripts/buildings/building_state.gd", r'''
class_name BuildingState
extends RefCounted

const ACTIVE := &"active"
const DISABLED := &"disabled"
const RUINED := &"ruined"

var outpost_id: StringName
var node_id: StringName
var definition: BuildingDefinition
var capture_revision: int
var state: StringName = ACTIVE
var effect_active := false


func _init(assigned_outpost_id: StringName, assigned_node_id: StringName, assigned_definition: BuildingDefinition, assigned_capture_revision: int) -> void:
	outpost_id = assigned_outpost_id
	node_id = assigned_node_id
	definition = assigned_definition
	capture_revision = assigned_capture_revision
''')

replace_once(
    "scripts/core/stage_economy.gd",
    "func add_food_cap(amount: int) -> void:\n\tfood_cap += maxi(0, amount)\n\n\nfunc try_reserve_food",
    "func add_food_cap(amount: int) -> void:\n\tfood_cap += maxi(0, amount)\n\n\nfunc remove_food_cap(amount: int) -> void:\n\tfood_cap = maxi(0, food_cap - maxi(0, amount))\n\n\nfunc try_reserve_food",
)

write("scripts/buildings/building_service.gd", r'''
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
		var should_be_active := outpost.owner_team_id == PLAYER_TEAM_ID
		state.state = state.ACTIVE if should_be_active else state.DISABLED
		_set_effect_active(state, should_be_active)


func roulette_token_sources() -> Array[Dictionary]:
	sync_outpost_states()
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
''')

write("scripts/battle/unit_instance.gd", r'''
class_name UnitInstance
extends RefCounted

var unit_id := 0
var archetype_id: StringName
var tier_id: StringName
var rank_id: StringName
var owner_team_id: StringName
var visual_faction_id: StringName
var lane_id: StringName
var lane_position := 0.0
var target_unit_id := -1
var state := "idle"
var health := 0.0
var cooldown_remaining := 0.0
var deterministic_animation_offset := 0
var capture_power := 0.0
var structure_damage_tags: PackedStringArray = PackedStringArray()

var _stats := {}
var _preparation_seconds := 0.1
var _hit_seconds := 0.1
var _recovery_seconds := 0.1


func _init(spawn: UnitSpawnDefinition, registry: DataRegistry, assigned_unit_id: int, animation_offset: int) -> void:
	unit_id = assigned_unit_id
	archetype_id = spawn.archetype_id
	tier_id = spawn.tier_id
	rank_id = spawn.rank_id
	owner_team_id = spawn.owner_team_id
	visual_faction_id = spawn.visual_faction_id
	lane_id = spawn.lane_id
	lane_position = 0.0 if owner_team_id == &"lumern" else 100.0
	deterministic_animation_offset = animation_offset
	var profile: UnitArchetypeProfile = registry.archetypes.get(str(archetype_id)) as UnitArchetypeProfile
	_stats = _build_combat_stats(profile, registry)
	capture_power = clampf(float(profile.capture_power), 0.0, 2.0) if profile != null else 0.0
	structure_damage_tags = PackedStringArray(profile.structure_damage_tags) if profile != null else PackedStringArray(["normal"])
	health = float(_stats.get("max_health", 0.0))
	_load_attack_timing(registry)


func combat_stats() -> Dictionary:
	return _stats.duplicate()


func is_alive() -> bool:
	return health > 0.0


func distance_to(other: UnitInstance) -> float:
	return absf(lane_position - other.lane_position)


func distance_to_position(position: float) -> float:
	return absf(lane_position - position)


func move_toward(other: UnitInstance, delta: float) -> void:
	move_toward_position(other.lane_position, delta)


func move_toward_position(position: float, delta: float) -> void:
	state = "move"
	var direction := signf(position - lane_position)
	lane_position += direction * float(_stats.get("move_speed", 0.0)) * delta


func advance_attack(delta: float) -> float:
	if not is_alive():
		return 0.0
	if state != "attack_preparation" and state != "attack_hit" and state != "attack_recovery":
		state = "attack_preparation"
		cooldown_remaining = _preparation_seconds
		return 0.0
	if state == "attack_preparation":
		cooldown_remaining -= delta
		if cooldown_remaining <= 0.0:
			state = "attack_hit"
			cooldown_remaining = _hit_seconds
		return 0.0
	if state == "attack_hit":
		state = "attack_recovery"
		cooldown_remaining = _recovery_seconds
		return float(_stats.get("attack", 0.0))
	if state == "attack_recovery":
		cooldown_remaining -= delta
		if cooldown_remaining <= 0.0:
			state = "idle"
		return 0.0
	return 0.0


func receive_damage(raw_damage: float) -> float:
	var mitigated := raw_damage * 100.0 / (100.0 + float(_stats.get("armor", 0.0)))
	health = maxf(0.0, health - mitigated)
	if health <= 0.0:
		state = "dead"
		target_unit_id = -1
	return mitigated


func is_siege_damage() -> bool:
	return structure_damage_tags.has("siege")


func to_snapshot() -> Dictionary:
	return {
		"unit_id": unit_id,
		"archetype_id": str(archetype_id),
		"tier_id": str(tier_id),
		"rank_id": str(rank_id),
		"owner_team_id": str(owner_team_id),
		"visual_faction_id": str(visual_faction_id),
		"lane_id": str(lane_id),
		"lane_position": lane_position,
		"target_unit_id": target_unit_id,
		"state": state,
		"health": health,
		"cooldown_remaining": cooldown_remaining,
		"deterministic_animation_offset": deterministic_animation_offset,
		"capture_power": capture_power,
		"structure_damage_tags": Array(structure_damage_tags),
	}


func _build_combat_stats(profile: UnitArchetypeProfile, registry: DataRegistry) -> Dictionary:
	if profile == null or profile.base_stats.is_empty():
		push_error("unknown shared archetype: %s" % archetype_id)
		return {}
	var multiplier := _tier_multiplier(registry) * _rank_multiplier(registry)
	var result := {}
	for key in profile.base_stats:
		result[key] = float(profile.base_stats[key]) * multiplier
	return result


func _tier_multiplier(registry: DataRegistry) -> float:
	for profile in registry.catalog.tier_profiles:
		if profile.tier_id == tier_id:
			return profile.stat_multiplier
	return 1.0


func _rank_multiplier(registry: DataRegistry) -> float:
	for profile in registry.catalog.rank_profiles:
		if profile.rank_id == rank_id:
			return profile.stat_multiplier
	return 1.0


func _load_attack_timing(registry: DataRegistry) -> void:
	for profile in registry.catalog.attack_profiles:
		if profile.profile_id == archetype_id:
			_preparation_seconds = float(profile.preparation_ms) / 1000.0
			_hit_seconds = float(profile.hit_ms) / 1000.0
			_recovery_seconds = float(profile.recovery_ms) / 1000.0
			return
''')

replace_once("scripts/core/stage_manifest.gd", "var starting_food_cap: int\nvar tutorial_stage := false", "var starting_food_cap: int\nvar base_max_health: float = 0.0\nvar tutorial_stage := false")
replace_once("scripts/core/stage_manifest.gd", '"starting_food_cap": starting_food_cap,\n\t\t"starting_gold": starting_gold,', '"starting_food_cap": starting_food_cap,\n\t\t"starting_gold": starting_gold,\n\t\t"base_max_health": base_max_health,')
replace_once("scripts/data/stage_definition.gd", "@export var starting_food_cap := 12\n@export var tutorial_stage := false", "@export var starting_food_cap := 12\n@export var base_max_health: float = 0.0\n@export var tutorial_stage := false")
replace_once("scripts/data/stage_definition.gd", "manifest.starting_food_cap = starting_food_cap\n\tmanifest.tutorial_stage = tutorial_stage", "manifest.starting_food_cap = starting_food_cap\n\tmanifest.base_max_health = base_max_health\n\tmanifest.tutorial_stage = tutorial_stage")

# The large battle and stage runtime files are generated by the companion runtime-body applicator.
self_path = ROOT / "tools/_apply_c2_runtime.py"
if self_path.exists():
    self_path.unlink()
