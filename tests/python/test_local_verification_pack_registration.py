from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "tools/run_local_verification_pack.py"
VALIDATOR = ROOT / "tools/verify_base_recovery_and_local_verification_pack.py"
WORKFLOW = ROOT / ".github/workflows/validate-base-recovery-local-verification-pack.yml"

TEST_PATH = "tests/python/test_local_verification_powershell_root.py"
TEST_MODULE = "tests.python.test_local_verification_powershell_root"


class LocalVerificationPackRegistrationContract(unittest.TestCase):
    def test_regression_test_is_registered_everywhere(self) -> None:
        runner = RUNNER.read_text(encoding="utf-8")
        validator = VALIDATOR.read_text(encoding="utf-8")
        workflow = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn(TEST_PATH, runner)
        self.assertIn(TEST_MODULE, runner)
        self.assertIn(TEST_PATH, validator)
        self.assertIn(TEST_PATH, workflow)
        self.assertIn(TEST_MODULE, workflow)


if __name__ == "__main__":
    unittest.main()
