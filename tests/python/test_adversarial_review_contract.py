from __future__ import annotations

import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("router", ROOT / "tools" / "route_skills.py")
router = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(router)
REGISTRY, ALIASES = router.load_contract(ROOT / "docs/base/SKILL_REGISTRY.json")


class AdversarialReviewContractTests(unittest.TestCase):
    def test_review_always_contains_attack_validation_and_integration(self) -> None:
        result = router.route("PR 누락 중복을 적대적으로 검토", REGISTRY, ALIASES)
        review = next(stage for stage in result["stages"] if stage["work_mode"] == "REVIEW")
        ids = {item["id"] for item in review["skills"]}
        self.assertTrue({
            "foundation.adversarial-review",
            "foundation.validation-review",
            "discipline.integration-review",
        }.issubset(ids))

    def test_adversarial_skill_has_critique_validation_and_regression(self) -> None:
        result = router.route("red team critique refine 후 회귀 재검토", REGISTRY, ALIASES)
        modes = {
            mode
            for stage in result["stages"]
            for item in stage["skills"]
            if item["id"] == "foundation.adversarial-review"
            for mode in item["modes"]
        }
        self.assertIn("attack", modes)
        self.assertTrue({"validate-critique", "regression-recheck"} & modes)


    def test_review_required_verification_modes_cannot_be_shadowed(self) -> None:
        result = router.route(
            "Base를 전부 읽고 반영한 뒤 스킬 통합 최적화하고 PR 검토",
            REGISTRY,
            ALIASES,
        )
        review = next(stage for stage in result["stages"] if stage["work_mode"] == "REVIEW")
        found = {item["id"]: set(item["modes"]) for item in review["skills"]}
        self.assertIn("verify", found["foundation.project-operating-system"])
        self.assertIn("verify", found["foundation.skill-evolution"])
        self.assertTrue({"contract-check", "reference-freshness", "regression", "evidence-report"}.issubset(found["foundation.validation-review"]))
        self.assertTrue({"cross-discipline", "no-loss", "pr-check"}.issubset(found["discipline.integration-review"]))

    def test_pruning_chain_is_dependency_first(self) -> None:
        result = router.route("가지치기 간소화 리팩토링 후 검토", REGISTRY, ALIASES)
        build = next(stage for stage in result["stages"] if stage["work_mode"] == "BUILD")
        ids = [item["id"] for item in build["skills"]]
        self.assertLess(ids.index("foundation.project-operating-system"), ids.index("foundation.pruning"))
        self.assertLess(ids.index("foundation.pruning"), ids.index("foundation.skill-simplification"))
        self.assertLess(ids.index("foundation.skill-simplification"), ids.index("foundation.contract-refactor"))


if __name__ == "__main__":
    unittest.main()
