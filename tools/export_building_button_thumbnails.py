#!/usr/bin/env python3
"""Export approved building masters as compact transparent HUD thumbnails."""

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
    max_content_width, max_content_height = entry["max_content_size"]
    if not source.is_file():
        raise FileNotFoundError(f"missing approved building master: {source}")
    if output.exists():
        raise FileExistsError(f"refusing to overwrite build button thumbnail: {output}")

    source_image = Image.open(source).convert("RGBA")
    alpha_bounds = source_image.getchannel("A").getbbox()
    if alpha_bounds is None:
        raise ValueError(f"approved building master has no visible pixels: {source}")
    left, top, right, bottom = alpha_bounds
    cropped = source_image.crop(alpha_bounds)
    scale = min(max_content_width / cropped.width, max_content_height / cropped.height)
    scaled_size = (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale)))
    scaled = cropped.resize(scaled_size, Image.Resampling.NEAREST)
    if scaled.width > max_content_width or scaled.height > max_content_height:
        raise ValueError(f"scaled thumbnail does not fit declared content bounds: {source}")

    canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
    offset = ((canvas_width - scaled.width) // 2, canvas_height - scaled.height)
    canvas.alpha_composite(scaled, offset)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)

    alpha = canvas.getchannel("A")
    if alpha.getbbox() is None:
        raise ValueError(f"empty build button thumbnail exported: {output}")
    if any(value not in (0, 255) for value in alpha.get_flattened_data()):
        raise ValueError(f"build button thumbnail contains partial alpha: {output}")
    corners = ((0, 0), (canvas_width - 1, 0), (0, canvas_height - 1), (canvas_width - 1, canvas_height - 1))
    if any(canvas.getpixel(point)[3] != 0 for point in corners):
        raise ValueError(f"build button thumbnail corners must stay transparent: {output}")

    return {
        "building_id": entry["building_id"],
        "consumer": entry["consumer"],
        "source": entry["source"],
        "source_sha256": sha256(source),
        "source_alpha_bounds": [left, top, right, bottom],
        "output": entry["output"],
        "output_sha256": sha256(output),
        "canvas_size": [canvas_width, canvas_height],
        "max_content_size": [max_content_width, max_content_height],
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
    manifest = json.loads(args.manifest.resolve().read_text(encoding="utf-8"))
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
    print(f"Exported {len(results)} building button thumbnails to {project_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
