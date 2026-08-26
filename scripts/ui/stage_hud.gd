class_name StageHud
extends Control

@onready var _gold_label: Label = $GoldLabel
@onready var _food_label: Label = $FoodLabel
@onready var _wave_label: Label = $WaveLabel
@onready var _omen_label: Label = $OmenLabel
@onready var _omen_detail_label: Label = $OmenDetailLabel
@onready var _token_ledger_label: Label = $TokenLedgerLabel
@onready var _construction_comparison_label: Label = $ConstructionComparisonLabel
@onready var _tactical_overlay_label: Label = $TacticalOverlayLabel
@onready var _wave_report_label: Label = $WaveReportLabel
@onready var _cards_label: Label = $CardsLabel
@onready var _result_label: Label = $ResultLabel
@onready var _retry_button: Button = $RetryButton
@onready var _barracks_button: Button = $BarracksButton
@onready var _tower_button: Button = $TowerButton
@onready var _farm_button: Button = $FarmButton

var run: Variant
var _spin_index := 0


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_update_display()


func _process(_delta: float) -> void:
	_update_display()


func _on_spin_pressed() -> void:
	if run == null:
		return
	_spin_index += 1
	run.spin_roulette({"seed": _spin_index})
	_update_display()


func _on_barracks_pressed() -> void:
	if run != null:
		run.construct_home(&"barracks")
	_update_display()


func _on_tower_pressed() -> void:
	if run != null:
		run.construct_home(&"tower")
	_update_display()


func _on_farm_pressed() -> void:
	if run != null:
		run.construct_home(&"farm")
	_update_display()


func _on_deploy_pressed(lane_id: StringName) -> void:
	if run != null:
		run.deploy_next_roulette_reward(lane_id)
	_update_display()


func _on_retry_pressed() -> void:
	var session := get_node_or_null("../../GameSession")
	if session != null:
		session.retry_stage()


func _update_display() -> void:
	if run == null or run.economy == null:
		return
	_gold_label.text = "Gold %d" % run.economy.gold
	_food_label.text = "Food %d/%d" % [run.economy.food_used, run.economy.food_cap]
	_wave_label.text = "Wave %d" % run.current_wave
	var omen: float = float(run.wave_director.seconds_until_next_wave()) if run.wave_director != null else 0.0
	_omen_label.text = "Next wave %.0fs" % omen
	var result: Variant = run.last_roulette_result
	var board_text := "-"
	var outcome_text := "none"
	if result != null:
		board_text = ",".join(result.board.map(func(symbol: StringName) -> String: return str(symbol)))
		outcome_text = "%s %s lines=%d gold=%d" % [str(result.outcome_type), str(result.rank_id), result.completed_line_count, result.gold_reward]
		if not result.accepted and result.failure_reason != &"":
			outcome_text = "blocked: %s" % str(result.failure_reason)
	_cards_label.text = "Board [%s]\n%s | Pending %d" % [board_text, outcome_text, run.pending_roulette_rewards.size()]
	_update_core_ux(run.core_ux_snapshot())
	_result_label.visible = run.result_state != run.RUNNING
	_result_label.text = "Stage %s" % str(run.result_state).capitalize()
	_retry_button.visible = run.result_state != run.RUNNING


func _update_core_ux(snapshot: Dictionary) -> void:
	_render_token_ledger(snapshot.get("token_ledger", []))
	_render_construction_comparison(snapshot.get("construction_comparison", []))
	_render_omen(snapshot.get("omen", {}))
	_render_tactical_overlay(snapshot.get("tactical_overlay", []))
	_render_wave_report(snapshot.get("latest_wave_report", {}))


func _render_token_ledger(entries: Array) -> void:
	var lines := PackedStringArray(["TOKEN LEDGER"])
	for entry in entries:
		var source_ids := _string_list(entry.get("source_building_ids", []))
		var reward_ids := _string_list(entry.get("reward_archetype_ids", []))
		lines.append("%s w=%d p=%s src=%d" % [
			str(entry.get("symbol_id", "")),
			int(entry.get("weight", 0)),
			_format_percent(float(entry.get("probability", 0.0))),
			int(entry.get("source_count", 0)),
		])
		if source_ids != "" or reward_ids != "":
			lines.append("  ids=%s reward=%s" % [source_ids if source_ids != "" else "-", reward_ids if reward_ids != "" else "-"])
	_token_ledger_label.text = "\n".join(lines)


func _render_construction_comparison(entries: Array) -> void:
	var lines := PackedStringArray(["BUILD / ROULETTE PREVIEW"])
	for entry in entries:
		var building_id := str(entry.get("building_id", ""))
		var reason := str(entry.get("block_reason", ""))
		var state_text := "ready" if bool(entry.get("can_construct", false)) else reason
		var symbol := str(entry.get("roulette_symbol_id", ""))
		var delta := float(entry.get("probability_delta", 0.0))
		var delta_text := ("+" if delta >= 0.0 else "") + _format_percent(delta)
		lines.append("%s %dg food+%d [%s]" % [building_id, int(entry.get("gold_cost", 0)), int(entry.get("food_cap_bonus", 0)), state_text])
		if symbol != "":
			lines.append("  %s %s -> %s (%s)" % [
				symbol,
				_format_percent(float(entry.get("probability_before", 0.0))),
				_format_percent(float(entry.get("probability_after", 0.0))),
				delta_text,
			])
		_apply_build_button_state(building_id, bool(entry.get("can_construct", false)), reason)
	_construction_comparison_label.text = "\n".join(lines)


func _apply_build_button_state(building_id: String, can_construct: bool, reason: String) -> void:
	var button: Button
	match building_id:
		"barracks":
			button = _barracks_button
		"tower":
			button = _tower_button
		"farm":
			button = _farm_button
		_:
			return
	button.disabled = not can_construct
	button.tooltip_text = "Ready" if can_construct else reason


func _render_omen(omen: Dictionary) -> void:
	var phase := str(omen.get("phase", "complete"))
	var lines := PackedStringArray(["OMEN W%d %s T-%.0f" % [int(omen.get("wave_number", 0)), phase.to_upper(), float(omen.get("seconds_remaining", 0.0))]])
	for lane in omen.get("lanes", []):
		var count := int(lane.get("count", 0))
		if count <= 0:
			continue
		var lane_id := str(lane.get("lane_id", ""))
		var roles := _string_list(lane.get("roles", []))
		var danger := " !" if lane_id == str(omen.get("danger_lane", "")) else ""
		var units: Array = lane.get("units", [])
		if units.is_empty():
			lines.append("%s x%d roles=%s%s" % [lane_id, count, roles, danger])
		else:
			var unit_text := PackedStringArray()
			for unit in units:
				unit_text.append("%s{%s}" % [str(unit.get("archetype_id", "")), _string_list(unit.get("counter_tags", []))])
			lines.append("%s x%d %s%s" % [lane_id, count, ",".join(unit_text), danger])
	_omen_detail_label.text = "\n".join(lines)


func _render_tactical_overlay(entries: Array) -> void:
	var lines := PackedStringArray(["TACTICAL RANGE / TARGET"])
	var shown := 0
	for entry in entries:
		if shown >= 9:
			break
		var team := "L" if str(entry.get("owner_team_id", "")) == "lumern" else "V"
		var target_id := int(entry.get("target_unit_id", -1))
		lines.append("%s %s #%d %s R%.1f -> %s [%s] prio=%s" % [
			str(entry.get("lane_id", "")),
			team,
			int(entry.get("unit_id", -1)),
			str(entry.get("archetype_id", "")),
			float(entry.get("attack_range", 0.0)),
			str(target_id) if target_id > 0 else "none",
			_string_list(entry.get("counter_tags", [])),
			_string_list(entry.get("target_priority_tags", [])),
		])
		shown += 1
	if entries.is_empty():
		lines.append("no active units")
	elif entries.size() > shown:
		lines.append("+%d more" % (entries.size() - shown))
	_tactical_overlay_label.text = "\n".join(lines)


func _render_wave_report(report: Dictionary) -> void:
	var lines := PackedStringArray(["WAVE CAUSE REPORT"])
	if report.is_empty():
		lines.append("waiting for resolved wave")
		_wave_report_label.text = "\n".join(lines)
		return
	lines.append("Wave %d" % int(report.get("wave_number", 0)))
	for lane in report.get("lanes", []):
		lines.append("%s %s E%d/L%d obj%d gate +%.0f/-%.0f base +%.0f/-%.0f" % [
			str(lane.get("lane_id", "")),
			str(lane.get("cause_code", "")),
			int(lane.get("enemy_defeated", 0)),
			int(lane.get("allied_lost", 0)),
			int(lane.get("objective_changes", 0)),
			float(lane.get("gate_damage_dealt", 0.0)),
			float(lane.get("gate_damage_taken", 0.0)),
			float(lane.get("base_damage_dealt", 0.0)),
			float(lane.get("base_damage_taken", 0.0)),
		])
	_wave_report_label.text = "\n".join(lines)


func _format_percent(value: float) -> String:
	return "%.1f%%" % (value * 100.0)


func _string_list(values: Array) -> String:
	var result := PackedStringArray()
	for value in values:
		result.append(str(value))
	return ",".join(result)
