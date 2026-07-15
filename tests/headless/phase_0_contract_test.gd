extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const DeterminismService = preload("res://scripts/core/determinism_service.gd")
const BootstrapValidator = preload("res://scripts/core/bootstrap_validator.gd")


func _init() -> void:
	var registry: Variant = DataRegistry.new()
	var errors: Variant = registry.load_bootstrap_catalog("res://data/bootstrap_catalog.tres")
	var failures := PackedStringArray()
	_expect(errors.is_empty(), "bootstrap catalog must load: %s" % errors, failures)
	_expect(registry.archetypes.size() == 10, "exactly ten shared archetypes are required", failures)
	_expect(registry.faction_visuals.size() == 20, "each shared archetype needs two faction visual profiles", failures)
	_expect(not registry.has_enemy_specific_profile(), "enemy-specific combat data is forbidden", failures)

	var validator: Variant = BootstrapValidator.new()
	_expect(validator.validate_registry(registry).is_empty(), "registry must satisfy the shared-archetype contract", failures)

	var determinism: Variant = DeterminismService.new(1001)
	var first_manifest: Variant = determinism.create_stage_manifest("phase_0", registry.archetype_ids())
	var second_manifest: Variant = DeterminismService.new(1001).create_stage_manifest("phase_0", registry.archetype_ids())
	_expect(first_manifest.to_json() == second_manifest.to_json(), "identical seeds must reproduce the same manifest", failures)
	_expect(first_manifest.input_log.size() == 0, "Phase 0 begins with an empty deterministic input log", failures)

	if failures.is_empty():
		print("Phase 0 contract checks passed")
		quit(0)
	else:
		printerr("Phase 0 contract failures:\n%s" % "\n".join(failures))
		quit(1)

func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)
