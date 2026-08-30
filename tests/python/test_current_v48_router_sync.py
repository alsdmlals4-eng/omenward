from __future__ import annotations

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]

CURRENT_CONTRACT = "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8"
CURRENT_VISUAL_DECISION = "OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01"
CURRENT_MAP_TOPOLOGY = "MAP_TOPOLOGY = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL"
CURRENT_LEGACY_RUNTIME_ASSET = "OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1"
CURRENT_REACTIVATION_GATE = "RUN_BATTLE_PRIMARY_RUNTIME_TECHNICAL_SMOKE_THEN_HUMAN_USABILITY_CHECK"
CURRENT_IMAGE_POLICY = "USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES"
CURRENT_AUTHORITY = "SCOPED_APPROVED"

GLOBAL_CURRENT_ROUTERS = (
    "README.md",
    "docs/PROJECT_CORE.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class CurrentV48RouterSyncTests(unittest.TestCase):
    def test_global_current_routers_share_20260825_state(self) -> None:
        for relative in GLOBAL_CURRENT_ROUTERS:
            text = read(relative)
            with self.subTest(relative=relative):
                self.assertIn(CURRENT_CONTRACT, text)
                self.assertIn("CURRENT_APPROVED_REPLAN_DECISIONS = 30", text)
                self.assertIn(CURRENT_VISUAL_DECISION, text)
                self.assertIn(CURRENT_MAP_TOPOLOGY, text)
                self.assertIn(CURRENT_LEGACY_RUNTIME_ASSET, text)
                self.assertIn(CURRENT_AUTHORITY, text)
                self.assertIn(CURRENT_IMAGE_POLICY, text)
                self.assertIn("FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL", text)

    def test_global_current_routers_do_not_reactivate_20260824_gate_or_visual_default(self) -> None:
        stale_exact_lines = (
            "CURRENT_APPROVED_REPLAN_DECISIONS = 19",
            "CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED",
            "CURRENT_IMPLEMENTATION_AUTHORITY = NONE",
            "IMPLEMENTATION_AUTHORITY = NONE",
            "CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART",
            "BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART",
            "DEFAULT_CAMERA = FULL_THREE_LANES_VISIBLE",
            "NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY",
        )
        for relative in GLOBAL_CURRENT_ROUTERS:
            text = read(relative)
            with self.subTest(relative=relative):
                for stale in stale_exact_lines:
                    self.assertIsNone(
                        re.search(rf"(?m)^{re.escape(stale)}$", text),
                        f"{relative} reactivated stale current line: {stale}",
                    )

    def test_handoff_distinguishes_historical_premerge_sha_from_integrated_closeout(self) -> None:
        handoff = read("docs/HANDOFF_CONTEXT.md")
        for marker in (
            "current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH",
            f"current_gate: {CURRENT_REACTIVATION_GATE}",
            f"CURRENT_NEXT = {CURRENT_REACTIVATION_GATE}",
            "runtime_validation: MACHINE_CONTRACT_PASS__RUNTIME_NOT_RUN__HUMAN_NOT_RUN",
        ):
            self.assertIn(marker, handoff)
        self.assertNotIn(
            "Current handoff closeout next action is exact-head PR verification",
            handoff,
        )

    def test_historical_final_review_keeps_preapproval_values(self) -> None:
        review = read("docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md")
        for marker in (
            "status: PASS_5_OF_5",
            "CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED",
            "IMPLEMENTATION_AUTHORITY = NONE",
            "GITHUB_NOTION_DRIFT_CHECK = PASS",
        ):
            self.assertIn(marker, review)


if __name__ == "__main__":
    unittest.main()
