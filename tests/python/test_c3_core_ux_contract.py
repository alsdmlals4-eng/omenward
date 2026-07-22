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
            service.write_text(
                service.read_text(encoding="utf-8").replace('"token_ledger"', '"ledger_removed"'),
                encoding="utf-8",
            )
            self.assertTrue(any("token_ledger" in error for error in validate(root)))

    def test_untyped_preview_sources_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            service = root / "scripts/core/core_ux_service.gd"
            service.write_text(
                service.read_text(encoding="utf-8").replace(
                    "var preview_sources: Array[Dictionary] = []",
                    "var preview_sources := []",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("preview_sources" in error for error in validate(root)))

    def test_explicit_stage_run_type_preload_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            stage_run = root / "scripts/core/stage_run.gd"
            stage_run.write_text(
                stage_run.read_text(encoding="utf-8").replace(
                    'const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")',
                    "# removed explicit UnitSpawnDefinition dependency",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("UnitSpawnDefinition" in error for error in validate(root)))

    def test_false_pass_guard_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            headless = root / "tests/headless/c3_core_ux_test.gd"
            headless.write_text(
                headless.read_text(encoding="utf-8").replace(
                    "func _test_script_instantiation",
                    "func _removed_script_instantiation",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("script_instantiation" in error for error in validate(root)))

    def test_boundary_regression_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            headless = root / "tests/headless/c3_core_ux_test.gd"
            phrase = "construction comparison exposes insufficient gold without mutating state"
            headless.write_text(
                headless.read_text(encoding="utf-8").replace(phrase, "removed boundary check"),
                encoding="utf-8",
            )
            self.assertTrue(any("insufficient gold" in error for error in validate(root)))

    def test_hud_domain_calculation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            hud = root / "scripts/ui/stage_hud.gd"
            hud.write_text(hud.read_text(encoding="utf-8") + "\n# X_WEIGHT\n", encoding="utf-8")
            self.assertTrue(any("HUD improperly owns domain calculation" in error for error in validate(root)))

    def test_hud_source_evidence_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            hud = root / "scripts/ui/stage_hud.gd"
            hud.write_text(
                hud.read_text(encoding="utf-8").replace(
                    'entry.get("source_building_ids"',
                    'entry.get("removed_source_ids"',
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("source_building_ids" in error for error in validate(root)))

    def test_c1u_leak_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            stage_run = root / "scripts/core/stage_run.gd"
            stage_run.write_text(
                stage_run.read_text(encoding="utf-8") + "\nfunc grant_move_token() -> void:\n\tpass\n",
                encoding="utf-8",
            )
            self.assertTrue(any("C1U implementation leaked" in error for error in validate(root)))

    def test_missing_hud_surface_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            scene = root / "scenes/ui/stage_hud.tscn"
            scene.write_text(
                scene.read_text(encoding="utf-8").replace(
                    'name="WaveReportLabel"', 'name="WaveReportRemoved"'
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("WaveReportLabel" in error for error in validate(root)))

    def test_missing_staged_omen_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            wave = root / "scripts/waves/wave_director.gd"
            wave.write_text(
                wave.read_text(encoding="utf-8").replace("OMEN_T5_SECONDS", "OMEN_LAST_SECONDS"),
                encoding="utf-8",
            )
            self.assertTrue(any("OMEN_T5_SECONDS" in error for error in validate(root)))

    def test_godot_timeout_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            workflow = root / ".github/workflows/validate-core-contracts.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace("timeout 60s", "godot-without-bound", 1),
                encoding="utf-8",
            )
            self.assertTrue(any("timeout 60s" in error for error in validate(root)))

    def test_temporary_hyphenated_workflow_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            temporary = root / ".github/workflows/diagnose-c3-headless.yml"
            temporary.parent.mkdir(parents=True, exist_ok=True)
            temporary.write_text("name: temporary\n", encoding="utf-8")
            self.assertTrue(any("temporary C3 artifact" in error for error in validate(root)))

    def test_audit_preimplementation_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            audit = root / "docs/C3_CORE_UX_AUDIT_2026-07-23.md"
            audit.write_text(
                audit.read_text(encoding="utf-8").replace(
                    "C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING",
                    "C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("pre-implementation" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
