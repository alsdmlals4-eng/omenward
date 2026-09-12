"""Separate existing painted poses losslessly; no new artwork or geometric deformation."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/images/candidates/blueprint-20260911/ward-shield-slash-alpha-candidate.png'
SOURCE_SHA = 'd291307bf45e3ebf910bc1385c80c0aa30f28bb4aaa5411a41b2653dfecd99ce'

def prepare(source):
    if source.mode != 'RGBA' or source.size != (1254, 1254):
        raise ValueError('Re-review changed source geometry/alpha')
    rgba = np.array(source)
    alpha = rgba[:, :, 3]
    mask = Image.fromarray(np.where(alpha > 0, 255, 0).astype('uint8')).copy()
    seeds = [(300, 300), (920, 300), (300, 950), (960, 950)]
    for index, seed in enumerate(seeds):
        if mask.getpixel(seed) != 255:
            raise ValueError('Missing or connected poses')
        ImageDraw.floodfill(mask, seed, (index + 1) * 40)
    labels = np.array(mask)
    if np.any((labels == 255) & (alpha > 8)):
        raise ValueError('Unassigned visible artwork; do not silently discard')
    frames, records = [], []
    for index, name in enumerate(['idle', 'windup', 'impact', 'recover']):
        selected = labels == (index + 1) * 40
        ys, xs = np.where(selected & (alpha >= 128))
        baseline = int(ys.max())
        feet = xs[ys >= baseline - 11]
        pivot = ((int(feet.min()) + int(feet.max())) // 2, baseline)
        dx, dy = 384 - pivot[0], 700 - pivot[1]
        ys, xs = np.where(selected)
        if xs.min()+dx <= 0 or xs.max()+dx >= 767 or ys.min()+dy <= 0 or ys.max()+dy >= 767:
            raise ValueError('Pose would touch/cross frame bounds')
        frame = np.zeros((768, 768, 4), dtype='uint8')
        frame[ys+dy, xs+dx] = rgba[ys, xs]
        frames.append(Image.fromarray(frame))
        records.append({'state': name, 'offset': [dx, dy], 'source_pivot': list(pivot),
                        'pivot': [384, 700], 'duration_ms': [400, 180, 100, 150][index]})
    return frames, records

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA:
        raise ValueError('Source changed; review seeds and anatomy before processing')
    with Image.open(SOURCE) as source:
        frames, records = prepare(source)
    args.output.mkdir(parents=True, exist_ok=False)
    for index, frame in enumerate(frames):
        frame.save(args.output / f'pose-{index}.png')
    (args.output / 'extraction.json').write_text(json.dumps({'source_sha256': SOURCE_SHA,
        'discarded_max_alpha': 8, 'frames': records}, indent=2), encoding='utf-8')
    print(json.dumps(records))

if __name__ == '__main__':
    main()
