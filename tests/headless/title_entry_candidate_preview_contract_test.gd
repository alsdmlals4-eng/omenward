# 후보 전용 타이틀 합성은 현재 전투 배경과 워드마크를 함께 보이되, 실제 TitleScreen의 런타임 자산이 되지 않는다.
extends SceneTree

const PREVIEW_SCENE_PATH := "res://scenes/preview/omenward_title_entry_candidate_preview.tscn"
const TITLE_SCENE_PATH := "res://scenes/ui/title_screen.tscn"
const BACKGROUND_CANDIDATE_PATH := "res://docs/images/candidates/title/omenward_title_wall_command_battle_surge_candidate_v6.png"
const WORDMARK_CANDIDATE_PATH := "res://docs/images/candidates/title/omenward_title_omenward_wordmark_candidate_v1.png"


func _init() -> void:
	var failures := PackedStringArray()
	_expect(ResourceLoader.exists(BACKGROUND_CANDIDATE_PATH, "Texture2D"), "candidate preview has the active wall-command battle-surge background", failures)
	_expect(ResourceLoader.exists(WORDMARK_CANDIDATE_PATH, "Texture2D"), "candidate preview has the transparent OMENWARD wordmark", failures)
	_expect(FileAccess.file_exists(PREVIEW_SCENE_PATH), "candidate preview scene exists", failures)
	if FileAccess.file_exists(PREVIEW_SCENE_PATH):
		var preview_packed := load(PREVIEW_SCENE_PATH) as PackedScene
		_expect(preview_packed != null, "candidate preview scene loads", failures)
		if preview_packed != null:
			var preview := preview_packed.instantiate()
			var background := preview.get_node_or_null("Background") as TextureRect
			var title_wordmark := preview.get_node_or_null("TitleWordmark") as TextureRect
			_expect(background != null and background.texture != null and background.texture.resource_path == BACKGROUND_CANDIDATE_PATH, "candidate preview renders the current battle-surge background", failures)
			_expect(title_wordmark != null and title_wordmark.texture != null and title_wordmark.texture.resource_path == WORDMARK_CANDIDATE_PATH, "candidate preview renders the current wordmark", failures)
			preview.free()
	if FileAccess.file_exists(TITLE_SCENE_PATH):
		var runtime_title_text := FileAccess.get_file_as_string(TITLE_SCENE_PATH)
		_expect(not runtime_title_text.contains(BACKGROUND_CANDIDATE_PATH) and not runtime_title_text.contains(WORDMARK_CANDIDATE_PATH), "unlocked candidate art is not bound to the runtime title scene", failures)
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Title entry candidate preview contracts passed")
		quit(0)
	else:
		printerr("Title entry candidate preview contract failures:\n%s" % "\n".join(failures))
		quit(1)
