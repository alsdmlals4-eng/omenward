from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

stage_path = ROOT / "scripts/core/stage_run.gd"
stage = stage_path.read_text(encoding="utf-8")
old = 'const RouletteSpinResultScript = preload("res://scripts/data/roulette_spin_result.gd")\n'
new = '''const RouletteSpinResultScript = preload("res://scripts/data/roulette_spin_result.gd")
const RouletteSpinResult = preload("res://scripts/data/roulette_spin_result.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
'''
if stage.count(old) != 1:
    raise RuntimeError("StageRun explicit type preload insertion point missing")
stage_path.write_text(stage.replace(old, new, 1), encoding="utf-8", newline="\n")

service_path = ROOT / "scripts/core/core_ux_service.gd"
service = service_path.read_text(encoding="utf-8")
replacements = (
    (
        'var before_probability := run.roulette.probability_for_symbol(symbol_id) if symbol_id != &"" else 0.0',
        'var before_probability: float = float(run.roulette.probability_for_symbol(symbol_id)) if symbol_id != &"" else 0.0',
    ),
    (
        'var after_probability := run.roulette.probability_for_symbol(symbol_id, [source]) if not source.is_empty() else before_probability',
        'var after_probability: float = float(run.roulette.probability_for_symbol(symbol_id, [source])) if not source.is_empty() else before_probability',
    ),
    (
        'var role := profile.role if profile != null else "unknown"',
        'var role: String = str(profile.role) if profile != null else "unknown"',
    ),
)
for old_value, new_value in replacements:
    if service.count(old_value) != 1:
        raise RuntimeError(f"CoreUxService type repair source missing: {old_value}")
    service = service.replace(old_value, new_value, 1)
service_path.write_text(service, encoding="utf-8", newline="\n")

test_path = ROOT / "tests/headless/c3_core_ux_test.gd"
test = test_path.read_text(encoding="utf-8")
old = '''const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
'''
new = '''const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
const CoreUxService = preload("res://scripts/core/core_ux_service.gd")
const RouletteService = preload("res://scripts/roulette/roulette_service.gd")
const WaveDirector = preload("res://scripts/waves/wave_director.gd")
'''
if test.count(old) != 1:
    raise RuntimeError("C3 script preload block missing")
test = test.replace(old, new, 1)
old = '''func _init() -> void:
	var failures := PackedStringArray()
	_test_token_ledger_and_construction_preview(failures)
'''
new = '''func _init() -> void:
	var failures := PackedStringArray()
	if not _test_script_instantiation(failures):
		_finish(failures)
		return
	_test_token_ledger_and_construction_preview(failures)
'''
if test.count(old) != 1:
    raise RuntimeError("C3 test init insertion point missing")
test = test.replace(old, new, 1)
marker = '''func _new_run(seed: int) -> Variant:
'''
insert = '''func _test_script_instantiation(failures: PackedStringArray) -> bool:
	var scripts := {
		"StageRun": StageRun,
		"CoreUxService": CoreUxService,
		"RouletteService": RouletteService,
		"WaveDirector": WaveDirector,
	}
	var valid := true
	for script_name in scripts:
		var script: Script = scripts[script_name]
		if not script.can_instantiate():
			failures.append("C3 dependency script cannot instantiate: %s" % script_name)
			valid = false
	return valid


'''
if test.count(marker) != 1:
    raise RuntimeError("C3 test instantiation marker missing")
test = test.replace(marker, insert + marker, 1)
test_path.write_text(test, encoding="utf-8", newline="\n")

for relative in ("docs/_C3_HEADLESS_DIAGNOSTIC.log", "tools/_repair_c3_stage_run_types.py"):
    path = ROOT / relative
    if path.exists():
        path.unlink()
