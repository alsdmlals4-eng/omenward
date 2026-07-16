class_name UnitInstance
extends RefCounted

const BASE_STATS := {
	"shield_guard": {"max_health": 180.0, "attack": 12.0, "armor": 24.0, "magic_resistance": 16.0, "move_speed": 1.0, "attack_range": 1.0},
	"greatsword_warrior": {"max_health": 155.0, "attack": 20.0, "armor": 14.0, "magic_resistance": 10.0, "move_speed": 1.0, "attack_range": 1.0},
	"assassin": {"max_health": 110.0, "attack": 24.0, "armor": 8.0, "magic_resistance": 12.0, "move_speed": 1.4, "attack_range": 1.0},
	"spear_guard": {"max_health": 145.0, "attack": 16.0, "armor": 16.0, "magic_resistance": 12.0, "move_speed": 1.0, "attack_range": 1.5},
	"archer": {"max_health": 95.0, "attack": 18.0, "armor": 6.0, "magic_resistance": 8.0, "move_speed": 1.0, "attack_range": 4.0},
	"cavalry": {"max_health": 165.0, "attack": 19.0, "armor": 18.0, "magic_resistance": 10.0, "move_speed": 1.6, "attack_range": 1.0},
	"priest": {"max_health": 105.0, "attack": 10.0, "armor": 7.0, "magic_resistance": 18.0, "move_speed": 1.0, "attack_range": 3.0},
	"mage": {"max_health": 100.0, "attack": 22.0, "armor": 5.0, "magic_resistance": 20.0, "move_speed": 1.0, "attack_range": 3.0},
	"flier": {"max_health": 120.0, "attack": 17.0, "armor": 10.0, "magic_resistance": 12.0, "move_speed": 1.3, "attack_range": 1.5},
	"giant": {"max_health": 320.0, "attack": 34.0, "armor": 30.0, "magic_resistance": 20.0, "move_speed": 0.7, "attack_range": 1.5},
}

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
	_stats = _build_combat_stats(registry)
	health = float(_stats["max_health"])
	_load_attack_timing(registry)


func combat_stats() -> Dictionary:
	return _stats.duplicate()


func is_alive() -> bool:
	return health > 0.0


func distance_to(other: UnitInstance) -> float:
	return absf(lane_position - other.lane_position)


func move_toward(other: UnitInstance, delta: float) -> void:
	state = "move"
	var direction := signf(other.lane_position - lane_position)
	lane_position += direction * float(_stats["move_speed"]) * delta


func advance_attack(delta: float) -> float:
	if state == "idle" or state == "move":
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
		return float(_stats["attack"])
	if state == "attack_recovery":
		cooldown_remaining -= delta
		if cooldown_remaining <= 0.0:
			state = "idle"
		return 0.0
	return 0.0


func receive_damage(raw_damage: float) -> float:
	var mitigated := raw_damage * 100.0 / (100.0 + float(_stats["armor"]))
	health = maxf(0.0, health - mitigated)
	if health <= 0.0:
		state = "dead"
		target_unit_id = -1
	return mitigated


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
	}


func _build_combat_stats(registry: DataRegistry) -> Dictionary:
	var base: Dictionary = BASE_STATS.get(str(archetype_id), {})
	if base.is_empty():
		push_error("unknown shared archetype: %s" % archetype_id)
		return {}
	var multiplier := _tier_multiplier(registry) * _rank_multiplier(registry)
	var result := {}
	for key in base:
		result[key] = float(base[key]) * multiplier
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
