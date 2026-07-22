class_name StageHud
extends Control

@onready var _resource_label: Label = $ResourceLabel
@onready var _wave_label: Label = $WaveLabel
@onready var _omen_label: Label = $OmenLabel
@onready var _cards_label: Label = $CardsLabel
@onready var _result_label: Label = $ResultLabel
@onready var _retry_button: Button = $RetryButton

var run: Variant
var _spin_index := 0


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_update_display()


func _process(_delta: float) -> void:
	_update_display()


func _on_spin_pressed() -> void:
	if run == null:
		return
	_spin_index += 1
	run.spin_roulette({"seed": _spin_index})
	_update_display()


func _on_barracks_pressed() -> void:
	if run != null:
		run.construct_home(&"barracks")
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
	if run != null:
		run.deploy_next_roulette_reward(lane_id)
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
	var result: Variant = run.last_roulette_result
	var board_text := "-"
	var outcome_text := "none"
	if result != null:
		board_text = ",".join(result.board.map(func(symbol: StringName) -> String: return str(symbol)))
		outcome_text = "%s %s lines=%d gold=%d" % [str(result.outcome_type), str(result.rank_id), result.completed_line_count, result.gold_reward]
		if not result.accepted and result.failure_reason != &"":
			outcome_text = "blocked: %s" % str(result.failure_reason)
	_cards_label.text = "Board [%s] | %s | Pending %d" % [board_text, outcome_text, run.pending_roulette_rewards.size()]
	_result_label.visible = run.result_state != run.RUNNING
	_result_label.text = "Stage %s" % str(run.result_state).capitalize()
	_retry_button.visible = run.result_state != run.RUNNING
