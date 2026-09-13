extends SceneTree

var checks := 0
var failures := 0

func check(ok: bool, message: String) -> void:
	checks += 1
	if not ok:
		failures += 1
		push_error(message)

func write_fixture(path: String, text: String) -> void:
	var file := FileAccess.open(path, FileAccess.WRITE)
	check(file != null, "Fixture file opens")
	if file:
		file.store_string(text)
		file.close()

func _initialize() -> void:
	var source := "res://scripts/replan/front_save.gd"
	check(ResourceLoader.exists(source), "P01 missing verified save transport")
	if not ResourceLoader.exists(source):
		quit(1)
		return
	var storage = load(source)
	var model = load("res://scripts/replan/front_run.gd").new()
	var folder := "user://save-test-%d-%d" % [OS.get_process_id(), Time.get_ticks_usec()]
	check(DirAccess.make_dir_recursive_absolute(folder) == OK, "Create isolated fixture directory")
	var path := folder + "/run.json"
	var initial: Dictionary = model.snapshot()
	check(storage.write_verified(path, initial).ok, "First save commits")
	check(storage.read_verified(path).state.gold == 120, "Disk read restores initial gold")
	model.gold = 80
	check(storage.write_verified(path, model.snapshot()).ok, "Second save commits")
	check(storage.read_verified(path).state.gold == 80, "Current save is newest")
	check(storage.read_verified(path + ".bak").state.gold == 120, "Backup retains preceding valid save")
	var digest := FileAccess.get_sha256(path)
	var invalid: Dictionary = model.snapshot()
	invalid.gold = -10
	check(not storage.write_verified(path, invalid).ok, "Invalid state cannot replace disk")
	check(FileAccess.get_sha256(path) == digest, "Rejected input leaves bytes unchanged")
	write_fixture(path, "{broken")
	var recovered: Dictionary = storage.read_verified(path)
	check(recovered.ok and recovered.recovered and recovered.state.gold == 120, "Corrupt primary falls back to valid backup")
	check(FileAccess.get_file_as_string(path) == "{broken", "Read-only recovery preserves damaged evidence")
	check(storage.write_verified(path, initial).ok, "Can save again after verified backup recovery")
	check(storage.read_verified(path).state.gold == 120, "Recovered continuation commits normally")
	var blocked := folder + "/blocked.json"
	check(storage.write_verified(blocked, initial).ok, "Prepare rename failure fixture")
	check(DirAccess.make_dir_absolute(blocked + ".bak") == OK, "Directory blocks backup promotion")
	check(not storage.write_verified(blocked, model.snapshot()).ok, "Backup failure prevents primary replacement")
	check(storage.read_verified(blocked).state.gold == 120, "Failed transaction preserves last primary")
	var future: Dictionary = initial.duplicate(true)
	future.version = 999
	write_fixture(path, JSON.stringify(future))
	digest = FileAccess.get_sha256(path)
	check(not storage.read_verified(path).ok, "Future save must not silently fall back to older run")
	check(not storage.write_verified(path, initial).ok, "Older code must not overwrite future save")
	check(FileAccess.get_sha256(path) == digest, "Future bytes preserved")
	var future_envelope := {"schema_version": 7, "ruleset_id": "fixed30-v1", "state": initial}
	write_fixture(path, JSON.stringify(future_envelope))
	digest = FileAccess.get_sha256(path)
	check(not storage.read_verified(path).ok, "Future envelope cannot fall back to legacy backup")
	check(not storage.write_verified(path, initial).ok, "Future envelope cannot be replaced by legacy writer")
	check(FileAccess.get_sha256(path) == digest, "Future envelope preserved at original path")
	var mixed_format: Dictionary = initial.duplicate(true)
	mixed_format.schema_version = 7
	check(not storage.write_verified(folder + "/mixed.json", mixed_format).ok, "Unknown schema input cannot masquerade as v6")
	var interrupted := folder + "/interrupted.json"
	write_fixture(interrupted + ".bak", JSON.stringify(initial))
	check(storage.read_verified(interrupted).ok, "Missing primary can recover valid backup")
	write_fixture(interrupted + ".bak", "[]")
	check(not storage.read_verified(interrupted).ok, "Invalid backup cannot become live state")
	check(not storage.read_verified(folder + "/missing.json").ok, "Missing save returns failure")
	for mode in ["missing", "valid", "corrupt"]:
		var guarded: String = folder + "/future-backup-" + mode + ".json"
		if mode == "valid":
			write_fixture(guarded, JSON.stringify(initial))
		elif mode == "corrupt":
			write_fixture(guarded, "{broken")
		write_fixture(guarded + ".bak", JSON.stringify(future_envelope))
		var backup_hash := FileAccess.get_sha256(guarded + ".bak")
		check(not storage.write_verified(guarded, initial).ok, "Future backup blocks older writer: " + mode)
		check(FileAccess.get_sha256(guarded + ".bak") == backup_hash, "Future backup bytes survive: " + mode)
	print("REPLAN_SAVE_TEST: %d checks, %d failures; fixtures retained at %s" % [checks, failures, ProjectSettings.globalize_path(folder)])
	quit(1 if failures else 0)
