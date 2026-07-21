from __future__ import annotations

import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("router", ROOT / "tools" / "route_skills.py")
router = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(router)
REGISTRY, ALIASES = router.load_contract(ROOT / "docs/base/SKILL_REGISTRY.json")


def flatten(result: dict) -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for stage in result["stages"]:
        for skill in stage["skills"]:
            found.setdefault(skill["id"], set()).update(skill["modes"])
    return found


class SkillRoutingContractTests(unittest.TestCase):
    def test_base_optimization_request_uses_full_loop(self) -> None:
        result = router.route(
            "Base를 전부 읽고 반영한 뒤 가지치기 간소화 리팩토링 통합 최적화하고 적대적 검토 레드팀 PR 체크",
            REGISTRY,
            ALIASES,
        )
        self.assertEqual(["PLAN", "BUILD", "REVIEW"], result["work_mode_sequence"])
        found = flatten(result)
        required = {
            "foundation.project-operating-system",
            "foundation.skill-evolution",
            "foundation.pruning",
            "foundation.skill-simplification",
            "foundation.contract-refactor",
            "foundation.adversarial-review",
            "foundation.validation-review",
            "discipline.integration-review",
        }
        self.assertTrue(required.issubset(found))

    def test_runtime_failure_routes_engineering_and_qa(self) -> None:
        result = router.route("Godot runtime crash와 signal node 오류를 재현하고 수정 후 회귀 검토", REGISTRY, ALIASES)
        found = flatten(result)
        self.assertIn("runtime-diagnosis", found["discipline.engineering"])
        self.assertTrue({"runtime-diagnosis-support", "reproduction"} & found["discipline.qa"])

    def test_concept_research_and_vertical_slice_are_preserved(self) -> None:
        result = router.route("게임 콘셉트 DDD 벤치마킹 플레이테스트 PoC 수직 슬라이스 MVP 계획", REGISTRY, ALIASES)
        found = flatten(result)
        self.assertIn("discipline.game-design", found)
        self.assertTrue({"concept-frame", "sharpen", "poc-contract", "vertical-slice"} & found["discipline.game-design"])
        self.assertIn("discipline.analytics-research", found)
        self.assertIn("discipline.production-pm", found)

    def test_user_research_coverage_routes_to_analytics(self) -> None:
        result = router.route("Games User Research 11영역과 텔레메트리 퍼널 밸런스 데이터 coverage를 감사", REGISTRY, ALIASES)
        found = flatten(result)
        self.assertIn("coverage-11", found["discipline.analytics-research"])
        self.assertTrue({"telemetry-funnel", "balance-data"} & found["discipline.analytics-research"])

    def test_art_prompt_and_ui_audit_are_domain_modes(self) -> None:
        prompt_result = router.route("아트 프롬프트와 기법 카드를 설계", REGISTRY, ALIASES)
        prompt_found = flatten(prompt_result)
        self.assertIn("discipline.art", prompt_found)
        self.assertTrue({"art-prompt", "technique-card"} & prompt_found["discipline.art"])
        audit_result = router.route("UI 아트 검수와 visual audit를 수행", REGISTRY, ALIASES)
        audit_found = flatten(audit_result)
        self.assertIn("ui-art-audit", audit_found["discipline.ux-ui-accessibility"])

    def test_learning_note_dashboard_sync_and_continuity_modes(self) -> None:
        learning = flatten(router.route("완료 작업을 사용자 학습 노트로 작성", REGISTRY, ALIASES))
        self.assertIn("learning-note", learning["foundation.design-documents"])
        dashboard = flatten(router.route("프로젝트 HTML 대시보드를 정본에 연결해 구축", REGISTRY, ALIASES))
        self.assertIn("visual-dashboard", dashboard["foundation.design-documents"])
        sync = flatten(router.route("로컬 GitHub branch가 diverged인지 확인하고 git sync", REGISTRY, ALIASES))
        self.assertIn("sync-local-github", sync["foundation.project-operating-system"])
        continuity = flatten(router.route("긴 작업 checkpoint를 남기고 다음 세션에서 resume", REGISTRY, ALIASES))
        self.assertTrue({"checkpoint", "resume"} & continuity["foundation.context-handoff"])

    def test_project_core_modes_preserve_authority_boundary(self) -> None:
        identify = flatten(router.route("기존 프로젝트 코어와 core vs MVP를 판정", REGISTRY, ALIASES))
        self.assertIn("identify-existing", identify["foundation.project-core"])
        confirm = flatten(router.route("새 프로젝트 코어를 제안하고 stress test 후 사용자 승인으로 확정", REGISTRY, ALIASES))
        self.assertTrue({"propose", "stress-test", "confirm"} & confirm["foundation.project-core"])

    def test_legacy_specialist_alias_resolves(self) -> None:
        result = router.route("UI 검수", REGISTRY, ALIASES, forced_skills=["specialist.ui-art-audit"])
        found = flatten(result)
        self.assertIn("ui-art-audit", found["discipline.ux-ui-accessibility"])


    def test_review_stage_never_selects_build_only_modes(self) -> None:
        result = router.route(
            "Base를 반영하고 스킬 통합 최적화한 뒤 PR을 검토",
            REGISTRY,
            ALIASES,
        )
        registry_by_id = {skill["id"]: skill for skill in REGISTRY["skills"]}
        review = next(stage for stage in result["stages"] if stage["work_mode"] == "REVIEW")
        for item in review["skills"]:
            permissions = registry_by_id[item["id"]]["mode_work_modes"]
            for mode in item["modes"]:
                self.assertIn("REVIEW", permissions[mode], f"{item['id']}:{mode}")

    def test_unknown_manual_skill_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            router.route("검토", REGISTRY, ALIASES, forced_skills=["missing.skill"])

    def test_no_more_than_three_disciplines_are_selected(self) -> None:
        result = router.route("게임 룰렛 UI 아트 Godot 코드 QA 분석 일정 사운드 통합 검토", REGISTRY, ALIASES)
        selected = {
            item["id"]
            for stage in result["stages"]
            for item in stage["skills"]
            if item["id"].startswith("discipline.")
            and item["id"] != "discipline.integration-review"
        }
        self.assertLessEqual(len(selected), 3)


if __name__ == "__main__":
    unittest.main()
