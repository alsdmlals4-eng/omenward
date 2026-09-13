extends SceneTree

var checks := 0
var failures := 0

func check(ok: bool, message: String) -> void:
	checks += 1
	if not ok:
		failures += 1
		push_error(message)

func verify_campaign(model: Script) -> void:
	var campaign = model.new()
	if campaign.has_method("unit_grade"):
		for completed in range(5):
			campaign.phase = "BATTLE"
			campaign.elapsed = 59.95
			campaign.wave_index = 3
			campaign.advance(0.1)
			check(campaign.units[0].survived == completed + 1, "Living soldier gains exactly one completed round")
			campaign.advance(1.0)
			check(campaign.units[0].survived == completed + 1, "Refit cannot farm survival grade")
		check(campaign.unit_grade(campaign.units[0]) == 2, "Five survived rounds reach elite")
		var veteran = model.new()
		veteran.units.clear()
		veteran.spawn("archer", 0, 50)
		veteran.spawn("giant", 1, 55)
		veteran.units[0].survived = 2
		check(veteran.unit_grade(veteran.units[0]) == 1, "Two survived rounds reach veteran")
		for hit in range(3):
			var hp: float = veteran.units[1].hp
			veteran._hit(veteran.units[0], veteran.units[1])
			check(is_equal_approx(hp - veteran.units[1].hp, 18.0 / 1.3 * (1.25 if hit == 2 else 1.0)), "Veteran archer third consecutive shot bonus only")
			if hit == 1:
				var two_shots = model.new()
				check(two_shots.restore(JSON.parse_string(JSON.stringify(veteran.snapshot()))) and two_shots.units[0].focus_count == 2 and two_shots.units[0].focus_target == veteran.units[1].id, "Second-shot save preserves pending third-shot bonus")
				veteran = two_shots
		var loaded_veteran = model.new()
		check(loaded_veteran.restore(JSON.parse_string(JSON.stringify(veteran.snapshot()))) and loaded_veteran.units[0].survived == 2, "Survival and attack streak survive disk")
		veteran.units[0].role = "greatsword_warrior"
		veteran.spawn("giant", 1, 56)
		veteran.units[1].hp = 320.0
		veteran._hit(veteran.units[0], veteran.units[1])
		check(is_equal_approx(320 - veteran.units[1].hp, 20.0 / 1.3 * 1.2) and is_equal_approx(320 - veteran.units[2].hp, 20.0 / 1.3), "Veteran greatsword boosts only primary target")
		campaign = model.new()
	else:
		check(false, "Missing survival grade progression")
	var roles = model.new()
	if roles.has_method("choose_target"):
		roles.units.clear()
		roles.spawn("archer", 0, 50)
		roles.spawn("shield_guard", 1, 52)
		roles.spawn("flying", 1, 58)
		check(roles.choose_target(roles.units[0]).id == roles.units[2].id, "Archer prioritizes in-range flying target")
		roles.units[2].x = 95.0
		check(roles.choose_target(roles.units[0]).id == roles.units[1].id, "Distant flyer does not suppress valid archer shot")
		roles.units[0].role = "assassin"
		roles.spawn("mage", 1, 56)
		check(roles.choose_target(roles.units[0]).role == "mage", "Assassin seeks backline over nearer frontliner")
		roles.units[3].x = 80.0
		check(roles.choose_target(roles.units[0]).role == "shield_guard", "Assassin does not skip frontline for backline beyond four scaled distance")
		roles.units[3].x = 56.0
		var hp: float = roles.units[3].hp
		roles._hit(roles.units[0], roles.units[3])
		check(is_equal_approx(hp - roles.units[3].hp, 26.0 / 1.05 * 1.4), "Assassin first backline hit burst")
		hp = roles.units[3].hp
		roles._hit(roles.units[0], roles.units[3])
		check(is_equal_approx(hp - roles.units[3].hp, 26.0 / 1.05), "Assassin repeat during cooldown is ordinary damage")
		var restored_role = model.new()
		check(restored_role.restore(JSON.parse_string(JSON.stringify(roles.snapshot()))) and restored_role.units[0].ambush == 10.0, "Ambush cooldown survives disk save")
		roles.units[0].role = "flying"
		roles.units[3].hp = 100.0
		check(roles.choose_target(roles.units[0]).role == "mage", "Flyer seeks living ground backline")
		roles.units[3].hp = 0.0
		check(roles.choose_target(roles.units[0]).role == "shield_guard", "Dead backline does not attract flyer")
		for side in range(2):
			var movement = model.new()
			movement.units.clear()
			movement.spawn("assassin", side, 50)
			movement.spawn("mage", 1 - side, 40 if side == 0 else 60)
			movement.units[0].ambush = 1.0
			movement.phase = "REFIT"
			movement.advance(0.5)
			check(movement.units[0].ambush == 1.0, "Ambush timer freezes outside battle")
			movement.begin_round()
			movement.advance(0.5)
			check(movement.units[0].x < 50 if side == 0 else movement.units[0].x > 50, "Both factions move toward backline behind their facing")
			check(is_equal_approx(movement.units[0].ambush, 0.5), "Ambush timer ticks only in battle")
	else:
		check(false, "Missing role target selection")
	if campaign.has_method("retry_map"):
		var entry = campaign.snapshot()
		check(not campaign.retry_map(), "Retry unavailable before defeat")
		campaign.construct("barracks")
		campaign.phase = "DEFEAT"
		var disk = model.new()
		check(disk.restore(JSON.parse_string(JSON.stringify(campaign.snapshot()))) and disk.retry_map() and equivalent_state(disk.snapshot(), entry), "Disk retry rolls back preparation purchases to exact map entry")
		var invalid_entry = disk.snapshot()
		invalid_entry.map_entry.map_entry = {"nested": true}
		var stable_entry = disk.snapshot()
		check(not disk.restore(invalid_entry) and disk.snapshot() == stable_entry, "Nested retry snapshot rejected without mutation")
		invalid_entry = disk.snapshot()
		invalid_entry.map_entry.wave = 1
		check(not disk.restore(invalid_entry) and disk.snapshot() == stable_entry, "Checkpoint must be pristine before first wave")
		disk.phase = "DEFEAT"
		check(disk.retry_map() and equivalent_state(disk.snapshot(), entry), "Repeat retry restores identical entry without accumulating rewards")
	else:
		check(false, "Missing map-entry retry transaction")
	if not campaign.has_method("next_map"):
		check(false, "Missing sequential campaign transition")
		return
	var before = campaign.snapshot()
	check(not campaign.next_map() and campaign.snapshot() == before, "Cannot skip an uncleared map")
	campaign.construct("barracks")
	campaign.units[0].hp = 77.0
	campaign.reserve.append("archer")
	for stage in range(4):
		campaign.points = [1, 0, -1]
		campaign.phase = "VICTORY"
		var funds = campaign.gold
		check(campaign.next_map(), "Victory opens next map")
		check(campaign.current_map == stage + 1 and campaign.round_number == 1 and campaign.phase == "PREPARE", "Next map begins in preparation")
		check(campaign.gold == funds and campaign.units[0].hp == 77.0 and campaign.reserve == ["archer"] and campaign.buildings.size() == 1, "Campaign preserves economy wounded survivors and supply")
		check(campaign.unlocked_slots() == 7 + stage and campaign.points == [0, 0, 0], "Only actually held old points unlock persistent slots")
		var loaded = model.new()
		check(loaded.restore(JSON.parse_string(JSON.stringify(campaign.snapshot()))) and equivalent_state(loaded.snapshot(), campaign.snapshot()), "Campaign disk continuation")
	campaign.phase = "VICTORY"
	before = campaign.snapshot()
	check(not campaign.next_map() and campaign.snapshot() == before, "Final map never creates sixth map")
	for point_list in [["ward_citadel:0", "ward_citadel:0"], ["veil_citadel:0"], ["unknown:0"]]:
		var corrupt = campaign.snapshot()
		corrupt.held_points = point_list
		check(not campaign.restore(corrupt) and campaign.snapshot() == before, "Invalid campaign points rejected atomically")
	var old_save = model.new().snapshot()
	old_save.version = 4
	old_save.erase("current_map")
	old_save.erase("held_points")
	check(campaign.restore(old_save) and campaign.current_map == 0 and campaign.held_points.is_empty(), "V4 save migrates to first map without invented captures")
	for map_index in range(5):
		var ending = model.new()
		ending.current_map = map_index
		ending.map_entry = ending.snapshot(false)
		ending.phase = "BATTLE"
		ending.round_number = int(ending.catalog.maps[map_index].rounds)
		ending.elapsed = 59.95
		ending.wave_index = 3
		ending.units.clear()
		ending.advance(0.1)
		check(ending.phase == "VICTORY", "Each map uses its own survival round total")
		var roundtrip = model.new()
		check(roundtrip.restore(JSON.parse_string(JSON.stringify(ending.snapshot()))), "Late map round count survives disk validation")
	for invalid_map in [-1, 0.5, 5, NAN]:
		var corrupt = campaign.snapshot()
		corrupt.current_map = invalid_map
		var stable = campaign.snapshot()
		check(not campaign.restore(corrupt) and campaign.snapshot() == stable, "Invalid map index rejected atomically")

func equivalent_state(left: Variant, right: Variant) -> bool:
	if left is Dictionary and right is Dictionary:
		if left.size() != right.size():
			return false
		for key in left:
			if not right.has(key) or not equivalent_state(left[key], right[key]):
				return false
		return true
	if left is Array and right is Array:
		if left.size() != right.size():
			return false
		for i in range(left.size()):
			if not equivalent_state(left[i], right[i]):
				return false
		return true
	if (left is int or left is float) and (right is int or right is float):
		return absf(float(left) - float(right)) <= 0.000000001
	return left == right

func _initialize() -> void:
	if not ResourceLoader.exists("res://scripts/replan/front_run.gd"):
		check(false, "Missing approved single-front construction/combat model")
		quit(1)
		return
	var model = load("res://scripts/replan/front_run.gd")
	verify_campaign(model)
	var r = model.new()
	check(r.wave_composition(1, 0) == {"shield_guard":2, "archer":1}, "New first-map playtest pressure starts with two shields and one archer")
	var charge = model.new()
	charge.units.clear()
	charge.spawn("cavalry", 0, 50)
	charge.spawn("spear_guard", 1, 52)
	charge.units[0].charge = 2.0
	charge.units[1].brace = 0.6
	charge._hit(charge.units[0], charge.units[1])
	check(is_equal_approx(charge.units[1].hp, 145 - 19.0 / 1.16 * 1.5 * 0.5), "Braced spear halves cavalry charge")
	check(charge.units[0].charge == 0.0, "Charge consumed on first hit")
	charge.units[1].hp = 145.0
	charge._hit(charge.units[0], charge.units[1])
	check(is_equal_approx(charge.units[1].hp, 145 - 19.0 / 1.16), "Following uncharged hit not reduced by brace")
	charge.units[1].hp = 145.0
	charge.units[1].brace = 0.0
	charge.units[0].charge = 2.0
	charge._hit(charge.units[0], charge.units[1])
	check(is_equal_approx(charge.units[1].hp, 145 - 19.0 / 1.16 * 1.5), "Unprepared spear receives full charge")
	var motion = model.new()
	motion.units.clear()
	motion.spawn("cavalry", 0, 10)
	motion.spawn("spear_guard", 1, 50)
	motion.begin_round()
	motion.advance(0.6)
	check(motion.units[0].charge == 2.0 and motion.units[1].brace == 0.0, "Real movement prepares charge but not spear brace")
	motion.units[0].x = 48.0
	motion.units[0].cooldown = 10.0
	motion.advance(0.7)
	check(motion.units[1].brace == 0.6, "Spear holding melee contact becomes braced")
	var saved_roles = motion.snapshot()
	var resumed_roles = model.new()
	check(resumed_roles.restore(JSON.parse_string(JSON.stringify(saved_roles))) and resumed_roles.units[0].charge == 2.0 and resumed_roles.units[1].brace == 0.6, "Role preparation persists through disk save")
	saved_roles.units[0].charge = NAN
	var before_roles = resumed_roles.snapshot()
	check(not resumed_roles.restore(saved_roles) and resumed_roles.snapshot() == before_roles, "Invalid role timer rejected before mutation")
	motion.units[0].charge = 1.0
	motion.advance(0.1)
	check(motion.units[0].charge == 0.0, "Interrupted partial cavalry advance resets before movement resumes")
	var guarding = model.new()
	guarding.units.clear()
	guarding.phase = "BATTLE"
	guarding.spawn("shield_guard", 0, 50)
	guarding.spawn("shield_guard", 1, 52)
	guarding.spawn("archer", 1, 60)
	guarding._hit(guarding.units[2], guarding.units[0])
	check(is_equal_approx(guarding.units[0].hp, 180.0 - 18.0 / 1.24 * 0.75), "Engaged shield reduces frontal arrow damage25 percent")
	guarding.units[0].hp = 180.0
	guarding.units[2].x = 40.0
	guarding._hit(guarding.units[2], guarding.units[0])
	check(is_equal_approx(guarding.units[0].hp, 180.0 - 18.0 / 1.24), "Rear arrows bypass shield stance")
	guarding.units[0].hp = 180.0
	guarding.units[2].x = 60.0
	guarding.units[1].x = 70.0
	guarding._hit(guarding.units[2], guarding.units[0])
	check(is_equal_approx(guarding.units[0].hp, 180.0 - 18.0 / 1.24), "Advancing shield gets no stationary defense")
	guarding.units[1].x = 52.0
	guarding.spawn("mage", 1, 58.0)
	guarding.units[0].hp = 180.0
	guarding._hit(guarding.units[3], guarding.units[0])
	check(is_equal_approx(guarding.units[0].hp, 180.0 - 22.0 / 1.16), "Magic bypasses frontal arrow defense")
	guarding.units[0].hp = 180.0
	guarding._hit(guarding.units[1], guarding.units[0])
	check(is_equal_approx(guarding.units[0].hp, 180.0 - 12.0 / 1.24), "Melee bypasses arrow defense")
	guarding.spawn("archer", 0, 42.0)
	guarding._hit(guarding.units[4], guarding.units[1])
	check(is_equal_approx(guarding.units[1].hp, 180.0 - 18.0 / 1.24 * 0.75), "Veil shield uses mirrored forward defense")
	guarding.units[0].hp = 0
	guarding.units[4].x = 40
	check(not guarding.shield_guarding(guarding.units[1]), "Dead nearby enemy cannot activate guard")
	if not r.has_method("wave_composition"):
		check(false, "Missing blueprint wave composition and staggered arrivals")
		quit(1)
		return
	var waves = model.new()
	waves.map_pressure = 1.0 # Explicit formula fixture, separate from tuned new-run default.
	check(waves.wave_composition(1, 2) == {"shield_guard":5, "greatsword_warrior":2}, "Third first-round wave uses cycle B")
	check(waves.wave_composition(2, 0) == {"shield_guard":4, "archer":3}, "Round scale applies ceiling to each group")
	waves.begin_round()
	for i in range(50):
		waves.advance(0.1)
	check(waves.next_id == 5, "At five seconds only first enemy has arrived")
	var midwave = model.new()
	check(midwave.restore(JSON.parse_string(JSON.stringify(waves.snapshot()))), "Midwave disk save loads")
	for i in range(17):
		waves.advance(0.1)
		midwave.advance(0.1)
	check(waves.next_id == 9 and midwave.next_id == 9, "Five sequential arrivals without duplicate after restore")
	check(equivalent_state(waves.snapshot(), midwave.snapshot()), "Midwave full-state continuation within 1e-9 JSON floating-point tolerance")
	var old_wave = model.new().snapshot()
	var v3_wave = waves.snapshot()
	v3_wave.version = 3
	v3_wave.erase("map_pressure")
	var migrated = model.new()
	check(migrated.restore(v3_wave) and migrated.map_pressure == 1.0 and migrated.wave_composition(2, 0) == waves.wave_composition(2, 0), "V3 staggered migration preserves actual wave pressure")
	check(migrated.restore(JSON.parse_string(JSON.stringify(migrated.snapshot()))) and migrated.map_pressure == 1.0, "Migrated pressure survives v4 disk roundtrip")
	for invalid_pressure in [NAN, 0.0, 2.01, -1.0]:
		var bad_pressure = migrated.snapshot()
		bad_pressure.map_pressure = invalid_pressure
		var before_pressure = migrated.snapshot()
		check(not migrated.restore(bad_pressure) and migrated.snapshot() == before_pressure, "Invalid pressure rejected atomically")
	var missing_pressure = migrated.snapshot()
	missing_pressure.erase("map_pressure")
	var before_missing = migrated.snapshot()
	check(not migrated.restore(missing_pressure) and migrated.snapshot() == before_missing, "V4 missing pressure rejected atomically")
	old_wave.version = 2
	old_wave.erase("wave_rules")
	check(midwave.restore(old_wave) and midwave.wave_rules == "legacy", "Old run preserves instantaneous wave rules")
	check(midwave.map_pressure == 1.0, "Old save keeps historical pressure rather than new default")
	midwave.begin_round()
	for i in range(50):
		midwave.advance(0.1)
	check(midwave.next_id == 9, "Legacy run still spawns all five at old boundary")
	var legacy_again = model.new()
	check(legacy_again.restore(midwave.snapshot()) and legacy_again.snapshot() == midwave.snapshot(), "Migrated legacy profile survives v3 resave")
	old_wave = waves.snapshot()
	old_wave.wave_rules = "unknown"
	var previous_wave = midwave.snapshot()
	check(not midwave.restore(old_wave) and midwave.snapshot() == previous_wave, "Unknown wave profile rejected without mutation")
	if not r.has_method("confirm_omen"):
		check(false, "Missing observation adjustment confirmation transaction")
		quit(1)
		return
	var omen = model.new()
	check(omen.spin() and omen.reserve.is_empty(), "Observation grants no troops before confirmation")
	check(not omen.spin() and not omen.begin_round() and not omen.construct("barracks"), "Pending result locks reroll battle and pool mutation")
	omen.last_board = ["shield_guard", "archer", "mage", "shield_guard", "archer", "mage", "shield_guard", "archer", "mage"]
	check(omen.bonus_options() == ["shield_guard", "archer", "mage"], "Three completed columns offer distinct bonus choices")
	check(not omen.confirm_omen(), "Multiple bonus roles require explicit choice")
	check(omen.confirm_omen("mage") and omen.reserve == ["shield_guard", "archer", "mage", "mage"], "Confirmation grants base plus selected single bonus")
	check(not omen.confirm_omen("mage"), "Cannot confirm twice")
	var moving = model.new()
	moving.spin()
	moving.last_board = ["shield_guard", "archer", "mage", "", "", "", "", "", ""]
	check(moving.shift_board("row", 0) and moving.last_board.slice(0, 3) == ["mage", "shield_guard", "archer"], "Row shifts one cell with wrapping")
	moving.shift_board("row", 0)
	moving.shift_board("row", 0)
	check(moving.last_board.slice(0, 3) == ["shield_guard", "archer", "mage"] and not moving.shift_board("column", 0), "Returning to original board still consumes all three moves")
	var pending_save = model.new()
	moving.last_board = ["shield_guard", "", "", "", "", "", "", "", ""]
	check(pending_save.restore(JSON.parse_string(JSON.stringify(moving.snapshot()))) and pending_save.omen_pending and pending_save.omen_moves == 0 and pending_save.last_board == moving.last_board and pending_save.rng.state == moving.rng.state, "Pending moves board and RNG survive JSON save")
	var corrupt_pending = moving.snapshot()
	corrupt_pending.board.fill("giant")
	var before_corrupt = pending_save.snapshot()
	check(not pending_save.restore(corrupt_pending) and pending_save.snapshot() == before_corrupt, "Pending save rejects roles outside locked source pool without mutation")
	check(pending_save.confirm_omen() and pending_save.reserve.is_empty(), "Blank/nonmatching result can confirm without bonus")
	var full_queue = model.new()
	full_queue.reserve = ["giant", "giant", "giant", "giant", "shield_guard"]
	var unchanged = full_queue.snapshot()
	check(not full_queue.spin() and full_queue.snapshot() == unchanged, "Weighted capacity rejects before payment free-token or RNG mutation")
	var legacy = model.new().snapshot()
	legacy.version = 1
	for key in ["omen_pending", "omen_moves", "omen_reserved"]:
		legacy.erase(key)
	check(full_queue.restore(legacy) and not full_queue.omen_pending, "Actual v1 save migrates without pending reward")
	legacy.reserve = ["giant", "giant", "giant", "giant", "giant"]
	unchanged = full_queue.snapshot()
	check(not full_queue.restore(legacy) and full_queue.snapshot() == unchanged, "Overweight legacy queue rejected without loss or mutation")
	var paid = model.new()
	paid.free_spin = false
	paid.gold = 19
	unchanged = paid.snapshot()
	check(not paid.spin() and paid.snapshot() == unchanged, "Poor paid spin preserves RNG and gold")
	paid.gold = 20
	check(paid.spin() and paid.gold == 0, "Paid observation charges exactly twenty once")
	paid.last_board = ["shield_guard", "", "", "", "", "", "", "", ""]
	check(paid.shift_board("column", 0) and paid.last_board[3] == "shield_guard" and paid.last_board[0] == "", "Column shift moves down one cell")
	for seed_value in [1947, 1948, 1949]:
		for policy in ["reinforcement", "ranged", "mixed", "paid_mobilization"]:
			run_policy(model, policy, seed_value)
	for pressure in [0.4, 0.6, 0.8]:
		run_policy(model, "paid_mobilization", 1947, pressure)
	for pressure in [0.4, 0.5]:
		for seed_value in [1948, 1949]:
			for policy in ["reinforcement", "ranged", "mixed", "paid_mobilization"]:
				run_policy(model, policy, seed_value, pressure)
	for seed_value in [1947, 1948, 1949]:
		run_policy(model, "paid_mobilization", seed_value, -1.0, true)
	verify_model(model, r)

func run_policy(model: Script, policy: String, seed_value: int, pressure: float = 1.0, whole_campaign: bool = false) -> void:
	var journey = model.new()
	journey.rng.seed = seed_value
	if pressure > 0:
		journey.map_pressure = pressure # Diagnostic fixture, never persists to catalog.
	var refits := 0
	var spent_on_healing := 0
	for step in range(33000 if whole_campaign else 6500):
		if whole_campaign and journey.phase == "VICTORY" and journey.next_map():
			print("CAMPAIGN_ENTER: seed=", seed_value, " map=", journey.current_map + 1, " gold=", journey.gold, " units=", journey.units.size())
		if journey.phase in ["VICTORY", "DEFEAT"]:
			break
		if journey.phase in ["PREPARE", "REFIT"]:
			if journey.phase == "REFIT":
				refits += 1
				var allied := 0
				for unit in journey.units:
					allied += int(unit.side == 0)
				print("FIRST_MAP_REFIT: seed=", seed_value, " policy=", policy, " round=", journey.round_number, " allied=", allied, " enemy=", journey.units.size() - allied, " gold=", journey.gold, " base_hp=", journey.bases[0])
			if policy == "reinforcement":
				while journey.construct("barracks"):
					pass
			elif policy == "mixed":
				if journey.buildings.is_empty():
					journey.construct("barracks")
				if journey.buildings.size() < 2:
					journey.construct("special_barracks")
			elif journey.buildings.is_empty():
				journey.construct("barracks")
			elif journey.buildings[0].id == "barracks":
				journey.upgrade(0, "range")
			if journey.free_spin:
				journey.spin()
			if journey.omen_pending:
				var options: Array = journey.bonus_options()
				journey.confirm_omen(options[0] if not options.is_empty() else "")
			if policy == "paid_mobilization":
				for attempt in range(8):
					for role in journey.reserve.duplicate():
						journey.deploy(role)
					if not journey.spin():
						break
					var options: Array = journey.bonus_options()
					journey.confirm_omen(options[0] if not options.is_empty() else "")
			for survivor in journey.units:
				var previous_gold: int = journey.gold
				journey.heal_unit(int(survivor.id))
				spent_on_healing += previous_gold - journey.gold
			journey.begin_round()
		for role in journey.reserve.duplicate():
			journey.deploy(role)
		journey.advance(0.1)
	check(journey.phase in ["VICTORY", "DEFEAT"], "Real-resource first-map policy reaches terminal state")
	print("CAMPAIGN_POLICY: " if whole_campaign else "FIRST_MAP_POLICY: ", "seed=", seed_value, " map=", journey.current_map + 1, " pressure=", journey.map_pressure, " policy=", policy, " phase=", journey.phase, " round=", journey.round_number, " refits=", refits, " recovery_spend=", spent_on_healing, " base_hp=", journey.bases[0])

func verify_model(model: Script, r) -> void:
	if not r.has_method("heal_unit"):
		check(false, "Missing preparation recovery transaction")
		quit(1)
		return
	var recovery = model.new()
	recovery.units[0].hp = 90.0
	check(recovery.heal_cost(0) == 9, "Half shield: ceil(30 * .5 * .6) = 9G")
	check(recovery.heal_unit(0) and recovery.gold == 111 and recovery.units[0].hp == 180, "Paid recovery restores and charges once")
	check(not recovery.heal_unit(0) and recovery.gold == 111, "Full health cannot repeat payment")
	recovery.units[0].hp = 179.0
	check(recovery.heal_cost(0) == 1, "Fractional recovery price rounds up")
	recovery.gold = 0
	check(not recovery.heal_unit(0) and recovery.units[0].hp == 179, "Insufficient funds preserves HP")
	recovery.gold = 120
	recovery.begin_round()
	check(not recovery.heal_unit(0), "Combat recovery command forbidden")
	recovery.phase = "REFIT"
	check(recovery.heal_unit(0), "Refit recovery enabled")
	recovery.spawn("shield_guard", 1, 60)
	recovery.units[-1].hp = 90
	check(not recovery.heal_unit(recovery.units[-1].id), "Cannot heal enemy by paid command")
	recovery.units[0].hp = 0
	check(not recovery.heal_unit(0) and not recovery.heal_unit(-1), "No resurrection or absent target")
	var recovered = model.new()
	check(recovered.restore(recovery.snapshot()) and recovered.snapshot() == recovery.snapshot(), "Recovery survives existing save format")
	check(r.gold == 120 and r.units.size() == 4, "Start: 120G and four shields")
	check(r.construct("barracks"), "Build T1 general barracks")
	check(r.gold == 80 and r.buildings[0].unit == "shield_guard", "Charge once and supply shield")
	check(not r.upgrade(0, "academy"), "No cross-family upgrade")
	check(not r.upgrade(0, "range"), "Specialization locked until round 2")
	r.round_number = 2
	check(r.upgrade(0, "range"), "General barracks specializes to archer")
	check(r.gold == 30 and r.buildings[0].unit == "archer", "Specialization cost and role")
	check(not r.construct("special_barracks"), "Cannot overspend")
	r.gold = 500
	check(r.construct("special_barracks"), "Separate T1 special root")
	check(r.catalog.unit_families.special.has(r.buildings[1].unit), "Special root draws only special family")
	check(not r.upgrade(1, "range"), "Special root cannot become general")
	check(r.upgrade(1, "academy"), "Special root specializes to mage")
	var before = r.snapshot()
	r.advance(3.0)
	check(r.snapshot() == before, "Refit freezes all simulation")
	r.begin_round()
	for i in range(350):
		r.advance(0.1)
	check(r.reserve.has("archer"), "Barracks automatically produces into reserve")
	check(r.wave_index >= 2, "Timed waves actually spawn")
	check(r.damage_events > 0, "Opposing soldiers actually deal damage")
	var count = r.units.size()
	check(r.deploy("archer"), "Produced archer deploys")
	check(r.units.size() == count + 1, "Deploy creates battle unit")
	var saved = r.snapshot()
	var restored = model.new()
	check(restored.restore(saved), "Restore valid snapshot")
	check(restored.snapshot() == saved, "Restore has no duplicated production or waves")
	check(restored.restore(JSON.parse_string(JSON.stringify(saved))), "Actual JSON number conversion round-trip")
	var restored_before = restored.snapshot()
	check(not restored.restore({"version": 900}), "Reject unknown save without mutation")
	check(restored.snapshot() == restored_before, "Invalid save leaves run unchanged")
	var corrupt = saved.duplicate(true)
	corrupt.gold = -1
	check(not restored.restore(corrupt), "Reject negative-gold save")
	corrupt = saved.duplicate(true)
	corrupt.units[0].side = 9
	check(not restored.restore(corrupt), "Reject invalid faction before indexing bases")
	corrupt = saved.duplicate(true)
	corrupt.buildings[0].unit = "mage"
	check(not restored.restore(corrupt), "Reject saved facility/role mismatch")
	corrupt = saved.duplicate(true)
	corrupt.units[0].x = NAN
	check(not restored.restore(corrupt), "Reject non-finite position")
	for i in range(250):
		r.advance(0.1)
	check(r.phase != "BATTLE", "Round ends after configured duration")
	var slots = model.new()
	slots.gold = 10000
	for i in range(6):
		check(slots.construct("barracks"), "Base slot %s" % i)
	check(not slots.construct("barracks"), "Cannot build beyond six unlocked slots")
	slots.points = [1, 0, 0]
	check(slots.construct("barracks"), "Capture unlocks seventh slot")
	check(slots.restore(JSON.parse_string(JSON.stringify(slots.snapshot()))) and slots.unlocked_slots() == 7, "Captured slot remains unlocked after disk round-trip")
	slots.points = [0, 0, 0]
	check(not slots.building_active(6) and slots.buildings.size() == 7, "Lost slot disables, never deletes building")
	var refit = model.new()
	refit.construct("barracks")
	refit.phase = "REFIT"
	check(refit.upgrade(0, "range"), "Round 1 refit prepares round 2 specialization")
	var duel = model.new()
	duel.units.clear()
	duel.spawn("shield_guard", 0, 50.0)
	duel.spawn("shield_guard", 1, 51.0)
	duel.units[1].cooldown = 10.0
	duel.phase = "BATTLE"
	duel.advance(0.05)
	check(duel.damage_events == 0 and duel.units[0].get("windup", 0) > 0, "Shield must prepare before damage")
	var windup_save = duel.snapshot()
	var resumed = model.new()
	check(resumed.restore(JSON.parse_string(JSON.stringify(windup_save))), "Save during windup restores")
	duel.advance(0.14)
	check(duel.damage_events == 0, "No early hit during preparation")
	duel.advance(0.05)
	check(duel.damage_events == 1 and duel.units[0].action > 0, "Impact frame and single damage occur together")
	resumed.advance(0.19)
	check(resumed.damage_events == 1, "Restored windup hits once")
	duel.advance(0.2)
	check(duel.damage_events == 1, "Recovery never deals duplicate damage")
	var missed = model.new()
	missed.restore(windup_save)
	missed.units[1].x = 90.0
	missed.advance(0.2)
	check(missed.damage_events == 0, "Out-of-range windup does not hit a replacement target")
	var siege = model.new()
	siege.units.clear()
	siege.spawn("shield_guard", 0, 100.0)
	siege.phase = "BATTLE"
	siege.advance(0.05)
	check(siege.bases[1] == 1000, "Base strike also waits for preparation")
	siege.advance(0.2)
	check(siege.bases[1] < 1000, "Base strike resolves on impact")
	var legacy = windup_save.duplicate(true)
	for u in legacy.units:
		u.erase("windup")
		u.erase("pending_target")
	check(resumed.restore(legacy), "Old v1 saves remain readable")
	var dead = model.new()
	dead.restore(windup_save)
	dead.units[0].hp = 0
	dead.advance(0.2)
	check(dead.damage_events == 0, "Dead attacker cannot finish pending strike")
	dead.restore(windup_save)
	dead.units[1].hp = 0
	dead.advance(0.2)
	check(dead.damage_events == 0, "Dead target cannot receive pending strike")
	resumed.restore(windup_save)
	resumed.phase = "REFIT"
	var frozen = resumed.snapshot()
	resumed.advance(0.5)
	check(resumed.snapshot() == frozen, "Refit freezes in-progress animation and damage")
	for invalid in [-1.0, 99.0, NAN]:
		var bad = windup_save.duplicate(true)
		bad.units[0].windup = invalid
		check(not resumed.restore(bad) and resumed.snapshot() == frozen, "Invalid windup fails atomically")
	var intel = model.new()
	check(intel.has_method("wave_forecast") and intel.has_method("production_status"), "Missing live forecast and production queries")
	if not intel.has_method("wave_forecast") or not intel.has_method("production_status"):
		quit(1)
		return
	var untouched = intel.snapshot()
	var forecast = intel.wave_forecast()
	check(forecast.round == 1 and forecast.wave == 1 and forecast.seconds == 5, "Preparation forecasts first actual wave")
	check(intel.snapshot() == untouched, "Inspecting forecast never consumes RNG or alters battle")
	intel.begin_round()
	for i in range(5):
		intel.advance(1.0)
	check(intel.wave_forecast().wave == 2 and is_equal_approx(intel.wave_forecast().seconds, 17), "Forecast advances after first arrival")
	intel.advance(1.0)
	intel.advance(0.7)
	var actual: Dictionary = {}
	for actor in intel.units:
		if actor.side == 1:
			actual[actor.role] = actual.get(actor.role, 0) + 1
	check(actual == forecast.units, "Forecast exactly matches spawned role counts")
	intel.wave_index = 3
	check(intel.wave_forecast().is_empty(), "No invented fourth wave")
	intel.phase = "REFIT"
	check(intel.wave_forecast().round == 2 and intel.wave_forecast().seconds == 5, "Refit forecasts next round, not finished round")
	intel.phase = "VICTORY"
	check(intel.wave_forecast().is_empty(), "No forecast after victory")
	intel = model.new()
	intel.construct("barracks")
	check(intel.production_status(0).state == "FROZEN", "Production reports preparation freeze")
	intel.begin_round()
	intel.advance(1)
	check(intel.production_status(0).state == "PRODUCING" and is_equal_approx(intel.production_status(0).remaining, 29), "Production exposes actual clock")
	for i in range(24):
		intel.reserve.append("shield_guard")
	check(intel.production_status(0).state == "QUEUE_FULL", "Full queue is visible")
	check(intel.production_status(8).state == "EMPTY", "Empty slot has no invented production")
	intel.gold = 1000
	intel.phase = "PREPARE"
	for i in range(5):
		intel.construct("barracks")
	intel.points[0] = 1
	intel.construct("barracks")
	intel.points[0] = 0
	check(intel.production_status(6).state == "LOCKED", "Lost territory reports disabled production")
	print("REPLAN_SLICE_TEST: %s checks, %s failures" % [checks, failures])
	quit(0 if failures == 0 else 1)
