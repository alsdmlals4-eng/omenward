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


func can_deploy_batch(cards: Array[UnitSpawnDefinition]) -> bool:
	if economy == null or cards.is_empty():
		return false
	var total_food := 0
	for card in cards:
		if card == null or not LANE_IDS.has(card.lane_id) or card.food_cost <= 0:
			return false
		total_food += card.food_cost
	return economy.food_used + total_food <= economy.food_cap


func deploy_batch(cards: Array[UnitSpawnDefinition], position: float) -> bool:
	if not can_deploy_batch(cards):
		return false
	var total_food := 0
	for card in cards:
		total_food += card.food_cost
	if not economy.try_reserve_food(total_food):
		return false
	for card in cards:
		var deployed := card.duplicate() as UnitSpawnDefinition
		deployed_cards.append(deployed)
		manifest.input_log.append({
			"action": "deploy",
			"lane_id": str(deployed.lane_id),
			"position": position,
			"card": deployed.to_dictionary(),
		})
	return true
