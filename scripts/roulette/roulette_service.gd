class_name RouletteService
extends RefCounted

const SPIN_COST := 20
const BOARD_SIZE := 9
const CENTER_LINE := [3, 4, 5]
const EVALUATION_LINES := [
	[0, 1, 2], [3, 4, 5], [6, 7, 8],
	[0, 3, 6], [1, 4, 7], [2, 5, 8],
	[0, 4, 8], [2, 4, 6],
]
const UnitSpawnDefinitionScript = preload("res://scripts/data/unit_spawn_definition.gd")
const DeterminismServiceScript = preload("res://scripts/core/determinism_service.gd")

var economy: Variant
var buildings: Variant
var manifest: Variant
var player_team_id: StringName
var last_resolution: Dictionary = {}


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
	last_resolution = evaluate_board(cards)
	if last_resolution.get("has_reward", false):
		for card in cards:
			if card.archetype_id == last_resolution["matched_symbol"]:
				card.rank_id = last_resolution["rank_id"]
	manifest.input_log.append({
		"action": "roulette",
		"seed": rng.seed,
		"cards": cards.map(func(card): return card.to_dictionary()),
		"resolution": last_resolution.duplicate(true),
	})
	return cards


func evaluate_board(cards: Array) -> Dictionary:
	var resolution := {
		"has_reward": false,
		"active_line": CENTER_LINE.duplicate(),
		"matched_symbol": &"",
		"completed_line_count": 0,
		"completed_lines": [],
		"rank_id": &"",
	}
	if cards.size() != BOARD_SIZE:
		return resolution
	var symbol: StringName = cards[CENTER_LINE[0]].archetype_id
	if symbol == &"" or symbol == &"x":
		return resolution
	for index in CENTER_LINE:
		if cards[index].archetype_id != symbol:
			return resolution
	var completed_lines: Array = []
	for line in EVALUATION_LINES:
		var is_complete := true
		for index in line:
			if cards[index].archetype_id != symbol:
				is_complete = false
				break
		if is_complete:
			completed_lines.append(line.duplicate())
	var line_count := completed_lines.size()
	resolution["has_reward"] = line_count > 0
	resolution["matched_symbol"] = symbol
	resolution["completed_line_count"] = line_count
	resolution["completed_lines"] = completed_lines
	resolution["rank_id"] = _rank_for_completed_lines(line_count)
	return resolution


func _rank_for_completed_lines(line_count: int) -> StringName:
	if line_count >= 8:
		return &"legendary"
	if line_count >= 3:
		return &"hero"
	if line_count == 2:
		return &"elite"
	if line_count == 1:
		return &"common"
	return &""
