from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "skills" / "PROJECT_BASE_ADAPTER.json"
SNAPSHOT = ROOT / "skills" / "PROJECT_SKILL_SNAPSHOT.json"

V944_RELEASE = {
    "version": "9.4.4",
    "release_commit": "210ec78292fa12ed7563ba743b322dd36103ae4a",
    "release_evidence_commit": "bb61e68dc3028421b60c11b87ba2abd297ee6f78",
    "finalization_commit": "5adc196c0185951f50e49ab5e51586eff8d60886",
}
V944_REGISTRY = "08f882d0c77339e8f7ff187c35b79501e0a2958ab1ff1c7aaa1c0ef8dbee45d6"


class TestBaseV94Omenward(unittest.TestCase):
    def test_identity_routes_and_protection(self) -> None:
        adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
        snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))

        self.assertEqual(2, adapter["schema_version"])
        self.assertEqual("omenward", adapter["project"]["project_id"])
        for key, expected in V944_RELEASE.items():
            self.assertEqual(expected, adapter["base_release"][key])
        self.assertEqual(V944_REGISTRY, adapter["skill_registry"]["base"]["sha256"])
        self.assertIn(
            "optimizing-ai-model-and-prompt-costs",
            {route["route_id"] for route in adapter["routing"]["base_routes"]},
        )
        self.assertEqual(
            {"omenward-art-assets", "omenward-core-design", "omenward-core-ux", "omenward-godot"},
            {route["route_id"] for route in adapter["routing"]["project_routes"]},
        )
        self.assertEqual(
            "BASE_SHARED",
            snapshot["effective_routes"]["optimizing-ai-model-and-prompt-costs"]["source"],
        )
        self.assertEqual(
            ["data/", "scripts/", "scenes/", "assets/", "addons/", "project.godot"],
            adapter["protected_paths"],
        )

    def test_generated_views_follow_the_canonical_adapter(self) -> None:
        adapter_hash = hashlib.sha256(ADAPTER.read_bytes()).hexdigest()
        snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        self.assertEqual(adapter_hash, snapshot["source_registry"]["sha256"])
        for relative in ("skills/BASE_V9_ADAPTER.json", "skills/PROJECT_BASE_SKILL_ADAPTER.json"):
            view = json.loads((ROOT / relative).read_text(encoding="utf-8"))
            self.assertEqual(adapter_hash, view["canonical_source_sha256"])
            self.assertEqual("9.4.4", view["base_release"]["version"])

    def test_historical_ai_contract_stays_separate_from_the_new_release_pin(self) -> None:
        ai = (ROOT / "docs/AI_WORKFLOW.md").read_text(encoding="utf-8")
        ux = (ROOT / "docs/UX_UI_SYSTEM.md").read_text(encoding="utf-8")
        audit = (ROOT / "docs/reviews/2026-08-01_BASE_V9_4_ADOPTION_AUDIT.md").read_text(encoding="utf-8")
        for marker in ("[모델 추천]", "HARD_CONSTRAINT", "Interface-first", "Example-as-Fixture", "refresh_trigger", "NOT_RUN"):
            self.assertIn(marker, ai)
        for marker in ("입력 접수", "처리 중", "중단", "즉시 완료", "빠른 반복", "재진입", "Reduced Motion", "mute", "haptic-off", "권위 시점"):
            self.assertIn(marker, ux)
        self.assertIn("product_paths_changed: false", audit)
        self.assertIn("HUMAN_NOT_RUN", audit)


if __name__ == "__main__":
    unittest.main()
