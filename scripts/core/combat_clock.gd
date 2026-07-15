class_name CombatClock
extends RefCounted

var active_combat_seconds := 0.0
var ui_planning_seconds := 0.0
var is_planning := true

func advance(delta: float) -> void:
	if is_planning:
		ui_planning_seconds += delta
	else:
		active_combat_seconds += delta
