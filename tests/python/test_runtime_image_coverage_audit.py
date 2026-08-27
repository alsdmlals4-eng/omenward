from __future__ import annotations

import pathlib
import runpy
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
AUDIT_PATH = ROOT / "tools" / "audit_runtime_image_coverage.py"


class RuntimeImageCoverageAuditTests(unittest.TestCase):
    def test_current_runtime_image_consumers_are_covered(self) -> None:
        self.assertTrue(AUDIT_PATH.is_file(), "the runtime image coverage audit must exist")
        module = runpy.run_path(str(AUDIT_PATH))
        self.assertEqual([], module["audit"](ROOT))

    def test_missing_unit_texture_is_reported(self) -> None:
        module = runpy.run_path(str(AUDIT_PATH))
        with self.subTest("unit texture"):
            self.assertTrue(any("missing unit texture" in error for error in module["audit"](ROOT / "does-not-exist")))


if __name__ == "__main__":
    unittest.main()
