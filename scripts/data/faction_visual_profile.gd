class_name FactionVisualProfile
extends Resource

@export var archetype_id: StringName
@export var visual_faction_id: StringName
@export var display_name: String
@export var palette_color: Color = Color.WHITE
@export var idle_texture: Texture2D
@export var idle_pivot: Vector2 = Vector2.ZERO
@export var idle_mirror_for_veil: bool = true
