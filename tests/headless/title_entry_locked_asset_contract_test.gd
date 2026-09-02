# 확정된 타이틀 아트는 실제 TitleScreen에서만 소비하고, 이전 후보 경로를 남기지 않는다.
extends SceneTree

const TITLE_SCENE_PATH := "res://scenes/ui/title_screen.tscn"
const BACKGROUND_PATH := "res://assets/art/ui/title/omenward_title_wall_battle_surge_v1.png"
const WORDMARK_PATH := "res://assets/art/ui/title/omenward_title_omenward_wordmark_v1.png"
const CANDIDATE_DIRECTORY_PATH := "res://docs/images/candidates/title"


func _init() -> void:
	var failures := PackedStringArray()
	_expect(ResourceLoader.exists(BACKGROUND_PATH, "Texture2D"), "approved battle-surge backdrop exists in the runtime asset root", failures)
	_expect(ResourceLoader.exists(WORDMARK_PATH, "Texture2D"), "approved OMENWARD wordmark exists in the runtime asset root", failures)
	_expect(not DirAccess.dir_exists_absolute(CANDIDATE_DIRECTORY_PATH), "superseded title candidate image directory is removed after promotion", failures)
	if FileAccess.file_exists(TITLE_SCENE_PATH):
		var title_packed := load(TITLE_SCENE_PATH) as PackedScene
		_expect(title_packed != null, "locked title scene loads", failures)
		if title_packed != null:
			var title_screen := title_packed.instantiate()
			var backdrop := title_screen.get_node_or_null("Backdrop") as TextureRect
			var wordmark := title_screen.get_node_or_null("TitleWordmark") as TextureRect
			_expect(backdrop != null and backdrop.texture != null and backdrop.texture.resource_path == BACKGROUND_PATH, "runtime title renders the approved battle-surge backdrop", failures)
			_expect(wordmark != null and wordmark.texture != null and wordmark.texture.resource_path == WORDMARK_PATH, "runtime title renders the approved transparent wordmark", failures)
			_expect(title_screen.get_node_or_null("Panel/Title") == null, "native placeholder title is removed instead of duplicating the approved wordmark", failures)
			title_screen.free()
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Title entry locked asset contracts passed")
		quit(0)
	else:
		printerr("Title entry locked asset contract failures:\n%s" % "\n".join(failures))
		quit(1)
