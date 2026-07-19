class_name StageSelect
extends Control

signal stage_requested(stage_id: StringName)

@onready var _regular_button: Button = $Panel/RegularButton
@onready var _status_label: Label = $Panel/StatusLabel

var _session: Variant


func _ready() -> void:
	_session = get_node_or_null("../../GameSession")
	if _session != null:
		_session.stage_started.connect(_on_stage_started)
	_refresh()


func _on_tutorial_pressed() -> void:
	stage_requested.emit(&"tutorial_stage")
	if _session != null:
		_session.start_stage(&"tutorial_stage")


func _on_regular_pressed() -> void:
	if _session != null and _session.start_stage(&"regular_stage"):
		stage_requested.emit(&"regular_stage")


func _on_stage_started(_stage_id: StringName, _run: Variant) -> void:
	_refresh()
	visible = false


func _refresh() -> void:
	var unlocked: bool = _session != null and bool(_session.progression.regular_unlocked)
	_regular_button.disabled = not unlocked
	_status_label.text = "Regular stage unlocked" if unlocked else "Complete the tutorial to unlock regular"
