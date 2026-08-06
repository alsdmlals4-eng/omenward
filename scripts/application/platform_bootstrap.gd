class_name PlatformBootstrap
extends RefCounted

const GameApplicationScript = preload("res://scripts/application/game_application.gd")
const SessionDriverScript = preload("res://scripts/application/session_driver.gd")
const SceneBinderScript = preload("res://scripts/presentation/scene_binder.gd")


func compose(host: Node, assigned_application: Variant = null) -> Dictionary:
	if host == null:
		return {}
	var application: Variant = assigned_application
	if application == null:
		application = GameApplicationScript.new()
	var driver: Variant = SessionDriverScript.new()
	driver.name = "SessionDriver"
	host.add_child(driver)
	driver.configure(application)
	var binder: Variant = SceneBinderScript.new()
	binder.name = "SceneBinder"
	host.add_child(binder)
	binder.configure(application, host)
	return {
		"application": application,
		"driver": driver,
		"binder": binder,
	}
