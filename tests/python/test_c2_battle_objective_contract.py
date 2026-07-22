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
            "README.md",
            "AGENTS.md",
            "docs/ACTIVE_CONTEXT.md",
            "docs/HANDOFF_CONTEXT.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/OMENWARD_GAME_DESIGN.md",
            "docs/OMENWARD_ROADMAP.md",
            "docs/DECISIONS_PENDING.md",
            "docs/DOCUMENTATION_MAP.md",
            "docs/VERTICAL_SLICE_VALIDATION.md",
            "docs/GODOT_PROJECT_STRUCTURE.md",
            "docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md",
            "docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md",
            "docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md",
            "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
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

    def test_stale_pr49_current_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            roadmap = root / "docs/OMENWARD_ROADMAP.md"
            roadmap.write_text(roadmap.read_text(encoding="utf-8") + "\nPR #49 사용자 검토 대기\n", encoding="utf-8")
            self.assertTrue(any("stale C1/C2 state" in error for error in validate(root)))

    def test_missing_c2_candidate_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            status = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
            status.write_text(status.read_text(encoding="utf-8").replace("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_STATE_REMOVED"), encoding="utf-8")
            self.assertTrue(any("missing C2 candidate state" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
