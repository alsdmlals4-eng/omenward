"""Planning input invariants. These checks are not combat/runtime evidence."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json'

class BlueprintContractTests(unittest.TestCase):
    def setUp(self):
        self.d = json.loads(PATH.read_text(encoding='utf-8'))
        self.units = {u[0]: u for u in self.d['units']}
        self.buildings = {b[0]: b for b in self.d['building_tree']}

    def test_ten_roles_no_duplicates(self):
        self.assertEqual(len(self.units), 10)
        self.assertEqual(len(self.d['units']), 10)

    def test_families_disjoint_complete(self):
        a,b = map(set, [self.d['unit_families']['general'],self.d['unit_families']['special']])
        self.assertEqual((len(a),len(b)), (5,5))
        self.assertFalse(a & b)
        self.assertEqual(a|b,set(self.units))

    def test_two_independent_roots(self):
        self.assertEqual({b[0] for b in self.buildings.values() if b[1] is None}, {'barracks','special_barracks'})
        self.assertEqual(self.buildings['barracks'][4], 'shield_guard')

    def test_no_cross_family_specialization(self):
        for family,root in [('general','barracks'),('special','special_barracks')]:
            children=[b for b in self.buildings.values() if b[1]==root]
            self.assertEqual({b[4] for b in children},set(self.d['unit_families'][family]))
            self.assertTrue(all(b[2]==2 for b in children))

    def test_capstone_coverage_not_rebranch(self):
        self.assertEqual({r[0] for r in self.d['capstones']},set(self.units))
        self.assertEqual(len(self.d['capstones']),10)
        self.assertFalse(any(b[2]==3 for b in self.buildings.values()))

    def test_rank_skills_complete(self):
        self.assertEqual({r[0] for r in self.d['unit_progression']},set(self.units))
        self.assertTrue(all(all(r[2:6]) for r in self.d['unit_progression']))

    def test_all_building_costs_and_production_linked(self):
        production={b[0]:b for b in self.d['buildings']}
        for b in self.buildings.values():
            self.assertEqual(b[5],production[b[0]][2])
            self.assertGreater(production[b[0]][5],0)

    def test_basic_archer_path_affordable(self):
        self.assertLessEqual(self.buildings['barracks'][5]+self.buildings['range'][5],self.d['economy']['starting_gold'])

    def test_roulette_maximum_fits_queue(self):
        self.assertLessEqual(4*max(u[11] for u in self.units.values()),self.d['economy']['queue_capacity'])

    def test_wave_refs_and_times(self):
        e=self.d['economy']
        self.assertEqual(sorted(set(e['wave_times'])),e['wave_times'])
        self.assertTrue(all(0<t<e['round_seconds'] for t in e['wave_times']))
        for wave in self.d['wave_templates'].values():
            self.assertTrue(all(uid in self.units and n>0 for uid,n in wave))

    def test_campaign_counts(self):
        self.assertEqual(sum(m['rounds'] for m in self.d['maps']),53)
        self.assertEqual(len(self.d['maps']),5)

    def test_not_runtime_ready(self):
        self.assertEqual(self.d['status'],'REVIEW_EDITION_NOT_FINAL_IMPLEMENTATION_READY')

if __name__ == '__main__':
    unittest.main(verbosity=2)
