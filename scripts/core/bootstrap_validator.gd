class_name BootstrapValidator
extends RefCounted

const REQUIRED_ARCHETYPE_COUNT := 10
const VALID_FACTION_IDS := [&"lumern", &"veil"]
const VALID_FRONT_IDS := [&"front"]

func validate_registry(registry: DataRegistry) -> PackedStringArray:
	var errors := PackedStringArray()
	if registry.archetypes.size() != REQUIRED_ARCHETYPE_COUNT:
		errors.append("expected %d shared archetypes" % REQUIRED_ARCHETYPE_COUNT)
	if registry.faction_visuals.size() != REQUIRED_ARCHETYPE_COUNT * 2:
		errors.append("expected two visual profiles for every shared archetype")
	for archetype_id in registry.archetype_ids():
		if not registry.animation_contracts.has(archetype_id):
			errors.append("missing animation contract: %s" % archetype_id)
		var visual_count := 0
		for visual in registry.faction_visuals:
			if str(visual.archetype_id) == archetype_id:
				visual_count += 1
		if visual_count != 2:
			errors.append("expected two visual profiles: %s" % archetype_id)
	var tutorial := registry.stage_definition(&"tutorial_stage")
	var regular := registry.stage_definition(&"regular_stage")
	if tutorial == null or not tutorial.tutorial_stage or tutorial.waves.size() != 4:
		errors.append("tutorial stage must contain four tutorial waves")
	if regular == null or regular.tutorial_stage or regular.waves.size() != 20:
		errors.append("regular stage must contain twenty waves")
	if tutorial != null:
		_validate_stage_spawns(tutorial, registry, errors)
	if regular != null:
		_validate_stage_spawns(regular, registry, errors)
	return errors


func _validate_stage_spawns(stage: StageDefinition, registry: DataRegistry, errors: PackedStringArray) -> void:
	for wave in stage.waves:
		for spawn in wave.spawns:
			if not registry.archetypes.has(str(spawn.archetype_id)):
				errors.append("unknown spawn archetype_id: %s" % spawn.archetype_id)
			if not VALID_FACTION_IDS.has(spawn.visual_faction_id):
				errors.append("invalid spawn visual_faction_id: %s" % spawn.visual_faction_id)
			if not VALID_FACTION_IDS.has(spawn.owner_team_id):
				errors.append("invalid spawn owner_team_id: %s" % spawn.owner_team_id)
			if not VALID_FRONT_IDS.has(spawn.lane_id):
				errors.append("invalid spawn front id: %s" % spawn.lane_id)
