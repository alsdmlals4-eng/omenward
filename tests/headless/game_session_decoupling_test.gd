extends SceneTree

const GameApplicationScript = preload("res://scripts/application/game_application.gd")
const SessionDriverScript = preload("res://scripts/application/session_driver.gd")
const SceneBinderScript = preload("res://scripts/presentation/scene_binder.gd")
const PlatformBootstrapScript = preload("res://scripts/application/platform_bootstrap.gd")
const GameSessionScript = preload("res://scripts/application/game_session.gd")

var failures := PackedStringArray()
var created_runs: Array = []


class FakeStage:
	extends RefCounted
	var tutorial_stage := true


class FakeRegistry:
	extends RefCounted
	var errors := PackedStringArray()
	var tutorial := FakeStage.new()
	var regular := FakeStage.new()

	func _init() -> void:
		regular.tutorial_stage = false

	func load_bootstrap_catalog(_path: String) -> PackedStringArray:
		return errors.duplicate()

	func archetype_ids() -> Array[String]:
		return ["archer"]

	func stage_definition(stage_id: StringName) -> Variant:
		return tutorial if stage_id == &"tutorial_stage" else regular if stage_id == &"regular_stage" else null


class FakeValidator:
	extends RefCounted
	func validate_registry(_registry: Variant) -> PackedStringArray:
		return PackedStringArray()


class FakeDeterminism:
	extends RefCounted
	var seed := 1001
	func create_stage_manifest(stage_id: String, archetype_ids: Array[String]) -> Dictionary:
		return {"stage_id": stage_id, "archetype_ids": archetype_ids}


class FakeProgression:
	extends RefCounted
	var regular_unlocked := false
	func can_start(stage: Variant) -> bool:
		return stage != null and (bool(stage.tutorial_stage) or regular_unlocked)


class FakeRun:
	extends RefCounted
	var result_state: StringName = &""
	var starts := 0
	var advanced := 0.0
	func start(_stage: Variant, _seed: int) -> void:
		starts += 1
		result_state = &"running"
	func advance(delta: float) -> void:
		advanced += delta


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
	var advanced := 0.0
	var starts: Array[StringName] = []
	var retries := 0
	func bootstrap() -> PackedStringArray:
		bootstrap_ready.emit({"ready": true})
		return PackedStringArray()
	func start_stage(stage_id: StringName) -> bool:
		starts.append(stage_id)
		current_stage_id = stage_id
		stage_started.emit(stage_id, stage_run)
		return true
	func retry_stage() -> bool:
		retries += 1
		return true
	func advance(delta: float) -> void:
		advanced += delta


class BindTarget:
	extends Node
	var run: Variant
	var calls := 0
	func bind_run(value: Variant) -> void:
		run = value
		calls += 1


class FakeDriver:
	extends Node
	var requested: Array[StringName] = []
	func start_stage_deferred(stage_id: StringName) -> void:
		requested.append(stage_id)


class FakeBootstrapper:
	extends RefCounted
	var app: Variant
	var driver: Variant
	func _init(value: Variant, driver_value: Variant) -> void:
		app = value
		driver = driver_value
	func compose(_host: Node, _assigned_application: Variant = null) -> Dictionary:
		return {"application": app, "driver": driver, "binder": Node.new()}


func _init() -> void:
	call_deferred("run_checks")


func check(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)


func make_run(_progression: Variant) -> Variant:
	var run := FakeRun.new()
	created_runs.append(run)
	return run


func run_checks() -> void:
	test_application()
	await test_driver()
	test_binder()
	test_bootstrap()
	await test_facade()
	if failures.is_empty():
		print("GameSession decoupling checks passed")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)


func test_application() -> void:
	created_runs.clear()
	var progression := FakeProgression.new()
	var app: Variant = GameApplicationScript.new({
		"clock": &"clock",
		"registry": FakeRegistry.new(),
		"determinism": FakeDeterminism.new(),
		"validator": FakeValidator.new(),
		"progression": progression,
		"stage_run_factory": Callable(self, "make_run"),
	})
	var counts := {"ready": 0, "started": 0}
	app.bootstrap_ready.connect(func(_manifest: Variant) -> void: counts["ready"] += 1)
	app.stage_started.connect(func(_id: StringName, _run: Variant) -> void: counts["started"] += 1)
	check(app.bootstrap().is_empty() and counts["ready"] == 1, "bootstrap should succeed and emit once")
	check(created_runs.size() == 1, "bootstrap should create one run")
	check(app.start_stage(&"tutorial_stage") and counts["started"] == 1, "tutorial should start and emit once")
	app.advance(0.25)
	check(is_equal_approx(app.stage_run.advanced, 0.25), "advance should reach the run")
	check(app.retry_stage() and app.stage_run.starts == 2, "retry should restart current stage")
	check(not app.start_stage(&"regular_stage"), "locked regular stage should fail")
	progression.regular_unlocked = true
	check(app.start_stage(&"regular_stage"), "unlocked regular stage should start")
	var bad_registry := FakeRegistry.new()
	bad_registry.errors.append("catalog failure")
	var failed: Variant = GameApplicationScript.new({
		"clock": &"clock", "registry": bad_registry, "determinism": FakeDeterminism.new(),
		"validator": FakeValidator.new(), "progression": FakeProgression.new(),
		"stage_run_factory": Callable(self, "make_run"),
	})
	var failed_counts := {"signals": 0}
	failed.bootstrap_failed.connect(func(_errors: PackedStringArray) -> void: failed_counts["signals"] += 1)
	check(failed.bootstrap().size() == 1 and failed_counts["signals"] == 1 and failed.stage_run == null, "bootstrap failure should fail closed")


func test_driver() -> void:
	var app := FakeApplication.new()
	var driver: Variant = SessionDriverScript.new()
	driver.configure(app)
	driver._process(0.5)
	check(is_equal_approx(app.advanced, 0.5), "driver should advance application")
	get_root().add_child(driver)
	driver.start_stage_deferred(&"regular_stage")
	await process_frame
	check(app.starts == [&"regular_stage"], "driver should defer stage start")
	driver.queue_free()
	await process_frame


func test_binder() -> void:
	var root := Node.new()
	get_root().add_child(root)
	var host := Node.new()
	root.add_child(host)
	var battlefield := BindTarget.new()
	battlefield.name = "Battlefield"
	root.add_child(battlefield)
	var ui := Node.new()
	ui.name = "UI"
	root.add_child(ui)
	var hud := BindTarget.new()
	hud.name = "StageHud"
	ui.add_child(hud)
	var command_screen := BindTarget.new()
	command_screen.name = "RunCommandScreen"
	ui.add_child(command_screen)
	var app := FakeApplication.new()
	var binder: Variant = SceneBinderScript.new()
	host.add_child(binder)
	binder.configure(app, host)
	app.stage_started.emit(&"tutorial_stage", &"shared_run")
	binder.configure(app, host)
	app.stage_started.emit(&"tutorial_stage", &"second_run")
	check(
		battlefield.calls == 0 and hud.calls == 2 and command_screen.calls == 2,
		"binder should leave the hidden legacy battlefield unbound and bind the active HUD and Run Command screen once"
	)
	check(
		battlefield.run == null and hud.run == &"second_run" and command_screen.run == &"second_run",
		"binder should pass the same run only to active presentation targets"
	)
	root.free()


func test_bootstrap() -> void:
	var host := Node.new()
	get_root().add_child(host)
	var app := FakeApplication.new()
	var composition: Dictionary = PlatformBootstrapScript.new().compose(host, app)
	check(composition.get("application") == app, "bootstrap should preserve injected application")
	check(composition.get("driver") != null and composition.get("binder") != null, "bootstrap should create driver and binder")
	check(host.get_child_count() == 2, "bootstrap should add exactly two children")
	host.free()


func test_facade() -> void:
	var root := Node.new()
	get_root().add_child(root)
	var app := FakeApplication.new()
	var driver := FakeDriver.new()
	var session: Variant = GameSessionScript.new(FakeBootstrapper.new(app, driver))
	var counts := {"ready": 0, "started": 0}
	session.bootstrap_ready.connect(func(_manifest: Variant) -> void: counts["ready"] += 1)
	session.stage_started.connect(func(_id: StringName, _run: Variant) -> void: counts["started"] += 1)
	root.add_child(session)
	await process_frame
	check(counts["ready"] == 1 and driver.requested == [&"tutorial_stage"], "facade should bootstrap and schedule tutorial once")
	check(session.clock == app.clock and session.progression == app.progression, "facade should expose compatibility state")
	check(session.start_stage(&"regular_stage") and counts["started"] == 1, "facade should delegate and forward stage start")
	check(session.retry_stage() and app.retries == 1, "facade should delegate retry")
	var loose_binder: Node = session.binder
	root.free()
	driver.free()
	loose_binder.free()
	await process_frame
