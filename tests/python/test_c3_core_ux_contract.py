from __future__ import annotations

import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_c3_core_ux import REQUIRED_FILES, validate  # noqa: E402


class C3CoreUxContractTests(unittest.TestCase):
    def _copy_contract_files(self, destination: pathlib.Path) -> None:
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def test_current_tree_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_token_ledger_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            service = root / "scripts/core/core_ux_service.gd"
            service.write_text(service.read_text(encoding="utf-8").replace('"token_ledger"', '"ledger_removed"'), encoding="utf-8")
            self.assertTrue(any("token_ledger" in error for error in validate(root)))

    def test_hud_domain_calculation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            hud = root / "scripts/ui/stage_hud.gd"
            hud.write_text(hud.read_text(encoding="utf-8") + "\n# X_WEIGHT\n", encoding="utf-8")
            self.assertTrue(any("HUD improperly owns domain calculation" in error for error in validate(root)))

    def test_c1u_leak_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            stage_run = root / "scripts/core/stage_run.gd"
            stage_run.write_text(stage_run.read_text(encoding="utf-8") + "\nfunc grant_move_token() -> void:\n\tpass\n", encoding="utf-8")
            self.assertTrue(any("C1U implementation leaked" in error for error in validate(root)))

    def test_missing_hud_surface_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            scene = root / "scenes/ui/stage_hud.tscn"
            scene.write_text(scene.read_text(encoding="utf-8").replace('name="WaveReportLabel"', 'name="WaveReportRemoved"'), encoding="utf-8")
            self.assertTrue(any("WaveReportLabel" in error for error in validate(root)))

    def test_missing_staged_omen_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            wave = root / "scripts/waves/wave_director.gd"
            wave.write_text(wave.read_text(encoding="utf-8").replace("OMEN_T5_SECONDS", "OMEN_LAST_SECONDS"), encoding="utf-8")
            self.assertTrue(any("OMEN_T5_SECONDS" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
