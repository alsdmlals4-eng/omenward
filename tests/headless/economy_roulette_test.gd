extends SceneTree

const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const OutpostState = preload("res://scripts/battle/outpost_state.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")


func _init() -> void:
	var failures := PackedStringArray()
	var economy_script := load("res://scripts/core/stage_economy.gd")
	var building_service_script := load("res://scripts/buildings/building_service.gd")
	var roulette_script := load("res://scripts/roulette/roulette_service.gd")
	var deployment_script := load("res://scripts/units/deployment_service.gd")
	_expect(economy_script != null, "stage economy service exists", failures)
	_expect(building_service_script != null, "building service exists", failures)
	_expect(roulette_script != null, "roulette service exists", failures)
	_expect(deployment_script != null, "deployment service exists", failures)
	if economy_script != null:
		_test_stage_economy(economy_script, failures)
	if economy_script != null and building_service_script != null:
		_test_building_ownership_and_capture_lock(economy_script, building_service_script, failures)
		_test_stabilized_capture_allows_rebuilding(economy_script, building_service_script, failures)
	if economy_script != null and building_service_script != null and roulette_script != null:
		_test_deterministic_approved_roulette(economy_script, building_service_script, roulette_script, failures)
	if economy_script != null and deployment_script != null:
		_test_deployment_food_limit(economy_script, deployment_script, failures)
	_finish(failures)


func _test_stage_economy(economy_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	_expect(economy.gold == 160, "regular stage starts at 160 gold", failures)
	_expect(economy.food_cap == 12, "regular stage starts with 12 food", failures)
	economy.advance(60.0, 1, 1)
	_expect(economy.gold == 183, "active combat grants base, controlled clash, and stable outpost income on their exact intervals", failures)


func _test_building_ownership_and_capture_lock(economy_script: GDScript, building_service_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	var buildings: Variant = building_service_script.new(economy, _manifest())
	var enemy_outpost := OutpostState.new(&"veil")
	var player_outpost := OutpostState.new(&"lumern")
	buildings.register_outpost(&"enemy_top", enemy_outpost, [&"front_a"])
	buildings.register_outpost(&"player_top", player_outpost, [&"front_a", &"front_b"])
	_expect(not buildings.try_construct(&"enemy_top", &"front_a", &"tower"), "enemy-owned node rejects player building", failures)
	_expect(buildings.try_construct(&"player_top", &"front_a", &"tower"), "owned stabilized outpost accepts a tower", failures)
	player_outpost.begin_capture(&"veil", 1.0)
	_expect(not buildings.try_construct(&"player_top", &"front_b", &"farm"), "capture locks construction nodes", failures)


func _test_stabilized_capture_allows_rebuilding(economy_script: GDScript, building_service_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	var buildings: Variant = building_service_script.new(economy, _manifest())
	var outpost := OutpostState.new(&"veil", true)
	buildings.register_outpost(&"captured_top", outpost, [&"front_a"])
	outpost.begin_capture(&"lumern", 1.0)
	outpost.advance(20.0)
	outpost.advance(5.0)
	_expect(buildings.try_construct(&"captured_top", &"front_a", &"farm"), "a captured outpost accepts new construction after stabilization", failures)


func _test_deterministic_approved_roulette(economy_script: GDScript, building_service_script: GDScript, roulette_script: GDScript, failures: PackedStringArray) -> void:
	var first_manifest := _manifest()
	var first_economy: Variant = economy_script.new(first_manifest)
	var first_buildings: Variant = building_service_script.new(first_economy, first_manifest)
	var outpost := OutpostState.new(&"lumern")
	first_buildings.register_outpost(&"player_top", outpost, [&"front_a", &"front_b", &"rear"])
	_expect(first_buildings.try_construct(&"player_top", &"front_a", &"tower"), "tower construction succeeds", failures)
	_expect(first_buildings.try_construct(&"player_top", &"front_b", &"farm"), "farm construction succeeds", failures)
	_expect(first_buildings.roulette_token_sources().is_empty(), "tower and farm do not create unit roulette tokens", failures)
	_expect(first_buildings.try_construct(&"player_top", &"rear", &"barracks"), "barracks construction succeeds", failures)
	_expect(first_buildings.roulette_token_sources().size() == 1, "one completed barracks contributes one source token entry", failures)
	var first_roulette: Variant = roulette_script.new(first_economy, first_buildings, first_manifest, &"lumern")
	var first_result: Variant = first_roulette.spin({"seed": 12})
	_expect(first_result.accepted and first_result.board.size() == 9, "a paid spin resolves one deterministic 3x3 board result", failures)
	_expect(first_economy.gold >= 30, "construction and roulette charge approved costs before any possible gold payout", failures)
	var second_manifest := _manifest()
	var second_economy: Variant = economy_script.new(second_manifest)
	var second_buildings: Variant = building_service_script.new(second_economy, second_manifest)
	var second_outpost := OutpostState.new(&"lumern")
	second_buildings.register_outpost(&"player_top", second_outpost, [&"front_a", &"front_b", &"rear"])
	second_buildings.try_construct(&"player_top", &"front_a", &"tower")
	second_buildings.try_construct(&"player_top", &"front_b", &"farm")
	second_buildings.try_construct(&"player_top", &"rear", &"barracks")
	var second_roulette: Variant = roulette_script.new(second_economy, second_buildings, second_manifest, &"lumern")
	var second_result: Variant = second_roulette.spin({"seed": 12})
	_expect(JSON.stringify(first_result.to_dictionary()) == JSON.stringify(second_result.to_dictionary()), "identical seed and building snapshot reproduce the same roulette result", failures)
	_expect(first_manifest.input_log.size() == 4, "three constructions and the roulette result are recorded", failures)


func _test_deployment_food_limit(economy_script: GDScript, deployment_script: GDScript, failures: PackedStringArray) -> void:
	var manifest := _manifest()
	var economy: Variant = economy_script.new(manifest)
	var deployment: Variant = deployment_script.new(economy, manifest)
	var card := UnitSpawnDefinition.new()
	card.archetype_id = &"shield_guard"
	card.owner_team_id = &"lumern"
	card.visual_faction_id = &"lumern"
	card.food_cost = 12
	_expect(deployment.deploy(card, &"top", 10.0), "deployment reserves available food", failures)
	_expect(not deployment.deploy(card, &"top", 20.0), "deployment rejects cards that exceed the food cap", failures)
	_expect(economy.food_used == 12, "rejected deployment does not spend additional food", failures)
	_expect(manifest.input_log.size() == 1, "only accepted deployment commands are recorded", failures)


func _manifest() -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = "regular_stage"
	manifest.seed = 101
	manifest.starting_gold = 160
	manifest.starting_food_cap = 12
	return manifest


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Economy, construction, approved roulette, and deployment checks passed")
		quit(0)
	else:
		printerr("Economy, construction, roulette, and deployment failures:
%s" % "
".join(failures))
		quit(1)
