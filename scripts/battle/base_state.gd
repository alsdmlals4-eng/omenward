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
