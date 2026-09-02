class_name BuildingState
extends RefCounted

const ACTIVE := &"active"
const INACTIVE_LOCKED := &"inactive_locked"

var slot_index := -1
var definition: BuildingDefinition
var tier_id: StringName = &"tier_1"
var state: StringName = ACTIVE
var effect_active := false


func _init(assigned_slot_index: int, assigned_definition: BuildingDefinition, assigned_tier_id: StringName = &"tier_1") -> void:
	slot_index = assigned_slot_index
	definition = assigned_definition
	tier_id = assigned_tier_id
