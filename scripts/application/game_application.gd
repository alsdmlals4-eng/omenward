class_name GameApplication
extends RefCounted

signal bootstrap_ready(manifest: Variant)
signal bootstrap_failed(errors: PackedStringArray)
signal stage_started(stage_id: StringName, run: Variant)

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const COMBAT_CLOCK_PATH := "res://scripts/core/combat_clock.gd"
const DATA_REGISTRY_PATH := "res://scripts/core/data_registry.gd"
const DETERMINISM_SERVICE_PATH := "res://scripts/core/determinism_service.gd"
const BOOTSTRAP_VALIDATOR_PATH := "res://scripts/core/bootstrap_validator.gd"
const STAGE_PROGRESSION_PATH := "res://scripts/core/stage_progression.gd"
const STAGE_RUN_PATH := "res://scripts/core/stage_run.gd"
const DEFAULT_SEED := 1001
const RUNNING := &"running"

var clock: Variant
var registry: Variant
var determinism: Variant
var validator: Variant
var progression: Variant
var stage_run: Variant
var current_stage_id: StringName = &"tutorial_stage"

var _stage_run_factory: Callable


func _init(dependencies: Dictionary = {}) -> void:
	clock = dependencies.get("clock")
	registry = dependencies.get("registry")
	determinism = dependencies.get("determinism")
	validator = dependencies.get("validator")
	progression = dependencies.get("progression")
	var factory: Variant = dependencies.get("stage_run_factory", Callable())
	_stage_run_factory = factory if factory is Callable else Callable()


func bootstrap() -> PackedStringArray:
	_ensure_default_dependencies()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	errors.append_array(validator.validate_registry(registry))
	if not errors.is_empty():
		stage_run = null
		bootstrap_failed.emit(errors)
		return errors
	stage_run = _create_stage_run()
	bootstrap_ready.emit(determinism.create_stage_manifest("phase_0", registry.archetype_ids()))
	return errors


func start_stage(stage_id: StringName) -> bool:
	if stage_run == null:
		return false
	var stage: Variant = registry.stage_definition(stage_id)
	if stage == null or not progression.can_start(stage):
		return false
	current_stage_id = stage_id
	stage_run.start(stage, determinism.seed)
	stage_started.emit(stage_id, stage_run)
	return stage_run.result_state == RUNNING


func retry_stage() -> bool:
	return start_stage(current_stage_id)


func advance(delta: float) -> void:
	if stage_run != null:
		stage_run.advance(delta)


func _ensure_default_dependencies() -> void:
	if clock == null:
		clock = load(COMBAT_CLOCK_PATH).new()
	if registry == null:
		registry = load(DATA_REGISTRY_PATH).new()
	if determinism == null:
		determinism = load(DETERMINISM_SERVICE_PATH).new(DEFAULT_SEED)
	if validator == null:
		validator = load(BOOTSTRAP_VALIDATOR_PATH).new()
	if progression == null:
		progression = load(STAGE_PROGRESSION_PATH).new()


func _create_stage_run() -> Variant:
	if _stage_run_factory.is_valid():
		return _stage_run_factory.call(progression)
	return load(STAGE_RUN_PATH).new(progression)
