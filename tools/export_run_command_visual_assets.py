#!/usr/bin/env python3
"""Export approved Run Command UI masters as deterministic local derivatives."""

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
    canvas_size = tuple(entry["canvas_size"])
    if not source.is_file():
        raise FileNotFoundError(f"missing approved Run Command master: {source}")
    if output.exists():
        raise FileExistsError(f"refusing to overwrite Run Command derivative: {output}")

    source_image = Image.open(source).convert("RGBA")
    alpha_bounds = source_image.getchannel("A").getbbox()
    if alpha_bounds is None:
        raise ValueError(f"approved Run Command master has no visible pixels: {source}")
    cropped = source_image.crop(alpha_bounds)
    scale = min(canvas_size[0] / cropped.width, canvas_size[1] / cropped.height)
    scaled_size = (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale)))
    scaled = cropped.resize(scaled_size, Image.Resampling.NEAREST)
    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    offset = ((canvas_size[0] - scaled.width) // 2, (canvas_size[1] - scaled.height) // 2)
    canvas.alpha_composite(scaled, offset)

    alpha = canvas.getchannel("A")
    if alpha.getbbox() is None:
        raise ValueError(f"empty Run Command derivative exported: {output}")
    if any(value not in (0, 255) for value in alpha.get_flattened_data()):
        raise ValueError(f"Run Command derivative contains partial alpha: {output}")
    corners = ((0, 0), (canvas_size[0] - 1, 0), (0, canvas_size[1] - 1), (canvas_size[0] - 1, canvas_size[1] - 1))
    if any(canvas.getpixel(point)[3] != 0 for point in corners):
        raise ValueError(f"Run Command derivative corners must stay transparent: {output}")

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)
    return {
        "asset_id": entry["asset_id"],
        "consumer": entry["consumer"],
        "source": entry["source"],
        "source_sha256": sha256(source),
        "source_alpha_bounds": list(alpha_bounds),
        "output": entry["output"],
        "output_sha256": sha256(output),
        "canvas_size": list(canvas_size),
        "scaled_size": list(scaled_size),
        "placement": list(offset),
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
    report = {
        "record_id": manifest["record_id"],
        "approval_reference": manifest["approval_reference"],
        "normalization": manifest["normalization"],
        "entries": [export_entry(project_root, entry) for entry in entries],
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(report['entries'])} Run Command visual derivatives")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
