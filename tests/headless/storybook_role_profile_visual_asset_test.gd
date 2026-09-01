# 승인·자동 제작된 Storybook 역할 자산이 실제 전투 표시와 카탈로그에 같은 방식으로 연결되는지 검증한다.
extends SceneTree

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const RUNTIME_CELL_SIZE := Vector2(512, 512)
const RUNTIME_PIVOT := Vector2(256, 448)
const EXPECTED_VISUALS := [
	{
		"team_id": &"lumern",
		"archetype_id": &"shield_guard",
		"path": "res://assets/art/units/lumern_shield_guard_storybook_idle_v1.png",
		"flip_h": false,
	},
	{
		"team_id": &"veil",
		"archetype_id": &"shield_guard",
		"path": "res://assets/art/units/veil_shield_guard_storybook_idle_v1.png",
		"flip_h": false,
	},
	{
		"team_id": &"lumern",
		"archetype_id": &"spear_guard",
		"path": "res://assets/art/units/lumern_spear_guard_storybook_idle_v3.png",
		"flip_h": false,
	},
	{
		"team_id": &"veil",
		"archetype_id": &"spear_guard",
		"path": "res://assets/art/units/veil_spear_guard_storybook_idle_v2.png",
		"flip_h": true,
	},
	{
		"team_id": &"lumern",
		"archetype_id": &"archer",
		"path": "res://assets/art/units/lumern_archer_storybook_idle_v1.png",
		"flip_h": false,
	},
	{
		"team_id": &"veil",
		"archetype_id": &"archer",
		"path": "res://assets/art/units/veil_archer_storybook_idle_v1.png",
		"flip_h": true,
	},
	{
		"team_id": &"lumern",
		"archetype_id": &"cavalry",
		"path": "res://assets/art/units/lumern_cavalry_storybook_idle_v2.png",
		"flip_h": false,
	},
	{
		"team_id": &"veil",
		"archetype_id": &"cavalry",
		"path": "res://assets/art/units/veil_cavalry_storybook_idle_v2.png",
		"flip_h": true,
	},
	{
		"team_id": &"lumern",
		"archetype_id": &"mage",
		"path": "res://assets/art/units/lumern_mage_storybook_idle_v1.png",
		"flip_h": false,
	},
	{
		"team_id": &"veil",
		"archetype_id": &"mage",
		"path": "res://assets/art/units/veil_mage_storybook_idle_v1.png",
		"flip_h": true,
	},
]


func _init() -> void:
	var failures := PackedStringArray()
	var view := BattleFocusView.new()
	_expect(view.has_method("resolve_unit_visual"), "BattleFocus resolves a visual by the unit's actual faction and archetype instead of always drawing a Shield Guard", failures)
	if view.has_method("resolve_unit_visual"):
		for expected: Dictionary in EXPECTED_VISUALS:
			var resolved: Dictionary = view.call("resolve_unit_visual", expected["team_id"], expected["archetype_id"]) as Dictionary
			var texture := resolved.get(&"texture") as Texture2D
			_expect(texture != null, "%s/%s resolves a role texture" % [expected["team_id"], expected["archetype_id"]], failures)
			if texture != null:
				_expect(texture.resource_path == expected["path"], "%s/%s uses its approved Storybook role asset" % [expected["team_id"], expected["archetype_id"]], failures)
			_expect(bool(resolved.get(&"flip_h", false)) == bool(expected["flip_h"]), "%s/%s keeps its intended battle-facing direction" % [expected["team_id"], expected["archetype_id"]], failures)
		var unsupported: Dictionary = view.call("resolve_unit_visual", &"lumern", &"giant") as Dictionary
		_expect(unsupported.is_empty(), "unsupported roles do not impersonate a Shield Guard in BattleFocus", failures)
	var catalog := load(BOOTSTRAP_CATALOG_PATH) as BootstrapCatalog
	_expect(catalog != null, "bootstrap catalog loads the role-specific Storybook assets", failures)
	if catalog != null:
		for expected: Dictionary in EXPECTED_VISUALS:
			var path := str(expected["path"])
			_expect(FileAccess.file_exists(path), "%s exists for Godot import" % path, failures)
			var profile := _find_profile(catalog, expected["team_id"], expected["archetype_id"])
			_expect(profile != null, "%s/%s profile exists" % [expected["team_id"], expected["archetype_id"]], failures)
			if profile != null:
				_expect(profile.idle_texture != null and profile.idle_texture.resource_path == path, "%s/%s catalog profile points at the same role asset" % [expected["team_id"], expected["archetype_id"]], failures)
				_expect(profile.idle_texture != null and profile.idle_texture.get_size() == RUNTIME_CELL_SIZE, "%s/%s retains the shared 512px cell" % [expected["team_id"], expected["archetype_id"]], failures)
				_expect(profile.idle_pivot == RUNTIME_PIVOT, "%s/%s retains the shared ground pivot" % [expected["team_id"], expected["archetype_id"]], failures)
				if expected["team_id"] == &"veil":
					_expect(profile.idle_mirror_for_veil == bool(expected["flip_h"]), "%s/%s catalog direction agrees with BattleFocus" % [expected["team_id"], expected["archetype_id"]], failures)
	view.free()
	_finish(failures)


func _find_profile(catalog: BootstrapCatalog, team_id: StringName, archetype_id: StringName) -> FactionVisualProfile:
	for profile in catalog.faction_visual_profiles:
		if profile.visual_faction_id == team_id and profile.archetype_id == archetype_id:
			return profile
	return null


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Storybook role profile visual asset contracts passed")
		quit(0)
		return
	printerr("Storybook role profile visual asset contract failures:\n%s" % "\n".join(failures))
	quit(1)
