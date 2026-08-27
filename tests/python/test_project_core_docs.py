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
CURRENT_VISUAL_SPEC = MODULE["CURRENT_VISUAL_SPEC"]
CURRENT_VISUAL_ASSET = MODULE["CURRENT_VISUAL_ASSET"]
CURRENT_VISUAL_HANDOFF = MODULE["CURRENT_VISUAL_HANDOFF"]
FINAL_REVIEW = MODULE["FINAL_REVIEW"]
IMPLEMENTATION_PACKET = MODULE["IMPLEMENTATION_PACKET"]
IMPLEMENTATION_PLAN = MODULE["IMPLEMENTATION_PLAN"]
EVIDENCE_PILOT = MODULE["EVIDENCE_PILOT"]
LEDGER = MODULE["LEDGER"]
LEGENDARY_DEPLOYMENT_POLICY = MODULE["LEGENDARY_DEPLOYMENT_POLICY"]
ROULETTE_RULES = MODULE["ROULETTE_RULES"]
HISTORICAL_VERTICAL_SLICE = MODULE["HISTORICAL_VERTICAL_SLICE"]


class CurrentProjectCoreDocumentationTests(unittest.TestCase):
    def test_current_repository_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_current_decision_route_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/PROJECT_CORE.md"
            path.write_text(path.read_text(encoding="utf-8").replace(pathlib.PurePosixPath(CURRENT_SPEC).name, "CURRENT_SPEC_REMOVED.md"), encoding="utf-8")
            self.assertTrue(any("Project Core" in error or "current decision" in error for error in validate(root)))

    def test_current_runtime_ceiling_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            path.write_text(path.read_text(encoding="utf-8").replace("CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED", "CURRENT_GODOT_RUNTIME = PASS"), encoding="utf-8")
            self.assertTrue(any("CURRENT_GODOT_RUNTIME" in error for error in validate(root)))

    def test_visual_runtime_ceiling_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / CURRENT_VISUAL_ASSET
            path.write_text(path.read_text(encoding="utf-8").replace("runtime_readability: PARTIAL_TECHNICAL_HERA_CAPTURE__HUMAN_NOT_RUN", "runtime_readability: PASS"), encoding="utf-8")
            self.assertTrue(any("runtime_readability: PARTIAL_TECHNICAL_HERA_CAPTURE__HUMAN_NOT_RUN" in error for error in validate(root)))

    def test_legacy_and_current_status_must_remain_separate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
            path.write_text(path.read_text(encoding="utf-8").replace("LEGACY_C1_C2_C3_PROVEN", "LEGACY_PROOF_REMOVED"), encoding="utf-8")
            self.assertTrue(any("LEGACY_C1_C2_C3_PROVEN" in error for error in validate(root)))

    def test_decision_count_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / CURRENT_SPEC
            body = path.read_text(encoding="utf-8").replace(
                "CURRENT_APPROVED_REPLAN_DECISIONS = 22",
                "CURRENT_APPROVED_REPLAN_DECISIONS = 23",
                1,
            )
            path.write_text(body, encoding="utf-8")
            self.assertTrue(any("decision count mismatch" in error for error in validate(root)))

    def test_stale_pre_audit_north_star_gate_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "README.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nREBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST\n", encoding="utf-8")
            self.assertTrue(any("stale marker" in error for error in validate(root)))

    def test_final_review_owner_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / FINAL_REVIEW).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_visual_closeout_cannot_reactivate_execution_gate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            body = path.read_text(encoding="utf-8").replace(
                "CURRENT_NEXT = HUMAN_PLAYTEST_FOR_BATTLEFIELD_READABILITY_AND_ROULETTE_INSPECTION",
                "CURRENT_NEXT = RUN_COMMAND_VERTICAL_SLICE_EXECUTION",
                1,
            )
            path.write_text(body, encoding="utf-8")
            errors = validate(root)
            self.assertTrue(any("HUMAN_PLAYTEST_FOR_BATTLEFIELD_READABILITY_AND_ROULETTE_INSPECTION" in error for error in errors), errors)

    def test_scoped_implementation_authority_cannot_expand_project_wide(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            body = path.read_text(encoding="utf-8").replace(
                "implementation_scope: RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE",
                "implementation_scope: ALL_PRODUCT_IMPLEMENTATION",
                1,
            )
            path.write_text(body, encoding="utf-8")
            errors = validate(root)
            self.assertTrue(any("RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE" in error for error in errors), errors)

    def test_current_visual_spec_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / CURRENT_VISUAL_SPEC).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_current_visual_asset_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / CURRENT_VISUAL_ASSET).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_current_visual_handoff_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / CURRENT_VISUAL_HANDOFF).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_implementation_packet_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / IMPLEMENTATION_PACKET).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_implementation_plan_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / IMPLEMENTATION_PLAN).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_final_review_remains_historical_pre_implementation_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / FINAL_REVIEW
            path.write_text(
                path.read_text(encoding="utf-8").replace("IMPLEMENTATION_AUTHORITY = NONE", "IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED"),
                encoding="utf-8",
            )
            self.assertTrue(any("final planning review" in error for error in validate(root)))

    def test_final_review_cannot_promote_runtime_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / FINAL_REVIEW
            path.write_text(
                path.read_text(encoding="utf-8").replace("CURRENT_GODOT_RUNTIME = NOT_RUN", "CURRENT_GODOT_RUNTIME = PASS", 1),
                encoding="utf-8",
            )
            self.assertTrue(any("CURRENT_GODOT_RUNTIME" in error for error in validate(root)))

    def test_evidence_pilot_is_required_as_history(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            (root / EVIDENCE_PILOT).unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_pilot_implementation_boundary_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / EVIDENCE_PILOT
            path.write_text(path.read_text(encoding="utf-8").replace("implementation_authority: NONE", "implementation_authority: GRANTED"), encoding="utf-8")
            self.assertTrue(any("Evidence Pilot" in error for error in validate(root)))

    def test_v2_decision_lineage_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / LEDGER
            path.write_text(path.read_text(encoding="utf-8").replace("AUTHORED_PRIORITY_LIST", "PRIORITY_LINEAGE_REMOVED"), encoding="utf-8")
            self.assertTrue(any("V2 decision lineage" in error for error in validate(root)))

    def test_legendary_policy_contract_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / LEGENDARY_DEPLOYMENT_POLICY
            path.write_text(path.read_text(encoding="utf-8").replace("COMMIT_TIME_REVALIDATION: REQUIRED", "COMMIT_REVALIDATION_REMOVED"), encoding="utf-8")
            self.assertTrue(any("legendary deployment" in error for error in validate(root)))

    def test_horizontal_cursor_contract_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / ROULETTE_RULES
            path.write_text(path.read_text(encoding="utf-8").replace("노출 인덱스", "삭제된 인덱스"), encoding="utf-8")
            self.assertTrue(any("horizontal movement" in error or "exposure index" in error for error in validate(root)))

    def test_active_context_self_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            path.write_text(path.read_text(encoding="utf-8") + "\ncurrent_branch_and_commit: forbidden-self-reference\n", encoding="utf-8")
            self.assertTrue(any("self-referential" in error for error in validate(root)))

    def test_active_context_fixed_current_main_sha_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/ACTIVE_CONTEXT.md"
            body = path.read_text(encoding="utf-8").replace(
                "current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH",
                f"current_main: {'a' * 40}",
                1,
            )
            path.write_text(body, encoding="utf-8")
            self.assertTrue(any("current_main must resolve dynamically" in error for error in validate(root)))

    def test_document_lifecycle_registry_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
            path.unlink()
            self.assertTrue(any("missing required file" in error for error in validate(root)))

    def test_historical_vertical_slice_cannot_be_promoted_to_current(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            lifecycle = root / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
            lifecycle.write_text(lifecycle.read_text(encoding="utf-8").replace(f"[증거/호환] {HISTORICAL_VERTICAL_SLICE}", f"[현행] {HISTORICAL_VERTICAL_SLICE}"), encoding="utf-8")
            self.assertTrue(any("lifecycle registry" in error or "historical Vertical Slice" in error for error in validate(root)))

    def test_legacy_master_gdd_requires_superseded_marker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/OMENWARD_GAME_DESIGN.md"
            path.write_text(path.read_text(encoding="utf-8").replace("[대체됨]", ""), encoding="utf-8")
            self.assertTrue(any("legacy GDD" in error for error in validate(root)))

    def test_project_core_rejects_legacy_food_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/PROJECT_CORE.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nstorage_selling_food\n", encoding="utf-8")
            self.assertTrue(any("legacy core marker" in error for error in validate(root)))

    def test_project_core_rejects_legacy_masok_term(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "docs/PROJECT_CORE.md"
            path.write_text(path.read_text(encoding="utf-8") + "\n구형 전술 자원: 마석\n", encoding="utf-8")
            self.assertTrue(any("legacy core marker" in error for error in validate(root)))

    def test_exact_premature_completion_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / "README.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nVERTICAL_SLICE_PROVEN\n", encoding="utf-8")
            self.assertTrue(any("premature completion" in error for error in validate(root)))

    def test_broken_local_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.copy(root)
            path = root / EVIDENCE_PILOT
            path.write_text(path.read_text(encoding="utf-8") + "\n[broken](missing/path.md)\n", encoding="utf-8")
            self.assertTrue(any("broken local link" in error for error in validate(root)))

    def copy(self, destination: pathlib.Path) -> None:
        for relative in MODULE["REQUIRED_FILES"]:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


if __name__ == "__main__":
    unittest.main()
