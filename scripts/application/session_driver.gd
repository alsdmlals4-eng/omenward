class_name SessionDriver
extends Node

var application: Variant


func _ready() -> void:
	set_process(application != null)


func configure(assigned_application: Variant) -> void:
	application = assigned_application
	set_process(application != null)


func _process(delta: float) -> void:
	if application != null:
		application.advance(delta)


func start_stage_deferred(stage_id: StringName) -> void:
	call_deferred("_start_stage", stage_id)


func _start_stage(stage_id: StringName) -> void:
	if application != null:
		application.start_stage(stage_id)
