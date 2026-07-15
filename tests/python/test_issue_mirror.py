import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "tools"))

from issue_mirror import (  # noqa: E402
    has_bidirectional_conflict,
    render_issue_markdown,
    validate_issue_numbers,
    write_all_snapshots,
)


class IssueMirrorTests(unittest.TestCase):
    def setUp(self):
        self.issue = {
            "number": 1,
            "title": "[Plan] Bootstrap",
            "body": "Canonical implementation context.",
            "state": "open",
            "html_url": "https://github.com/example/omenward/issues/1",
            "labels": [{"name": "documentation"}],
            "assignees": [{"login": "owner"}],
            "updated_at": "2026-07-16T00:00:00Z",
        }

    def test_render_issue_marks_metadata_and_body(self):
        rendered = render_issue_markdown(self.issue, canonical_documents=["docs/goals/0001.md"])

        self.assertIn("issue_number: 1", rendered)
        self.assertIn('title: "[Plan] Bootstrap"', rendered)
        self.assertIn("state: open", rendered)
        self.assertIn("- documentation", rendered)
        self.assertIn("- owner", rendered)
        self.assertIn("- docs/goals/0001.md", rendered)
        self.assertIn("Canonical implementation context.", rendered)

    def test_render_issue_accepts_the_connector_issue_number_field(self):
        connector_issue = dict(self.issue)
        connector_issue["issue_number"] = connector_issue.pop("number")

        rendered = render_issue_markdown(connector_issue)

        self.assertIn("issue_number: 1", rendered)

    def test_snapshot_validation_requires_every_remote_issue_once(self):
        self.assertEqual(validate_issue_numbers({1, 2}, [1, 2]), [])
        self.assertEqual(validate_issue_numbers({1, 2}, [1, 1]), ["duplicate issue number: 1", "missing issue number: 2"])

    def test_conflict_blocks_when_local_and_remote_changed_after_last_sync(self):
        last_synced = hashlib.sha256(b"original").hexdigest()

        self.assertTrue(
            has_bidirectional_conflict(
                local_content="edited locally",
                last_synced_body_sha=last_synced,
                remote_body="edited remotely",
            )
        )
        self.assertFalse(
            has_bidirectional_conflict(
                local_content="original",
                last_synced_body_sha=last_synced,
                remote_body="edited remotely",
            )
        )
        self.assertFalse(
            has_bidirectional_conflict(
                local_content="edited locally",
                last_synced_body_sha=last_synced,
                remote_body="edited locally",
            )
        )

    def test_local_sync_command_refuses_dirty_worktrees_and_non_fast_forward_merges(self):
        sync_script = PROJECT_ROOT / "tools" / "sync_repo.ps1"
        script_text = sync_script.read_text(encoding="utf-8")

        self.assertIn("git status --porcelain", script_text)
        self.assertIn("git fetch origin --prune", script_text)
        self.assertIn("git pull --ff-only origin main", script_text)
        self.assertNotIn("git pull origin main", script_text)

    def test_write_all_snapshots_uses_stable_issue_number_filenames(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            snapshot_dir = Path(temporary_directory)
            second_issue = dict(self.issue, number=2, title="Second")

            write_all_snapshots([second_issue, self.issue], snapshot_dir)

            self.assertEqual([path.name for path in sorted(snapshot_dir.glob("*.md"))], ["0001.md", "0002.md"])

    def test_outbound_workflow_reads_remote_issue_before_updating_it(self):
        workflow = (PROJECT_ROOT / ".github" / "workflows" / "repo-to-issue.yml").read_text(encoding="utf-8")

        self.assertIn('method="GET"', workflow)
        self.assertIn("if current != desired", workflow)


if __name__ == "__main__":
    unittest.main()
