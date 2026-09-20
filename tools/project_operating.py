"""Project-selected router projection over the unchanged Base release validator.

Only the generated router body is specialized; protected-path, release, schema,
hash, and other generated-view checks remain the upstream implementation.
"""
import argparse
import importlib
import pathlib
import sys
import json
import re
import subprocess


def selected_source_errors(adapter, base=None):
    errors = []
    overrides = adapter.get('shared_overrides', {})
    if not isinstance(overrides, dict):
        return ['shared_overrides must be an object']
    for sid, value in overrides.items():
        if not isinstance(value, dict):
            errors.append(f'Invalid override: {sid}')
            continue
        if 'selected_source' not in value:
            continue
        source = value['selected_source']
        if not isinstance(source, dict):
            errors.append(f'Invalid selected source: {sid}')
            continue
        commit, path = source.get('commit', ''), source.get('path', '')
        if not isinstance(commit, str) or not re.fullmatch(r'[0-9a-f]{40}', commit):
            errors.append(f'Invalid selected commit: {sid}')
            continue
        if path != f'skills/{sid}/SKILL.md':
            errors.append(f'Invalid selected path: {sid}')
            continue
        if base is not None:
            for obj in (f'{commit}^{{commit}}', f'{commit}:{path}'):
                result = subprocess.run(['git', '-C', str(base), 'cat-file', '-e', obj],
                                        capture_output=True)
                if result.returncode:
                    errors.append(f'Missing selected Base object: {obj}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-tools', type=pathlib.Path, required=True)
    parser.add_argument('--base-repository', type=pathlib.Path, required=True)
    parser.add_argument('--project-root', type=pathlib.Path,
                        default=pathlib.Path(__file__).resolve().parents[1])
    parser.add_argument('--protected-base', default='')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write', action='store_true')
    group.add_argument('--check', action='store_true')
    args = parser.parse_args()
    sys.path.insert(0, str(args.base_tools.resolve()))
    contract = importlib.import_module('project_operating_contract')
    importlib.import_module('base_release_index').install_release_lock_paths(contract)

    def router(adapter):
        body = adapter['shared_overrides']['managing-game-project-operating-system']['router_body']
        return (body.rstrip() + '\n').encode('utf-8')

    contract._project_router = router
    root, base = args.project_root.resolve(), args.base_repository.resolve()
    try:
        adapter = json.loads((root / 'skills/PROJECT_BASE_ADAPTER.json').read_text(encoding='utf-8'))
        errors = selected_source_errors(adapter, base)
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            return 1
        if args.write:
            changed = contract.write_or_check_artifacts(root, base, check=False,
                                                       protected_base=args.protected_base)
            print(f'Generated {len(changed)} project operating views')
        else:
            errors = contract.validation_errors(root, base, check_generated=True,
                                                protected_base=args.protected_base)
            if errors:
                for error in errors:
                    print(error, file=sys.stderr)
                return 1
            print('Project operating contract validation passed (project router projection)')
    except (contract.ContractError, KeyError, TypeError, ValueError, OSError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
