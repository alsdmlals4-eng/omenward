from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
QUALITY = ROOT / "docs/design/APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md"
CADENCE = ROOT / "docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md"
GDD = ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md"
MAPRUN_CORE = ROOT / "docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"
OLD_MATRIX = ROOT / "docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
DOC_MAP = ROOT / "docs/DOCUMENTATION_MAP.md"
ACTIVE = ROOT / "docs/ACTIVE_CONTEXT.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"

QUALITY_DECISION = "OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1"
CADENCE_DECISION = "OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1"


class QualityGuardrailsEliteBossCadenceTest(unittest.TestCase):
    def test_quality_guardrail_owner_has_all_approved_contracts(self) -> None:
        self.assertTrue(QUALITY.exists(), "quality guardrail owner must exist")
        text = QUALITY.read_text(encoding="utf-8")
        for marker in (
            QUALITY_DECISION,
            "RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN",
            "FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE",
            "ELITE_CADENCE_FIXED = EVERY_STAGE_FINAL_WAVE",
            "SOFT_SYNERGY_DISCOVERY = PREFERRED",
            "POST_STAGE_CAUSAL_REVIEW = FORECAST -> KEY_EVENTS -> PLAYER_RESPONSE_OUTCOME",
            "PRESCRIPTIVE_NEXT_BUILD_COMMAND = FORBIDDEN",
            "HORIZONTAL_CHALLENGE_EXPANSION = ALLOWED",
            "SEEDED_RUN = ALLOWED",
            "ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE",
            "GAMBLING_FANTASY_POSITIONING = FORBIDDEN",
            "PAID_SPIN = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_cadence_owner_replaces_danger_stage_type(self) -> None:
        self.assertTrue(CADENCE.exists(), "elite/boss cadence owner must exist")
        text = CADENCE.read_text(encoding="utf-8")
        for marker in (
            CADENCE_DECISION,
            "MAPRUN_STAGE_COUNT = 20",
            "BASELINE_WAVE_BEATS = 3",
            "DANGER_STAGE_TYPE = REMOVED",
            "ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE",
            "ELITE_PRESENCE_REQUIRED = TRUE",
            "BOSS_STAGES = 5 / 10 / 15 / 20",
            "BOSS_STAGE_BOSS_PRESENCE_REQUIRED = TRUE",
            "BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE",
            "ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING",
            "ELITE_EXACT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("DANGER_STAGES = 4 / 9 / 14 / 19", text)

    def test_current_gameplay_routers_point_to_new_cadence(self) -> None:
        combined = "\n".join(path.read_text(encoding="utf-8") for path in (GDD, MAPRUN_CORE, LIFECYCLE, DOC_MAP))
        for marker in (
            CADENCE_DECISION,
            QUALITY_DECISION,
            "DANGER_STAGE_TYPE = REMOVED",
            "ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE",
            "BOSS_STAGES = 5 / 10 / 15 / 20",
        ):
            self.assertIn(marker, combined)

    def test_old_pressure_matrix_is_superseded_lineage(self) -> None:
        text = OLD_MATRIX.read_text(encoding="utf-8")
        self.assertIn("SUPERSEDED", text)
        self.assertIn(CADENCE_DECISION, text)
        self.assertIn("IMPLEMENTATION_INPUT_FOR_CURRENT_PHASE = FORBIDDEN", text)

    def test_phase_gate_remains_closed_after_new_approvals(self) -> None:
        combined = "\n".join(path.read_text(encoding="utf-8") for path in (ACTIVE, PENDING))
        for marker in (
            "WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0",
            "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED",
            "PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN",
            "PHASE_C_BLOCKED",
            QUALITY_DECISION,
            CADENCE_DECISION,
        ):
            self.assertIn(marker, combined)

    def test_no_final_elite_or_boss_numerics_are_selected(self) -> None:
        text = CADENCE.read_text(encoding="utf-8") if CADENCE.exists() else ""
        for marker in (
            "ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING",
            "ELITE_EXACT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING",
            "BOSS_EXACT_ENTRY_WAVE_AND_NUMERICS = CONTENT_AND_RUNTIME_EVIDENCE_TUNING",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
