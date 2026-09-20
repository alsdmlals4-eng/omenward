extends SceneTree

func _initialize() -> void:
	call_deferred("verify")

func verify() -> void:
	var screen = load("res://scenes/replan/front_slice.tscn").instantiate()
	screen.save_path = "user://replan-screen-test-v1.json"
	root.add_child(screen)
	await process_frame
	var failed := false
	if not screen.has_method("unit_draw_anchor"):
		push_error("Missing bounded presentation projection")
		quit(1)
		return
	var before_layout: Dictionary = screen.run.snapshot()
	if not screen.has_method("inspect_front"):
		push_error("Default minimap must open one actual frontline inspection")
		quit(1)
		return
	if screen.run.front_count() != 3 or not screen.overview:
		push_error("Fresh screen must start in three-front overview")
		failed = true
	var before_tick: int = screen.run.tick
	if not screen.forecast_text().contains("북부 1") or not screen.forecast_text().contains("중앙 1") or not screen.forecast_text().contains("남부 1"):
		push_error("Three-front forecast must show where incoming enemies will appear")
		failed = true
	screen.inspect_front(2)
	if not screen.forecast_text().contains("선택 남부"):
		push_error("Forecast composition must follow inspected deployment front")
		failed = true
	if screen.overview or screen.run.selected_front != 2 or screen.run.tick != before_tick:
		push_error("Inspection changes view and deployment front only, not simulation time")
		failed = true
	screen.show_overview()
	if not screen.overview:
		failed = true
	screen.run.restore(before_layout)
	screen.run.restore(screen.Model.new().snapshot())
	if not screen.forecast_text().contains("갑각수 ×2") or screen.forecast_text().contains("선택 남부"):
		push_error("Legacy forecast keeps total composition without invented fronts")
		failed = true
	screen.show_overview()
	if screen.overview:
		push_error("Legacy single-front save must keep all three old capture points visible in inspection")
		failed = true
	screen.run.restore(before_layout)
	screen.show_overview()
	screen.run._enqueue("shield_guard", 1, 0)
	screen.run.construct("barracks")
	screen.run._enqueue("shield_guard", 2, int(screen.run.buildings[0].instance_id))
	screen.tab = "전선"
	screen._refresh_panel()
	var recruit_card = screen.find_child("Deploy_shield_guard", true, false)
	if recruit_card == null or not "T1" in recruit_card.tooltip_text:
		push_error("Reserve card must disclose frozen tier and bind an exact recruit")
		failed = true
	else:
		var first_id: int = screen.run.reserve[0].entry_id
		screen.run.deploy_entry(first_id)
		recruit_card.pressed.emit()
		if screen.run.reserve.size() != 1 or screen.run.reserve[0].birth_tier != 2:
			push_error("Stale recruit card cannot deploy a different recruit of same role")
			failed = true
	screen.run.restore(before_layout)
	screen.run.construct("barracks")
	screen.run.gold = 1000
	screen.run.phase = "REFIT"
	screen.run.upgrade(0, "shield_hall")
	screen.run.spin()
	var token := {"role_id": "shield_guard", "birth_tier": 2, "source_facility_id": 1}
	screen.run.last_board = [token, token.duplicate(), token.duplicate(), "", "", "", "", "", ""]
	screen.tab = "징조륜"
	screen._refresh_panel()
	var tier_label = screen.find_child("OmenTier_0", true, false)
	if tier_label == null or tier_label.text != "T2":
		push_error("Pending omen cell must expose the token tier before committing")
		failed = true
	screen.run.restore(before_layout)
	screen.tab = "내정"
	screen.run.construct("barracks")
	screen.run.gold = 1000
	screen.run.phase = "VICTORY"
	screen.run._settle_map(false)
	screen.run.next_map()
	screen.selected = 0
	screen._refresh_panel()
	var specialization: Button = null
	for candidate in screen.ui.find_children("*", "Button", true, false):
		if candidate.text.begins_with("사격장"):
			specialization = candidate
	if specialization == null or specialization.disabled:
		push_error("Later map preparation must keep specialization card enabled")
		failed = true
	else:
		specialization.pressed.emit()
		if screen.run.buildings[0].id != "range":
			failed = true
		screen._refresh_panel()
		var capstone = screen.find_child("UpgradeTier", true, false)
		if capstone == null or capstone.disabled:
			push_error("Later-map specialized facility must expose affordable T3 purchase")
			failed = true
		else:
			var before_gold: int = screen.run.gold
			capstone.pressed.emit()
			if screen.run.facility_tier(0) != 3 or screen.run.gold != before_gold - 63:
				push_error("T3 button must apply exact purchase once")
				failed = true
	screen.run.restore(before_layout)
	screen._refresh_panel()
	screen.run.construct("logistics")
	screen.selected = 0
	screen._refresh_panel()
	var demolish_button = screen.find_child("DemolishFacility", true, false)
	if demolish_button == null:
		push_error("P03 missing demolition confirmation control")
		failed = true
	else:
		demolish_button.pressed.emit()
		var dialog = screen.find_child("DemolishConfirmation", true, false)
		if dialog == null or not dialog.visible or screen.run.capacity_limit() != 24:
			push_error("Demolition must wait for visible confirmation")
			failed = true
		else:
			dialog.canceled.emit()
			await process_frame
			if screen.run.capacity_limit() != 24:
				failed = true
			demolish_button.pressed.emit()
			dialog = screen.find_child("DemolishConfirmation", true, false)
			var same_state: Dictionary = screen.run.snapshot()
			screen.run.restore(same_state)
			dialog.confirmed.emit()
			await process_frame
			if screen.run.capacity_limit() != 24:
				push_error("Stale demolition must not affect restored same-value building")
				failed = true
			screen.run.restore(same_state)
			screen._refresh_panel()
			screen.find_child("DemolishFacility", true, false).pressed.emit()
			dialog = screen.find_child("DemolishConfirmation", true, false)
			dialog.confirmed.emit()
			await process_frame
			if screen.run.capacity_limit() != 18 or screen.run.building_present(0) or screen.find_child("BuildLogistics", true, false) == null:
				push_error("Confirmed demolition must expose reusable empty slot")
				failed = true
	screen.run.restore(before_layout)
	screen._refresh_panel()
	var logistics = screen.find_child("BuildLogistics", true, false)
	if logistics == null:
		push_error("Logistics needs a build control in domestic tab")
		failed = true
	else:
		logistics.pressed.emit()
		screen._process(0)
		if screen.run.capacity_limit() != 24 or not screen.header.text.contains("/24"):
			push_error("Logistics UI and header must consume same capacity")
			failed = true
		screen.run.units.clear()
		for i in range(9):
			screen.run.spawn("shield_guard", 0, 5)
		screen.run.reserve.append("shield_guard")
		screen.tab = "전선"
		screen._refresh_panel()
		var deployment: Button = null
		for button in screen.ui.find_children("*", "Button", true, false):
			if button.tooltip_text.begins_with("방패병"):
				deployment = button
		if deployment == null or deployment.disabled:
			push_error("Active logistics must enable actual reserve card above18")
			failed = true
		else:
			deployment.pressed.emit()
			if screen.run.capacity_used() != 20:
				failed = true
		screen.run.restore(before_layout)
		screen.tab = "내정"
		screen._refresh_panel()
	var capture_label = screen.find_child("CaptureStatus1", true, false)
	if capture_label == null:
		push_error("Timed capture must expose progress on battlefield")
		failed = true
	else:
		screen.run.capture[1] = {"side": 1, "work": 600}
		screen._process(0)
		if not capture_label.text.contains("50%"):
			push_error("Capture UI must consume actual model progress")
			failed = true
		screen.run.restore(before_layout)
	var base_label = screen.find_child("BaseClaimStatus", true, false)
	if base_label == null:
		push_error("Breached base needs visible claim progress")
		failed = true
	else:
		screen.run.bases[1] = 0
		screen.run.base_claim_work = 600
		screen._process(0)
		if not base_label.text.contains("50%"):
			failed = true
		screen.run.restore(before_layout)
	screen.speed_button.pressed.emit()
	if screen.speed != 2.0:
		push_error("Speed control must select 2x without changing combat constants")
		failed = true
	screen.speed_button.pressed.emit()
	if screen.speed != 1.0:
		failed = true
	screen.tab = "징조륜"
	screen._refresh_panel()
	var observe = screen.find_child("ObserveOmen", true, false)
	if observe == null:
		push_error("Missing player omen transaction controls")
		quit(1)
		return
	observe.pressed.emit()
	if not screen.run.omen_pending or not screen.run.reserve.is_empty():
		failed = true
	screen.find_child("ShiftRow0", true, false).pressed.emit()
	if screen.run.omen_moves != 2:
		failed = true
	screen.find_child("ConfirmOmen", true, false).pressed.emit()
	if screen.run.omen_pending:
		failed = true
	screen.run.restore(before_layout)
	screen.tab = "전선"
	screen._refresh_panel()
	var recovery_button = screen.find_child("OpenRecovery", true, false)
	if recovery_button == null:
		push_error("Missing player recovery entry")
		quit(1)
		return
	screen.run.units[0].hp = 90.0
	screen.run.units[1].hp = 90.0
	recovery_button.pressed.emit()
	var recovery_dialog = screen.find_child("RecoveryDialog", true, false)
	var heal_button = screen.find_child("HealUnit0", true, false)
	if recovery_dialog == null or heal_button == null or not heal_button.text.contains("9G"):
		push_error("Recovery must preview individual cost")
		failed = true
	else:
		heal_button.pressed.emit()
		if screen.run.gold != 111 or screen.run.units[0].hp != 180 or not heal_button.disabled:
			push_error("Recovery UI must charge model once and disable healed target")
			failed = true
		var second = screen.find_child("HealUnit1", true, false)
		second.pressed.emit()
		if screen.run.gold != 102 or screen.run.units[1].hp != 180:
			push_error("Each recovery button must bind its own unit")
			failed = true
		recovery_dialog.queue_free()
		await process_frame
	screen.run.restore(before_layout)
	if not screen.has_method("_get_tooltip"):
		push_error("Missing crowd inspection")
		quit(1)
		return
	screen.run.units.clear()
	screen.run.spawn("archer", 0, 50)
	screen.run.spawn("mage", 1, 50)
	screen.inspect_front(0)
	var inspect_at: Vector2 = screen.unit_draw_anchor(screen.run.units[0])
	screen.run.apply_status(screen.run.units[0], "barrier", 12, 3)
	screen.run.apply_status(screen.run.units[0], "slow", 0.3, 1)
	screen.run.apply_status(screen.run.units[0], "stun", 0, 0.3)
	var status_info: String = screen._get_tooltip(inspect_at)
	if not status_info.contains("보호막12") or not status_info.contains("둔화30%") or not status_info.contains("경직"):
		push_error("Unit hover must expose actual active statuses")
		failed = true
	var info: String = screen._get_tooltip(inspect_at)
	if not info.contains("아군") or not info.contains("궁병") or not info.contains("체력"):
		push_error("Crowd inspection must identify actual faction, role and health")
		quit(1)
		return
	if screen._get_tooltip(Vector2(10, 500)) != "":
		failed = true
	var inspect_before: Dictionary = screen.run.snapshot()
	for side in range(2):
		for i in range(12):
			screen.run.spawn("priest", side, 50)
	var crowded: Dictionary = screen.run.snapshot()
	var crowd_info: String = screen._get_tooltip(inspect_at)
	if not crowd_info.contains("더 있음") or crowd_info.split("\n").size() > 7:
		push_error("Dense inspection must bound tooltip length and disclose overflow")
		failed = true
	if crowded != screen.run.snapshot():
		failed = true
	screen.run.restore(inspect_before)
	screen.run.units[0].hp = 0
	if screen._get_tooltip(inspect_at).contains("궁병"):
		push_error("Dead actors must not appear in live inspection")
		failed = true
	screen.run.restore(before_layout)
	var anchors: Array = []
	for id in range(8):
		var anchor: Vector2 = screen.unit_draw_anchor({"id": id, "side": 0, "x": 50.0})
		if anchors.has(anchor) or absf(anchor.x - 640.0) > 24 or anchor.y < 260 or anchor.y > 360:
			push_error("Crowded units need distinct bounded display anchors")
			failed = true
		anchors.append(anchor)
	if before_layout != screen.run.snapshot():
		push_error("Presentation must not mutate combat or save state")
		failed = true
	var control = screen.Model.new()
	control.enable_three_fronts()
	screen.run.begin_round()
	control.begin_round()
	for step in range(230):
		screen.run.advance(0.1)
		for actor in screen.run.units:
			screen.unit_draw_anchor(actor)
		control.advance(0.1)
	if screen.run.snapshot() != control.snapshot():
		push_error("Display projection changed deterministic battle outcome")
		failed = true
	screen.run.restore(before_layout)
	for role in screen.run.definitions:
		var ward: AtlasTexture = screen.art.unit(role, 0)
		if ward == null or ward.atlas.get_image().detect_alpha() == Image.ALPHA_NONE:
			push_error("Ward role must use transparent atlas: " + role)
			failed = true
	for building_id in screen.art.BUILDINGS:
		var facility: AtlasTexture = screen.art.building(building_id)
		if facility == null or facility.atlas.get_image().detect_alpha() == Image.ALPHA_NONE:
			push_error("Facility must use transparent atlas: " + building_id)
			failed = true
	for role in screen.run.definitions:
		var veil: AtlasTexture = screen.art.unit(role, 1)
		var veil_image := veil.atlas.get_image()
		if veil_image.detect_alpha() == Image.ALPHA_NONE:
			push_error("Veil role still uses opaque atlas: " + role)
			failed = true
	var idle: AtlasTexture = screen.art.unit("shield_guard", 0)
	var source := idle.atlas.get_image()
	if source.detect_alpha() == Image.ALPHA_NONE or source.get_pixel(0, 0).a != 0:
		push_error("Shield idle must use genuine transparent pixels")
		failed = true
	if idle.region != Rect2(0, 0, 768, 768):
		push_error("Shield must use the aligned motion atlas")
		failed = true
	if not screen.art.has_method("motion_frame"):
		push_error("Missing combat-state motion selection")
		quit(1)
		return
	for sample in [[0.0, 0.0, 0], [0.1, 0.0, 1], [0.0, 0.25, 2], [0.0, 0.1, 3]]:
		var unit := {"side": 0, "role": "shield_guard", "windup": sample[0], "action": sample[1]}
		var frame: int = screen.art.motion_frame(unit)
		var pose: AtlasTexture = screen.art.unit("shield_guard", 0, frame)
		if frame != sample[2] or pose.region != Rect2(sample[2] * 768, 0, 768, 768):
			push_error("Combat state selected wrong shield pose")
			failed = true
	var motion = JSON.parse_string(FileAccess.get_file_as_string(screen.art.ROOT + "ward-shield-motion.json"))
	if not is_equal_approx(motion.frames[1].duration / 1000.0, screen.run.SHIELD_WINDUP) or not is_equal_approx(motion.frames[2].duration / 1000.0, screen.run.SHIELD_IMPACT) or not is_equal_approx(motion.frames[3].duration / 1000.0, screen.run.SHIELD_RECOVERY):
		push_error("Aseprite timing differs from actual combat timing")
		failed = true
	if not screen.has_method("phase_label"):
		push_error("Missing localized battle phase presentation")
		quit(1)
		return
	if screen.phase_label() != "출정 준비":
		failed = true
	if not screen.has_method("forecast_text"):
		push_error("Missing visible wave forecast")
		quit(1)
		return
	if not screen.forecast_text().contains("갑각수 ×1") or not screen.forecast_text().contains("5초"):
		push_error("Forecast must name actual Veil composition and arrival")
		failed = true
	for button in screen.find_children("*", "Button", true, false):
		if button.text == "전선":
			button.pressed.emit()
			if not button.button_pressed or screen.tab != "전선":
				failed = true
	screen.tab = "내정"
	screen._refresh_panel()
	screen.paused = true
	screen._process(0.0)
	if screen.pause_button.text != "계속 진행":
		failed = true
	screen.paused = false
	for node in screen.find_children("*", "TextureRect", true, false):
		if node.size.x > 130 or node.size.y > 130:
			push_error("Atlas picture exceeds its UI allocation: %s" % node.size)
			failed = true
	var found := false
	for button in screen.find_children("*", "Button", true, false):
		if button.text.begins_with("일반 병영"):
			button.pressed.emit()
			found = true
			break
	if not found or screen.run.buildings.size() != 1 or screen.run.gold != 80:
		failed = true
		push_error("Build button does not consume the real model")
	screen._process(0.0)
	var production = screen.find_child("ProductionStatus", true, false)
	if production == null or not production.text.contains("동결"):
		push_error("Production must explain preparation freeze")
		failed = true
	screen._save()
	screen.run.gold = 1
	screen._load_save()
	if screen.run.gold != 80:
		failed = true
		push_error("Save/load button path loses gold")
	screen.run.gold = 60
	screen._save()
	var damaged := FileAccess.open(screen.save_path, FileAccess.WRITE)
	damaged.store_string("{broken")
	damaged.close()
	screen.run.gold = 1
	screen._load_save()
	if screen.run.gold != 80 or not screen.run.message.contains("이전 정상"):
		failed = true
		push_error("UI must recover previous valid save and disclose rollback")
	if FileAccess.get_file_as_string(screen.save_path) != "{broken":
		failed = true
		push_error("Loading backup must preserve corrupt primary evidence")
	screen._save()
	if not screen.run.message.begins_with("저장 완료"):
		failed = true
		push_error("Recovered player must be able to save continued run")
	screen.run.phase = "BATTLE"
	screen.paused = true
	screen._process(1.0)
	production = screen.find_child("ProductionStatus", true, false)
	if not production.text.contains("일시정지") or not is_zero_approx(screen.run.buildings[0].clock):
		failed = true
		push_error("Paused production must stop both countdown and status")
	screen.run.phase = "VICTORY"
	screen.run._settle_map(false)
	screen._process(0.0)
	if not production.text.contains("생산 종료"):
		failed = true
		push_error("Completed battle must show production ended")
	screen.paused = false
	screen.run.gold = 1000
	screen.run.phase = "REFIT"
	screen.run.points = [1, 0, 0]
	while screen.run.buildings.size() < 7:
		screen.run.construct("barracks")
	screen.selected = 6
	screen.run.points = [0, 0, 0]
	screen._refresh_panel()
	await process_frame
	screen._process(0.0)
	production = screen.find_child("ProductionStatus", true, false)
	if production == null or not production.text.contains("슬롯 잠김"):
		failed = true
		push_error("Lost territory must explain selected building lock")
	screen.paused = true
	screen._process(0.0)
	if not production.text.contains("생산 중단") or production.text.contains("정지단"):
		failed = true
		push_error("Paused locked facility must preserve its lock reason")
	for button in screen.find_children("*", "Button", true, false):
		if button.tooltip_text.begins_with("T2:") and not button.disabled:
			failed = true
			push_error("Locked building must not offer enabled specialization")
	screen.run = screen.Model.new()
	screen.run.phase = "VICTORY"
	screen.run._settle_map(false)
	screen._process(0.0)
	if screen.start_button.disabled or screen.start_button.text != "다음 맵 준비":
		failed = true
	screen.start_button.pressed.emit()
	screen._process(0.0)
	if screen.run.current_map != 1 or not screen.map_labels[1].text.begins_with("◆") or not screen.map_labels[0].text.begins_with("✓"):
		push_error("Campaign button must advance and update map ribbon")
		failed = true
	screen.tab = "내정"
	screen.building_page = 1
	screen._refresh_panel()
	var tenth_slot := false
	for button in screen.find_children("*", "Button", true, false):
		if button.text.begins_with("10 "):
			tenth_slot = true
	if not tenth_slot:
		push_error("Second building page must expose slots beyond nine")
		failed = true
	screen.run.phase = "DEFEAT"
	screen._process(0.0)
	if screen.start_button.disabled or screen.start_button.text != "맵 진입부터 재도전":
		failed = true
	screen.start_button.pressed.emit()
	if screen.run.phase != "PREPARE" or screen.run.current_map != 1:
		push_error("Retry button must restore current map entry")
		failed = true
	print("REPLAN_SCREEN_TEST: ", "FAIL" if failed else "PASS")
	# User deletes disposable files manually; leave this deterministic test save for collection.
	screen.queue_free()
	await process_frame
	quit(1 if failed else 0)
