class_name BuildingDefinition
extends Resource

@export var building_id: StringName
@export var display_name := ""
@export var gold_cost: int
@export var food_cap_bonus: int
@export var roulette_symbol_id: StringName
@export var roulette_reward_archetype_id: StringName
@export var roulette_board_weight: int
@export var roulette_source_tier_id: StringName = &"tier_1"
@export var roulette_source_weight: int = 1
@export var runtime_available := true
