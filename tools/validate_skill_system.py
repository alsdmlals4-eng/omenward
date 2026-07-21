#!/usr/bin/env python3
"""Validate Omenward's optimized, no-loss Skill system without third-party packages."""

from __future__ import annotations

import argparse
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "docs" / "base" / "SKILL_REGISTRY.json"
SCHEMA_PATH = ROOT / "schemas" / "skill-registry-v4.schema.json"
REQUIRED_SECTIONS = (
    "## 사용 조건",
    "## 사용하지 않는 조건",
    "## 고유 책임",
    "## 입력",
    "## 절차",
    "## 출력",
    "## 고유 검수",
)
EXPECTED_BASE_COMMIT = "41a20584dd2ee51d917e5c9d7cab6838e1ceba7e"
EXPECTED_BASE_SKILLS = {
    "managing-project-intake-and-work-contract",
    "managing-game-project-operating-system",
    "evolving-project-discipline-skills",
    "managing-design-documents",
    "maintaining-project-context-and-handoff",
    "analyzing-and-refining-game-concepts",
    "designing-vertical-slices",
    "orchestrating-deepseek-worktrees",
    "reviewing-and-validating-project-changes",
    "auditing-canonical-reference-freshness",
    "designing-art-prompts-and-technique-cards",
    "auditing-and-refining-ui-art",
    "managing-base-change-proposals",
    "identifying-project-core",
    "establishing-project-core",
    "running-adversarial-review-and-refinement",
    "refactoring-with-contract-preservation",
    "simplifying-skill-bodies",
    "pruning-stale-and-nonfunctional-material",
    "synchronizing-local-and-github-state",
    "maintaining-long-running-task-continuity",
    "governing-game-user-research-coverage",
    "creating-user-learning-notes",
    "building-project-visual-dashboards",
    "diagnosing-game-engine-runtime-failures",
}
REMOVED_SPECIALIST_PATHS = {
    "skills/specialists/analyzing-and-refining-game-concepts/SKILL.md",
    "skills/specialists/auditing-and-refining-ui-art/SKILL.md",
    "skills/specialists/auditing-canonical-reference-freshness/SKILL.md",
    "skills/specialists/designing-art-prompts-and-technique-cards/SKILL.md",
    "skills/specialists/designing-vertical-slices/SKILL.md",
    "skills/specialists/orchestrating-deepseek-worktrees/SKILL.md",
}
REQUIRED_OLD_ALIASES = {
    "specialist.game-concept",
    "specialist.ui-art-audit",
    "specialist.canonical-freshness",
    "specialist.art-prompts",
    "specialist.vertical-slice",
    "specialist.deepseek-worktrees",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_shape(errors: list[str], value: dict, schema: dict, label: str) -> None:
    required = set(schema.get("required", []))
    properties = set(schema.get("properties", {}))
    missing = required - set(value)
    unknown = set(value) - properties if schema.get("additionalProperties") is False else set()
    if missing:
        fail(errors, f"{label} missing schema fields: {sorted(missing)}")
    if unknown:
        fail(errors, f"{label} has fields outside schema: {sorted(unknown)}")


def detect_dependency_cycles(skills: list[dict], errors: list[str]) -> None:
    known = {skill["id"]: skill for skill in skills}
    permanent: set[str] = set()
    temporary: set[str] = set()

    def visit(skill_id: str) -> None:
        if skill_id in permanent:
            return
        if skill_id in temporary:
            fail(errors, f"circular dependency involving {skill_id}")
            return
        temporary.add(skill_id)
        for dependency in known[skill_id].get("depends_on", []):
            if dependency in known:
                visit(dependency)
        temporary.remove(skill_id)
        permanent.add(skill_id)

    for skill_id in known:
        visit(skill_id)


def validate(registry_path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    check_shape(errors, registry, schema, "registry")
    check_shape(errors, registry.get("base_source", {}), schema["properties"]["base_source"], "base_source")
    check_shape(errors, registry.get("routing", {}), schema["properties"]["routing"], "routing")

    if registry.get("schema_version") != 4:
        fail(errors, "registry schema_version must be 4")
    if registry.get("base_source", {}).get("commit") != EXPECTED_BASE_COMMIT:
        fail(errors, "Base source commit is not the latest audited Base main")
    if registry.get("base_source", {}).get("policy") != "project_canon_first_explicit_adoption_no_auto_overwrite":
        fail(errors, "Base adoption policy is missing or unsafe")

    skills = registry.get("skills", [])
    skill_schema = schema["properties"]["skills"]["items"]
    for index, skill in enumerate(skills):
        check_shape(errors, skill, skill_schema, f"skills[{index}]")

    ids = [skill.get("id") for skill in skills]
    paths = [skill.get("path") for skill in skills]
    if len(skills) != 23:
        fail(errors, f"registry must contain 23 optimized packages, found {len(skills)}")
    if len(ids) != len(set(ids)):
        fail(errors, "duplicate Skill IDs")
    if len(paths) != len(set(paths)):
        fail(errors, "duplicate Skill paths")

    known = {skill["id"]: skill for skill in skills}
    categories = {"foundation": "foundation", "disciplines": "disciplines"}
    for skill in skills:
        skill_id = skill["id"]
        category = skill["category"]
        path_text = skill["path"]
        path = ROOT / path_text
        if category not in categories:
            fail(errors, f"unsupported category: {category}")
        elif not path_text.startswith(f"skills/{categories[category]}/"):
            fail(errors, f"category/path mismatch: {skill_id}")
        if not path.is_file():
            fail(errors, f"missing package: {path_text}")
            continue
        text = path.read_text(encoding="utf-8")
        if f"`{skill_id}`" not in text:
            fail(errors, f"Skill ID not declared in package: {skill_id}")
        if "skills/SHARED_EXECUTION_CONTRACT.md" not in text:
            fail(errors, f"shared contract not referenced: {skill_id}")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                fail(errors, f"missing section {section}: {skill_id}")
        if re.search(r"\b(TODO|TBD|FIXME)\b", text):
            fail(errors, f"unfinished marker in {skill_id}")
        if len(text.splitlines()) > 90:
            fail(errors, f"Skill body is not compact: {skill_id} ({len(text.splitlines())} lines)")
        if not skill["modes"] or len(skill["modes"]) != len(set(skill["modes"])):
            fail(errors, f"invalid or duplicate modes: {skill_id}")
        mode_set = set(skill["modes"])
        if set(skill["mode_triggers"]) - mode_set:
            fail(errors, f"mode_triggers reference unknown modes: {skill_id}")
        if set(skill["mode_work_modes"]) != mode_set:
            fail(errors, f"mode_work_modes must cover every mode exactly: {skill_id}")
        for mode, stages in skill["mode_work_modes"].items():
            if not stages:
                fail(errors, f"mode has no allowed Work Mode: {skill_id} -> {mode}")
            if set(stages) - set(skill["work_modes"]):
                fail(errors, f"mode_work_modes outside Skill Work Modes: {skill_id} -> {mode}")
        for stage, modes in skill["default_modes"].items():
            if stage not in skill["work_modes"]:
                fail(errors, f"default mode stage not supported: {skill_id} -> {stage}")
            if set(modes) - mode_set:
                fail(errors, f"default_modes reference unknown modes: {skill_id} -> {stage}")
            if any(stage not in skill["mode_work_modes"][mode] for mode in modes if mode in mode_set):
                fail(errors, f"default_modes violate mode Work Mode: {skill_id} -> {stage}")
        for stage, modes in skill["required_modes"].items():
            if stage not in skill["work_modes"]:
                fail(errors, f"required mode stage not supported: {skill_id} -> {stage}")
            if set(modes) - mode_set:
                fail(errors, f"required_modes reference unknown modes: {skill_id} -> {stage}")
            if any(stage not in skill["mode_work_modes"][mode] for mode in modes if mode in mode_set):
                fail(errors, f"required_modes violate mode Work Mode: {skill_id} -> {stage}")
        normalized = [re.sub(r"\s+", " ", trigger.casefold()).strip() for trigger in skill["triggers"]]
        if len(normalized) != len(set(normalized)):
            fail(errors, f"duplicate normalized triggers: {skill_id}")
        for dependency in skill["depends_on"]:
            if dependency not in known:
                fail(errors, f"unknown dependency {dependency} in {skill_id}")

    registered = set(paths)
    actual = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "skills").glob("*/*/SKILL.md")
    }
    if registered != actual:
        fail(errors, f"registry/package mismatch missing={sorted(registered-actual)} orphan={sorted(actual-registered)}")
    for removed in REMOVED_SPECIALIST_PATHS:
        if (ROOT / removed).exists():
            fail(errors, f"pruned specialist package still exists: {removed}")

    selected = set(registry.get("selected_disciplines", []))
    disciplines = {skill["id"] for skill in skills if skill["category"] == "disciplines"}
    if len(disciplines) != 11 or selected != disciplines:
        fail(errors, "selected_disciplines must exactly match the 11 Omenward disciplines")

    routing = registry["routing"]
    if routing["entry_stack"] != ["foundation.project-intake"]:
        fail(errors, "entry_stack must contain only project intake")
    required_review = {
        "foundation.adversarial-review",
        "foundation.validation-review",
        "discipline.integration-review",
    }
    if not required_review.issubset(routing["review_stack"]):
        fail(errors, "mandatory adversarial review stack is incomplete")
    if routing["max_primary_disciplines"] != 1 or routing["max_support_disciplines"] > 2:
        fail(errors, "discipline routing limits are unsafe")
    detect_dependency_cycles(skills, errors)

    coverage_path = ROOT / registry["capability_coverage"]
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    if coverage.get("base_commit") != EXPECTED_BASE_COMMIT:
        fail(errors, "coverage Base commit mismatch")
    mappings = coverage.get("mappings", [])
    base_ids = [mapping.get("base_skill_id") for mapping in mappings]
    if set(base_ids) != EXPECTED_BASE_SKILLS or len(base_ids) != len(EXPECTED_BASE_SKILLS):
        fail(errors, f"Base capability coverage mismatch missing={sorted(EXPECTED_BASE_SKILLS-set(base_ids))} extra={sorted(set(base_ids)-EXPECTED_BASE_SKILLS)}")
    for mapping in mappings:
        if mapping.get("status") != "COVERED":
            fail(errors, f"Base capability is not covered: {mapping.get('base_skill_id')}")
        targets = mapping.get("local_targets", [])
        if not targets:
            fail(errors, f"Base capability has no local target: {mapping.get('base_skill_id')}")
        for target in targets:
            target_id = target.get("id")
            if target_id not in known:
                fail(errors, f"coverage target is not registered: {target_id}")
                continue
            unknown_modes = set(target.get("modes", [])) - set(known[target_id]["modes"])
            if unknown_modes:
                fail(errors, f"coverage target modes missing: {target_id} -> {sorted(unknown_modes)}")

    alias_path = ROOT / registry["legacy_aliases"]
    aliases = json.loads(alias_path.read_text(encoding="utf-8")).get("aliases", {})
    if not REQUIRED_OLD_ALIASES.issubset(aliases):
        fail(errors, f"old Omenward aliases missing: {sorted(REQUIRED_OLD_ALIASES-set(aliases))}")
    for source, alias in aliases.items():
        target = alias.get("target")
        if source in known:
            fail(errors, f"alias shadows active Skill ID: {source}")
        if target not in known:
            fail(errors, f"alias target not registered: {source} -> {target}")
            continue
        unknown_modes = set(alias.get("modes", [])) - set(known[target]["modes"])
        if unknown_modes:
            fail(errors, f"alias modes missing: {source} -> {sorted(unknown_modes)}")

    required_files = [
        registry["shared_contract"],
        registry["capability_coverage"],
        registry["legacy_aliases"],
        "skills/LEGACY_SKILL_ALIASES.md",
        "docs/base/START_HERE_SKILLS.md",
        "docs/base/WORK_MODE_AND_SKILL_ROUTING.md",
        "docs/base/PRUNING_LEDGER.md",
    ]
    for relative in required_files:
        if not (ROOT / relative).is_file():
            fail(errors, f"required entrypoint missing: {relative}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=pathlib.Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()
    try:
        errors = validate(args.registry)
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors = [f"validator could not read contract: {exc}"]
    if errors:
        print("Skill system validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    print(f"Skill system validation PASSED: {len(registry['skills'])} packages, 25/25 Base capabilities, 11 disciplines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
