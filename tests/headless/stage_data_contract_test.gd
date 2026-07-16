extends SceneTree

const BootstrapValidator = preload("res://scripts/core/bootstrap_validator.gd")
const DataRegistry = preload("res://scripts/core/data_registry.gd")
const StageDefinition = preload("res://scripts/data/stage_definition.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"
const MANIFEST_SEED := 20260716


func _init() -> void:
	var failures := PackedStringArray()
	var tutorial := ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var regular := ResourceLoader.load(REGULAR_STAGE_PATH)

	_expect(tutorial != null, "tutorial stage resource must load", failures)
	_expect(regular != null, "regular stage resource must load", failures)
	if tutorial != null:
		_expect(_waves(tutorial).size() == 4, "tutorial has four waves", failures)
	if regular != null:
		var waves := _waves(regular)
		_expect(waves.size() == 20, "regular stage has W1 through W20", failures)
		if waves.size() >= 20:
			_expect(waves[14].boss_kind == &"legendary", "W15 is legendary", failures)
			_expect(waves[19].boss_kind == &"mythic", "W20 is mythic", failures)
		_assert_regular_manifest_contract(regular as StageDefinition, failures)

	_expect_spawn_is_rejected(
		&"enemy_only",
		&"veil",
		&"veil",
		&"top",
		"unknown spawn archetype IDs are rejected",
		"unknown spawn archetype_id: enemy_only",
		failures,
	)
	_expect_spawn_is_rejected(
		&"shield_guard",
		&"other",
		&"veil",
		&"top",
		"non-lumern/veil visual factions are rejected",
		"invalid spawn visual_faction_id: other",
		failures,
	)
	_expect_spawn_is_rejected(
		&"shield_guard",
		&"veil",
		&"other",
		&"top",
		"non-lumern/veil owner teams are rejected",
		"invalid spawn owner_team_id: other",
		failures,
	)
	_expect_spawn_is_rejected(
		&"shield_guard",
		&"veil",
		&"veil",
		&"side",
		"lane IDs outside top/middle/bottom are rejected",
		"invalid spawn lane_id: side",
		failures,
	)

	if failures.is_empty():
		print("Stage data contract checks passed")
		quit(0)
	else:
		printerr("Stage data contract failures:\n%s" % "\n".join(failures))
		quit(1)


func _waves(stage: Resource) -> Array:
	return stage.get("waves") as Array


func _assert_regular_manifest_contract(regular: StageDefinition, failures: PackedStringArray) -> void:
	var parsed: Variant = JSON.parse_string(regular.build_manifest(MANIFEST_SEED).to_json())
	_expect(parsed is Dictionary, "regular manifest JSON parses into an object", failures)
	if not parsed is Dictionary:
		return
	var manifest: Dictionary = parsed
	_expect(manifest.get("stage_id") == "regular_stage", "manifest includes the regular stage ID", failures)
	_expect(manifest.get("seed") == MANIFEST_SEED, "manifest includes the supplied seed", failures)
	_expect(manifest.get("starting_gold") == 160, "manifest includes starting gold", failures)
	_expect(manifest.get("starting_food_cap") == 12, "manifest includes starting food cap", failures)
	_expect(manifest.get("tutorial_stage") == false, "manifest identifies the regular stage", failures)
	_expect(manifest.get("wave_count") == 20, "manifest includes the regular wave count", failures)

	var manifest_waves: Array = manifest.get("waves", []) as Array
	_expect(manifest_waves.size() == 20, "manifest includes resolved waves", failures)
	if manifest_waves.is_empty():
		return
	var first_wave: Dictionary = manifest_waves[0] as Dictionary
	_expect(first_wave.has("wave_number"), "manifest wave includes a wave number", failures)
	_expect(first_wave.has("omen_lead_seconds"), "manifest wave includes omen lead time", failures)
	_expect(first_wave.has("boss_kind"), "manifest wave includes boss kind", failures)
	_expect(first_wave.has("is_overtime"), "manifest wave includes overtime state", failures)
	var spawns: Array = first_wave.get("spawns", []) as Array
	_expect(not spawns.is_empty(), "manifest wave includes resolved spawns", failures)
	if spawns.is_empty():
		return
	var first_spawn: Dictionary = spawns[0] as Dictionary
	for field in ["archetype_id", "tier_id", "rank_id", "owner_team_id", "visual_faction_id", "lane_id", "spawn_delay_seconds"]:
		_expect(first_spawn.has(field), "manifest spawn includes %s" % field, failures)

	var input_log: Variant = manifest.get("input_log")
	_expect(input_log is Array, "manifest includes an input log array", failures)
	if input_log is Array:
		_expect((input_log as Array).is_empty(), "new manifests begin with an empty input log", failures)


func _expect_spawn_is_rejected(
	archetype_id: StringName,
	visual_faction_id: StringName,
	owner_team_id: StringName,
	lane_id: StringName,
	message: String,
	expected_error: String,
	failures: PackedStringArray,
) -> void:
	var errors := _invalid_spawn_errors(archetype_id, visual_faction_id, owner_team_id, lane_id)
	_expect(errors.has(expected_error), "%s: %s" % [message, errors], failures)


func _invalid_spawn_errors(
	archetype_id: StringName,
	visual_faction_id: StringName,
	owner_team_id: StringName,
	lane_id: StringName,
) -> PackedStringArray:
	var registry: DataRegistry = DataRegistry.new()
	var load_errors := registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not load_errors.is_empty():
		return load_errors
	var regular: StageDefinition = registry.stage_definition(&"regular_stage").duplicate(true) as StageDefinition
	var spawn: UnitSpawnDefinition = regular.waves[0].spawns[0].duplicate() as UnitSpawnDefinition
	spawn.archetype_id = archetype_id
	spawn.visual_faction_id = visual_faction_id
	spawn.owner_team_id = owner_team_id
	spawn.lane_id = lane_id
	regular.waves[0].spawns[0] = spawn
	registry.stages[str(regular.stage_id)] = regular
	return BootstrapValidator.new().validate_registry(registry)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)
