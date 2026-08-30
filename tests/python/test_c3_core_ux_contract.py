from __future__ import annotations

import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_c3_core_ux import PROOF_RUN, REQUIRED_FILES, validate  # noqa: E402


class C3CoreUxContractTests(unittest.TestCase):
    """Protect runtime contracts plus the current v4.7/historical evidence boundary."""

    def _copy_contract_files(self, destination: pathlib.Path) -> None:
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def _mutate(self, root: pathlib.Path, relative: str, old: str, new: str) -> None:
        path = root / relative
        body = path.read_text(encoding="utf-8")
        self.assertIn(old, body, f"mutation source missing: {relative} -> {old}")
        path.write_text(body.replace(old, new, 1), encoding="utf-8")

    def _mutate_all(self, root: pathlib.Path, relative: str, old: str, new: str) -> None:
        path = root / relative
        body = path.read_text(encoding="utf-8")
        self.assertIn(old, body, f"mutation source missing: {relative} -> {old}")
        path.write_text(body.replace(old, new), encoding="utf-8")

    def _errors_after(self, relative: str, old: str, new: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(root, relative, old, new)
            return validate(root)

    def _errors_after_all(self, relative: str, old: str, new: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate_all(root, relative, old, new)
            return validate(root)

    def test_current_tree_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_token_ledger_removal_is_rejected(self) -> None:
        errors = self._errors_after("scripts/core/core_ux_service.gd", '"token_ledger"', '"ledger_removed"')
        self.assertTrue(any("token_ledger" in error for error in errors))

    def test_untyped_preview_sources_are_rejected(self) -> None:
        errors = self._errors_after("scripts/core/core_ux_service.gd", "var preview_sources: Array[Dictionary] = []", "var preview_sources := []")
        self.assertTrue(any("preview_sources" in error for error in errors))

    def test_explicit_stage_run_type_preload_removal_is_rejected(self) -> None:
        errors = self._errors_after("scripts/core/stage_run.gd", 'const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")', "# removed explicit UnitSpawnDefinition dependency")
        self.assertTrue(any("UnitSpawnDefinition" in error for error in errors))

    def test_false_pass_guard_removal_is_rejected(self) -> None:
        errors = self._errors_after("tests/headless/c3_core_ux_test.gd", "func _test_script_instantiation", "func _removed_script_instantiation")
        self.assertTrue(any("script_instantiation" in error for error in errors))

    def test_building_snapshot_api_removal_is_rejected(self) -> None:
        errors = self._errors_after("scripts/buildings/building_service.gd", "func roulette_token_sources_snapshot()", "func removed_token_sources_snapshot()")
        self.assertTrue(any("roulette_token_sources_snapshot" in error for error in errors))

    def test_mutating_building_query_in_core_ux_is_rejected(self) -> None:
        errors = self._errors_after("scripts/core/core_ux_service.gd", "run.buildings.roulette_token_sources_snapshot()", "run.buildings.roulette_token_sources()")
        self.assertTrue(any("mutating query path" in error for error in errors))

    def test_source_based_probability_api_removal_is_rejected(self) -> None:
        errors = self._errors_after("scripts/roulette/roulette_service.gd", "func probability_for_symbol_from_sources(", "func removed_probability_from_sources(")
        self.assertTrue(any("probability_for_symbol_from_sources" in error for error in errors))

    def test_read_only_headless_regression_removal_is_rejected(self) -> None:
        phrase = "C3 snapshot does not change global roster activation"
        errors = self._errors_after("tests/headless/c3_core_ux_test.gd", phrase, "removed read-only check")
        self.assertTrue(any("global roster activation" in error for error in errors))

    def test_boundary_regression_removal_is_rejected(self) -> None:
        phrase = "construction comparison exposes insufficient gold without mutating state"
        errors = self._errors_after("tests/headless/c3_core_ux_test.gd", phrase, "removed boundary check")
        self.assertTrue(any("insufficient gold" in error for error in errors))

    def test_hud_domain_calculation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            hud = root / "scripts/ui/stage_hud.gd"
            hud.write_text(hud.read_text(encoding="utf-8") + "\n# X_WEIGHT\n", encoding="utf-8")
            self.assertTrue(any("HUD improperly owns domain calculation" in error for error in validate(root)))

    def test_hud_source_evidence_removal_is_rejected(self) -> None:
        errors = self._errors_after("scripts/ui/stage_hud.gd", 'entry.get("source_building_ids"', 'entry.get("removed_source_ids"')
        self.assertTrue(any("source_building_ids" in error for error in errors))

    def test_c1u_leak_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            stage_run = root / "scripts/core/stage_run.gd"
            stage_run.write_text(stage_run.read_text(encoding="utf-8") + "\nfunc grant_move_token() -> void:\n\tpass\n", encoding="utf-8")
            self.assertTrue(any("C1U implementation leaked" in error for error in validate(root)))

    def test_missing_hud_surface_is_rejected(self) -> None:
        errors = self._errors_after("scenes/ui/stage_hud.tscn", 'name="WaveReportLabel"', 'name="WaveReportRemoved"')
        self.assertTrue(any("WaveReportLabel" in error for error in errors))

    def test_missing_staged_omen_regression_is_rejected(self) -> None:
        errors = self._errors_after("scripts/waves/wave_director.gd", "OMEN_T5_SECONDS", "OMEN_LAST_SECONDS")
        self.assertTrue(any("OMEN_T5_SECONDS" in error for error in errors))

    def test_final_workflow_timeout_removal_is_rejected(self) -> None:
        errors = self._errors_after(".github/workflows/validate-omenward-core.yml", "timeout 60s", "godot-without-bound")
        self.assertTrue(any("timeout 60s" in error for error in errors))

    def test_temporary_finalizer_workflow_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            temporary = root / ".github/workflows/finalize-c3-proof.yml"
            temporary.parent.mkdir(parents=True, exist_ok=True)
            temporary.write_text("name: temporary\n", encoding="utf-8")
            self.assertTrue(any("temporary C3 artifact" in error for error in validate(root)))

    def test_superseded_core_workflow_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            temporary = root / ".github/workflows/core-contracts.yml"
            temporary.parent.mkdir(parents=True, exist_ok=True)
            temporary.write_text("name: duplicate\n", encoding="utf-8")
            self.assertTrue(any("temporary C3 artifact" in error for error in validate(root)))

    def test_historical_c3_audit_state_regression_is_rejected(self) -> None:
        errors = self._errors_after("docs/C3_CORE_UX_AUDIT_2026-07-23.md", "C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING", "C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING")
        self.assertTrue(errors)

    def test_current_readme_historical_boundary_loss_is_rejected(self) -> None:
        errors = self._errors_after_all("README.md", "LEGACY_C1_C2_C3_PROVEN", "LEGACY_PROOF_REMOVED")
        self.assertTrue(any("README.md" in error and "LEGACY_C1_C2_C3_PROVEN" in error for error in errors))

    def test_current_status_boundary_loss_is_rejected(self) -> None:
        errors = self._errors_after_all("docs/CURRENT_IMPLEMENTATION_STATUS.md", "LEGACY_C1_C2_C3_PROVEN", "LEGACY_C3_PROOF_REMOVED")
        self.assertTrue(any("CURRENT_IMPLEMENTATION_STATUS.md" in error for error in errors))

    def test_current_status_runtime_ceiling_loss_is_rejected(self) -> None:
        errors = self._errors_after("docs/CURRENT_IMPLEMENTATION_STATUS.md", "CURRENT_GODOT_RUNTIME = PARTIAL__BATTLE_PRIMARY_MACHINE_VERIFIED__RUNTIME_NOT_RUN", "CURRENT_GODOT_RUNTIME = PASS")
        self.assertTrue(any("CURRENT_IMPLEMENTATION_STATUS.md" in error for error in errors))

    def test_current_v2_gdd_version_regression_is_rejected(self) -> None:
        errors = self._errors_after("docs/OMENWARD_GAME_DESIGN.md", "문서 버전: **v0.26", "문서 버전: **v0.25")
        self.assertTrue(errors)

    def test_current_v2_product_authority_loss_is_rejected(self) -> None:
        errors = self._errors_after("docs/OMENWARD_GAME_DESIGN.md", "PRODUCT_CODE_NOT_AUTHORIZED", "PRODUCT_CODE_AUTHORITY_REMOVED")
        self.assertTrue(any("PRODUCT_CODE_NOT_AUTHORIZED" in error for error in errors))

    def test_historical_c3_exact_run_cannot_regress(self) -> None:
        errors = self._errors_after_all("docs/C3_CORE_UX_AUDIT_2026-07-23.md", PROOF_RUN, "29900000000")
        self.assertTrue(any("C3 audit" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
