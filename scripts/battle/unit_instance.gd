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
var role := ""
var counter_tags: PackedStringArray = PackedStringArray()
var target_priority_tags: PackedStringArray = PackedStringArray()

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
	role = profile.role if profile != null else "unknown"
	counter_tags = PackedStringArray(profile.counter_tags) if profile != null else PackedStringArray()
	target_priority_tags = PackedStringArray(profile.target_priority_tags) if profile != null else PackedStringArray(["nearest"])
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
	var distance := position - lane_position
	var step := float(_stats.get("move_speed", 0.0)) * delta
	if absf(distance) <= step:
		lane_position = position
	else:
		lane_position += signf(distance) * step


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
	return receive_damage_with_channel(raw_damage, &"physical")


func receive_damage_with_channel(raw_damage: float, channel: StringName) -> float:
	var resistance_key := "armor" if channel == &"physical" else "magic_resistance" if channel == &"magic" else ""
	if resistance_key.is_empty():
		push_error("unknown damage channel: %s" % channel)
		return 0.0
	var mitigated := raw_damage * 100.0 / (100.0 + float(_stats.get(resistance_key, 0.0)))
	health = maxf(0.0, health - mitigated)
	if health <= 0.0:
		state = "dead"
		target_unit_id = -1
	return mitigated


func receive_heal(raw_heal: float) -> Dictionary:
	var maximum := float(_stats.get("max_health", 0.0))
	var effective := minf(maxf(0.0, raw_heal), maxf(0.0, maximum - health))
	health += effective
	return {
		"raw_heal": maxf(0.0, raw_heal),
		"effective_heal": effective,
		"overheal": maxf(0.0, raw_heal) - effective,
	}


func is_siege_damage() -> bool:
	return structure_damage_tags.has("siege")


func tactical_snapshot() -> Dictionary:
	return {
		"unit_id": unit_id,
		"archetype_id": str(archetype_id),
		"owner_team_id": str(owner_team_id),
		"lane_id": str(lane_id),
		"role": role,
		"attack_range": float(_stats.get("attack_range", 0.0)),
		"target_unit_id": target_unit_id,
		"counter_tags": Array(counter_tags),
		"target_priority_tags": Array(target_priority_tags),
		"state": state,
		"health": health,
	}


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
		"role": role,
		"counter_tags": Array(counter_tags),
		"target_priority_tags": Array(target_priority_tags),
		"attack_range": float(_stats.get("attack_range", 0.0)),
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
