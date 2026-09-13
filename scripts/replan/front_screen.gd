extends Control
## Presentation and input only; FrontRun owns all game rules.
const Model := preload("res://scripts/replan/front_run.gd")
const Art := preload("res://scripts/replan/front_art.gd")
@export var save_path := "user://replan-front-v1.json"
var run = Model.new()
var art = Art.new()
var tab := "내정"
var speed := 1.0
var paused := false
var ui: Control
var header: Label
var notice: Label
var start_button: Button
var pause_button: Button
var speed_button: Button
var tab_buttons: Dictionary = {}
var detail: Label
var panel_key := ""
var selected := 0
var font := SystemFont.new()
var backdrop: Texture2D
var refresh_clock := 0.0
var forecast_label: Label
var production_label: Label
var production_bar: ProgressBar
var selected_bonus := ""
var map_labels: Array = []
var building_page := 0

func _ready() -> void:
	get_window().content_scale_size = Vector2i(1280, 720)
	get_window().content_scale_mode = Window.CONTENT_SCALE_MODE_CANVAS_ITEMS
	get_window().content_scale_stretch = Window.CONTENT_SCALE_STRETCH_FRACTIONAL
	get_window().size = Vector2i(1280, 720)
	font.font_names = PackedStringArray(["Malgun Gothic", "Noto Sans CJK KR"])
	theme = Theme.new()
	theme.default_font = font
	theme.default_font_size = 16
	backdrop = load(Art.ROOT + "battlefield-layer.png")
	_make_shell()
	_refresh_panel()

func _label(text: String, rect: Rect2, parent: Node = self, size_px: int = 16) -> Label:
	var label := Label.new()
	label.text = text
	label.position = rect.position
	label.size = rect.size
	label.add_theme_font_size_override("font_size", size_px)
	parent.add_child(label)
	return label

func _button(text: String, rect: Rect2, action: Callable, parent: Node = self) -> Button:
	var button := Button.new()
	button.text = text
	button.position = rect.position
	button.size = rect.size
	button.pressed.connect(action)
	parent.add_child(button)
	return button

func _make_shell() -> void:
	_label("OMENWARD  /  전선 실전 검토판", Rect2(22, 5, 600, 35), self, 22)
	header = _label("", Rect2(24, 73, 1050, 30))
	notice = _label("", Rect2(24, 430, 1230, 30))
	var forecast_panel := Panel.new()
	forecast_panel.position = Vector2(26, 120)
	forecast_panel.size = Vector2(1228, 51)
	forecast_panel.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(forecast_panel)
	forecast_label = _label("", Rect2(12, 4, 1204, 44), forecast_panel, 15)
	for i in range(5):
		var map: Dictionary = run.catalog.maps[i]
		var label := _label(("◆ " if i == 0 else "◇ ") + map.name, Rect2(25 + i * 250, 40, 240, 28))
		label.modulate = Color("f6d687") if i == 0 else Color("8796ad")
		map_labels.append(label)
	start_button = _button("공세 시작", Rect2(1070, 76, 185, 34), func():
		if run.phase == "DEFEAT":
			run.retry_map()
			selected = 0
			paused = false
		elif run.phase == "VICTORY":
			run.next_map()
			paused = false
		else:
			run.begin_round()
		_refresh_panel())
	for i in range(3):
		var title: String = ["내정", "징조륜", "전선"][i]
		var tab_button := _button(title, Rect2(24 + i * 130, 473, 122, 36), func(): tab = title; _refresh_panel())
		tab_button.toggle_mode = true
		tab_buttons[title] = tab_button
	pause_button = _button("일시정지", Rect2(445, 473, 116, 36), func(): paused = not paused)
	speed_button = _button("속도 1×", Rect2(569, 473, 150, 36), func(): speed = 3.0 if speed == 1.0 else 1.0)
	_button("저장", Rect2(800, 473, 95, 36), _save)
	_button("불러오기", Rect2(903, 473, 115, 36), _load_save)
	_button("새 출정", Rect2(1026, 473, 112, 36), _restart)
	_button("기존 빌드", Rect2(1146, 473, 110, 36), func(): get_tree().change_scene_to_file("res://scenes/main/main.tscn"))
	ui = Control.new()
	ui.position = Vector2(24, 519)
	ui.size = Vector2(1232, 170)
	add_child(ui)
	_label("투명 후보: 베일 10종 · 방패병 베기 4자세/Aseprite 연결 | 나머지 공격 모션·T3·영웅·등급 스킬 미연결", Rect2(24, 691, 1240, 25), self, 13)

func _restart() -> void:
	# Explicit confirmation prevents accidental loss of a running battle.
	var dialog := ConfirmationDialog.new()
	dialog.dialog_text = "현재 출정을 끝내고 새로 시작할까요? 저장 파일은 유지됩니다."
	add_child(dialog)
	dialog.confirmed.connect(func(): run = Model.new(); selected = 0; paused = false; _refresh_panel(); dialog.queue_free())
	dialog.canceled.connect(dialog.queue_free)
	dialog.popup_centered()

func _picture(texture: Texture2D, rect: Rect2, parent: Node) -> void:
	var picture := TextureRect.new()
	picture.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	picture.texture = texture
	picture.position = rect.position
	picture.size = rect.size
	picture.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	picture.mouse_filter = Control.MOUSE_FILTER_IGNORE
	parent.add_child(picture)

func _refresh_panel() -> void:
	production_label = null
	production_bar = null
	for title in tab_buttons:
		tab_buttons[title].set_pressed_no_signal(title == tab)
	for child in ui.get_children():
		ui.remove_child(child)
		child.queue_free()
	if tab == "내정":
		_build_panel()
	elif tab == "징조륜":
		_omen_panel()
	else:
		_reserve_panel()
	panel_key = _state_key()

func _state_key() -> String:
	return "%s:%s:%s:%s:%s:%s" % [run.phase, run.gold, run.reserve, run.buildings.size(), run.points, run.capacity_used()]

func _build_panel() -> void:
	_label("건물 %s/%s칸 · 위에서부터 해금 / 잠기면 생산 중단" % [run.buildings.size(), run.unlocked_slots()], Rect2(0, 0, 600, 26), ui)
	var pages := ceili((6 + (run.current_map + 1) * 3) / 9.0)
	building_page = mini(building_page, pages - 1)
	if pages > 1:
		_button("슬롯 %d/%d ▸" % [building_page + 1, pages], Rect2(425, 0, 135, 26), func(): building_page = (building_page + 1) % pages; _refresh_panel(), ui)
	for local_slot in range(9):
		var i := local_slot + building_page * 9
		if i >= 6 + (run.current_map + 1) * 3:
			break
		var y := 29 + (local_slot % 3) * 43
		var x := (local_slot / 3) * 185
		var text := "%d 잠김" % (i + 1)
		if i < run.buildings.size():
			var building: Dictionary = run.buildings[i]
			text = "%d %s" % [i + 1, run.facilities[building.id][1]]
		elif i < run.unlocked_slots():
			text = "%d 빈 슬롯" % (i + 1)
		var b := _button(text, Rect2(x, y, 177, 38), func(): selected = i; _refresh_panel(), ui)
		b.add_theme_font_size_override("font_size", 13)
		b.modulate = Color("f7d27d") if selected == i else Color.WHITE
		b.disabled = i >= run.unlocked_slots()
		b.tooltip_text = "점령지 확보 시 위에서부터 해금됩니다. 잠긴 건물은 보존되지만 생산을 멈춥니다." if b.disabled else "선택한 시설의 공급 병종과 생산 상태를 확인합니다."
	if selected < run.buildings.size():
		var b: Dictionary = run.buildings[selected]
		_picture(art.building(b.id), Rect2(570, 8, 130, 130), ui)
		_label("%s → %s\n자동 생산 %s초 / 대기열로 공급" % [run.facilities[b.id][1], run.definitions[b.unit][1], run.facilities[b.id][5]], Rect2(714, 0, 510, 48), ui)
		production_bar = ProgressBar.new()
		production_bar.position = Vector2(570, 143)
		production_bar.size = Vector2(130, 12)
		production_bar.show_percentage = false
		production_bar.mouse_filter = Control.MOUSE_FILTER_IGNORE
		ui.add_child(production_bar)
		production_label = _label("", Rect2(714, 132, 510, 30), ui, 13)
		production_label.name = "ProductionStatus"
		var options: Array = []
		for id in run.branches:
			if run.branches[id][1] == b.id:
				options.append(id)
		for j in range(options.size()):
			var id: String = options[j]
			var button := _button("%s %sG" % [run.facilities[id][1], run.facilities[id][2]], Rect2(714 + (j % 3) * 170, 54 + (j / 3) * 39, 164, 35), func(): run.upgrade(selected, id); _refresh_panel(), ui)
			button.add_theme_font_size_override("font_size", 13)
			button.disabled = run.omen_pending or not run.building_active(selected) or run.phase not in ["PREPARE", "REFIT"] or (run.round_number < 2 and run.phase != "REFIT") or run.gold < int(run.facilities[id][2])
			button.tooltip_text = "T2: 1라운드 재정비부터 / 활성 슬롯에서만 가능 / 전문화 시 생산 시간 초기화"
	else:
		_picture(art.building("barracks"), Rect2(578, 12, 125, 125), ui)
		_label("T1부터 건설 → T2에서 같은 계열 전문화", Rect2(714, 0, 510, 28), ui)
		var normal := _button("일반 병영 · 방패병 · 40G", Rect2(714, 39, 490, 43), func(): run.construct("barracks"); _refresh_panel(), ui)
		var special := _button("특수 병영 · 특수병 1종 고정 추첨 · 75G", Rect2(714, 90, 490, 43), func(): run.construct("special_barracks"); _refresh_panel(), ui)
		normal.disabled = run.omen_pending or run.phase not in ["PREPARE", "REFIT"] or run.gold < 40 or run.buildings.size() >= run.unlocked_slots()
		special.disabled = run.omen_pending or run.phase not in ["PREPARE", "REFIT"] or run.gold < 75 or run.buildings.size() >= run.unlocked_slots()
		_label("건설은 첫 빈 슬롯에 배치됩니다. 특수 병영 추첨은 저장됩니다.", Rect2(714, 137, 510, 25), ui, 13)

func _omen_panel() -> void:
	for i in range(9):
		var rect := Rect2((i % 3) * 55, (i / 3) * 55, 50, 50)
		if i < run.last_board.size() and run.last_board[i] != "":
			_picture(art.unit(run.last_board[i], 0), rect, ui)
		else:
			_label("—", rect, ui)
	var b := _button("관측 · %s" % ("무료" if run.free_spin else "20G"), Rect2(290, 0, 195, 38), func(): run.spin(); selected_bonus = ""; _refresh_panel(), ui)
	b.name = "ObserveOmen"
	b.disabled = not run.can_spin()
	b.tooltip_text = "미확정 결과를 먼저 확정하세요." if run.omen_pending else "준비/재정비 전용. 최대 지급 %d칸의 대기 공간과 회전 비용이 필요합니다." % run.spin_required_capacity()
	for i in range(3):
		var row := _button("%d행 →" % (i + 1), Rect2(172, i * 53, 103, 32), func(): run.shift_board("row", i); selected_bonus = ""; _refresh_panel(), ui)
		row.name = "ShiftRow%d" % i
		row.disabled = not run.omen_pending or run.omen_moves == 0
		var column := _button("%d열 ↓" % (i + 1), Rect2(290 + i * 95, 43, 88, 32), func(): run.shift_board("column", i); selected_bonus = ""; _refresh_panel(), ui)
		column.disabled = row.disabled
	var options: Array = run.bonus_options()
	if not options.has(selected_bonus):
		selected_bonus = ""
	var choose := OptionButton.new()
	choose.position = Vector2(592, 0)
	choose.size = Vector2(280, 38)
	choose.add_item("완성선 보너스 병종 선택")
	for role in options:
		choose.add_item(run.definitions[role][1])
	if options.has(selected_bonus):
		choose.select(options.find(selected_bonus) + 1)
	choose.disabled = not run.omen_pending or options.size() < 2
	choose.item_selected.connect(func(index): selected_bonus = options[index - 1] if index > 0 else ""; _refresh_panel())
	ui.add_child(choose)
	var confirm := _button("결과 확정 → 병력 지급", Rect2(889, 0, 320, 38), func(): run.confirm_omen(selected_bonus); _refresh_panel(), ui)
	confirm.name = "ConfirmOmen"
	confirm.disabled = not run.omen_pending or (options.size() > 1 and selected_bonus == "")
	var names: Array = []
	for role in run.omen_rewards(selected_bonus):
		names.append(run.definitions[role][1])
	_label("남은 이동 %d회 · 대기 용량 %d/24 · 예약 %d칸\n%s\n3칸당 1명 + 완성선 보너스 최대 1명. 확정 전 지급 없음." % [run.omen_moves, run.queue_used(), run.omen_reserved, ("예상: " + (", ".join(names) if not names.is_empty() else "병력 없음")) if run.omen_pending else "관측 → 행/열 이동 → 보너스 선택 → 확정 → 전선 출전"], Rect2(290, 83, 915, 78), ui, 15)

func _reserve_panel() -> void:
	var recovery := _button("부상병 치료 · 비용 확인", Rect2(970, 0, 240, 32), _show_recovery, ui)
	recovery.name = "OpenRecovery"
	recovery.disabled = run.phase not in ["PREPARE", "REFIT"]
	recovery.tooltip_text = "준비·재정비 중 생존한 아군을 골드로 회복합니다."
	_label("대기 용량 %s/24 · 출전 %s/18 · 병종 카드를 눌러 전장에 투입" % [run.queue_used(), run.capacity_used()], Rect2(0, 0, 950, 26), ui)
	var counts: Dictionary = {}
	for role in run.reserve:
		counts[role] = counts.get(role, 0) + 1
	var i := 0
	for role in counts:
		var b := _button("", Rect2(i * 122, 32, 116, 126), func(): run.deploy(role); _refresh_panel(), ui)
		b.tooltip_text = "%s · %s\n체력 %s · 공격 %s · 출전 한도 %s칸\n현재 검토판: 기본 공격/범위/치료만 구현. 도감의 고유 능력은 후속." % [run.definitions[role][1], run.definitions[role][2], run.definitions[role][4], run.definitions[role][5], run.definitions[role][11]]
		if role == "shield_guard":
			b.tooltip_text = "방패병 · 체력%s · 공격%s · 출전%s칸\n근접 적을 막는 동안 정면 화살 피해25%% 완화\n이동 중·후방·마법·근접 공격에는 미적용" % [run.definitions[role][4], run.definitions[role][5], run.definitions[role][11]]
		elif role in ["cavalry", "spear_guard"]:
			b.tooltip_text = "%s · 체력%s · 공격%s · 출전%s칸\n%s" % [run.definitions[role][1], run.definitions[role][4], run.definitions[role][5], run.definitions[role][11], "2거리 이동 후 첫 타격1.5배" if role == "cavalry" else "접전에서0.6초 정지 후 돌격 피해50% 완화"]
		elif role in ["archer", "flying", "assassin"]:
			b.tooltip_text = "%s · 체력%s · 공격%s · 출전%s칸\n%s" % [run.definitions[role][1], run.definitions[role][4], run.definitions[role][5], run.definitions[role][11], {"archer": "사거리 안 공중 표적 우선 사격", "flying": "지상 후열 우선 접근 · 무적 아님", "assassin": "후열 우선 · 후열 타격1.4배 / 10초 재사용"}[role]]
		_picture(art.unit(role, 0), Rect2(20, 4, 76, 76), b)
		_label("%s ×%s\n출전" % [run.definitions[role][1], counts[role]], Rect2(5, 79, 108, 44), b, 13)
		b.disabled = run.capacity_used() + int(run.definitions[role][11]) > 18 or run.phase in ["VICTORY", "DEFEAT"]
		i += 1
	if counts.is_empty():
		_label("대기 병력이 없습니다. 병영 자동 생산 또는 징조륜으로 보충하세요.", Rect2(20, 54, 1150, 40), ui)

func _process(delta: float) -> void:
	if not paused:
		run.advance(delta * speed)
	refresh_clock += delta
	if refresh_clock > 0.25:
		refresh_clock = 0
		if panel_key != _state_key():
			_refresh_panel()
	header.text = "%s  |  라운드 %d/%d  ·  공세 %d/3  ·  %02d초  |  %dG  ·  출전 %d/18  |  %s" % [phase_label(), run.round_number, int(run.catalog.maps[run.current_map].rounds), run.wave_index, ceili(maxf(0, 60 - run.elapsed)), run.gold, run.capacity_used(), "정지" if paused else "%d×" % int(speed)]
	for i in range(map_labels.size()):
		map_labels[i].text = ("◆ " if i == run.current_map else "✓ " if i < run.current_map else "◇ ") + run.catalog.maps[i].name
		map_labels[i].modulate = Color("f6d687") if i == run.current_map else Color("8796ad")
	pause_button.text = "계속 진행" if paused else "일시정지"
	speed_button.text = "속도 %d×" % int(speed)
	speed_button.tooltip_text = "누르면 %d배속으로 변경" % (1 if speed == 3.0 else 3)
	notice.text = run.message
	forecast_label.text = forecast_text()
	if is_instance_valid(production_label):
		var status: Dictionary = run.production_status(selected)
		var state: String = {"LOCKED": "슬롯 잠김 · 생산 중단", "FROZEN": "전투 외 시간 · 생산 동결", "QUEUE_FULL": "대기열 가득 참 · 출전 후 공급", "PRODUCING": "생산 중", "EMPTY": "빈 슬롯"}[status.state]
		if run.phase in ["VICTORY", "DEFEAT"]:
			state = "전투 종료 · 생산 종료"
		elif paused:
			state = "일시정지 · " + ("생산 정지" if status.state == "PRODUCING" else state)
		production_label.text = "%s · 남은 %d초" % [state, ceili(status.remaining)]
		production_bar.value = status.progress * 100
	start_button.text = "다음 라운드" if run.phase == "REFIT" else "공세 시작"
	start_button.disabled = run.omen_pending or run.phase not in ["PREPARE", "REFIT"]
	if run.phase == "VICTORY":
		start_button.text = "다음 맵 준비" if run.current_map < run.catalog.maps.size() - 1 else "원정 완료"
		start_button.disabled = run.current_map >= run.catalog.maps.size() - 1
	start_button.tooltip_text = ""
	if run.phase == "DEFEAT":
		start_button.text = "맵 진입부터 재도전"
		start_button.disabled = run.map_entry.is_empty()
		start_button.tooltip_text = "구형 저장에는 맵 진입 기록이 없어 재도전할 수 없습니다. 새 출정은 가능합니다." if run.map_entry.is_empty() else "이 맵에서 사용하거나 얻은 자원·병력·추첨을 진입 당시로 되돌립니다."
	queue_redraw()

func phase_label() -> String:
	return {"PREPARE": "출정 준비", "BATTLE": "전투 중", "REFIT": "재정비", "VICTORY": "승리", "DEFEAT": "패배"}.get(run.phase, run.phase)

func forecast_text() -> String:
	var forecast: Dictionary = run.wave_forecast()
	if forecast.is_empty():
		return "전투 종료 · 결과를 확인하세요." if run.phase in ["VICTORY", "DEFEAT"] else "이번 라운드 추가 공세 없음 · 남은 적과 전선 유지"
	var groups := PackedStringArray()
	for role in forecast.units:
		groups.append("%s ×%d" % [run.definitions[role][3], forecast.units[role]])
	var timing := "%d초 후" % ceili(forecast.seconds) if run.phase == "BATTLE" else "공세 시작 후 %d초" % ceili(forecast.seconds)
	return "다음 공세 · %d라운드 %d/3 · %s%s · %s\n%s" % [forecast.round, forecast.wave, timing, " (정지)" if paused else "", "0.4초 간격 출현" if run.wave_rules == "staggered_v1" else "구형 저장 공세 유지", "  /  ".join(groups)]

func _show_recovery() -> void:
	if run.phase not in ["PREPARE", "REFIT"] or find_child("RecoveryDialog", true, false) != null:
		return
	var dialog := AcceptDialog.new()
	dialog.name = "RecoveryDialog"
	dialog.title = "부상병 치료 · 건설과 같은 골드 사용"
	dialog.ok_button_text = "돌아가기"
	add_child(dialog)
	var content := VBoxContainer.new()
	dialog.add_child(content)
	var balance := _label("보유 %dG · 선택한 병사를 최대 체력까지 회복" % run.gold, Rect2(0, 0, 570, 30), content, 16)
	balance.custom_minimum_size.y = 30
	var scroll := ScrollContainer.new()
	scroll.custom_minimum_size = Vector2(580, 310)
	content.add_child(scroll)
	var list := VBoxContainer.new()
	list.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	scroll.add_child(list)
	var count := 0
	for unit in run.units:
		var id: int = int(unit.id)
		var cost: int = run.heal_cost(id)
		if cost <= 0:
			continue
		count += 1
		var button := Button.new()
		button.name = "HealUnit%d" % id
		button.custom_minimum_size = Vector2(540, 40)
		button.text = "%s · 체력 %d/%d → 완전 회복 · %dG" % [run.definitions[unit.role][1], ceili(unit.hp), int(run.definitions[unit.role][4]), cost]
		button.disabled = run.gold < cost
		list.add_child(button)
		button.pressed.connect(func():
			if run.heal_unit(id):
				button.text = "%s · 치료 완료" % run.definitions[unit.role][1]
			balance.text = "보유 %dG · 선택한 병사를 최대 체력까지 회복" % run.gold
			for option in list.get_children():
				if option is Button:
					var target_id := int(String(option.name).trim_prefix("HealUnit"))
					var price: int = run.heal_cost(target_id)
					option.disabled = price <= 0 or run.gold < price)
	if count == 0:
		var empty := Label.new()
		empty.text = "치료할 생존 아군이 없습니다."
		list.add_child(empty)
	dialog.confirmed.connect(dialog.queue_free)
	dialog.canceled.connect(dialog.queue_free)
	dialog.popup_centered(Vector2i(620, 420))

func _get_tooltip(at_position: Vector2) -> String:
	if not Rect2(20, 225, 1240, 160).has_point(at_position):
		return ""
	var lines: PackedStringArray = []
	var count := 0
	for unit in run.units:
		if float(unit.hp) <= 0 or unit_draw_anchor(unit).distance_to(at_position) > 42:
			continue
		count += 1
		if lines.size() < 6:
			var row: Array = run.definitions[unit.role]
			lines.append("%s · %s · 체력 %d/%d%s" % ["아군" if unit.side == 0 else "베일", row[1] if unit.side == 0 else row[3], ceili(unit.hp), int(row[4]), " · 정면 화살 방어25%" if run.shield_guarding(unit) else ""])
			if unit.role == "cavalry" and float(unit.get("charge", 0.0)) >= 2.0:
				lines[-1] += " · 돌격 준비"
			elif unit.role == "spear_guard" and float(unit.get("brace", 0.0)) >= 0.6:
				lines[-1] += " · 돌격 저지 준비"
	if count > 6:
		lines.append("근처 병력 %d명 더 있음 · 정지 후 위치를 옮겨 확인" % (count - 6))
	return "\n".join(lines)

func unit_draw_anchor(unit: Dictionary) -> Vector2:
	# Stable display-only stagger: never feed these coordinates into combat.
	var rear := -1.0 if int(unit.side) == 0 else 1.0
	var stagger := (int(unit.id) / 4 % 2) * 24.0
	return Vector2(65 + float(unit.x) * 11.5 + rear * stagger, 262 + (int(unit.id) % 4) * 32)

func _draw() -> void:
	draw_rect(Rect2(0, 0, 1280, 720), Color("111c2b"))
	if backdrop == null:
		return
	draw_texture_rect(backdrop, Rect2(20, 115, 1240, 310), false)
	draw_rect(Rect2(20, 115, 1240, 310), Color("b99b65"), false, 2)
	for i in range(3):
		var color := Color("7bc7ec") if run.points[i] == 1 else Color("cf8bdf") if run.points[i] == -1 else Color("e6d8b6")
		var x := 65.0 + (25 + i * 25) * 11.5
		draw_string(font, Vector2(x - 40, 190), ["수호 전진지", "접전 / 방어탑", "장막 전진지"][i], HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("172235"))
		draw_circle(Vector2(x, 200), 5, color)
	# Tower is a labeled UI marker in this candidate preview, not invented artwork.
	draw_string(font, Vector2(567, 222), "탑  %s" % ("아군" if run.points[1] == 1 else "베일" if run.points[1] == -1 else "중립"), HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("253249"))
	var actors: Array = run.units.duplicate()
	actors.sort_custom(func(a, b):
		var ay: float = unit_draw_anchor(a).y
		var by: float = unit_draw_anchor(b).y
		return int(a.id) < int(b.id) if is_equal_approx(ay, by) else ay < by)
	for unit in actors:
		var anchor := unit_draw_anchor(unit)
		var x: float = anchor.x
		var y: float = anchor.y
		var movement := float(unit.action) * 15 * (1 if unit.side == 0 else -1)
		var rect := Rect2(x - 26 + movement, y - 32, 52, 52)
		if unit.side == 0 and unit.role == "shield_guard":
			# Native 768px frames share foot pivot (384,700); do not slide the whole sprite.
			rect = Rect2(x - 34, y + 20 - 700.0 / 768.0 * 68, 68, 68)
		draw_texture_rect(art.unit(unit.role, int(unit.side), art.motion_frame(unit)), rect, false, Color(1, 0.65, 0.65) if unit.flash > 0 else Color.WHITE)
	# Draw status after every sprite, so later actors cannot cover health bars.
	for unit in actors:
		var anchor := unit_draw_anchor(unit)
		var side_color := Color("48b5ee") if unit.side == 0 else Color("ae57d3")
		draw_rect(Rect2(anchor.x - 20, anchor.y + 23, 40, 5), Color("172235"))
		draw_rect(Rect2(anchor.x - 19, anchor.y + 24, 38 * clampf(float(unit.hp) / float(run.definitions[unit.role][4]), 0, 1), 3), side_color)
	draw_rect(Rect2(26, 388, 185, 31), Color("14293b"))
	draw_rect(Rect2(1065, 388, 190, 31), Color("35213d"))
	draw_string(font, Vector2(35, 409), "수호 성채 %d" % maxi(0, int(run.bases[0])), HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("c3e8fb"))
	draw_string(font, Vector2(1078, 409), "베일 본진 %d" % maxi(0, int(run.bases[1])), HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("f0c8ff"))

func _save() -> void:
	var file := FileAccess.open(save_path + ".tmp", FileAccess.WRITE)
	if file == null:
		run.message = "저장 파일을 열 수 없습니다."
		return
	file.store_string(JSON.stringify(run.snapshot()))
	file.close()
	var result := DirAccess.rename_absolute(save_path + ".tmp", save_path)
	run.message = "저장 완료 · 현재 전투/생산 상태 보존" if result == OK else "저장 교체 실패 · 기존 파일 유지"

func _load_save() -> void:
	if not FileAccess.file_exists(save_path):
		run.message = "저장된 검토판 출정이 없습니다."
		return
	if run.restore(JSON.parse_string(FileAccess.get_file_as_string(save_path))):
		run.message = "불러오기 완료"
	else:
		run.message = "저장 형식이 맞지 않습니다. 현재 출정을 유지합니다."
	_refresh_panel()
