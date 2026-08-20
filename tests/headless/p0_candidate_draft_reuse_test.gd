extends SceneTree

const ENGINE_PATH := "res://vendor/base-reuse/candidate_draft_weight_engine.gd"
const ADAPTER_PATH := "res://vendor/base-reuse/omenward_candidate_draft_adapter.gd"


func _init() -> void:
	var failures := PackedStringArray()
	_expect(ResourceLoader.exists(ENGINE_PATH, "Script"), "candidate draft engine must be vendored", failures)
	_expect(ResourceLoader.exists(ADAPTER_PATH, "Script"), "Omenward candidate adapter must exist", failures)
	if ResourceLoader.exists(ENGINE_PATH, "Script") and ResourceLoader.exists(ADAPTER_PATH, "Script"):
		var engine: Variant = load(ENGINE_PATH).new()
		var pool := [
			{"id": "barracks", "weight": 5},
			{"id": "stable", "weight": 3},
			{"id": "ritual", "weight": 2},
		]
		var first: Dictionary = engine.generate(pool, 3, 4242)
		var second: Dictionary = engine.generate(pool, 3, 4242)
		_expect(first.ok, "integer-weight pool must generate candidates", failures)
		_expect(JSON.stringify(first.candidates) == JSON.stringify(second.candidates), "same seed must reproduce the same candidate order", failures)
		var ids := PackedStringArray()
		for candidate: Dictionary in first.candidates:
			ids.append(str(candidate.get("id", "")))
		_expect(ids.size() == 3 and ids[0] != ids[1] and ids[1] != ids[2] and ids[0] != ids[2], "FORBID duplicate policy must keep three distinct entries", failures)

		var adapter: Variant = load(ADAPTER_PATH).new()
		var valid: Dictionary = adapter.generate_token_source_candidates(pool, 3, 4242)
		_expect(valid.ok and valid.candidates.size() == 3, "Omenward adapter must produce exactly three token-source candidates", failures)
		var fractional: Dictionary = adapter.generate_token_source_candidates([{"id": "bad", "weight": 1.5}], 3, 1)
		_expect(not fractional.ok and str(fractional.reason) == "FRACTIONAL_WEIGHT_FORBIDDEN", "Omenward adapter must reject fractional roulette weights", failures)
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("P0 candidate draft reuse checks passed")
		quit(0)
	else:
		printerr("P0 candidate draft reuse failures:\n%s" % "\n".join(failures))
		quit(1)
