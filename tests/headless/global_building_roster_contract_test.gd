extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const StageEconomy = preload("res://scripts/core/stage_economy.gd")
const BuildingService = preload("res://scripts/buildings/building_service.gd")
const BattleSimulator = preload("res://scripts/battle/battle_simulator.gd")
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const BATTLEFIELD_VIEW_PATH := "res://scripts/battle/battlefield_view.gd"


func _init() -> void:
	var failures := PackedStringArray()
	_test_global_roster_capacity_and_effect_lifecycle(failures)
	_test_fixed_tower_contract(failures)
	_test_income_boundary(failures)
	_test_stage_one_blocks_roster_mutation(failures)
	_test_battlefield_excludes_construction_nodes(failures)
	_finish(failures)


func _test_global_roster_capacity_and_effect_lifecycle(failures: PackedStringArray) -> void:
	var manifest := StageManifest.new()
	manifest.starting_gold = 500
	manifest.starting_food_cap = 12
	var economy := StageEconomy.new(manifest)
	var buildings: Variant = BuildingService.new(economy, manifest)
	_expect(buildings.has_method(&"set_roster_mutation_allowed"), "building service exposes the Stage 1 mutation gate", failures)
	_expect(buildings.has_method(&"sync_occupation_capacity"), "building service derives global roster capacity from stable objectives", failures)
	_expect(buildings.has_method(&"unlocked_slot_capacity"), "building service exposes the unlocked slot count", failures)
	_expect(buildings.has_method(&"try_install"), "building service installs through one global roster operation", failures)
	_expect(buildings.has_method(&"move_roster_entry"), "building service lets the player reorder owned global-roster entries", failures)
	_expect(buildings.has_method(&"roster_snapshot"), "building service exposes player-visible roster entries", failures)
	if not buildings.has_method(&"set_roster_mutation_allowed") or not buildings.has_method(&"sync_occupation_capacity") or not buildings.has_method(&"try_install") or not buildings.has_method(&"move_roster_entry") or not buildings.has_method(&"roster_snapshot"):
		return
	buildings.set_roster_mutation_allowed(true)
	buildings.sync_occupation_capacity(1, 1)
	_expect(buildings.unlocked_slot_capacity() == 8, "one stable Ward forward base and one stable clash zone unlock six plus two slots", failures)
	for _index in 6:
		_expect(buildings.try_install(&"barracks"), "top-priority base slots accept an available building", failures)
	_expect(buildings.try_install(&"farm"), "an available building installs into the first occupation slot", failures)
	_expect(economy.food_cap == 18, "an active farm applies its passive once", failures)
	_expect(buildings.move_roster_entry(6, 0), "the player can move a building from an occupation slot to the highest-priority slot", failures)
	var reordered_roster: Array = buildings.roster_snapshot()
	_expect(reordered_roster[0].get("building_id", "") == "farm" and reordered_roster[6].get("building_id", "") == "barracks", "reordering swaps owned entries without deleting either building", failures)
	buildings.sync_occupation_capacity(0, 0)
	var locked_roster: Array = buildings.roster_snapshot()
	_expect(locked_roster.size() > 6 and locked_roster[6].get("state", "") == "inactive_locked", "a capacity loss locks the lower-priority building instead of deleting it", failures)
	_expect(economy.food_cap == 18, "moving the farm into the top-priority slot keeps its food-cap effect active", failures)
	var token_manifest := StageManifest.new()
	token_manifest.starting_gold = 500
	var token_economy := StageEconomy.new(token_manifest)
	var token_buildings: Variant = BuildingService.new(token_economy, token_manifest)
	token_buildings.set_roster_mutation_allowed(true)
	token_buildings.sync_occupation_capacity(1, 1)
	for _index in 6:
		_expect(token_buildings.try_install(&"farm"), "base slots can contain passive buildings before a source is installed", failures)
	_expect(token_buildings.try_install(&"barracks"), "an occupation slot can contain a roulette source", failures)
	token_buildings.sync_occupation_capacity(0, 0)
	_expect(token_buildings.roulette_token_sources_snapshot().is_empty(), "an inactive building contributes no roulette TokenSource", failures)
	buildings.sync_occupation_capacity(1, 1)
	var restored_roster: Array = buildings.roster_snapshot()
	_expect(restored_roster.size() > 6 and restored_roster[6].get("state", "") == "active", "capacity recovery restores the same top-priority entry", failures)
	_expect(economy.food_cap == 18, "capacity recovery leaves the already-active top-priority passive applied exactly once", failures)


func _test_fixed_tower_contract(failures: PackedStringArray) -> void:
	var battle: Variant = BattleSimulator.new(_registry(), 901)
	var property_names := PackedStringArray()
	for property in battle.get_property_list():
		property_names.append(str(property.get("name", "")))
	_expect(property_names.has("fixed_towers"), "battle state owns one fixed-tower collection", failures)
	if not property_names.has("fixed_towers"):
		return
	var towers: Dictionary = battle.fixed_towers
	_expect(towers.size() == 1, "the battle exposes exactly one fixed tower for its one shared front", failures)
	_expect(towers.has(&"front"), "the single front owns the only fixed tower", failures)
	if not towers.has(&"front"):
		return
	var tower: Variant = towers[&"front"]
	_expect(tower.owner_team_id == &"" and not tower.active, "the tower stays neutral and inactive until Ward forward base is stabilized", failures)
	_expect(is_equal_approx(float(tower.capture_power), 0.0), "the fixed tower has zero capture power", failures)
	var ward_forward: Variant = battle.outposts[&"lumern"][&"front"]
	ward_forward.begin_capture(&"lumern", 2.0)
	ward_forward.advance(10.0)
	ward_forward.advance(5.0)
	battle.advance(0.1)
	_expect(tower.owner_team_id == &"lumern" and tower.active, "stabilized Ward forward base grants the only tower to Lumern", failures)
	ward_forward.begin_capture(&"veil", 1.0)
	battle.advance(0.1)
	_expect(not tower.active and tower.owner_team_id == &"", "a tower disables throughout neutralizing/capturing/stabilizing", failures)


func _test_income_boundary(failures: PackedStringArray) -> void:
	var manifest := StageManifest.new()
	manifest.starting_gold = 0
	manifest.starting_food_cap = 12
	var economy := StageEconomy.new(manifest)
	economy.advance(60.0, 1, 1)
	_expect(economy.gold == 23, "base, one clash, and one Ward forward base pay through their existing single income paths", failures)


func _test_stage_one_blocks_roster_mutation(failures: PackedStringArray) -> void:
	var tutorial: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var run: Variant = StageRun.new(StageProgression.new())
	run.start(tutorial, 902)
	_expect(run.has_method(&"install_building"), "StageRun exposes only global roster installation", failures)
	if run.has_method(&"install_building"):
		_expect(not run.install_building(&"farm"), "Stage 1 rejects direct roster mutation", failures)


func _test_battlefield_excludes_construction_nodes(failures: PackedStringArray) -> void:
	var source := FileAccess.get_file_as_string(BATTLEFIELD_VIEW_PATH)
	_expect(not source.contains("_draw_outpost_nodes"), "battlefield view has no construction-node drawing helper", failures)
	_expect(not source.contains("draw_circle(center + Vector2(-20, -14)"), "battlefield view has no visible construction-pad geometry", failures)
	_expect(source.contains("_draw_fixed_tower"), "battlefield view draws fixed tower ownership state", failures)


func _registry() -> Variant:
	var registry := DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not errors.is_empty():
		push_error("Global roster registry failed to load: %s" % errors)
	return registry


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Global building roster and fixed tower contracts passed")
		quit(0)
	else:
		printerr("Global building roster contract failures:\n%s" % "\n".join(failures))
		quit(1)
