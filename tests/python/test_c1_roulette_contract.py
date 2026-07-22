from __future__ import annotations

import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_c1_roulette import REQUIRED_FILES, validate  # noqa: E402


class C1RouletteValidationTests(unittest.TestCase):
    def _copy_contract_files(self, destination: pathlib.Path) -> None:
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        for relative in (
            "scripts/core/stage_run.gd",
            "tests/headless/economy_roulette_test.gd",
            "docs/OMENWARD_GAME_DESIGN.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/OMENWARD_ROADMAP.md",
            "docs/design/APPROVED_ROULETTE_CORE_RULES.md",
            "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
            "README.md",
            "AGENTS.md",
        ):
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def test_current_tree_passes(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_direct_nine_card_placeholder_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            roulette = root / "scripts" / "roulette" / "roulette_service.gd"
            roulette.write_text(roulette.read_text(encoding="utf-8") + "\n# return cards\n", encoding="utf-8")
            self.assertTrue(any("nine-card placeholder" in error for error in validate(root)))

    def test_retired_work_order_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            readme = root / "README.md"
            readme.write_text(readme.read_text(encoding="utf-8") + "\n`docs/work_orders/0001-phase-0-codex-plan-mode.md`\n", encoding="utf-8")
            self.assertTrue(any("retired execution input" in error for error in validate(root)))

    def test_pending_remote_validation_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            report = root / "docs" / "C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md"
            report.write_text(
                report.read_text(encoding="utf-8").replace(
                    "C1_ROULETTE_CORE_REMOTE_PROVEN",
                    "IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("pre-validation C1 state" in error or "missing proven C1 evidence" in error for error in validate(root)))

    def test_missing_judgment_line_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            test_file = root / "tests" / "headless" / "roulette_contract_test.gd"
            test_file.write_text(test_file.read_text(encoding="utf-8").replace("middle judgment line fails", "middle line omitted"), encoding="utf-8")
            self.assertTrue(any("middle judgment line fails" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
