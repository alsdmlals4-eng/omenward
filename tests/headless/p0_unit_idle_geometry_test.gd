# P0 병종 idle 런타임 셀과 공통 바닥 기준점 계약을 검증한다.
extends SceneTree

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const RUNTIME_CELL_SIZE := Vector2(512, 512)
const RUNTIME_IDLE_PIVOT := Vector2(256, 448)
const P0_ARCHETYPES := [
	&"greatsword_warrior",
	&"assassin",
	&"spear_guard",
	&"archer",
	&"cavalry",
	&"priest",
	&"mage",
	&"flier",
	&"giant",
]
const FACTIONS := [&"lumern", &"veil"]


func _init() -> void:
	var failures := PackedStringArray()
	var catalog := load(BOOTSTRAP_CATALOG_PATH) as BootstrapCatalog
	_expect(catalog != null, "bootstrap catalog loads for P0 idle geometry", failures)
	if catalog != null:
		for archetype_id in P0_ARCHETYPES:
			for faction_id in FACTIONS:
				var profile := _find_profile(catalog, archetype_id, faction_id)
				var prefix := "%s/%s" % [archetype_id, faction_id]
				_expect(profile != null, "%s visual profile exists" % prefix, failures)
				if profile == null:
					continue
				_expect(profile.idle_texture != null, "%s resolves a runtime idle texture" % prefix, failures)
				if profile.idle_texture != null:
					_expect(
						profile.idle_texture.get_size() == RUNTIME_CELL_SIZE,
						"%s uses the shared 512x512 runtime cell" % prefix,
						failures,
					)
				_expect(
					profile.idle_pivot == RUNTIME_IDLE_PIVOT,
					"%s uses the shared ground pivot" % prefix,
					failures,
				)
	_finish(failures)


func _find_profile(catalog: BootstrapCatalog, archetype_id: StringName, faction_id: StringName) -> FactionVisualProfile:
	for profile in catalog.faction_visual_profiles:
		if profile.archetype_id == archetype_id and profile.visual_faction_id == faction_id:
			return profile
	return null


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("P0 unit idle geometry contracts passed")
		quit(0)
	else:
		printerr("P0 unit idle geometry contract failures:\n%s" % "\n".join(failures))
		quit(1)
