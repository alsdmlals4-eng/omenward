extends SceneTree

var checks := 0
var failures := 0

func check(ok: bool, message: String) -> void:
	checks += 1
	if not ok:
		failures += 1
		push_error(message)

func verify_birth_records(model: Script) -> void:
	verify_three_fronts(model)
	verify_area_selection(model)
	verify_capstones(model)
	var run = model.new()
	check(run.has_method("deploy_entry"), "P03 must preserve production birth identity through exact deployment")
	if not run.has_method("deploy_entry"):
		return
	run.gold = 1000
	run.construct("barracks")
	var original_id: int = run.buildings[0].instance_id
	run.phase = "BATTLE"
	run.buildings[0].clock = 99.0
	run.advance_ticks(1)
	check(run.reserve[0] is Dictionary and run.reserve[0].birth_tier == 1 and run.reserve[0].source_facility_id == original_id, "Production records actual T1 source")
	var born: Dictionary = run.reserve[0].duplicate(true)
	run.phase = "REFIT"
	check(run.upgrade(0, "range") and run.buildings[0].instance_id == original_id, "Specialization retains facility instance")
	run.phase = "BATTLE"
	run.buildings[0].clock = 99.0
	run.advance_ticks(1)
	check(run.reserve[1].role_id == "archer" and run.reserve[1].birth_tier == 2 and run.reserve[0] == born, "New T2 production never rewrites old T1 recruit")
	check(run.deploy_entry(int(born.entry_id)) and run.units.back().birth_tier == 1 and run.units.back().source_facility_id == original_id, "Exact entry deployment carries frozen birth fields")
	check(not run.deploy_entry(int(born.entry_id)), "Entry cannot deploy twice")
	run.phase = "REFIT"
	run.demolish(0)
	run.construct("barracks")
	check(run.buildings[0].instance_id > original_id, "Rebuilt same slot cannot reuse old source identity")
	var copy = model.new()
	var loaded: bool = copy.restore(JSON.parse_string(JSON.stringify(run.snapshot())))
	check(loaded, "Birth state accepts valid disk JSON")
	check(copy.reserve == run.reserve, "Birth records preserve typed fields through JSON")
	var corrupt: Dictionary = run.snapshot()
	corrupt.reserve[0].birth_tier = 4
	check(not copy.restore(corrupt), "Invalid birth tier fails closed")
	check(run.reserve[0].birth_tier == 2, "Snapshot is deeply isolated from live recruits")
	corrupt = run.snapshot()
	corrupt.reserve[0].entry_id = born.entry_id
	check(not copy.restore(corrupt), "Duplicate deployed/reserve birth identity rejected")
	var omen = model.new()
	omen.gold = 1000
	omen.construct("barracks")
	omen.phase = "REFIT"
	omen.upgrade(0, "shield_hall")
	omen.spin()
	var token := {"role_id": "shield_guard", "birth_tier": 2, "source_facility_id": 1}
	omen.last_board = [token.duplicate(), token.duplicate(), token.duplicate(), "", "", "", "", "", ""]
	check(omen.has_method("omen_reward_tokens"), "Omen must preserve token birth metadata rather than returning role-only recruits")
	if not omen.has_method("omen_reward_tokens"):
		return
	check(omen.confirm_omen() and omen.reserve.size() == 2 and omen.reserve[0].birth_tier == 2 and omen.reserve[1].birth_tier == 2, "T2 line yields both actual T2 base reward and bonus")
	check(omen.reserve[0].source_facility_id == 1 and omen.reserve[0].entry_id != omen.reserve[1].entry_id, "Omen keeps facility source but issues unique recruit identities")
	omen.spin()
	omen.last_board = [token.duplicate(), "shield_guard", token.duplicate(), "", "", "", "", "", ""]
	var pending = model.new()
	check(pending.restore(JSON.parse_string(JSON.stringify(omen.snapshot()))), "Pending mixed-tier tokens survive verified JSON restore")
	check(omen.confirm_omen() and omen.reserve[2].birth_tier == 1 and omen.reserve[3].birth_tier == 1, "Mixed-tier group and line use lowest tier instead of duplicating a high token")
	var future: Dictionary = omen.snapshot()
	future.birth_rules = "birth_v999"
	check(not copy.restore(future), "Unknown birth rules are rejected")
	var invalid: Dictionary = run.snapshot()
	invalid.units[0].erase("entry_id")
	check(not copy.restore(invalid), "Partial unit birth metadata cannot bypass validation")
	invalid = run.snapshot()
	invalid.buildings[0].erase("instance_id")
	check(not copy.restore(invalid), "New facility identity cannot be omitted")
	invalid = run.snapshot()
	invalid.reserve[0].source_facility_id = 0
	check(not copy.restore(invalid), "Base source cannot manufacture T2 recruit")
	invalid = model.new().snapshot()
	invalid.erase("birth_rules")
	invalid.map_entry.erase("birth_rules")
	check(not copy.restore(invalid), "Missing marker cannot silently downgrade birth records")
	invalid = run.snapshot()
	invalid.map_entry.next_facility_id = 999
	check(not copy.restore(invalid), "Checkpoint cannot contain future facility counter")

func verify_three_fronts(model: Script) -> void:
	var run = model.new()
	check(run.has_method("enable_three_fronts"), "New game must support three concurrently simulated fronts")
	if not run.has_method("enable_three_fronts"):
		return
	run.enable_three_fronts()
	check(run.front_count() == 3 and run.units[1].front == 1 and run.units[2].front == 2, "Initial defenders distribute among all three fronts")
	run.units.clear()
	run.spawn("mage", 0, 50, 0)
	run.spawn("giant", 1, 51, 1)
	check(run.choose_target(run.units[0]).is_empty(), "Identical positions on other fronts are not attack targets")
	run.spawn("giant", 1, 51, 0)
	run._hit(run.units[0], run.units[2])
	check(run.units[1].hp == 320 and run.units[2].hp < 320, "Area damage cannot leak across fronts")
	run.phase = "BATTLE"
	run.points = [1, 0, 0]
	run._tick_tower(2)
	check(run.units[1].hp == 320, "Owned tower cannot damage another front")
	run.units.clear()
	run.spawn("shield_guard", 0, 50, 2)
	run.points = [0, 0, 0]
	for i in range(240):
		run._tick_capture()
	check(run.points == [0, 0, 1], "Single frontline soldier claims only its front midpoint")
	run.selected_front = 1
	run._enqueue("archer")
	check(run.deploy_entry(int(run.reserve[0].entry_id)) and run.units.back().front == 1, "Exact reserve deployment commits to selected front")
	var restored = model.new()
	check(restored.restore(JSON.parse_string(JSON.stringify(run.snapshot()))) and restored.front_count() == 3 and restored.selected_front == 1, "Three-front snapshot preserves selection and real unit assignment")
	var bad: Dictionary = run.snapshot()
	bad.units[0].front = 3
	check(not restored.restore(bad), "Out-of-range front rejected without mutation")
	bad = run.snapshot()
	bad.front_rules = "three_future"
	check(not restored.restore(bad), "Unknown front rules fail closed")
	check(restored.restore(model.new().snapshot()) and restored.front_count() == 1, "Existing single-front game is not silently migrated")
	var waves = model.new()
	waves.enable_three_fronts()
	var forecast_before: Dictionary = waves.snapshot()
	var forecast: Dictionary = waves.wave_forecast()
	check(forecast.has("fronts"), "Forecast must disclose actual next-wave assignment for each front")
	if forecast.has("fronts"):
		check(forecast.fronts == [{"shield_guard": 1}, {"shield_guard": 1}, {"archer": 1}], "First wave distributes actual two shields and one archer without multiplying them")
		waves.selected_front = 2
		check(waves.wave_forecast() == forecast, "Inspection cannot change incoming enemy assignments")
		waves.selected_front = 0
		forecast.fronts[0]["shield_guard"] = 999
		check(waves.snapshot() == forecast_before and waves.wave_forecast().fronts[0].shield_guard == 1, "Forecast projection must be read-only and deeply isolated")
	waves.begin_round()
	waves.advance_ticks(270)
	var lanes: Array = []
	for unit in waves.units:
		if unit.side == 1 and not lanes.has(unit.front):
			lanes.append(unit.front)
	check(lanes.size() == 3, "Existing wave total reaches all three fronts without view dependence")
	if forecast.has("fronts"):
		var arrived: Array = [{}, {}, {}]
		for unit in waves.units:
			if unit.side == 1:
				arrived[unit.front][unit.role] = arrived[unit.front].get(unit.role, 0) + 1
		var preview = model.new()
		preview.enable_three_fronts()
		check(arrived == preview.wave_forecast().fronts, "Displayed frontline counts match real first-wave arrivals")
	var old_waves = model.new()
	old_waves.begin_round()
	old_waves.advance_ticks(270)
	check(waves.units.filter(func(u): return u.side == 1).size() == old_waves.units.filter(func(u): return u.side == 1).size(), "Three fronts distribute rather than triple the same wave")
	var live_before: Dictionary = run.snapshot()
	for selection in [-1, 3, 1.5, null]:
		bad = live_before.duplicate(true)
		bad.selected_front = selection
		var input_before := bad.duplicate(true)
		check(not run.restore(bad) and run.snapshot() == live_before and bad == input_before, "Invalid selection is rejected atomically without mutating input")
	bad = live_before.duplicate(true)
	bad.units[0].erase("front")
	check(not run.restore(bad), "Missing front on a three-front unit fails closed")
	bad = live_before.duplicate(true)
	bad.map_entry.front_rules = "single_v1"
	check(not run.restore(bad), "Checkpoint cannot silently change front topology")
	run.units.clear()
	run.spawn("priest", 0, 50, 0)
	run.spawn("shield_guard", 0, 50, 1)
	run.units[0].survived = 5
	run.units[0].heal_count = 2
	run.units[1].hp = 179
	run.apply_status(run.units[1], "slow", 0.3, 1)
	var untouched: Array = run.units.duplicate(true)
	run.heal_target(run.units[0], run.units[1])
	check(run.units == untouched, "Direct cross-front heal cannot heal, cleanse, shield or advance counters")

func verify_area_selection(model: Script) -> void:
	for side in [0, 1]:
		var run = model.new()
		run.units.clear()
		var direction: float = 1.0 if side == 0 else -1.0
		run.spawn("greatsword_warrior", side, 50)
		run.spawn("giant", 1 - side, 50 + direction * 0.5)
		run.spawn("giant", 1 - side, 50 - direction * 0.5)
		run.spawn("giant", 1 - side, 50 + direction * 1.0)
		run._hit(run.units[0], run.units[1])
		check(run.units[2].hp == 320 and run.units[3].hp < 320, "Greatsword sweep excludes rear enemies on either side")
		check(run.units[0].hit_count == 1 and run.damage_events == 2, "Area hit counts one basic swing and one hit per selected target")
	var run = model.new()
	run.units.clear()
	run.spawn("mage", 0, 10)
	run.spawn("giant", 1, 20)
	run.spawn("giant", 1, 21.5)
	run.spawn("giant", 1, 20.25)
	run.spawn("giant", 1, 20.5)
	run.spawn("giant", 1, 19.5)
	run.spawn("giant", 0, 20.1)
	run.spawn("giant", 1, 20.1)
	run.units.back().hp = 0
	var attacker: Dictionary = run.units[0]
	var primary: Dictionary = run.units[1]
	var farther: Dictionary = run.units[2]
	var tied_first: Dictionary = run.units[4]
	var tied_second: Dictionary = run.units[5]
	run.units.reverse()
	run._hit(attacker, primary)
	check(farther.hp == 320 and tied_first.hp < 320 and tied_second.hp < 320, "Mage cap selects closest candidates independent of live array order")
	check(run.damage_events == 4 and attacker.hit_count == 1, "Mage primary appears once and dead/allied candidates are excluded")
	# With one nearer extra, only the lower ID of an equidistant pair fits the remaining cap.
	for unit in run.units:
		if unit.hp > 0:
			unit.hp = float(run.definitions[unit.role][4])
	run.spawn("giant", 1, 20.1)
	run._hit(attacker, primary)
	check(tied_first.hp < 320 and tied_second.hp == 320, "Equal-distance final slot uses lower unit ID, not array order")
	# Existing save validation permits distinct fractional numeric unit IDs.
	tied_first.id = 4.1
	tied_second.id = 4.9
	for order in range(2):
		for unit in run.units:
			if unit.hp > 0:
				unit.hp = float(run.definitions[unit.role][4])
		run.units.reverse()
		run._hit(attacker, primary)
		check(tied_first.hp < 320 and tied_second.hp == 320, "Distinct legacy numeric IDs retain deterministic tie priority")

func verify_capstones(model: Script) -> void:
	var run = model.new()
	check(run.has_method("upgrade_tier"), "P03 requires guarded T3 purchase connected to birth records")
	if not run.has_method("upgrade_tier"):
		return
	run.gold = 1000
	run.construct("barracks")
	check(not run.upgrade_tier(0), "T1 cannot skip specialization")
	run.phase = "REFIT"
	run.upgrade(0, "range")
	check(not run.upgrade_tier(0), "T3 stays locked before first-map round6")
	run.round_number = 5
	run._enqueue("archer", 2, 1)
	var price_before: int = run.gold
	check(run.upgrade_tier(0) and run.gold == price_before - 63 and run.facility_tier(0) == 3, "Round5 refit enables T3 at ceil50*1.25 cost")
	check(not run.upgrade_tier(0) and run.reserve[0].birth_tier == 2, "T3 cannot purchase twice or upgrade existing reserve")
	run.phase = "BATTLE"
	run.buildings[0].clock = 99
	run.advance_ticks(1)
	check(run.reserve[1].birth_tier == 3, "Subsequent production carries T3")
	var copy = model.new()
	check(copy.restore(JSON.parse_string(JSON.stringify(run.snapshot()))) and copy.facility_tier(0) == 3, "T3 building and recruits round-trip")
	check(run.deploy_entry(int(run.reserve[1].entry_id)) and run.units.back().birth_tier == 3, "Exact T3 recruit deploys without promoting older one")
	run.units.clear()
	run.spawn("priest", 0, 10)
	run.spawn("shield_guard", 0, 11)
	run.units[0].birth_tier = 3
	run.units[1].hp = 100
	run.heal_target(run.units[0], run.units[1])
	check(run.units[1].hp == 115, "T3 priest heals15 rather than base12")
	run.units.clear()
	run.spawn("spear_guard", 0, 10)
	run.units[0].birth_tier = 3
	check(is_equal_approx(run.attack_range(run.units[0]), 5.4), "T3 spear has actual1.8 range in model units")
	var fight = model.new()
	fight.units.clear()
	fight.phase = "BATTLE"
	fight.spawn("archer", 0, 10)
	fight.spawn("giant", 1, 15)
	fight.units[0].birth_tier = 3
	fight.units[0].survived = 2
	fight._hit(fight.units[0], fight.units[1])
	fight._hit(fight.units[0], fight.units[1])
	var before: float = fight.units[1].hp
	fight._hit(fight.units[0], fight.units[1])
	check(is_equal_approx(before - fight.units[1].hp, 18.0 * 100 / 130 * 1.35), "T3 veteran archer enhances third shot to1.35")
	fight.units.clear()
	fight.spawn("mage", 0, 10)
	fight.units[0].birth_tier = 3
	for i in range(5):
		fight.spawn("giant", 1, 15 + i * 0.1)
	fight._hit(fight.units[0], fight.units[1])
	check(fight.units[5].hp < 320, "T3 mage hits fifth clustered target")
	fight.units.clear()
	fight.spawn("shield_guard", 0, 10)
	fight.spawn("shield_guard", 1, 11)
	fight.units[0].birth_tier = 3
	fight.apply_status(fight.units[0], "stun", 0, 0.6)
	check(is_equal_approx(fight.units[0].effects.stun, 0.3), "T3 guarding shield halves stun duration")
	fight.units.clear()
	fight.spawn("cavalry", 0, 10)
	fight.spawn("giant", 1, 11)
	fight.units[0].birth_tier = 3
	fight.units[0].charge = 2.0
	fight._hit(fight.units[0], fight.units[1])
	before = fight.units[0].hp
	fight.take_damage(fight.units[0], 100)
	check(is_equal_approx(before - fight.units[0].hp, 85), "T3 charge provides15percent reduction after impact")
	for i in range(60):
		fight._tick_effects(fight.units[0], 1.0 / 30.0)
	before = fight.units[0].hp
	fight.take_damage(fight.units[0], 10)
	check(is_equal_approx(before - fight.units[0].hp, 10), "Charge guard expires rather than persisting forever")
	fight.units.clear()
	fight.spawn("assassin", 0, 10)
	fight.spawn("archer", 1, 11)
	fight.units[0].birth_tier = 3
	fight._hit(fight.units[0], fight.units[1])
	before = fight.units[0].hp
	fight._hit(fight.units[1], fight.units[0])
	check(is_equal_approx(before - fight.units[0].hp, 18.0 * 100 / 108 * 0.75), "T3 ambush guards against immediate ranged retaliation")
	fight.units.clear()
	fight.spawn("flying", 0, 10)
	fight.spawn("giant", 1, 11)
	fight.units[0].birth_tier = 3
	fight._hit(fight.units[0], fight.units[1])
	check(is_equal_approx(320 - fight.units[1].hp, 20.0 * 100 / 130 * 1.3), "T3 flying opening multiplier applies once")
	before = fight.units[1].hp
	fight._hit(fight.units[0], fight.units[1])
	check(is_equal_approx(before - fight.units[1].hp, 20.0 * 100 / 130), "Flying second hit cannot reuse opening")
	fight.units.clear()
	fight.spawn("greatsword_warrior", 0, 10)
	fight.spawn("giant", 1, 11)
	fight.units[0].birth_tier = 3
	for i in range(4):
		fight._hit(fight.units[0], fight.units[1])
	check(fight.units[1].effects.get("armor_break", 0) == 10, "T3 fourth slash applies nonstacking armor reduction")
	fight.units.clear()
	fight.spawn("giant", 0, 100)
	fight.units[0].birth_tier = 3
	fight.advance_ticks(1)
	check(is_equal_approx(1000 - fight.bases[1], 34 * 1.7), "T3 giant applies actual1.7 structure multiplier")
	var states = model.new()
	states.gold = 1000
	states.construct("barracks")
	states.phase = "REFIT"
	states.upgrade(0, "stable")
	states.round_number = 5
	states.upgrade_tier(0)
	states._enqueue("cavalry", 3, 1)
	states.units.clear()
	states.deploy_entry(int(states.reserve[0].entry_id))
	states.spawn("giant", 1, 6)
	states.units[0].charge = 2
	states._hit(states.units[0], states.units[1])
	var saved: Dictionary = states.snapshot()
	check(saved.units[0].effects.damage_guard == 60 and copy.restore(JSON.parse_string(JSON.stringify(saved))), "Guard saves in integer ticks and restores")
	check(is_equal_approx(copy.units[0].effects.damage_guard, 2.0), "Guard restore returns same model duration")
	saved.units[0].effects.damage_guard = 61
	check(not copy.restore(saved), "Guard cannot restore longer than2seconds")
	saved = states.snapshot()
	saved.units[1].effects = {"armor_break": 10}
	check(not copy.restore(saved), "Armor reduction requires matching live duration")
	saved = states.snapshot()
	saved.units[1].effects = {"damage_guard": 30}
	check(not copy.restore(saved), "Charge-only guard cannot attach to unrelated giant")
	var old = model.new()
	saved = old.snapshot()
	saved.birth_rules = "birth_v1"
	saved.map_entry.birth_rules = "birth_v1"
	check(old.restore(saved), "Previous birth_v1 profile remains supported")
	saved.units[0].effects = {"armor_break": 10, "armor_break_time": 30}
	check(not old.restore(saved), "Previous ruleset rejects newly introduced effect fields")
	old.gold = 1000
	old.construct("barracks")
	old.phase = "REFIT"
	old.upgrade(0, "range")
	old.round_number = 5
	check(not old.upgrade_tier(0), "Previous profile does not silently gain T3 rules")
	states.phase = "REFIT"
	states.spin()
	var t3_token := {"role_id": "cavalry", "birth_tier": 3, "source_facility_id": 1}
	states.last_board = [t3_token, t3_token.duplicate(), t3_token.duplicate(), "", "", "", "", "", ""]
	check(copy.restore(JSON.parse_string(JSON.stringify(states.snapshot()))) and copy.confirm_omen() and copy.reserve[0].birth_tier == 3, "T3 pending tokens restore and award T3 recruits")
	fight.units.clear()
	fight.spawn("flying", 0, 10)
	fight.spawn("giant", 1, 11)
	fight.units[0].birth_tier = 3
	fight.units[0].air_reengage = 0.1
	fight.apply_status(fight.units[0], "stun", 0, 0.1)
	fight.advance_ticks(1)
	check(is_equal_approx(fight.units[0].air_reengage, 8), "Stunned flying unit still counts nearby engagement for rearm")
	fight.units.clear()
	fight.spawn("assassin", 0, 50)
	fight.units[0].birth_tier = 3
	fight.units[0].effects = {"ranged_guard": 1.0}
	fight.points[1] = -1
	fight.tower_clock = 0
	fight._tick_tower(2)
	check(is_equal_approx(fight.units[0].hp, 96.5), "T3 ranged guard also protects against tower shots")
	before = fight.units[0].hp
	fight.take_damage(fight.units[0], 10)
	check(is_equal_approx(before - fight.units[0].hp, 10), "Ranged guard never reduces melee/untyped damage")
	fight.units.clear()
	fight.spawn("flying", 1, 90)
	fight.spawn("giant", 0, 89)
	fight.units[0].birth_tier = 3
	fight._hit(fight.units[0], fight.units[1])
	check(is_equal_approx(320 - fight.units[1].hp, 20.0 * 100 / 130 * 1.3), "Veil uses the same T3 opening rule when explicitly authored")
	fight.units[1].x = 0
	fight.units[1].cooldown = 60
	fight.units[0].cooldown = 60
	fight.wave_index = 3
	fight.elapsed = 0
	fight.advance_ticks(239)
	check(fight.units[0].air_reengage > 0, "Flying rearm cannot finish before eight seconds away")
	fight.advance_ticks(1)
	check(is_zero_approx(fight.units[0].air_reengage), "Flying rearms after full eight seconds away")

func verify_logistics(model: Script) -> void:
	verify_birth_records(model)
	verify_fixed_slots(model)
	var run = model.new()
	check(run.has_method("capacity_limit"), "P03 missing shared logistics capacity")
	if not run.has_method("capacity_limit"):
		return
	check(run.capacity_limit() == 18 and run.construct("logistics"), "Logistics is buildable at base capacity")
	check(run.capacity_limit() == 24 and run.gold == 85, "Active logistics adds6 for35G")
	var slot = run.production_status(0)
	check(slot.state == "PASSIVE", "Logistics exposes passive supply, not unit production")
	var restored = model.new()
	check(restored.restore(JSON.parse_string(JSON.stringify(run.snapshot()))) and restored.capacity_limit() == 24, "Logistics survives validated save")
	run.begin_round()
	run.advance_ticks(120)
	check(run.reserve.is_empty(), "Logistics never creates blank units")
	run = model.new()
	run.gold = 1000
	for i in range(6):
		run.construct("barracks")
	run.points[0] = 1
	check(run.construct("logistics") and run.capacity_limit() == 24, "Territory slot can host logistics")
	run.units.clear()
	for i in range(10):
		run.spawn("shield_guard", 0, 5)
	run.reserve.append("shield_guard")
	run.points[0] = 0
	check(run.capacity_limit() == 18 and run.units.size() == 10 and not run.deploy("shield_guard"), "Lost slot disables capacity without deleting overcap army")
	run.points[0] = 1
	check(run.deploy("shield_guard") and run.capacity_used() == 22, "Recaptured slot re-enables deployment")
	var pool_before: int = run.spin_required_capacity()
	run.points[0] = 0
	check(run.spin_required_capacity() == pool_before, "Logistics never adds an omen unit source")

func verify_fixed_slots(model: Script) -> void:
	var run = model.new()
	var gate = model.new()
	gate.gold = 1000
	gate.construct("barracks")
	check(not gate.upgrade(0, "range"), "First round preparation keeps T2 locked")
	gate.phase = "VICTORY"
	gate._settle_map(false)
	check(gate.next_map() and gate.upgrade(0, "range"), "T2 must remain open in second map round1")
	check(run.has_method("demolish"), "P03 missing fixed-slot demolition")
	if not run.has_method("demolish"):
		return
	run.gold = 1000
	for i in range(6):
		run.construct("barracks")
	run.points[0] = 1
	run.construct("logistics")
	run.points[0] = 0
	run.spin()
	run.confirm_omen()
	check(not run.reserve.is_empty(), "Demolition preservation fixture has confirmed troops")
	var before_gold: int = run.gold
	var before_reserve: Array = run.reserve.duplicate()
	var before_units: Array = run.units.duplicate(true)
	check(not run.demolish(6), "Locked facility cannot be demolished")
	check(run.demolish(0) and run.buildings.size() == 7, "Demolition leaves an uncompressed slot")
	check(run.gold == before_gold and run.reserve == before_reserve and run.units == before_units, "Demolition has no refund or army loss")
	check(run.buildings[6].id == "logistics" and run.capacity_limit() == 18, "Locked logistics cannot slide into active slots")
	check(run.production_status(0).state == "EMPTY" and not run.building_active(0), "Empty slot never produces")
	var restored = model.new()
	check(restored.restore(JSON.parse_string(JSON.stringify(run.snapshot()))) and restored.buildings[6].id == "logistics" and restored.reserve == before_reserve, "Sparse slots preserve indices and confirmed troops through save")
	check(restored.construct("special_barracks") and restored.buildings[0].id == "special_barracks" and restored.buildings.size() == 7, "Construction reuses first unlocked hole")
	var broken: Dictionary = run.snapshot()
	broken.buildings[0].unit = "shield_guard"
	check(not restored.restore(broken), "Empty slot cannot carry a hidden unit")
	broken = run.snapshot()
	broken.facility_rules = "logistics_v1"
	check(not restored.restore(broken), "Old facility schema cannot import sparse slots")
	check(not run.demolish(0) and not run.demolish(-1) and not run.demolish(99), "Empty and invalid slots reject demolition")
	run.points[0] = 1
	check(run.demolish(6) and run.capacity_limit() == 18, "Active logistics removal drops capacity")
	run = model.new()
	run.construct("barracks")
	run.spin()
	check(not run.demolish(0), "Pending omen source cannot be removed")
	run.confirm_omen()
	run.begin_round()
	check(not run.demolish(0), "Combat rejects demolition")
	run.phase = "REFIT"
	check(run.demolish(0), "Refit permits demolition")
	run = model.new()
	run.facility_rules = "logistics_v1"
	run.construct("barracks")
	check(not run.demolish(0), "Existing logistics profile keeps its prior rules")

func verify_capture(model: Script) -> void:
	var run = model.new()
	check(run.has_method("capture_state"), "P02 missing timed capture")
	if not run.has_method("capture_state"):
		return
	run.units.clear()
	run.spawn("shield_guard", 0, 25)
	run.apply_status(run.units[0], "stun", 0, 30)
	run.begin_round()
	run.advance_ticks(239)
	check(run.points[0] == 0, "One ground unit cannot capture before eight seconds")
	var restored = model.new()
	check(restored.restore(JSON.parse_string(JSON.stringify(run.snapshot()))), "Partial capture survives disk")
	run.advance_ticks(1)
	restored.advance_ticks(1)
	check(run.points[0] == 1 and restored.points[0] == 1, "Ground unit captures at240ticks after save")
	run = model.new()
	run.units.clear()
	for i in range(10):
		run.spawn("flying", 0, 25)
		run.apply_status(run.units[-1], "stun", 0, 30)
	run.begin_round()
	run.advance_ticks(240)
	check(run.points[0] == 0 and run.capture_state(0).progress == 0, "Flying units cannot capture")
	run = model.new()
	run.units.clear()
	for side in [0, 1]:
		run.spawn("shield_guard", side, 50)
		run.apply_status(run.units[-1], "stun", 0, 30)
	run.begin_round()
	run.advance_ticks(30)
	check(run.capture_state(1).progress == 0, "Contested point freezes without ownership change")
	run.units.pop_back()
	run.advance_ticks(120)
	check(is_equal_approx(run.capture_state(1).progress, 0.5), "Half claim after four seconds")
	run.units[0].x = 30
	run.advance_ticks(30)
	check(is_equal_approx(run.capture_state(1).progress, 0.4), "Abandoned capture decays one tenth per second")
	run = model.new()
	run.units.clear()
	run.points[1] = -1
	for i in range(2):
		run.spawn("shield_guard", 0, 50)
		run.apply_status(run.units[-1], "stun", 0, 30)
	run.begin_round()
	run.advance_ticks(120)
	check(run.points[1] == 0, "Two ground units neutralize enemy tower in four seconds")
	run.advance_ticks(120)
	check(run.points[1] == 1, "Neutralized tower requires a second claim leg")
	var marching = model.new()
	marching.units.clear()
	marching.spawn("shield_guard", 0, 25)
	marching.begin_round()
	marching.advance_ticks(240)
	check(marching.points[0] == 1, "Automatic ground advance holds long enough to secure empty point")
	var held_x: float = marching.units[0].x
	marching.advance_ticks(1)
	check(marching.units[0].x > held_x, "Secured point releases automatic advance")
	var contested = model.new()
	contested.units.clear()
	contested.spawn("shield_guard", 0, 22)
	contested.spawn("shield_guard", 1, 28)
	contested.begin_round()
	contested.advance_ticks(1)
	check(contested.units[0].x > 22 and contested.units[1].x < 28, "Contested edge holders close distance instead of deadlocking")
	var siege = model.new()
	siege.units.clear()
	siege.begin_round()
	siege.advance_ticks(600)
	check(siege.gold == 125 and siege.basic_gold_paid == 5, "Early settlement excludes already paid basic income")
	siege.spawn("giant", 0, 100)
	# Spawned waves precede the new giant in the array.
	siege.apply_status(siege.units[-1], "stun", 0, 30)
	siege.bases[1] = 0
	siege.advance_ticks(239)
	check(siege.phase == "BATTLE", "Breached base needs ground claim, not HP-only victory")
	siege.advance_ticks(1)
	check(siege.phase == "VICTORY" and siege.gold == 270, "Base claim settles remaining145G of map basic income once")
	var paid: Dictionary = siege.snapshot()
	check(model.new().restore(JSON.parse_string(JSON.stringify(paid))), "Settled map saves correctly")
	siege.advance_ticks(300)
	check(siege.snapshot() == paid, "Repeated updates after victory cannot duplicate reward")
	var both = model.new()
	both.begin_round()
	both.bases = [0, 0]
	both.advance_ticks(1)
	check(both.phase == "DEFEAT" and both.gold == 120, "Home destruction wins simultaneous outcome and denies reward")
	var untouched: Dictionary = restored.snapshot()
	for mode in ["missing", "checkpoint_work", "checkpoint_rule"]:
		var bad: Dictionary = restored.snapshot()
		if mode == "missing":
			bad.erase("capture")
		elif mode == "checkpoint_work":
			bad.map_entry.capture[0] = {"side": 1, "work": 600}
		else:
			bad.map_entry.capture_rules = "legacy"
		var input_before := bad.duplicate(true)
		check(not restored.restore(bad) and restored.snapshot() == untouched and bad == input_before, "Capture corruption rejects atomically: " + mode)
	for mode in ["premature_ledger", "primed_base", "overpaid", "fractional_paid"]:
		var bad: Dictionary = restored.snapshot()
		if mode == "premature_ledger":
			bad.settled_maps = [0]
		elif mode == "primed_base":
			bad.base_claim_work = 1199
		elif mode == "overpaid":
			bad.basic_gold_paid = 1000
		else:
			bad.basic_gold_paid = 3
		check(not restored.restore(bad) and restored.snapshot() == untouched, "Invalid reward relation rejected: " + mode)
	var tower = model.new()
	tower.units.clear()
	tower.spawn("shield_guard", 0, 50)
	tower.units[0].hp = 1
	tower.apply_status(tower.units[0], "stun", 0, 1)
	tower.points[1] = -1
	tower.capture[1] = {"side": 1, "work": 1195}
	tower.tower_clock = 2
	tower.begin_round()
	tower.advance_ticks(1)
	check(tower.points[1] == -1, "Tower hit resolves before dead soldier can finish neutralization")

func verify_fixed_clock(model: Script) -> void:
	var reference = model.new()
	check(reference.has_method("advance_ticks"), "P01 missing fixed tick driver")
	if not reference.has_method("advance_ticks"):
		return
	reference.begin_round()
	reference.advance_ticks(300)
	for fps in [30, 60, 144]:
		var run = model.new()
		run.begin_round()
		for frame in range(fps * 10):
			run.advance(1.0 / fps)
		check(run.simulation_tick() == 300, "No fractional tick loss at %d FPS" % fps)
		check(run.snapshot() == reference.snapshot(), "Identical combat at %d FPS" % fps)
	var delayed = model.new()
	delayed.begin_round()
	delayed.advance(10)
	check(delayed.simulation_tick() == 120 and delayed.tick_debt == 180, "Frame work bounded without losing deferred ticks")
	for frame in range(20):
		delayed.advance(0)
	check(delayed.snapshot() == reference.snapshot(), "Long frame debt must not be discarded")
	var partial = model.new()
	partial.begin_round()
	partial.advance(0.01)
	var restored = model.new()
	check(restored.restore(JSON.parse_string(JSON.stringify(partial.snapshot()))), "Fractional accumulator restores")
	partial.advance(0.03)
	restored.advance(0.03)
	check(equivalent_state(partial.snapshot(), restored.snapshot()) and partial.simulation_tick() == 1, "Save retains fractional time")
	var before: Dictionary = partial.snapshot()
	for delta in [NAN, INF, -1.0, 1e308, 1e18]:
		partial.advance(delta)
	check(partial.snapshot() == before, "Invalid delta cannot poison simulation")
	partial.phase = "REFIT"
	before = partial.snapshot()
	partial.advance(30)
	partial.advance_ticks(30)
	check(partial.snapshot() == before, "Refit freezes simulation and debt")
	for field in ["tick", "tick_debt"]:
		var bad: Dictionary = reference.snapshot()
		bad[field] = -1
		check(not partial.restore(bad), "Invalid clock rejected: " + field)
	var timer = model.new()
	timer.begin_round()
	timer.units[0].cooldown = 0.18
	var timer_save: Dictionary = timer.snapshot()
	check(timer_save.get("timer_units") == "ticks" and timer_save.units[0].cooldown == 6, "New save stores duration as integer ceil ticks")
	var timer_load = model.new()
	check(timer_load.restore(JSON.parse_string(JSON.stringify(timer_save))), "Integer duration save restores")
	timer.advance_ticks(5)
	timer_load.advance_ticks(5)
	check(equivalent_state(timer.snapshot(), timer_load.snapshot()), "Quantized duration continues identically after load")
	var legacy: Dictionary = model.new().snapshot()
	legacy.version = 6
	for key in ["ruleset_id", "tick", "tick_debt", "timer_units"]:
		legacy.erase(key)
	legacy.map_entry = {}
	check(timer_load.restore(legacy), "Legacy v6 remains loadable")
	timer_load.begin_round()
	timer_load.advance(0.01)
	check(timer_load.simulation_tick() == 0 and is_equal_approx(timer_load.elapsed, 0.01), "Legacy fractional integration retained")
	timer_load.phase = "VICTORY"
	timer_load.next_map()
	check(timer_load.snapshot().version == 6, "Next map must not upgrade legacy rules")
	var ending = model.new()
	ending.capture_rules = "legacy"
	ending.map_entry = ending.snapshot(false)
	ending.begin_round()
	ending.advance(0.01)
	ending.bases[1] = 0
	ending.advance_ticks(1)
	check(ending.tick_debt == 0 and ending.phase == "VICTORY", "Direct ticks clear battle-exit debt")
	ending.next_map()
	check(model.new().restore(JSON.parse_string(JSON.stringify(ending.snapshot()))), "Mixed drivers produce a restorable next-map checkpoint")
	for version in range(1, 7):
		var old = model.new()
		var fixture: Dictionary = old.snapshot()
		fixture.version = version
		fixture.map_entry = {}
		for key in ["ruleset_id", "tick", "tick_debt", "timer_units"]:
			fixture.erase(key)
		# Hand-authored seconds, not a v7 duration copied and relabelled.
		fixture.units[0].cooldown = 0.18
		check(old.restore(JSON.parse_string(JSON.stringify(fixture))), "Historical seconds fixture v%d" % version)
		old.begin_round()
		old.advance(0.01)
		check(is_equal_approx(old.units[0].cooldown, 0.17), "Legacy timer preserves seconds v%d" % version)
		var original_wave: String = old.wave_rules
		old.phase = "VICTORY"
		old.next_map()
		check(old.wave_rules == original_wave and old.snapshot().version == 6, "Legacy rules survive next map v%d" % version)
	var economy = model.new()
	economy.units.clear()
	economy.begin_round()
	economy.advance_ticks(599)
	check(economy.gold == 120, "Base income not paid before tick600")
	economy.advance_ticks(1)
	check(economy.gold == 125, "Base income paid exactly at tick600")
	var unsupported: Dictionary = reference.snapshot()
	unsupported.ruleset_id = "unknown-future"
	var unchanged: Dictionary = partial.snapshot()
	check(not partial.restore(unsupported) and partial.snapshot() == unchanged, "Unknown ruleset cannot mutate live run")

func verify_statuses(model: Script) -> void:
	var run = model.new()
	check(run.has_method("apply_status"), "Missing shared status behavior")
	if not run.has_method("apply_status"):
		return
	run.units.clear()
	run.spawn("shield_guard", 0, 20)
	var actor: Dictionary = run.units[0]
	run.phase = "BATTLE"
	run.apply_status(actor, "slow", 0.3, 0.2)
	run.apply_status(actor, "slow", 0.15, 1.0)
	check(is_equal_approx(run.movement_factor(actor), 0.7), "Slow takes strongest, not sum")
	run.advance(0.25)
	check(is_equal_approx(run.movement_factor(actor), 0.85), "Weaker slow resumes after stronger expires")
	run.apply_status(actor, "slow", 0.9, 1)
	check(is_equal_approx(run.movement_factor(actor), 0.5), "Movement never falls below half from slows")
	run.apply_status(actor, "barrier", 20, 3)
	run.apply_status(actor, "barrier", 12, 5)
	var hp: float = actor.hp
	run.take_damage(actor, 25)
	check(is_equal_approx(actor.hp, hp - 5), "Barrier absorbs before HP and does not sum")
	run.apply_status(actor, "barrier", 12, 0.1)
	run.advance(0.15)
	hp = actor.hp
	run.take_damage(actor, 5)
	check(is_equal_approx(actor.hp, hp - 5), "Expired barrier cannot absorb")
	actor.windup = 0.18
	actor.pending_target = -2
	run.apply_status(actor, "stun", 0, 0.3)
	check(actor.windup == 0 and actor.pending_target == -1, "Stun cancels unlaunched strike")
	var x: float = actor.x
	run.advance(0.3)
	check(is_equal_approx(actor.x, x), "Stun blocks movement for its duration")
	check(not run.apply_status(actor, "stun", 0, 0.4), "One second immunity blocks chain stun")
	var save: Dictionary = run.snapshot()
	var restored = model.new()
	check(restored.restore(JSON.parse_string(JSON.stringify(save))), "Status survives real JSON roundtrip")
	check(is_equal_approx(restored.movement_factor(restored.units[0]), 0.5), "Restored slow retains strength")
	for bad_effect in [{"stun": -1}, {"immune": NAN}, {"slows": [{"amount": 0.9, "time": 1}]}, {"barrier": 5, "barrier_time": 0}]:
		var bad := save.duplicate(true)
		bad.units[0].effects = bad_effect
		var before: Dictionary = restored.snapshot()
		check(not restored.restore(bad) and restored.snapshot() == before, "Malformed effects rejected before mutation")
	run.phase = "REFIT"
	var frozen: Dictionary = run.snapshot()
	run.advance(1)
	check(run.snapshot() == frozen, "Refit freezes statuses")
	run.phase = "BATTLE"
	run.advance(1)
	check(run.apply_status(actor, "stun", 0, 0.3), "Stun can apply after immunity expires")
	run.phase = "VICTORY"
	run.next_map()
	check(run.units[0].effects.is_empty(), "New map clears temporary combat effects")
	for role in ["shield_guard", "cavalry", "mage"]:
		var duel = model.new()
		duel.units.clear()
		duel.spawn(role, 0, 50)
		duel.spawn("giant", 1, 51)
		duel.units[0].survived = 2
		duel.units[0].charge = 2.0
		for i in range(4 if role == "shield_guard" else 1):
			duel._hit(duel.units[0], duel.units[1])
		check(duel.units[1].effects.get("stun", 0) > 0 if role != "mage" else is_equal_approx(duel.movement_factor(duel.units[1]), 0.85), "Veteran role consumes common control: " + role)
	var healer = model.new()
	healer.units.clear()
	healer.spawn("priest", 0, 20)
	healer.spawn("shield_guard", 0, 21)
	healer.units[0].survived = 5
	for i in range(3):
		healer.units[1].hp = 175
		healer.apply_status(healer.units[1], "slow", 0.3, 1)
		healer.heal_target(healer.units[0], healer.units[1])
	check(healer.movement_factor(healer.units[1]) == 1, "Veteran priest cleanses every third heal")
	check(healer.units[1].effects.get("barrier", 0) == 7, "Elite priest converts only overheal to barrier")
	healer.units[0].heal_count = 2
	healer.apply_status(healer.units[1], "slow", 0.3, 1)
	healer.apply_status(healer.units[1], "slow", 0.15, 2)
	healer.heal_target(healer.units[0], healer.units[1])
	check(is_equal_approx(healer.movement_factor(healer.units[1]), 0.85), "Cleanse removes only strongest single slow")
	var rider = model.new()
	rider.units.clear()
	rider.spawn("cavalry", 0, 20)
	rider.units[0].charge = 1.0
	rider.apply_status(rider.units[0], "stun", 0, 0.3)
	check(rider.units[0].charge == 0, "Stun breaks unfinished consecutive charge")
	var interrupted = model.new()
	interrupted.apply_status(interrupted.units[0], "stun", 0, 0.3)
	var invalid_pending: Dictionary = interrupted.snapshot()
	invalid_pending.units[0].windup = 0.1
	invalid_pending.units[0].pending_target = -2
	check(not interrupted.restore(invalid_pending), "Stunned save cannot resurrect cancelled pending attack")

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
		# Authored transition fixture includes the settlement a real victory performs.
		campaign._settle_map(false)
		var funds = campaign.gold
		check(campaign.next_map(), "Victory opens next map")
		check(campaign.current_map == stage + 1 and campaign.round_number == 1 and campaign.phase == "PREPARE", "Next map begins in preparation")
		check(campaign.gold == funds and campaign.units[0].hp == 77.0 and campaign.reserve == ["archer"] and campaign.buildings.size() == 1, "Campaign preserves economy wounded survivors and supply")
		check(campaign.unlocked_slots() == 7 + stage and campaign.points == [0, 0, 0], "Only actually held old points unlock persistent slots")
		var loaded = model.new()
		check(loaded.restore(JSON.parse_string(JSON.stringify(campaign.snapshot()))) and equivalent_state(loaded.snapshot(), campaign.snapshot()), "Campaign disk continuation")
	campaign.phase = "VICTORY"
	campaign._settle_map(false)
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
		ending.settled_maps = range(map_index)
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
	if "--front-policy-only" in OS.get_cmdline_user_args():
		verify_front_policies(model)
		print("REPLAN_FRONT_POLICY_TEST: %d checks, %d failures" % [checks, failures])
		quit(0 if failures == 0 else 1)
		return
	if "--birth-only" in OS.get_cmdline_user_args():
		verify_birth_records(model)
		print("REPLAN_BIRTH_TEST: %d checks, %d failures" % [checks, failures])
		quit(0 if failures == 0 else 1)
		return
	verify_logistics(model)
	verify_capture(model)
	verify_fixed_clock(model)
	verify_campaign(model)
	verify_front_policies(model)
	verify_statuses(model)
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
	var v3_wave = old_wave.duplicate(true)
	v3_wave.version = 3
	v3_wave.map_pressure = waves.map_pressure
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
	check(omen.confirm_omen("mage") and omen.reserve_roles() == ["shield_guard", "archer", "mage", "mage"], "Confirmation grants base plus selected single bonus")
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

func verify_front_policies(model: Script) -> void:
	# Diagnostic policies, not stand-ins for human choices or a win-rate target.
	# Catch save/restore dropping in-flight front, queue, cooldown or RNG state.
	var folder := "user://front-policy-%d-%d" % [OS.get_process_id(), Time.get_ticks_usec()]
	check(DirAccess.make_dir_recursive_absolute(folder) == OK, "Create isolated policy save folder")
	print("FRONT_POLICY_SAVE_FOLDER: ", ProjectSettings.globalize_path(folder))
	for seed_value in [1947, 1948, 1949]:
		for policy in ["balanced", "north_focus", "ranged", "mixed"]:
			var continuous := front_policy_result(model, policy, seed_value, false)
			var resumed := front_policy_result(model, policy, seed_value, true, folder + "/%s-%d.json" % [policy, seed_value])
			check(not continuous.is_empty() and not resumed.is_empty(), "Policy must finish within first-map time budget")
			check(equivalent_state(continuous, resumed), "Mid-wave JSON resume must preserve policy outcome: %s/%d" % [policy, seed_value])
			if not equivalent_state(continuous, resumed):
				for key in continuous:
					if not equivalent_state(continuous[key], resumed.get(key)):
						print("POLICY_DIFF: ", policy, "/", seed_value, " field=", key)
			if not continuous.is_empty():
				print("THREE_FRONT_POLICY: seed=", seed_value, " policy=", policy, " phase=", continuous.phase, " round=", continuous.round, " base_hp=", continuous.bases[0], " gold=", continuous.gold, " resume_equal=", equivalent_state(continuous, resumed))

func front_policy_result(model: Script, policy: String, seed_value: int, resume_once: bool, save_path: String = "") -> Dictionary:
	var journey = model.new()
	journey.rng.seed = seed_value
	journey.enable_three_fronts()
	var original_pressure: float = journey.map_pressure
	var restored := false
	for second in range(720):
		if journey.phase in ["VICTORY", "DEFEAT"]:
			check(journey.map_pressure == original_pressure and journey.current_map == 0, "Diagnostic must not lower difficulty or advance maps")
			check(not resume_once or restored, "Resumed policy must actually traverse JSON restore")
			var facilities: Array = []
			for building in journey.buildings:
				facilities.append(building.id)
			if policy == "ranged":
				check("range" in facilities, "Ranged policy must actually purchase its specialization")
			if policy == "mixed":
				check("barracks" in facilities and "special_barracks" in facilities, "Mixed policy must actually purchase both troop families")
			return journey.snapshot()
		if journey.phase in ["PREPARE", "REFIT"]:
			if journey.building_count() == 0:
				check(journey.construct("barracks"), "Policy buys normal starting barracks")
			if policy == "mixed" and journey.building_count() == 1:
				journey.construct("special_barracks")
			if policy == "ranged" and journey.buildings[0].id == "barracks":
				journey.upgrade(0, "range")
			if journey.free_spin and journey.spin():
				var options: Array = journey.bonus_options()
				check(journey.confirm_omen(options[0] if not options.is_empty() else ""), "Policy confirms actual rolled recruits")
			check(journey.begin_round(), "Policy advances through real round transition")
		for entry in journey.reserve.duplicate():
			var counts := [0, 0, 0]
			for unit in journey.units:
				if unit.side == 0:
					counts[unit.front] += 1
			journey.selected_front = 0 if policy == "north_focus" else counts.find(counts.min())
			journey.deploy_entry(int(entry.entry_id))
		journey.advance_ticks(30)
		if resume_once and not restored and journey.phase == "BATTLE" and journey.elapsed >= 22.0:
			var storage = load("res://scripts/replan/front_save.gd")
			var written: Dictionary = storage.write_verified(save_path, journey.snapshot())
			check(written.ok, "Natural mid-wave state must reach production disk transport")
			if not written.ok:
				return {}
			var disk: Dictionary = storage.read_verified(save_path)
			var copy = model.new()
			if not disk.ok or not copy.restore(disk.state):
				check(false, "Natural mid-wave save must restore")
				return {}
			journey = copy
			restored = true
	return {}

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
	check(r.reserve_roles().has("archer"), "Barracks automatically produces into reserve")
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
	legacy.version = 1
	legacy.map_entry = {}
	for key in ["ruleset_id", "tick", "tick_debt", "timer_units"]:
		legacy.erase(key)
	for u in legacy.units:
		u.erase("windup")
		u.erase("pending_target")
		# Historical fixtures use seconds; use a literal active cooldown.
		u.cooldown = 0.5
		u.flash = 0.0
		u.action = 0.0
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
