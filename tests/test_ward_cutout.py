from pathlib import Path
import unittest
from PIL import Image

ART = Path(__file__).resolve().parents[1] / 'docs/images/candidates/blueprint-20260911'

class WardCutoutTests(unittest.TestCase):
    def test_source_rgb_is_preserved_with_real_alpha(self):
        for source, target, crop in [
            ('ward-roster.png', 'ward-roster-alpha.png', None),
            ('special-roster-additions.png', 'ward-special-alpha.png', (0, 0, 1254, 610)),
            ('building-tree.png', 'building-tree-alpha.png', None),
        ]:
            with self.subTest(target=target):
                self.assertTrue((ART / target).exists(), 'Missing transparent runtime derivative')
                with Image.open(ART / source) as original, Image.open(ART / target) as result:
                    expected = original.convert('RGB')
                    if crop:
                        expected = expected.crop(crop)
                    self.assertEqual(result.mode, 'RGBA')
                    self.assertEqual(result.size, expected.size)
                    self.assertEqual(result.convert('RGB').tobytes(), expected.tobytes())
                    self.assertGreater(result.getchannel('A').histogram()[0], result.width * result.height * .15)
                    self.assertEqual(result.getpixel((0, 0))[3], 0)

    def test_pale_robes_and_wings_are_not_background(self):
        for target, points in [
            ('ward-roster-alpha.png', [(1510, 115), (1565, 350)]),
            ('ward-special-alpha.png', [(760, 120), (1100, 365)]),
        ]:
            self.assertTrue((ART / target).exists(), 'Missing pale-subject derivative')
            with Image.open(ART / target) as result:
                for point in points:
                    self.assertGreater(result.getpixel(point)[3], 240, (target, point))

if __name__ == '__main__':
    unittest.main()
