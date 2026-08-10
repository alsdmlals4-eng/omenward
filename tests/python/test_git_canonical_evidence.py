from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.git_canonical_evidence import git_blob_bytes, git_blob_sha256, git_tracked_paths_utf8


class GitCanonicalEvidenceTest(unittest.TestCase):
    def _repo(self, root: Path) -> None:
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "OMENWARD Test"], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.email", "omenward-test@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(root), "config", "core.autocrlf", "false"], check=True)

    def test_blob_hash_uses_committed_bytes_not_working_tree_newlines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._repo(root)
            evidence = root / "evidence.json"
            committed = b'{\n  "status": "PASS"\n}\n'
            evidence.write_bytes(committed)
            subprocess.run(["git", "-C", str(root), "add", "evidence.json"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "fixture"], check=True)

            evidence.write_bytes(committed.replace(b"\n", b"\r\n"))
            self.assertNotEqual(hashlib.sha256(evidence.read_bytes()).hexdigest(), hashlib.sha256(committed).hexdigest())
            self.assertEqual(git_blob_bytes(root, evidence), committed)
            self.assertEqual(git_blob_sha256(root, evidence), hashlib.sha256(committed).hexdigest())

    def test_tracked_paths_decode_utf8_without_git_quoting_or_console_codepage(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._repo(root)
            relative = "[수정제안서]/증거.md"
            target = root / relative
            target.parent.mkdir(parents=True)
            target.write_text("evidence\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", relative], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "unicode fixture"], check=True)

            self.assertIn(relative, git_tracked_paths_utf8(root))


if __name__ == "__main__":
    unittest.main()
