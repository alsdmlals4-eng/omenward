class_name SceneBinder
extends Node

var application: Variant
var host: Node


func configure(assigned_application: Variant, assigned_host: Node) -> void:
	var callback := Callable(self, "_on_stage_started")
	if application != null and application.stage_started.is_connected(callback):
		application.stage_started.disconnect(callback)
	application = assigned_application
	host = assigned_host
	if application != null and not application.stage_started.is_connected(callback):
		application.stage_started.connect(callback)


func _on_stage_started(_stage_id: StringName, run: Variant) -> void:
	if host == null:
		return
	var scene_root := host.get_parent()
	if scene_root == null:
		return
	var stage_hud := scene_root.get_node_or_null("UI/StageHud")
	if stage_hud != null and stage_hud.has_method("bind_run"):
		stage_hud.bind_run(run)
	var run_command_screen := scene_root.get_node_or_null("UI/RunCommandScreen")
	if run_command_screen != null and run_command_screen.has_method("bind_run"):
		run_command_screen.bind_run(run)
