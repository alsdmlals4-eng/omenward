from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POWERSHELL = ROOT / "tools/run_local_verification_pack.ps1"


class PowerShellRepositoryRootContract(unittest.TestCase):
    def test_repository_root_is_parent_of_tools_directory(self) -> None:
        source = POWERSHELL.read_text(encoding="utf-8")
        self.assertIn(
            "$RepositoryRoot = Split-Path -Parent $PSScriptRoot",
            source,
        )
        self.assertNotIn(
            "$RepositoryRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)",
            source,
        )


if __name__ == "__main__":
    unittest.main()
