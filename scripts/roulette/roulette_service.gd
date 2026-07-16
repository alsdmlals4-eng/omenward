class_name RouletteService
extends RefCounted

const SPIN_COST := 20
const BOARD_SIZE := 9
const UnitSpawnDefinitionScript = preload("res://scripts/data/unit_spawn_definition.gd")
const DeterminismServiceScript = preload("res://scripts/core/determinism_service.gd")

var economy: Variant
var buildings: Variant
var manifest: Variant
var player_team_id: StringName


func _init(assigned_economy: Variant, assigned_buildings: Variant, assigned_manifest: Variant, assigned_player_team_id: StringName) -> void:
	economy = assigned_economy
	buildings = assigned_buildings
	manifest = assigned_manifest
	player_team_id = assigned_player_team_id


func spin(seed_input: Dictionary) -> Array[UnitSpawnDefinition]:
	if not economy.try_spend_gold(SPIN_COST):
		return []
	var spin_seed := int(seed_input.get("seed", manifest.seed))
	var rng: RandomNumberGenerator = DeterminismServiceScript.new(manifest.seed).create_roulette_rng(spin_seed)
	var token_ids: Array[StringName] = buildings.roulette_archetype_ids()
	var cards: Array = []
	for index in BOARD_SIZE:
		var card: Variant = UnitSpawnDefinitionScript.new()
		card.archetype_id = token_ids[rng.randi_range(0, token_ids.size() - 1)]
		card.owner_team_id = player_team_id
		card.visual_faction_id = player_team_id
		cards.append(card)
	manifest.input_log.append({
		"action": "roulette",
		"seed": rng.seed,
		"cards": cards.map(func(card): return card.to_dictionary()),
	})
	return cards
