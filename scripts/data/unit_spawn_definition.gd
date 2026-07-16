class_name UnitSpawnDefinition
extends Resource

@export var archetype_id: StringName
@export var tier_id: StringName = &"tier_1"
@export var rank_id: StringName = &"common"
@export var owner_team_id: StringName
@export var visual_faction_id: StringName
@export var lane_id: StringName
@export var spawn_delay_seconds: float = 0.0
@export var food_cost: int = 1


func to_dictionary() -> Dictionary:
	return {
		"archetype_id": str(archetype_id),
		"tier_id": str(tier_id),
		"rank_id": str(rank_id),
		"owner_team_id": str(owner_team_id),
		"visual_faction_id": str(visual_faction_id),
		"lane_id": str(lane_id),
		"spawn_delay_seconds": spawn_delay_seconds,
		"food_cost": food_cost,
	}
