#!/usr/bin/env python3
"""Verify that every current raster runtime consumer has a source asset."""
from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = pathlib.PurePosixPath("data/bootstrap_catalog.tres")
BATTLEFIELD_SCENE = pathlib.PurePosixPath("scenes/battle/battlefield.tscn")
RUN_COMMAND_SCENE = pathlib.PurePosixPath("scenes/ui/run_command_screen.tscn")
UNIT_VIEW = pathlib.PurePosixPath("scripts/units/unit_view.gd")
REQUIRED_ROULETTE_ASSETS = {
    "assets/art/ui/run_command/roulette_board_frame.png",
    "assets/art/ui/run_command/roulette_arrow.png",
    "assets/art/ui/run_command/omen_device.png",
    "assets/art/ui/run_command/token_x.png",
    "assets/art/ui/run_command/token_gold.png",
}
REQUIRED_STATE_MARKERS = (
    'state_name.begins_with("attack")',
    'state_name == "hit_light"',
    'state_name == "dead"',
    'state_name.begins_with("bypass")',
    'state_name == "capture"',
    'state_name == "victory"',
)


def _read(root: pathlib.Path, relative: pathlib.PurePosixPath, errors: list[str], label: str) -> str:
    path = root / relative
    if not path.is_file():
        errors.append(f"missing {label}: {relative.as_posix()}")
        return ""
    return path.read_text(encoding="utf-8")


def _asset_paths(scene_text: str) -> set[str]:
    return set(re.findall(r'path="res://(assets/art/[^"]+\.png)"', scene_text))


def audit(root: pathlib.Path = ROOT) -> list[str]:
    """Return concrete gaps for current Godot image consumers, otherwise an empty list."""
    errors: list[str] = []
    catalog = _read(root, CATALOG, errors, "unit texture coverage source")
    battlefield = _read(root, BATTLEFIELD_SCENE, errors, "battlefield scene")
    roulette = _read(root, RUN_COMMAND_SCENE, errors, "roulette scene")
    unit_view = _read(root, UNIT_VIEW, errors, "unit state renderer")
    if not catalog or not battlefield or not roulette or not unit_view:
        return errors

    unit_paths = sorted(_asset_paths(catalog) & {path for path in _asset_paths(catalog) if "/units/" in path})
    if len(unit_paths) != 20:
        errors.append(f"missing unit texture coverage: expected 20 faction/archetype idle textures, found {len(unit_paths)}")
    for relative in unit_paths:
        if not (root / relative).is_file():
            errors.append(f"missing unit texture: {relative}")

    backdrop_paths = [path for path in _asset_paths(battlefield) if "/battlefield/" in path]
    if backdrop_paths != ["assets/art/battlefield/ward_veil_three_lane_backdrop_v1.png"]:
        errors.append("missing battlefield backdrop consumer binding")
    elif not (root / backdrop_paths[0]).is_file():
        errors.append(f"missing battlefield backdrop: {backdrop_paths[0]}")

    roulette_paths = _asset_paths(roulette)
    for relative in REQUIRED_ROULETTE_ASSETS:
        if relative not in roulette_paths and relative not in {"assets/art/ui/run_command/token_x.png", "assets/art/ui/run_command/token_gold.png"}:
            errors.append(f"missing roulette consumer binding: {relative}")
        if not (root / relative).is_file():
            errors.append(f"missing roulette texture: {relative}")

    for marker in REQUIRED_STATE_MARKERS:
        if marker not in unit_view:
            errors.append(f"missing procedural unit state expression: {marker}")
    return errors


def main() -> int:
    errors = audit(ROOT)
    if errors:
        print("Runtime image coverage audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Runtime image coverage audit passed: 20 unit idle textures, battlefield backdrop, roulette sources, and procedural state expressions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
