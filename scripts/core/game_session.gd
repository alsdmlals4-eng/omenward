class_name GameSession
extends Node

const StageRunScript = preload("res://scripts/core/stage_run.gd")
const StageProgressionScript = preload("res://scripts/core/stage_progression.gd")

signal bootstrap_ready(manifest: StageManifest)
signal bootstrap_failed(errors: PackedStringArray)
signal stage_started(stage_id: StringName, run: Variant)

var clock := CombatClock.new()
var registry := DataRegistry.new()
var determinism := DeterminismService.new(1001)
var validator := BootstrapValidator.new()
var progression: Variant = StageProgressionScript.new()
var stage_run: Variant
var current_stage_id: StringName = &"tutorial_stage"

func _ready() -> void:
	var errors := registry.load_bootstrap_catalog("res://data/bootstrap_catalog.tres")
	errors.append_array(validator.validate_registry(registry))
	if not errors.is_empty():
		bootstrap_failed.emit(errors)
		push_error("Phase 0 bootstrap validation failed: %s" % errors)
		return
	stage_run = StageRunScript.new(progression)
	bootstrap_ready.emit(determinism.create_stage_manifest("phase_0", registry.archetype_ids()))
	call_deferred("start_stage", &"tutorial_stage")


func _process(delta: float) -> void:
	if stage_run != null:
		stage_run.advance(delta)


func start_stage(stage_id: StringName) -> bool:
	var stage := registry.stage_definition(stage_id)
	if stage == null or not progression.can_start(stage):
		return false
	current_stage_id = stage_id
	stage_run.start(stage, determinism.seed)
	var battlefield := get_parent().get_node_or_null("Battlefield")
	if battlefield != null:
		battlefield.bind_run(stage_run)
	var stage_hud := get_parent().get_node_or_null("UI/StageHud")
	if stage_hud != null:
		stage_hud.bind_run(stage_run)
	stage_started.emit(stage_id, stage_run)
	return stage_run.result_state == StageRunScript.RUNNING


func retry_stage() -> bool:
	return start_stage(current_stage_id)
