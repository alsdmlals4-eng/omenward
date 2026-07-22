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

    def _mutate(self, root: pathlib.Path, relative: str, old: str, new: str) -> None:
        path = root / relative
        body = path.read_text(encoding="utf-8")
        self.assertIn(old, body, f"mutation source missing: {relative} -> {old}")
        path.write_text(body.replace(old, new, 1), encoding="utf-8")

    def test_current_tree_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_token_ledger_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "scripts/core/core_ux_service.gd",
                '"token_ledger"',
                '"ledger_removed"',
            )
            self.assertTrue(any("token_ledger" in error for error in validate(root)))

    def test_untyped_preview_sources_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "scripts/core/core_ux_service.gd",
                "var preview_sources: Array[Dictionary] = []",
                "var preview_sources := []",
            )
            self.assertTrue(any("preview_sources" in error for error in validate(root)))

    def test_explicit_stage_run_type_preload_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "scripts/core/stage_run.gd",
                'const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")',
                "# removed explicit UnitSpawnDefinition dependency",
            )
            self.assertTrue(any("UnitSpawnDefinition" in error for error in validate(root)))

    def test_false_pass_guard_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "tests/headless/c3_core_ux_test.gd",
                "func _test_script_instantiation",
                "func _removed_script_instantiation",
            )
            self.assertTrue(any("script_instantiation" in error for error in validate(root)))

    def test_boundary_regression_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            phrase = "construction comparison exposes insufficient gold without mutating state"
            self._mutate(root, "tests/headless/c3_core_ux_test.gd", phrase, "removed boundary check")
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
            self._mutate(
                root,
                "scripts/ui/stage_hud.gd",
                'entry.get("source_building_ids"',
                'entry.get("removed_source_ids"',
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
            self._mutate(
                root,
                "scenes/ui/stage_hud.tscn",
                'name="WaveReportLabel"',
                'name="WaveReportRemoved"',
            )
            self.assertTrue(any("WaveReportLabel" in error for error in validate(root)))

    def test_missing_staged_omen_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "scripts/waves/wave_director.gd",
                "OMEN_T5_SECONDS",
                "OMEN_LAST_SECONDS",
            )
            self.assertTrue(any("OMEN_T5_SECONDS" in error for error in validate(root)))

    def test_godot_timeout_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                ".github/workflows/validate-core-contracts.yml",
                "timeout 60s",
                "godot-without-bound",
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

    def test_temporary_doc_sync_script_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            temporary = root / "tools/sync_c3_canonical_docs.py"
            temporary.parent.mkdir(parents=True, exist_ok=True)
            temporary.write_text("# temporary\n", encoding="utf-8")
            self.assertTrue(any("temporary C3 artifact" in error for error in validate(root)))

    def test_audit_preimplementation_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
                "C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING",
                "C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING",
            )
            self.assertTrue(any("stale or forbidden" in error for error in validate(root)))

    def test_readme_stale_next_implementation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            readme = root / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n→ [다음 구현] C3 승인 코어 UX 6종\n",
                encoding="utf-8",
            )
            self.assertTrue(any("stale or forbidden" in error for error in validate(root)))

    def test_documentation_map_c3_route_removal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "docs/DOCUMENTATION_MAP.md",
                "C3 코어 UX 구현·검증 계약",
                "removed C3 route",
            )
            self.assertTrue(any("C3 코어 UX 구현·검증 계약" in error for error in validate(root)))

    def test_gdd_version_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "docs/OMENWARD_GAME_DESIGN.md",
                "문서 버전: **v0.23**",
                "문서 버전: **v0.22**",
            )
            errors = validate(root)
            self.assertTrue(any("v0.23" in error or "stale or forbidden" in error for error in errors))

    def test_gdd_approved_battle_value_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "docs/OMENWARD_GAME_DESIGN.md",
                "공성 태그 피해 200%",
                "removed siege multiplier",
            )
            self.assertTrue(any("공성 태그 피해 200%" in error for error in validate(root)))

    def test_gdd_truncation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            gdd = root / "docs/OMENWARD_GAME_DESIGN.md"
            gdd.write_text(gdd.read_text(encoding="utf-8")[:8000], encoding="utf-8")
            self.assertTrue(any("GDD appears truncated" in error for error in validate(root)))

    def test_roadmap_section_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(root, "docs/OMENWARD_ROADMAP.md", "## 11. P4", "## removed P4")
            self.assertTrue(any("roadmap lost required section 11" in error for error in validate(root)))

    def test_roadmap_stale_c3_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            roadmap = root / "docs/OMENWARD_ROADMAP.md"
            roadmap.write_text(
                roadmap.read_text(encoding="utf-8") + "\nC3 코어 UX 다음 구현\n",
                encoding="utf-8",
            )
            self.assertTrue(any("stale or forbidden" in error for error in validate(root)))

    def test_decision_fallback_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "docs/DECISIONS_PENDING.md",
                "640×360 논리 화면 대안",
                "removed resolution fallback",
            )
            self.assertTrue(any("640×360 논리 화면 대안" in error for error in validate(root)))

    def test_decision_c1u_option_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            self._mutate(
                root,
                "docs/DECISIONS_PENDING.md",
                "이동권 심벌 완성선의 정확한 지급량",
                "removed move-token decision",
            )
            self.assertTrue(any("이동권 심벌 완성선" in error for error in validate(root)))

    def test_duplicate_c2_validation_command_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            validation = root / "docs/VERTICAL_SLICE_VALIDATION.md"
            validation.write_text(
                validation.read_text(encoding="utf-8")
                + "\npython tools/validate_c2_battle_objective.py\n",
                encoding="utf-8",
            )
            self.assertTrue(any("C2 validator exactly once" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
