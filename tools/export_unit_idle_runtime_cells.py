#!/usr/bin/env python3
"""Export approved cleanup masters as transparent, common-ground idle cells."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from PIL import Image


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def export_entry(project_root: Path, entry: dict[str, Any]) -> dict[str, Any]:
    source = project_root / entry["source"]
    output = project_root / entry["output"]
    canvas_width, canvas_height = entry["canvas_size"]
    pivot_x, pivot_y = entry["pivot"]
    max_content_height = entry["max_content_height"]
    if not source.is_file():
        raise FileNotFoundError(f"missing cleanup master: {source}")
    if output.exists():
        raise FileExistsError(f"refusing to overwrite runtime cell: {output}")

    source_image = Image.open(source).convert("RGBA")
    alpha_bounds = source_image.getchannel("A").getbbox()
    if alpha_bounds is None:
        raise ValueError(f"cleanup master has no visible pixels: {source}")
    left, top, right, bottom = alpha_bounds
    cropped = source_image.crop(alpha_bounds)
    crop_width, crop_height = cropped.size
    scale = min(canvas_width / crop_width, max_content_height / crop_height)
    scaled_size = (max(1, round(crop_width * scale)), max(1, round(crop_height * scale)))
    scaled = cropped.resize(scaled_size, Image.Resampling.NEAREST)
    if scaled.width > canvas_width or scaled.height > max_content_height:
        raise ValueError(f"scaled content does not fit cell: {source}")

    canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
    offset = ((canvas_width - scaled.width) // 2, pivot_y - scaled.height)
    if offset[1] < 0:
        raise ValueError(f"scaled content crosses cell top: {source}")
    canvas.alpha_composite(scaled, offset)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)

    output_alpha = canvas.getchannel("A")
    if output_alpha.getbbox() is None:
        raise ValueError(f"empty runtime cell exported: {output}")
    if any(value not in (0, 255) for value in output_alpha.get_flattened_data()):
        raise ValueError(f"runtime cell contains partial alpha: {output}")
    if any(canvas.getpixel(point)[3] != 0 for point in ((0, 0), (canvas_width - 1, 0), (0, canvas_height - 1), (canvas_width - 1, canvas_height - 1))):
        raise ValueError(f"runtime cell corners must remain transparent: {output}")

    return {
        "archetype_id": entry["archetype_id"],
        "visual_faction_id": entry["visual_faction_id"],
        "source": entry["source"],
        "source_sha256": sha256(source),
        "source_alpha_bounds": [left, top, right, bottom],
        "output": entry["output"],
        "output_sha256": sha256(output),
        "canvas_size": [canvas_width, canvas_height],
        "pivot": [pivot_x, pivot_y],
        "max_content_height": max_content_height,
        "scaled_size": [scaled.width, scaled.height],
        "placement": [offset[0], offset[1]],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = manifest.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("manifest must contain at least one entry")

    results = [export_entry(project_root, entry) for entry in entries]
    report = {
        "record_id": manifest["record_id"],
        "normalization": manifest["normalization"],
        "entries": results,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(results)} runtime cells to {project_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
