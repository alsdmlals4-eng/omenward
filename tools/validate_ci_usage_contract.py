from __future__ import annotations

import pathlib
import sys

WORKFLOW_NAMES = (
    "validate-project-core-docs.yml",
    "validate-omenward-core.yml",
    "validate-skill-system.yml",
)


def _read(root: pathlib.Path, name: str) -> tuple[str, list[str]]:
    path = root / ".github" / "workflows" / name
    if not path.exists():
        return "", [f"missing workflow: {path.relative_to(root)}"]
    return path.read_text(encoding="utf-8"), []


def _require(text: str, needle: str, message: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(message)


def _reject(text: str, needle: str, message: str, errors: list[str]) -> None:
    if needle in text:
        errors.append(message)


def validate(root: pathlib.Path) -> list[str]:
    errors: list[str] = []
    contents: dict[str, str] = {}

    for name in WORKFLOW_NAMES:
        text, read_errors = _read(root, name)
        errors.extend(read_errors)
        contents[name] = text

    docs = contents["validate-project-core-docs.yml"]
    core = contents["validate-omenward-core.yml"]
    skill = contents["validate-skill-system.yml"]

    if docs:
        _require(docs, "runs-on: ubuntu-latest", "documentation workflow must use ubuntu-latest", errors)
        _require(docs, 'python-version: "3.12"', "documentation workflow must use Python 3.12", errors)
        _reject(docs, "matrix:", "documentation workflow must not use a matrix", errors)
        _reject(docs, "unittest discover", "documentation workflow must not run all Python tests", errors)
        _reject(docs, "validate_skill_system.py", "documentation workflow must not validate the Skill system", errors)
        _require(docs, "push:", "documentation workflow must validate main pushes", errors)

    if core:
        _require(core, "contracts_pr:", "core workflow must define contracts_pr", errors)
        _require(core, "contracts_full:", "core workflow must define contracts_full", errors)
        _require(core, "github.event_name == 'pull_request'", "core PR job condition is missing", errors)
        _require(core, "github.event_name != 'pull_request'", "core full-matrix condition is missing", errors)
        _require(core, "os: [ubuntu-latest, windows-latest]", "core full matrix must retain Ubuntu and Windows", errors)
        _require(core, 'python-version: ["3.12", "3.13"]', "core full matrix must retain Python 3.12 and 3.13", errors)
        _require(core, "push:", "core workflow must run full regression on main pushes", errors)
        _reject(core, '- "docs/**"', "core workflow must not trigger on docs/**", errors)
        _reject(core, '- "README.md"', "core workflow must not trigger on README.md", errors)
        _reject(core, "validate_project_core_docs.py", "core workflow must not duplicate project-core document validation", errors)
        _reject(core, "validate_skill_system.py", "core workflow must not duplicate Skill validation", errors)

    if skill:
        _require(skill, "runs-on: ubuntu-latest", "Skill workflow must use ubuntu-latest", errors)
        _require(skill, 'python-version: "3.12"', "Skill workflow must use Python 3.12", errors)
        _reject(skill, "matrix:", "Skill workflow must remain single-job without a matrix", errors)
        _require(skill, "push:", "Skill workflow must validate main pushes", errors)

    for name, text in contents.items():
        if not text:
            continue
        _require(text, "concurrency:", f"{name} must define concurrency", errors)
        _require(text, "cancel-in-progress: true", f"{name} must cancel stale runs", errors)

    return errors


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("CI usage contract validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
