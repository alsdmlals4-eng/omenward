class_name BuildingState
extends RefCounted

var outpost_id: StringName
var node_id: StringName
var definition: BuildingDefinition
var capture_revision: int


func _init(assigned_outpost_id: StringName, assigned_node_id: StringName, assigned_definition: BuildingDefinition, assigned_capture_revision: int) -> void:
	outpost_id = assigned_outpost_id
	node_id = assigned_node_id
	definition = assigned_definition
	capture_revision = assigned_capture_revision
