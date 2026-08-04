from __future__ import annotations

import pathlib
import re
import runpy
import shutil
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODULE = runpy.run_path(str(ROOT / "tools" / "validate_project_core_docs.py"))
validate = MODULE["validate"]
CURRENT_SPEC = MODULE["CURRENT_SPEC"]
CURRENT_REVIEW = MODULE["CURRENT_REVIEW"]
EVIDENCE_PILOT = MODULE["EVIDENCE_PILOT"]
LEDGER = MODULE["LEDGER"]
LEGENDARY_DEPLOYMENT_POLICY = MODULE["LEGENDARY_DEPLOYMENT_POLICY"]
ROULETTE_RULES = MODULE["ROULETTE_RULES"]


class CurrentVerticalSliceDocumentationTests(unittest.TestCase):
    def test_current_repository_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_current_spec_route_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/PROJECT_CORE.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    pathlib.PurePosixPath(CURRENT_SPEC).name,
                    "CURRENT_SPEC_REMOVED.md",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("current Vertical Slice" in error for error in validate(root)))

    def test_latest_implementation_boundary_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED",
                    "VERTICAL_SLICE_IMPLEMENTATION_UNKNOWN",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("implementation" in error for error in validate(root)))

    def test_legacy_and_latest_status_must_remain_separate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN",
                    "LEGACY_C1_EVIDENCE_REMOVED",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("Legacy C1" in error for error in validate(root)))

    def test_evidence_pilot_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / EVIDENCE_PILOT).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_pilot_non_canon_boundary_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/DOCUMENTATION_MAP.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "PILOT_RECOMMENDATION / NOT_CANON",
                    "PILOT_CANONIZED_WITHOUT_APPROVAL",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("non-canon" in error for error in validate(root)))

    def test_pilot_implementation_boundary_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / EVIDENCE_PILOT
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "implementation_authority: NONE",
                    "implementation_authority: GRANTED",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("Evidence Pilot" in error for error in validate(root)))

    def test_v2_decision_lineage_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / LEDGER
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "AUTHORED_PRIORITY_LIST",
                    "PRIORITY_LINEAGE_REMOVED",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("V2 decision lineage" in error for error in validate(root)))

    def test_legendary_policy_contract_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / LEGENDARY_DEPLOYMENT_POLICY
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "COMMIT_TIME_REVALIDATION: REQUIRED",
                    "COMMIT_REVALIDATION_REMOVED",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("legendary deployment" in error for error in validate(root)))

    def test_horizontal_cursor_contract_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / ROULETTE_RULES
            path.write_text(
                path.read_text(encoding="utf-8").replace("노출 인덱스", "삭제된 인덱스"),
                encoding="utf-8",
            )
            self.assertTrue(any("horizontal movement" in error for error in validate(root)))

    def test_active_context_self_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\ncurrent_branch_and_commit: forbidden-self-reference\n",
                encoding="utf-8",
            )
            self.assertTrue(any("self-referential" in error for error in validate(root)))

    def test_active_context_fixed_current_main_sha_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            text = re.sub(
                r"(?m)^current_main:.*$",
                f"current_main: {'a' * 40}",
                path.read_text(encoding="utf-8"),
            )
            path.write_text(text, encoding="utf-8")
            self.assertTrue(
                any("current_main must resolve dynamically" in error for error in validate(root))
            )

    def test_active_context_fixed_baseline_sha_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            text = re.sub(
                r"(?m)^context_baseline_commit:.*$",
                f"context_baseline_commit: {'b' * 40}",
                path.read_text(encoding="utf-8"),
            )
            path.write_text(text, encoding="utf-8")
            self.assertTrue(
                any(
                    "context_baseline_commit must resolve dynamically" in error
                    for error in validate(root)
                )
            )

    def test_document_lifecycle_registry_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
            if path.exists():
                path.unlink()
            self.assertTrue(any("lifecycle registry" in error for error in validate(root)))

    def test_legacy_master_gdd_requires_superseded_marker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/OMENWARD_GAME_DESIGN.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace("[대체됨]", ""),
                encoding="utf-8",
            )
            self.assertTrue(any("legacy GDD" in error for error in validate(root)))

    def test_project_core_rejects_legacy_food_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/PROJECT_CORE.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nstorage_selling_food\n",
                encoding="utf-8",
            )
            self.assertTrue(any("legacy core marker" in error for error in validate(root)))

    def test_exact_premature_completion_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "README.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nVERTICAL_SLICE_PROVEN\n",
                encoding="utf-8",
            )
            self.assertTrue(any("premature completion" in error for error in validate(root)))

    def test_broken_local_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / EVIDENCE_PILOT
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
