from __future__ import annotations

import pathlib
import runpy
import shutil
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODULE = runpy.run_path(str(ROOT / "tools" / "validate_project_core_docs.py"))
validate = MODULE["validate"]
LEDGER = MODULE["LEDGER"]
HISTORICAL_PLAN = MODULE["HISTORICAL_PLAN"]


class ProjectCoreV2DocumentationTests(unittest.TestCase):
    def test_current_repository_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_missing_v2_status_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            for relative in (
                "docs/PROJECT_CORE.md",
                "docs/CURRENT_IMPLEMENTATION_STATUS.md",
                "docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md",
            ):
                path = root / relative
                path.write_text(
                    path.read_text(encoding="utf-8").replace(
                        "V2_CANON_CURRENT_BY_PR_57_MERGE",
                        "V2_CANON_REMOVED",
                    ),
                    encoding="utf-8",
                )
            self.assertTrue(any("missing V2 contract" in error for error in validate(root)))

    def test_horizontal_cursor_contract_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/design/APPROVED_ROULETTE_CORE_RULES.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "노출 인덱스",
                    "삭제된 인덱스",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("horizontal movement" in error for error in validate(root)))

    def test_legacy_and_v2_status_must_be_separated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "V2_IMPLEMENTATION_NOT_STARTED",
                    "V2_IMPLEMENTATION_UNKNOWN",
                ),
                encoding="utf-8",
            )
            self.assertTrue(
                any(
                    "separate V2" in error or "missing V2 contract" in error
                    for error in validate(root)
                )
            )

    def test_documentation_map_owner_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/DOCUMENTATION_MAP.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "APPROVED_ROULETTE_CORE_RULES.md",
                    "ROULETTE_OWNER_REMOVED.md",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("documentation map missing" in error for error in validate(root)))

    def test_decision_ledger_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / LEDGER).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_decision_ledger_contract_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / LEDGER
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "AUTHORED_PRIORITY_LIST",
                    "REMOVED_PRIORITY_CONTRACT",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("decision ledger missing contract" in error for error in validate(root)))

    def test_decision_ledger_precedence_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "충돌할 경우 해당 결정 원장이 우선",
                    "충돌 우선순위 제거",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("precedence" in error for error in validate(root)))

    def test_historical_plan_authority_marker_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / HISTORICAL_PLAN
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "REVALIDATION_REQUIRED",
                    "REVALIDATION_MARKER_REMOVED",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("authority marker" in error for error in validate(root)))

    def test_exact_premature_completion_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "README.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nCORE_LOCK_V2\n",
                encoding="utf-8",
            )
            self.assertTrue(any("claims premature completion" in error for error in validate(root)))

    def test_pending_completion_state_is_not_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            self.assertFalse(
                any("claims premature completion" in error for error in validate(root))
            )

    def test_baseline_main_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "5a9c02b0ed4757c379fd8dfcb89fcc362b8cf185",
                    "0000000000000000000000000000000000000000",
                    1,
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("baseline main mismatch" in error for error in validate(root)))

    def test_missing_required_file_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / "docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md").unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_broken_local_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/PROJECT_CORE.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\n[broken](missing/path.md)\n",
                encoding="utf-8",
            )
            self.assertTrue(any("broken local link" in error for error in validate(root)))

    def copy(self, destination: pathlib.Path) -> None:
        for relative in MODULE["REQUIRED_FILES"]:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


if __name__ == "__main__":
    unittest.main()
