class_name InputAdapter
extends RefCounted


func poll_commands() -> Array[GameCommand]:
	var commands: Array[GameCommand] = []
	return commands


func active_device() -> StringName:
	return &"unknown"
