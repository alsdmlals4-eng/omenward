from __future__ import annotations

from pathlib import Path
import unittest

from tools.git_canonical_evidence import git_tracked_paths_utf8

ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "docs" / "analysis" / "barracks_simulation"
GITIGNORE = ROOT / ".gitignore"

DECISION = "OMW-DEC-20260809-TOOLING-GODOT-CSV-IMPORT-ARTIFACT-HYGIENE-V1"


class GodotCsvImportArtifactHygieneTest(unittest.TestCase):
    def test_no_generated_translation_artifacts_are_tracked(self) -> None:
        tracked = set(git_tracked_paths_utf8(ROOT))
        generated = sorted(
            p.relative_to(ROOT).as_posix()
            for p in SIM_DIR.iterdir()
            if (p.name.endswith(".csv.import") or p.suffix == ".translation")
            and p.relative_to(ROOT).as_posix() in tracked
        )
        self.assertEqual(generated, [], f"generated Godot CSV translation artifacts must not be tracked: {generated}")

    def test_gitignore_prevents_recurrence(self) -> None:
        text = GITIGNORE.read_text(encoding="utf-8")
        self.assertIn("docs/analysis/barracks_simulation/*.csv.import", text)
        self.assertIn("docs/analysis/barracks_simulation/*.translation", text)

    def test_source_csvs_remain_canonical(self) -> None:
        self.assertTrue((SIM_DIR / "robustness_sweep_10000.v1.csv").is_file())
        self.assertTrue((SIM_DIR / "smoke_sweep_2000.v2.csv").is_file())


if __name__ == "__main__":
    unittest.main()
