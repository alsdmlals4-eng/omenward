from __future__ import annotations

import pathlib
import tempfile
import textwrap
import unittest

from tools.platform_boundary_guard import (
    DEFAULT_LEGACY_ALLOWLIST,
    LegacyAllowance,
    scan_forbidden_references,
)

ROOT = pathlib.Path(__file__).resolve().parents[2]


class PlatformBoundaryStaticGuardTests(unittest.TestCase):
    def test_detects_code_but_ignores_comments_and_string_literals(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = pathlib.Path(temporary_directory)
            target = root / "scripts/core/sample.gd"
            target.parent.mkdir(parents=True)
            target.write_text(
                textwrap.dedent(
                    '''\
                    extends RefCounted
                    # Input.is_action_pressed("ignored")
                    var label := "DisplayServer FileAccess Steam GooglePlay"
                    var pressed := Input.is_action_pressed("move")
                    '''
                ),
                encoding="utf-8",
            )

            report = scan_forbidden_references(
                [target.parent],
                repository_root=root,
                allowlist=(),
            )

            self.assertEqual(1, len(report.unapproved))
            self.assertEqual("INPUT_SINGLETON", report.unapproved[0].rule_id)
            self.assertEqual(4, report.unapproved[0].line_number)

    def test_allowlist_is_exact_and_cannot_hide_a_second_usage(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = pathlib.Path(temporary_directory)
            target = root / "scripts/core/legacy.gd"
            target.parent.mkdir(parents=True)
            target.write_text(
                'var first := Input.is_action_pressed("move")\n'
                'var second := Input.is_action_pressed("cancel")\n',
                encoding="utf-8",
            )
            allowlist = (
                LegacyAllowance(
                    path="scripts/core/legacy.gd",
                    rule_id="INPUT_SINGLETON",
                    code='var first := Input.is_action_pressed("move")',
                    reason="fixture legacy call",
                ),
            )

            report = scan_forbidden_references(
                [target.parent],
                repository_root=root,
                allowlist=allowlist,
            )

            self.assertEqual(1, len(report.allowed))
            self.assertEqual(1, len(report.unapproved))
            self.assertIn("cancel", report.unapproved[0].code)
            self.assertEqual([], report.stale_allowances)

    def test_current_repository_has_no_legacy_exceptions(self) -> None:
        roots = [ROOT / "scripts/core"]
        domain_root = ROOT / "scripts/domain"
        if domain_root.exists():
            roots.append(domain_root)
        self.assertTrue(roots[0].is_dir(), "scripts/core must exist")

        report = scan_forbidden_references(
            roots,
            repository_root=ROOT,
            allowlist=DEFAULT_LEGACY_ALLOWLIST,
        )

        self.assertGreater(report.scanned_files, 0)
        self.assertEqual([], report.unapproved)
        self.assertEqual([], report.stale_allowances)
        self.assertEqual(0, len(report.allowed))
        self.assertEqual((), DEFAULT_LEGACY_ALLOWLIST)


if __name__ == "__main__":
    unittest.main()
