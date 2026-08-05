class_name GameEvent
extends RefCounted

var event_id: StringName = &""
var _payload: Dictionary = {}
var payload: Dictionary:
	get:
		return _payload.duplicate(true)
var _payload_is_valid := true


func _init(assigned_event_id: StringName = &"", assigned_payload: Dictionary = {}) -> void:
	event_id = assigned_event_id
	_payload_is_valid = _is_platform_neutral(assigned_payload)
	_payload = assigned_payload.duplicate(true) if _payload_is_valid else {}


func is_valid() -> bool:
	return event_id != &"" and _payload_is_valid


func to_dictionary() -> Dictionary:
	return {
		"event_id": str(event_id),
		"payload": _payload.duplicate(true),
	}


static func _is_platform_neutral(value: Variant) -> bool:
	return _is_platform_neutral_recursive(value, [])


static func _is_platform_neutral_recursive(value: Variant, active_containers: Array) -> bool:
	match typeof(value):
		TYPE_OBJECT, TYPE_CALLABLE, TYPE_SIGNAL, TYPE_RID:
			return false
		TYPE_ARRAY:
			if _contains_same_container(active_containers, value):
				return false
			active_containers.append(value)
			for item in value:
				if not _is_platform_neutral_recursive(item, active_containers):
					active_containers.pop_back()
					return false
			active_containers.pop_back()
		TYPE_DICTIONARY:
			if _contains_same_container(active_containers, value):
				return false
			active_containers.append(value)
			for key in value:
				if not _is_platform_neutral_recursive(key, active_containers):
					active_containers.pop_back()
					return false
				if not _is_platform_neutral_recursive(value[key], active_containers):
					active_containers.pop_back()
					return false
			active_containers.pop_back()
	return true


static func _contains_same_container(active_containers: Array, candidate: Variant) -> bool:
	for active_container in active_containers:
		if is_same(active_container, candidate):
			return true
	return false
