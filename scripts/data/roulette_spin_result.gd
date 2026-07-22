class_name RouletteSpinResult
extends RefCounted

var accepted := false
var failure_reason: StringName = &""
var board: Array[StringName] = []
var judging_symbol: StringName = &""
var completed_line_count := 0
var rank_id: StringName = &""
var outcome_type: StringName = &"none"
var rewards: Array[UnitSpawnDefinition] = []
var gold_reward := 0
var paid_cost := 0
var spin_seed := 0
var source_building_id: StringName = &""
var source_tier_id: StringName = &""
var legendary_converted_to_heroes := false
var template_resolution: StringName = &""


func to_dictionary() -> Dictionary:
	var reward_dictionaries: Array[Dictionary] = []
	for reward in rewards:
		reward_dictionaries.append(reward.to_dictionary())
	return {
		"accepted": accepted,
		"failure_reason": str(failure_reason),
		"board": board.map(func(symbol: StringName) -> String: return str(symbol)),
		"judging_symbol": str(judging_symbol),
		"completed_line_count": completed_line_count,
		"rank_id": str(rank_id),
		"outcome_type": str(outcome_type),
		"rewards": reward_dictionaries,
		"gold_reward": gold_reward,
		"paid_cost": paid_cost,
		"spin_seed": spin_seed,
		"source_building_id": str(source_building_id),
		"source_tier_id": str(source_tier_id),
		"legendary_converted_to_heroes": legendary_converted_to_heroes,
		"template_resolution": str(template_resolution),
	}
