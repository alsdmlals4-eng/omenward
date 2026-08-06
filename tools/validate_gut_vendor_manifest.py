#!/usr/bin/env python3
"""Validate the static GUT 9.7.1 vendor manifest and activation blockers."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = Path("docs/operations/GUT_9_7_1_VENDOR_MANIFEST.v1.json")
DECISION_ID = "OMW-DEC-20260806-TOOLS-GUT-9-7-1-VENDOR-MANIFEST-RECONCILIATION-V1"
UPSTREAM_COMMIT = "aeb5d4f3f7f0a6c9b5e178876d6c99b791fda605"
UPSTREAM_TREE = "5d6893836af4917ee62b1a395125a7530b1f239d"
PROJECT_TREE = "09d040309bbed0e07420ad72c4aa69cbd0e58190"

EXPECTED_CHANGED_PATHS = frozenset(["GutScene.tscn", "UserFileViewer.tscn", "gui/GutControl.tscn", "gui/GutLogo.tscn", "gui/GutRunner.tscn", "gui/GutSceneTheme.tres", "gui/MinGui.tscn", "gui/NormalGui.tscn", "gui/OutputText.tscn", "gui/ResizeHandle.tscn", "gui/RunAtCursor.tscn", "gui/RunExternally.tscn", "gui/RunResults.tscn", "gui/ShellOutOptions.tscn", "gui/ShortcutButton.tscn", "gui/run_from_editor.tscn", "gut_loader_the_scene.tscn", "source_code_pro.fnt"])
FORBIDDEN_CODE_SUFFIXES = (".gd", ".gd.uid")
FORBIDDEN_EXACT_PATHS = frozenset({"plugin.cfg", "LICENSE.md", "fonts/OFL.txt"})


def load_manifest(root: Path = ROOT) -> dict[str, Any]:
    return json.loads((root / MANIFEST_PATH).read_text(encoding="utf-8"))


def validate_manifest(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("Decision ID mismatch")
    if data.get("status") != "VENDOR_DELTA_CLASSIFIED_ACTIVATION_BLOCKED":
        errors.append("manifest status must remain activation-blocked")

    upstream = data.get("upstream", {})
    project = data.get("project", {})
    if upstream.get("commit") != UPSTREAM_COMMIT:
        errors.append("upstream commit mismatch")
    if upstream.get("addons_gut_tree_sha") != UPSTREAM_TREE:
        errors.append("upstream tree mismatch")
    if project.get("addons_gut_tree_sha") != PROJECT_TREE:
        errors.append("project tree mismatch")
    if upstream.get("recursive_tree_truncated") or project.get("recursive_tree_truncated"):
        errors.append("recursive tree evidence must be complete")

    path_set = data.get("path_set", {})
    if path_set.get("status") != "MATCH":
        errors.append("vendor path sets must match")
    if path_set.get("missing_paths"):
        errors.append("vendor manifest must not hide missing paths")
    if path_set.get("extra_paths"):
        errors.append("vendor manifest must not hide extra paths")

    rows = data.get("changed_paths", [])
    actual_paths = {row.get("path") for row in rows}
    if actual_paths != EXPECTED_CHANGED_PATHS:
        errors.append("changed path set mismatch")
    if path_set.get("changed_path_count") != len(EXPECTED_CHANGED_PATHS):
        errors.append("changed path count mismatch")

    for row in rows:
        path = str(row.get("path", ""))
        if path.endswith(FORBIDDEN_CODE_SUFFIXES) or path in FORBIDDEN_EXACT_PATHS:
            errors.append(f"code/config/license delta forbidden: {path}")
        classification = row.get("classification")
        if path == "source_code_pro.fnt":
            if classification != "UNCLASSIFIED_BINARY_DELTA":
                errors.append("source_code_pro.fnt must remain unclassified until decoded")
            if row.get("size_delta") != 0:
                errors.append("source_code_pro.fnt recorded size delta must be zero")
        else:
            if classification != "HEADER_LOAD_STEPS_NORMALIZATION_CANDIDATE":
                errors.append(f"text resource classification mismatch: {path}")
            if row.get("size_delta") != -13:
                errors.append(f"text resource size delta must be -13: {path}")
            if not path.endswith((".tscn", ".tres")):
                errors.append(f"header normalization candidate has invalid extension: {path}")

    summary = data.get("classification_summary", {})
    if summary.get("header_normalization_candidates") != 17:
        errors.append("header candidate count mismatch")
    if summary.get("unclassified_binary_deltas") != 1:
        errors.append("binary delta count mismatch")
    if summary.get("code_or_plugin_deltas") != 0:
        errors.append("code or plugin deltas must be zero")

    activation = data.get("activation", {})
    blockers = set(activation.get("blockers", []))
    if activation.get("status") != "BLOCKED":
        errors.append("activation must remain BLOCKED")
    required_blockers = {
        "FULL_CONTENT_DIFF_NOT_COMPLETED_FOR_17_TEXT_RESOURCES",
        "SOURCE_CODE_PRO_FNT_BINARY_DELTA_UNCLASSIFIED",
        "EXACT_GODOT_4_7_IMPORT_NOT_RUN",
        "GUT_CLI_CANARY_NOT_RUN",
        "PROJECT_REGRESSION_NOT_RUN",
    }
    if not required_blockers.issubset(blockers):
        errors.append("activation blockers incomplete")
    return errors


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", action="store_true")
    parser.add_argument("--activation", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)

    try:
        data = load_manifest(ROOT)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"manifest=FAILED error={exc}")
        return 1

    errors = validate_manifest(data)
    if errors:
        print("manifest=FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("manifest=PASS activation=BLOCKED changed_paths=18")
    if args.activation:
        for blocker in data["activation"]["blockers"]:
            print(f"blocker={blocker}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
