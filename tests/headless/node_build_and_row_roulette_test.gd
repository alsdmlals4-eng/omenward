# 노드 건설 선택과 중앙 판정줄 기반 룰렛 보상 계약을 검증한다.
extends SceneTree

const STAGE_RUN_SCRIPT := preload("res://scripts/core/stage_run.gd")
const UNIT_SPAWN_DEFINITION := preload("res://scripts/data/unit_spawn_definition.gd")
const BATTLEFIELD_VIEW_SCENE := preload("res://scenes/battle/battlefield.tscn")
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	_test_node_construction_contract(failures)
	_test_battlefield_node_selection_contract(failures)
	_test_row_based_roulette_contract(failures)
	_finish(failures)


func _test_node_construction_contract(failures: PackedStringArray) -> void:
	var tutorial := load(TUTORIAL_STAGE_PATH) as Resource
	var run: Variant = STAGE_RUN_SCRIPT.new()
	run.start(tutorial, 1001)
	_expect(run.has_method("construction_status"), "stage run exposes selected-node status", failures)
	_expect(run.has_method("available_buildings_for_node"), "stage run exposes permitted buildings for a selected node", failures)
	_expect(run.has_method("construct_at_node"), "stage run installs a selected building into the selected node", failures)
	if not run.has_method("construction_status") or not run.has_method("available_buildings_for_node") or not run.has_method("construct_at_node"):
		return
	_expect(run.construction_status(&"home_top", &"front_a") == &"available", "an owned empty node is selectable", failures)
	var options: Array = run.available_buildings_for_node(&"home_top", &"front_a")
	_expect(options.has(&"tower") and options.has(&"farm"), "a selectable node lists its permitted buildings", failures)
	_expect(run.construct_at_node(&"home_top", &"front_a", &"tower"), "selected tower installs into the selected node", failures)
	_expect(run.construction_status(&"home_top", &"front_a") == &"occupied", "installed node reports occupied", failures)
	_expect(not run.construct_at_node(&"home_top", &"front_a", &"farm"), "occupied node rejects a second building", failures)


func _test_battlefield_node_selection_contract(failures: PackedStringArray) -> void:
	var tutorial := load(TUTORIAL_STAGE_PATH) as Resource
	var run: Variant = STAGE_RUN_SCRIPT.new()
	run.start(tutorial, 1001)
	var battlefield := BATTLEFIELD_VIEW_SCENE.instantiate()
	get_root().add_child(battlefield)
	var selections: Array = []
	battlefield.construction_node_selected.connect(func(outpost_id: StringName, node_id: StringName): selections.append([outpost_id, node_id]))
	battlefield.bind_run(run)
	var click := InputEventMouseButton.new()
	click.button_index = MOUSE_BUTTON_LEFT
	click.pressed = true
	click.position = Vector2(272, 142)
	battlefield._unhandled_input(click)
	_expect(selections.size() == 1 and selections[0] == [&"home_top", &"front_a"], "clicking a friendly node selects its exact lane outpost and node ID", failures)
	get_root().remove_child(battlefield)
	battlefield.queue_free()


func _test_row_based_roulette_contract(failures: PackedStringArray) -> void:
	var roulette_script := load("res://scripts/roulette/roulette_service.gd") as GDScript
	_expect(roulette_script != null, "roulette service exists", failures)
	if roulette_script == null:
		return
	var roulette: Variant = roulette_script.new(null, null, null, &"lumern")
	_expect(roulette.has_method("evaluate_board"), "roulette exposes central-row match evaluation", failures)
	if not roulette.has_method("evaluate_board"):
		return
	var one_line := _cards([
		&"archer", &"mage", &"giant",
		&"shield_guard", &"shield_guard", &"shield_guard",
		&"cavalry", &"archer", &"mage",
	])
	var one_line_result: Dictionary = roulette.evaluate_board(one_line)
	_expect(one_line_result.get("has_reward", false), "a completed center row earns a reward", failures)
	_expect(one_line_result.get("matched_symbol", &"") == &"shield_guard", "center row fixes the matched symbol", failures)
	_expect(int(one_line_result.get("completed_line_count", 0)) == 1, "only matching lines using the center-row symbol count", failures)
	_expect(one_line_result.get("rank_id", &"") == &"common", "one completed line grants common rank", failures)
	var two_line := _cards([
		&"shield_guard", &"archer", &"mage",
		&"shield_guard", &"shield_guard", &"shield_guard",
		&"shield_guard", &"cavalry", &"mage",
	])
	var two_line_result: Dictionary = roulette.evaluate_board(two_line)
	_expect(int(two_line_result.get("completed_line_count", 0)) == 2, "overlapping completed lines count separately", failures)
	_expect(two_line_result.get("rank_id", &"") == &"elite", "two completed lines grant elite rank", failures)
	var invalid_center := _cards([
		&"shield_guard", &"shield_guard", &"shield_guard",
		&"archer", &"mage", &"giant",
		&"cavalry", &"archer", &"mage",
	])
	var invalid_center_result: Dictionary = roulette.evaluate_board(invalid_center)
	_expect(not invalid_center_result.get("has_reward", true), "a completed non-center row is ignored when the center row misses", failures)
	_expect(int(invalid_center_result.get("completed_line_count", -1)) == 0, "center-row miss produces zero completed lines", failures)


func _cards(archetype_ids: Array[StringName]) -> Array:
	var cards: Array = []
	for archetype_id in archetype_ids:
		var card := UNIT_SPAWN_DEFINITION.new()
		card.archetype_id = archetype_id
		card.owner_team_id = &"lumern"
		card.visual_faction_id = &"lumern"
		cards.append(card)
	return cards


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Node build and row roulette contracts passed")
		quit(0)
	else:
		printerr("Node build and row roulette contract failures:\n%s" % "\n".join(failures))
		quit(1)
