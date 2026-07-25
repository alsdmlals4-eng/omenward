#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "docs/archive/ARCHIVE_RETENTION_ADAPTER.json"
MANIFEST = ROOT / "docs/archive/MANIFEST.json"
ROUTES = ROOT / "skills/BASE_SHARED_SKILL_ROUTES.json"
PROJECT_ADAPTER = ROOT / "skills/PROJECT_BASE_SKILL_ADAPTER.json"
EXPECTED_BASE_COMMIT = "6a224e450f9420223c00921f3c56e051612f92ad"
CLASSIFICATIONS = {
    "CURRENT_AUTHORITY",
    "COMPATIBILITY_ONLY",
    "ARCHIVE_HISTORY",
    "EVIDENCE_RETENTION",
    "GENERATED_DERIVATIVE",
    "DELETE_PROHIBITED_SECRET",
    "DELETE_APPROVED",
    "KEEP_UNRESOLVED",
}
STATUSES = {"PASS", "PARTIAL", "FAIL", "NOT_RUN"}
SECRET_PATTERNS = (
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be object: {path.relative_to(ROOT)}")
    return value


def _safe_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def _body(text: str) -> str:
    text = text.lstrip("\ufeff")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            text = text[end + 5 :]
    return text.strip()


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        adapter = _load(root / ADAPTER.relative_to(ROOT))
        manifest = _load(root / MANIFEST.relative_to(ROOT))
        routes = _load(root / ROUTES.relative_to(ROOT))
        project_adapter = _load(root / PROJECT_ADAPTER.relative_to(ROOT))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [f"parse failure: {error}"]

    if adapter.get("schema_version") != 1 or adapter.get("adapter_role") != "legacy-retention-archive-project-adapter":
        errors.append("invalid archive adapter identity")
    if adapter.get("base", {}).get("commit") != EXPECTED_BASE_COMMIT:
        errors.append("archive adapter Base commit is not pinned to approved merge")
    if adapter.get("base", {}).get("skill_id") != "governing-legacy-retention-and-archives":
        errors.append("archive adapter shared Skill ID mismatch")
    if adapter.get("project", {}).get("repository") != "alsdmlals4-eng/omenward":
        errors.append("archive adapter project mismatch")

    policies = adapter.get("policies", {})
    expected_policies = {
        "preserve_original_content": True,
        "blank_placeholders_allowed": False,
        "secrets_may_be_archived": False,
        "default_active_authority": False,
        "default_implementation_authority": "NONE",
    }
    for key, expected in expected_policies.items():
        if policies.get(key) != expected:
            errors.append(f"unsafe archive policy: {key}")

    route_base = routes.get("base", {}).get("commit")
    project_base = project_adapter.get("base", {}).get("commit")
    if route_base != EXPECTED_BASE_COMMIT:
        errors.append("shared route Base commit mismatch")
    if project_base != EXPECTED_BASE_COMMIT:
        errors.append("project Base adapter commit mismatch")
    route = routes.get("routes", {}).get("legacy_retention_and_archives", {})
    if route.get("skill_id") != "governing-legacy-retention-and-archives":
        errors.append("legacy retention shared route missing")
    if (root / "skills/governing-legacy-retention-and-archives/SKILL.md").exists():
        errors.append("Base shared Skill body must not be copied into Omenward")

    paths = adapter.get("paths", {})
    single_paths = (
        "project_agents",
        "documentation_map",
        "active_context",
        "skill_registry",
        "archive_root",
        "archive_readme",
        "archive_manifest",
    )
    for key in single_paths:
        value = paths.get(key)
        if not isinstance(value, str) or not _safe_path(value):
            errors.append(f"unsafe or missing adapter path: {key}")
    for key in (
        "canonical_sources",
        "protected_paths",
        "legacy_search_roots",
        "generated_derivative_roots",
        "protected_evidence_roots",
    ):
        values = paths.get(key)
        if not isinstance(values, list) or any(not isinstance(item, str) or not _safe_path(item) for item in values):
            errors.append(f"unsafe or missing adapter path list: {key}")

    for key in ("project_agents", "documentation_map", "active_context", "skill_registry", "archive_root", "archive_readme", "archive_manifest"):
        value = paths.get(key)
        if isinstance(value, str) and not (root / value).exists():
            errors.append(f"required path missing: {value}")

    archive_root = root / paths.get("archive_root", "docs/archive")
    for source in paths.get("canonical_sources", []):
        try:
            (root / source).resolve().relative_to(archive_root.resolve())
        except ValueError:
            pass
        else:
            errors.append(f"canonical source is inside archive: {source}")

    if manifest.get("schema_version") != 1 or manifest.get("manifest_role") != "project-archive-retention-index":
        errors.append("invalid archive manifest identity")
    records = manifest.get("records")
    if not isinstance(records, list):
        errors.append("archive manifest records must be list")
        records = []

    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for record in records:
        if not isinstance(record, dict):
            errors.append("archive record must be object")
            continue
        archive_id = record.get("archive_id")
        current_path = record.get("current_path")
        if not isinstance(archive_id, str) or not archive_id:
            errors.append("archive record missing archive_id")
        elif archive_id in seen_ids:
            errors.append(f"duplicate archive_id: {archive_id}")
        else:
            seen_ids.add(archive_id)
        if not isinstance(current_path, str) or not _safe_path(current_path):
            errors.append(f"unsafe archive current_path: {current_path}")
            continue
        if current_path in seen_paths:
            errors.append(f"duplicate archive current_path: {current_path}")
        seen_paths.add(current_path)
        path = root / current_path
        if not path.is_file():
            errors.append(f"archive file missing: {current_path}")
        else:
            if path.suffix.lower() == ".md" and not _body(path.read_text(encoding="utf-8", errors="replace")):
                errors.append(f"archived Markdown body is empty: {current_path}")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if record.get("content_sha256") != digest:
                errors.append(f"archive hash mismatch: {current_path}")
        if record.get("classification") not in CLASSIFICATIONS:
            errors.append(f"invalid archive classification: {current_path}")
        if record.get("active_authority") is not False:
            errors.append(f"archive retains active authority: {current_path}")
        if record.get("implementation_authority") != "NONE":
            errors.append(f"archive retains implementation authority: {current_path}")
        if record.get("validation_status") not in STATUSES:
            errors.append(f"invalid archive validation status: {current_path}")
        if not record.get("rollback_ref"):
            errors.append(f"archive rollback_ref missing: {current_path}")
        for replacement in record.get("superseded_by", []):
            if isinstance(replacement, str) and replacement.startswith("external:"):
                continue
            if not isinstance(replacement, str) or not _safe_path(replacement) or not (root / replacement).exists():
                errors.append(f"archive replacement missing: {current_path} -> {replacement}")

    if archive_root.is_dir():
        for path in archive_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".json", ".txt", ".yml", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if any(pattern.search(text) for pattern in SECRET_PATTERNS):
                errors.append(f"secret-like material in archive: {path.relative_to(root)}")

    readme = root / paths.get("archive_readme", "docs/archive/README.md")
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        for token in ("현재 정본이 아니며 구현 권한이 없습니다", "원문을 비우지 않습니다", "비밀키"):
            if token not in text:
                errors.append(f"archive README missing contract token: {token}")

    return sorted(set(errors))


def main() -> int:
    errors = validate()
    if errors:
        print("Omenward archive governance validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Omenward archive governance validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
