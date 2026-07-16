class_name DataRegistry
extends RefCounted

var catalog: BootstrapCatalog
var archetypes: Dictionary = {}
var faction_visuals: Array[FactionVisualProfile] = []
var animation_contracts: Dictionary = {}

func load_bootstrap_catalog(resource_path: String) -> PackedStringArray:
	var errors := PackedStringArray()
	var loaded := ResourceLoader.load(resource_path)
	if loaded == null or not loaded is BootstrapCatalog:
		errors.append("bootstrap catalog could not load: %s" % resource_path)
		return errors
	catalog = loaded as BootstrapCatalog
	for archetype in catalog.archetypes:
		var key := str(archetype.archetype_id)
		if archetypes.has(key):
			errors.append("duplicate archetype: %s" % key)
		archetypes[key] = archetype
	for contract in catalog.animation_contracts:
		animation_contracts[str(contract.archetype_id)] = contract
	faction_visuals = catalog.faction_visual_profiles.duplicate()
	return errors

func archetype_ids() -> Array[String]:
	var ids: Array[String] = []
	for key in archetypes.keys():
		ids.append(str(key))
	ids.sort()
	return ids

func has_enemy_specific_profile() -> bool:
	return false
