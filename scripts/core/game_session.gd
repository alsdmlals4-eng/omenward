class_name GameSession
extends Node

signal bootstrap_ready(manifest: StageManifest)
signal bootstrap_failed(errors: PackedStringArray)

var clock := CombatClock.new()
var registry := DataRegistry.new()
var determinism := DeterminismService.new(1001)
var validator := BootstrapValidator.new()

func _ready() -> void:
	var errors := registry.load_bootstrap_catalog("res://data/bootstrap_catalog.tres")
	errors.append_array(validator.validate_registry(registry))
	if not errors.is_empty():
		bootstrap_failed.emit(errors)
		push_error("Phase 0 bootstrap validation failed: %s" % errors)
		return
	bootstrap_ready.emit(determinism.create_stage_manifest("phase_0", registry.archetype_ids()))
