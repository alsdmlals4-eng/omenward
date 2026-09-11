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
	for i in range(5):
		var map: Dictionary = run.catalog.maps[i]
		var label := _label(("◆ " if i == 0 else "◇ ") + map.name, Rect2(25 + i * 250, 40, 240, 28))
		label.modulate = Color("f6d687") if i == 0 else Color("8796ad")
	start_button = _button("공세 시작", Rect2(1070, 76, 185, 34), func(): run.begin_round(); _refresh_panel())
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
	_label("투명 후보: 베일 10종·아군 방패병 대기 | 베일 Aseprite 검수 · 공격 프레임/T3/영웅/등급 스킬 미연결", Rect2(24, 691, 1240, 25), self, 13)

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
	for i in range(9):
		var y := 29 + (i % 3) * 43
		var x := (i / 3) * 185
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
	if selected < run.buildings.size():
		var b: Dictionary = run.buildings[selected]
		_picture(art.building(b.id), Rect2(570, 8, 130, 130), ui)
		_label("%s → %s\n자동 생산 %s초 / 대기열로 공급" % [run.facilities[b.id][1], run.definitions[b.unit][1], run.facilities[b.id][5]], Rect2(714, 0, 510, 48), ui)
		var options: Array = []
		for id in run.branches:
			if run.branches[id][1] == b.id:
				options.append(id)
		for j in range(options.size()):
			var id: String = options[j]
			var button := _button("%s %sG" % [run.facilities[id][1], run.facilities[id][2]], Rect2(714 + (j % 3) * 170, 54 + (j / 3) * 39, 164, 35), func(): run.upgrade(selected, id); _refresh_panel(), ui)
			button.add_theme_font_size_override("font_size", 13)
			button.disabled = run.phase not in ["PREPARE", "REFIT"] or (run.round_number < 2 and run.phase != "REFIT") or run.gold < int(run.facilities[id][2])
		_label("T2: 2라운드 준비부터 · 변경 시 생산 시간 초기화", Rect2(714, 139, 510, 26), ui, 13)
	else:
		_picture(art.building("barracks"), Rect2(578, 12, 125, 125), ui)
		_label("T1부터 건설 → T2에서 같은 계열 전문화", Rect2(714, 0, 510, 28), ui)
		var normal := _button("일반 병영 · 방패병 · 40G", Rect2(714, 39, 490, 43), func(): run.construct("barracks"); _refresh_panel(), ui)
		var special := _button("특수 병영 · 특수병 1종 고정 추첨 · 75G", Rect2(714, 90, 490, 43), func(): run.construct("special_barracks"); _refresh_panel(), ui)
		normal.disabled = run.phase not in ["PREPARE", "REFIT"] or run.gold < 40 or run.buildings.size() >= run.unlocked_slots()
		special.disabled = run.phase not in ["PREPARE", "REFIT"] or run.gold < 75 or run.buildings.size() >= run.unlocked_slots()
		_label("건설은 첫 빈 슬롯에 배치됩니다. 특수 병영 추첨은 저장됩니다.", Rect2(714, 137, 510, 25), ui, 13)

func _omen_panel() -> void:
	for i in range(9):
		var rect := Rect2((i % 3) * 55, (i / 3) * 55, 50, 50)
		if i < run.last_board.size() and run.last_board[i] != "":
			_picture(art.unit(run.last_board[i], 0), rect, ui)
		else:
			_label("—", rect, ui)
	var b := _button("징조륜 관측 · %s" % ("무료" if run.free_spin else "20G"), Rect2(195, 5, 285, 42), func(): run.spin(); _refresh_panel(), ui)
	b.disabled = run.phase not in ["PREPARE", "REFIT"] or run.reserve.size() > 20 or (not run.free_spin and run.gold < 20)
	_label("건설한 시설이 확률 풀에 공급 병종을 추가합니다.\n같은 병종 3칸마다 1명 → 전선 탭에서 출전\n현재 기본 추첨 검토판: 행/열 이동·보너스 미구현", Rect2(195, 58, 780, 100), ui)

func _reserve_panel() -> void:
	_label("대기 병력 %s/24 · 출전 %s/18 · 생산된 병종 카드를 눌러 전장에 투입" % [run.reserve.size(), run.capacity_used()], Rect2(0, 0, 1210, 26), ui)
	var counts: Dictionary = {}
	for role in run.reserve:
		counts[role] = counts.get(role, 0) + 1
	var i := 0
	for role in counts:
		var b := _button("", Rect2(i * 122, 32, 116, 126), func(): run.deploy(role); _refresh_panel(), ui)
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
	header.text = "%s  |  라운드 %d/10  ·  공세 %d/3  ·  %02d초  |  %dG  ·  출전 %d/18  |  %s" % [phase_label(), run.round_number, run.wave_index, ceili(maxf(0, 60 - run.elapsed)), run.gold, run.capacity_used(), "정지" if paused else "%d×" % int(speed)]
	pause_button.text = "계속 진행" if paused else "일시정지"
	speed_button.text = "속도 %d×" % int(speed)
	speed_button.tooltip_text = "누르면 %d배속으로 변경" % (1 if speed == 3.0 else 3)
	notice.text = run.message
	start_button.text = "다음 라운드" if run.phase == "REFIT" else "공세 시작"
	start_button.disabled = run.phase not in ["PREPARE", "REFIT"]
	queue_redraw()

func phase_label() -> String:
	return {"PREPARE": "출정 준비", "BATTLE": "전투 중", "REFIT": "재정비", "VICTORY": "승리", "DEFEAT": "패배"}.get(run.phase, run.phase)

func _draw() -> void:
	draw_rect(Rect2(0, 0, 1280, 720), Color("111c2b"))
	if backdrop == null:
		return
	draw_texture_rect(backdrop, Rect2(20, 115, 1240, 310), false)
	draw_rect(Rect2(20, 115, 1240, 310), Color("b99b65"), false, 2)
	for i in range(3):
		var color := Color("7bc7ec") if run.points[i] == 1 else Color("cf8bdf") if run.points[i] == -1 else Color("e6d8b6")
		var x := 65.0 + (25 + i * 25) * 11.5
		draw_string(font, Vector2(x - 40, 146), ["수호 전진지", "접전 / 방어탑", "장막 전진지"][i], HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("172235"))
		draw_circle(Vector2(x, 156), 5, color)
	# Tower is a labeled UI marker in this candidate preview, not invented artwork.
	draw_string(font, Vector2(567, 178), "탑  %s" % ("아군" if run.points[1] == 1 else "베일" if run.points[1] == -1 else "중립"), HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("253249"))
	for unit in run.units:
		var x: float = 65 + float(unit.x) * 11.5
		var y: float = 292 + (int(unit.id) % 3) * 38
		var movement := float(unit.action) * 15 * (1 if unit.side == 0 else -1)
		var rect := Rect2(x - 26 + movement, y - 32, 52, 52)
		draw_texture_rect(art.unit(unit.role, int(unit.side)), rect, false, Color(1, 0.65, 0.65) if unit.flash > 0 else Color.WHITE)
		var side_color := Color("48b5ee") if unit.side == 0 else Color("ae57d3")
		if unit.side == 0 and unit.role != "shield_guard":
			draw_rect(rect, side_color, false, 2)
		draw_rect(Rect2(x - 26, y + 23, 52, 5), Color("302d36"))
		draw_rect(Rect2(x - 26, y + 23, 52 * clampf(float(unit.hp) / float(run.definitions[unit.role][4]), 0, 1), 5), side_color)
		if unit.action > 0:
			draw_string(font, Vector2(x - 12, y - 38), "+" if unit.role == "priest" else "공격", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color("15283e"))
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
