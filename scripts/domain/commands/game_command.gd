class_name GameCommand
extends RefCounted

var action_id: StringName = &""
var payload: Dictionary = {}


func _init(assigned_action_id: StringName = &"", assigned_payload: Dictionary = {}) -> void:
	action_id = assigned_action_id
	payload = assigned_payload.duplicate(true)


func is_valid() -> bool:
	return action_id != &"" and _is_platform_neutral(payload)


func to_dictionary() -> Dictionary:
	return {
		"action_id": str(action_id),
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
