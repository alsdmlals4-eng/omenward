# P0 병종 idle 런타임 셀을 같은 전장 배율로 배치해 검토한다.
extends Node2D

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const UNIT_SCENE := preload("res://scenes/units/unit.tscn")
const ARCHETYPES := [
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
const COLUMN_X := {&"lumern": 280.0, &"veil": 720.0}
const FIRST_ROW_Y := 108.0
const ROW_GAP := 51.0


func _ready() -> void:
	var catalog := load(BOOTSTRAP_CATALOG_PATH) as BootstrapCatalog
	if catalog == null:
		push_error("P0 idle gallery could not load bootstrap catalog")
		return
	for row_index in ARCHETYPES.size():
		var archetype_id: StringName = ARCHETYPES[row_index]
		for faction_id in FACTIONS:
			var profile := _find_profile(catalog, archetype_id, faction_id)
			if profile == null:
				push_error("P0 idle gallery has no profile for %s/%s" % [archetype_id, faction_id])
				continue
			var unit_view := UNIT_SCENE.instantiate() as UnitView
			unit_view.name = "%s_%s" % [faction_id, archetype_id]
			unit_view.position = Vector2(COLUMN_X[faction_id], FIRST_ROW_Y + row_index * ROW_GAP)
			add_child(unit_view)
			unit_view.bind_unit({"owner_team_id": faction_id, "state": &"idle"}, profile)
	queue_redraw()


func _draw() -> void:
	draw_rect(Rect2(0, 0, 960, 540), Color(0.035, 0.055, 0.09), true)
	draw_string(ThemeDB.fallback_font, Vector2(24, 28), "P0 IDLE RUNTIME REVIEW · SHARED BATTLE SCALE", HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color(0.86, 0.9, 0.96))
	draw_string(ThemeDB.fallback_font, Vector2(230, 50), "LUMERN", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color(0.58, 0.76, 1.0))
	draw_string(ThemeDB.fallback_font, Vector2(682, 50), "VEIL", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color(0.96, 0.46, 0.66))
	for row_index in ARCHETYPES.size():
		var y := FIRST_ROW_Y + row_index * ROW_GAP
		draw_line(Vector2(140, y), Vector2(820, y), Color(0.2, 0.25, 0.31), 1.0)
		draw_string(ThemeDB.fallback_font, Vector2(24, y + 5), str(ARCHETYPES[row_index]), HORIZONTAL_ALIGNMENT_LEFT, 108, 12, Color(0.72, 0.78, 0.84))


func _find_profile(catalog: BootstrapCatalog, archetype_id: StringName, faction_id: StringName) -> FactionVisualProfile:
	for profile in catalog.faction_visual_profiles:
		if profile.archetype_id == archetype_id and profile.visual_faction_id == faction_id:
			return profile
	return null
