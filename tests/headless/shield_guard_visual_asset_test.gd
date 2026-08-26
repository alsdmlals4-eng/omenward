# Shield Guard idle 런타임 자산 계약을 검증한다.
extends SceneTree

const UNIT_SCENE_PATH := "res://scenes/units/unit.tscn"
const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const LUMERN_IDLE_PATH := "res://assets/art/units/lumern_shield_guard_idle.png"
const VEIL_IDLE_PATH := "res://assets/art/units/veil_shield_guard_idle.png"


func _init() -> void:
	var failures := PackedStringArray()
	_expect(FileAccess.file_exists(LUMERN_IDLE_PATH), "Lumern Shield Guard idle texture is available to Godot", failures)
	_expect(FileAccess.file_exists(VEIL_IDLE_PATH), "Veil Shield Guard idle texture is available to Godot", failures)
	var visual_profile := FactionVisualProfile.new()
	_expect(_has_property(visual_profile, &"idle_texture"), "faction visual profiles can provide an idle texture", failures)
	_expect(_has_property(visual_profile, &"idle_pivot"), "faction visual profiles declare the idle pivot", failures)
	var catalog := load(BOOTSTRAP_CATALOG_PATH) as BootstrapCatalog
	_expect(catalog != null, "bootstrap catalog loads for Shield Guard texture binding", failures)
	var lumern_profile: FactionVisualProfile
	var veil_profile: FactionVisualProfile
	if catalog != null:
		lumern_profile = _find_profile(catalog, &"lumern")
		veil_profile = _find_profile(catalog, &"veil")
		_expect(lumern_profile != null and lumern_profile.idle_texture != null, "Lumern Shield Guard profile resolves its idle texture", failures)
		_expect(veil_profile != null and veil_profile.idle_texture != null, "Veil Shield Guard profile resolves its idle texture", failures)
		_expect(lumern_profile != null and lumern_profile.idle_pivot == Vector2(640, 1280), "Lumern uses the locked Shield Guard pivot", failures)
		_expect(veil_profile != null and veil_profile.idle_pivot == Vector2(640, 1280), "Veil uses the locked Shield Guard pivot", failures)
	var packed := load(UNIT_SCENE_PATH) as PackedScene
	_expect(packed != null, "shared unit scene loads for Shield Guard textures", failures)
	if packed != null:
		var unit_view := packed.instantiate()
		root.add_child(unit_view)
		_expect(unit_view.get_node_or_null("IdleSprite") is Sprite2D, "shared unit scene has an idle sprite receiver", failures)
		if lumern_profile != null:
			var idle_sprite := unit_view.get_node_or_null("IdleSprite") as Sprite2D
			unit_view.idle_sprite = idle_sprite
			unit_view.bind_unit({"owner_team_id": &"lumern", "state": &"idle"}, lumern_profile)
			unit_view.call("_sync_idle_sprite")
			_expect(idle_sprite != null and idle_sprite.texture == lumern_profile.idle_texture, "UnitView renders the resolved Lumern idle texture", failures)
			_expect(idle_sprite != null and idle_sprite.visible, "UnitView shows the resolved idle sprite", failures)
		unit_view.queue_free()
	_finish(failures)


func _has_property(value: Object, property_name: StringName) -> bool:
	for property in value.get_property_list():
		if property.name == property_name:
			return true
	return false


func _find_profile(catalog: BootstrapCatalog, faction_id: StringName) -> FactionVisualProfile:
	for profile in catalog.faction_visual_profiles:
		if profile.archetype_id == &"shield_guard" and profile.visual_faction_id == faction_id:
			return profile
	return null


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Shield Guard visual asset contracts passed")
		quit(0)
	else:
		printerr("Shield Guard visual asset contract failures:\n%s" % "\n".join(failures))
		quit(1)
