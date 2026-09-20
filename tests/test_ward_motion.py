import importlib.util
from pathlib import Path
import unittest
import json
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

class WardMotionTests(unittest.TestCase):
    def test_separate_and_align_without_losing_visible_pixels(self):
        path = ROOT / 'tools/ward_motion.py'
        self.assertTrue(path.exists(), 'Missing source-preserving pose extraction')
        spec = importlib.util.spec_from_file_location('ward_motion', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        source = Image.open(ROOT / 'docs/images/candidates/blueprint-20260911/ward-shield-slash-alpha-candidate.png').convert('RGBA')
        frames, records = module.prepare(source)
        self.assertEqual(len(frames), 4)
        rebuilt = np.zeros_like(np.array(source))
        for frame, record in zip(frames, records):
            self.assertEqual(frame.size, (768, 768))
            pixels = np.array(frame)
            ys, xs = np.where(pixels[:, :, 3] > 0)
            self.assertGreater(xs.min(), 0)
            self.assertLess(xs.max(), 767)
            self.assertGreater(ys.min(), 0)
            self.assertLess(ys.max(), 767)
            dx, dy = record['offset']
            self.assertTrue(np.all(rebuilt[ys-dy, xs-dx, 3] == 0), 'Poses overlap')
            rebuilt[ys-dy, xs-dx] = pixels[ys, xs]
            self.assertEqual(record['source_pivot'][1] + dy, 700)
            self.assertEqual(record['source_pivot'][0] + dx, 384)
        original = np.array(source)
        visible = original[:, :, 3] > 8
        self.assertTrue(np.array_equal(rebuilt[visible], original[visible]), 'Visible source pixels lost or recolored')

    def test_native_export_contains_each_pose_once_without_cel_overlay(self):
        spec = importlib.util.spec_from_file_location('ward_motion', ROOT / 'tools/ward_motion.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        folder = ROOT / 'docs/images/candidates/blueprint-20260911'
        with Image.open(module.SOURCE) as source:
            frames, _ = module.prepare(source)
        with Image.open(folder / 'ward-shield-motion.png') as atlas:
            self.assertEqual(atlas.mode, 'RGBA')
            self.assertEqual(atlas.size, (3072, 768))
            for index, pose in enumerate(frames):
                self.assertEqual(atlas.crop((index*768, 0, (index+1)*768, 768)).tobytes(), pose.tobytes())
        metadata = json.loads((folder / 'ward-shield-motion.json').read_text())
        self.assertTrue((folder / metadata['meta']['image']).is_file())
        self.assertEqual([frame['duration'] for frame in metadata['frames']], [400, 180, 100, 150])

if __name__ == '__main__':
    unittest.main()
