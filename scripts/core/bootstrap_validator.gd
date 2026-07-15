class_name BootstrapValidator
extends RefCounted

const REQUIRED_ARCHETYPE_COUNT := 10

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
	return errors
