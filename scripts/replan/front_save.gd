extends RefCounted
## File transport only. The run model remains the sole state validator.

const Model = preload("res://scripts/replan/front_run.gd")
const MAX_BYTES := 4 * 1024 * 1024

static func _failure(reason: String, recoverable: bool = false) -> Dictionary:
	return {"ok": false, "reason": reason, "state": {}, "recovered": false, "recoverable": recoverable}

static func _unsupported(value: Variant) -> bool:
	return _unsupported_state(value) or (value is Dictionary and _unsupported_state(value.get("map_entry")))

static func _unsupported_state(value: Variant) -> bool:
	if not value is Dictionary:
		return false
	# Envelope formats remain unsupported; known v7 is a flat model snapshot.
	if value.has("schema_version"):
		return true
	var version: Variant = value.get("version")
	if value.has("ruleset_id") and (version != 7 or value.ruleset_id != Model.FIXED_RULESET):
		return true
	if value.has("capture_rules") and value.capture_rules not in ["legacy", "timed_v1"]:
		return true
	if value.has("facility_rules") and value.facility_rules not in ["legacy", "logistics_v1", "slots_v1"]:
		return true
	if value.has("birth_rules") and value.birth_rules not in ["legacy", "birth_v1", "birth_v2"]:
		return true
	return (version is float or version is int) and version > 7

static func _read(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return _failure("MISSING", true)
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return _failure("READ_FAILED")
	if file.get_length() > MAX_BYTES:
		file.close()
		return _failure("TOO_LARGE")
	var text := file.get_as_text()
	var error := file.get_error()
	file.close()
	if error != OK and error != ERR_FILE_EOF:
		return _failure("READ_FAILED")
	var parser := JSON.new()
	if parser.parse(text) != OK:
		return _failure("CORRUPT_JSON", true)
	var value: Variant = parser.data
	if _unsupported(value):
		return _failure("UNSUPPORTED_VERSION")
	var probe = Model.new()
	if not probe.restore(value):
		return _failure("INVALID_STATE", true)
	return {"ok": true, "reason": "OK", "state": value, "recovered": false, "recoverable": false}

static func read_verified(path: String) -> Dictionary:
	var primary := _read(path)
	if primary.ok or not primary.recoverable:
		return primary
	var backup := _read(path + ".bak")
	if not backup.ok:
		return _failure("NO_VALID_SAVE: " + primary.reason + "/" + backup.reason)
	backup.recovered = true
	backup.reason = "BACKUP_RECOVERED"
	return backup

static func write_verified(path: String, state: Dictionary) -> Dictionary:
	# Reject before even opening a temp file; never mutate caller state.
	if _unsupported(state):
		return _failure("UNSUPPORTED_VERSION")
	var probe = Model.new()
	if not probe.restore(state.duplicate(true)):
		return _failure("INVALID_STATE")
	var primary := _read(path)
	if not primary.ok and not primary.recoverable:
		return primary
	var backup := _read(path + ".bak")
	if not backup.ok and not backup.recoverable:
		return _failure("BACKUP_PROTECTED: " + backup.reason)
	var text := JSON.stringify(state)
	if text.to_utf8_buffer().size() > MAX_BYTES:
		return _failure("TOO_LARGE")
	var temp := path + ".tmp"
	var file := FileAccess.open(temp, FileAccess.WRITE)
	if file == null:
		return _failure("TEMP_OPEN_FAILED")
	file.store_string(text)
	file.flush()
	var error := file.get_error()
	file.close()
	if error != OK:
		return _failure("TEMP_WRITE_FAILED")
	var verified := _read(temp)
	if not verified.ok or FileAccess.get_sha256(temp) != text.sha256_text():
		return _failure("TEMP_VERIFY_FAILED")
	if primary.ok:
		var backup_temp := path + ".bak.tmp"
		if DirAccess.copy_absolute(path, backup_temp) != OK:
			return _failure("BACKUP_COPY_FAILED")
		if not _read(backup_temp).ok or FileAccess.get_sha256(backup_temp) != FileAccess.get_sha256(path):
			return _failure("BACKUP_VERIFY_FAILED")
		if DirAccess.rename_absolute(backup_temp, path + ".bak") != OK:
			return _failure("BACKUP_REPLACE_FAILED")
	elif FileAccess.file_exists(path):
		# A corrupt primary is evidence, not disposable. Preserve before replacement.
		var retained := path + ".rejected-%d-%d" % [OS.get_process_id(), Time.get_ticks_usec()]
		if FileAccess.file_exists(retained) or DirAccess.rename_absolute(path, retained) != OK:
			return _failure("CORRUPT_PRESERVE_FAILED")
		if DirAccess.rename_absolute(temp, path) != OK:
			if DirAccess.rename_absolute(retained, path) != OK:
				return _failure("REPLACE_FAILED_EVIDENCE_AT: " + retained)
			return _failure("PRIMARY_REPLACE_FAILED")
		verified.reason = "SAVED_CORRUPT_PRESERVED: " + retained
		return verified
	if DirAccess.rename_absolute(temp, path) != OK:
		return _failure("PRIMARY_REPLACE_FAILED")
	verified.reason = "SAVED"
	return verified
