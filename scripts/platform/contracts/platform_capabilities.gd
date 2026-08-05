class_name PlatformCapabilities
extends RefCounted

var _capabilities: Dictionary = {}


func _init(capability_ids: PackedStringArray = PackedStringArray()) -> void:
	for capability_id in capability_ids:
		_capabilities[StringName(capability_id)] = true


func has_capability(capability_id: StringName) -> bool:
	return _capabilities.has(capability_id)


func all_capabilities() -> PackedStringArray:
	var result := PackedStringArray()
	for capability_id in _capabilities:
		result.append(str(capability_id))
	result.sort()
	return result
