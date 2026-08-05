class_name GameEvent
extends RefCounted

var event_id: StringName = &""
var payload: Dictionary = {}


func _init(assigned_event_id: StringName = &"", assigned_payload: Dictionary = {}) -> void:
	event_id = assigned_event_id
	payload = assigned_payload.duplicate(true)


func is_valid() -> bool:
	return event_id != &"" and _is_platform_neutral(payload)


func to_dictionary() -> Dictionary:
	return {
		"event_id": str(event_id),
		"payload": payload.duplicate(true),
	}


static func _is_platform_neutral(value: Variant) -> bool:
	match typeof(value):
		TYPE_OBJECT, TYPE_CALLABLE, TYPE_SIGNAL, TYPE_RID:
			return false
		TYPE_ARRAY:
			for item in value:
				if not _is_platform_neutral(item):
					return false
		TYPE_DICTIONARY:
			for key in value:
				if not _is_platform_neutral(key) or not _is_platform_neutral(value[key]):
					return false
	return true
