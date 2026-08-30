# BATTLE 단계의 실제 단일 전선 상태를 가까운 교전 장면으로 투영한다.
class_name BattleFocusView
extends Control

const FRONT_ID := &"front"
const BACKDROP := preload("res://assets/art/battlefield/ward_veil_three_lane_backdrop_v1.png")
const LUMERN_SHIELD_GUARD_TEXTURE := preload("res://assets/art/units/lumern_shield_guard_storybook_idle_v1.png")
const VEIL_SHIELD_GUARD_TEXTURE := preload("res://assets/art/units/veil_shield_guard_storybook_idle_v1.png")
const WARD_COLOR := Color(0.42, 0.7, 1.0, 1.0)
const VEIL_COLOR := Color(0.76, 0.38, 0.82, 1.0)
const CLASH_COLOR := Color(1.0, 0.7, 0.26, 1.0)
const BACKDROP_SOURCE_RECT := Rect2(0.0, 250.0, 1672.0, 430.0)

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
	draw_texture_rect_region(BACKDROP, combat_rect, BACKDROP_SOURCE_RECT, Color(0.8, 0.86, 0.98, 0.88))
	draw_rect(combat_rect, Color(0.02, 0.04, 0.08, 0.28), true)
	_draw_header()
	_draw_clash_focus(combat_rect)
	_draw_fixed_tower(combat_rect)
	_draw_live_units(combat_rect)
	_draw_footer(combat_rect)


func _draw_header() -> void:
	var sector := current_sector_id()
	draw_string(ThemeDB.fallback_font, Vector2(14.0, 21.0), "전투 초점 · %s" % _sector_title(sector), HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color(0.98, 0.93, 0.76, 1.0))
	var counts := _unit_counts()
	draw_string(ThemeDB.fallback_font, Vector2(maxf(176.0, size.x - 168.0), 21.0), "수호 %d  ·  장막 %d" % [counts.get(&"lumern", 0), counts.get(&"veil", 0)], HORIZONTAL_ALIGNMENT_RIGHT, 150.0, 12, Color(0.9, 0.94, 0.98, 0.96))


func _draw_clash_focus(combat_rect: Rect2) -> void:
	var center := combat_rect.get_center() + Vector2(0.0, 12.0)
	var color := CLASH_COLOR
	match current_sector_id():
		&"ward_forward": color = WARD_COLOR
		&"veil_forward", &"veil_citadel": color = VEIL_COLOR
	draw_circle(center, minf(46.0, combat_rect.size.y * 0.26), Color(color.r, color.g, color.b, 0.16))
	draw_arc(center, minf(46.0, combat_rect.size.y * 0.26), 0.0, TAU, 28, Color(color.r, color.g, color.b, 0.8), 1.5, true)


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
