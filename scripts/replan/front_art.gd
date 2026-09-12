extends RefCounted
## Candidate-only atlas consumer. No copied pixels, alpha claims or final promotion.
const ROOT := "res://docs/images/candidates/blueprint-20260911/"
const Run = preload("res://scripts/replan/front_run.gd")
const ROLES := ["shield_guard", "archer", "mage", "priest", "spear_guard", "greatsword_warrior", "cavalry", "giant"]
const BUILDINGS := ["barracks", "spear_hall", "range", "academy", "chapel", "blade_hall", "stable", "siege"]
var cache: Dictionary = {}

func tile(file: String, columns: int, rows: int, index: int) -> Texture2D:
	var key := "%s:%s" % [file, index]
	if not cache.has(key):
		var texture: Texture2D = load(ROOT + file)
		var atlas := AtlasTexture.new()
		atlas.atlas = texture
		var cell := texture.get_size() / Vector2(columns, rows)
		atlas.region = Rect2(Vector2(index % columns, index / columns) * cell, cell)
		atlas.filter_clip = true
		cache[key] = atlas
	return cache[key]

func motion_frame(actor: Dictionary) -> int:
	if actor.side != 0 or actor.role != "shield_guard":
		return 0
	if float(actor.get("windup", 0.0)) > 0:
		return 1
	if float(actor.action) > Run.SHIELD_RECOVERY:
		return 2
	return 3 if float(actor.action) > 0 else 0

func unit(role: String, side: int, frame: int = 0) -> Texture2D:
	if side == 1:
		if role in ["assassin", "flying"]:
			return tile("veil-special-alpha.png", 2, 1, 0 if role == "assassin" else 1)
		return tile("veil-roster-alpha.png", 4, 2, ROLES.find(role))
	if role == "shield_guard" and side == 0:
		return tile("ward-shield-motion.png", 4, 1, clampi(frame, 0, 3))
	if role in ["assassin", "flying"]:
		return tile("special-roster-additions.png", 2, 2, (0 if role == "assassin" else 1) + side * 2)
	return tile("ward-roster.png" if side == 0 else "veil-roster.png", 4, 2, ROLES.find(role))

func building(id: String) -> Texture2D:
	var index := BUILDINGS.find(id)
	if index >= 0:
		return tile("building-tree.png", 4, 2, index)
	# Explicit generic facility emblem, not a falsely identified building portrait.
	return tile("ui-icons.png", 4, 4, 8 if id == "shield_hall" else 2)
