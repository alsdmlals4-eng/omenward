from __future__ import annotations

import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]

EXPECTED_FILES = {
    "scripts/application/game_application.gd",
    "scripts/application/game_session.gd",
    "scripts/application/session_driver.gd",
    "scripts/application/platform_bootstrap.gd",
    "scripts/presentation/scene_binder.gd",
}


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class GameSessionDecouplingContractTests(unittest.TestCase):
    def test_target_files_replace_the_core_session_host(self) -> None:
        for path in sorted(EXPECTED_FILES):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertFalse((ROOT / "scripts/core/game_session.gd").exists())

    def test_game_application_is_platform_neutral(self) -> None:
        source = _read("scripts/application/game_application.gd")
        self.assertIn("class_name GameApplication", source)
        self.assertRegex(source, r"(?m)^extends RefCounted$")
        self.assertNotRegex(source, r"(?m)^\s*func _process\(")
        self.assertNotRegex(source, r"\b(?:get_node|get_node_or_null|find_child|find_children)\s*\(")
        self.assertNotIn("get_parent()", source)

    def test_game_session_is_only_a_compatibility_facade(self) -> None:
        source = _read("scripts/application/game_session.gd")
        self.assertIn("class_name GameSession", source)
        self.assertRegex(source, r"(?m)^extends Node$")
        self.assertNotRegex(source, r"(?m)^\s*func _process\(")
        self.assertNotRegex(source, r"\b(?:get_node|get_node_or_null|find_child|find_children)\s*\(")
        self.assertNotIn("get_parent()", source)
        self.assertNotIn("load_bootstrap_catalog", source)
        self.assertNotIn("StageRunScript", source)
        self.assertIn("return application.start_stage(stage_id)", source)
        self.assertIn("return application.retry_stage()", source)

    def test_driver_and_binder_own_frame_and_scene_responsibilities(self) -> None:
        driver = _read("scripts/application/session_driver.gd")
        binder = _read("scripts/presentation/scene_binder.gd")
        self.assertRegex(driver, r"(?m)^\s*func _process\(delta: float\) -> void:")
        self.assertIn("application.advance(delta)", driver)
        self.assertIn('call_deferred("_start_stage", stage_id)', driver)
        self.assertNotIn("get_node", driver)
        self.assertIn('get_node_or_null("Battlefield")', binder)
        self.assertIn('get_node_or_null("UI/StageHud")', binder)
        self.assertIn("host.get_parent()", binder)
        self.assertNotRegex(binder, r"(?m)^\s*func _process\(")

    def test_bootstrap_composes_one_driver_and_one_binder(self) -> None:
        source = _read("scripts/application/platform_bootstrap.gd")
        self.assertIn("func compose(", source)
        self.assertEqual(1, len(re.findall(r"host\.add_child\(driver\)", source)))
        self.assertEqual(1, len(re.findall(r"host\.add_child\(binder\)", source)))
        self.assertIn('"application": application', source)
        self.assertIn('"driver": driver', source)
        self.assertIn('"binder": binder', source)

    def test_main_scene_uses_the_application_facade_path(self) -> None:
        scene = _read("scenes/main/main.tscn")
        self.assertIn('path="res://scripts/application/game_session.gd"', scene)
        self.assertNotIn('path="res://scripts/core/game_session.gd"', scene)


if __name__ == "__main__":
    unittest.main()
