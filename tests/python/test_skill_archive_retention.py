from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_checker():
    path = ROOT / "tools/check_archive_governance.py"
    spec = importlib.util.spec_from_file_location("check_archive_governance", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


checker = load_checker()


class OmenwardArchiveGovernanceTests(unittest.TestCase):
    def test_current_repository_archive_contract_passes(self) -> None:
        self.assertEqual([], checker.validate(ROOT))

    def test_base_commit_is_pinned_consistently(self) -> None:
        expected = checker.EXPECTED_BASE_COMMIT
        archive = json.loads((ROOT / "docs/archive/ARCHIVE_RETENTION_ADAPTER.json").read_text(encoding="utf-8"))
        routes = json.loads((ROOT / "skills/BASE_SHARED_SKILL_ROUTES.json").read_text(encoding="utf-8"))
        adapter = json.loads((ROOT / "skills/PROJECT_BASE_SKILL_ADAPTER.json").read_text(encoding="utf-8"))
        self.assertEqual(expected, archive["base"]["commit"])
        self.assertEqual(expected, routes["base"]["commit"])
        self.assertEqual(expected, adapter["base"]["commit"])

    def test_unsafe_archive_policies_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in (
                "docs/archive",
                "skills",
                "docs/base",
                "docs/design",
            ):
                (root / relative).mkdir(parents=True, exist_ok=True)
            for source in (
                "AGENTS.md",
                "docs/DOCUMENTATION_MAP.md",
                "docs/PROJECT_CONTEXT.md",
                "docs/base/SKILL_REGISTRY.json",
            ):
                path = root / source
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("{}" if path.suffix == ".json" else "current", encoding="utf-8")
            archive_adapter = json.loads((ROOT / "docs/archive/ARCHIVE_RETENTION_ADAPTER.json").read_text(encoding="utf-8"))
            archive_adapter["policies"]["blank_placeholders_allowed"] = True
            archive_adapter["policies"]["secrets_may_be_archived"] = True
            (root / "docs/archive/ARCHIVE_RETENTION_ADAPTER.json").write_text(json.dumps(archive_adapter), encoding="utf-8")
            (root / "docs/archive/MANIFEST.json").write_text('{"schema_version":1,"manifest_role":"project-archive-retention-index","records":[]}', encoding="utf-8")
            (root / "docs/archive/README.md").write_text("현재 정본이 아니며 구현 권한이 없습니다\n원문을 비우지 않습니다\n비밀키", encoding="utf-8")
            (root / "skills/BASE_SHARED_SKILL_ROUTES.json").write_text((ROOT / "skills/BASE_SHARED_SKILL_ROUTES.json").read_text(encoding="utf-8"), encoding="utf-8")
            (root / "skills/PROJECT_BASE_SKILL_ADAPTER.json").write_text((ROOT / "skills/PROJECT_BASE_SKILL_ADAPTER.json").read_text(encoding="utf-8"), encoding="utf-8")
            errors = checker.validate(root)
            self.assertIn("unsafe archive policy: blank_placeholders_allowed", errors)
            self.assertIn("unsafe archive policy: secrets_may_be_archived", errors)

    def test_empty_archived_markdown_is_rejected(self) -> None:
        manifest = {
            "schema_version": 1,
            "manifest_role": "project-archive-retention-index",
            "records": [{
                "archive_id": "empty",
                "classification": "ARCHIVE_HISTORY",
                "original_path": "docs/old.md",
                "current_path": "docs/archive/empty.md",
                "content_sha256": "0" * 64,
                "archived_at": "2026-07-25",
                "superseded_by": ["docs/PROJECT_CONTEXT.md"],
                "reason": "test",
                "active_authority": False,
                "implementation_authority": "NONE",
                "compatibility_consumers": [],
                "rollback_ref": "a" * 40,
                "validation_status": "NOT_RUN",
            }],
        }
        original = (ROOT / "docs/archive/MANIFEST.json").read_text(encoding="utf-8")
        empty_path = ROOT / "docs/archive/empty.md"
        try:
            empty_path.write_text("---\narchive_metadata: true\n---\n", encoding="utf-8")
            (ROOT / "docs/archive/MANIFEST.json").write_text(json.dumps(manifest), encoding="utf-8")
            errors = checker.validate(ROOT)
            self.assertIn("archived Markdown body is empty: docs/archive/empty.md", errors)
        finally:
            (ROOT / "docs/archive/MANIFEST.json").write_text(original, encoding="utf-8")
            empty_path.unlink(missing_ok=True)

    def test_shared_skill_body_is_not_copied_locally(self) -> None:
        self.assertFalse((ROOT / "skills/governing-legacy-retention-and-archives/SKILL.md").exists())


if __name__ == "__main__":
    unittest.main()
