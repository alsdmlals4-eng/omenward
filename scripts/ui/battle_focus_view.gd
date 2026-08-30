# BATTLE 단계의 실제 단일 전선 상태를 가까운 교전 장면으로 투영한다.
class_name BattleFocusView
extends Control

const FRONT_ID := &"front"
const BATTLEFIELD_FOUNDATION := preload("res://assets/art/battlefield/omenward_close_single_front_foundation_v1.png")
const LUMERN_LOW_SLAB_CLUSTER := preload("res://assets/art/battlefield/props/omenward_lumern_low_slab_cluster_v1.png")
const LUMERN_MEADOW_BANK := preload("res://assets/art/battlefield/props/omenward_lumern_meadow_bank_v1.png")
const LUMERN_BLUE_FLOWER_BANK := preload("res://assets/art/battlefield/props/omenward_lumern_blue_flower_bank_v1.png")
const VEIL_RUBBLE := preload("res://assets/art/battlefield/props/omenward_veil_rubble_v1.png")
const VEIL_CRYSTAL_CLUSTER := preload("res://assets/art/battlefield/props/omenward_veil_crystal_cluster_v1.png")
const VEIL_THORN_BRUSH := preload("res://assets/art/battlefield/props/omenward_veil_thorn_brush_v1.png")
const LUMERN_SHIELD_GUARD_TEXTURE := preload("res://assets/art/units/lumern_shield_guard_storybook_idle_v1.png")
const VEIL_SHIELD_GUARD_TEXTURE := preload("res://assets/art/units/veil_shield_guard_storybook_idle_v1.png")
const WARD_COLOR := Color(0.42, 0.7, 1.0, 1.0)
const VEIL_COLOR := Color(0.76, 0.38, 0.82, 1.0)
const LUMERN_PROP_MAX_X_RATIO := 0.36
const VEIL_PROP_MIN_X_RATIO := 0.64
const UNIT_TRAVEL_Y_MIN_RATIO := 0.36
const UNIT_TRAVEL_Y_MAX_RATIO := 0.80

var run: Variant


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


func current_sector_id() -> StringName:
	if run == null or run.battle == null:
		return &"ward_forward"
	var route: Dictionary = run.battle.route_state_for(FRONT_ID)
	if StringName((route.get("ward_forward", {}) as Dictionary).get("owner_team_id", &"")) != &"lumern":
		return &"ward_forward"
	if StringName((route.get("clash", {}) as Dictionary).get("owner_team_id", &"")) != &"lumern":
		return &"clash"
	if StringName((route.get("veil_forward", {}) as Dictionary).get("owner_team_id", &"")) != &"lumern":
		return &"veil_forward"
	return &"veil_citadel"


func displayed_unit_count() -> int:
	if run == null or run.battle == null:
		return 0
	return mini(6, (run.battle.front_units(FRONT_ID) as Array).size())


func _process(_delta: float) -> void:
	queue_redraw()


func _draw() -> void:
	if size.x <= 0.0 or size.y <= 0.0:
		return
	var frame := StyleBoxFlat.new()
	frame.bg_color = Color(0.015, 0.03, 0.05, 0.96)
	frame.border_width_left = 2
	frame.border_width_top = 2
	frame.border_width_right = 2
	frame.border_width_bottom = 2
	frame.border_color = Color(0.75, 0.64, 0.38, 0.92)
	frame.corner_radius_top_left = 8
	frame.corner_radius_top_right = 8
	frame.corner_radius_bottom_left = 8
	frame.corner_radius_bottom_right = 8
	draw_style_box(frame, Rect2(Vector2.ZERO, size))
	var combat_rect := Rect2(Vector2(8.0, 31.0), Vector2(maxf(1.0, size.x - 16.0), maxf(1.0, size.y - 39.0)))
	draw_texture_rect(BATTLEFIELD_FOUNDATION, combat_rect, false, Color.WHITE)
	draw_rect(combat_rect, Color(0.02, 0.04, 0.08, 0.12), true)
	_draw_territory_props(combat_rect)
	_draw_header()
	_draw_fixed_tower(combat_rect)
	_draw_live_units(combat_rect)
	_draw_footer(combat_rect)


func terrain_prop_layout(combat_rect: Rect2) -> Array:
	# 통행·교전 구간은 y_ratio 0.36..0.80으로 비워 둔다. 이 사각형들은
	# 단지 유닛보다 먼저 그려지는 것이 아니라, 그 구간을 기하적으로 피한다.
	return [
		{
			"id": &"lumern_low_slabs",
			"x_ratio": 0.12,
			"texture": LUMERN_LOW_SLAB_CLUSTER,
			"rect": _prop_rect(combat_rect, 0.03, 0.04, 0.20, 0.18),
		},
		{
			"id": &"lumern_meadow_bank",
			"x_ratio": 0.26,
			"texture": LUMERN_MEADOW_BANK,
			"rect": _prop_rect(combat_rect, 0.18, 0.84, 0.16, 0.12),
		},
		{
			"id": &"lumern_blue_flower_bank",
			"x_ratio": 0.29,
			"texture": LUMERN_BLUE_FLOWER_BANK,
			"rect": _prop_rect(combat_rect, 0.22, 0.82, 0.14, 0.14),
		},
		{
			"id": &"veil_rubble",
			"x_ratio": 0.86,
			"texture": VEIL_RUBBLE,
			"rect": _prop_rect(combat_rect, 0.75, 0.05, 0.21, 0.20),
		},
		{
			"id": &"veil_crystal_cluster",
			"x_ratio": 0.78,
			"texture": VEIL_CRYSTAL_CLUSTER,
			"rect": _prop_rect(combat_rect, 0.68, 0.82, 0.19, 0.16),
		},
		{
			"id": &"veil_thorn_brush",
			"x_ratio": 0.91,
			"texture": VEIL_THORN_BRUSH,
			"rect": _prop_rect(combat_rect, 0.84, 0.11, 0.14, 0.17),
		},
	]


func _prop_rect(combat_rect: Rect2, x_ratio: float, y_ratio: float, width_ratio: float, height_ratio: float) -> Rect2:
	return Rect2(
		combat_rect.position + Vector2(combat_rect.size.x * x_ratio, combat_rect.size.y * y_ratio),
		Vector2(combat_rect.size.x * width_ratio, combat_rect.size.y * height_ratio)
	)


func _draw_territory_props(combat_rect: Rect2) -> void:
	for placement in terrain_prop_layout(combat_rect):
		var prop_texture := placement.get("texture") as Texture2D
		if prop_texture != null and is_terrain_prop_placement_allowed(placement, combat_rect):
			var prop_rect: Rect2 = placement.get("rect", Rect2())
			draw_texture_rect(prop_texture, prop_rect, false, Color.WHITE)


func is_terrain_prop_placement_allowed(placement: Dictionary, combat_rect: Rect2) -> bool:
	var prop_id := str(placement.get("id", &""))
	var x_ratio := float(placement.get("x_ratio", -1.0))
	var prop_rect: Rect2 = placement.get("rect", Rect2())
	var is_faction_band := false
	if prop_id.begins_with("lumern_"):
		is_faction_band = x_ratio <= LUMERN_PROP_MAX_X_RATIO and prop_rect.end.x <= combat_rect.position.x + combat_rect.size.x * LUMERN_PROP_MAX_X_RATIO
	elif prop_id.begins_with("veil_"):
		is_faction_band = x_ratio >= VEIL_PROP_MIN_X_RATIO and prop_rect.position.x >= combat_rect.position.x + combat_rect.size.x * VEIL_PROP_MIN_X_RATIO
	if not is_faction_band:
		return false
	return not prop_rect.intersects(_unit_travel_corridor(combat_rect))


func _unit_travel_corridor(combat_rect: Rect2) -> Rect2:
	return Rect2(
		combat_rect.position + Vector2(0.0, combat_rect.size.y * UNIT_TRAVEL_Y_MIN_RATIO),
		Vector2(combat_rect.size.x, combat_rect.size.y * (UNIT_TRAVEL_Y_MAX_RATIO - UNIT_TRAVEL_Y_MIN_RATIO))
	)


func _draw_header() -> void:
	var sector := current_sector_id()
	draw_string(ThemeDB.fallback_font, Vector2(14.0, 21.0), "전투 초점 · %s" % _sector_title(sector), HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color(0.98, 0.93, 0.76, 1.0))
	var counts := _unit_counts()
	draw_string(ThemeDB.fallback_font, Vector2(maxf(176.0, size.x - 168.0), 21.0), "수호 %d  ·  장막 %d" % [counts.get(&"lumern", 0), counts.get(&"veil", 0)], HORIZONTAL_ALIGNMENT_RIGHT, 150.0, 12, Color(0.9, 0.94, 0.98, 0.96))


func _draw_fixed_tower(combat_rect: Rect2) -> void:
	if run == null or run.battle == null or not run.battle.fixed_towers.has(FRONT_ID):
		return
	var tower: Variant = run.battle.fixed_towers[FRONT_ID]
	var color := Color(0.42, 0.46, 0.54, 0.96)
	if tower.active and tower.owner_team_id == &"lumern":
		color = WARD_COLOR
	elif tower.active and tower.owner_team_id == &"veil":
		color = VEIL_COLOR
	var tower_origin := combat_rect.position + Vector2(combat_rect.size.x * 0.18, combat_rect.size.y * 0.58)
	draw_rect(Rect2(tower_origin - Vector2(7.0, 20.0), Vector2(14.0, 31.0)), color, true)
	draw_rect(Rect2(tower_origin - Vector2(9.0, 22.0), Vector2(18.0, 35.0)), Color(0.01, 0.02, 0.04, 0.78), false, 1.5)
	draw_circle(tower_origin + Vector2(0.0, -23.0), 5.0, color)
	draw_string(ThemeDB.fallback_font, tower_origin + Vector2(-26.0, 31.0), "방어탑", HORIZONTAL_ALIGNMENT_CENTER, 52.0, 10, Color(0.96, 0.9, 0.72, 0.96))


func _draw_live_units(combat_rect: Rect2) -> void:
	if run == null or run.battle == null:
		return
	var units: Array = run.battle.front_units(FRONT_ID)
	var index := 0
	for unit in units:
		if index >= 6:
			break
		var owner_team_id: StringName = unit.owner_team_id
		var texture := VEIL_SHIELD_GUARD_TEXTURE if owner_team_id == &"veil" else LUMERN_SHIELD_GUARD_TEXTURE
		var position_ratio := clampf(float(unit.lane_position) / 100.0, 0.12, 0.88)
		var center := combat_rect.position + Vector2(combat_rect.size.x * position_ratio, combat_rect.size.y * 0.62) + _formation_offset(index, owner_team_id)
		var faction_color := VEIL_COLOR if owner_team_id == &"veil" else WARD_COLOR
		draw_circle(center + Vector2(0.0, 24.0), 27.0, Color(0.01, 0.02, 0.04, 0.72))
		draw_circle(center + Vector2(0.0, 17.0), 31.0, Color(faction_color.r, faction_color.g, faction_color.b, 0.28))
		draw_arc(center + Vector2(0.0, 17.0), 32.0, 0.0, TAU, 20, Color(faction_color.r, faction_color.g, faction_color.b, 0.84), 1.25, true)
		draw_texture_rect(texture, Rect2(center - Vector2(37.0, 59.0), Vector2(74.0, 74.0)), false, Color.WHITE)
		_draw_unit_health(center, unit_health_ratio(unit), faction_color)
		index += 1


func _formation_offset(index: int, owner_team_id: StringName) -> Vector2:
	var row := index % 3
	var depth := float(index) / 3.0
	var direction := -1.0 if owner_team_id == &"lumern" else 1.0
	return Vector2(direction * float(row - 1) * 18.0, -depth * 29.0 - float(row) * 7.0)


func unit_health_ratio(unit: Variant) -> float:
	if unit == null or not unit.has_method("combat_stats"):
		return 0.0
	var stats: Dictionary = unit.combat_stats()
	var max_health := float(stats.get("max_health", 0.0))
	return clampf(float(unit.health) / maxf(1.0, max_health), 0.0, 1.0)


func _draw_unit_health(center: Vector2, health_ratio: float, faction_color: Color) -> void:
	var width := 40.0
	var bar_rect := Rect2(center + Vector2(-width * 0.5, 31.0), Vector2(width, 4.0))
	draw_rect(bar_rect, Color(0.015, 0.02, 0.03, 0.9), true)
	draw_rect(Rect2(bar_rect.position, Vector2(width * health_ratio, 4.0)), faction_color, true)


func _draw_footer(combat_rect: Rect2) -> void:
	var sector_hint := "전진기지 확보 전" if current_sector_id() == &"ward_forward" else "현 구간 교전 중"
	draw_string(ThemeDB.fallback_font, combat_rect.position + Vector2(10.0, combat_rect.size.y - 10.0), sector_hint, HORIZONTAL_ALIGNMENT_LEFT, -1, 10, Color(0.95, 0.92, 0.8, 0.96))


func _unit_counts() -> Dictionary:
	var counts := {&"lumern": 0, &"veil": 0}
	if run == null or run.battle == null:
		return counts
	for unit in run.battle.front_units(FRONT_ID):
		var owner_team_id: StringName = unit.owner_team_id
		counts[owner_team_id] = int(counts.get(owner_team_id, 0)) + 1
	return counts


func _sector_title(sector_id: StringName) -> String:
	match sector_id:
		&"ward_forward": return "수호 전진기지"
		&"clash": return "접전지"
		&"veil_forward": return "장막 전진기지"
		&"veil_citadel": return "장막 성채"
	return "수호 성채"
