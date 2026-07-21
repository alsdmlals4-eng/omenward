#!/usr/bin/env python3
"""Stage-aware deterministic Omenward Work Mode, Skill, and Skill Mode router."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "docs" / "base" / "SKILL_REGISTRY.json"

REVIEW_WORDS = (
    "검토", "검수", "리뷰", "감사", "누락", "중복", "적대적", "레드팀",
    "adversarial", "red team", "critique", "review", "validate", "audit", "pr 체크",
)
BUILD_WORDS = (
    "반영", "구현", "수정", "고쳐", "추가", "삭제", "가지치기", "간소화",
    "작성", "생성", "만들", "구축",
    "리팩터", "통합", "최적화", "build", "implement", "fix", "add", "remove",
    "refactor", "prune", "migrate", "write", "create",
)
PLAN_WORDS = (
    "기획", "계획", "제안", "설계", "분석", "판정", "전부 읽", "대조",
    "plan", "proposal", "design", "analyze", "identify",
)


class Match:
    __slots__ = ("skill_id", "score", "category", "priority")

    def __init__(self, skill_id: str, score: int, category: str, priority: int) -> None:
        self.skill_id = skill_id
        self.score = score
        self.category = category
        self.priority = priority


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def contains_any(text: str, words: Iterable[str]) -> bool:
    return any(normalize(word) in text for word in words)


def infer_sequence(request: str) -> list[str]:
    text = normalize(request)
    has_review = contains_any(text, REVIEW_WORDS)
    has_build = contains_any(text, BUILD_WORDS)
    has_plan = contains_any(text, PLAN_WORDS)
    if has_build and has_review:
        return ["PLAN", "BUILD", "REVIEW"]
    if has_build:
        return ["BUILD", "REVIEW"]
    if has_plan and has_review:
        return ["PLAN", "REVIEW"]
    if has_review:
        return ["REVIEW"]
    if has_plan:
        return ["PLAN"]
    return ["PLAN"]


def score_tokens(request: str, tokens: Iterable[str]) -> int:
    text = normalize(request)
    score = 0
    for token in tokens:
        normalized = normalize(token)
        if normalized and normalized in text:
            score += max(1, len(normalized.split()))
    return score


def select_modes(request: str, skill: dict, stage: str, forced_modes: list[str] | None = None) -> list[str]:
    allowed = {
        mode for mode, stages in skill.get("mode_work_modes", {}).items()
        if stage in stages
    }
    required = [mode for mode in skill.get("required_modes", {}).get(stage, []) if mode in allowed]
    if forced_modes:
        unknown = set(forced_modes) - set(skill["modes"])
        forbidden = set(forced_modes) - allowed
        if unknown:
            raise ValueError(f"Unknown modes for {skill['id']}: {sorted(unknown)}")
        if forbidden:
            raise ValueError(f"Modes not allowed in {stage} for {skill['id']}: {sorted(forbidden)}")
        return list(dict.fromkeys(required + forced_modes))

    scored = [
        (score_tokens(request, tokens), mode)
        for mode, tokens in skill.get("mode_triggers", {}).items()
        if mode in allowed
    ]
    matched = [mode for score, mode in sorted(scored, key=lambda item: (-item[0], item[1])) if score > 0]
    if matched:
        return list(dict.fromkeys(required + matched[:3]))
    defaults = [mode for mode in skill.get("default_modes", {}).get(stage, []) if mode in allowed]
    selected = defaults or sorted(allowed)[:1]
    return list(dict.fromkeys(required + selected))


def load_contract(registry_path: pathlib.Path) -> tuple[dict, dict]:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    alias_path = ROOT / registry["legacy_aliases"]
    aliases = json.loads(alias_path.read_text(encoding="utf-8"))["aliases"]
    return registry, aliases


def resolve_manual_skill(skill_id: str, known: dict[str, dict], aliases: dict) -> tuple[str, list[str] | None, str]:
    if skill_id in known:
        return skill_id, None, "manual_override"
    if skill_id in aliases:
        alias = aliases[skill_id]
        return alias["target"], alias.get("modes"), f"legacy_alias:{skill_id}"
    raise ValueError(f"Unknown registered or alias Skill ID: {skill_id}")


def dependency_first_order(selected: list[str], known: dict[str, dict], stage: str) -> list[str]:
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
            if stage in known[dependency]["work_modes"]:
                visit(dependency)
        temporary.remove(skill_id)
        permanent.add(skill_id)
        ordered.append(skill_id)

    for skill_id in selected:
        visit(skill_id)
    return ordered


def route(
    request: str,
    registry: dict,
    aliases: dict,
    forced_sequence: list[str] | None = None,
    forced_skills: list[str] | None = None,
) -> dict:
    sequence = forced_sequence or infer_sequence(request)
    known = {skill["id"]: skill for skill in registry["skills"]}
    matches = [
        Match(skill["id"], score_tokens(request, skill["triggers"]), skill["category"], skill["priority"])
        for skill in registry["skills"]
    ]
    matches = [match for match in matches if match.score > 0]
    matches.sort(key=lambda item: (-item.score, -item.priority, item.skill_id))

    discipline_matches = [match for match in matches if match.category == "disciplines"]
    selected_disciplines = discipline_matches[: 1 + registry["routing"]["max_support_disciplines"]]
    primary_id = selected_disciplines[0].skill_id if selected_disciplines else None

    manual_targets: list[tuple[str, list[str] | None, str]] = []
    for item in forced_skills or []:
        manual_targets.append(resolve_manual_skill(item, known, aliases))

    stages: list[dict] = []
    for stage_index, stage in enumerate(sequence):
        selected: list[str] = []
        reasons: dict[str, str] = {}
        forced_modes: dict[str, list[str]] = {}

        def add(skill_id: str, reason: str, modes: list[str] | None = None) -> None:
            if skill_id not in known:
                raise ValueError(f"Unknown Skill ID in routing contract: {skill_id}")
            if stage not in known[skill_id]["work_modes"]:
                return
            if skill_id not in selected:
                selected.append(skill_id)
                reasons[skill_id] = reason
            if modes:
                forced_modes.setdefault(skill_id, []).extend(modes)

        if stage_index == 0:
            for skill_id in registry["routing"]["entry_stack"]:
                add(skill_id, "entry_stack")

        foundation_matches = [
            match for match in matches
            if match.category == "foundation"
            and stage in known[match.skill_id]["work_modes"]
            and match.skill_id not in registry["routing"]["entry_stack"]
            and match.skill_id not in registry["routing"]["review_stack"]
        ]
        for match in foundation_matches[: registry["routing"]["max_foundation_skills_per_stage"]]:
            add(match.skill_id, f"foundation_trigger score={match.score}")

        for index, match in enumerate(selected_disciplines):
            reason = "primary_discipline" if index == 0 else "support_discipline"
            add(match.skill_id, f"{reason} score={match.score}")

        if stage == "REVIEW":
            for skill_id in registry["routing"]["review_stack"]:
                add(skill_id, "mandatory_review_stack")

        for target, modes, reason in manual_targets:
            add(target, reason, modes)

        ordered = dependency_first_order(selected, known, stage)
        items = []
        for skill_id in ordered:
            skill = known[skill_id]
            modes = select_modes(request, skill, stage, forced_modes.get(skill_id))
            items.append({
                "id": skill_id,
                "role": (
                    "primary_discipline" if skill_id == primary_id
                    else "support_discipline" if skill_id in {m.skill_id for m in selected_disciplines[1:]}
                    else "foundation"
                ),
                "modes": modes,
                "reason": reasons.get(skill_id, "dependency"),
                "path": skill["path"],
            })
        stages.append({"work_mode": stage, "skills": items})

    return {
        "request": request,
        "work_mode_sequence": sequence,
        "primary_discipline": primary_id,
        "stages": stages,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--registry", type=pathlib.Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--sequence", help="Comma-separated PLAN,BUILD,REVIEW override")
    parser.add_argument("--skill", action="append", default=[])
    args = parser.parse_args()

    forced_sequence = None
    if args.sequence:
        forced_sequence = [item.strip().upper() for item in args.sequence.split(",") if item.strip()]
        invalid = set(forced_sequence) - {"PLAN", "BUILD", "REVIEW"}
        if invalid:
            print(f"ERROR: invalid work modes: {sorted(invalid)}", file=sys.stderr)
            return 2
    try:
        registry, aliases = load_contract(args.registry)
        result = route(args.request, registry, aliases, forced_sequence, args.skill)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    stdout_encoding = (sys.stdout.encoding or "").lower().replace("-", "")
    ensure_ascii = not stdout_encoding.startswith("utf")
    print(json.dumps(result, ensure_ascii=ensure_ascii, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
