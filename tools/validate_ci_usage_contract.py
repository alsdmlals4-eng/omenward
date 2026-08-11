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


def _require_count(text: str, needle: str, count: int, message: str, errors: list[str]) -> None:
    if text.count(needle) != count:
        errors.append(message)


def _section(text: str, start: str, end: str | None = None) -> str:
    start_index = text.find(start)
    if start_index < 0:
        return ""
    if end is None:
        return text[start_index:]
    end_index = text.find(end, start_index + len(start))
    if end_index < 0:
        return text[start_index:]
    return text[start_index:end_index]


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
        _require_count(docs, '- "!docs/base/**"', 2, "documentation workflow must exclude Skill base docs from PR and push triggers", errors)
        _require_count(docs, '- "!docs/BASE_RULES_VERSION.md"', 2, "documentation workflow must exclude the Skill base version document from PR and push triggers", errors)
        _reject(docs, '.github/workflows/validate-omenward-core.yml', "documentation workflow must not duplicate core workflow changes", errors)
        _reject(docs, '.github/workflows/validate-skill-system.yml', "documentation workflow must not duplicate Skill workflow changes", errors)

    if core:
        _require(core, "contracts_pr:", "core workflow must define contracts_pr", errors)
        _require(core, "contracts_full:", "core workflow must define contracts_full", errors)
        _require(core, "github.event_name == 'pull_request'", "core PR job condition is missing", errors)
        _require(core, "github.event_name != 'pull_request'", "core full-matrix condition is missing", errors)
        _require(core, "os: [ubuntu-latest, windows-latest]", "core full matrix must retain Ubuntu and Windows", errors)
        _require(core, 'python-version: ["3.11", "3.12", "3.13"]', "core full matrix must retain Python 3.11, 3.12, and 3.13", errors)
        _require(core, "workflow_dispatch:", "core workflow must support manual dispatch", errors)
        _reject(core, "self-hosted", "core full matrix must use standard GitHub-hosted runners", errors)
        _require(core, "push:", "core workflow must run full regression on main pushes", errors)
        _require_count(core, '- "addons/**"', 2, "core workflow must trigger for addons/** on PR and push", errors)
        _reject(core, '- "docs/**"', "core workflow must not trigger on docs/**", errors)
        _reject(core, '- "README.md"', "core workflow must not trigger on README.md", errors)
        _reject(core, "validate_project_core_docs.py", "core workflow must not duplicate project-core document validation", errors)
        _reject(core, "validate_skill_system.py", "core workflow must not duplicate Skill validation", errors)
        pr_section = _section(core, "  contracts_pr:", "  contracts_full:")
        full_section = _section(core, "  contracts_full:", "  godot:")
        pr_checkout = _section(pr_section, "    steps:\n", "      - name: Checkout exact Base recovery source")
        project_checkout = _section(full_section, "    steps:\n", "      - name: Checkout exact Base recovery source")
        _require(pr_section, "python -m unittest discover -s tests/python -v", "core PR job must run the full Python suite", errors)
        _require(pr_section, "::error title=Python repository test failure::", "core PR full suite must emit failing unittest annotations", errors)
        _require(pr_checkout, "fetch-depth: 0", "core PR job must fetch project history", errors)
        _require(
            pr_section,
            "python -m pip install --disable-pip-version-check numpy",
            "core PR job must install numpy for full-suite parity",
            errors,
        )
        for test_name in (
            "tests.python.test_c1_roulette_contract",
            "tests.python.test_c2_battle_objective_contract",
            "tests.python.test_c3_core_ux_contract",
            "tests.python.test_ci_usage_contract",
            "tests.python.test_base_recovery_map",
        ):
            _require(pr_section, test_name, f"core PR job must run {test_name}", errors)
        _require(pr_section, "python tools/validate_ci_usage_contract.py", "core PR job must validate the CI usage contract", errors)
        _require(full_section, "unittest discover", "core full matrix must retain the full Python suite", errors)
        _require(project_checkout, "fetch-depth: 0", "core full matrix must fetch project history", errors)
        _require(
            full_section,
            "python -m pip install --disable-pip-version-check numpy",
            "core full matrix must install numpy",
            errors,
        )

    if skill:
        _require(skill, "runs-on: ubuntu-latest", "Skill workflow must use ubuntu-latest", errors)
        _require(skill, 'python-version: "3.12"', "Skill workflow must use Python 3.12", errors)
        _reject(skill, "matrix:", "Skill workflow must remain single-job without a matrix", errors)
        _require(skill, "push:", "Skill workflow must validate main pushes", errors)
        _require(skill, "python tools/validate_ci_usage_contract.py", "Skill workflow must validate the CI usage contract", errors)
        _require(skill, "tests.python.test_ci_usage_contract", "Skill workflow must run CI usage mutation tests", errors)
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
