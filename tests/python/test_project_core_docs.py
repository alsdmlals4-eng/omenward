from __future__ import annotations

import pathlib
import runpy
import shutil
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODULE = runpy.run_path(str(ROOT / "tools" / "validate_project_core_docs.py"))
validate = MODULE["validate"]


class ProjectCoreDocumentationTests(unittest.TestCase):
    def test_current_repository_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_stale_completion_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_contract_files(temp_root)
            readme = temp_root / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n플레이 가능한 수직 슬라이스 구현 완료\n",
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("stale current-state claim" in error for error in errors))

    def test_missing_core_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_contract_files(temp_root)
            active = temp_root / "docs" / "ACTIVE_CONTEXT.md"
            active.write_text(
                active.read_text(encoding="utf-8").replace("PROJECT_CORE.md", "PROJECT_CORE_REMOVED.md"),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("does not reference PROJECT_CORE.md" in error for error in errors))

    def _copy_contract_files(self, destination: pathlib.Path) -> None:
        for relative in MODULE["REQUIRED_FILES"]:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


if __name__ == "__main__":
    unittest.main()
