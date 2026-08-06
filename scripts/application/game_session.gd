class_name GameSession
extends Node

signal bootstrap_ready(manifest: Variant)
signal bootstrap_failed(errors: PackedStringArray)
signal stage_started(stage_id: StringName, run: Variant)

const PlatformBootstrapScript = preload("res://scripts/application/platform_bootstrap.gd")

var application: Variant
var driver: Variant
var binder: Variant
var _bootstrapper: Variant

var clock: Variant:
	get:
		return application.clock if application != null else null
var registry: Variant:
	get:
		return application.registry if application != null else null
var determinism: Variant:
	get:
		return application.determinism if application != null else null
var validator: Variant:
	get:
		return application.validator if application != null else null
var progression: Variant:
	get:
		return application.progression if application != null else null
var stage_run: Variant:
	get:
		return application.stage_run if application != null else null
var current_stage_id: StringName:
	get:
		return application.current_stage_id if application != null else &"tutorial_stage"


func _init(assigned_bootstrapper: Variant = null) -> void:
	_bootstrapper = assigned_bootstrapper


func _ready() -> void:
	if _bootstrapper == null:
		_bootstrapper = PlatformBootstrapScript.new()
	var composition: Dictionary = _bootstrapper.compose(self)
	application = composition.get("application")
	driver = composition.get("driver")
	binder = composition.get("binder")
	if application == null or driver == null or binder == null:
		var composition_errors := PackedStringArray()
		composition_errors.append("GameSession composition failed")
		bootstrap_failed.emit(composition_errors)
		push_error(composition_errors[0])
		return
	_connect_application_signals()
	var errors: PackedStringArray = application.bootstrap()
	if not errors.is_empty():
		push_error("Phase 2 bootstrap validation failed: %s" % errors)
		return
	driver.start_stage_deferred(&"tutorial_stage")


func start_stage(stage_id: StringName) -> bool:
	if application == null:
		return false
	return application.start_stage(stage_id)


func retry_stage() -> bool:
	if application == null:
		return false
	return application.retry_stage()


func _connect_application_signals() -> void:
	var ready_callback := Callable(self, "_on_bootstrap_ready")
	if not application.bootstrap_ready.is_connected(ready_callback):
		application.bootstrap_ready.connect(ready_callback)
	var failed_callback := Callable(self, "_on_bootstrap_failed")
	if not application.bootstrap_failed.is_connected(failed_callback):
		application.bootstrap_failed.connect(failed_callback)
	var started_callback := Callable(self, "_on_stage_started")
	if not application.stage_started.is_connected(started_callback):
		application.stage_started.connect(started_callback)


func _on_bootstrap_ready(manifest: Variant) -> void:
	bootstrap_ready.emit(manifest)


func _on_bootstrap_failed(errors: PackedStringArray) -> void:
	bootstrap_failed.emit(errors)


func _on_stage_started(stage_id: StringName, run: Variant) -> void:
	stage_started.emit(stage_id, run)
