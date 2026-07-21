#!/usr/bin/env python3
"""Validate the Omenward Skill registry and packages without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "docs" / "base" / "SKILL_REGISTRY.json"
SCHEMA_PATH = ROOT / "schemas" / "skill-registry-v3.schema.json"
SHARED = ROOT / "skills" / "SHARED_EXECUTION_CONTRACT.md"
REQUIRED_SECTIONS = (
    "## 사용 조건",
    "## 사용하지 않는 조건",
    "## 고유 책임",
    "## 입력",
    "## 절차",
    "## 출력",
    "## 고유 검수",
)


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

    skills = registry.get("skills", [])
    skill_schema = schema["properties"]["skills"]["items"]
    for index, skill in enumerate(skills):
        check_shape(errors, skill, skill_schema, f"skills[{index}]")

    ids = [s.get("id") for s in skills]
    paths = [s.get("path") for s in skills]
    if len(ids) != len(set(ids)):
        fail(errors, "duplicate Skill IDs")
    if len(paths) != len(set(paths)):
        fail(errors, "duplicate Skill paths")
    if len(skills) != 24:
        fail(errors, "registry must contain 24 optimized Skill packages")
    if registry.get("base_source", {}).get("commit") != "ee265576da7f67d3278f8099dd97d4e714ef0651":
        fail(errors, "Base source commit is not the audited Base main commit")
    if registry.get("base_source", {}).get("policy") != "project_canon_first_explicit_adoption_no_auto_overwrite":
        fail(errors, "Base adoption policy is missing or unsafe")
    if not SHARED.is_file():
        fail(errors, "missing shared execution contract")

    registered_disciplines = {s["id"] for s in skills if s.get("category") == "disciplines"}
    selected_disciplines = set(registry.get("selected_disciplines", []))
    if len(selected_disciplines) != 11 or selected_disciplines != registered_disciplines:
        fail(errors, "selected_disciplines must exactly match the 11 registered Omenward disciplines")

    registered = set(paths)
    actual = {path.relative_to(ROOT).as_posix() for path in (ROOT / "skills").glob("*/*/SKILL.md")}
    if registered != actual:
        fail(errors, f"registry/package mismatch missing={sorted(registered-actual)} orphan={sorted(actual-registered)}")

    known = set(ids)
    category_roots = {"foundation": "foundation", "disciplines": "disciplines", "specialists": "specialists"}
    for skill in skills:
        skill_id = skill.get("id", "<missing>")
        path_text = skill.get("path", "")
        path = ROOT / path_text
        category = skill.get("category")
        if category in category_roots and not path_text.startswith(f"skills/{category_roots[category]}/"):
            fail(errors, f"category/path mismatch: {skill_id}")
        if not path.is_file():
            fail(errors, f"missing package: {path_text}")
            continue
        if not path.resolve().is_relative_to((ROOT / "skills").resolve()):
            fail(errors, f"path escapes skills root: {path_text}")
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
        normalized_triggers = [re.sub(r"\s+", " ", item.casefold()).strip() for item in skill.get("triggers", [])]
        if len(normalized_triggers) != len(set(normalized_triggers)):
            fail(errors, f"duplicate normalized triggers in {skill_id}")
        for dependency in skill.get("depends_on", []):
            if dependency not in known:
                fail(errors, f"unknown dependency {dependency} in {skill_id}")

    detect_dependency_cycles(skills, errors)
    routing = registry.get("routing", {})
    if "foundation.project-intake" not in routing.get("always_on", []):
        fail(errors, "project intake must be always-on")
    review = {"foundation.validation-review", "discipline.integration-review"}
    if not review.issubset(routing.get("review_stack", [])):
        fail(errors, "mandatory adversarial review stack is incomplete")
    if routing.get("max_primary_disciplines") != 1 or routing.get("max_support_disciplines", 99) > 2:
        fail(errors, "discipline routing limits are unsafe")
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
    print(f"Skill system validation PASSED: {len(registry['skills'])} packages, {len(registry['selected_disciplines'])} disciplines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
