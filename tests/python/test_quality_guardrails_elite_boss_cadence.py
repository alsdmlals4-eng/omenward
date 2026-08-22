from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
QUALITY = ROOT / "docs/design/APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md"
CADENCE = ROOT / "docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md"
AGENTS = ROOT / "AGENTS.md"
ACTIVE = ROOT / "docs/ACTIVE_CONTEXT.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
PHASE_B = ROOT / "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"

QUALITY_DECISION = "OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1"
CADENCE_DECISION = "OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1"


class QualityGuardrailsEliteBossCadenceTest(unittest.TestCase):
    def test_quality_guardrail_owner_has_all_approved_contracts(self) -> None:
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
            "LEGACY_DANGER_CADENCE_AUTHORITY = NONE",
            "ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING",
            "ELITE_EXACT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING",
            "SUPERSEDED_FOR_STAGE_TYPE_AND_CADENCE",
            "IMPLEMENTATION_INPUT_FOR_CURRENT_PHASE = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_current_consumers_route_durable_cadence_without_historical_decision_ids(self) -> None:
        combined = "\n".join(path.read_text(encoding="utf-8") for path in (AGENTS, ACTIVE, PENDING))
        for marker in (
            "DANGER_STAGE_TYPE = REMOVED",
            "ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE",
            "BOSS_STAGES = 5 / 10 / 15 / 20",
        ):
            self.assertIn(marker, combined)
        self.assertNotIn(QUALITY_DECISION, combined)
        self.assertNotIn(CADENCE_DECISION, combined)

    def test_phase_b_gate_is_historical_evidence_not_current_execution_gate(self) -> None:
        phase_b = PHASE_B.read_text(encoding="utf-8")
        for marker in (
            "WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0",
            "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED",
            "PHASE_B_FINAL_PLANNING_REVIEW = PASS",
            "PHASE_C_GATE = OPEN",
            "NEW_PRODUCT_DECISION_REQUIRED = FALSE",
        ):
            self.assertIn(marker, phase_b)

        current = "\n".join(path.read_text(encoding="utf-8") for path in (ACTIVE, PENDING))
        self.assertNotIn("PHASE_C_GATE = OPEN", current)
        self.assertIn("CURRENT_CANON_RECONCILIATION = REQUIRED_UNTIL_EXACT_HEAD_GREEN_AND_MERGED_MAIN_READBACK", current)
        self.assertIn("CURRENT_IMPLEMENTATION_AUTHORITY = NONE", current)

    def test_no_final_elite_or_boss_numerics_are_selected(self) -> None:
        text = CADENCE.read_text(encoding="utf-8")
        for marker in (
            "ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING",
            "ELITE_EXACT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING",
            "BOSS_EXACT_ENTRY_WAVE_AND_NUMERICS = CONTENT_AND_RUNTIME_EVIDENCE_TUNING",
            "ELITE_HP_MULTIPLIER = NOT_SELECTED",
            "BOSS_HP = NOT_SELECTED",
            "THREAT_BUDGET = NOT_SELECTED",
        ):
            self.assertIn(marker, text)
        self.assertIn("FINAL_PARAMETER_VECTOR = NOT_SELECTED", PENDING.read_text(encoding="utf-8"))
        self.assertIn("FINAL_PRODUCT_NUMERICS = NOT_APPROVED", PENDING.read_text(encoding="utf-8"))

    def test_godot_ai_314_phase_b_claim_stays_historical(self) -> None:
        phase_b = PHASE_B.read_text(encoding="utf-8")
        self.assertIn("USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4", phase_b)
        self.assertIn("GODOT_AI_3_1_4_CANON_AUTHORITY_RECONCILIATION = DEFER_TO_PHASE_C_FRESH_VERIFY", phase_b)
        self.assertIn("GODOT_AI_3_1_4_EXACT_UPSTREAM_VERIFICATION = NOT_CONFIRMED_IN_PHASE_B_WEB_CHECK", phase_b)


if __name__ == "__main__":
    unittest.main()
