class_name StageHud
extends Control

const SPIN_COST := 20

@onready var _resource_label: Label = $ResourceLabel
@onready var _wave_label: Label = $WaveLabel
@onready var _omen_label: Label = $OmenLabel
@onready var _result_label: Label = $ResultLabel
@onready var _retry_button: Button = $RetryButton
@onready var _spin_button: Button = $BottomDock/RoulettePanel/SpinButton
@onready var _reserve_label: Label = $BottomDock/RoulettePanel/ReserveLabel
@onready var _roulette_feedback: Label = $BottomDock/RoulettePanel/FeedbackLabel
@onready var _deployment_label: Label = $BottomDock/RoulettePanel/DeploymentLabel
@onready var _row_status_label: Label = $BottomDock/RoulettePanel/RowStatusLabel
@onready var _node_build_panel: Panel = $NodeBuildPanel
@onready var _node_title: Label = $NodeBuildPanel/Title
@onready var _node_status: Label = $NodeBuildPanel/StatusLabel
@onready var _tower_button: Button = $NodeBuildPanel/TowerButton
@onready var _farm_button: Button = $NodeBuildPanel/FarmButton
@onready var _roulette_cells: Array[Label] = [
	$BottomDock/RoulettePanel/Board/Cell0/Token,
	$BottomDock/RoulettePanel/Board/Cell1/Token,
	$BottomDock/RoulettePanel/Board/Cell2/Token,
	$BottomDock/RoulettePanel/Board/Cell3/Token,
	$BottomDock/RoulettePanel/Board/Cell4/Token,
	$BottomDock/RoulettePanel/Board/Cell5/Token,
	$BottomDock/RoulettePanel/Board/Cell6/Token,
	$BottomDock/RoulettePanel/Board/Cell7/Token,
	$BottomDock/RoulettePanel/Board/Cell8/Token,
]

var run: Variant
var _pending_cards: Array = []
var _board_cards: Array = []
var _roulette_resolution: Dictionary = {}
var _spin_index := 0
var _roulette_feedback_text := "징조를 읽고 전력 표식을 회전하세요."
var _selected_outpost_id: StringName = &""
var _selected_node_id: StringName = &""


func _ready() -> void:
	var battlefield := get_node_or_null("../../Battlefield")
	if battlefield != null and battlefield.has_signal("construction_node_selected"):
		battlefield.construction_node_selected.connect(_on_construction_node_selected)
	_refresh_roulette_dock()
	_refresh_node_build_panel()


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_pending_cards.clear()
	_board_cards.clear()
	_roulette_resolution.clear()
	_roulette_feedback_text = "징조를 읽고 전력 표식을 회전하세요."
	_update_display()
	_refresh_roulette_dock()
	_refresh_node_build_panel()


func _process(_delta: float) -> void:
	_update_display()
	_refresh_roulette_dock()
	_refresh_node_build_panel()


func _on_spin_pressed() -> void:
	if run == null or run.economy == null:
		return
	if not _pending_cards.is_empty():
		_roulette_feedback_text = "보관함의 전력을 먼저 라인에 배치하세요."
		_refresh_roulette_dock()
		return
	if run.economy.gold < SPIN_COST:
		_roulette_feedback_text = "금화가 부족합니다. 회전에는 %d Gold가 필요합니다." % SPIN_COST
		_refresh_roulette_dock()
		return
	_spin_index += 1
	_board_cards = run.spin_roulette({"seed": _spin_index})
	_roulette_resolution = run.last_roulette_resolution.duplicate(true)
	_pending_cards.clear()
	if _roulette_resolution.get("has_reward", false):
		var matched_symbol: StringName = _roulette_resolution.get("matched_symbol", &"")
		for card in _board_cards:
			if card.archetype_id == matched_symbol:
				_pending_cards.append(card)
		_roulette_feedback_text = "중앙 줄 적중. %d줄 완성 %s 보상을 보관했습니다." % [int(_roulette_resolution.get("completed_line_count", 0)), _rank_name(_pending_cards.front())]
	else:
		_roulette_feedback_text = "중앙 가로줄이 맞지 않았습니다. 이번 회전 보상은 없습니다."
	_refresh_roulette_dock()


func _on_deploy_pressed(lane_id: StringName) -> void:
	if run == null:
		return
	if _pending_cards.is_empty():
		_roulette_feedback_text = "먼저 룰렛을 회전해 배치할 전력을 확보하세요."
		_refresh_roulette_dock()
		return
	var card: Variant = _pending_cards.front()
	if run.deploy_card(card, lane_id):
		_pending_cards.pop_front()
		_roulette_feedback_text = "%s 라인에 %s 배치 완료." % [_lane_name(lane_id), _display_name(card)]
	else:
		_roulette_feedback_text = "식량 또는 배치 조건이 부족해 배치하지 못했습니다."
	_refresh_roulette_dock()


func _on_retry_pressed() -> void:
	var session := get_node_or_null("../../GameSession")
	if session != null:
		session.retry_stage()


func _on_construction_node_selected(outpost_id: StringName, node_id: StringName) -> void:
	_selected_outpost_id = outpost_id
	_selected_node_id = node_id
	var battlefield := get_node_or_null("../../Battlefield")
	if battlefield != null:
		battlefield.set_selected_construction_node(outpost_id, node_id)
	_refresh_node_build_panel()


func _on_building_pressed(building_id: StringName) -> void:
	if run == null or _selected_outpost_id.is_empty() or _selected_node_id.is_empty():
		return
	if run.construct_at_node(_selected_outpost_id, _selected_node_id, building_id):
		_roulette_feedback_text = "%s 설치 완료. 다음 회전부터 표식 풀에 반영됩니다." % _building_name(building_id)
	else:
		_roulette_feedback_text = "%s 설치 조건을 충족하지 못했습니다." % _building_name(building_id)
	_refresh_node_build_panel()


func _on_node_build_close_pressed() -> void:
	_selected_outpost_id = &""
	_selected_node_id = &""
	_refresh_node_build_panel()


func _update_display() -> void:
	if run == null or run.economy == null:
		return
	_resource_label.text = "Gold %d   Food %d/%d" % [run.economy.gold, run.economy.food_used, run.economy.food_cap]
	_wave_label.text = "Wave %d" % run.current_wave
	var omen: float = float(run.wave_director.omen_seconds_remaining()) if run.wave_director != null else 0.0
	_omen_label.text = "Next omen %.0fs" % omen
	_result_label.visible = run.result_state != run.RUNNING
	_result_label.text = "Stage %s" % str(run.result_state).capitalize()
	_retry_button.visible = run.result_state != run.RUNNING


func _refresh_roulette_dock() -> void:
	if not is_instance_valid(_spin_button):
		return
	var gold := int(run.economy.gold) if run != null and run.economy != null else 0
	_spin_button.disabled = run == null or gold < SPIN_COST or not _pending_cards.is_empty()
	_spin_button.text = "회전 · %dG" % SPIN_COST
	_reserve_label.text = "결과 보관함  %d / 9" % _pending_cards.size()
	_deployment_label.text = "배치: %s" % (_display_name(_pending_cards.front()) if not _pending_cards.is_empty() else "대기 중")
	_roulette_feedback.text = _roulette_feedback_text
	_row_status_label.text = _row_status_text()
	var completed_cells := _completed_cell_indices()
	for index in _roulette_cells.size():
		var cell := _roulette_cells[index]
		if index < _board_cards.size():
			var card: Variant = _board_cards[index]
			cell.text = _token_symbol(card)
			cell.tooltip_text = "%s · %s" % [_display_name(card), _rank_name(card)]
			if completed_cells.has(index):
				cell.modulate = Color(1.0, 0.84, 0.35, 1.0)
			elif index in [3, 4, 5]:
				cell.modulate = Color(0.58, 0.83, 1.0, 1.0) if _roulette_resolution.get("has_reward", false) else Color(0.98, 0.55, 0.5, 1.0)
			else:
				cell.modulate = Color(0.83, 0.9, 0.98, 1.0)
		else:
			cell.text = "·"
			cell.tooltip_text = "비어 있음"
			cell.modulate = Color(0.48, 0.55, 0.62, 1.0)


func _refresh_node_build_panel() -> void:
	if not is_instance_valid(_node_build_panel):
		return
	_node_build_panel.visible = run != null and not _selected_outpost_id.is_empty() and not _selected_node_id.is_empty()
	if not _node_build_panel.visible:
		return
	var status: StringName = run.construction_status(_selected_outpost_id, _selected_node_id)
	var options: Array[StringName] = run.available_buildings_for_node(_selected_outpost_id, _selected_node_id)
	_node_title.text = "%s 노드" % _node_name(_selected_node_id)
	_node_status.text = "상태: %s\n설치할 건물을 선택하세요." % _node_status_name(status)
	_tower_button.disabled = not options.has(&"tower")
	_farm_button.disabled = not options.has(&"farm")


func _row_status_text() -> String:
	if _board_cards.is_empty():
		return "판정줄: 중앙 가로줄 3칸"
	if not _roulette_resolution.get("has_reward", false):
		return "중앙 줄 불일치 · 보상 없음"
	return "중앙 적중 · 완성 %d줄 · %s" % [int(_roulette_resolution.get("completed_line_count", 0)), _rank_name_by_id(_roulette_resolution.get("rank_id", &""))]


func _completed_cell_indices() -> Dictionary:
	var cells := {}
	for line in _roulette_resolution.get("completed_lines", []):
		for index in line:
			cells[index] = true
	return cells


func _token_symbol(card: Variant) -> String:
	match String(card.archetype_id):
		"shield_guard": return "방"
		"greatsword_warrior": return "검"
		"assassin": return "암"
		"spear_guard": return "창"
		"archer": return "궁"
		"cavalry": return "기"
		"priest": return "사"
		"mage": return "마"
		"flier": return "비"
		"giant": return "거"
		_: return "?"


func _display_name(card: Variant) -> String:
	match String(card.archetype_id):
		"shield_guard": return "방패병"
		"greatsword_warrior": return "대검전사"
		"assassin": return "암살자"
		"spear_guard": return "창병"
		"archer": return "궁병"
		"cavalry": return "기병"
		"priest": return "사제"
		"mage": return "마법사"
		"flier": return "비행병"
		"giant": return "거인"
		_: return str(card.archetype_id)


func _rank_name(card: Variant) -> String:
	return _rank_name_by_id(card.rank_id)


func _rank_name_by_id(rank_id: StringName) -> String:
	match String(rank_id):
		"common": return "일반"
		"elite": return "엘리트"
		"hero": return "영웅"
		"legendary": return "전설"
		_: return str(rank_id)


func _building_name(building_id: StringName) -> String:
	match building_id:
		&"tower": return "포탑"
		&"farm": return "농장"
		_: return str(building_id)


func _node_name(node_id: StringName) -> String:
	match node_id:
		&"front_a": return "전방 A"
		&"front_b": return "전방 B"
		&"rear": return "후방"
		_: return str(node_id)


func _node_status_name(status: StringName) -> String:
	match status:
		&"available": return "설치 가능"
		&"occupied": return "점유됨"
		&"locked": return "점령 중 잠김"
		&"enemy": return "적 소유"
		_: return "선택 불가"


func _lane_name(lane_id: StringName) -> String:
	match lane_id:
		&"top": return "상단"
		&"middle": return "중단"
		&"bottom": return "하단"
		_: return str(lane_id)
