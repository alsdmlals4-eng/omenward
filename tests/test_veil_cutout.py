import importlib.util
from pathlib import Path
import unittest
from PIL import Image

class CutoutTests(unittest.TestCase):
    def test_priest_pale_exterior_survives(self):
        path = Path(__file__).resolve().parents[1] / 'docs/images/candidates/blueprint-20260911/veil-roster-alpha.png'
        with Image.open(path) as image:
            for point in [(1450, 100), (1480, 100)]:
                self.assertEqual(image.getpixel(point)[3], 255, point)
            self.assertGreater(image.getpixel((1415, 405))[3], 0, 'Lower magic glow must survive ground cleanup')

    def test_special_wing_is_not_cut_at_top(self):
        path = Path(__file__).resolve().parents[1] / 'docs/images/candidates/blueprint-20260911/veil-special-alpha.png'
        if not path.exists():
            self.skipTest('Run the candidate processor first')
        with Image.open(path) as image:
            self.assertEqual(image.getchannel('A').crop((0, 0, image.width, 1)).getextrema(), (0, 0))

    def test_priest_verified_background_pockets_are_clear(self):
        path = Path(__file__).resolve().parents[1] / 'docs/images/candidates/blueprint-20260911/veil-roster-alpha.png'
        with Image.open(path) as image:
            for point in [(1425, 32), (1530, 412)]:
                self.assertEqual(image.getpixel(point)[3], 0, point)

    def test_alpha_only_preserves_enclosed_pale_foreground(self):
        path = Path(__file__).resolve().parents[1] / 'tools/veil_cutout.py'
        self.assertTrue(path.exists(), 'Missing approved local alpha-only processor')
        spec = importlib.util.spec_from_file_location('cutout', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        source = Image.new('RGB', (9, 9), (248, 240, 224))
        for y in range(2, 7):
            for x in range(2, 7):
                source.putpixel((x, y), (30, 20, 50))
        source.putpixel((4, 4), (248, 240, 224))
        result = module.cutout(source)
        self.assertEqual(result.getpixel((0, 0))[3], 0)
        self.assertEqual(result.getpixel((4, 4))[3], 255)
        self.assertEqual(result.convert('RGB').tobytes(), source.tobytes())

    def test_edge_refinement_preserves_support_and_rgb(self):
        path = Path(__file__).resolve().parents[1] / 'tools/veil_cutout.py'
        spec = importlib.util.spec_from_file_location('cutout', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertTrue(hasattr(module, 'soften_edges'), 'Missing bounded alpha edge refinement')
        source = Image.new('RGBA', (15, 15), (248, 240, 224, 0))
        for y in range(3, 12):
            for x in range(3, 12):
                source.putpixel((x, y), (40, 25, 60, 255))
        source.putpixel((1, 1), (40, 25, 60, 255))  # Thin detached tip must survive.
        result = module.soften_edges(source)
        self.assertEqual(result.convert('RGB').tobytes(), source.convert('RGB').tobytes())
        self.assertEqual(result.getpixel((7, 7))[3], 255)
        self.assertGreater(result.getpixel((3, 3))[3], 0)
        self.assertLess(result.getpixel((3, 3))[3], 255)
        self.assertGreater(result.getpixel((1, 1))[3], 0)
        for before, after in zip(source.getchannel('A').tobytes(), result.getchannel('A').tobytes()):
            self.assertEqual(before > 0, after > 0)

if __name__ == '__main__':
    unittest.main()
