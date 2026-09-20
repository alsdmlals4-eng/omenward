extends RefCounted
## Replan preview model. The blueprint owns base numbers; this model owns simulation.

const CATALOG_PATH := "res://docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json"
const SHIELD_WINDUP := 0.18
const SHIELD_IMPACT := 0.10
const SHIELD_RECOVERY := 0.15
const FIXED_RULESET := "fixed30-v1"
const TICK_RATE := 30
const MAX_FRAME_TICKS := 120
var ruleset_id := FIXED_RULESET
var tick := 0
# Debt is measured in ticks, including the fraction not yet executable.
var tick_debt := 0.0
var capture_rules := "timed_v1"
var capture: Array = [{"side": 0, "work": 0}, {"side": 0, "work": 0}, {"side": 0, "work": 0}]
var base_claim_work := 0
var basic_gold_paid := 0
var settled_maps: Array = []
var facility_rules := "slots_v1"
const BIRTH_RULES := ["birth_v1", "birth_v2"]
var birth_rules := "birth_v2"
var next_facility_id := 1
var next_entry_id := 1
var catalog: Dictionary
var definitions: Dictionary = {}
var facilities: Dictionary = {}
var branches: Dictionary = {}
var gold := 120
var phase := "PREPARE"
var round_number := 1
var elapsed := 0.0
var wave_index := 0
var wave_rules := "staggered_v1"
var map_pressure := 1.0
var current_map := 0
var held_points: Array = []
var map_entry: Dictionary = {}
var units: Array = []
var buildings: Array = []
var reserve: Array = []
var points: Array = [0, 0, 0]
var bases: Array = [1000.0, 1000.0]
var next_id := 0
var damage_events := 0
var rng := RandomNumberGenerator.new()
var free_spin := true
var last_board: Array = []
var omen_pending := false
var omen_moves := 0
var omen_reserved := 0
var message := "병영을 건설하고 공세를 시작하세요."
var income_clock := 0.0
var point_clock := 0.0
var tower_clock := 0.0
var front_rules := "single_v1"
var selected_front := 0
var combat_rules := "legacy"
var event_serial := 0
# Transient synchronous transaction only; snapshots are taken between impacts.
var _active_attack := 0

func front_count() -> int:
	return int(catalog.front_layout.count) if front_rules == "three_v1" else 1

func enable_three_fronts() -> bool:
	if phase != "PREPARE" or tick != 0 or current_map != 0 or not buildings.is_empty() or not reserve.is_empty() or omen_pending:
		return false
	front_rules = "three_v1"
	combat_rules = "proc_v1"
	selected_front = 0
	for i in range(units.size()):
		units[i].front = i % 3
	map_entry = snapshot(false)
	return true

func same_front(a: Dictionary, b: Dictionary) -> bool:
	return front_count() == 1 or a.get("front", 0) == b.get("front", 0)

func point_position(index: int) -> float:
	return float(catalog.front_layout.point_position) if front_count() == 3 else float(catalog.capture_rules.point_positions[index])

func point_contains(index: int, unit: Dictionary) -> bool:
	return (front_count() == 1 or unit.get("front", 0) == index) and absf(float(unit.x) - point_position(index)) <= float(catalog.capture_rules.radius)

func _init() -> void:
	catalog = JSON.parse_string(FileAccess.get_file_as_string(CATALOG_PATH))
	for row in catalog.units:
		definitions[row[0]] = row
	for row in catalog.buildings:
		facilities[row[0]] = row
	for row in catalog.building_tree:
		branches[row[0]] = row
	gold = int(catalog.economy.starting_gold)
	map_pressure = float(catalog.maps[0].pressure)
	rng.seed = 1947
	for i in range(4):
		spawn("shield_guard", 0, 8.0 + i * 1.4)
	map_entry = snapshot(false)

func unlocked_slots() -> int:
	return 6 + held_points.size() + points.count(1)

func next_map() -> bool:
	if phase != "VICTORY" or current_map + 1 >= catalog.maps.size():
		return false
	for i in range(points.size()):
		if points[i] == 1:
			held_points.append("%s:%d" % [catalog.maps[current_map].id, i])
	current_map += 1
	map_pressure = float(catalog.maps[current_map].pressure)
	# Loaded legacy runs retain their wave and simulation rules across maps.
	phase = "PREPARE"
	round_number = 1
	elapsed = 0.0
	wave_index = 0
	points = [0, 0, 0]
	capture = [{"side": 0, "work": 0}, {"side": 0, "work": 0}, {"side": 0, "work": 0}]
	base_claim_work = 0
	basic_gold_paid = 0
	bases = [1000.0, 1000.0]
	income_clock = 0.0
	point_clock = 0.0
	tower_clock = 0.0
	free_spin = true
	last_board = []
	units = units.filter(func(unit): return unit.side == 0 and unit.hp > 0)
	for i in range(units.size()):
		var unit: Dictionary = units[i]
		unit.x = 5.0 + (i % 9) * 0.4
		for key in ["cooldown", "flash", "action", "windup", "charge", "brace", "ambush", "air_reengage"]:
			unit[key] = 0.0
		unit.pending_target = -1
		unit.focus_target = -1
		unit.focus_count = 0
		unit.effects = {}
		unit.hit_count = 0
		unit.heal_count = 0
		if unit.has("pierce_count"):
			unit.pierce_count = 0
		if unit.has("counter_cd"):
			unit.counter_cd = 0.0
	message = "%s 진입 · 병력 체력/시설/골드 계승" % catalog.maps[current_map].name
	map_entry = snapshot(false)
	return true

func retry_map() -> bool:
	if phase != "DEFEAT" or map_entry.is_empty():
		return false
	var entry := map_entry.duplicate(true)
	if not restore(entry):
		return false
	map_entry = entry
	return true

func building_active(slot: int) -> bool:
	return building_present(slot) and slot < unlocked_slots()

func building_present(slot: int) -> bool:
	return slot >= 0 and slot < buildings.size() and buildings[slot].id != ""

func building_count() -> int:
	var count := 0
	for slot in range(buildings.size()):
		if building_present(slot):
			count += 1
	return count

func next_build_slot() -> int:
	for slot in range(unlocked_slots()):
		if not building_present(slot):
			return slot
	return -1

func demolish(slot: int) -> bool:
	if facility_rules != "slots_v1" or omen_pending or phase not in ["PREPARE", "REFIT"] or not building_active(slot):
		return false
	buildings[slot] = {"id": "", "unit": "", "clock": 0.0}
	message = "%d번 시설 철거 · 환급 없음 · 기존 병력/확정 대기 보존" % (slot + 1)
	return true

func wave_composition(round_id: int, wave_id: int) -> Dictionary:
	var cycle_index := round_id - 1 + (wave_id if wave_rules == "staggered_v1" else 0)
	var template: String = catalog.wave_cycle[cycle_index % catalog.wave_cycle.size()]
	var scale := map_pressure * (1.0 + 0.03 * (round_id - 1)) if wave_rules == "staggered_v1" else 1.0
	var composition: Dictionary = {}
	for group in catalog.wave_templates[template]:
		composition[group[0]] = composition.get(group[0], 0) + ceili(float(group[1]) * scale)
	return composition

func wave_forecast() -> Dictionary:
	if phase in ["VICTORY", "DEFEAT"]:
		return {}
	var next_round := round_number + (1 if phase == "REFIT" else 0)
	var next_wave := wave_index if phase == "BATTLE" else 0
	if next_round > int(catalog.maps[current_map].rounds) or next_wave >= catalog.economy.wave_times.size():
		return {}
	var composition := wave_composition(next_round, next_wave)
	# Same ordered distribution as staggered arrivals; inspection never changes it.
	var fronts: Array = []
	for front in range(front_count()):
		fronts.append({})
	var order := 0
	for role in composition:
		for i in range(int(composition[role])):
			var front := (order + next_wave) % front_count()
			fronts[front][role] = fronts[front].get(role, 0) + 1
			order += 1
	return {"round": next_round, "wave": next_wave + 1,
		"seconds": maxf(0, float(catalog.economy.wave_times[next_wave]) - (elapsed if phase == "BATTLE" else 0.0)),
		"units": composition, "fronts": fronts}

func production_status(slot: int) -> Dictionary:
	if not building_present(slot):
		return {"state": "EMPTY", "remaining": 0.0, "progress": 0.0}
	var building: Dictionary = buildings[slot]
	if building.id == "logistics":
		return {"state": "PASSIVE" if building_active(slot) else "LOCKED", "remaining": 0.0, "progress": 0.0}
	var interval: float = float(facilities[building.id][5])
	var state := "PRODUCING"
	if not building_active(slot):
		state = "LOCKED"
	elif phase != "BATTLE":
		state = "FROZEN"
	elif queue_used() + int(definitions[building.unit][11]) > int(catalog.economy.queue_capacity):
		state = "QUEUE_FULL"
	return {"state": state, "remaining": maxf(0, interval - float(building.clock)),
		"progress": clampf(float(building.clock) / interval, 0, 1)}

func construct(id: String) -> bool:
	if omen_pending or phase not in ["PREPARE", "REFIT"] or (id not in ["barracks", "special_barracks"] and not (id == "logistics" and facility_rules in ["logistics_v1", "slots_v1"])):
		return false
	var slot := next_build_slot()
	if slot < 0 or gold < int(facilities[id][2]):
		return false
	var role: String = "" if id == "logistics" else branches[id][4]
	if role == "random_special":
		role = catalog.unit_families.special[rng.randi_range(0, 4)]
	gold -= int(facilities[id][2])
	var building := {"id": id, "unit": role, "clock": 0.0}
	if birth_rules in BIRTH_RULES:
		building.instance_id = next_facility_id
		next_facility_id += 1
	if slot == buildings.size():
		buildings.append(building)
	else:
		buildings[slot] = building
	message = "군수소 건설 · 출전 한도 +6" if id == "logistics" else "%s 건설 · %s 공급" % [facilities[id][1], definitions[role][1]]
	return true

func specialization_unlocked() -> bool:
	if facility_rules != "slots_v1":
		return round_number >= 2 or phase == "REFIT"
	return current_map > 0 or round_number + (1 if phase == "REFIT" else 0) >= int(catalog.facility_progression.specialization_round)

func upgrade(slot: int, id: String) -> bool:
	if omen_pending or phase not in ["PREPARE", "REFIT"] or not specialization_unlocked() or not building_active(slot):
		return false
	if not branches.has(id) or branches[id][1] != buildings[slot].id:
		return false
	if gold < int(facilities[id][2]):
		return false
	gold -= int(facilities[id][2])
	var instance_id: int = int(buildings[slot].get("instance_id", 0))
	buildings[slot] = {"id": id, "unit": branches[id][4], "clock": 0.0}
	if birth_rules in BIRTH_RULES:
		buildings[slot].instance_id = instance_id
	message = "%s 전문화 완료" % facilities[id][1]
	return true

func facility_tier(slot: int) -> int:
	if not building_present(slot) or buildings[slot].id == "logistics":
		return 0
	return int(buildings[slot].get("tier", branches[buildings[slot].id][2]))

func tier_upgrade_cost(slot: int) -> int:
	if not building_present(slot) or not branches.has(buildings[slot].id):
		return 0
	return ceili(float(facilities[buildings[slot].id][2]) * float(catalog.facility_progression.capstone_cost_multiplier))

func can_upgrade_tier(slot: int) -> bool:
	return birth_rules == "birth_v2" and facility_rules == "slots_v1" and not omen_pending and phase in ["PREPARE", "REFIT"] and building_active(slot) and facility_tier(slot) == 2 and (current_map > 0 or round_number + (1 if phase == "REFIT" else 0) >= int(catalog.facility_progression.capstone_round)) and gold >= tier_upgrade_cost(slot)

func upgrade_tier(slot: int) -> bool:
	if not can_upgrade_tier(slot):
		return false
	gold -= tier_upgrade_cost(slot)
	buildings[slot].tier = 3
	buildings[slot].clock = 0.0
	message = "T3 심화 완료 · 이후 생산/징조 토큰 적용 · 기존 병력 유지"
	return true

func is_capstone(unit: Dictionary) -> bool:
	return birth_rules == "birth_v2" and int(unit.get("birth_tier", 1)) == 3

func attack_range(unit: Dictionary) -> float:
	return (float(catalog.capstone_rules.spear_range) if is_capstone(unit) and unit.role == "spear_guard" else float(definitions[unit.role][9])) * 3.0

func capacity_limit() -> int:
	var result := int(catalog.economy.starting_capacity)
	if facility_rules in ["logistics_v1", "slots_v1"]:
		for slot in range(buildings.size()):
			if building_active(slot) and buildings[slot].id == "logistics":
				result += int(catalog.economy.logistics_capacity_bonus)
	return result

func capacity_used() -> int:
	var result := 0
	for unit in units:
		if unit.side == 0:
			result += int(definitions[unit.role][11])
	return result

func heal_cost(unit_id: int) -> int:
	for unit in units:
		if int(unit.id) != unit_id or unit.side != 0 or unit.hp <= 0:
			continue
		var row: Array = definitions[unit.role]
		var missing := maxf(0, float(row[4]) - float(unit.hp))
		return ceili(float(row[12]) * missing / float(row[4]) * float(catalog.economy.heal_coefficient))
	return 0

func heal_unit(unit_id: int) -> bool:
	if phase not in ["PREPARE", "REFIT"]:
		return false
	var cost := heal_cost(unit_id)
	if cost <= 0 or gold < cost:
		return false
	for unit in units:
		if int(unit.id) == unit_id and unit.side == 0 and unit.hp > 0:
			gold -= cost
			unit.hp = float(definitions[unit.role][4])
			message = "%s 치료 완료 · %dG 사용" % [definitions[unit.role][1], cost]
			return true
	return false

func entry_role(entry: Variant) -> String:
	return str(entry.get("role_id", "")) if entry is Dictionary else str(entry)

func reserve_roles() -> Array:
	return reserve.map(func(entry): return entry_role(entry))

func _birth_record(role: String, tier: int = 1, source: int = 0) -> Dictionary:
	var entry := {"entry_id": next_entry_id, "role_id": role, "birth_tier": tier, "source_facility_id": source, "survived": 0}
	next_entry_id += 1
	return entry

func _enqueue(role: String, tier: int = 1, source: int = 0) -> void:
	reserve.append(_birth_record(role, tier, source) if birth_rules in BIRTH_RULES else role)

func deploy(entry: Variant) -> bool:
	var role := entry_role(entry)
	for index in range(reserve.size()):
		if entry_role(reserve[index]) == role:
			return _deploy_index(index)
	return false

func deploy_entry(entry_id: int) -> bool:
	for index in range(reserve.size()):
		if reserve[index] is Dictionary and int(reserve[index].entry_id) == entry_id:
			return _deploy_index(index)
	return false

func _deploy_index(index: int) -> bool:
	if phase not in ["PREPARE", "REFIT", "BATTLE"]:
		return false
	var entry: Variant = reserve[index]
	var role := entry_role(entry)
	if capacity_used() + int(definitions[role][11]) > capacity_limit():
		message = "출전 한도가 부족합니다. 대기 병력은 보존됩니다."
		return false
	reserve.remove_at(index)
	spawn(role, 0, 5.0)
	if birth_rules in BIRTH_RULES and entry is Dictionary:
		for key in ["entry_id", "birth_tier", "source_facility_id", "survived"]:
			units.back()[key] = entry[key]
	message = "%s 출전" % definitions[role][1]
	return true

func queue_used() -> int:
	var used := 0
	for entry in reserve:
		used += int(definitions[entry_role(entry)][11])
	return used

func spin_required_capacity() -> int:
	var maximum := int(definitions.shield_guard[11])
	for i in range(buildings.size()):
		if building_active(i) and buildings[i].unit != "":
			maximum = maxi(maximum, int(definitions[buildings[i].unit][11]))
	return 4 * maximum

func can_spin() -> bool:
	return not omen_pending and phase in ["PREPARE", "REFIT"] and queue_used() + spin_required_capacity() <= int(catalog.economy.queue_capacity) and (free_spin or gold >= int(catalog.economy.paid_spin))

func spin() -> bool:
	if not can_spin():
		return false
	if not free_spin:
		gold -= int(catalog.economy.paid_spin)
	free_spin = false
	omen_pending = true
	omen_moves = 3
	omen_reserved = spin_required_capacity()
	var pool: Array = ["shield_guard", "shield_guard", "", ""]
	for i in range(buildings.size()):
		if building_active(i) and buildings[i].unit != "":
			pool.append({"role_id": buildings[i].unit, "birth_tier": facility_tier(i), "source_facility_id": int(buildings[i].get("instance_id", 0))} if birth_rules in BIRTH_RULES else buildings[i].unit)
	last_board.clear()
	for i in range(9):
		var token: Variant = pool[rng.randi_range(0, pool.size() - 1)]
		last_board.append(token.duplicate(true) if token is Dictionary else token)
	message = "관측 완료 · 행/열 이동 후 결과를 확정하세요."
	return true

func shift_board(axis: String, index: int) -> bool:
	if not omen_pending or omen_moves <= 0 or axis not in ["row", "column"] or index < 0 or index > 2:
		return false
	var ids: Array = [index * 3, index * 3 + 1, index * 3 + 2] if axis == "row" else [index, index + 3, index + 6]
	var last: Variant = last_board[ids[2]]
	last_board[ids[2]] = last_board[ids[1]]
	last_board[ids[1]] = last_board[ids[0]]
	last_board[ids[0]] = last
	omen_moves -= 1
	return true

func bonus_options() -> Array:
	var options: Array = []
	if last_board.size() != 9:
		return options
	for line in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
		var role := entry_role(last_board[line[0]])
		if role != "" and role == entry_role(last_board[line[1]]) and role == entry_role(last_board[line[2]]) and not options.has(role):
			options.append(role)
	return options

func omen_rewards(bonus: String = "") -> Array:
	return omen_reward_tokens(bonus).map(func(token): return entry_role(token))

func _lowest_token(tokens: Array) -> Dictionary:
	var result: Dictionary = {}
	for token in tokens:
		var normalized: Dictionary = token.duplicate(true) if token is Dictionary else {"role_id": token, "birth_tier": 1, "source_facility_id": 0}
		if result.is_empty() or normalized.birth_tier < result.birth_tier:
			result = normalized
	return result

func omen_reward_tokens(bonus: String = "") -> Array:
	var groups: Dictionary = {}
	for token in last_board:
		var role := entry_role(token)
		if role == "":
			continue
		if not groups.has(role):
			groups[role] = []
		groups[role].append(token)
	var rewards: Array = []
	for role in groups:
		for i in range(groups[role].size() / 3):
			rewards.append(_lowest_token(groups[role].slice(i * 3, i * 3 + 3)))
	var options := bonus_options()
	var selected: String = options[0] if options.size() == 1 else bonus
	if options.has(selected):
		var line_tokens: Array = []
		for line in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
			if entry_role(last_board[line[0]]) == selected and entry_role(last_board[line[1]]) == selected and entry_role(last_board[line[2]]) == selected:
				line_tokens.append_array([last_board[line[0]], last_board[line[1]], last_board[line[2]]])
		rewards.append(_lowest_token(line_tokens))
	return rewards

func confirm_omen(bonus: String = "") -> bool:
	if not omen_pending or phase not in ["PREPARE", "REFIT"]:
		return false
	var options := bonus_options()
	if (options.size() > 1 and not options.has(bonus)) or (bonus != "" and not options.has(bonus)):
		return false
	var rewards := omen_reward_tokens(bonus)
	var cost := 0
	for token in rewards:
		cost += int(definitions[token.role_id][11])
	if queue_used() + cost > int(catalog.economy.queue_capacity):
		return false
	for token in rewards:
		_enqueue(token.role_id, int(token.birth_tier), int(token.source_facility_id))
	omen_pending = false
	omen_moves = 0
	omen_reserved = 0
	message = "징조륜 확정 · %d명 대기열 합류" % rewards.size()
	return true

func begin_round() -> bool:
	if omen_pending or phase not in ["PREPARE", "REFIT"]:
		return false
	if phase == "REFIT":
		round_number += 1
	phase = "BATTLE"
	elapsed = 0.0
	wave_index = 0
	message = "공세 시작 · 5 / 22 / 40초에 적이 진입합니다."
	return true

func spawn(role: String, side: int, x: float, front: int = -1) -> void:
	var row: Array = definitions[role]
	units.append({"id": next_id, "role": role, "side": side, "x": x,
		"hp": float(row[4]), "cooldown": 0.0, "flash": 0.0, "action": 0.0,
		"windup": 0.0, "pending_target": -1, "charge": 0.0, "brace": 0.0, "ambush": 0.0, "air_reengage": 0.0,
		"survived": 0, "focus_target": -1, "focus_count": 0,
		"effects": {}, "hit_count": 0, "heal_count": 0})
	if front_count() == 3:
		units.back().front = selected_front if front < 0 else clampi(front, 0, 2)
	if combat_rules == "proc_v1":
		if role == "archer":
			units.back().pierce_count = 0
		if role == "spear_guard":
			units.back().counter_cd = 0.0
	if birth_rules in BIRTH_RULES and side == 0:
		var birth := _birth_record(role)
		for key in ["entry_id", "birth_tier", "source_facility_id"]:
			units.back()[key] = birth[key]
	next_id += 1

func advance(delta: float) -> void:
	if phase != "BATTLE" or not is_finite(delta) or delta < 0.0:
		return
	if ruleset_id == FIXED_RULESET:
		if delta > (100000000.0 - tick_debt) / TICK_RATE:
			return
		tick_debt += delta * TICK_RATE
		var count := mini(MAX_FRAME_TICKS, int(floorf(tick_debt + 0.00000001)))
		tick_debt = maxf(0, tick_debt - count)
		advance_ticks(count)
		if phase != "BATTLE":
			tick_debt = 0.0
		return
	# Historical v1-v6 integration is intentionally retained for loaded runs.
	var remaining: float = minf(delta, 1.0)
	while remaining > 0.00001 and phase == "BATTLE":
		var step: float = minf(remaining, 0.05)
		_tick(step)
		remaining -= step

func simulation_tick() -> int:
	return tick

func advance_ticks(count: int) -> void:
	if ruleset_id != FIXED_RULESET or phase != "BATTLE":
		return
	for index in range(maxi(0, count)):
		if phase != "BATTLE":
			break
		tick += 1
		_tick(1.0 / TICK_RATE)
	if phase != "BATTLE":
		tick_debt = 0.0

func _countdown(seconds: float, dt: float) -> float:
	if ruleset_id == FIXED_RULESET:
		return maxi(0, ceili(seconds * TICK_RATE - 0.00000001) - 1) / float(TICK_RATE)
	return maxf(0, seconds - dt)

func _tick(dt: float) -> void:
	var before := elapsed
	elapsed += dt
	if ruleset_id == FIXED_RULESET:
		elapsed = minf(float(catalog.economy.round_seconds), elapsed)
	while wave_index < 3 and elapsed + 0.0001 >= float(catalog.economy.wave_times[wave_index]):
		if wave_rules == "legacy":
			var groups := wave_composition(round_number, wave_index)
			for role in groups:
				for i in range(int(groups[role])):
					spawn(role, 1, 95.0 + float(i) * 1.2)
		wave_index += 1
	if wave_rules == "staggered_v1":
		for wave in range(wave_index):
			var groups := wave_composition(round_number, wave)
			var order := 0
			for role in groups:
				for i in range(int(groups[role])):
					var arrival := float(catalog.economy.wave_times[wave]) + order * 0.4
					if before + 0.0001 < arrival and elapsed + 0.0001 >= arrival:
						spawn(role, 1, 95.0, (order + wave) % front_count())
					order += 1
	income_clock += dt
	point_clock += dt
	if income_clock >= 20.0:
		gold += 5
		basic_gold_paid += 5
		income_clock -= 20.0
	if point_clock >= 15.0:
		gold += held_points.size() + points.count(1)
		point_clock -= 15.0
	for i in range(buildings.size()):
		if not building_active(i):
			continue
		var building: Dictionary = buildings[i]
		if building.id == "logistics":
			continue
		var interval: float = float(facilities[building.id][5])
		building.clock = minf(float(building.clock) + dt, interval)
		if building.clock + 0.0001 >= interval and queue_used() + int(definitions[building.unit][11]) <= int(catalog.economy.queue_capacity):
			_enqueue(building.unit, facility_tier(i), int(building.get("instance_id", 0)))
			building.clock = 0.0
	var stunned: Array = []
	for actor in units:
		if float(actor.get("effects", {}).get("stun", 0)) > 0:
			stunned.append(actor.id)
		_tick_effects(actor, dt)
	for unit in units:
		if unit.hp <= 0:
			continue
		unit.flash = _countdown(float(unit.flash), dt)
		unit.action = _countdown(float(unit.action), dt)
		unit.cooldown = _countdown(float(unit.cooldown), dt)
		if is_capstone(unit) and unit.role == "flying" and float(unit.get("air_reengage", 0)) > 0:
			var engagement := choose_target(unit)
			var near: bool = not engagement.is_empty() and absf(float(unit.x) - float(engagement.x)) <= attack_range(unit)
			unit.air_reengage = float(catalog.capstone_rules.flying_reengage_seconds) if near else _countdown(float(unit.air_reengage), dt)
		if stunned.has(unit.id) or float(unit.get("effects", {}).get("stun", 0)) > 0:
			unit.brace = 0.0
			continue
		var row: Array = definitions[unit.role]
		if float(unit.get("windup", 0.0)) > 0:
			unit.windup = _countdown(float(unit.windup), dt)
			if unit.windup <= 0.00001:
				unit.windup = 0.0
				unit.action = SHIELD_IMPACT + SHIELD_RECOVERY
				if unit.pending_target == -2:
					if unit.x >= 99:
						bases[1] -= float(row[5])
				else:
					for victim in units:
						if victim.id == unit.pending_target and victim.hp > 0 and same_front(unit, victim) and victim.side != unit.side and absf(float(unit.x) - float(victim.x)) <= attack_range(unit):
							_hit(unit, victim)
							break
				unit.pending_target = -1
			continue
		unit.ambush = _countdown(float(unit.get("ambush", 0.0)), dt)
		var target := choose_target(unit)
		var distance := absf(float(unit.x) - float(target.x)) if not target.is_empty() else INF
		if not target.is_empty() and distance <= attack_range(unit):
			if unit.role == "cavalry" and float(unit.get("charge", 0.0)) < 2.0:
				unit.charge = 0.0
			if unit.role == "spear_guard":
				unit.brace = minf(0.6, float(unit.get("brace", 0.0)) + dt)
			if unit.cooldown <= 0:
				unit.cooldown = float(row[10])
				if unit.side == 0 and unit.role == "shield_guard":
					unit.windup = SHIELD_WINDUP
					unit.pending_target = int(target.id)
					continue
				unit.action = 0.25
				if unit.role == "priest":
					heal_target(unit, target)
				else:
					_hit(unit, target)
		else:
			if (unit.role != "assassin" or target.is_empty()) and _holds_for_capture(unit):
				unit.charge = 0.0
				continue
			var direction: float = 1.0 if unit.side == 0 else -1.0
			if unit.role in ["flying", "assassin"] and not target.is_empty():
				direction = signf(float(target.x) - float(unit.x))
			var previous_x: float = unit.x
			unit.x = clampf(float(unit.x) + direction * float(row[8]) * dt * 2.2 * movement_factor(unit), 0, 100)
			if unit.role == "spear_guard":
				unit.brace = 0.0
			if unit.role == "cavalry":
				unit.charge = minf(2.0, float(unit.get("charge", 0.0)) + absf(float(unit.x) - previous_x))
			if (unit.x >= 99 and unit.side == 0) or (unit.x <= 1 and unit.side == 1):
				if unit.cooldown <= 0 and float(row[5]) > 0:
					if unit.side == 0 and unit.role == "shield_guard":
						unit.cooldown = float(row[10])
						unit.windup = SHIELD_WINDUP
						unit.pending_target = -2
						continue
					var structure_multiplier := (float(catalog.capstone_rules.giant_structure_multiplier) if is_capstone(unit) else 1.5) if unit.role == "giant" else 1.0
					bases[1 - int(unit.side)] -= float(row[5]) * structure_multiplier
					unit.cooldown = float(row[10])
					unit.action = 0.25
	units = units.filter(func(u): return u.hp > 0)
	if ruleset_id == FIXED_RULESET and capture_rules == "timed_v1":
		_tick_tower(dt)
		units = units.filter(func(u): return u.hp > 0)
		_tick_capture()
		_tick_base_claim()
	else:
		for i in range(3):
			var ward := false
			var veil := false
			for unit in units:
				if absf(float(unit.x) - float(25 + 25 * i)) < 5:
					ward = ward or unit.side == 0
					veil = veil or unit.side == 1
			if ward and not veil:
				points[i] = 1
			elif veil and not ward:
				points[i] = -1
		_tick_tower(dt)
	if bases[0] <= 0:
		phase = "DEFEAT"
		message = "수호 성채 함락 · 새 출정으로 다시 도전하세요."
	elif bases[1] <= 0 and (capture_rules == "legacy" or base_claim_work >= _capture_total()):
		phase = "VICTORY"
		message = "베일 본진 점령 · 승리"
		_settle_map(true)
	elif elapsed + 0.0001 >= float(catalog.economy.round_seconds):
		phase = "VICTORY" if round_number >= int(catalog.maps[current_map].rounds) else "REFIT"
		free_spin = true
		message = "전 병력·생산 동결 · 건설/전문화/출전 후 다음 공세" if phase == "REFIT" else "모든 공세 생존 · 승리"
		if phase == "VICTORY":
			_settle_map(false)
	if phase in ["REFIT", "VICTORY"]:
		for unit in units:
			if unit.side == 0 and unit.hp > 0:
				unit.survived = mini(53, int(unit.get("survived", 0)) + 1)

func _tick_tower(dt: float) -> void:
	tower_clock += dt
	if tower_clock >= 2.0:
		tower_clock -= 2.0
		for index in (range(3) if front_count() == 3 else [1]):
			if points[index] == 0:
				continue
			var enemy: int = 1 if points[index] == 1 else 0
			for unit in units:
				if unit.hp > 0 and unit.side == enemy and (front_count() == 1 or unit.get("front", 0) == index) and absf(float(unit.x) - 50) <= 12:
					take_damage(unit, 18, true)
					break

func _capture_total() -> int:
	return ceili(float(catalog.capture_rules.claim_seconds) * TICK_RATE) * 5

func _tick_base_claim() -> void:
	if bases[1] > 0:
		return
	var counts := [0, 0]
	for unit in units:
		if unit.hp > 0 and unit.role != "flying" and float(unit.x) >= 100.0 - float(catalog.capture_rules.radius):
			counts[int(unit.side)] += 1
	if counts[0] > 0 and counts[1] > 0:
		return
	if counts[0] == 0:
		base_claim_work = maxi(0, base_claim_work - roundi(_capture_total() * float(catalog.capture_rules.decay_per_second) / TICK_RATE))
	else:
		base_claim_work = mini(_capture_total(), base_claim_work + mini(int(catalog.capture_rules.max_contributors), counts[0]) * 5)

func _settle_map(captured: bool) -> void:
	if capture_rules != "timed_v1" or settled_maps.has(current_map):
		return
	if captured:
		gold += maxi(0, int(catalog.maps[current_map].rounds) * int(catalog.economy.base_gold_per_round) - basic_gold_paid)
	settled_maps.append(current_map)

func _holds_for_capture(unit: Dictionary) -> bool:
	if ruleset_id != FIXED_RULESET or capture_rules != "timed_v1" or unit.role == "flying":
		return false
	var settings: Dictionary = catalog.capture_rules
	var owner := 1 if unit.side == 0 else -1
	for index in range(3):
		var position: float = point_position(index)
		if points[index] == owner or not point_contains(index, unit):
			continue
		for other in units:
			if other.hp > 0 and other.side != unit.side and same_front(unit, other) and other.role != "flying" and absf(float(other.x) - position) <= float(settings.radius):
				return false
		return true
	return false

func capture_state(index: int) -> Dictionary:
	if index < 0 or index >= 3:
		return {}
	var state: Dictionary = capture[index]
	var total := ceili(float(catalog.capture_rules.claim_seconds) * TICK_RATE) * 5
	return {"owner": points[index], "capturing_side": state.side, "progress": float(state.work) / total,
		"leg": "CLAIM" if points[index] == 0 else "NEUTRALIZE"}

func _tick_capture() -> void:
	var settings: Dictionary = catalog.capture_rules
	var total := ceili(float(settings.claim_seconds) * TICK_RATE) * 5
	var decay := roundi(total * float(settings.decay_per_second) / TICK_RATE)
	for index in range(3):
		var counts := [0, 0]
		for unit in units:
			if unit.hp > 0 and unit.role != "flying" and point_contains(index, unit):
				counts[int(unit.side)] += 1
		if counts[0] > 0 and counts[1] > 0:
			continue
		var side := 1 if counts[0] > 0 else -1 if counts[1] > 0 else 0
		var state: Dictionary = capture[index]
		if side == 0 or side == points[index]:
			state.work = maxi(0, int(state.work) - decay)
			if state.work == 0:
				state.side = 0
			continue
		if state.side != side:
			state.side = side
			state.work = 0
		state.work += mini(int(settings.max_contributors), counts[0] if side == 1 else counts[1]) * 5
		if state.work >= total:
			state.work -= total
			points[index] = side if points[index] == 0 else 0
			if points[index] == side:
				state.work = 0
				state.side = 0

func unit_grade(unit: Dictionary) -> int:
	var survived := int(unit.get("survived", 0))
	return 2 if survived >= 5 else 1 if survived >= 2 else 0

func apply_status(unit: Dictionary, kind: String, amount: float, duration: float) -> bool:
	if unit.hp <= 0 or not is_finite(amount) or not is_finite(duration) or duration <= 0 or duration > 60 or amount < 0:
		return false
	var effects: Dictionary = unit.get("effects", {})
	match kind:
		"stun":
			if float(effects.get("stun", 0)) > 0 or float(effects.get("immune", 0)) > 0:
				return false
			effects.stun = duration * (float(catalog.capstone_rules.shield_stun_multiplier) if is_capstone(unit) and shield_guarding(unit) else 1.0)
			if float(unit.get("charge", 0)) < 2.0:
				unit.charge = 0.0
			unit.windup = 0.0
			unit.pending_target = -1
			unit.action = 0.0
		"barrier":
			if amount <= 0 or amount > 1000:
				return false
			if amount >= float(effects.get("barrier", 0)):
				effects.barrier = amount
				effects.barrier_time = duration
		"slow":
			var slows: Array = effects.get("slows", [])
			var strength := minf(amount, 0.5)
			if strength <= 0:
				return false
			for slow in slows:
				if is_equal_approx(float(slow.amount), strength):
					slow.time = maxf(float(slow.time), duration)
					unit.effects = effects
					return true
			if slows.size() >= 16:
				return false
			slows.append({"amount": strength, "time": duration})
			effects.slows = slows
		_:
			return false
	unit.effects = effects
	return true

func _tick_effects(unit: Dictionary, dt: float) -> void:
	if unit.has("counter_cd"):
		unit.counter_cd = _countdown(float(unit.counter_cd), dt)
	var effects: Dictionary = unit.get("effects", {})
	for key in ["immune", "barrier_time", "damage_guard", "ranged_guard", "armor_break_time"]:
		if effects.has(key):
			effects[key] = _countdown(float(effects[key]), dt)
	if float(effects.get("barrier_time", 0)) <= 0:
		effects.erase("barrier")
	if float(effects.get("armor_break_time", 0)) <= 0:
		effects.erase("armor_break")
	if float(effects.get("stun", 0)) > 0:
		effects.stun = _countdown(float(effects.stun), dt)
		if effects.stun <= 0.00001:
			effects.stun = 0.0
			effects.immune = 1.0
	if effects.has("slows"):
		for slow in effects.slows:
			slow.time = _countdown(float(slow.time), dt)
		effects.slows = effects.slows.filter(func(slow): return slow.time > 0.00001)
	unit.effects = effects

func movement_factor(unit: Dictionary) -> float:
	var strongest := 0.0
	for slow in unit.get("effects", {}).get("slows", []):
		strongest = maxf(strongest, float(slow.amount))
	return maxf(0.5, 1.0 - strongest)

func take_damage(unit: Dictionary, amount: float, ranged: bool = false) -> void:
	if unit.hp <= 0 or not is_finite(amount) or amount <= 0:
		return
	var effects: Dictionary = unit.get("effects", {})
	if float(effects.get("damage_guard", 0)) > 0:
		amount *= float(catalog.capstone_rules.cavalry_damage_multiplier)
	if ranged and float(effects.get("ranged_guard", 0)) > 0:
		amount *= float(catalog.capstone_rules.assassin_ranged_multiplier)
	var absorbed := minf(amount, float(effects.get("barrier", 0)))
	if absorbed > 0:
		effects.barrier -= absorbed
	unit.hp -= amount - absorbed
	unit.flash = 0.2
	unit.effects = effects

func heal_target(healer: Dictionary, target: Dictionary) -> void:
	if healer.hp <= 0 or target.hp <= 0 or healer.side != target.side or healer.id == target.id or not same_front(healer, target):
		return
	var healing := float(catalog.capstone_rules.priest_heal) if is_capstone(healer) else 12.0
	var healed := minf(healing, maxf(0, float(definitions[target.role][4]) - float(target.hp)))
	target.hp += healed
	target.flash = 0.2
	healer.heal_count = (int(healer.get("heal_count", 0)) + 1) % 3
	if unit_grade(healer) >= 1 and healer.heal_count == 0:
		var effects: Dictionary = target.get("effects", {})
		var slows: Array = effects.get("slows", [])
		if not slows.is_empty():
			var strongest := 0
			for i in range(1, slows.size()):
				if float(slows[i].amount) > float(slows[strongest].amount):
					strongest = i
			slows.remove_at(strongest)
		target.effects = effects
	if unit_grade(healer) >= 2 and healed < healing:
		apply_status(target, "barrier", minf(12, healing - healed), 3)

func shield_guarding(unit: Dictionary) -> bool:
	if phase != "BATTLE" or unit.role != "shield_guard" or unit.hp <= 0:
		return false
	for other in units:
		if other.hp > 0 and same_front(unit, other) and other.side != unit.side and absf(float(other.x) - float(unit.x)) <= float(definitions.shield_guard[9]) * 3.0:
			return true
	return false

func choose_target(unit: Dictionary) -> Dictionary:
	var target: Dictionary = {}
	var best_priority := 2
	var best_distance := INF
	for other in units:
		if other.hp <= 0 or other.id == unit.id or not same_front(unit, other):
			continue
		if unit.role == "priest":
			if other.side != unit.side or other.hp >= float(definitions[other.role][4]):
				continue
		elif other.side == unit.side:
			continue
		var distance := absf(float(unit.x) - float(other.x))
		var priority := 1
		if unit.role == "archer" and other.role == "flying" and distance <= float(definitions.archer[9]) * 3.0:
			priority = 0
		elif other.role in ["archer", "mage", "priest"] and (unit.role == "flying" or (unit.role == "assassin" and distance <= 12.0)):
			priority = 0
		if priority < best_priority or (priority == best_priority and distance < best_distance):
			best_priority = priority
			best_distance = distance
			target = other
	return target

func _hit(attacker: Dictionary, target: Dictionary) -> void:
	if combat_rules == "proc_v1":
		resolve_hit({"event_id": event_serial + 1, "attack_id": event_serial + 1, "parent_event_id": 0,
			"kind": "BASIC", "source_id": attacker.id, "target_id": target.id, "side_at_launch": attacker.side})
	else:
		_basic_hit(attacker, target)

func resolve_hit(event: Dictionary) -> bool:
	if combat_rules != "proc_v1" or not _valid_integer(event.get("event_id"), 1, 100000000) or event.event_id != event_serial + 1:
		return false
	var kind: String = str(event.get("kind", ""))
	if kind not in ["BASIC", "SECONDARY", "COUNTER"]:
		return false
	var basic := kind == "BASIC"
	if basic:
		if _active_attack != 0 or event.get("parent_event_id") != 0 or event.get("attack_id") != event.event_id:
			return false
	elif _active_attack == 0 or event.get("parent_event_id") != _active_attack or event.get("attack_id") != _active_attack or not _finite_number(event.get("base_damage")) or event.base_damage <= 0:
		return false
	var attacker: Dictionary = {}
	var target: Dictionary = {}
	for unit in units:
		if unit.id == event.get("source_id"):
			attacker = unit
		if unit.id == event.get("target_id"):
			target = unit
	if attacker.is_empty() or target.is_empty() or attacker.hp <= 0 or target.hp <= 0 or attacker.side == target.side or attacker.side != event.get("side_at_launch") or not same_front(attacker, target):
		return false
	if float(attacker.get("effects", {}).get("stun", 0)) > 0:
		return false
	if basic and absf(float(attacker.x) - float(target.x)) > attack_range(attacker):
		return false
	event_serial = int(event.event_id)
	if basic:
		_active_attack = event_serial
		_basic_hit(attacker, target)
		_active_attack = 0
	else:
		var armor := float(definitions[target.role][6])
		if float(target.get("effects", {}).get("armor_break_time", 0)) > 0:
			armor = maxf(0, armor - float(target.effects.armor_break))
		var damage := maxf(1, float(event.base_damage) * 100.0 / (100.0 + armor))
		var ranged := kind == "SECONDARY"
		var forward := (float(attacker.x) - float(target.x)) * (1.0 if target.side == 0 else -1.0)
		if ranged and forward > 0 and shield_guarding(target):
			damage = maxf(1, damage * 0.75)
		take_damage(target, damage, ranged)
		if kind == "COUNTER":
			attacker.action = 0.25
		damage_events += 1
	return true

func _secondary_hit(attacker: Dictionary, target: Dictionary, kind: String, base_damage: float) -> bool:
	return resolve_hit({"event_id": event_serial + 1, "attack_id": _active_attack, "parent_event_id": _active_attack,
		"kind": kind, "source_id": attacker.id, "target_id": target.id, "side_at_launch": attacker.side, "base_damage": base_damage})

func _pierce_target(attacker: Dictionary, primary: Dictionary) -> Dictionary:
	var candidates: Array = []
	var direction := 1.0 if attacker.side == 0 else -1.0
	for other in units:
		var distance := (float(other.x) - float(primary.x)) * direction
		if other.hp > 0 and other.side != attacker.side and other.id != primary.id and same_front(attacker, other) and distance > 0 and distance <= float(catalog.grade_proc_rules.archer_behind_range) * 3.0:
			candidates.append(other)
	candidates.sort_custom(func(a: Dictionary, b: Dictionary) -> bool:
		var a_distance := absf(float(a.x) - float(primary.x))
		var b_distance := absf(float(b.x) - float(primary.x))
		return int(a.id) < int(b.id) if a_distance == b_distance else a_distance < b_distance)
	return candidates[0] if not candidates.is_empty() else {}

func _basic_hit(attacker: Dictionary, target: Dictionary) -> void:
	if attacker.hp <= 0 or target.hp <= 0 or not same_front(attacker, target):
		return
	attacker.hit_count = (int(attacker.get("hit_count", 0)) + 1) % 4
	var row: Array = definitions[attacker.role]
	var focused := false
	if attacker.role == "archer":
		attacker.focus_count = (int(attacker.get("focus_count", 0)) + 1) % 3 if int(attacker.get("focus_target", -1)) == int(target.id) else 1
		attacker.focus_target = int(target.id)
		focused = unit_grade(attacker) >= 1 and attacker.focus_count == 0
		if combat_rules == "proc_v1":
			attacker.pierce_count = (int(attacker.get("pierce_count", 0)) + 1) % int(catalog.grade_proc_rules.archer_every)
	var ambush: bool = attacker.role == "assassin" and target.role in ["archer", "mage", "priest"] and float(attacker.get("ambush", 0.0)) <= 0
	if ambush:
		attacker.ambush = 10.0
	var charged: bool = attacker.role == "cavalry" and float(attacker.get("charge", 0.0)) >= 2.0
	var opening: bool = is_capstone(attacker) and attacker.role == "flying" and float(attacker.get("air_reengage", 0)) <= 0
	if opening:
		attacker.air_reengage = float(catalog.capstone_rules.flying_reengage_seconds)
	if is_capstone(attacker):
		var effects: Dictionary = attacker.get("effects", {})
		if charged:
			effects.damage_guard = float(catalog.capstone_rules.cavalry_guard_seconds)
		if ambush:
			effects.ranged_guard = float(catalog.capstone_rules.assassin_guard_seconds)
		attacker.effects = effects
	if attacker.role == "cavalry":
		attacker.charge = 0.0
	var targets: Array = [target]
	if attacker.role in ["mage", "greatsword_warrior"]:
		var limit: int = 4 if attacker.role == "mage" else 3
		if is_capstone(attacker) and attacker.role == "mage":
			limit = int(catalog.capstone_rules.mage_target_limit)
		var candidates: Array = []
		for other in units:
			if other.hp <= 0 or not same_front(attacker, other) or other.side == attacker.side or other.id == target.id or absf(float(other.x) - float(target.x)) > 1.8:
				continue
			if attacker.role == "greatsword_warrior" and (float(other.x) - float(attacker.x)) * (1.0 if attacker.side == 0 else -1.0) < 0:
				continue
			candidates.append(other)
		# Never reorder live simulation units. Explicit ID tie-break makes the
		# capped selection independent of the engine's unstable sorting algorithm.
		candidates.sort_custom(func(a: Dictionary, b: Dictionary) -> bool:
			var distance_a := absf(float(a.x) - float(target.x))
			var distance_b := absf(float(b.x) - float(target.x))
			return a.id < b.id if distance_a == distance_b else distance_a < distance_b)
		for other in candidates.slice(0, limit - 1):
			targets.append(other)
	for victim in targets:
		var armor: float = float(definitions[victim.role][7 if attacker.role == "mage" else 6])
		if attacker.role != "mage" and float(victim.get("effects", {}).get("armor_break_time", 0)) > 0:
			armor = maxf(0, armor - float(victim.effects.get("armor_break", 0)))
		var damage := maxf(1, float(row[5]) * 100.0 / (100.0 + armor))
		if focused:
			damage *= float(catalog.capstone_rules.archer_focus_multiplier) if is_capstone(attacker) else 1.25
		if opening:
			damage *= float(catalog.capstone_rules.flying_opening_multiplier)
		if attacker.role == "greatsword_warrior" and victim.id == target.id and unit_grade(attacker) >= 1:
			damage *= 1.2
		if ambush:
			damage *= 1.4
		if charged:
			damage *= 1.5
			if victim.role == "spear_guard" and float(victim.get("brace", 0.0)) >= 0.6:
				damage = maxf(1, damage * 0.5)
		var forward := (float(attacker.x) - float(victim.x)) * (1.0 if victim.side == 0 else -1.0)
		if attacker.role == "archer" and forward > 0 and shield_guarding(victim):
			damage = maxf(1, damage * 0.75)
		take_damage(victim, damage, attacker.role in ["archer", "mage"])
		if combat_rules == "proc_v1" and charged and victim.role == "spear_guard" and float(victim.get("brace", 0)) >= 0.6 and victim.hp > 0 and float(victim.get("effects", {}).get("stun", 0)) <= 0:
			if unit_grade(victim) >= 1:
				apply_status(attacker, "slow", float(catalog.grade_proc_rules.spear_slow), float(catalog.grade_proc_rules.spear_slow_seconds))
			if unit_grade(victim) >= 2 and float(victim.get("counter_cd", 0)) <= 0:
				if _secondary_hit(victim, attacker, "COUNTER", float(definitions.spear_guard[5])):
					victim.counter_cd = float(catalog.grade_proc_rules.spear_counter_seconds)
		if is_capstone(attacker) and attacker.role == "greatsword_warrior" and attacker.hit_count == 0 and victim.id == target.id:
			var effects: Dictionary = victim.get("effects", {})
			effects.armor_break = float(catalog.capstone_rules.blade_armor_reduction)
			effects.armor_break_time = float(catalog.capstone_rules.blade_armor_seconds)
			victim.effects = effects
		if unit_grade(attacker) >= 1:
			if attacker.role == "mage":
				apply_status(victim, "slow", 0.15, 1)
			elif attacker.role == "shield_guard" and attacker.hit_count == 0:
				apply_status(victim, "stun", 0, 0.3)
			elif charged:
				apply_status(victim, "stun", 0, 0.4)
		damage_events += 1
	if combat_rules == "proc_v1" and attacker.role == "archer" and unit_grade(attacker) >= 2 and attacker.pierce_count == 0:
		var behind := _pierce_target(attacker, target)
		if not behind.is_empty():
			var raw := float(row[5]) * float(catalog.grade_proc_rules.archer_multiplier)
			if focused:
				raw *= float(catalog.capstone_rules.archer_focus_multiplier) if is_capstone(attacker) else 1.25
			_secondary_hit(attacker, behind, "SECONDARY", raw)

func snapshot(include_entry: bool = true) -> Dictionary:
	var result := {"version": 6, "map_entry": map_entry.duplicate(true) if include_entry else {}, "current_map": current_map, "held_points": held_points.duplicate(), "map_pressure": map_pressure, "wave_rules": wave_rules, "omen_pending": omen_pending, "omen_moves": omen_moves, "omen_reserved": omen_reserved, "gold": gold, "phase": phase, "round": round_number,
		"elapsed": elapsed, "wave": wave_index, "units": units.duplicate(true),
		"buildings": buildings.duplicate(true), "reserve": reserve.duplicate(true),
		"points": points.duplicate(), "bases": bases.duplicate(), "next_id": next_id,
		"damage_events": damage_events, "rng": str(rng.state), "free_spin": free_spin,
		"board": last_board.duplicate(true), "income": income_clock, "point_clock": point_clock,
		"tower_clock": tower_clock, "message": message}
	if ruleset_id == FIXED_RULESET:
		result.merge({"version": 7, "ruleset_id": ruleset_id, "tick": tick, "tick_debt": tick_debt, "timer_units": "ticks"}, true)
		if combat_rules == "proc_v1":
			result.merge({"combat_rules": combat_rules, "event_serial": event_serial})
		if front_count() == 3:
			result.merge({"front_rules": front_rules, "selected_front": selected_front})
		result.merge({"capture_rules": capture_rules, "capture": capture.duplicate(true)}, true)
		result.facility_rules = facility_rules
		result.birth_rules = birth_rules
		if birth_rules in BIRTH_RULES:
			result.next_facility_id = next_facility_id
			result.next_entry_id = next_entry_id
		if capture_rules == "timed_v1":
			result.merge({"base_claim_work": base_claim_work, "basic_gold_paid": basic_gold_paid, "settled_maps": settled_maps.duplicate()}, true)
		_convert_duration_units(result, true)
	return result

# Model-facing seconds are retained for presentation. Disk durations are integer ticks.
# This mutates only a snapshot/deep copy, never the live model or caller's save object.
func _convert_duration_units(state: Dictionary, encode: bool) -> bool:
	if not state.get("units") is Array:
		return false
	for unit in state.units:
		if not unit is Dictionary:
			return false
		var groups: Array = [{"value": unit, "keys": ["cooldown", "flash", "action", "windup", "brace", "ambush", "air_reengage", "counter_cd"]}]
		var effects: Variant = unit.get("effects", {})
		if not effects is Dictionary or not effects.get("slows", []) is Array:
			return false
		groups.append({"value": effects, "keys": ["barrier_time", "stun", "immune", "damage_guard", "ranged_guard", "armor_break_time"]})
		for slow in effects.get("slows", []):
			if not slow is Dictionary:
				return false
			groups.append({"value": slow, "keys": ["time"]})
		for group in groups:
			for key in group.keys:
				if not group.value.has(key):
					continue
				var number: Variant = group.value[key]
				if not _finite_number(number) or number < 0 or (not encode and (number != floorf(number) or number > 1800)):
					return false
				group.value[key] = maxi(0, ceili(number * TICK_RATE - 0.00000001)) if encode else float(number) / TICK_RATE
	return true

func restore(value: Variant) -> bool:
	if not value is Dictionary or not _finite_number(value.get("version")) or value.version != floorf(value.version) or value.version < 1 or value.version > 7 or value.has("schema_version"):
		return false
	value = value.duplicate(true)
	var saved_combat: String = str(value.get("combat_rules", "legacy"))
	if saved_combat not in ["legacy", "proc_v1"]:
		return false
	if saved_combat == "proc_v1":
		if value.version != 7 or not _valid_integer(value.get("event_serial"), 0, 100000000):
			return false
	elif value.has("event_serial"):
		return false
	var saved_fronts: String = str(value.get("front_rules", "single_v1"))
	if saved_fronts not in ["single_v1", "three_v1"]:
		return false
	if saved_fronts == "three_v1":
		if value.version != 7 or value.get("capture_rules") != "timed_v1" or value.get("wave_rules") != "staggered_v1" or not _valid_integer(value.get("selected_front"), 0, 2):
			return false
	elif value.has("selected_front"):
		return false
	if value.version == 7 and value.get("birth_rules", "legacy") not in ["legacy", "birth_v1", "birth_v2"]:
		return false
	var has_birth: bool = value.version == 7 and value.get("birth_rules") in BIRTH_RULES
	if value.version == 7 and not has_birth:
		if value.has("next_entry_id") or value.has("next_facility_id"):
			return false
	if has_birth:
		for key in ["next_entry_id", "next_facility_id"]:
			if not _valid_integer(value.get(key), 1, 100000000):
				return false
	if value.version == 7:
		if value.get("ruleset_id") != FIXED_RULESET or value.get("timer_units") != "ticks":
			return false
		for field in ["tick", "tick_debt"]:
			if not _finite_number(value.get(field)) or value[field] < 0 or value[field] > 100000000:
				return false
		if value.tick != floorf(value.tick):
			return false
		if not _convert_duration_units(value, false):
			return false
		if value.get("facility_rules", "legacy") not in ["legacy", "logistics_v1", "slots_v1"]:
			return false
		value.facility_rules = value.get("facility_rules", "legacy")
		if value.get("capture_rules", "legacy") not in ["legacy", "timed_v1"]:
			return false
		if (value.get("capture_rules") == "timed_v1" and not value.has("capture")) or (not value.has("capture_rules") and value.has("capture")):
			return false
		if value.get("capture_rules") == "timed_v1":
			for field in ["base_claim_work", "basic_gold_paid"]:
				if not _finite_number(value.get(field)) or value[field] != floorf(value[field]) or value[field] < 0:
					return false
			if value.base_claim_work > _capture_total() or value.basic_gold_paid > 1000 or not _finite_number(value.get("current_map")) or not value.get("settled_maps") is Array or value.settled_maps.size() > 5:
				return false
			var previous := -1
			for map_index in value.settled_maps:
				if not _finite_number(map_index) or map_index != floorf(map_index) or map_index <= previous or map_index > value.get("current_map", -1):
					return false
				previous = int(map_index)
		var saved_capture: Variant = value.get("capture", [{"side": 0, "work": 0}, {"side": 0, "work": 0}, {"side": 0, "work": 0}])
		if not saved_capture is Array or saved_capture.size() != 3:
			return false
		for state in saved_capture:
			if not state is Dictionary or not _finite_number(state.get("side")) or state.side != floorf(state.side) or absf(state.side) > 1 or not _finite_number(state.get("work")) or state.work != floorf(state.work) or state.work < 0 or state.work >= ceili(float(catalog.capture_rules.claim_seconds) * TICK_RATE) * 5 or (state.side == 0 and state.work != 0):
				return false
		value.capture_rules = value.get("capture_rules", "legacy")
		value.capture = saved_capture
	if value.version < 6:
		value.map_entry = {}
	if value.version < 5:
		value.current_map = 0
		value.held_points = []
	if value.version < 4:
		value.map_pressure = 1.0
	if value.version < 3:
		value.wave_rules = "legacy"
	if value.version == 1:
		value.omen_pending = false
		value.omen_moves = 0
		value.omen_reserved = 0
	for key in snapshot():
		if key in ["birth_rules", "next_entry_id", "next_facility_id", "front_rules", "selected_front", "combat_rules", "event_serial"]:
			continue
		if key in ["ruleset_id", "tick", "tick_debt", "timer_units", "capture_rules", "capture", "base_claim_work", "basic_gold_paid", "settled_maps", "facility_rules"] and (value.version < 7 or (key in ["base_claim_work", "basic_gold_paid", "settled_maps"] and value.get("capture_rules") == "legacy")):
			continue
		if not value.has(key):
			return false
	if value.wave_rules not in ["legacy", "staggered_v1"]:
		return false
	if not _finite_number(value.current_map) or value.current_map != floorf(value.current_map) or value.current_map < 0 or value.current_map >= catalog.maps.size() or not value.held_points is Array:
		return false
	var valid_points: Array = []
	for map_index in range(int(value.current_map)):
		for point in range(3):
			valid_points.append("%s:%d" % [catalog.maps[map_index].id, point])
	var seen_points: Array = []
	for point in value.held_points:
		if point not in valid_points or point in seen_points:
			return false
		seen_points.append(point)
	if not _finite_number(value.map_pressure) or value.map_pressure <= 0 or value.map_pressure > 2:
		return false
	if value.phase not in ["PREPARE", "BATTLE", "REFIT", "VICTORY", "DEFEAT"]:
		return false
	if not value.units is Array or not value.buildings is Array or not value.reserve is Array:
		return false
	if value.version == 7 and not has_birth:
		for unit in value.units:
			if unit is Dictionary and (unit.has("entry_id") or unit.has("birth_tier") or unit.has("source_facility_id")):
				return false
		for building in value.buildings:
			if building is Dictionary and building.has("instance_id"):
				return false
	for key in ["points", "bases", "board"]:
		if not value[key] is Array:
			return false
	for key in ["gold", "round", "elapsed", "wave", "next_id", "damage_events", "income", "point_clock", "tower_clock"]:
		if not _finite_number(value[key]) or float(value[key]) < 0:
			return false
	if value.elapsed > 60.001 or value.wave > 3 or value.gold > 1000000 or not value.free_spin is bool or not value.rng is String or not value.rng.is_valid_int() or not value.message is String:
		return false
	for owner in value.points:
		if not _finite_number(owner) or float(owner) < -1 or float(owner) > 1 or float(owner) != floorf(float(owner)):
			return false
	for hp in value.bases:
		if not _finite_number(hp) or hp > 1000:
			return false
	if value.board.size() not in [0, 9]:
		return false
	for token in value.board:
		if token is Dictionary and (not has_birth or not _valid_token(token, value)):
			return false
		var role := entry_role(token)
		if role != "" and not definitions.has(role):
			return false
	if value.buildings.size() > 6 + (int(value.current_map) + 1) * 3 or value.units.size() > 500 or value.reserve.size() > 24:
		return false
	if value.points.size() != 3 or value.bases.size() != 2 or int(value.round) < 1 or int(value.round) > int(catalog.maps[int(value.current_map)].rounds):
		return false
	if value.version == 7 and value.capture_rules == "timed_v1":
		if (value.bases[1] > 0 and value.base_claim_work != 0) or int(value.basic_gold_paid) % 5 != 0 or value.basic_gold_paid > int(value.round) * int(catalog.economy.base_gold_per_round):
			return false
		var expected_count := int(value.current_map) + (1 if value.phase == "VICTORY" else 0)
		if value.settled_maps.size() != expected_count:
			return false
		for index in range(expected_count):
			if value.settled_maps[index] != index:
				return false
	var seen_ids: Array = []
	var seen_birth_ids: Array = []
	for unit in value.units:
		if not unit is Dictionary or not definitions.has(unit.get("role", "")):
			return false
		if saved_fronts == "three_v1":
			if not _valid_integer(unit.get("front"), 0, 2):
				return false
		elif unit.has("front"):
			return false
		for key in ["id", "side", "x", "hp", "cooldown", "flash", "action"]:
			if not unit.has(key) or not _finite_number(unit[key]):
				return false
		if (unit.side != 0 and unit.side != 1) or unit.x < 0 or unit.x > 110 or unit.id < 0 or unit.id >= value.next_id or seen_ids.has(unit.id):
			return false
		seen_ids.append(unit.id)
		if has_birth and (unit.has("entry_id") or unit.has("birth_tier") or unit.has("source_facility_id")):
			if not _valid_birth(unit, value) or unit.entry_id in seen_birth_ids:
				return false
			seen_birth_ids.append(unit.entry_id)
		var windup: Variant = unit.get("windup", 0.0)
		if saved_combat == "proc_v1":
			if unit.role == "archer" and not _valid_integer(unit.get("pierce_count"), 0, int(catalog.grade_proc_rules.archer_every) - 1):
				return false
			if unit.role == "spear_guard" and (not _finite_number(unit.get("counter_cd")) or unit.counter_cd < 0 or unit.counter_cd > float(catalog.grade_proc_rules.spear_counter_seconds)):
				return false
		if unit.has("pierce_count") and (saved_combat != "proc_v1" or unit.role != "archer"):
			return false
		if unit.has("counter_cd") and (saved_combat != "proc_v1" or unit.role != "spear_guard"):
			return false
		if not _valid_effects(unit.get("effects", {})):
			return false
		var effects: Dictionary = unit.get("effects", {})
		for key in ["damage_guard", "ranged_guard", "armor_break", "armor_break_time"]:
			if effects.has(key) and (value.version != 7 or value.get("birth_rules") != "birth_v2"):
				return false
		for pair in [["damage_guard", "cavalry"], ["ranged_guard", "assassin"]]:
			if float(effects.get(pair[0], 0)) > 0 and (unit.role != pair[1] or unit.get("birth_tier", 1) != 3):
				return false
		if not _finite_number(unit.get("air_reengage", 0)) or unit.get("air_reengage", 0) < 0 or unit.get("air_reengage", 0) > 8:
			return false
		if unit.get("air_reengage", 0) > 0 and (unit.role != "flying" or unit.get("birth_tier", 1) != 3 or value.get("birth_rules") != "birth_v2"):
			return false
		for counter in ["hit_count", "heal_count"]:
			var count: Variant = unit.get(counter, 0)
			if not _finite_number(count) or count != floorf(count) or count < 0 or count > (3 if counter == "hit_count" else 2):
				return false
		for counter in ["survived", "focus_count", "focus_target"]:
			var number: Variant = unit.get(counter, -1 if counter == "focus_target" else 0)
			var limit: int = int(value.next_id) - 1 if counter == "focus_target" else 2 if counter == "focus_count" else 53
			if not _finite_number(number) or number != floorf(number) or number < (-1 if counter == "focus_target" else 0) or number > limit:
				return false
		for ability in ["charge", "brace", "ambush"]:
			var amount: Variant = unit.get(ability, 0.0)
			if not _finite_number(amount) or amount < 0 or amount > (10.0 if ability == "ambush" else 2.0 if ability == "charge" else 0.6):
				return false
		var pending: Variant = unit.get("pending_target", -1)
		if float(unit.get("effects", {}).get("stun", 0)) > 0 and (windup != 0 or pending != -1):
			return false
		if not _finite_number(windup) or windup < 0 or windup > (0.2 if value.version == 7 else SHIELD_WINDUP) or not _finite_number(pending) or pending != floorf(float(pending)) or pending < -2 or pending >= value.next_id:
			return false
		if windup > 0 and (unit.side != 0 or unit.role != "shield_guard" or pending == -1):
			return false
	var seen_facilities: Array = []
	for building in value.buildings:
		if building is Dictionary and building.has("tier"):
			if not has_birth or value.get("birth_rules") != "birth_v2" or not branches.has(building.get("id", "")) or int(branches[building.id][2]) != 2 or building.tier != 3:
				return false
		if has_birth and building is Dictionary and building.get("id") != "":
			if not _valid_integer(building.get("instance_id"), 1, int(value.next_facility_id) - 1) or building.instance_id in seen_facilities:
				return false
			seen_facilities.append(building.instance_id)
		if building is Dictionary and building.get("id") == "":
			if value.version != 7 or value.facility_rules != "slots_v1" or building.size() != 3 or building.get("unit") != "" or not _finite_number(building.get("clock")) or building.clock != 0:
				return false
			continue
		if building is Dictionary and building.get("id") == "logistics":
			if value.version != 7 or value.facility_rules not in ["logistics_v1", "slots_v1"] or building.get("unit") != "" or not _finite_number(building.get("clock")) or building.clock != 0:
				return false
			continue
		if not building is Dictionary or not facilities.has(building.get("id", "")) or not definitions.has(building.get("unit", "")) or not building.has("clock"):
			return false
		if not branches.has(building.id) or not _finite_number(building.clock) or building.clock < 0:
			return false
		if building.id == "special_barracks":
			if building.unit not in catalog.unit_families.special:
				return false
		elif building.unit != branches[building.id][4]:
			return false
	for entry in value.reserve:
		if entry is Dictionary:
			if not has_birth or not _valid_birth(entry, value) or entry.entry_id in seen_birth_ids or entry.get("survived") != 0:
				return false
			seen_birth_ids.append(entry.entry_id)
		if not definitions.has(entry_role(entry)):
			return false
	var queue_cost := 0
	for entry in value.reserve:
		queue_cost += int(definitions[entry_role(entry)][11])
	if not value.omen_pending is bool or not _finite_number(value.omen_moves) or value.omen_moves != floorf(value.omen_moves) or value.omen_moves < 0 or value.omen_moves > 3 or not _finite_number(value.omen_reserved):
		return false
	if value.omen_pending:
		var max_cost := int(definitions.shield_guard[11])
		var allowed_roles: Array = ["", "shield_guard"]
		for i in range(value.buildings.size()):
			if i < 6 + value.held_points.size() + value.points.count(1) and value.buildings[i].unit != "":
				max_cost = maxi(max_cost, int(definitions[value.buildings[i].unit][11]))
				allowed_roles.append(value.buildings[i].unit)
		for token in value.board:
			if not allowed_roles.has(entry_role(token)):
				return false
			if token is Dictionary:
				var found := false
				for i in range(value.buildings.size()):
					var building: Dictionary = value.buildings[i]
					if i < 6 + value.held_points.size() + value.points.count(1) and building.unit == token.role_id and building.get("instance_id", 0) == token.source_facility_id and int(building.get("tier", branches[building.id][2])) == token.birth_tier:
						found = true
				if not found:
					return false
		if value.phase not in ["PREPARE", "REFIT"] or value.board.size() != 9 or value.free_spin or value.omen_reserved != max_cost * 4:
			return false
	elif value.omen_moves != 0 or value.omen_reserved != 0:
		return false
	if queue_cost + int(value.omen_reserved) > int(catalog.economy.queue_capacity):
		return false
	if not value.map_entry is Dictionary:
		return false
	if not value.map_entry.is_empty():
		var entry: Dictionary = value.map_entry
		if not entry.get("map_entry") is Dictionary or not entry.map_entry.is_empty() or entry.get("current_map") != value.current_map or entry.get("held_points") != value.held_points or entry.get("phase") != "PREPARE" or entry.get("round") != 1 or entry.get("elapsed") != 0:
			return false
		var probe = get_script().new()
		for key in ["wave", "omen_moves", "omen_reserved", "income", "point_clock", "tower_clock"]:
			if entry.get(key) != 0:
				return false
		if entry.get("omen_pending") != false or entry.get("free_spin") != true:
			return false
		if not probe.restore(entry):
			return false
		if probe.front_rules != saved_fronts:
			return false
		if probe.combat_rules != saved_combat or probe.event_serial > int(value.get("event_serial", 0)):
			return false
		if value.version == 7:
			if probe.birth_rules != value.get("birth_rules", "legacy"):
				return false
			if has_birth and (probe.next_facility_id > value.next_facility_id or probe.next_entry_id > value.next_entry_id):
				return false
			if probe.facility_rules != value.facility_rules:
				return false
			if probe.capture_rules != value.capture_rules or probe.base_claim_work != 0 or probe.basic_gold_paid != 0:
				return false
			for state in probe.capture:
				if state.side != 0 or state.work != 0:
					return false
		if value.version == 7 and (entry.get("version") != 7 or entry.get("ruleset_id") != value.ruleset_id or entry.get("tick", 0) > value.tick or entry.get("tick_debt") != 0):
			return false
		for owner in probe.points:
			if owner != 0:
				return false
		for hp in probe.bases:
			if hp != 1000:
				return false
	ruleset_id = FIXED_RULESET if value.version == 7 else "legacy"
	front_rules = saved_fronts
	combat_rules = saved_combat
	event_serial = int(value.get("event_serial", 0))
	_active_attack = 0
	selected_front = int(value.get("selected_front", 0))
	birth_rules = value.birth_rules if has_birth else "legacy"
	next_facility_id = int(value.get("next_facility_id", 1)) if has_birth else 1
	next_entry_id = int(value.get("next_entry_id", 1)) if has_birth else 1
	facility_rules = value.get("facility_rules", "legacy") if value.version == 7 else "legacy"
	capture_rules = value.get("capture_rules", "legacy") if value.version == 7 else "legacy"
	base_claim_work = int(value.get("base_claim_work", 0)) if capture_rules == "timed_v1" else 0
	basic_gold_paid = int(value.get("basic_gold_paid", 0)) if capture_rules == "timed_v1" else 0
	settled_maps = value.get("settled_maps", []).map(func(index): return int(index)) if capture_rules == "timed_v1" else []
	capture = value.get("capture", [{"side": 0, "work": 0}, {"side": 0, "work": 0}, {"side": 0, "work": 0}]).duplicate(true) if value.version == 7 else [{"side": 0, "work": 0}, {"side": 0, "work": 0}, {"side": 0, "work": 0}]
	tick = int(value.get("tick", 0)) if value.version == 7 else 0
	tick_debt = float(value.get("tick_debt", 0)) if value.version == 7 else 0.0
	omen_pending = value.omen_pending
	map_entry = value.map_entry.duplicate(true)
	current_map = int(value.current_map)
	held_points = value.held_points.duplicate()
	wave_rules = value.wave_rules
	map_pressure = float(value.map_pressure)
	omen_moves = int(value.omen_moves)
	omen_reserved = int(value.omen_reserved)
	gold = int(value.gold)
	phase = value.phase
	round_number = int(value.round)
	elapsed = float(value.elapsed)
	wave_index = int(value.wave)
	units = value.units.duplicate(true)
	for unit in units:
		unit.effects = unit.get("effects", {})
		if unit.has("pierce_count"):
			unit.pierce_count = int(unit.pierce_count)
		if unit.has("counter_cd"):
			unit.counter_cd = float(unit.counter_cd)
		for key in ["entry_id", "birth_tier", "source_facility_id"]:
			if unit.has(key):
				if has_birth:
					unit[key] = int(unit[key])
				else:
					unit.erase(key)
		unit.hit_count = int(unit.get("hit_count", 0))
		unit.heal_count = int(unit.get("heal_count", 0))
		unit.survived = int(unit.get("survived", 0))
		unit.focus_count = int(unit.get("focus_count", 0))
		unit.focus_target = int(unit.get("focus_target", -1))
		unit.ambush = float(unit.get("ambush", 0.0))
		unit.air_reengage = float(unit.get("air_reengage", 0.0))
		unit.charge = float(unit.get("charge", 0.0))
		unit.brace = float(unit.get("brace", 0.0))
		unit.windup = float(unit.get("windup", 0.0))
		unit.pending_target = int(unit.get("pending_target", -1))
	buildings = value.buildings.duplicate(true)
	for building in buildings:
		if building.has("tier"):
			building.tier = int(building.tier)
		if building.has("instance_id"):
			if has_birth:
				building.instance_id = int(building.instance_id)
			else:
				building.erase("instance_id")
	reserve = value.reserve.duplicate(true)
	for entry in reserve:
		if entry is Dictionary:
			for key in ["entry_id", "birth_tier", "source_facility_id", "survived"]:
				entry[key] = int(entry[key])
	points = value.points.map(func(owner): return int(owner))
	bases = value.bases.duplicate()
	next_id = int(value.next_id)
	damage_events = int(value.damage_events)
	rng.state = int(value.rng)
	free_spin = value.free_spin
	last_board = value.board.duplicate(true)
	for token in last_board:
		if token is Dictionary:
			token.birth_tier = int(token.birth_tier)
			token.source_facility_id = int(token.source_facility_id)
	income_clock = float(value.income)
	point_clock = float(value.point_clock)
	tower_clock = float(value.tower_clock)
	message = value.message
	return true

func _valid_integer(value: Variant, minimum: int, maximum: int) -> bool:
	return _finite_number(value) and value == floorf(value) and value >= minimum and value <= maximum

func _valid_birth(entry: Dictionary, state: Dictionary) -> bool:
	return _valid_integer(entry.get("entry_id"), 1, int(state.next_entry_id) - 1) and _valid_integer(entry.get("birth_tier"), 1, 3 if state.birth_rules == "birth_v2" else 2) and _valid_integer(entry.get("source_facility_id"), 0, int(state.next_facility_id) - 1) and (entry.source_facility_id != 0 or entry.birth_tier == 1)

func _valid_token(token: Dictionary, state: Dictionary) -> bool:
	return token.size() == 3 and definitions.has(token.get("role_id", "")) and _valid_integer(token.get("birth_tier"), 1, 3 if state.birth_rules == "birth_v2" else 2) and _valid_integer(token.get("source_facility_id"), 0, int(state.next_facility_id) - 1) and (token.source_facility_id != 0 or token.birth_tier == 1)

func _finite_number(value: Variant) -> bool:
	return (value is int or value is float) and is_finite(float(value))

func _valid_effects(value: Variant) -> bool:
	if not value is Dictionary:
		return false
	var limits := {"damage_guard": float(catalog.capstone_rules.cavalry_guard_seconds), "ranged_guard": float(catalog.capstone_rules.assassin_guard_seconds), "armor_break": float(catalog.capstone_rules.blade_armor_reduction), "armor_break_time": float(catalog.capstone_rules.blade_armor_seconds)}
	for key in limits:
		if value.has(key) and (not _finite_number(value[key]) or value[key] < 0 or value[key] > limits[key]):
			return false
	if float(value.get("armor_break", 0)) > 0 and float(value.get("armor_break_time", 0)) <= 0:
		return false
	for key in value:
		if key not in ["barrier", "barrier_time", "stun", "immune", "slows", "damage_guard", "ranged_guard", "armor_break", "armor_break_time"]:
			return false
		if key == "slows":
			if not value.slows is Array or value.slows.size() > 16:
				return false
			for slow in value.slows:
				if not slow is Dictionary or slow.size() != 2 or not _finite_number(slow.get("amount")) or not _finite_number(slow.get("time")):
					return false
				if slow.amount <= 0 or slow.amount > 0.5 or slow.time <= 0 or slow.time > 60:
					return false
		elif not _finite_number(value[key]) or value[key] < 0 or value[key] > (1000 if key == "barrier" else 1 if key == "immune" else 60):
			return false
	return float(value.get("barrier", 0)) <= 0 or float(value.get("barrier_time", 0)) > 0
