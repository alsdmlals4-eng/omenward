class_name SaveAdapter
extends RefCounted


func load_payload(_slot_id: StringName) -> Dictionary:
	return {"ok": false, "error": "not_implemented"}


func write_payload_atomic(_slot_id: StringName, _payload: Dictionary) -> Dictionary:
	return {"ok": false, "error": "not_implemented"}
