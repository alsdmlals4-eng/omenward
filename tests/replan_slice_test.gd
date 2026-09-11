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
	print("REPLAN_SLICE_TEST: %s checks, %s failures" % [checks, failures])
	quit(0 if failures == 0 else 1)
