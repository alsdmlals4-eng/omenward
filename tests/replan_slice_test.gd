extends SceneTree

var checks := 0
var failures := 0

func check(ok: bool, message: String) -> void:
	checks += 1
	if not ok:
		failures += 1
		push_error(message)

func _initialize() -> void:
	if not ResourceLoader.exists("res://scripts/replan/front_run.gd"):
		check(false, "Missing approved single-front construction/combat model")
		quit(1)
		return
	var model = load("res://scripts/replan/front_run.gd")
	var r = model.new()
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
	var actual: Dictionary = {}
	for actor in intel.units:
		if actor.side == 1:
			actual[actor.role] = actual.get(actor.role, 0) + 1
	check(actual == forecast.units, "Forecast exactly matches spawned role counts")
	check(intel.wave_forecast().wave == 2 and is_equal_approx(intel.wave_forecast().seconds, 17), "Forecast advances after wave arrival")
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
