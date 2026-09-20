"""Exercise the cold-start router, not historical registry wording."""
import json
import pathlib
import subprocess
import sys
import tempfile
import copy
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import route_skills
import validate_skill_system


class CurrentRoutingTests(unittest.TestCase):
    def run_route(self, request, *args):
        result = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'tools/route_skills.py'),
                                 '--request', request, *args], capture_output=True, text=True,
                                encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_governance_does_not_load_game_design_or_legacy_stack(self):
        result = self.run_route('AGENTS Skill 작업구조 감사 및 규칙 경량화', '--mode', 'REVIEW')
        self.assertEqual([s['id'] for s in result['skills']],
                         ['managing-game-project-operating-system'])

    def test_godot_routes_to_registered_local_package(self):
        result = self.run_route('Godot 저장 버그 수정', '--mode', 'BUILD')
        self.assertEqual([s['id'] for s in result['skills']], ['omenward-godot'])
        self.assertTrue((ROOT / result['skills'][0]['path']).is_file())

    def test_review_without_domain_selects_only_review(self):
        result = self.run_route('검토', '--mode', 'REVIEW')
        self.assertEqual([s['id'] for s in result['skills']],
                         ['reviewing-and-validating-project-changes'])

    def test_unknown_explicit_skill_fails_closed(self):
        result = subprocess.run([sys.executable, str(ROOT / 'tools/route_skills.py'),
                                 '--request', '작업', '--skill', 'not-a-skill'], capture_output=True)
        self.assertEqual(result.returncode, 2)

    def test_english_build_is_not_ui_and_game_skill_is_not_governance(self):
        for request in ('build save system', 'Godot unit skill damage bug fix'):
            result = self.run_route(request, '--mode', 'BUILD')
            self.assertEqual([s['id'] for s in result['skills']], ['omenward-godot'])

    def test_bad_selected_source_is_rejected(self):
        from tools.project_operating import selected_source_errors
        data = json.loads((ROOT / 'skills/PROJECT_BASE_ADAPTER.json').read_text(encoding='utf-8'))
        data['shared_overrides']['managing-game-project-operating-system']['selected_source'] = {
            'commit': 'not-a-commit', 'path': '../../missing/SKILL.md'}
        self.assertTrue(selected_source_errors(data))

    def test_shared_router_projection_preserves_utf8_source(self):
        from tools.project_operating import project_router
        adapter = {'shared_overrides': {'managing-game-project-operating-system':
                                      {'router_body': '한국어 router\n\n'}}}
        self.assertEqual(project_router(adapter), '한국어 router\n'.encode('utf-8'))

    def test_stale_snapshot_is_rejected_by_current_validator(self):
        import shutil
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            shutil.copytree(ROOT / 'skills', root / 'skills')
            path = root / 'skills/PROJECT_SKILL_SNAPSHOT.json'
            value = json.loads(path.read_text(encoding='utf-8'))
            value['effective_routes']['omenward-godot']['status'] = 'INACTIVE'
            path.write_text(json.dumps(value), encoding='utf-8')
            self.assertTrue(validate_skill_system.validate(root / 'skills/SKILL_REGISTRY.json', root))

    def test_current_registry_validates_without_legacy_package_shape(self):
        self.assertEqual(validate_skill_system.validate(ROOT / 'skills/SKILL_REGISTRY.json', ROOT), [])

    def test_current_validator_rejects_escaping_package(self):
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            path = root / 'skills/SKILL_REGISTRY.json'
            path.parent.mkdir()
            path.write_text(json.dumps({'schema_version': 1, 'skills': [
                {'skill_id': 'bad', 'path': '../../outside/SKILL.md', 'status': 'ACTIVE'}]}), encoding='utf-8')
            self.assertTrue(validate_skill_system.validate(path, root))

    def test_governance_scope_rejects_product_and_unrelated_paths(self):
        from tools.validate_canon_freshness_v45_scope import validate_canon_freshness_scope
        allowed = ['AGENTS.md', 'docs/BASE_RULES_VERSION.md', 'tools/route_skills.py',
                   'tools/project_operating.py', 'tests/python/test_current_skill_routing.py']
        self.assertEqual(validate_canon_freshness_scope(allowed), [])
        for other in ('scripts/game.gd', 'assets/unit.png', '.codex/config.toml', '../escape'):
            self.assertTrue(validate_canon_freshness_scope(allowed + [other]))


if __name__ == '__main__':
    unittest.main()
