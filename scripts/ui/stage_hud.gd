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
var _spin_index := 0
var _roulette_feedback_text := "징조를 읽고 전력 표식을 회전하세요."


func _ready() -> void:
	_refresh_roulette_dock()


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_pending_cards.clear()
	_roulette_feedback_text = "징조를 읽고 전력 표식을 회전하세요."
	_update_display()
	_refresh_roulette_dock()


func _process(_delta: float) -> void:
	_update_display()
	_refresh_roulette_dock()


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
	_pending_cards = run.spin_roulette({"seed": _spin_index})
	_roulette_feedback_text = "3×3 전력 표식 확정. 첫 결과를 배치할 라인을 선택하세요."
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
	for index in _roulette_cells.size():
		var cell := _roulette_cells[index]
		if index < _pending_cards.size():
			var card: Variant = _pending_cards[index]
			cell.text = _token_symbol(card)
			cell.tooltip_text = "%s · %s" % [_display_name(card), _rank_name(card)]
			cell.modulate = Color(0.94, 0.82, 0.43, 1.0) if index == 0 else Color(0.83, 0.9, 0.98, 1.0)
		else:
			cell.text = "·"
			cell.tooltip_text = "비어 있음"
			cell.modulate = Color(0.48, 0.55, 0.62, 1.0)


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
	match String(card.rank_id):
		"common": return "일반"
		"elite": return "엘리트"
		"hero": return "영웅"
		"legendary": return "전설"
		_: return str(card.rank_id)


func _lane_name(lane_id: StringName) -> String:
	match lane_id:
		&"top": return "상단"
		&"middle": return "중단"
		&"bottom": return "하단"
		_: return str(lane_id)
