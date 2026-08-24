from __future__ import annotations

import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]

CURRENT_DOCS = (
    "README.md",
    "AGENTS.md",
    "docs/PROJECT_CORE.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
)

TOPDOWN_LAYOUT = "OMW-PLAN-20260820-TOPDOWN-BATTLEFIELD-LAYOUT-01"
TOPDOWN_SILHOUETTE = "OMW-PLAN-20260820-TOPDOWN-UNIT-SILHOUETTE-01"
NORTH_STAR_AUDIT = "OMW-PLAN-20260824-NORTH-STAR-V2-1-AUDIT-01"
NORTH_STAR_AUDIT_OWNER = "APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md"
FINAL_REVIEW_OWNER = "FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md"
CURRENT_CONTRACT = "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8"
CURRENT_GATE = "IMPLEMENTATION_AUTHORITY_REQUIRED"
STALE_NORTH_STAR_GATE = "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST"
C2_HISTORICAL_STATUS = "docs/archive/2026-07/pre-v2-canon/CURRENT_IMPLEMENTATION_STATUS_PRE_V2.md"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class CurrentCanonReconciliationTests(unittest.TestCase):
    def test_current_entry_docs_do_not_route_closed_pr197_as_open(self) -> None:
        stale = "PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY"
        for relative in CURRENT_DOCS:
            self.assertNotIn(stale, read(relative), relative)

    def test_current_decision_index_routes_all_approved_visual_owners(self) -> None:
        decisions = read("docs/CURRENT_CONFIRMED_DECISIONS.md")
        self.assertIn(TOPDOWN_LAYOUT, decisions)
        self.assertIn(TOPDOWN_SILHOUETTE, decisions)
        self.assertIn(NORTH_STAR_AUDIT, decisions)
        self.assertIn("APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md", decisions)
        self.assertIn("APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md", decisions)
        self.assertIn(NORTH_STAR_AUDIT_OWNER, decisions)
        self.assertIn("NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY", decisions)
        self.assertIn("NORTH_STAR_LOWER_DECK = NEEDS_CORRECTION", decisions)
        self.assertIn("NORTH_STAR_ROULETTE_INTERACTION = NEEDS_CORRECTION", decisions)

    def test_current_decision_count_matches_registered_table(self) -> None:
        decisions = read("docs/CURRENT_CONFIRMED_DECISIONS.md")
        match = re.search(r"CURRENT_APPROVED_REPLAN_DECISIONS\s*=\s*(\d+)", decisions)
        self.assertIsNotNone(match)
        table_ids = set(re.findall(r"\| `(OMW-PLAN-[^`]+)` \|", decisions))
        self.assertEqual(int(match.group(1)), len(table_ids))
        self.assertEqual(19, len(table_ids))

    def test_current_routers_use_v48_and_retire_pre_audit_gate(self) -> None:
        for relative in CURRENT_DOCS:
            text = read(relative)
            self.assertIn(CURRENT_CONTRACT, text, relative)
            self.assertNotIn(STALE_NORTH_STAR_GATE, text, relative)

        for relative in (
            "README.md",
            "docs/PROJECT_CORE.md",
            "docs/ACTIVE_CONTEXT.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/CURRENT_CONFIRMED_DECISIONS.md",
            "docs/OMENWARD_GDD_CURRENT_CANON.md",
            "docs/OMENWARD_ROADMAP.md",
            "docs/DECISIONS_PENDING.md",
            "docs/DOCUMENTATION_MAP.md",
            "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
            "docs/HANDOFF_CONTEXT.md",
            "docs/PROJECT_CANON_DECISION_LEDGER.md",
        ):
            text = read(relative)
            self.assertIn("USER_REQUEST_ONLY", text, relative)

        agents = read("AGENTS.md")
        self.assertIn("current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md", agents)
        self.assertIn("current_context: docs/ACTIVE_CONTEXT.md", agents)
        self.assertNotIn("CURRENT_APPROVED_REPLAN_DECISIONS = 19", agents)

    def test_current_north_star_audit_is_consistent_across_state_owners(self) -> None:
        for relative in (
            "README.md",
            "docs/PROJECT_CORE.md",
            "docs/ACTIVE_CONTEXT.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/CURRENT_CONFIRMED_DECISIONS.md",
            "docs/OMENWARD_GDD_CURRENT_CANON.md",
            "docs/OMENWARD_ROADMAP.md",
            "docs/DECISIONS_PENDING.md",
            "docs/DOCUMENTATION_MAP.md",
            "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
            "docs/HANDOFF_CONTEXT.md",
            "docs/PROJECT_CANON_DECISION_LEDGER.md",
        ):
            text = read(relative)
            self.assertIn("NORTH_STAR_V2_1", text, relative)
            self.assertTrue(
                NORTH_STAR_AUDIT in text or NORTH_STAR_AUDIT_OWNER in text,
                f"{relative} does not route the current North Star audit owner",
            )

    def test_final_planning_review_is_current_and_routes_implementation_authority(self) -> None:
        review = read("docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md")
        for marker in (
            "status: PASS_5_OF_5",
            "ADVERSARIAL_REVIEW = PASS_5_OF_5",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
            "CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED",
            "IMPLEMENTATION_AUTHORITY = NONE",
        ):
            self.assertIn(marker, review)

        for relative in (
            "README.md",
            "docs/PROJECT_CORE.md",
            "docs/ACTIVE_CONTEXT.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/CURRENT_CONFIRMED_DECISIONS.md",
            "docs/OMENWARD_GDD_CURRENT_CANON.md",
            "docs/OMENWARD_ROADMAP.md",
            "docs/DECISIONS_PENDING.md",
            "docs/DOCUMENTATION_MAP.md",
            "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
            "docs/HANDOFF_CONTEXT.md",
            "docs/PROJECT_CANON_DECISION_LEDGER.md",
        ):
            text = read(relative)
            self.assertIn(CURRENT_GATE, text, relative)
            self.assertIn("FINAL_PLANNING_ADVERSARIAL_REVIEW", text, relative)

        routed = "\n".join(read(path) for path in ("README.md", "docs/ACTIVE_CONTEXT.md", "docs/DOCUMENTATION_MAP.md", "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"))
        self.assertIn(FINAL_REVIEW_OWNER, routed)

    def test_current_world_docs_use_approved_veil_convergence_truth(self) -> None:
        for relative in ("docs/PROJECT_CORE.md", "docs/OMENWARD_GDD_CURRENT_CANON.md"):
            text = read(relative)
            self.assertIn("VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상", text, relative)
            self.assertIn("RUN_HISTORY_RESET = FALSE", text, relative)
            self.assertNotIn("CAUSE_OF_OMEN_CYCLE = USER_DECISION_REQUIRED", text, relative)
            self.assertNotIn("HIGH_LEVEL_ENEMY_OR_VEIL_IDENTITY = USER_DECISION_REQUIRED", text, relative)
            self.assertNotIn("STAGE_20_NARRATIVE_RESOLUTION = USER_DECISION_REQUIRED", text, relative)

    def test_current_status_preserves_historical_proof_without_claiming_current_runtime(self) -> None:
        status = read("docs/CURRENT_IMPLEMENTATION_STATUS.md")
        self.assertIn("LEGACY_C1_C2_C3_PROVEN", status)
        self.assertIn("CURRENT_GODOT_RUNTIME = NOT_RUN", status)
        self.assertIn("CURRENT_WINDOWS_RUNTIME = NOT_RUN", status)
        self.assertIn("CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN", status)
        self.assertNotIn("C1 구현 검증 head:", status)
        self.assertNotIn("C1 최종 검증 run:", status)
        self.assertNotIn("C2 최종 검증 run:", status)

    def test_legacy_proof_validators_use_evidence_owners_not_current_status(self) -> None:
        c1 = read("tools/validate_c1_roulette.py")
        c2 = read("tools/validate_c2_battle_objective.py")
        c3 = read("tools/validate_c3_core_ux.py")
        sheet = read("tests/python/test_bca_visual_sheet_adoption.py")
        project_core = read("tools/validate_project_core_docs.py")

        self.assertIn('"docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md"', c1)
        self.assertNotIn('"docs/CURRENT_IMPLEMENTATION_STATUS.md": (\n            "C1_ROULETTE_CORE_REMOTE_PROVEN"', c1)
        self.assertIn(f'HISTORICAL_STATUS = "{C2_HISTORICAL_STATUS}"', c2)
        self.assertIn("historical C2 exact proof missing", c2)
        self.assertNotIn('status = (root / "docs/CURRENT_IMPLEMENTATION_STATUS.md").read_text', c2)
        self.assertNotIn('CURRENT_IMPLEMENTATION_STATUS missing C2 proof', c2)
        self.assertNotIn('"LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN"', c3)
        self.assertIn("test_c1_exact_proof_lives_in_historical_evidence_owner", sheet)
        self.assertIn("docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md", sheet)
        self.assertIn('self.assertNotIn(f"C1 구현 검증 head: `{C1_HEAD}`", status)', sheet)
        self.assertIn("CURRENT_CONFIRMED_DECISIONS.md", project_core)
        self.assertNotIn('CURRENT_SPEC = "docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md"', project_core)


if __name__ == "__main__":
    unittest.main()
