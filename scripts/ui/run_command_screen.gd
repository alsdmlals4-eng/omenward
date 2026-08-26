# 플레이어용 Run Command 화면의 표시·입력만 담당하며 규칙 계산은 StageRun에 위임한다.
class_name RunCommandScreen
extends Control

const LANE_IDS := [&"top", &"middle", &"bottom"]
const LANE_TITLES := {&"top": "상단 전선", &"middle": "중앙 전선", &"bottom": "하단 전선"}
const UNIT_TOKEN_TEXTURE := preload("res://assets/art/units/lumern_shield_guard_idle.png")

@onready var _phase_label: Label = $TopBar/PhaseLabel
@onready var _gold_label: Label = $TopBar/GoldLabel
@onready var _food_label: Label = $TopBar/FoodLabel
@onready var _primary_label: Label = $LowerDeck/PrimaryLabel
@onready var _prepare_panel: Control = $LowerDeck/PreparePanel
@onready var _roulette_panel: Control = $LowerDeck/RoulettePanel
@onready var _commit_panel: Control = $LowerDeck/CommitPanel
@onready var _battle_panel: Control = $LowerDeck/BattlePanel
@onready var _review_panel: Control = $LowerDeck/ReviewPanel
@onready var _board_grid: GridContainer = $LowerDeck/RoulettePanel/BoardGrid
@onready var _result_label: Label = $LowerDeck/RoulettePanel/ResultLabel
@onready var _move_label: Label = $LowerDeck/RoulettePanel/MoveLabel
@onready var _commit_assignments: VBoxContainer = $LowerDeck/CommitPanel/Assignments
@onready var _commit_label: Label = $LowerDeck/CommitPanel/CommitLabel

var run: Variant
var _spin_seed := 1


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_refresh()


func _process(_delta: float) -> void:
	_refresh()


func _on_barracks_pressed() -> void:
	if run != null:
		run.construct_home(&"barracks")


func _on_tower_pressed() -> void:
	if run != null:
		run.construct_home(&"tower")


func _on_farm_pressed() -> void:
	if run != null:
		run.construct_home(&"farm")


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


func _refresh() -> void:
	if run == null or run.economy == null:
		return
	_gold_label.text = "Gold %d" % int(run.economy.gold)
	_food_label.text = "병력 %d/%d" % [int(run.economy.food_used), int(run.economy.food_cap)]
	_phase_label.text = _phase_title(StringName(run.command_phase))
	_refresh_fronts()
	_refresh_phase_panels()
	_refresh_roulette()
	_refresh_commit()


func _refresh_fronts() -> void:
	var omen: Dictionary = run.core_ux_snapshot().get("omen", {})
	var lanes: Array = omen.get("lanes", [])
	var lane_details := {}
	for lane in lanes:
		lane_details[StringName(lane.get("lane_id", ""))] = lane
	for lane_id in LANE_IDS:
		var panel := $Fronts.get_node(NodePath("%s" % str(lane_id).capitalize()))
		var detail: Dictionary = lane_details.get(lane_id, {})
		var enemy_count := int(detail.get("count", 0))
		var friendly_count := _friendly_count(lane_id)
		panel.get_node("Title").text = "%s · 아군 %d / 징조 %d" % [LANE_TITLES[lane_id], friendly_count, enemy_count]
		panel.get_node("Minimap/Progress").value = clampi(50 + (friendly_count - enemy_count) * 10, 5, 95)
		panel.get_node("Minimap/Context").text = "수호성  ◇───◆  Veil"


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
	for child in _board_grid.get_children():
		child.queue_free()
	for symbol in board:
		var tile := TextureRect.new()
		tile.custom_minimum_size = Vector2(34, 34)
		tile.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		tile.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		tile.texture = _token_texture(StringName(symbol))
		_board_grid.add_child(tile)
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


func _friendly_count(lane_id: StringName) -> int:
	if run.battle == null or not run.battle.lanes.has(lane_id):
		return 0
	var count := 0
	for unit in run.battle.lanes[lane_id].units:
		if unit.owner_team_id == &"lumern":
			count += 1
	return count


func _lane_index(lane_id: StringName) -> int:
	return LANE_IDS.find(lane_id)


func _phase_title(phase: StringName) -> String:
	return str(phase).replace("_", " ").to_upper()
