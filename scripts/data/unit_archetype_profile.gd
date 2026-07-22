class_name UnitArchetypeProfile
extends Resource

@export var archetype_id: StringName
@export var display_name: String
@export var role: String
@export var base_stats: Dictionary = {}
@export_range(0.0, 2.0, 0.05) var capture_power: float = 1.0
@export var structure_damage_tags: PackedStringArray = PackedStringArray(["normal"])
@export var attack_profile_id: StringName
@export var animation_contract_id: StringName
