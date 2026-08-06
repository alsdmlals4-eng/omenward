class_name PlatformBootstrap
extends RefCounted

const GameApplicationScript = preload("res://scripts/application/game_application.gd")
const SessionDriverScript = preload("res://scripts/application/session_driver.gd")
const SceneBinderScript = preload("res://scripts/presentation/scene_binder.gd")
const DRIVER_META := &"_omenward_session_driver"
const BINDER_META := &"_omenward_scene_binder"


func compose(host: Node, assigned_application: Variant = null) -> Dictionary:
	if host == null:
		return {}
	var application: Variant = assigned_application
	if application == null:
		application = GameApplicationScript.new()
	var driver: Variant = host.get_meta(DRIVER_META) if host.has_meta(DRIVER_META) else null
	if not is_instance_valid(driver):
		driver = SessionDriverScript.new()
		driver.name = "SessionDriver"
		host.add_child(driver)
		host.set_meta(DRIVER_META, driver)
	driver.configure(application)
	var binder: Variant = host.get_meta(BINDER_META) if host.has_meta(BINDER_META) else null
	if not is_instance_valid(binder):
		binder = SceneBinderScript.new()
		binder.name = "SceneBinder"
		host.add_child(binder)
		host.set_meta(BINDER_META, binder)
	binder.configure(application, host)
	return {
		"application": application,
		"driver": driver,
		"binder": binder,
	}
