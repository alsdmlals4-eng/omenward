class_name TitleScreen
extends Control

@onready var _start_expedition_button: Button = $Panel/StartExpeditionButton
@onready var _status_label: Label = $Panel/StatusLabel

var _session: Variant


func _ready() -> void:
	_session = get_node_or_null("../../GameSession")
	if _session != null:
		_connect_signal("bootstrap_ready", Callable(self, "_on_bootstrap_ready"))
		_connect_signal("bootstrap_failed", Callable(self, "_on_bootstrap_failed"))
		_connect_signal("stage_started", Callable(self, "_on_stage_started"))
	_refresh_bootstrap_state()


func _on_start_expedition_pressed() -> void:
	if _session == null or not _session.has_method("begin_tutorial"):
		return
	_start_expedition_button.disabled = true
	_status_label.text = "전선을 준비하는 중..."
	if not bool(_session.begin_tutorial()):
		_refresh_bootstrap_state()


func _on_bootstrap_ready(_manifest: Variant) -> void:
	_refresh_bootstrap_state()


func _on_bootstrap_failed(_errors: PackedStringArray) -> void:
	_refresh_bootstrap_state()


func _on_stage_started(stage_id: StringName, _run: Variant) -> void:
	if stage_id != &"tutorial_stage":
		return
	var run_command_screen := get_node_or_null("../RunCommandScreen") as Control
	if run_command_screen != null:
		run_command_screen.show()
	hide()


func _refresh_bootstrap_state() -> void:
	var is_ready: bool = _session != null and _session.has_method("is_bootstrap_ready") and bool(_session.is_bootstrap_ready())
	_start_expedition_button.disabled = not is_ready
	if is_ready:
		_status_label.text = "징조 정렬 완료 · 단일 전선 원정을 시작할 수 있습니다"
		return
	var failure_message := ""
	if _session != null and _session.has_method("bootstrap_failure_message"):
		failure_message = str(_session.bootstrap_failure_message())
	_status_label.text = "전선을 준비할 수 없습니다: %s" % failure_message if not failure_message.is_empty() else "징조를 정렬하는 중..."


func _connect_signal(signal_name: StringName, callback: Callable) -> void:
	if _session.has_signal(signal_name) and not _session.is_connected(signal_name, callback):
		_session.connect(signal_name, callback)
