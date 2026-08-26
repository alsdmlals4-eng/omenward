from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION = "OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1"
ACTIVATION_DECISION = "OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1"
PHASE_B_DECISION = "OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1"
C0_LOCAL_DECISION = "OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1"
RUNTIME_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1"
BASE_MAIN = "069f0c9654a6cde7cea6f3343dd2fa81c6248d5d"
PROJECT_BASELINE = "87339f87949c8faea0dfe1482c5d0887a04d94f4"
PR193_MERGE = "7d421372c33c2d6a32ee3ef8bdb94ead333bc0c0"
CURRENT_CONTRACT = "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8"
CURRENT_NORTH_STAR_AUDIT = "OMW-PLAN-20260824-NORTH-STAR-V2-1-AUDIT-01"
CURRENT_VISUAL_DECISION = "OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01"
STALE_NORTH_STAR_GATE = "REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST"

BINDING = ROOT / "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"
CANONICAL_V45_R2 = ROOT / "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md"
GDD = ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md"
BARRACKS_OWNER = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md"
WORKBOOK = ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md"
ACTIVE_CONTEXT = ROOT / "docs/ACTIVE_CONTEXT.md"
CURRENT_STATUS = ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
HANDOFF = ROOT / "docs/HANDOFF_CONTEXT.md"
AGENTS = ROOT / "AGENTS.md"
README = ROOT / "README.md"
PROJECT_CORE = ROOT / "docs/PROJECT_CORE.md"
ROADMAP = ROOT / "docs/OMENWARD_ROADMAP.md"
DOCUMENTATION_MAP = ROOT / "docs/DOCUMENTATION_MAP.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
LEDGER = ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md"
CURRENT_DECISIONS = ROOT / "docs/CURRENT_CONFIRMED_DECISIONS.md"
C0_REVIEW = ROOT / "docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md"
PHASE_B_REVIEW = ROOT / "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"

CURRENT_ROUTERS = (
    AGENTS,
    README,
    PROJECT_CORE,
    ACTIVE_CONTEXT,
    CURRENT_STATUS,
    PENDING,
    HANDOFF,
    ROADMAP,
    DOCUMENTATION_MAP,
    LIFECYCLE,
    LEDGER,
    GDD,
    CURRENT_DECISIONS,
)


class CanonFreshnessV45RoutingTest(unittest.TestCase):
    def test_v45_historical_authority_files_still_exist(self) -> None:
        for path in (BINDING, STATE, CANONICAL_V45_R2, PHASE_B_REVIEW, C0_REVIEW):
            self.assertTrue(path.is_file(), f"missing historical authority artifact: {path.relative_to(ROOT)}")

    def test_v45_r2_source_and_machine_state_keep_exact_historical_identity(self) -> None:
        text = CANONICAL_V45_R2.read_text(encoding="utf-8")
        for marker in (
            "contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION",
            "contract_version: '4.5'",
            "revision: '2026-08-11-r2'",
            "adapter_policy: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON",
            'project_local_path: "C:/Users/user/Documents/GitHub/Ninza/omenward"',
        ):
            self.assertIn(marker, text)
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["active_contract"]["source"], str(CANONICAL_V45_R2.relative_to(ROOT)).replace("\\", "/"))
        self.assertEqual(state["active_contract"]["activation_decision_id"], ACTIVATION_DECISION)
        self.assertEqual(state["decision_id"], DECISION)
        self.assertEqual(state["phase_b_decision_id"], PHASE_B_DECISION)
        self.assertEqual(state["activation_baseline_main_sha"], PROJECT_BASELINE)
        self.assertEqual(state["base_current_main_observed"], BASE_MAIN)
        self.assertEqual(state["phase_c_c0"], "PASS")
        self.assertEqual(state["current_execution_decision_id"], C0_LOCAL_DECISION)
        self.assertEqual(state["closure_lineage"]["pr193"]["merge_sha"], PR193_MERGE)

    def test_durable_product_rules_survive_without_reactivating_v45_process(self) -> None:
        gdd = GDD.read_text(encoding="utf-8")
        for marker in (
            "DANGER_STAGE_TYPE = REMOVED",
            "ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE",
            "BOSS_STAGES = 5 / 10 / 15 / 20",
            "TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1",
            "TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3",
            "FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN",
        ):
            self.assertIn(marker, gdd)
        barracks = BARRACKS_OWNER.read_text(encoding="utf-8")
        for marker in (
            "SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT",
            "SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT",
            "SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT",
            "SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS",
        ):
            self.assertIn(marker, barracks)

    def test_current_routers_use_v48_and_current_visual_closeout(self) -> None:
        for path in CURRENT_ROUTERS:
            text = path.read_text(encoding="utf-8")
            self.assertIn(CURRENT_CONTRACT, text, str(path.relative_to(ROOT)))
            self.assertNotIn(STALE_NORTH_STAR_GATE, text, str(path.relative_to(ROOT)))

        decisions = CURRENT_DECISIONS.read_text(encoding="utf-8")
        self.assertIn(CURRENT_NORTH_STAR_AUDIT, decisions)
        self.assertIn(CURRENT_VISUAL_DECISION, decisions)
        self.assertIn("CURRENT_APPROVED_REPLAN_DECISIONS = 21", decisions)
        self.assertIn("VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION", decisions)
        self.assertIn("PER_FRONT_MINIMAP = REQUIRED", decisions)
        self.assertIn("APPROVED_VISUAL = OM-IMG-023", decisions)
        self.assertIn("PROJECT_STATE = PAUSED_AT_PAIR_CLEANUP_APPROVAL_GATE", decisions)

        agents = AGENTS.read_text(encoding="utf-8")
        self.assertIn("current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md", agents)
        self.assertIn("current_context: docs/ACTIVE_CONTEXT.md", agents)
        self.assertIn(CURRENT_VISUAL_DECISION, agents)
        self.assertNotIn("CURRENT_APPROVED_REPLAN_DECISIONS = 19", agents)

        active = ACTIVE_CONTEXT.read_text(encoding="utf-8")
        self.assertIn("status: PAUSED_AT_PAIR_PIXEL_CLEANUP_APPROVAL_GATE", active)
        self.assertIn("CURRENT_APPROVED_REPLAN_DECISIONS = 21", active)
        self.assertIn("CURRENT_NEXT = USER_EXPLICIT_PAIR_PIXEL_CLEANUP_OR_EDIT_APPROVAL", active)
        self.assertIn("NOTION_CURRENT_VISUAL_IMAGE = SERVER_READBACK_PASS", active)

        handoff = HANDOFF.read_text(encoding="utf-8")
        self.assertIn("APPROVED_VISUAL = OM-IMG-023", handoff)
        self.assertIn("BCP-2026-033-visual-canon-approval-and-handoff-integrity", handoff)

    def test_v45_phase_b_c0_and_issue176_do_not_freeze_current_execution_routing(self) -> None:
        stale_current_markers = (
            "contract_version: 4.5",
            "PHASE_C_GATE = OPEN",
            "PR175_DRAFT_7_RUNTIME_GAPS_OPEN",
            "PR175_CURRENT_MAIN_REVALIDATION_NEXT",
            "CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY",
            "DISPOSABLE_AUTOLOAD_AB_ISOLATION",
        )
        for path in (AGENTS, README, PROJECT_CORE, ACTIVE_CONTEXT, CURRENT_STATUS, PENDING, HANDOFF, ROADMAP, DOCUMENTATION_MAP, LEDGER, GDD):
            text = path.read_text(encoding="utf-8")
            for marker in stale_current_markers:
                self.assertNotIn(marker, text, f"{path.relative_to(ROOT)} reactivated historical routing {marker}")

    def test_c0_and_runtime_package_remain_discoverable_as_history(self) -> None:
        c0 = C0_REVIEW.read_text(encoding="utf-8")
        self.assertIn(C0_LOCAL_DECISION, c0)
        self.assertIn("PHASE_C_C0_OVERALL = PASS", c0)
        phase_b = PHASE_B_REVIEW.read_text(encoding="utf-8")
        self.assertIn(PHASE_B_DECISION, phase_b)
        history_blob = "\n".join((BINDING.read_text(encoding="utf-8"), WORKBOOK.read_text(encoding="utf-8"), json.dumps(json.loads(STATE.read_text(encoding="utf-8")), sort_keys=True)))
        self.assertIn(RUNTIME_DECISION, history_blob)

    def test_transient_ops_pr_state_is_fresh_read_only_not_current_canon(self) -> None:
        c0 = C0_REVIEW.read_text(encoding="utf-8")
        self.assertIn("TRANSIENT_OPS_PR_STATE = FRESH_READ_ONLY_NOT_DURABLE_CANON", c0)
        ledger = LEDGER.read_text(encoding="utf-8")
        self.assertIn("CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED", ledger)
        self.assertNotIn("PR193_CURRENT_STATUS = RED_FIRST_FULL_CURRENT_CONSUMER_CLOSURE", ledger)

    def test_lifecycle_routes_v45_and_v44_as_history_only(self) -> None:
        text = LIFECYCLE.read_text(encoding="utf-8")
        for marker in (
            "ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
            "ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
            "ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md",
            "HISTORICAL_V4_4_BINDING",
            "PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md",
            "LEGACY_DANGER_CADENCE_AUTHORITY = NONE",
        ):
            self.assertIn(marker, text)
        self.assertIn("[증거/호환]", text)

    def test_sheet_workbook_is_history_compatibility_not_current_human_authority(self) -> None:
        workbook = WORKBOOK.read_text(encoding="utf-8")
        self.assertIn("PROJECT_SHEET_CONFIGURED", workbook)
        doc_map = DOCUMENTATION_MAP.read_text(encoding="utf-8")
        self.assertIn("Google Sheet는 current human authority가 아니다", doc_map)
        lifecycle = LIFECYCLE.read_text(encoding="utf-8")
        self.assertIn("GOOGLE_SHEET = COMPATIBILITY_HISTORY_ONLY", lifecycle)


if __name__ == "__main__":
    unittest.main()
