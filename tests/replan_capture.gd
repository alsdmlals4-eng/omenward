extends SceneTree
## Natural battle first; explicitly labeled mixed-role stress fixture second.

func save_review_frame(screen: Control, filename: String) -> void:
	screen._refresh_panel()
	screen._process(0.0)
	screen.queue_redraw()
	await process_frame
	await RenderingServer.frame_post_draw
	var error := root.get_texture().get_image().save_png("res://output/" + filename)
	assert(error == OK, "Capture must be written, not only claimed")

func deploy_review_reserves(screen: Control) -> void:
	screen.tab_buttons["전선"].pressed.emit()
	for entry in screen.run.reserve.duplicate():
		var counts := [0, 0, 0]
		for unit in screen.run.units:
			if unit.side == 0:
				counts[unit.front] += 1
		screen.front_buttons[counts.find(counts.min())].pressed.emit()
		var button = screen.find_child("Deploy_" + screen.run.entry_role(entry), true, false)
		if button != null and not button.disabled:
			button.pressed.emit()

func capture_first_map(screen: Control) -> void:
	# A deterministic real-resource policy, not human play or balance approval.
	# Pause wall time; advance the real fixed clock only. Never grant gold/units/HP.
	for button in screen.ui.find_children("*", "Button", true, false):
		if button.text.begins_with("일반 병영"):
			button.pressed.emit()
			break
	assert(screen.run.building_count() == 1 and screen.run.gold == 80)
	screen.tab_buttons["징조륜"].pressed.emit()
	screen.find_child("ObserveOmen", true, false).pressed.emit()
	assert(screen.run.omen_pending)
	await save_review_frame(screen, "front-first-map-prepare.png")
	screen.find_child("ConfirmOmen", true, false).pressed.emit()
	assert(not screen.run.omen_pending)
	deploy_review_reserves(screen)
	screen.start_button.pressed.emit()
	assert(screen.run.phase == "BATTLE")
	var refits := 0
	var saw_battle := false
	for second in range(720):
		if screen.run.phase in ["VICTORY", "DEFEAT"]:
			break
		deploy_review_reserves(screen)
		screen.run.advance_ticks(30)
		if not saw_battle and screen.run.elapsed >= 30.0:
			screen.show_overview()
			await save_review_frame(screen, "front-overview.png")
			var before: Dictionary = screen.run.snapshot()
			var click := InputEventMouseButton.new()
			click.position = Vector2(465, 292)
			click.button_index = MOUSE_BUTTON_LEFT
			click.pressed = true
			root.push_input(click, true)
			click = click.duplicate()
			click.pressed = false
			root.push_input(click, true)
			await save_review_frame(screen, "front-inspection.png")
			before.selected_front = 1
			assert(not screen.overview and screen.run.snapshot() == before)
			screen.overview_button.pressed.emit()
			saw_battle = true
		if screen.run.phase == "REFIT":
			refits += 1
			screen.show_overview()
			if refits == 1:
				await save_review_frame(screen, "front-first-map-refit.png")
			screen.tab_buttons["징조륜"].pressed.emit()
			var observe = screen.find_child("ObserveOmen", true, false)
			if not observe.disabled:
				observe.pressed.emit()
				var confirm = screen.find_child("ConfirmOmen", true, false)
				assert(not confirm.disabled, "Single barracks should not need ambiguous bonus selection")
				confirm.pressed.emit()
			deploy_review_reserves(screen)
			screen.start_button.pressed.emit()
		await process_frame
	assert(saw_battle and refits > 0 and screen.run.phase in ["VICTORY", "DEFEAT"])
	screen.show_overview()
	await save_review_frame(screen, "front-first-map-result.png")
	print("FIRST_MAP_UI_REVIEW: fronts=", screen.run.front_count(), " phase=", screen.run.phase, " round=", screen.run.round_number, " refits=", refits, " gold=", screen.run.gold, " base_hp=", screen.run.bases[0], "; real starting resources, accelerated fixed clock; HUMAN_NOT_RUN")
	screen.queue_free()
	await process_frame
	quit()

func _initialize() -> void:
	call_deferred("capture")

func capture() -> void:
	root.gui_embed_subwindows = true
	var screen = load("res://scenes/replan/front_slice.tscn").instantiate()
	screen.save_path = "user://replan-capture-%d.json" % OS.get_process_id()
	root.add_child(screen)
	screen.paused = true
	if "--first-map-only" in OS.get_cmdline_user_args():
		await capture_first_map(screen)
		return
	if "--three-front-only" in OS.get_cmdline_user_args():
		screen.run.begin_round()
		screen.run.advance_ticks(900)
		screen._refresh_panel()
		await process_frame
		await RenderingServer.frame_post_draw
		root.get_texture().get_image().save_png("res://output/front-overview.png")
		var before_view: Dictionary = screen.run.snapshot()
		var click := InputEventMouseButton.new()
		click.position = Vector2(465, 292)
		click.button_index = MOUSE_BUTTON_LEFT
		click.pressed = true
		root.push_input(click, true)
		var release := click.duplicate()
		release.pressed = false
		root.push_input(release, true)
		await process_frame
		await RenderingServer.frame_post_draw
		root.get_texture().get_image().save_png("res://output/front-inspection.png")
		before_view.selected_front = 1
		if screen.overview or screen.run.snapshot() != before_view:
			push_error("Inspection must preserve concurrent gameplay state")
			quit(1)
			return
		screen.get_node("OverviewButton").pressed.emit()
		if not screen.overview:
			quit(1)
			return
		print("THREE_FRONT_GPU: overview -> center inspection -> overview; view switch preserved simulation")
		quit()
		return
	screen.inspect_front(0)
	screen.run.construct("barracks")
	screen._refresh_panel()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-building.png")
	var before_demolition: Dictionary = screen.run.snapshot()
	screen._request_demolish()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-demolition.png")
	var demolition_dialog = screen.get_node("DemolishConfirmation")
	demolition_dialog.canceled.emit()
	await process_frame
	if screen.run.snapshot() != before_demolition:
		push_error("Demolition preview/cancel changed gameplay state")
		quit(1)
		return
	print("DEMOLITION_RUNTIME: confirmation captured, cancel preserved state")
	# Explicit late-round setup fixture, not evidence of natural round6 progression.
	screen.run.gold = 1000
	screen.run.phase = "REFIT"
	screen.run.round_number = 5
	screen.run.upgrade(0, "range")
	if not screen.run.upgrade_tier(0):
		push_error("T3 fixture purchase failed")
		quit(1)
		return
	screen.run.begin_round()
	screen.run.buildings[0].clock = 99
	screen.run.advance_ticks(1)
	var born_tier: int = screen.run.reserve[0].birth_tier
	screen.run.deploy_entry(int(screen.run.reserve[0].entry_id))
	screen._refresh_panel()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-tier3.png")
	if born_tier != 3 or screen.run.units.back().birth_tier != 3:
		push_error("T3 fixture did not retain birth on deployment")
		quit(1)
		return
	print("T3_RUNTIME: purchase + production + exact deployment tier3, fixture not natural progression")
	if not screen.run.restore(before_demolition):
		quit(1)
		return
	screen.run.spin()
	screen.tab = "징조륜"
	screen._refresh_panel()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-omen.png")
	screen.run.confirm_omen()
	while screen.run.reserve_roles().has("shield_guard"):
		if not screen.run.deploy("shield_guard"):
			break
	screen.run.begin_round()
	var captured: Dictionary = {}
	for i in range(600):
		screen.run.advance(0.1)
		for actor in screen.run.units:
			if actor.side != 0 or actor.role != "shield_guard":
				continue
			var pose: int = screen.art.motion_frame(actor)
			if pose > 0 and not captured.has(pose):
				screen.queue_redraw()
				await process_frame
				await RenderingServer.frame_post_draw
				root.get_texture().get_image().save_png("res://output/front-shield-%s.png" % ["idle", "windup", "impact", "recover"][pose])
				captured[pose] = true
		if captured.size() == 3:
			break
	screen.tab = "전선"
	screen._refresh_panel()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-battle.png")
	root.size = Vector2i(1920, 1080)
	await process_frame
	await RenderingServer.frame_post_draw
	var hd := root.get_texture().get_image()
	hd.save_png("res://output/front-battle-1080.png")
	if hd.get_size() != Vector2i(1920, 1080):
		push_error("Full HD capture has wrong dimensions")
		quit(1)
		return
	print("REPLAN_RENDER: damage_events=", screen.run.damage_events, " units=", screen.run.units.size())
	print("SHIELD_RUNTIME_POSES: ", captured.size(), "/3")
	root.size = Vector2i(1280, 720)
	screen.run = screen.Model.new()
	screen.run.units.clear()
	for side in range(2):
		for role in ["shield_guard", "archer", "mage", "priest", "spear_guard"]:
			screen.run.spawn(role, side, 46.0 if side == 0 else 54.0)
	screen.run.begin_round()
	screen.run.advance(0.6)
	screen.run.message = "혼합 병종 검증 편성 · 일반 획득 흐름 아님 · 병사 위에 마우스로 정보 확인"
	screen._refresh_panel()
	screen.queue_redraw()
	await process_frame
	var hover := InputEventMouseMotion.new()
	hover.position = screen.unit_draw_anchor(screen.run.units[1])
	hover.global_position = hover.position
	root.push_input(hover)
	await create_timer(0.8).timeout
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-mixed.png")
	root.size = Vector2i(1920, 1080)
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-mixed-1080.png")
	print("MIXED_FIXTURE: units=", screen.run.units.size(), " damage_events=", screen.run.damage_events)
	# Recovery dialog boundary fixture, not evidence this army survived a full round.
	root.size = Vector2i(1280, 720)
	screen.run.phase = "REFIT"
	screen.run.message = "치료 UI 경계 검증 · 혼합 편성의 부상 상태 사용"
	screen._refresh_panel()
	screen._show_recovery()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-recovery.png")
	screen.queue_free()
	await process_frame
	var campaign_screen = load("res://scenes/replan/front_slice.tscn").instantiate()
	root.add_child(campaign_screen)
	await process_frame
	campaign_screen.paused = true
	campaign_screen.run.points = [1, 0, 0]
	campaign_screen.run.phase = "VICTORY"
	campaign_screen.run._settle_map(false)
	campaign_screen.start_button.pressed.emit()
	campaign_screen.paused = true
	campaign_screen.run.message = "맵 전환 경계 검증 · 실제 전체 맵 승리 기록 아님 · 배경 공통 임시 사용"
	campaign_screen._process(0.0)
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-campaign.png")
	campaign_screen.queue_free()
	await process_frame
	var status_screen = load("res://scenes/replan/front_slice.tscn").instantiate()
	root.add_child(status_screen)
	await process_frame
	status_screen.paused = true
	status_screen.run.units.clear()
	status_screen.run.spawn("mage", 0, 45)
	status_screen.run.spawn("priest", 0, 44)
	status_screen.run.spawn("shield_guard", 0, 47)
	status_screen.run.spawn("giant", 1, 50)
	status_screen.run.units[0].survived = 2
	status_screen.run.units[1].survived = 5
	status_screen.run.units[2].survived = 2
	status_screen.run.units[2].hit_count = 3
	status_screen.run.units[2].hp = 175
	# Observe the shield before the giant consumes it; fixture timing only.
	status_screen.run.units[3].cooldown = 2.0
	status_screen.run.begin_round()
	status_screen.run.advance(0.25)
	var guard: Dictionary = status_screen.run.units[2]
	var giant: Dictionary = status_screen.run.units[3]
	var controlled: bool = float(giant.effects.get("stun", 0)) > 0 and is_equal_approx(status_screen.run.movement_factor(giant), 0.85) and float(guard.effects.get("barrier", 0)) == 7
	status_screen.run.message = "효과 시험 편성 · 거인 둔화15%/경직 · 방패병 보호막7 · 일반 성장 획득 증거 아님"
	status_screen._refresh_panel()
	status_screen.queue_redraw()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-status.png")
	print("STATUS_RUNTIME: ", controlled, " barrier=", guard.effects.get("barrier", 0), " stun=", giant.effects.get("stun", 0), " move=", status_screen.run.movement_factor(giant))
	status_screen.queue_free()
	await process_frame
	quit(0 if captured.size() == 3 and controlled else 1)
