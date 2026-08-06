extends SceneTree

const GameApplicationScript = preload("res://scripts/application/game_application.gd")
const SessionDriverScript = preload("res://scripts/application/session_driver.gd")
const SceneBinderScript = preload("res://scripts/presentation/scene_binder.gd")
const PlatformBootstrapScript = preload("res://scripts/application/platform_bootstrap.gd")
const GameSessionScript = preload("res://scripts/application/game_session.gd")

var _failures: PackedStringArray = []
var _created_stage_runs: Array = []


class FakeStage:
	extends RefCounted
	var tutorial_stage := true
	var stage_id: StringName = &"tutorial_stage"


class FakeRegistry:
	extends RefCounted
	var load_errors := PackedStringArray()
	var stages: Dictionary = {}

	func _init() -> void:
		var tutorial := FakeStage.new()
		stages[&"tutorial_stage"] = tutorial
		var regular := FakeStage.new()
		regular.tutorial_stage = false
		regular.stage_id = &"regular_stage"
		stages[&"regular_stage"] = regular

	func load_bootstrap_catalog(_path: String) -> PackedStringArray:
		return load_errors.duplicate()

	func archetype_ids() -> Array[String]:
		return ["archer", "guard"]

	func stage_definition(stage_id: StringName) -> Variant:
		return stages.get(stage_id)


class FakeValidator:
	extends RefCounted
	var errors := PackedStringArray()

	func validate_registry(_registry: Variant) -> PackedStringArray:
		return errors.duplicate()


class FakeDeterminism:
	extends RefCounted
	var seed := 1001

	func create_stage_manifest(stage_id: String, archetype_ids: Array[String]) -> Dictionary:
		return {
			"stage_id": stage_id,
			"seed": seed,
			"archetype_ids": archetype_ids.duplicate(),
		}


class FakeProgression:
	extends RefCounted
	var regular_unlocked := false

	func can_start(stage: Variant) -> bool:
		return stage != null and (bool(stage.tutorial_stage) or regular_unlocked)


class FakeStageRun:
	extends RefCounted
	const RUNNING := &"running"
	var result_state: StringName = &""
	var start_calls := 0
	var advance_total := 0.0
	var last_stage: Variant
	var last_seed := 0

	func start(stage: Variant, seed: int) -> void:
		start_calls += 1
		last_stage = stage
		last_seed = seed
		result_state = RUNNING

	func advance(delta: float) -> void:
		advance_total += delta


class FakeApplication:
	extends RefCounted
	signal bootstrap_ready(manifest: Variant)
	signal bootstrap_failed(errors: PackedStringArray)
	signal stage_started(stage_id: StringName, run: Variant)

	var clock: Variant = &"clock"
	var registry: Variant = &"registry"
	var determinism: Variant = &"determinism"
	var validator: Variant = &"validator"
	var progression: Variant = &"progression"
	var stage_run: Variant = &"run"
	var current_stage_id: StringName = &"tutorial_stage"
	var bootstrap_errors := PackedStringArray()
	var started_stages: Array[StringName] = []
	var advance_total := 0.0
	var retry_calls := 0

	func bootstrap() -> PackedStringArray:
		if bootstrap_errors.is_empty():
			bootstrap_ready.emit({"ready": true})
		else:
			bootstrap_failed.emit(bootstrap_errors)
		return bootstrap_errors.duplicate()

	func start_stage(stage_id: StringName) -> bool:
		started_stages.append(stage_id)
		current_stage_id = stage_id
		stage_started.emit(stage_id, stage_run)
		return true

	func retry_stage() -> bool:
		retry_calls += 1
		return true

	func advance(delta: float) -> void:
		advance_total += delta


class BindingTarget:
	extends Node
	var bound_run: Variant
	var bind_count := 0

	func bind_run(run: Variant) -> void:
		bound_run = run
		bind_count += 1


class FakeDriver:
	extends Node
	var requested_stages: Array[StringName] = []

	func start_stage_deferred(stage_id: StringName) -> void:
		requested_stages.append(stage_id)


class FakeBootstrapper:
	extends RefCounted
	var application: Variant
	var driver: Variant

	func _init(assigned_application: Variant, assigned_driver: Variant) -> void:
		application = assigned_application
		driver = assigned_driver

	func compose(_host: Node, _assigned_application: Variant = null) -> Dictionary:
		return {
			"application": application,
			"driver": driver,
			"binder": Node.new(),
		}


func _init() -> void:
	call_deferred("_run")


func _check(condition: bool, message: String) -> void:
	if not condition:
		_failures.append(message)


func _create_stage_run(_progression: Variant) -> Variant:
	var run := FakeStageRun.new()
	_created_stage_runs.append(run)
	return run


func _run() -> void:
	_test_game_application()
	await _test_session_driver()
	_test_scene_binder()
	_test_platform_bootstrap()
	await _test_game_session_facade()

	if _failures.is_empty():
		print("GameSession decoupling checks passed")
		quit(0)
		return
	for failure in _failures:
		push_error(failure)
	quit(1)


func _test_game_application() -> void:
	_created_stage_runs.clear()
	var registry := FakeRegistry.new()
	var validator := FakeValidator.new()
	var determinism := FakeDeterminism.new()
	var progression := FakeProgression.new()
	var application: Variant = GameApplicationScript.new({
		"clock": &"clock",
		"registry": registry,
		"determinism": determinism,
		"validator": validator,
		"progression": progression,
		"stage_run_factory": Callable(self, "_create_stage_run"),
	})
	var ready_count := 0
	var failure_count := 0
	var started_count := 0
	application.bootstrap_ready.connect(func(_manifest: Variant) -> void: ready_count += 1)
	application.bootstrap_failed.connect(func(_errors: PackedStringArray) -> void: failure_count += 1)
	application.stage_started.connect(func(_stage_id: StringName, _run: Variant) -> void: started_count += 1)

	var errors: PackedStringArray = application.bootstrap()
	_check(errors.is_empty(), "application bootstrap should succeed with valid fakes")
	_check(ready_count == 1 and failure_count == 0, "application should emit one bootstrap_ready signal")
	_check(_created_stage_runs.size() == 1, "application should create one stage run after bootstrap")
	_check(application.start_stage(&"tutorial_stage"), "tutorial stage should start")
	_check(started_count == 1, "application should emit one stage_started signal")
	_check(application.current_stage_id == &"tutorial_stage", "application should retain the current stage id")
	var run: Variant = application.stage_run
	_check(run.start_calls == 1 and run.last_seed == 1001, "stage run should receive the selected stage and deterministic seed")
	application.advance(0.25)
	_check(is_equal_approx(run.advance_total, 0.25), "application should delegate advance to the stage run")
	_check(application.retry_stage(), "retry should restart the current stage")
	_check(run.start_calls == 2 and started_count == 2, "retry should start and emit exactly once")
	_check(not application.start_stage(&"regular_stage"), "locked regular stage should be rejected")
	progression.regular_unlocked = true
	_check(application.start_stage(&"regular_stage"), "unlocked regular stage should start")

	var failed_registry := FakeRegistry.new()
	failed_registry.load_errors.append("catalog failure")
	var failed_application: Variant = GameApplicationScript.new({
		"clock": &"clock",
		"registry": failed_registry,
		"determinism": FakeDeterminism.new(),
		"validator": FakeValidator.new(),
		"progression": FakeProgression.new(),
		"stage_run_factory": Callable(self, "_create_stage_run"),
	})
	var failed_signal_count := 0
	failed_application.bootstrap_failed.connect(func(_errors: PackedStringArray) -> void: failed_signal_count += 1)
	var failed_errors: PackedStringArray = failed_application.bootstrap()
	_check(failed_errors.size() == 1 and failed_signal_count == 1, "bootstrap errors should emit once and be returned")
	_check(failed_application.stage_run == null, "failed bootstrap must not create a stage run")


func _test_session_driver() -> void:
	var application := FakeApplication.new()
	var driver: Variant = SessionDriverScript.new()
	driver.configure(application)
	driver._process(0.5)
	_check(is_equal_approx(application.advance_total, 0.5), "SessionDriver should delegate process delta")
	get_root().add_child(driver)
	driver.start_stage_deferred(&"regular_stage")
	await process_frame
	_check(application.started_stages == [&"regular_stage"], "SessionDriver should defer the requested stage start")
	driver.queue_free()
	await process_frame


func _test_scene_binder() -> void:
	var scene_root := Node.new()
	get_root().add_child(scene_root)
	var host := Node.new()
	host.name = "GameSession"
	scene_root.add_child(host)
	var battlefield := BindingTarget.new()
	battlefield.name = "Battlefield"
	scene_root.add_child(battlefield)
	var ui := Node.new()
	ui.name = "UI"
	scene_root.add_child(ui)
	var hud := BindingTarget.new()
	hud.name = "StageHud"
	ui.add_child(hud)
	var application := FakeApplication.new()
	var binder: Variant = SceneBinderScript.new()
	host.add_child(binder)
	binder.configure(application, host)
	application.stage_started.emit(&"tutorial_stage", &"shared_run")
	_check(battlefield.bound_run == &"shared_run" and battlefield.bind_count == 1, "SceneBinder should bind Battlefield once")
	_check(hud.bound_run == &"shared_run" and hud.bind_count == 1, "SceneBinder should bind StageHud once")
	binder.configure(application, host)
	application.stage_started.emit(&"tutorial_stage", &"second_run")
	_check(battlefield.bind_count == 2 and hud.bind_count == 2, "SceneBinder reconfigure must not duplicate signal connections")
	scene_root.queue_free()


func _test_platform_bootstrap() -> void:
	var host := Node.new()
	get_root().add_child(host)
	var application := FakeApplication.new()
	var bootstrapper: Variant = PlatformBootstrapScript.new()
	var composition: Dictionary = bootstrapper.compose(host, application)
	_check(composition.get("application") == application, "PlatformBootstrap should preserve an injected application")
	_check(composition.get("driver") != null and composition.get("binder") != null, "PlatformBootstrap should create driver and binder")
	_check(host.get_child_count() == 2, "PlatformBootstrap should add exactly two composition children")
	host.queue_free()


func _test_game_session_facade() -> void:
	var scene_root := Node.new()
	get_root().add_child(scene_root)
	var application := FakeApplication.new()
	var driver := FakeDriver.new()
	var bootstrapper := FakeBootstrapper.new(application, driver)
	var session: Variant = GameSessionScript.new(bootstrapper)
	var ready_count := 0
	var started_count := 0
	session.bootstrap_ready.connect(func(_manifest: Variant) -> void: ready_count += 1)
	session.stage_started.connect(func(_stage_id: StringName, _run: Variant) -> void: started_count += 1)
	scene_root.add_child(session)
	await process_frame
	_check(ready_count == 1, "GameSession should forward bootstrap_ready exactly once")
	_check(driver.requested_stages == [&"tutorial_stage"], "GameSession should schedule the default tutorial stage after bootstrap")
	_check(session.clock == application.clock, "GameSession should expose the application clock")
	_check(session.progression == application.progression, "GameSession should expose application progression")
	_check(session.current_stage_id == application.current_stage_id, "GameSession should expose the current stage id")
	_check(session.start_stage(&"regular_stage"), "GameSession should delegate start_stage")
	_check(started_count == 1, "GameSession should forward stage_started exactly once")
	_check(session.retry_stage() and application.retry_calls == 1, "GameSession should delegate retry_stage")
	scene_root.queue_free()
	await process_frame
