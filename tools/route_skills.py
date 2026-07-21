#!/usr/bin/env python3
"""Deterministic Omenward Work Mode and Skill router."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from dataclasses import dataclass
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "docs" / "base" / "SKILL_REGISTRY.json"

REVIEW_WORDS = ("검토", "검수", "리뷰", "감사", "누락", "중복", "adversarial", "red team", "critique", "review", "validate", "audit", "pr")
BUILD_WORDS = ("구현", "수정", "고쳐", "추가", "삭제", "리팩터", "build", "implement", "fix", "add", "remove", "refactor")
PLAN_WORDS = ("기획", "계획", "제안", "설계", "분석", "plan", "proposal", "design", "analyze")


@dataclass(frozen=True)
class Match:
    skill_id: str
    score: int
    category: str
    priority: int


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def contains_any(text: str, words: Iterable[str]) -> bool:
    return any(normalize(word) in text for word in words)


def infer_mode(request: str) -> str:
    text = normalize(request)
    if contains_any(text, REVIEW_WORDS):
        return "REVIEW"
    if contains_any(text, BUILD_WORDS):
        return "BUILD"
    if contains_any(text, PLAN_WORDS):
        return "PLAN"
    return "PLAN"


def score_skill(request: str, skill: dict) -> int:
    text = normalize(request)
    score = 0
    for trigger in skill["triggers"]:
        token = normalize(trigger)
        if token and token in text:
            score += max(1, len(token.split()))
    for exclusion in skill.get("not_use", []):
        token = normalize(exclusion)
        if token and token in text:
            score -= 5
    return score


def _dependency_first_order(selected: list[str], known: dict[str, dict]) -> list[str]:
    ordered: list[str] = []
    permanent: set[str] = set()
    temporary: set[str] = set()

    def visit(skill_id: str) -> None:
        if skill_id in permanent:
            return
        if skill_id in temporary:
            raise ValueError(f"Circular Skill dependency: {skill_id}")
        temporary.add(skill_id)
        for dependency in known[skill_id].get("depends_on", []):
            if dependency not in known:
                raise ValueError(f"Unknown dependency {dependency} in {skill_id}")
            visit(dependency)
        temporary.remove(skill_id)
        permanent.add(skill_id)
        ordered.append(skill_id)

    for skill_id in selected:
        visit(skill_id)
    return ordered


def route(request: str, registry: dict, forced_mode: str | None = None, forced_skills: list[str] | None = None) -> dict:
    mode = forced_mode or infer_mode(request)
    known = {skill["id"]: skill for skill in registry["skills"]}
    selected: list[str] = []
    reasons: dict[str, str] = {}

    def add(skill_id: str, reason: str) -> None:
        if skill_id not in known:
            raise ValueError(f"Unknown registered Skill ID: {skill_id}")
        if skill_id not in selected:
            selected.append(skill_id)
            reasons[skill_id] = reason

    for skill_id in registry["routing"]["always_on"]:
        add(skill_id, "always_on")

    matches: list[Match] = []
    for skill in registry["skills"]:
        score = score_skill(request, skill)
        if score > 0:
            matches.append(Match(skill["id"], score, skill["category"], skill["priority"]))
    matches.sort(key=lambda item: (-item.score, -item.priority, item.skill_id))

    disciplines = [m for m in matches if m.category == "disciplines"]
    if disciplines:
        add(disciplines[0].skill_id, f"primary_discipline score={disciplines[0].score}")
        for match in disciplines[1 : 1 + registry["routing"]["max_support_disciplines"]]:
            add(match.skill_id, f"support_discipline score={match.score}")

    for match in matches:
        if match.category == "foundation" and match.skill_id not in registry["routing"]["always_on"]:
            add(match.skill_id, f"foundation_trigger score={match.score}")
        elif match.category == "specialists":
            add(match.skill_id, f"specialist_trigger score={match.score}")

    if mode == "REVIEW":
        for skill_id in registry["routing"]["review_stack"]:
            add(skill_id, "mandatory_review_stack")

    for skill_id in forced_skills or []:
        add(skill_id, "manual_override")

    ordered = _dependency_first_order(selected, known)
    for skill_id in ordered:
        reasons.setdefault(skill_id, "dependency")

    return {
        "request": request,
        "mode": mode,
        "skills": [{"id": skill_id, "reason": reasons[skill_id], "path": known[skill_id]["path"]} for skill_id in ordered],
    }


def load_registry(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--registry", type=pathlib.Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--mode", choices=("PLAN", "BUILD", "REVIEW"))
    parser.add_argument("--skill", action="append", default=[])
    args = parser.parse_args()
    try:
        result = route(args.request, load_registry(args.registry), args.mode, args.skill)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
