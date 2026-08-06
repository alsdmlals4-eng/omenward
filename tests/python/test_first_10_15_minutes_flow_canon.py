from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md"
FINAL = ROOT / "docs/design/APPROVED_OMENWARD_ONBOARDING_COMPLETION_MINIMUM_VALID_PATHS_AND_HUMAN_STOP_SHIP_2026-08-06.md"

class FirstFlowFinalAuthorityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = PARENT.read_text(encoding="utf-8")
        cls.final = FINAL.read_text(encoding="utf-8")

    def test_parent_flow_and_final_child_exist(self):
        self.assertIn("OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1", self.parent)
        self.assertIn("OMW-DEC-20260806-PLANNING-ONBOARDING-COMPLETION-MINIMUM-VALID-PATHS-HUMAN-STOP-SHIP-V1", self.final)

    def test_final_child_closes_ten_checkpoint_cycle(self):
        self.assertIn("DECISION_STATUS = APPROVED_10_OF_10", self.final)
        self.assertIn("PARENT_FIRST_10_15_MINUTES_FLOW = PLANNING_COMPLETE", self.final)
        self.assertIn("MINIMUM_VALID_PLAYER_PATHS = SHIELD_WITHOUT_SPECIAL / ARCHER_WITHOUT_SPECIAL", self.final)
        self.assertIn("INTERNAL_QA_REQUIRED_SCENARIO_COUNT = TWELVE", self.final)

    def test_validation_and_product_boundaries(self):
        self.assertIn("FIRST_TIME_HUMAN_SAMPLE_MINIMUM = TWENTY", self.final)
        self.assertIn("GITHUB_ACTIONS_GREEN = NOT_PROVEN", self.final)
        self.assertIn("LOCAL_GODOT_PROJECT = UNCHANGED", self.final)

if __name__ == "__main__":
    unittest.main()
