class_name GateState
extends RefCounted

const MAX_HP := 5000.0
const ARMOR := 80.0
const MAGIC_RESISTANCE := 80.0
const NORMAL_STRUCTURE_MULTIPLIER := 0.4
const SIEGE_STRUCTURE_MULTIPLIER := 2.0
const COLLAPSE_SECONDS := 2.0

var health := MAX_HP
var state := "standing"
var collapse_remaining := 0.0


func apply_damage(raw_damage: float, is_siege: bool, is_magic: bool = false) -> float:
	if state != "standing":
		return 0.0
	var resistance := MAGIC_RESISTANCE if is_magic else ARMOR
	var multiplier := SIEGE_STRUCTURE_MULTIPLIER if is_siege else NORMAL_STRUCTURE_MULTIPLIER
	var damage := raw_damage * multiplier * 100.0 / (100.0 + resistance)
	var applied := minf(health, damage)
	health -= applied
	if health <= 0.0:
		health = 0.0
		state = "collapsing"
		collapse_remaining = COLLAPSE_SECONDS
	return applied


func advance(delta: float) -> void:
	if state != "collapsing":
		return
	collapse_remaining = maxf(0.0, collapse_remaining - delta)
	if collapse_remaining <= 0.000001:
		collapse_remaining = 0.0
		state = "collapsed"


func is_collapsing() -> bool:
	return state == "collapsing"


func is_collapsed() -> bool:
	return state == "collapsed"


func snapshot() -> Dictionary:
	return {"health": health, "state": state, "collapse_remaining": collapse_remaining}
