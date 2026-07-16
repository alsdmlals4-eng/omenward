class_name DeploymentService
extends RefCounted

const LANE_IDS := [&"top", &"middle", &"bottom"]

var economy: Variant
var manifest: Variant
var deployed_cards: Array[UnitSpawnDefinition] = []


func _init(assigned_economy: Variant, assigned_manifest: Variant) -> void:
	economy = assigned_economy
	manifest = assigned_manifest


func deploy(card: UnitSpawnDefinition, lane_id: StringName, position: float) -> bool:
	if card == null or not LANE_IDS.has(lane_id) or not economy.try_reserve_food(card.food_cost):
		return false
	var deployed := card.duplicate() as UnitSpawnDefinition
	deployed.lane_id = lane_id
	deployed_cards.append(deployed)
	manifest.input_log.append({
		"action": "deploy",
		"lane_id": str(lane_id),
		"position": position,
		"card": deployed.to_dictionary(),
	})
	return true
