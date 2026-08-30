# 플레이어용 Run Command 화면의 표시·입력만 담당하며 규칙 계산은 StageRun에 위임한다.
class_name RunCommandScreen
extends Control

const LANE_IDS := [&"top", &"middle", &"bottom"]
const UNIT_TOKEN_TEXTURE := preload("res://assets/art/units/lumern_shield_guard_storybook_idle_v1.png")

@onready var _phase_label: Label = $TopBar/PhaseLabel
@onready var _gold_label: Label = $TopBar/GoldLabel
@onready var _food_label: Label = $TopBar/FoodLabel
@onready var _strategic_map: Control = $StrategicMap
@onready var _primary_label: Label = $LowerDeck/PrimaryLabel
@onready var _building_roster: ItemList = $LowerDeck/PreparePanel/BuildingRoster
@onready var _prepare_panel: Control = $LowerDeck/PreparePanel
@onready var _roulette_panel: Control = $LowerDeck/RoulettePanel
@onready var _commit_panel: Control = $LowerDeck/CommitPanel
@onready var _battle_panel: Control = $LowerDeck/BattlePanel
@onready var _review_panel: Control = $LowerDeck/ReviewPanel
@onready var _board_grid: GridContainer = $LowerDeck/RoulettePanel/BoardGrid
@onready var _result_label: Label = $LowerDeck/RoulettePanel/ResultLabel
@onready var _move_label: Label = $LowerDeck/RoulettePanel/MoveLabel
@onready var _selection_detail: Label = $LowerDeck/RoulettePanel/SelectionDetail
@onready var _result_list: GridContainer = $LowerDeck/RoulettePanel/ResultList
@onready var _commit_assignments: VBoxContainer = $LowerDeck/CommitPanel/Assignments
@onready var _commit_label: Label = $LowerDeck/CommitPanel/CommitLabel

var run: Variant
var _spin_seed := 1
var _selected_roulette_index := -1
var _selected_roster_slot := -1


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_refresh()


func _process(_delta: float) -> void:
	_refresh()


func _on_barracks_pressed() -> void:
	if run != null:
		run.install_building(&"barracks")


func _on_tower_pressed() -> void:
	if run != null:
		run.install_building(&"tower")


func _on_farm_pressed() -> void:
	if run != null:
		run.install_building(&"farm")


func _on_roster_selected(slot_index: int) -> void:
	_selected_roster_slot = slot_index


func _on_roster_move_up_pressed() -> void:
	_move_selected_roster_entry(-1)


func _on_roster_move_down_pressed() -> void:
	_move_selected_roster_entry(1)


func _on_spin_pressed() -> void:
	if run != null:
		_spin_seed += 1
		run.begin_roulette_session({"seed": _spin_seed})


func _on_lock_result_pressed() -> void:
	if run != null:
		run.lock_roulette_result()


func _on_confirm_result_pressed() -> void:
	if run != null:
		run.confirm_roulette_result()


func _on_commit_pressed() -> void:
	if run != null:
		run.confirm_pending_deployment()


func _on_begin_battle_pressed() -> void:
	if run != null:
		run.begin_battle()


func _on_retry_pressed() -> void:
	var session := get_node_or_null("../../GameSession")
	if session != null:
		session.retry_stage()


func _move_row(row_index: int, direction: int) -> void:
	if run != null:
		run.move_roulette_row(row_index, direction)


func _move_column(column_index: int, direction: int) -> void:
	if run != null:
		run.move_roulette_column(column_index, direction)


func select_roulette_tile(index: int) -> void:
	if index >= 0 and index < 9:
		_selected_roulette_index = index


func selected_roulette_tile_index() -> int:
	return _selected_roulette_index


func _refresh() -> void:
	if run == null or run.economy == null:
		return
	_gold_label.text = "Gold %d" % int(run.economy.gold)
	_food_label.text = "병력 %d/%d" % [int(run.economy.food_used), int(run.economy.food_cap)]
	_phase_label.text = _phase_title(StringName(run.command_phase))
	_strategic_map.bind_run(run)
	_refresh_phase_panels()
	_refresh_building_roster()
	_refresh_roulette()
	_refresh_commit()


func _refresh_building_roster() -> void:
	if run == null or run.buildings == null:
		return
	var roster: Array = run.building_roster_snapshot()
	_building_roster.clear()
	for entry in roster:
		var state := str(entry.get("state", ""))
		var building_name := str(entry.get("display_name", "빈 슬롯"))
		var status := "활성" if state == "active" else ("잠김" if state == "inactive_locked" else "비어 있음")
		_building_roster.add_item("%d. %s · %s" % [int(entry.get("slot_index", 0)) + 1, building_name, status])
	if roster.is_empty():
		_selected_roster_slot = -1
	elif _selected_roster_slot < 0 or _selected_roster_slot >= roster.size():
		_selected_roster_slot = 0
	if _selected_roster_slot >= 0:
		_building_roster.select(_selected_roster_slot, true)
	var roster_is_mutable := StringName(run.command_phase) == &"prepare"
	$LowerDeck/PreparePanel/RosterMoveUpButton.disabled = not roster_is_mutable or _selected_roster_slot <= 0
	$LowerDeck/PreparePanel/RosterMoveDownButton.disabled = not roster_is_mutable or _selected_roster_slot < 0 or _selected_roster_slot >= roster.size() - 1
	_update_install_button_state(&"barracks", $LowerDeck/PreparePanel/BarracksButton)
	_update_install_button_state(&"tower", $LowerDeck/PreparePanel/TowerButton)
	_update_install_button_state(&"farm", $LowerDeck/PreparePanel/FarmButton)


func _update_install_button_state(building_id: StringName, button: Button) -> void:
	var reason := String(run.buildings.install_block_reason(building_id))
	var phase_is_prepare := StringName(run.command_phase) == &"prepare"
	button.disabled = reason != "" or not phase_is_prepare
	button.tooltip_text = "로스터에 추가" if reason == "" and phase_is_prepare else (reason if reason != "" else "준비 단계에서만 변경할 수 있습니다")


func _move_selected_roster_entry(direction: int) -> void:
	if run == null or _selected_roster_slot < 0:
		return
	var target_slot := _selected_roster_slot + direction
	if target_slot < 0 or target_slot >= run.building_roster_snapshot().size():
		return
	if run.move_building_roster_entry(_selected_roster_slot, target_slot):
		_selected_roster_slot = target_slot


func _refresh_phase_panels() -> void:
	var phase := StringName(run.command_phase)
	_prepare_panel.visible = phase == run.PREPARE
	_roulette_panel.visible = phase == run.STOPPED_3X3 or phase == run.MANIPULATE or phase == run.RESULT_CONFIRM
	_commit_panel.visible = phase == run.COMMIT
	_battle_panel.visible = phase == run.BATTLE
	_review_panel.visible = phase == run.REVIEW
	match phase:
		run.PREPARE:
			_primary_label.text = "다가오는 징조를 보고 무엇을 준비할까?"
		run.STOPPED_3X3, run.MANIPULATE:
			_primary_label.text = "3×3 징조를 조정할까, 지금 결과를 볼까?"
		run.RESULT_CONFIRM:
			_primary_label.text = "이 결과를 확정하고 병력을 커밋할까?"
		run.COMMIT:
			_primary_label.text = "획득 병력을 어느 전선에 되돌릴 수 없게 보낼까?"
		run.BATTLE:
			_primary_label.text = "세 전선의 현재 전황을 관찰한다"
		run.REVIEW:
			_primary_label.text = "이번 설계와 배치가 만든 결과를 복기한다"


func _refresh_roulette() -> void:
	if run.command_phase != run.STOPPED_3X3 and run.command_phase != run.MANIPULATE and run.command_phase != run.RESULT_CONFIRM:
		return
	var board: Array = run.roulette_session.get("board", [])
	if board.size() != 9:
		return
	if _selected_roulette_index < 0 or _selected_roulette_index >= board.size():
		_selected_roulette_index = 4
	for child in _board_grid.get_children():
		child.queue_free()
	for index in board.size():
		var symbol: StringName = board[index]
		var tile := Button.new()
		tile.custom_minimum_size = Vector2(34, 34)
		tile.icon = _token_texture(symbol)
		tile.expand_icon = true
		tile.tooltip_text = "%d번 슬롯 · %s" % [index + 1, _roulette_symbol_name(symbol)]
		tile.modulate = Color(1.25, 1.16, 0.72, 1.0) if index == _selected_roulette_index else Color.WHITE
		tile.pressed.connect(func() -> void: select_roulette_tile(index))
		_board_grid.add_child(tile)
	_refresh_roulette_picker(board)
	_move_label.text = "남은 이동 %d · preview는 비용 없음" % int(run.roulette_moves_remaining)
	var preview: Variant = run.preview_roulette_result()
	_result_label.text = "중앙 판정: %s · 완성선 %d" % [str(preview.outcome_type), int(preview.completed_line_count)]
	$LowerDeck/RoulettePanel/LockResultButton.visible = run.command_phase != run.RESULT_CONFIRM
	$LowerDeck/RoulettePanel/ConfirmResultButton.visible = run.command_phase == run.RESULT_CONFIRM
	_set_arrow_buttons_disabled(run.command_phase == run.RESULT_CONFIRM or int(run.roulette_moves_remaining) <= 0)


func _refresh_commit() -> void:
	if run.command_phase != run.COMMIT:
		return
	for child in _commit_assignments.get_children():
		child.queue_free()
	if run.pending_roulette_rewards.is_empty():
		_commit_label.text = "획득 병력이 없습니다. 전투를 시작할 수 있습니다."
		$LowerDeck/CommitPanel/ConfirmDeploymentButton.visible = false
		$LowerDeck/CommitPanel/BeginBattleButton.visible = true
		return
	$LowerDeck/CommitPanel/ConfirmDeploymentButton.visible = true
	$LowerDeck/CommitPanel/BeginBattleButton.visible = false
	_commit_label.text = "모든 병력의 전선을 고른 뒤 한 번에 커밋합니다."
	for reward_index in run.pending_roulette_rewards.size():
		if not run.pending_deployment_assignments.has(reward_index):
			run.assign_pending_reward(reward_index, &"top")
		var assignment := OptionButton.new()
		assignment.add_item("상단 전선")
		assignment.add_item("중앙 전선")
		assignment.add_item("하단 전선")
		assignment.select(_lane_index(StringName(run.pending_deployment_assignments.get(reward_index, &"top"))))
		assignment.tooltip_text = "획득 병력 %d의 비가역 배치 전선" % (reward_index + 1)
		assignment.item_selected.connect(func(selected: int) -> void: run.assign_pending_reward(reward_index, LANE_IDS[selected]))
		_commit_assignments.add_child(assignment)


func _set_arrow_buttons_disabled(disabled: bool) -> void:
	for button in $LowerDeck/RoulettePanel/ArrowControls.get_children():
		if button is Button:
			button.disabled = disabled


func _token_texture(symbol: StringName) -> Texture2D:
	match symbol:
		&"x":
			return load("res://assets/art/ui/run_command/token_x.png")
		&"gold":
			return load("res://assets/art/ui/run_command/token_gold.png")
		_:
			return UNIT_TOKEN_TEXTURE


func _refresh_roulette_picker(board: Array) -> void:
	for child in _result_list.get_children():
		child.queue_free()
	var selected_symbol: StringName = board[_selected_roulette_index]
	_selection_detail.text = "선택 %d번 · %s\n아래 목록이나 타일을 눌러 다른 결과도 살펴보세요." % [_selected_roulette_index + 1, _roulette_symbol_name(selected_symbol)]
	for index in board.size():
		var symbol: StringName = board[index]
		var entry := Button.new()
		entry.custom_minimum_size = Vector2(88, 16)
		entry.add_theme_font_size_override("font_size", 10)
		entry.text = "%d. %s" % [index + 1, _roulette_symbol_name(symbol)]
		entry.tooltip_text = "이 항목을 선택해 결과 의미를 확인합니다."
		entry.modulate = Color(1.25, 1.16, 0.72, 1.0) if index == _selected_roulette_index else Color.WHITE
		entry.pressed.connect(func() -> void: select_roulette_tile(index))
		_result_list.add_child(entry)


func _roulette_symbol_name(symbol: StringName) -> String:
	match symbol:
		&"x":
			return "빈 징조"
		&"gold":
			return "황금 징조"
		_:
			return "수호 병력"


func _lane_index(lane_id: StringName) -> int:
	return LANE_IDS.find(lane_id)


func _phase_title(phase: StringName) -> String:
	return str(phase).replace("_", " ").to_upper()
