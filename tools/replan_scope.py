"""User-approved, project-local BUILD scope. Does not rewrite Base validation."""
from __future__ import annotations
import argparse
import importlib
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
APPROVAL = 'docs/process/APPROVED_REPLAN_UI_MOTION_BUILD_SCOPE_20260911.md'
# Exact files only: adding a sibling module requires a reviewed scope amendment.
ALLOWED = {
    'docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json',
    'docs/design/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911.md',
    'tools/ward_motion.py', 'tests/test_ward_motion.py',
    'docs/images/candidates/blueprint-20260911/ward-shield-motion.png',
    'docs/images/candidates/blueprint-20260911/ward-shield-motion.png.import',
    'docs/images/candidates/blueprint-20260911/ward-shield-motion.aseprite',
    'docs/images/candidates/blueprint-20260911/ward-shield-motion.json',
    'tools/veil_cutout.py', 'tests/test_veil_cutout.py',
    'docs/images/candidates/blueprint-20260911/veil-roster-alpha.png',
    'docs/images/candidates/blueprint-20260911/veil-special-alpha.png',
    'docs/images/candidates/blueprint-20260911/veil-roster-alpha.aseprite',
    'docs/images/candidates/blueprint-20260911/veil-special-alpha.aseprite',
    'AGENTS.md', APPROVAL,
    'project.godot', 'scenes/replan/front_slice.tscn',
    'scripts/replan/front_art.gd', 'scripts/replan/front_art.gd.uid',
    'scripts/replan/front_run.gd', 'scripts/replan/front_run.gd.uid',
    'scripts/replan/front_screen.gd', 'scripts/replan/front_screen.gd.uid',
    'docs/ACTIVE_CONTEXT.md', 'docs/CURRENT_CONFIRMED_DECISIONS.md',
    'docs/OMENWARD_ROADMAP.md',
    'docs/images/candidates/blueprint-20260911/ROSTER_PROVENANCE.md',
    'docs/images/candidates/blueprint-20260911/ward-shield-slash-alpha-candidate.png',
    'docs/images/candidates/blueprint-20260911/ward-shield-slash-alpha-candidate.png.import',
    'docs/superpowers/plans/2026-09-11-visible-battle-slice.md',
    'output/front-battle.png', 'output/front-building.png',
    'output/front-battle-1080.png',
    'output/front-mixed.png', 'output/front-mixed-1080.png',
    'output/front-recovery.png',
    'output/front-omen.png',
    'output/front-campaign.png',
    'output/front-shield-windup.png', 'output/front-shield-impact.png', 'output/front-shield-recover.png',
    'tests/replan_slice_test.gd', 'tests/replan_slice_test.gd.uid',
    'tests/replan_screen_test.gd', 'tests/replan_screen_test.gd.uid',
    'tests/replan_capture.gd', 'tests/replan_capture.gd.uid',
    'tools/validate_replan_slice.ps1', 'tools/replan_scope.py', 'tests/test_replan_scope.py',
    '.github/workflows/validate-base-v9-adoption.yml',
    '.github/workflows/validate-active-integrated-contract-v4-4.yml',
}

def unapproved(paths):
    return sorted(set(paths) - ALLOWED)

def unresolved(errors):
    remaining = []
    prefix = 'Protected-path changes detected: '
    for error in errors:
        if error.startswith(prefix):
            paths = error[len(prefix):].split(', ')
            if paths and all(paths) and not unapproved(paths):
                continue
        remaining.append(error)
    return remaining

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-repository', type=Path)
    parser.add_argument('--base', help='Git comparison base for the scoped PR check')
    args = parser.parse_args()
    if not (ROOT / APPROVAL).is_file():
        parser.error('Missing project approval owner')
    if args.base_repository:
        # Execute the unchanged pinned validator including locks/schema/authority checks.
        sys.path.insert(0, str(args.base_repository.resolve() / 'tools'))
        module = importlib.import_module('project_operating_contract')
        release = importlib.import_module('base_release_index')
        release.install_release_lock_paths(module)
        errors = module.validation_errors(ROOT, args.base_repository.resolve(), check_generated=True)
        print('BASE_RAW_RESULT:', 'FAIL' if errors else 'PASS')
        for error in errors:
            print('BASE:', error)
        pending = unresolved(errors)
        if pending:
            print('PROJECT_SCOPED_BUILD: FAIL', pending)
            return 1
    elif args.base:
        paths = subprocess.check_output(['git', 'diff', '--name-only', '--no-renames', '-z', args.base, 'HEAD'], cwd=ROOT).decode().split('\0')
        pending = unapproved(p for p in paths if p)
        if pending:
            print('PROJECT_SCOPED_BUILD: FAIL', pending)
            return 1
    else:
        parser.error('Supply --base-repository or --base')
    print('PROJECT_SCOPED_BUILD: PASS; NOT Base raw PASS or runtime/Human approval')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
