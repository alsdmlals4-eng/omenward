extends SceneTree

const GameCommandScript = preload("res://scripts/domain/commands/game_command.gd")
const GameEventScript = preload("res://scripts/domain/events/game_event.gd")
const InputAdapterScript = preload("res://scripts/platform/contracts/input_adapter.gd")
const DisplayAdapterScript = preload("res://scripts/platform/contracts/display_adapter.gd")
const SaveAdapterScript = preload("res://scripts/platform/contracts/save_adapter.gd")
const LifecycleAdapterScript = preload("res://scripts/platform/contracts/lifecycle_adapter.gd")
const PerformanceAdapterScript = preload("res://scripts/platform/contracts/performance_adapter.gd")
const StoreAdapterScript = preload("res://scripts/platform/contracts/store_adapter.gd")
const PlatformCapabilitiesScript = preload("res://scripts/platform/contracts/platform_capabilities.gd")


func _init() -> void:
	var failures := PackedStringArray()
	_test_game_command(failures)
	_test_game_event(failures)
	_test_input_contract(failures)
	_test_display_contract(failures)
	_test_save_contract(failures)
	_test_lifecycle_contract(failures)
	_test_performance_contract(failures)
	_test_store_contract(failures)
	_test_capabilities_contract(failures)
	_finish(failures)


func _test_game_command(failures: PackedStringArray) -> void:
	var original_payload := {"slot": 2, "path": [&"left", &"down"]}
	var command: Variant = GameCommandScript.new(&"roulette_move", original_payload)
	original_payload["slot"] = 9
	_expect(command.action_id == &"roulette_move", "command keeps semantic action id", failures)
	_expect(command.payload["slot"] == 2, "command deep-copies constructor payload", failures)
	var exposed_payload: Dictionary = command.payload
	exposed_payload["slot"] = 7
	_expect(command.payload["slot"] == 2, "command payload getter returns an isolated snapshot", failures)
	_expect(command.is_valid(), "semantic command with plain payload is valid", failures)
	_expect(command.to_dictionary()["action_id"] == "roulette_move", "command dictionary normalizes action id", failures)
	_expect(not GameCommandScript.new().is_valid(), "empty command id is invalid", failures)
	_expect(
		not GameCommandScript.new(&"bad", {"nested": [{"object": RefCounted.new()}]}).is_valid(),
		"command rejects nested Object payload values",
		failures,
	)
	var cyclic_payload := {}
	cyclic_payload["self"] = cyclic_payload
	_expect(
		not GameCommandScript.new(&"cycle", cyclic_payload).is_valid(),
		"command rejects cyclic payload containers without recursive duplication",
		failures,
	)


func _test_game_event(failures: PackedStringArray) -> void:
	var original_payload := {"stage": 3, "tags": PackedStringArray(["regular"])}
	var event: Variant = GameEventScript.new(&"stage_started", original_payload)
	original_payload["stage"] = 8
	_expect(event.event_id == &"stage_started", "event keeps semantic event id", failures)
	_expect(event.payload["stage"] == 3, "event deep-copies constructor payload", failures)
	var exposed_payload: Dictionary = event.payload
	exposed_payload["stage"] = 11
	_expect(event.payload["stage"] == 3, "event payload getter returns an isolated snapshot", failures)
	_expect(event.is_valid(), "semantic event with plain payload is valid", failures)
	_expect(event.to_dictionary()["event_id"] == "stage_started", "event dictionary normalizes event id", failures)
	_expect(not GameEventScript.new().is_valid(), "empty event id is invalid", failures)
	_expect(
		not GameEventScript.new(&"bad", {"callable": func() -> void: pass}).is_valid(),
		"event rejects Callable payload values",
		failures,
	)
	var cyclic_payload := {}
	cyclic_payload["self"] = cyclic_payload
	_expect(
		not GameEventScript.new(&"cycle", cyclic_payload).is_valid(),
		"event rejects cyclic payload containers without recursive duplication",
		failures,
	)


func _test_input_contract(failures: PackedStringArray) -> void:
	var adapter: Variant = InputAdapterScript.new()
	_expect(adapter is RefCounted and not adapter is Node, "input adapter is platform-neutral RefCounted", failures)
	_expect(adapter.poll_commands().is_empty(), "base input adapter returns no commands", failures)
	_expect(adapter.active_device() == &"unknown", "base input adapter reports unknown device", failures)


func _test_display_contract(failures: PackedStringArray) -> void:
	var adapter: Variant = DisplayAdapterScript.new()
	var settings := {"fullscreen": true}
	var result: Dictionary = adapter.apply_settings(settings)
	_expect(_is_not_implemented(adapter.display_snapshot()), "display snapshot fails closed", failures)
	_expect(_is_not_implemented(result), "display settings fail closed", failures)
	_expect(settings == {"fullscreen": true}, "display contract does not mutate settings", failures)


func _test_save_contract(failures: PackedStringArray) -> void:
	var adapter: Variant = SaveAdapterScript.new()
	var payload := {"schema_version": 1}
	var result: Dictionary = adapter.write_payload_atomic(&"slot_1", payload)
	_expect(_is_not_implemented(adapter.load_payload(&"slot_1")), "save load fails closed", failures)
	_expect(_is_not_implemented(result), "save write fails closed", failures)
	_expect(payload == {"schema_version": 1}, "save contract does not mutate payload", failures)


func _test_lifecycle_contract(failures: PackedStringArray) -> void:
	var adapter: Variant = LifecycleAdapterScript.new()
	_expect(adapter.has_signal("lifecycle_event"), "lifecycle adapter declares lifecycle_event signal", failures)
	_expect(adapter is RefCounted and not adapter is Node, "lifecycle adapter is platform-neutral RefCounted", failures)


func _test_performance_contract(failures: PackedStringArray) -> void:
	var adapter: Variant = PerformanceAdapterScript.new()
	_expect(_is_not_implemented(adapter.budget_snapshot()), "performance snapshot fails closed", failures)


func _test_store_contract(failures: PackedStringArray) -> void:
	var adapter: Variant = StoreAdapterScript.new()
	_expect(not adapter.is_available(), "base store adapter is unavailable", failures)
	_expect(adapter.capabilities().is_empty(), "base store adapter exposes no capabilities", failures)


func _test_capabilities_contract(failures: PackedStringArray) -> void:
	var adapter: Variant = PlatformCapabilitiesScript.new(PackedStringArray(["touch", "cloud_save", "touch"]))
	_expect(adapter.has_capability(&"touch"), "explicit touch capability is present", failures)
	_expect(adapter.has_capability(&"cloud_save"), "explicit cloud capability is present", failures)
	_expect(not adapter.has_capability(&"achievements"), "unsupplied capability is absent", failures)
	var all_capabilities: PackedStringArray = adapter.all_capabilities()
	_expect(all_capabilities.size() == 2, "capability snapshot is deduplicated", failures)
	all_capabilities.append("achievements")
	_expect(not adapter.has_capability(&"achievements"), "returned capability snapshot cannot mutate contract state", failures)


func _is_not_implemented(result: Dictionary) -> bool:
	return result.get("ok") == false and result.get("error") == "not_implemented"


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Platform contract checks passed")
		quit(0)
	else:
		printerr("Platform contract failures:\n%s" % "\n".join(failures))
		quit(1)
