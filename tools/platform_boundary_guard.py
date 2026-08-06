from __future__ import annotations

import argparse
import dataclasses
import pathlib
import re
import sys
from collections.abc import Iterable, Sequence


@dataclasses.dataclass(frozen=True, slots=True)
class LegacyAllowance:
    path: str
    rule_id: str
    code: str
    reason: str

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.path, self.rule_id, _normalize_code(self.code))


@dataclasses.dataclass(frozen=True, slots=True)
class Finding:
    path: str
    line_number: int
    rule_id: str
    code: str

    def format(self) -> str:
        return f"{self.path}:{self.line_number}:{self.rule_id}: {self.code}"


@dataclasses.dataclass(frozen=True, slots=True)
class ScanReport:
    scanned_files: int
    allowed: list[Finding]
    unapproved: list[Finding]
    stale_allowances: list[LegacyAllowance]
    missing_paths: list[str]

    @property
    def ok(self) -> bool:
        return bool(self.scanned_files) and not self.unapproved and not self.stale_allowances


@dataclasses.dataclass(frozen=True, slots=True)
class _Rule:
    rule_id: str
    pattern: re.Pattern[str]


_RULES: tuple[_Rule, ...] = (
    _Rule("NODE_BASE_CLASS", re.compile(r"^\s*extends\s+Node(?:2D|3D)?\s*$")),
    _Rule("SCENE_TREE_TYPE", re.compile(r"\bSceneTree\b")),
    _Rule(
        "SCENE_TREE_LOOKUP",
        re.compile(r"\b(?:get_node|get_node_or_null|find_child|find_children)\s*\("),
    ),
    _Rule("INPUT_SINGLETON", re.compile(r"\bInput\s*\.")),
    _Rule("DISPLAY_SERVER", re.compile(r"\bDisplayServer\b")),
    _Rule("FILE_ACCESS", re.compile(r"\bFileAccess\b")),
    _Rule("OS_FEATURE_SWITCH", re.compile(r"\bOS\s*\.\s*has_feature\s*\(")),
    _Rule("STEAM_SDK", re.compile(r"\bSteam(?:works)?\b")),
    _Rule("GOOGLE_PLAY_SDK", re.compile(r"\b(?:GooglePlay|PlayGames)\b")),
)


DEFAULT_LEGACY_ALLOWLIST: tuple[LegacyAllowance, ...] = ()


def scan_forbidden_references(
    paths: Iterable[pathlib.Path],
    *,
    repository_root: pathlib.Path,
    allowlist: Sequence[LegacyAllowance] = DEFAULT_LEGACY_ALLOWLIST,
) -> ScanReport:
    root = repository_root.resolve()
    files, missing_paths = _collect_gd_files(paths)
    allowance_by_key = {allowance.key: allowance for allowance in allowlist}
    used_allowances: set[tuple[str, str, str]] = set()
    allowed: list[Finding] = []
    unapproved: list[Finding] = []

    for file_path in files:
        relative_path = _relative_path(file_path, root)
        text = file_path.read_text(encoding="utf-8")
        for line_number, detection_code, exact_code in _line_views(text):
            if not detection_code.strip():
                continue
            for rule in _RULES:
                if not rule.pattern.search(detection_code):
                    continue
                finding = Finding(
                    path=relative_path,
                    line_number=line_number,
                    rule_id=rule.rule_id,
                    code=exact_code.strip(),
                )
                key = (relative_path, rule.rule_id, _normalize_code(exact_code))
                if key in allowance_by_key:
                    allowed.append(finding)
                    used_allowances.add(key)
                else:
                    unapproved.append(finding)

    stale_allowances = [
        allowance
        for allowance in allowlist
        if allowance.key not in used_allowances
        and _allowance_is_in_scan_scope(allowance, files, root)
    ]
    allowed.sort(key=_finding_sort_key)
    unapproved.sort(key=_finding_sort_key)
    stale_allowances.sort(key=lambda item: item.key)
    return ScanReport(
        scanned_files=len(files),
        allowed=allowed,
        unapproved=unapproved,
        stale_allowances=stale_allowances,
        missing_paths=missing_paths,
    )


def _collect_gd_files(paths: Iterable[pathlib.Path]) -> tuple[list[pathlib.Path], list[str]]:
    files: set[pathlib.Path] = set()
    missing: list[str] = []
    for raw_path in paths:
        path = pathlib.Path(raw_path)
        if not path.exists():
            missing.append(path.as_posix())
            continue
        if path.is_file():
            if path.suffix == ".gd":
                files.add(path.resolve())
            continue
        files.update(candidate.resolve() for candidate in path.rglob("*.gd") if candidate.is_file())
    return sorted(files, key=lambda item: item.as_posix()), sorted(missing)


def _relative_path(path: pathlib.Path, root: pathlib.Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError as error:
        raise ValueError(f"scanned path is outside repository root: {path}") from error


def _allowance_is_in_scan_scope(
    allowance: LegacyAllowance,
    files: Sequence[pathlib.Path],
    root: pathlib.Path,
) -> bool:
    target = (root / allowance.path).resolve()
    return target in files


def _finding_sort_key(finding: Finding) -> tuple[str, int, str, str]:
    return (finding.path, finding.line_number, finding.rule_id, finding.code)


def _normalize_code(code: str) -> str:
    return " ".join(code.strip().split())


def _line_views(text: str) -> Iterable[tuple[int, str, str]]:
    in_quote: str | None = None
    triple = False
    escaped = False

    for line_number, line in enumerate(text.splitlines(), start=1):
        detection: list[str] = []
        exact: list[str] = []
        index = 0

        while index < len(line):
            char = line[index]
            next_three = line[index : index + 3]

            if in_quote is not None:
                exact.append(char)
                detection.append(" ")
                if triple:
                    if next_three == in_quote * 3:
                        exact.extend(line[index + 1 : index + 3])
                        detection.extend("  ")
                        index += 3
                        in_quote = None
                        triple = False
                        escaped = False
                        continue
                    index += 1
                    continue
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == in_quote:
                    in_quote = None
                index += 1
                continue

            if char == "#":
                break
            if char in ("'", '"'):
                if next_three == char * 3:
                    exact.extend(next_three)
                    detection.extend("   ")
                    index += 3
                    in_quote = char
                    triple = True
                    escaped = False
                    continue
                exact.append(char)
                detection.append(" ")
                in_quote = char
                triple = False
                escaped = False
                index += 1
                continue

            exact.append(char)
            detection.append(char)
            index += 1

        yield line_number, "".join(detection), "".join(exact).rstrip()


def _print_report(report: ScanReport) -> None:
    print(f"scanned_files={report.scanned_files}")
    print(f"allowed_legacy_findings={len(report.allowed)}")
    print(f"unapproved_findings={len(report.unapproved)}")
    print(f"stale_allowances={len(report.stale_allowances)}")
    if report.missing_paths:
        print("optional_missing_paths=" + ",".join(report.missing_paths))
    for finding in report.unapproved:
        print("UNAPPROVED " + finding.format())
    for allowance in report.stale_allowances:
        print(
            "STALE_ALLOWANCE "
            f"{allowance.path}:{allowance.rule_id}: {_normalize_code(allowance.code)}"
        )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Reject direct platform and SceneTree API use in OMENWARD domain/core GDScript.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=("scripts/core", "scripts/domain"),
        help="Files or directories to scan. Missing optional roots are reported but do not fail.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root used for stable relative paths.",
    )
    arguments = parser.parse_args(argv)
    root = pathlib.Path(arguments.root).resolve()
    report = scan_forbidden_references(
        [root / path for path in arguments.paths],
        repository_root=root,
    )
    _print_report(report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
