from __future__ import annotations

import pathlib
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
)

TOPDOWN_LAYOUT = "OMW-PLAN-20260820-TOPDOWN-BATTLEFIELD-LAYOUT-01"
TOPDOWN_SILHOUETTE = "OMW-PLAN-20260820-TOPDOWN-UNIT-SILHOUETTE-01"


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
        self.assertIn("CURRENT_APPROVED_REPLAN_DECISIONS = 18", decisions)
        self.assertIn("APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md", decisions)
        self.assertIn("APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md", decisions)

    def test_entry_docs_route_current_north_star_gate_and_user_request_only_visuals(self) -> None:
        for relative in ("README.md", "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/OMENWARD_ROADMAP.md", "docs/DOCUMENTATION_MAP.md"):
            text = read(relative)
            self.assertIn("REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST", text, relative)
            self.assertIn("USER_REQUEST_ONLY", text, relative)
            self.assertNotIn("PAUSED_PENDING_USER_REFERENCE_FILES", text, relative)
            self.assertNotIn("current_next_gate: ROULETTE_DDD_FEEDBACK_SPEC", text, relative)

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
        self.assertNotIn('CURRENT_IMPLEMENTATION_STATUS missing C2 proof', c2)
        self.assertNotIn('"C2 최종 검증 run:', c2)
        self.assertNotIn('"LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN"', c3)
        self.assertNotIn("C1 구현 검증 head:", sheet)
        self.assertIn("CURRENT_CONFIRMED_DECISIONS.md", project_core)
        self.assertNotIn('CURRENT_SPEC = "docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md"', project_core)


if __name__ == "__main__":
    unittest.main()
