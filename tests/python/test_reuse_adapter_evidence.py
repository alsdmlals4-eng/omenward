from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class ReuseAdapterEvidenceTests(unittest.TestCase):
    def test_installation_evidence_is_final_and_exact(self) -> None:
        evidence = json.loads(
            (ROOT / "docs/REUSE_ADAPTER_INSTALLATION_EVIDENCE_2026-08-20.json").read_text(encoding="utf-8")
        )
        self.assertEqual("FINAL", evidence["state"])
        self.assertEqual("RM-SYS-003", evidence["module"])
        self.assertEqual("67487c932cc883db95da7bc852f4eb33883f0052", evidence["installation_commit"])
        self.assertEqual("8553678f70e22f193a2336b591f677dcfa5a8965", evidence["base_source_commit"])
        self.assertEqual("SUCCESS", evidence["verification"]["python_regression"])
        self.assertEqual("SUCCESS", evidence["verification"]["godot_4_7_1_import"])
        self.assertEqual("SUCCESS", evidence["verification"]["headless_contract_suite"])
        self.assertEqual("SUCCESS", evidence["verification"]["runtime_smoke"])


if __name__ == "__main__":
    unittest.main()
