"""Create and validate tracked Markdown mirrors for GitHub Issues.

The module deliberately has no third-party dependency so the same rules run on a
Windows checkout and in GitHub Actions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


DOCUMENT_PATH_PATTERN = re.compile(r"docs/[A-Za-z0-9_./-]+\.md")
FRONT_MATTER_PATTERN = re.compile(r"\A---\n(?P<metadata>.*?)\n---\n", re.DOTALL)
BODY_MARKER = "## Issue body\n"


def body_sha(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _names(values: Iterable[dict[str, Any]], key: str) -> list[str]:
    return [str(value[key]) for value in values if value.get(key)]


def _document_paths(body: str) -> list[str]:
    return sorted(set(DOCUMENT_PATH_PATTERN.findall(body)))


def _issue_number(issue: dict[str, Any]) -> int:
    value = issue.get("number", issue.get("issue_number"))
    if value is None:
        raise KeyError("Issue payload has neither 'number' nor 'issue_number'.")
    return int(value)


def _append_yaml_list(lines: list[str], key: str, values: Iterable[str]) -> None:
    normalized_values = list(values)
    if not normalized_values:
        lines.append(f"{key}: []")
        return
    lines.append(f"{key}:")
    lines.extend(f"- {value}" for value in normalized_values)


def render_issue_markdown(issue: dict[str, Any], canonical_documents: Iterable[str] | None = None) -> str:
    """Render one normalized, tracked issue snapshot."""
    issue_body = issue.get("body") or ""
    documents = list(canonical_documents) if canonical_documents is not None else _document_paths(issue_body)
    labels = _names(issue.get("labels") or [], "name")
    assignees = _names(issue.get("assignees") or [], "login")
    issue_number = _issue_number(issue)
    lines = [
        "---",
        f"issue_number: {issue_number}",
        f"title: {_quoted(str(issue['title']))}",
        f"state: {issue.get('state') or 'unknown'}",
        f"github_url: {_quoted(str(issue.get('html_url') or issue.get('display_url') or issue.get('url') or ''))}",
        f"github_updated_at: {_quoted(str(issue.get('updated_at') or ''))}",
        f"last_synced_body_sha: {body_sha(issue_body)}",
    ]
    _append_yaml_list(lines, "labels", labels)
    _append_yaml_list(lines, "assignees", assignees)
    _append_yaml_list(lines, "canonical_documents", documents)
    lines.extend(["---", "", f"# Issue #{issue_number}: {issue['title']}", "", BODY_MARKER.rstrip(), issue_body.rstrip(), ""])
    return "\n".join(lines)


def validate_issue_numbers(remote_numbers: set[int], snapshot_numbers: Iterable[int]) -> list[str]:
    """Return deterministic completeness errors for a local issue set."""
    errors: list[str] = []
    seen: set[int] = set()
    for number in sorted(snapshot_numbers):
        if number in seen:
            errors.append(f"duplicate issue number: {number}")
        seen.add(number)
    for number in sorted(remote_numbers - seen):
        errors.append(f"missing issue number: {number}")
    for number in sorted(seen - remote_numbers):
        errors.append(f"unexpected issue number: {number}")
    return errors


def has_bidirectional_conflict(local_content: str, last_synced_body_sha: str, remote_body: str) -> bool:
    """A conflict exists only when both sides differ from the last synchronized body."""
    return (
        body_sha(local_content) != last_synced_body_sha
        and body_sha(remote_body) != last_synced_body_sha
        and local_content != remote_body
    )


def parse_front_matter(markdown: str) -> dict[str, Any]:
    match = FRONT_MATTER_PATTERN.match(markdown)
    if not match:
        return {}
    metadata: dict[str, Any] = {}
    list_key: str | None = None
    for line in match.group("metadata").splitlines():
        if line.startswith("- ") and list_key is not None:
            metadata[list_key].append(line[2:].strip())
            continue
        if ":" in line and not line.startswith("-"):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if not value:
                metadata[key] = []
                list_key = key
            elif value == "[]":
                metadata[key] = []
                list_key = None
            elif value.startswith('"'):
                metadata[key] = json.loads(value)
                list_key = None
            else:
                metadata[key] = value
                list_key = None
    return metadata


def extract_issue_body(markdown: str) -> str:
    marker_index = markdown.find(BODY_MARKER)
    if marker_index < 0:
        return ""
    return markdown[marker_index + len(BODY_MARKER) :].rstrip("\n")


def mirror_filename(issue_number: int) -> str:
    return f"{issue_number:04d}.md"


def write_snapshot(issue: dict[str, Any], output_path: Path) -> None:
    if output_path.exists():
        existing = output_path.read_text(encoding="utf-8")
        metadata = parse_front_matter(existing)
        last_sha = metadata.get("last_synced_body_sha", "")
        if last_sha and has_bidirectional_conflict(extract_issue_body(existing), last_sha, issue.get("body") or ""):
            raise RuntimeError(f"bidirectional conflict for issue #{_issue_number(issue)}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_issue_markdown(issue), encoding="utf-8", newline="\n")


def write_all_snapshots(issues: Iterable[dict[str, Any]], snapshot_dir: Path) -> None:
    """Write one stable, number-keyed mirror for every supplied Issue."""
    for issue in sorted(issues, key=_issue_number):
        write_snapshot(issue, snapshot_dir / mirror_filename(_issue_number(issue)))


def _read_issues(path: Path) -> list[dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    return value["issues"] if isinstance(value, dict) and "issues" in value else value


def command_write(args: argparse.Namespace) -> int:
    issue = json.loads(Path(args.issue_json).read_text(encoding="utf-8"))
    write_snapshot(issue, Path(args.output))
    return 0


def command_validate(args: argparse.Namespace) -> int:
    remote_numbers = {_issue_number(issue) for issue in _read_issues(Path(args.issues_json))}
    snapshot_numbers = [int(path.stem) for path in Path(args.snapshot_dir).glob("[0-9][0-9][0-9][0-9].md")]
    errors = validate_issue_numbers(remote_numbers, snapshot_numbers)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    return 0


def command_write_all(args: argparse.Namespace) -> int:
    write_all_snapshots(_read_issues(Path(args.issues_json)), Path(args.snapshot_dir))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    write = commands.add_parser("write")
    write.add_argument("--issue-json", required=True)
    write.add_argument("--output", required=True)
    write.set_defaults(handler=command_write)
    validate = commands.add_parser("validate")
    validate.add_argument("--issues-json", required=True)
    validate.add_argument("--snapshot-dir", default="docs/issues")
    validate.set_defaults(handler=command_validate)
    write_all = commands.add_parser("write-all")
    write_all.add_argument("--issues-json", required=True)
    write_all.add_argument("--snapshot-dir", default="docs/issues")
    write_all.set_defaults(handler=command_write_all)
    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
