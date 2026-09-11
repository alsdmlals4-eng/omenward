extends RefCounted
## Candidate-only atlas consumer. No copied pixels, alpha claims or final promotion.
const ROOT := "res://docs/images/candidates/blueprint-20260911/"
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

func unit(role: String, side: int) -> Texture2D:
	if role == "shield_guard" and side == 0:
		# Only the clean idle cell is consumed; crossed slash cells are NOT animation-ready.
		return tile("ward-shield-slash-alpha-candidate.png", 2, 2, 0)
	if role in ["assassin", "flying"]:
		return tile("special-roster-additions.png", 2, 2, (0 if role == "assassin" else 1) + side * 2)
	return tile("ward-roster.png" if side == 0 else "veil-roster.png", 4, 2, ROLES.find(role))

func building(id: String) -> Texture2D:
	var index := BUILDINGS.find(id)
	if index >= 0:
		return tile("building-tree.png", 4, 2, index)
	# Explicit generic facility emblem, not a falsely identified building portrait.
	return tile("ui-icons.png", 4, 4, 8 if id == "shield_hall" else 2)
