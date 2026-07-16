class_name StageHud
extends Control

@onready var _resource_label: Label = $ResourceLabel
@onready var _wave_label: Label = $WaveLabel
@onready var _omen_label: Label = $OmenLabel
@onready var _cards_label: Label = $CardsLabel
@onready var _result_label: Label = $ResultLabel
@onready var _retry_button: Button = $RetryButton

var run: Variant
var _pending_cards: Array = []
var _spin_index := 0


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_pending_cards.clear()
	_update_display()


func _process(_delta: float) -> void:
	_update_display()


func _on_spin_pressed() -> void:
	if run == null:
		return
	_spin_index += 1
	_pending_cards = run.spin_roulette({"seed": _spin_index})
	_update_display()


func _on_tower_pressed() -> void:
	if run != null:
		run.construct_home(&"tower")
	_update_display()


func _on_farm_pressed() -> void:
	if run != null:
		run.construct_home(&"farm")
	_update_display()


func _on_deploy_pressed(lane_id: StringName) -> void:
	if run == null or _pending_cards.is_empty():
		return
	var card: Variant = _pending_cards.front()
	if run.deploy_card(card, lane_id):
		_pending_cards.pop_front()
	_update_display()


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
	_cards_label.text = "Cards: %s" % ", ".join(_pending_cards.map(func(card: Variant) -> String: return str(card.archetype_id)))
	_result_label.visible = run.result_state != run.RUNNING
	_result_label.text = "Stage %s" % str(run.result_state).capitalize()
	_retry_button.visible = run.result_state != run.RUNNING
