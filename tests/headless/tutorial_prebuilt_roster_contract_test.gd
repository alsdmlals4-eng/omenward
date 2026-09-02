# 튜토리얼은 건물을 전장에 배치하지 않되, 룰렛에서 병력이 나올 수 있는 사전 편성 하나를 보여 준다.
extends SceneTree

const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	var run := StageRun.new(StageProgression.new())
	run.start(ResourceLoader.load(TUTORIAL_STAGE_PATH), 31103)
	var roster: Array = run.building_roster_snapshot()
	_expect(not roster.is_empty(), "tutorial exposes the global building roster", failures)
	if not roster.is_empty():
		_expect(roster[0].get("building_id", "") == "barracks", "tutorial starts with one prebuilt barracks in roster slot one", failures)
		_expect(roster[0].get("state", "") == "active", "tutorial prebuilt barracks is active", failures)
	_expect(not run.buildings.roster_mutation_allowed(), "tutorial retains its no-building-mutation teaching boundary", failures)
	_expect(not run.install_building(&"farm"), "tutorial does not permit an extra building install", failures)
	var sources: Array = run.buildings.roulette_token_sources()
	_expect(sources.size() == 1 and sources[0].get("symbol_id", "") == "warrior", "tutorial prebuilt barracks supplies a visible warrior roulette source", failures)
	_expect(run.begin_roulette_session({"seed": 2}), "tutorial can open its first 3x3 roulette session", failures)
	var board: Array = run.roulette_session.get("board", [])
	_expect(board.has(&"warrior"), "tutorial roulette board includes a player unit symbol", failures)
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Tutorial prebuilt roster contracts passed")
		quit(0)
	else:
		printerr("Tutorial prebuilt roster contract failures:\n%s" % "\n".join(failures))
		quit(1)
