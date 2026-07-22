from __future__ import annotations

import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_c2_battle_objective import REQUIRED_FILES, validate  # noqa: E402


class C2BattleObjectiveContractTests(unittest.TestCase):
    def _copy_contract_files(self, destination: pathlib.Path) -> None:
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        for relative in (
            "scripts/data/unit_archetype_profile.gd",
            "scripts/core/stage_economy.gd",
            "scripts/buildings/building_state.gd",
        ):
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def test_current_tree_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_external_only_result_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            stage = root / "scripts/core/stage_run.gd"
            stage.write_text(stage.read_text(encoding="utf-8").replace("_resolve_natural_result()", "# natural result removed"), encoding="utf-8")
            self.assertTrue(any("natural result" in error for error in validate(root)))

    def test_fractional_capture_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            outpost = root / "scripts/battle/outpost_state.gd"
            outpost.write_text(outpost.read_text(encoding="utf-8").replace("clampf(power, 0.0, MAX_CAPTURE_POWER)", "0.0"), encoding="utf-8")
            self.assertTrue(any("capture contract" in error for error in validate(root)))

    def test_line_gate_isolation_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            test_file = root / "tests/headless/c2_battle_objective_test.gd"
            test_file.write_text(test_file.read_text(encoding="utf-8").replace("other lane gates remain standing", "gate isolation omitted"), encoding="utf-8")
            self.assertTrue(any("other lane gates remain standing" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
