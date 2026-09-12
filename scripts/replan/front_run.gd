extends RefCounted
## Replan preview model. The blueprint owns base numbers; this model owns simulation.

const CATALOG_PATH := "res://docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json"
const SHIELD_WINDUP := 0.18
const SHIELD_IMPACT := 0.10
const SHIELD_RECOVERY := 0.15
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

func _init() -> void:
	catalog = JSON.parse_string(FileAccess.get_file_as_string(CATALOG_PATH))
	for row in catalog.units:
		definitions[row[0]] = row
	for row in catalog.buildings:
		facilities[row[0]] = row
	for row in catalog.building_tree:
		branches[row[0]] = row
	gold = int(catalog.economy.starting_gold)
	rng.seed = 1947
	for i in range(4):
		spawn("shield_guard", 0, 8.0 + i * 1.4)

func unlocked_slots() -> int:
	return 6 + points.count(1)

func building_active(slot: int) -> bool:
	return slot >= 0 and slot < buildings.size() and slot < unlocked_slots()

func wave_composition(round_id: int, wave_id: int) -> Dictionary:
	var cycle_index := round_id - 1 + (wave_id if wave_rules == "staggered_v1" else 0)
	var template: String = catalog.wave_cycle[cycle_index % catalog.wave_cycle.size()]
	var scale := float(catalog.maps[0].pressure) * (1.0 + 0.03 * (round_id - 1)) if wave_rules == "staggered_v1" else 1.0
	var composition: Dictionary = {}
	for group in catalog.wave_templates[template]:
		composition[group[0]] = composition.get(group[0], 0) + ceili(float(group[1]) * scale)
	return composition

func wave_forecast() -> Dictionary:
	if phase in ["VICTORY", "DEFEAT"]:
		return {}
	var next_round := round_number + (1 if phase == "REFIT" else 0)
	var next_wave := wave_index if phase == "BATTLE" else 0
	if next_round > int(catalog.maps[0].rounds) or next_wave >= catalog.economy.wave_times.size():
		return {}
	var composition := wave_composition(next_round, next_wave)
	return {"round": next_round, "wave": next_wave + 1,
		"seconds": maxf(0, float(catalog.economy.wave_times[next_wave]) - (elapsed if phase == "BATTLE" else 0.0)),
		"units": composition}

func production_status(slot: int) -> Dictionary:
	if slot < 0 or slot >= buildings.size():
		return {"state": "EMPTY", "remaining": 0.0, "progress": 0.0}
	var building: Dictionary = buildings[slot]
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
	if omen_pending or phase not in ["PREPARE", "REFIT"] or id not in ["barracks", "special_barracks"]:
		return false
	if buildings.size() >= unlocked_slots() or gold < int(facilities[id][2]):
		return false
	var role: String = branches[id][4]
	if role == "random_special":
		role = catalog.unit_families.special[rng.randi_range(0, 4)]
	gold -= int(facilities[id][2])
	buildings.append({"id": id, "unit": role, "clock": 0.0})
	message = "%s 건설 · %s 공급" % [facilities[id][1], definitions[role][1]]
	return true

func upgrade(slot: int, id: String) -> bool:
	if omen_pending or phase not in ["PREPARE", "REFIT"] or (round_number < 2 and phase != "REFIT") or not building_active(slot):
		return false
	if not branches.has(id) or branches[id][1] != buildings[slot].id:
		return false
	if gold < int(facilities[id][2]):
		return false
	gold -= int(facilities[id][2])
	buildings[slot] = {"id": id, "unit": branches[id][4], "clock": 0.0}
	message = "%s 전문화 완료" % facilities[id][1]
	return true

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

func deploy(role: String) -> bool:
	if phase not in ["PREPARE", "REFIT", "BATTLE"] or not reserve.has(role):
		return false
	if capacity_used() + int(definitions[role][11]) > int(catalog.economy.starting_capacity):
		message = "출전 한도가 부족합니다. 대기 병력은 보존됩니다."
		return false
	reserve.erase(role)
	spawn(role, 0, 5.0)
	message = "%s 출전" % definitions[role][1]
	return true

func queue_used() -> int:
	var used := 0
	for role in reserve:
		used += int(definitions[role][11])
	return used

func spin_required_capacity() -> int:
	var maximum := int(definitions.shield_guard[11])
	for i in range(buildings.size()):
		if building_active(i):
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
		if building_active(i):
			pool.append(buildings[i].unit)
	last_board.clear()
	for i in range(9):
		var role: String = pool[rng.randi_range(0, pool.size() - 1)]
		last_board.append(role)
	message = "관측 완료 · 행/열 이동 후 결과를 확정하세요."
	return true

func shift_board(axis: String, index: int) -> bool:
	if not omen_pending or omen_moves <= 0 or axis not in ["row", "column"] or index < 0 or index > 2:
		return false
	var ids: Array = [index * 3, index * 3 + 1, index * 3 + 2] if axis == "row" else [index, index + 3, index + 6]
	var last: String = last_board[ids[2]]
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
		var role: String = last_board[line[0]]
		if role != "" and role == last_board[line[1]] and role == last_board[line[2]] and not options.has(role):
			options.append(role)
	return options

func omen_rewards(bonus: String = "") -> Array:
	var counts: Dictionary = {}
	for role in last_board:
		if role != "":
			counts[role] = counts.get(role, 0) + 1
	var rewards: Array = []
	for role in counts:
		for i in range(int(counts[role]) / 3):
			rewards.append(role)
	var options := bonus_options()
	if options.size() == 1:
		rewards.append(options[0])
	elif options.has(bonus):
		rewards.append(bonus)
	return rewards

func confirm_omen(bonus: String = "") -> bool:
	if not omen_pending or phase not in ["PREPARE", "REFIT"]:
		return false
	var options := bonus_options()
	if (options.size() > 1 and not options.has(bonus)) or (bonus != "" and not options.has(bonus)):
		return false
	var rewards := omen_rewards(bonus)
	var cost := 0
	for role in rewards:
		cost += int(definitions[role][11])
	if queue_used() + cost > int(catalog.economy.queue_capacity):
		return false
	reserve.append_array(rewards)
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

func spawn(role: String, side: int, x: float) -> void:
	var row: Array = definitions[role]
	units.append({"id": next_id, "role": role, "side": side, "x": x,
		"hp": float(row[4]), "cooldown": 0.0, "flash": 0.0, "action": 0.0,
		"windup": 0.0, "pending_target": -1})
	next_id += 1

func advance(delta: float) -> void:
	if phase != "BATTLE" or delta <= 0.0:
		return
	# Fixed substeps keep movement/attack ordering stable under UI speed changes.
	var remaining: float = minf(delta, 1.0)
	while remaining > 0.00001 and phase == "BATTLE":
		var step: float = minf(remaining, 0.05)
		_tick(step)
		remaining -= step

func _tick(dt: float) -> void:
	var before := elapsed
	elapsed += dt
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
						spawn(role, 1, 95.0)
					order += 1
	income_clock += dt
	point_clock += dt
	if income_clock >= 20.0:
		gold += 5
		income_clock -= 20.0
	if point_clock >= 15.0:
		gold += points.count(1)
		point_clock -= 15.0
	for i in range(buildings.size()):
		if not building_active(i):
			continue
		var building: Dictionary = buildings[i]
		var interval: float = float(facilities[building.id][5])
		building.clock = minf(float(building.clock) + dt, interval)
		if building.clock + 0.0001 >= interval and queue_used() + int(definitions[building.unit][11]) <= int(catalog.economy.queue_capacity):
			reserve.append(building.unit)
			building.clock = 0.0
	for unit in units:
		if unit.hp <= 0:
			continue
		unit.flash = maxf(0, float(unit.flash) - dt)
		unit.action = maxf(0, float(unit.action) - dt)
		unit.cooldown = maxf(0, float(unit.cooldown) - dt)
		var row: Array = definitions[unit.role]
		if float(unit.get("windup", 0.0)) > 0:
			unit.windup = maxf(0, float(unit.windup) - dt)
			if unit.windup <= 0.00001:
				unit.windup = 0.0
				unit.action = SHIELD_IMPACT + SHIELD_RECOVERY
				if unit.pending_target == -2:
					if unit.x >= 99:
						bases[1] -= float(row[5])
				else:
					for victim in units:
						if victim.id == unit.pending_target and victim.hp > 0 and victim.side != unit.side and absf(float(unit.x) - float(victim.x)) <= float(row[9]) * 3.0:
							_hit(unit, victim)
							break
				unit.pending_target = -1
			continue
		var target: Dictionary = {}
		var distance := INF
		for other in units:
			if other.hp <= 0 or other.id == unit.id:
				continue
			var friendly: bool = other.side == unit.side
			if unit.role == "priest":
				if not friendly or other.hp >= float(definitions[other.role][4]):
					continue
			elif friendly:
				continue
			var d: float = absf(float(unit.x) - float(other.x))
			if d < distance:
				distance = d
				target = other
		if not target.is_empty() and distance <= float(row[9]) * 3.0:
			if unit.cooldown <= 0:
				unit.cooldown = float(row[10])
				if unit.side == 0 and unit.role == "shield_guard":
					unit.windup = SHIELD_WINDUP
					unit.pending_target = int(target.id)
					continue
				unit.action = 0.25
				if unit.role == "priest":
					target.hp = minf(float(target.hp) + 12, float(definitions[target.role][4]))
					target.flash = 0.2
				else:
					_hit(unit, target)
		else:
			var direction: float = 1.0 if unit.side == 0 else -1.0
			unit.x = clampf(float(unit.x) + direction * float(row[8]) * dt * 2.2, 0, 100)
			if (unit.x >= 99 and unit.side == 0) or (unit.x <= 1 and unit.side == 1):
				if unit.cooldown <= 0 and float(row[5]) > 0:
					if unit.side == 0 and unit.role == "shield_guard":
						unit.cooldown = float(row[10])
						unit.windup = SHIELD_WINDUP
						unit.pending_target = -2
						continue
					bases[1 - int(unit.side)] -= float(row[5]) * (1.5 if unit.role == "giant" else 1.0)
					unit.cooldown = float(row[10])
					unit.action = 0.25
	units = units.filter(func(u): return u.hp > 0)
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
	tower_clock += dt
	if tower_clock >= 2.0:
		tower_clock -= 2.0
		if points[1] != 0:
			var enemy: int = 1 if points[1] == 1 else 0
			for unit in units:
				if unit.side == enemy and absf(float(unit.x) - 50) <= 12:
					unit.hp -= 18
					unit.flash = 0.2
					break
	if bases[0] <= 0:
		phase = "DEFEAT"
		message = "수호 성채 함락 · 새 출정으로 다시 도전하세요."
	elif bases[1] <= 0:
		phase = "VICTORY"
		message = "베일 본진 점령 · 승리"
	elif elapsed + 0.0001 >= float(catalog.economy.round_seconds):
		phase = "VICTORY" if round_number >= int(catalog.maps[0].rounds) else "REFIT"
		free_spin = true
		message = "전 병력·생산 동결 · 건설/전문화/출전 후 다음 공세" if phase == "REFIT" else "모든 공세 생존 · 승리"

func _hit(attacker: Dictionary, target: Dictionary) -> void:
	var row: Array = definitions[attacker.role]
	var targets: Array = [target]
	if attacker.role in ["mage", "greatsword_warrior"]:
		var limit: int = 4 if attacker.role == "mage" else 3
		for other in units:
			if targets.size() >= limit:
				break
			if other.hp > 0 and other.side != attacker.side and other.id != target.id and absf(float(other.x) - float(target.x)) <= 1.8:
				targets.append(other)
	for victim in targets:
		var armor: float = float(definitions[victim.role][7 if attacker.role == "mage" else 6])
		victim.hp -= maxf(1, float(row[5]) * 100.0 / (100.0 + armor))
		victim.flash = 0.2
		damage_events += 1

func snapshot() -> Dictionary:
	return {"version": 3, "wave_rules": wave_rules, "omen_pending": omen_pending, "omen_moves": omen_moves, "omen_reserved": omen_reserved, "gold": gold, "phase": phase, "round": round_number,
		"elapsed": elapsed, "wave": wave_index, "units": units.duplicate(true),
		"buildings": buildings.duplicate(true), "reserve": reserve.duplicate(),
		"points": points.duplicate(), "bases": bases.duplicate(), "next_id": next_id,
		"damage_events": damage_events, "rng": str(rng.state), "free_spin": free_spin,
		"board": last_board.duplicate(), "income": income_clock, "point_clock": point_clock,
		"tower_clock": tower_clock, "message": message}

func restore(value: Variant) -> bool:
	if not value is Dictionary or (value.get("version") != 1 and value.get("version") != 2 and value.get("version") != 3):
		return false
	value = value.duplicate(true)
	if value.version < 3:
		value.wave_rules = "legacy"
	if value.version == 1:
		value.omen_pending = false
		value.omen_moves = 0
		value.omen_reserved = 0
	for key in snapshot():
		if not value.has(key):
			return false
	if value.wave_rules not in ["legacy", "staggered_v1"]:
		return false
	if value.phase not in ["PREPARE", "BATTLE", "REFIT", "VICTORY", "DEFEAT"]:
		return false
	if not value.units is Array or not value.buildings is Array or not value.reserve is Array:
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
	for role in value.board:
		if role != "" and not definitions.has(role):
			return false
	if value.buildings.size() > 9 or value.units.size() > 500 or value.reserve.size() > 24:
		return false
	if value.points.size() != 3 or value.bases.size() != 2 or int(value.round) < 1 or int(value.round) > 10:
		return false
	var seen_ids: Array = []
	for unit in value.units:
		if not unit is Dictionary or not definitions.has(unit.get("role", "")):
			return false
		for key in ["id", "side", "x", "hp", "cooldown", "flash", "action"]:
			if not unit.has(key) or not _finite_number(unit[key]):
				return false
		if (unit.side != 0 and unit.side != 1) or unit.x < 0 or unit.x > 110 or unit.id < 0 or unit.id >= value.next_id or seen_ids.has(unit.id):
			return false
		seen_ids.append(unit.id)
		var windup: Variant = unit.get("windup", 0.0)
		var pending: Variant = unit.get("pending_target", -1)
		if not _finite_number(windup) or windup < 0 or windup > SHIELD_WINDUP or not _finite_number(pending) or pending != floorf(float(pending)) or pending < -2 or pending >= value.next_id:
			return false
		if windup > 0 and (unit.side != 0 or unit.role != "shield_guard" or pending == -1):
			return false
	for building in value.buildings:
		if not building is Dictionary or not facilities.has(building.get("id", "")) or not definitions.has(building.get("unit", "")) or not building.has("clock"):
			return false
		if not branches.has(building.id) or not _finite_number(building.clock) or building.clock < 0:
			return false
		if building.id == "special_barracks":
			if building.unit not in catalog.unit_families.special:
				return false
		elif building.unit != branches[building.id][4]:
			return false
	for role in value.reserve:
		if not definitions.has(role):
			return false
	var queue_cost := 0
	for role in value.reserve:
		queue_cost += int(definitions[role][11])
	if not value.omen_pending is bool or not _finite_number(value.omen_moves) or value.omen_moves != floorf(value.omen_moves) or value.omen_moves < 0 or value.omen_moves > 3 or not _finite_number(value.omen_reserved):
		return false
	if value.omen_pending:
		var max_cost := int(definitions.shield_guard[11])
		var allowed_roles: Array = ["", "shield_guard"]
		for i in range(value.buildings.size()):
			if i < 6 + value.points.count(1):
				max_cost = maxi(max_cost, int(definitions[value.buildings[i].unit][11]))
				allowed_roles.append(value.buildings[i].unit)
		for role in value.board:
			if not allowed_roles.has(role):
				return false
		if value.phase not in ["PREPARE", "REFIT"] or value.board.size() != 9 or value.free_spin or value.omen_reserved != max_cost * 4:
			return false
	elif value.omen_moves != 0 or value.omen_reserved != 0:
		return false
	if queue_cost + int(value.omen_reserved) > int(catalog.economy.queue_capacity):
		return false
	omen_pending = value.omen_pending
	wave_rules = value.wave_rules
	omen_moves = int(value.omen_moves)
	omen_reserved = int(value.omen_reserved)
	gold = int(value.gold)
	phase = value.phase
	round_number = int(value.round)
	elapsed = float(value.elapsed)
	wave_index = int(value.wave)
	units = value.units.duplicate(true)
	for unit in units:
		unit.windup = float(unit.get("windup", 0.0))
		unit.pending_target = int(unit.get("pending_target", -1))
	buildings = value.buildings.duplicate(true)
	reserve = value.reserve.duplicate()
	points = value.points.map(func(owner): return int(owner))
	bases = value.bases.duplicate()
	next_id = int(value.next_id)
	damage_events = int(value.damage_events)
	rng.state = int(value.rng)
	free_spin = value.free_spin
	last_board = value.board.duplicate()
	income_clock = float(value.income)
	point_clock = float(value.point_clock)
	tower_clock = float(value.tower_clock)
	message = value.message
	return true

func _finite_number(value: Variant) -> bool:
	return (value is int or value is float) and is_finite(float(value))
