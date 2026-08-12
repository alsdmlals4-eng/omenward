# 병영 역할 출력 런타임 계약을 검증하는 GUT 테스트입니다.
extends GutTest

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const BattleSimulator = preload("res://scripts/battle/battle_simulator.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const BLOCKED_RUNTIME_OUTPUT := "BLOCKED_RUNTIME_OUTPUT"


func test_priest_heals_lowest_health_same_lane_ally_with_effective_and_overheal_separated() -> void:
	var battle := _battle(1101)
	battle.objectives_enabled = false
	var priest = battle.spawn_unit(_spawn(&"lumern", &"top", &"priest"))
	var first_ally = battle.spawn_unit(_spawn(&"lumern", &"top", &"shield_guard"))
	var second_ally = battle.spawn_unit(_spawn(&"lumern", &"top", &"greatsword_warrior"))
	first_ally.health = first_ally.combat_stats()["max_health"] - 5.0
	second_ally.health = first_ally.health
	_advance(battle, 1.0)
	var heal = _first_event(battle.drain_events(), "role_heal")
	assert_not_null(heal, "Priest must emit a role_heal event when a damaged same-lane ally exists.")
	if heal == null:
		return
	assert_eq(int(heal["source"]), priest.unit_id, "The event identifies the Priest source.")
	assert_eq(int(heal["target"]), first_ally.unit_id, "Equal lowest-health allies resolve by unit id deterministically.")
	assert_gt(float(heal["raw_heal"]), float(heal["effective_heal"]), "Near-full target creates distinct raw and effective healing.")
	assert_gt(float(heal["overheal"]), 0.0, "Overheal is observable rather than folded into effective healing.")
	assert_almost_eq(float(heal["raw_heal"]), float(heal["effective_heal"]) + float(heal["overheal"]), 0.001, "Heal accounting is conserved.")


func test_priest_buffs_only_without_valid_heal_target_and_reports_uptime() -> void:
	var battle := _battle(1102)
	battle.objectives_enabled = false
	var priest = battle.spawn_unit(_spawn(&"lumern", &"top", &"priest"))
	var ally = battle.spawn_unit(_spawn(&"lumern", &"top", &"shield_guard"))
	_advance(battle, 1.0)
	var events = battle.drain_events()
	var buff_start = _first_event(events, "role_buff_start")
	assert_not_null(buff_start, "Priest must encourage an ally when no valid heal target exists.")
	if buff_start == null:
		return
	assert_eq(int(buff_start["source"]), priest.unit_id, "Buff source is the Priest.")
	assert_eq(int(buff_start["target"]), ally.unit_id, "Single same-lane ally receives encouragement.")
	_advance(battle, 5.1)
	var buff_end = _first_event(battle.drain_events(), "role_buff_end")
	assert_not_null(buff_end, "Buff end is emitted after its bounded duration.")
	var metrics = _role_metrics(battle)
	assert_gt(float(metrics["BUFF_UPTIME"]), 0.0, "Buff uptime is measurable.")
	assert_gt(float(metrics["SUPPORTED_TARGET_SECONDS"]), 0.0, "Supported target time is measurable.")


func test_mage_cluster_selection_and_primary_collateral_outputs_are_deterministic() -> void:
	var first := _mage_cluster_battle(1103)
	var second := _mage_cluster_battle(1103)
	_advance(first, 2.0)
	_advance(second, 2.0)
	var first_events = first.drain_events()
	var second_events = second.drain_events()
	var hit = _first_event(first_events, "role_aoe_hit")
	assert_not_null(hit, "Mage must emit a role_aoe_hit event for a same-lane cluster.")
	if hit == null:
		return
	assert_gt(int(hit["affected_unit_ids"].size()), 1, "Cluster cast affects primary plus collateral targets.")
	assert_gt(float(hit["primary_damage"]), 0.0, "Primary damage remains separately observable.")
	assert_gt(float(hit["collateral_damage"]), 0.0, "Collateral damage remains separately observable.")
	assert_eq(JSON.stringify(first_events), JSON.stringify(second_events), "Identical seed/input produces identical cluster selection and event order.")


func test_damage_channels_apply_armor_or_magic_resistance() -> void:
	var battle := _battle(1104)
	var physical_target = battle.spawn_unit(_spawn(&"veil", &"top", &"shield_guard"))
	var magic_target = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
	assert_true(physical_target.has_method("receive_damage_with_channel"), "Runtime exposes explicit physical and magic damage channels.")
	if not physical_target.has_method("receive_damage_with_channel"):
		return
	var stats = physical_target.combat_stats()
	var physical = physical_target.receive_damage_with_channel(100.0, &"physical")
	var magic = magic_target.receive_damage_with_channel(100.0, &"magic")
	assert_almost_eq(float(physical), 100.0 * 100.0 / (100.0 + float(stats["armor"])), 0.001, "Physical damage exercises armor.")
	assert_almost_eq(float(magic), 100.0 * 100.0 / (100.0 + float(stats["magic_resistance"])), 0.001, "Magic damage exercises base_stats.magic_resistance.")


func test_flier_uses_own_backline_route_and_emits_first_contact_timing() -> void:
	var battle := _battle(1105)
	battle.objectives_enabled = false
	var flier = battle.spawn_unit(_spawn(&"lumern", &"top", &"flier"))
	var frontline = battle.spawn_unit(_spawn(&"veil", &"top", &"shield_guard"))
	var backline = battle.spawn_unit(_spawn(&"veil", &"top", &"archer"))
	flier.lane_position = 0.0
	frontline.lane_position = 25.0
	backline.lane_position = 40.0
	_advance(battle, 40.0)
	var contact = _first_event(battle.drain_events(), "role_backline_contact")
	assert_not_null(contact, "Flier reaching the same-lane backline emits first-contact timing.")
	if contact == null:
		return
	assert_eq(int(contact["source"]), flier.unit_id, "Contact event identifies the Flier.")
	assert_eq(int(contact["target"]), backline.unit_id, "Flier route reaches the backline rather than the frontline.")
	assert_gt(float(contact["time_to_contact"]), 0.0, "Time-to-contact is observable.")
	var metrics = _role_metrics(battle)
	assert_eq(metrics["AIR_TARGETABILITY_EXPOSURE"], BLOCKED_RUNTIME_OUTPUT, "Unimplemented anti-air exposure remains explicitly blocked.")


func test_archer_anti_air_priority_selects_flier_when_applicable() -> void:
	var battle := _battle(1106)
	battle.objectives_enabled = false
	var archer = battle.spawn_unit(_spawn(&"lumern", &"top", &"archer"))
	var ground = battle.spawn_unit(_spawn(&"veil", &"top", &"shield_guard"))
	var flier = battle.spawn_unit(_spawn(&"veil", &"top", &"flier"))
	archer.lane_position = 50.0
	ground.lane_position = 51.0
	flier.lane_position = 53.0
	var target = battle.lanes[&"top"].find_target(archer)
	assert_not_null(target, "Archer receives an enemy target.")
	if target != null:
		assert_eq(target.unit_id, flier.unit_id, "Archer anti-air priority selects a Flier over a nearer ground unit.")


func test_giant_slam_is_bounded_deterministic_and_excludes_air() -> void:
	var first := _giant_slam_battle(1107)
	var second := _giant_slam_battle(1107)
	_advance(first, 2.0)
	_advance(second, 2.0)
	var first_events = first.drain_events()
	var second_events = second.drain_events()
	var slam = _first_event(first_events, "role_slam")
	assert_not_null(slam, "Giant emits role_slam for same-lane ground cluster.")
	if slam == null:
		return
	assert_lte(int(slam["affected_unit_ids"].size()), 6, "Slam remains bounded to six targets.")
	var air_id = _unit_id_for_archetype(first, &"flier")
	assert_false(slam["affected_unit_ids"].has(air_id), "Slam excludes air targets.")
	assert_eq(JSON.stringify(first_events), JSON.stringify(second_events), "Slam targeting is deterministic.")


func test_giant_preserves_siege_gate_output() -> void:
	var battle := _battle(1108)
	var giant = battle.spawn_unit(_spawn(&"lumern", &"top", &"giant"))
	_stabilize_lane_for_lumern_gate(battle, &"top")
	giant.lane_position = float(battle.GATE_POSITIONS[&"veil"])
	battle.gates[&"veil"][&"top"].health = 1.0
	_advance(battle, 2.0)
	assert_not_null(_first_event(battle.drain_events(), "gate_damage"), "Giant continues to emit the existing siege gate_damage output.")


func test_blocked_runtime_output_is_never_serialized_as_numeric_zero() -> void:
	var battle := _battle(1109)
	assert_true(battle.has_method("role_output_metrics"), "Runtime exposes role-output metrics.")
	if not battle.has_method("role_output_metrics"):
		return
	var metrics = _role_metrics(battle)
	assert_eq(metrics["CONTROL_TARGET_SECONDS"], BLOCKED_RUNTIME_OUTPUT, "Absent control stays BLOCKED_RUNTIME_OUTPUT.")
	assert_eq(metrics["AIR_TARGETABILITY_EXPOSURE"], BLOCKED_RUNTIME_OUTPUT, "Absent anti-air exposure stays BLOCKED_RUNTIME_OUTPUT.")
	assert_false(JSON.stringify(metrics).contains("\"CONTROL_TARGET_SECONDS\":0"), "Blocked control is never serialized as numeric zero.")
	assert_false(JSON.stringify(metrics).contains("\"AIR_TARGETABILITY_EXPOSURE\":0"), "Blocked air exposure is never serialized as numeric zero.")


func test_identical_role_fixture_keeps_event_order_identical() -> void:
	var first := _role_fixture(1110)
	var second := _role_fixture(1110)
	_advance(first, 12.0)
	_advance(second, 12.0)
	var first_events = first.drain_events()
	var second_events = second.drain_events()
	assert_false(first_events.is_empty(), "Role fixture produces observable role events.")
	assert_eq(JSON.stringify(first_events), JSON.stringify(second_events), "Identical deterministic input preserves event ordering.")


func test_priest_encouragement_changes_attack_rate_for_five_seconds_then_reverts_after_expiry() -> void:
	var encouraged := _battle(1161)
	encouraged.objectives_enabled = false
	var priest = encouraged.spawn_unit(_spawn(&"lumern", &"top", &"priest"))
	var encouraged_ally = encouraged.spawn_unit(_spawn(&"lumern", &"top", &"shield_guard"))
	var encouraged_enemy = encouraged.spawn_unit(_spawn(&"veil", &"top", &"shield_guard"))
	encouraged_ally.lane_position = 50.0
	encouraged_enemy.lane_position = 51.0
	_advance(encouraged, 4.0)
	var first_window_events = encouraged.drain_events()
	assert_not_null(_first_event(first_window_events, "role_buff_start"), "Priest encouragement starts when its ally is healthy.")
	var control := _battle(1161)
	control.objectives_enabled = false
	var control_ally = control.spawn_unit(_spawn(&"lumern", &"top", &"shield_guard"))
	var control_enemy = control.spawn_unit(_spawn(&"veil", &"top", &"shield_guard"))
	control_ally.lane_position = 50.0
	control_enemy.lane_position = 51.0
	_advance(control, 4.0)
	var encouraged_damage: float = float(encouraged_enemy.combat_stats()["max_health"]) - float(encouraged_enemy.health)
	var control_damage: float = float(control_enemy.combat_stats()["max_health"]) - float(control_enemy.health)
	assert_gt(encouraged_damage, control_damage, "Encouragement increases the ally attack rate during its five-second uptime.")
	_advance(encouraged, 1.2)
	assert_not_null(_first_event(encouraged.drain_events(), "role_buff_end"), "Priest encouragement emits an end event at expiry.")
	_advance(control, 1.2)
	encouraged_ally.state = "idle"
	encouraged_ally.cooldown_remaining = 0.0
	control_ally.state = "idle"
	control_ally.cooldown_remaining = 0.0
	var encouraged_health_at_expiry: float = float(encouraged_enemy.health)
	var control_health_at_expiry: float = float(control_enemy.health)
	_advance(encouraged, 1.5)
	_advance(control, 1.5)
	assert_almost_eq(encouraged_health_at_expiry - encouraged_enemy.health, control_health_at_expiry - control_enemy.health, 0.001, "Attack timing returns to the unbuffed rate after encouragement expires.")


func test_support_without_priest_special_action_uses_existing_objective_fallback() -> void:
	var battle := _battle(1162)
	var priest = battle.spawn_unit(_spawn(&"lumern", &"top", &"priest"))
	var starting_position: float = float(priest.lane_position)
	_advance(battle, 1.0)
	assert_gt(priest.lane_position, starting_position, "A support unit with no heal or encouragement target keeps deterministic objective movement.")


func test_untagged_attacker_retains_legal_air_candidate_while_archer_priority_remains_flying_first() -> void:
	var battle := _battle(1163)
	battle.objectives_enabled = false
	var attacker = battle.spawn_unit(_spawn(&"lumern", &"top", &"greatsword_warrior"))
	var flier = battle.spawn_unit(_spawn(&"veil", &"top", &"flier"))
	attacker.lane_position = 50.0
	flier.lane_position = 51.0
	var target = battle.lanes[&"top"].find_target(attacker)
	assert_not_null(target, "A legal air enemy remains a candidate even without an explicit flying-priority tag.")
	if target != null:
		assert_eq(target.unit_id, flier.unit_id, "The only legal enemy is selected.")


func test_mage_cluster_density_tie_uses_lane_order_unit_id_not_nearest_distance() -> void:
	var battle := _battle(1164)
	var mage = battle.spawn_unit(_spawn(&"lumern", &"middle", &"mage"))
	mage.lane_position = 0.0
	var first_lane_order = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
	first_lane_order.lane_position = 20.0
	var first_neighbor = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
	first_neighbor.lane_position = 21.0
	var nearer_cluster = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
	nearer_cluster.lane_position = 10.0
	var nearer_neighbor = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
	nearer_neighbor.lane_position = 11.0
	var target = battle.lanes[&"middle"].find_target(mage)
	assert_not_null(target, "Mage receives a tied-density cluster target.")
	if target != null:
		assert_eq(target.unit_id, first_lane_order.unit_id, "Equal-density clusters resolve by lane order and unit id rather than distance order.")


func test_giant_reports_frontline_survival_and_structure_damage_without_fake_zeroes() -> void:
	var battle := _giant_slam_battle(1165)
	_advance(battle, 2.0)
	var metrics := _role_metrics(battle)
	assert_true(metrics.has("FRONTLINE_SURVIVAL_TIME"), "Giant exposes FRONTLINE_SURVIVAL_TIME as a measured or explicitly blocked output.")
	assert_true(metrics.has("STRUCTURE_DAMAGE"), "Giant exposes STRUCTURE_DAMAGE as a measured or explicitly blocked output.")
	if metrics.has("FRONTLINE_SURVIVAL_TIME"):
		assert_ne(metrics["FRONTLINE_SURVIVAL_TIME"], 0.0, "Unavailable Giant frontline survival is never falsified as numeric zero.")
	if metrics.has("STRUCTURE_DAMAGE"):
		assert_ne(metrics["STRUCTURE_DAMAGE"], 0.0, "Unavailable Giant structure damage is never falsified as numeric zero.")


func test_targets_hit_per_cast_is_not_a_running_total_across_multiple_mage_casts() -> void:
	var battle := _mage_cluster_battle(1166)
	for unit in battle.lanes[&"middle"].units:
		if unit.owner_team_id == &"veil":
			unit.health = 1000.0
	_advance(battle, 10.0)
	var casts := _events_of_type(battle.drain_events(), "role_aoe_hit")
	assert_gte(casts.size(), 2, "Fixture produces multiple Mage casts.")
	if casts.size() < 2:
		return
	var metrics := _role_metrics(battle)
	var last_cast: Dictionary = casts[casts.size() - 1]
	assert_eq(float(metrics["TARGETS_HIT_PER_CAST"]), float((last_cast["affected_unit_ids"] as Array).size()), "TARGETS_HIT_PER_CAST reports the current cast cardinality, not a running total.")


func _events_of_type(events: Array, event_type: String) -> Array:
	var matched: Array = []
	for event in events:
		if event.get("event_type") == event_type:
			matched.append(event)
	return matched


func _battle(seed: int) -> BattleSimulator:
	return BattleSimulator.new(_registry(), seed)


func _mage_cluster_battle(seed: int) -> BattleSimulator:
	var battle := _battle(seed)
	battle.objectives_enabled = false
	var mage = battle.spawn_unit(_spawn(&"lumern", &"middle", &"mage"))
	mage.lane_position = 50.0
	for position in [51.0, 52.0, 53.0]:
		var enemy = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
		enemy.lane_position = position
	return battle


func _giant_slam_battle(seed: int) -> BattleSimulator:
	var battle := _battle(seed)
	battle.objectives_enabled = false
	var giant = battle.spawn_unit(_spawn(&"lumern", &"bottom", &"giant"))
	giant.lane_position = 50.0
	for position in [51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0]:
		var enemy = battle.spawn_unit(_spawn(&"veil", &"bottom", &"shield_guard"))
		enemy.lane_position = position
	var flier = battle.spawn_unit(_spawn(&"veil", &"bottom", &"flier"))
	flier.lane_position = 51.5
	return battle


func _role_fixture(seed: int) -> BattleSimulator:
	var battle := _battle(seed)
	battle.objectives_enabled = false
	var priest = battle.spawn_unit(_spawn(&"lumern", &"top", &"priest"))
	var ally = battle.spawn_unit(_spawn(&"lumern", &"top", &"shield_guard"))
	ally.health = ally.combat_stats()["max_health"] - 10.0
	var mage = battle.spawn_unit(_spawn(&"lumern", &"middle", &"mage"))
	mage.lane_position = 50.0
	var giant = battle.spawn_unit(_spawn(&"lumern", &"bottom", &"giant"))
	giant.lane_position = 50.0
	var flier = battle.spawn_unit(_spawn(&"lumern", &"top", &"flier"))
	flier.lane_position = 0.0
	for position in [51.0, 52.0, 53.0]:
		var mage_enemy = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
		mage_enemy.lane_position = position
	for position in [51.0, 52.0, 53.0]:
		var giant_enemy = battle.spawn_unit(_spawn(&"veil", &"bottom", &"shield_guard"))
		giant_enemy.lane_position = position
	var backline = battle.spawn_unit(_spawn(&"veil", &"top", &"archer"))
	backline.lane_position = 20.0
	return battle


func _stabilize_lane_for_lumern_gate(battle: BattleSimulator, lane_id: StringName) -> void:
	battle.clash_zones[lane_id].outpost.owner_team_id = &"lumern"
	battle.clash_zones[lane_id].outpost.state = battle.clash_zones[lane_id].outpost.STABLE
	battle.outposts[&"veil"][lane_id].owner_team_id = &"lumern"
	battle.outposts[&"veil"][lane_id].state = battle.outposts[&"veil"][lane_id].outpost.STABLE if false else battle.outposts[&"veil"][lane_id].STABLE


func _registry() -> DataRegistry:
	var registry := DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	assert_true(errors.is_empty(), "Test registry loads the approved bootstrap catalog.")
	return registry


func _spawn(team_id: StringName, lane_id: StringName, archetype_id: StringName) -> UnitSpawnDefinition:
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = archetype_id
	spawn.owner_team_id = team_id
	spawn.visual_faction_id = team_id
	spawn.lane_id = lane_id
	return spawn


func _advance(battle: BattleSimulator, seconds: float) -> void:
	var steps := int(round(seconds / 0.1))
	for _step in steps:
		battle.advance(0.1)


func _first_event(events: Array, event_type: String) -> Variant:
	for event in events:
		if event.get("event_type") == event_type:
			return event
	return null


func _role_metrics(battle: BattleSimulator) -> Dictionary:
	return battle.role_output_metrics() if battle.has_method("role_output_metrics") else {}


func _unit_id_for_archetype(battle: BattleSimulator, archetype_id: StringName) -> int:
	for unit in battle.lanes[&"bottom"].units:
		if unit.archetype_id == archetype_id:
			return unit.unit_id
	return -1
