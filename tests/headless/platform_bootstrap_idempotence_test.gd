extends SceneTree

const PlatformBootstrapScript = preload("res://scripts/application/platform_bootstrap.gd")


class FakeApplication:
	extends RefCounted
	signal stage_started(stage_id: StringName, run: Variant)
	func advance(_delta: float) -> void:
		pass
	func start_stage(_stage_id: StringName) -> bool:
		return true


func _init() -> void:
	var host := Node.new()
	get_root().add_child(host)
	var application := FakeApplication.new()
	var bootstrapper: Variant = PlatformBootstrapScript.new()
	var first: Dictionary = bootstrapper.compose(host, application)
	var second: Dictionary = bootstrapper.compose(host, application)
	var ok: bool = (
		host.get_child_count() == 2
		and first.get("driver") == second.get("driver")
		and first.get("binder") == second.get("binder")
	)
	host.free()
	if ok:
		print("PlatformBootstrap idempotence checks passed")
		quit(0)
		return
	printerr("PlatformBootstrap created duplicate composition children")
	quit(1)
