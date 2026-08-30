class_name CoreUxService
extends RefCounted

const PLAYER_TEAM_ID := &"lumern"
const ENEMY_TEAM_ID := &"veil"
const FRONT_IDS := [&"front"]
var run: Variant
var registry: Variant
var _wave_metrics := {}
var _unit_registration := {}
var _defeat_recorded := {}
var _wave_reports: Array[Dictionary] = []


func _init(assigned_run: Variant, assigned_registry: Variant) -> void:
	run = assigned_run
	registry = assigned_registry


func reset() -> void:
	_wave_metrics.clear()
	_unit_registration.clear()
	_defeat_recorded.clear()
	_wave_reports.clear()


func register_wave(wave: Variant, spawned_units: Array[Dictionary]) -> void:
	if wave == null:
		return
	var wave_number := int(wave.wave_number)
	var metrics := {
		"wave_number": wave_number,
		"enemy_unit_ids": [],
		"reported": false,
		"fronts": _empty_front_metrics(),
	}
	for record in spawned_units:
		var unit_id := int(record.get("unit_id", -1))
		if unit_id <= 0:
			continue
		var front_id := StringName(record.get("front_id", record.get("lane_id", &"")))
		var team_id := StringName(record.get("team_id", &""))
		_unit_registration[unit_id] = {
			"wave_number": wave_number,
			"front_id": front_id,
			"team_id": team_id,
		}
		if team_id == ENEMY_TEAM_ID:
			(metrics["enemy_unit_ids"] as Array).append(unit_id)
	_wave_metrics[wave_number] = metrics


func observe_unit_delta(before_units: Array, after_units: Array) -> void:
	var after_ids := {}
	for unit in after_units:
		after_ids[int(unit.get("unit_id", -1))] = true
	for unit in before_units:
		var unit_id := int(unit.get("unit_id", -1))
		if unit_id <= 0 or after_ids.has(unit_id):
			continue
		if StringName(unit.get("owner_team_id", &"")) != PLAYER_TEAM_ID:
			continue
		var wave_number := _latest_active_wave_number()
		if wave_number <= 0:
			continue
		var front_id := StringName(unit.get("front_id", unit.get("lane_id", &"")))
		_increment_front_metric(wave_number, front_id, "allied_lost", 1.0)


func consume_battle_events(events: Array[Dictionary]) -> void:
	for event in events:
		var event_type := StringName(event.get("event_type", &""))
		var front_id := StringName(event.get("front_id", event.get("lane_id", &"")))
		var wave_number := _latest_active_wave_number()
		if wave_number <= 0 or not FRONT_IDS.has(front_id):
			continue
		match event_type:
			&"objective_state":
				_increment_front_metric(wave_number, front_id, "objective_changes", 1.0)
			&"gate_damage":
				var damage := float(event.get("damage", 0.0))
				if StringName(event.get("attacker_team", &"")) == PLAYER_TEAM_ID:
					_increment_front_metric(wave_number, front_id, "gate_damage_dealt", damage)
				else:
					_increment_front_metric(wave_number, front_id, "gate_damage_taken", damage)
			&"base_damage":
				var base_damage := float(event.get("damage", 0.0))
				if StringName(event.get("attacker_team", &"")) == PLAYER_TEAM_ID:
					_increment_front_metric(wave_number, front_id, "base_damage_dealt", base_damage)
				else:
					_increment_front_metric(wave_number, front_id, "base_damage_taken", base_damage)


func update_wave_reports() -> void:
	var wave_numbers: Array = _wave_metrics.keys()
	wave_numbers.sort()
	for value in wave_numbers:
		var wave_number := int(value)
		var metrics: Dictionary = _wave_metrics[wave_number]
		if bool(metrics.get("reported", false)):
			continue
		var enemy_unit_ids: Array = metrics.get("enemy_unit_ids", [])
		if enemy_unit_ids.is_empty():
			continue
		var all_defeated := true
		for unit_id_value in enemy_unit_ids:
			var unit_id := int(unit_id_value)
			if run.battle.is_unit_alive(unit_id):
				all_defeated = false
				continue
			_record_enemy_defeat(unit_id)
		if all_defeated:
			_finalize_wave_report(wave_number)


func snapshot() -> Dictionary:
	var token_sources: Array[Dictionary] = []
	if run != null and run.buildings != null:
		token_sources = run.buildings.roulette_token_sources_snapshot()
	return {
		"token_ledger": run.roulette.token_ledger_from_sources(token_sources) if run != null and run.roulette != null else [],
		"construction_comparison": _construction_comparison(token_sources),
		"omen": _omen_snapshot(),
		"tactical_overlay": _tactical_overlay_snapshot(),
		"latest_wave_report": _wave_reports.back().duplicate(true) if not _wave_reports.is_empty() else {},
		"wave_reports": _wave_reports.duplicate(true),
	}


func _construction_comparison(token_sources: Array[Dictionary]) -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	if run == null or run.buildings == null or run.economy == null or run.roulette == null:
		return result
	for entry in run.buildings.available_definitions_snapshot():
		var building_id := StringName(entry.get("building_id", ""))
		var definition: Variant = run.buildings.definitions.get(building_id)
		if definition == null:
			continue
		var block_reason := StringName(entry.get("install_block_reason", ""))
		var source := _preview_source(definition)
		var symbol_id := StringName(entry.get("roulette_symbol_id", ""))
		var before_probability: float = float(run.roulette.probability_for_symbol_from_sources(symbol_id, token_sources)) if symbol_id != &"" else 0.0
		var preview_sources: Array[Dictionary] = []
		if not source.is_empty():
			preview_sources.append(source)
		var after_probability: float = float(run.roulette.probability_for_symbol_from_sources(symbol_id, token_sources, preview_sources)) if not preview_sources.is_empty() else before_probability
		result.append({
			"building_id": str(building_id),
			"display_name": str(entry.get("display_name", "")),
			"gold_cost": int(entry.get("gold_cost", 0)),
			"food_cap_bonus": int(entry.get("food_cap_bonus", 0)),
			"roulette_symbol_id": str(symbol_id),
			"roulette_board_weight": int(entry.get("roulette_board_weight", 0)),
			"reward_archetype_id": str(entry.get("reward_archetype_id", "")),
			"can_construct": block_reason == &"" and bool(entry.get("runtime_available", false)),
			"block_reason": str(block_reason),
			"probability_before": before_probability,
			"probability_after": after_probability,
			"probability_delta": after_probability - before_probability,
		})
	return result


func _preview_source(definition: Variant) -> Dictionary:
	if StringName(definition.roulette_symbol_id) == &"" or int(definition.roulette_board_weight) <= 0:
		return {}
	return {
		"symbol_id": definition.roulette_symbol_id,
		"reward_archetype_id": definition.roulette_reward_archetype_id,
		"board_weight": definition.roulette_board_weight,
		"source_tier_id": definition.roulette_source_tier_id,
		"source_weight": definition.roulette_source_weight,
		"source_building_id": StringName("preview:%s" % definition.building_id),
	}


func _omen_snapshot() -> Dictionary:
	if run == null or run.wave_director == null:
		return {"phase": "complete", "seconds_remaining": 0.0}
	var wave: Variant = run.wave_director.next_wave()
	var phase := StringName(run.wave_director.omen_phase())
	var snapshot := {
		"phase": str(phase),
		"seconds_remaining": float(run.wave_director.seconds_until_next_wave()),
		"wave_number": int(wave.wave_number) if wave != null else 0,
		"danger_front": "",
		"fronts": [],
	}
	if wave == null or phase == &"countdown":
		return snapshot
	var front_data := {}
	for front_id in FRONT_IDS:
		front_data[front_id] = {
			"front_id": str(front_id),
			"count": 0,
			"roles": [],
			"units": [],
		}
	for spawn in wave.spawns:
		var front_id := StringName(spawn.lane_id)
		if not front_data.has(front_id):
			continue
		var profile: Variant = registry.archetypes.get(str(spawn.archetype_id)) if registry != null else null
		var entry: Dictionary = front_data[front_id]
		entry["count"] = int(entry["count"]) + 1
		var roles: Array = entry["roles"]
		var role: String = str(profile.role) if profile != null else "unknown"
		if not roles.has(role):
			roles.append(role)
		if phase == &"t15" or phase == &"t5" or phase == &"now":
			(entry["units"] as Array).append({
				"archetype_id": str(spawn.archetype_id),
				"role": role,
				"counter_tags": Array(profile.counter_tags) if profile != null else [],
			})
		front_data[front_id] = entry
	var danger_front := &""
	var danger_count := -1
	for front_id in FRONT_IDS:
		var entry: Dictionary = front_data[front_id]
		(entry["roles"] as Array).sort()
		(entry["units"] as Array).sort_custom(func(a: Dictionary, b: Dictionary) -> bool: return str(a.get("archetype_id", "")) < str(b.get("archetype_id", "")))
		(snapshot["fronts"] as Array).append(entry)
		if int(entry["count"]) > danger_count:
			danger_count = int(entry["count"])
			danger_front = front_id
	if phase == &"t5" or phase == &"now":
		snapshot["danger_front"] = str(danger_front)
	return snapshot


func _tactical_overlay_snapshot() -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	if run == null or run.battle == null:
		return result
	var battle_snapshot: Dictionary = run.battle.snapshot()
	for unit in battle_snapshot.get("units", []):
		if float(unit.get("health", 0.0)) <= 0.0:
			continue
		result.append({
			"unit_id": int(unit.get("unit_id", -1)),
			"archetype_id": str(unit.get("archetype_id", "")),
			"owner_team_id": str(unit.get("owner_team_id", "")),
			"front_id": str(unit.get("front_id", unit.get("lane_id", ""))),
			"role": str(unit.get("role", "")),
			"attack_range": float(unit.get("attack_range", 0.0)),
			"target_unit_id": int(unit.get("target_unit_id", -1)),
			"counter_tags": (unit.get("counter_tags", []) as Array).duplicate(),
			"target_priority_tags": (unit.get("target_priority_tags", []) as Array).duplicate(),
			"state": str(unit.get("state", "")),
		})
	result.sort_custom(func(a: Dictionary, b: Dictionary) -> bool:
		var front_compare := FRONT_IDS.find(StringName(a.get("front_id", &""))) - FRONT_IDS.find(StringName(b.get("front_id", &"")))
		if front_compare != 0:
			return front_compare < 0
		if str(a.get("owner_team_id", "")) != str(b.get("owner_team_id", "")):
			return str(a.get("owner_team_id", "")) < str(b.get("owner_team_id", ""))
		return int(a.get("unit_id", 0)) < int(b.get("unit_id", 0))
	)
	return result


func _record_enemy_defeat(unit_id: int) -> void:
	if _defeat_recorded.has(unit_id) or not _unit_registration.has(unit_id):
		return
	var registration: Dictionary = _unit_registration[unit_id]
	if StringName(registration.get("team_id", &"")) != ENEMY_TEAM_ID:
		return
	_defeat_recorded[unit_id] = true
	_increment_front_metric(
		int(registration.get("wave_number", 0)),
		StringName(registration.get("front_id", &"")),
		"enemy_defeated",
		1.0,
	)


func _finalize_wave_report(wave_number: int) -> void:
	if not _wave_metrics.has(wave_number):
		return
	var metrics: Dictionary = _wave_metrics[wave_number]
	if bool(metrics.get("reported", false)):
		return
	metrics["reported"] = true
	_wave_metrics[wave_number] = metrics
	var fronts: Array[Dictionary] = []
	for front_id in FRONT_IDS:
		var front_metrics: Dictionary = (metrics["fronts"] as Dictionary)[front_id]
		var front_report := front_metrics.duplicate(true)
		front_report["front_id"] = str(front_id)
		front_report["cause_code"] = _cause_code(front_metrics)
		fronts.append(front_report)
	var report := {
		"wave_number": wave_number,
		"fronts": fronts,
	}
	_wave_reports.append(report)
	if _wave_reports.size() > 3:
		_wave_reports.pop_front()
	if run.manifest != null:
		run.manifest.input_log.append({"action": "wave_report", "report": report.duplicate(true)})


func _cause_code(metrics: Dictionary) -> String:
	if float(metrics.get("gate_damage_taken", 0.0)) > 0.0 or float(metrics.get("base_damage_taken", 0.0)) > 0.0:
		return "gate_under_pressure"
	if int(metrics.get("allied_lost", 0)) > int(metrics.get("enemy_defeated", 0)):
		return "heavy_losses"
	if int(metrics.get("objective_changes", 0)) > 0:
		return "objective_swing"
	if int(metrics.get("enemy_defeated", 0)) > 0 and int(metrics.get("allied_lost", 0)) == 0:
		return "clean_defense"
	if int(metrics.get("enemy_defeated", 0)) > 0:
		return "attrition"
	return "no_contact"


func _increment_front_metric(wave_number: int, front_id: StringName, key: String, amount: float) -> void:
	if not _wave_metrics.has(wave_number) or not FRONT_IDS.has(front_id):
		return
	var metrics: Dictionary = _wave_metrics[wave_number]
	var fronts: Dictionary = metrics["fronts"]
	var front_metrics: Dictionary = fronts[front_id]
	if key in ["enemy_defeated", "allied_lost", "objective_changes"]:
		front_metrics[key] = int(front_metrics.get(key, 0)) + int(amount)
	else:
		front_metrics[key] = float(front_metrics.get(key, 0.0)) + amount
	fronts[front_id] = front_metrics
	metrics["fronts"] = fronts
	_wave_metrics[wave_number] = metrics


func _latest_active_wave_number() -> int:
	var wave_numbers: Array = _wave_metrics.keys()
	wave_numbers.sort()
	for index in range(wave_numbers.size() - 1, -1, -1):
		var wave_number := int(wave_numbers[index])
		if not bool((_wave_metrics[wave_number] as Dictionary).get("reported", false)):
			return wave_number
	return 0


func _empty_front_metrics() -> Dictionary:
	var result := {}
	for front_id in FRONT_IDS:
		result[front_id] = {
			"enemy_defeated": 0,
			"allied_lost": 0,
			"objective_changes": 0,
			"gate_damage_dealt": 0.0,
			"gate_damage_taken": 0.0,
			"base_damage_dealt": 0.0,
			"base_damage_taken": 0.0,
		}
	return result
