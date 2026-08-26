# P0 병종 idle 런타임 가독성 갤러리 계약을 검증한다.
extends SceneTree

const GALLERY_SCENE_PATH := "res://tests/visual/p0_unit_idle_gallery.tscn"
const EXPECTED_UNIT_VIEW_COUNT := 18
const EXPECTED_UNIT_NAMES := [
	&"lumern_greatsword_warrior",
	&"veil_greatsword_warrior",
	&"lumern_assassin",
	&"veil_assassin",
	&"lumern_spear_guard",
	&"veil_spear_guard",
	&"lumern_archer",
	&"veil_archer",
	&"lumern_cavalry",
	&"veil_cavalry",
	&"lumern_priest",
	&"veil_priest",
	&"lumern_mage",
	&"veil_mage",
	&"lumern_flier",
	&"veil_flier",
	&"lumern_giant",
	&"veil_giant",
]


func _init() -> void:
	call_deferred("_run")


func _run() -> void:
	var failures := PackedStringArray()
	var packed := load(GALLERY_SCENE_PATH) as PackedScene
	_expect(packed != null, "P0 idle gallery scene loads", failures)
	if packed != null:
		var gallery := packed.instantiate()
		root.add_child(gallery)
		await process_frame
		_expect(gallery.get_child_count() == EXPECTED_UNIT_VIEW_COUNT, "gallery creates all 18 P0 runtime unit views", failures)
		for unit_name in EXPECTED_UNIT_NAMES:
			var unit_view := gallery.get_node_or_null(NodePath(unit_name))
			_expect(unit_view is UnitView, "%s gallery unit view exists" % unit_name, failures)
			if unit_view is UnitView:
				_expect(unit_view.idle_sprite != null and unit_view.idle_sprite.visible, "%s gallery unit renders an idle sprite" % unit_name, failures)
		var first_row_unit := gallery.get_node_or_null(NodePath(&"lumern_greatsword_warrior")) as UnitView
		_expect(first_row_unit != null and first_row_unit.position.y >= 108.0, "first gallery row clears the column headings", failures)
		gallery.queue_free()
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("P0 unit idle gallery contracts passed")
		quit(0)
	else:
		printerr("P0 unit idle gallery contract failures:\n%s" % "\n".join(failures))
		quit(1)
