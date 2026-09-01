extends Node

# QA 전용: 실제 Main/RunCommandScreen/BattleFocus consumer 안에서 역할별 승인·후보
# 스프라이트를 함께 읽기 위한 재현 가능한 편성이다. 플레이어 진입 경로에는 포함하지 않는다.
const FRONT_ID := &"front"
const SHOWCASE_UNITS := [
	{&"team": &"lumern", &"role": &"spear_guard", &"position": 18.0},
	{&"team": &"lumern", &"role": &"archer", &"position": 30.0},
	{&"team": &"lumern", &"role": &"mage", &"position": 42.0},
	{&"team": &"veil", &"role": &"spear_guard", &"position": 58.0},
	{&"team": &"veil", &"role": &"archer", &"position": 70.0},
	{&"team": &"veil", &"role": &"mage", &"position": 82.0},
]


func _ready() -> void:
	call_deferred("_activate_showcase")


func _activate_showcase() -> void:
	var session := $Main/GameSession as GameSession
	if session == null or not session.is_bootstrap_ready():
		push_error("BattleFocus role profile fixture requires a bootstrapped GameSession")
		return
	if not session.begin_tutorial():
		push_error("BattleFocus role profile fixture could not start tutorial stage")
		return
	await get_tree().process_frame
	var run: Variant = session.stage_run
	if run == null or not run.begin_battle():
		push_error("BattleFocus role profile fixture could not enter BATTLE")
		return
	for entry in SHOWCASE_UNITS:
		_spawn_showcase_unit(run, entry)
	# SessionDriver만 멈춰 QA 편성의 역할별 스프라이트가 전투 처리로 사라지지 않게 한다.
	# BattleFocus 자체의 redraw는 계속 동작하며, 실제 런타임 consumer를 그대로 사용한다.
	if session.driver != null:
		session.driver.set_process(false)
	var command_screen := $Main/UI/RunCommandScreen as RunCommandScreen
	if command_screen != null:
		command_screen.set_active_tab(&"front")


func _spawn_showcase_unit(run: Variant, entry: Dictionary) -> void:
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = entry.get(&"role", &"") as StringName
	spawn.owner_team_id = entry.get(&"team", &"") as StringName
	spawn.visual_faction_id = spawn.owner_team_id
	spawn.lane_id = FRONT_ID
	var unit: Variant = run.battle.spawn_unit(spawn)
	if unit == null:
		push_error("BattleFocus role profile fixture failed to spawn %s" % spawn.archetype_id)
		return
	unit.lane_position = float(entry.get(&"position", 50.0))
