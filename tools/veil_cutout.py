"""User-approved local alpha-only cutouts; never redraw or overwrite source pixels."""
from pathlib import Path
import hashlib
import argparse
import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'docs/images/candidates/blueprint-20260911'

def soften_edges(source):
    """Subpixel inward feather: no new silhouette pixels, no RGB alteration."""
    result = source.copy()
    alpha = source.getchannel('A')
    result.putalpha(ImageChops.darker(alpha, alpha.filter(ImageFilter.GaussianBlur(0.5))))
    return result

def cutout(source, minimum=155):
    rgb = source.convert('RGB')
    pixels = np.asarray(rgb).astype(np.int16)
    # Conservative paper mask. Enclosed pale anatomy remains opaque.
    paper = (pixels.min(axis=2) > minimum) & ((pixels.max(axis=2) - pixels.min(axis=2)) < 65)
    mask = ImageOps.expand(Image.fromarray((paper * 255).astype('uint8')), border=1, fill=255)
    ImageDraw.floodfill(mask, (0, 0), 128, thresh=0)
    connected = np.asarray(mask)[1:-1, 1:-1] == 128
    result = rgb.convert('RGBA')
    result.putalpha(Image.fromarray(np.where(connected, 0, 255).astype('uint8')))
    return result

def ward_assets():
    jobs = [('ward-roster.png', 'ward-roster-alpha.png', (1774, 887)),
            ('special-roster-additions.png', 'ward-special-alpha.png', (1254, 1254)),
            ('building-tree.png', 'building-tree-alpha.png', (1774, 887))]
    for original, target, dimensions in jobs:
        source_path, output = ART / original, ART / target
        if output.exists():
            raise FileExistsError(output)
        digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        with Image.open(source_path) as source:
            image = source.convert('RGB')
        if image.size != dimensions:
            raise ValueError('Re-review changed source dimensions')
        if original == 'special-roster-additions.png':
            image = image.crop((0, 0, 1254, 610))
        result = soften_edges(cutout(image))
        assert result.convert('RGB').tobytes() == image.tobytes()
        assert hashlib.sha256(source_path.read_bytes()).hexdigest() == digest
        result.save(output)
        print(target, 'sha256=', hashlib.sha256(output.read_bytes()).hexdigest())

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ward', action='store_true', help='Create Ward and facility derivatives only')
    if parser.parse_args().ward:
        ward_assets()
        return
    jobs = [('veil-roster.png', 'veil-roster-alpha.png', False),
            ('special-roster-additions.png', 'veil-special-alpha.png', True)]
    for original, target, lower_half in jobs:
        source_path, output = ART / original, ART / target
        if output.exists():
            raise FileExistsError(output)
        digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        with Image.open(source_path) as source:
            image = source.convert('RGB')
        if lower_half:
            # Source row 605..617 is empty; the Veil wing begins at 618,
            # above the nominal 627 split. Use the verified empty gutter.
            if image.size != (1254, 1254):
                raise ValueError('Re-review the special atlas crop for changed source dimensions')
            image = image.crop((0, 610, image.width, image.height))
        result = cutout(image)
        if not lower_half:
            if image.size != (1774, 887):
                raise ValueError('Re-review priest protection for changed atlas dimensions')
            # Pale grub anatomy is connected to paper: protect its whole cell.
            # Residual paper is preferable to removing the creature's exterior.
            priest = (1330, 0, image.width, 444)
            priest_threshold = np.full((444, image.width - 1330), 210)
            # Reviewed ground strip below the pale body; keep dark leg tips.
            priest_threshold[405:, 150:] = 140
            result.paste(cutout(image.crop(priest), minimum=priest_threshold), priest)
        result = soften_edges(result)
        result.save(output)
        assert hashlib.sha256(source_path.read_bytes()).hexdigest() == digest
        assert result.convert('RGB').tobytes() == image.tobytes()
        print(target, result.size, 'transparent=', result.getchannel('A').histogram()[0],
              'sha256=', hashlib.sha256(output.read_bytes()).hexdigest())

if __name__ == '__main__':
    main()
