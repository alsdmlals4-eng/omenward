extends SceneTree

const StageManifestScript = preload("res://scripts/core/stage_manifest.gd")
const StageEconomyScript = preload("res://scripts/core/stage_economy.gd")
const RouletteServiceScript = preload("res://scripts/roulette/roulette_service.gd")


func _init() -> void:
	var failures := PackedStringArray()
	_test_manifest_determinism(failures)
	_test_stage_economy_baseline(failures)
	_test_roulette_resolution_determinism(failures)
	_finish(failures)


func _test_manifest_determinism(failures: PackedStringArray) -> void:
	var first := _manifest()
	var second := _manifest()
	_expect(
		first.to_json() == second.to_json(),
		"identical platform-neutral manifests must serialize identically",
		failures,
	)
	_expect(first.input_log.is_empty(), "baseline manifest input log starts empty", failures)


func _test_stage_economy_baseline(failures: PackedStringArray) -> void:
	var economy: Variant = StageEconomyScript.new(_manifest())
	_expect(economy.gold == 160, "baseline regular stage starts with 160 gold", failures)
	_expect(economy.food_cap == 12, "baseline regular stage starts with 12 food", failures)
	economy.advance(60.0, 1, 1)
	_expect(
		economy.gold == 183,
		"60 seconds with one clash and one stable outpost produces the recorded 183 gold baseline",
		failures,
	)


func _test_roulette_resolution_determinism(failures: PackedStringArray) -> void:
	var board: Array[StringName] = []
	for _index in 9:
		board.append(&"barracks")
	var sources: Array[Dictionary] = [{
		"symbol_id": &"barracks",
		"reward_archetype_id": &"shield_guard",
		"source_building_id": &"fixture_barracks",
		"source_tier_id": &"tier_1",
		"source_weight": 1,
	}]
	var first: Variant = RouletteServiceScript.new(null, null, null, &"lumern")
	var second: Variant = RouletteServiceScript.new(null, null, null, &"lumern")
	var first_result: Variant = first.resolve_board_snapshot(board, sources, 77, 20, false)
	var second_result: Variant = second.resolve_board_snapshot(board, sources, 77, 20, false)
	_expect(first_result.accepted, "recorded roulette fixture is accepted", failures)
	_expect(first_result.completed_line_count == 8, "full 3x3 fixture completes eight lines", failures)
	_expect(first_result.rank_id == &"legendary", "eight completed lines preserve legendary rank", failures)
	_expect(
		JSON.stringify(first_result.to_dictionary()) == JSON.stringify(second_result.to_dictionary()),
		"identical board, source snapshot, and seed reproduce the same roulette result",
		failures,
	)


func _manifest() -> StageManifest:
	var manifest := StageManifestScript.new() as StageManifest
	manifest.stage_id = "regular_stage"
	manifest.seed = 101
	manifest.archetype_ids = ["shield_guard", "spear_guard"]
	manifest.random_roll = 17
	manifest.starting_gold = 160
	manifest.starting_food_cap = 12
	manifest.base_max_health = 100.0
	manifest.tutorial_stage = false
	manifest.wave_count = 2
	manifest.waves = [{"wave_number": 1}, {"wave_number": 2}]
	return manifest


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Platform-neutral core characterization checks passed")
		quit(0)
	else:
		printerr("Platform-neutral core characterization failures:\n%s" % "\n".join(failures))
		quit(1)
