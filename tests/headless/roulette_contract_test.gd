extends SceneTree

const StageManifest = preload("res://scripts/core/stage_manifest.gd")


func _init() -> void:
	var failures := PackedStringArray()
	var roulette_script := load("res://scripts/roulette/roulette_service.gd")
	_expect(roulette_script != null, "roulette service loads", failures)
	if roulette_script != null:
		_test_judgment_line_gate(roulette_script, failures)
		_test_grade_mapping(roulette_script, failures)
		_test_gold_payout(roulette_script, failures)
		_test_source_selection_determinism(roulette_script, failures)
		_test_legendary_limit(roulette_script, failures)
	_finish(failures)


func _test_judgment_line_gate(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var result: Variant = service.resolve_board_snapshot([
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"x",
		&"x", &"gold", &"x",
	], _sources(), 1, 20, false)
	_expect(result.accepted, "a valid board snapshot is accepted", failures)
	_expect(result.outcome_type == &"none" and result.rewards.is_empty(), "other completed lines are ignored when the middle judgment line fails", failures)
	var x_result: Variant = service.resolve_board_snapshot([
		&"x", &"x", &"x",
		&"x", &"x", &"x",
		&"x", &"x", &"x",
	], _sources(), 2, 20, false)
	_expect(x_result.outcome_type == &"none", "X never produces a reward", failures)


func _test_grade_mapping(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var common: Variant = service.resolve_board_snapshot([
		&"x", &"gold", &"x",
		&"warrior", &"warrior", &"warrior",
		&"gold", &"x", &"gold",
	], _sources(), 3, 20, false)
	_expect(common.completed_line_count == 1 and common.rank_id == &"common" and common.rewards.size() == 1, "one matching line produces one common reward", failures)
	var elite: Variant = service.resolve_board_snapshot([
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"warrior",
		&"x", &"gold", &"x",
	], _sources(), 4, 20, false)
	_expect(elite.completed_line_count == 2 and elite.rank_id == &"elite", "two matching lines produce elite", failures)
	var hero: Variant = service.resolve_board_snapshot([
		&"warrior", &"warrior", &"x",
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"x",
	], _sources(), 5, 20, false)
	_expect(hero.completed_line_count == 3 and hero.rank_id == &"hero", "three matching lines produce hero", failures)
	_expect(hero.template_resolution == &"source_archetype_rank_fallback", "unresolved fixed upper-grade templates use an explicit provisional fallback", failures)


func _test_gold_payout(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var one_line: Variant = service.resolve_board_snapshot([
		&"x", &"warrior", &"x",
		&"gold", &"gold", &"gold",
		&"x", &"warrior", &"x",
	], _sources(), 6, 20, false)
	_expect(one_line.gold_reward == 15, "one gold line pays 75 percent of the paid spin cost", failures)
	var two_lines: Variant = service.resolve_board_snapshot([
		&"gold", &"gold", &"gold",
		&"gold", &"gold", &"gold",
		&"x", &"warrior", &"x",
	], _sources(), 7, 20, false)
	_expect(two_lines.gold_reward == 40, "two gold lines pay 200 percent", failures)
	var three_lines: Variant = service.resolve_board_snapshot([
		&"gold", &"gold", &"x",
		&"gold", &"gold", &"gold",
		&"gold", &"gold", &"x",
	], _sources(), 8, 20, false)
	_expect(three_lines.gold_reward == 100, "three or more gold lines pay 500 percent", failures)


func _test_source_selection_determinism(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var sources := _sources()
	sources.append({
		"symbol_id": &"warrior",
		"reward_archetype_id": &"archer",
		"board_weight": 3,
		"source_tier_id": &"tier_1",
		"source_weight": 3,
		"source_building_id": &"captured_top:rear",
	})
	var board := [
		&"x", &"gold", &"x",
		&"warrior", &"warrior", &"warrior",
		&"gold", &"x", &"gold",
	]
	var first: Variant = service.resolve_board_snapshot(board, sources, 12345, 20, false)
	var second: Variant = service.resolve_board_snapshot(board, sources, 12345, 20, false)
	_expect(first.source_building_id != &"", "a matching token resolves to an explicit building source", failures)
	_expect(first.source_building_id == second.source_building_id, "multiple matching sources remain deterministic for the same seed", failures)
	_expect(first.rewards[0].archetype_id == second.rewards[0].archetype_id, "the same source selection produces the same reward archetype", failures)


func _test_legendary_limit(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var board := [
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"warrior",
	]
	var first: Variant = service.resolve_board_snapshot(board, _sources(), 9, 20, true)
	_expect(first.completed_line_count == 8 and first.rank_id == &"legendary" and first.rewards.size() == 1, "the first all-nine board produces one legendary", failures)
	var repeat: Variant = service.resolve_board_snapshot(board, _sources(), 10, 20, true)
	_expect(repeat.rank_id == &"hero" and repeat.rewards.size() == 2 and repeat.legendary_converted_to_heroes, "later all-nine boards convert to two heroes", failures)


func _sources() -> Array[Dictionary]:
	return [{
		"symbol_id": &"warrior",
		"reward_archetype_id": &"shield_guard",
		"board_weight": 3,
		"source_tier_id": &"tier_1",
		"source_weight": 1,
		"source_building_id": &"home:rear",
	}]


func _manifest() -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = "roulette_contract"
	manifest.seed = 20260722
	manifest.starting_gold = 160
	manifest.starting_food_cap = 12
	return manifest


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Approved roulette contract checks passed")
		quit(0)
	else:
		printerr("Approved roulette contract failures:\n%s" % "\n".join(failures))
		quit(1)
