# Omenward Skill System v4 Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the fixed 24-package routing model with a minimal active-skill architecture while preserving historical Skill IDs and eliminating active references to stale Base and schema contracts.

**Architecture:** Keep the existing package files as registered inactive history, route only active packages, and resolve old IDs through aliases. Consolidate project execution into seven foundation Skills, four Omenward-specific disciplines, and one canonical-freshness specialist. Validate structural invariants rather than exact package counts or a hard-coded Base commit.

**Tech Stack:** Python 3.12, JSON Registry, Markdown Skill packages, GitHub Actions.

## Global Constraints

- Omenward project canon remains authoritative over Base examples.
- Base source is pinned to `41a20584dd2ee51d917e5c9d7cab6838e1ceba7e`.
- No Skill is always-on.
- REVIEW adds validation and canonical-freshness Skills only at the review stage.
- One primary and at most one supporting Omenward discipline may be routed.
- Historical IDs must resolve to an active replacement and must never be selected as inactive packages.
- C1/C2/C3 automated evidence must not be reported as C4 human playtest evidence.

---

### Task 1: Registry v4 and compatibility map

**Files:**
- Modify: `docs/base/SKILL_REGISTRY.json`
- Modify: `docs/BASE_RULES_VERSION.md`

- [x] Pin the latest audited Base commit and synchronization date.
- [x] Add active/inactive status, stage modes, exclusions, replacement targets, and aliases.
- [x] Consolidate active disciplines into core design, Godot, core UX, and art/assets.
- [x] Preserve legacy package paths as inactive history.

### Task 2: Minimal deterministic routing

**Files:**
- Modify: `tools/route_skills.py`
- Test: `tests/python/test_skill_system_v4.py`

- [x] Ignore inactive packages.
- [x] Resolve legacy aliases before manual routing.
- [x] Remove always-on routing.
- [x] Add review stack only in REVIEW mode.
- [x] Limit supporting disciplines to one.
- [x] Prevent `pr` from matching inside `project`.

### Task 3: Dynamic integrity validation

**Files:**
- Modify: `tools/validate_skill_system.py`
- Test: `tests/python/test_skill_system_v4.py`

- [x] Remove exact package-count and exact Base-commit assertions.
- [x] Validate active review-stack targets and alias targets.
- [x] Validate active dependency closure and cycles.
- [x] Validate Registry/package missing and orphan paths.
- [x] Validate required sections only for active packages.

### Task 4: Omenward-specific execution Skills

**Files:**
- Create: `skills/disciplines/governing-omenward-core-design-and-data/SKILL.md`
- Create: `skills/disciplines/planning-and-validating-omenward-godot-implementation/SKILL.md`
- Create: `skills/disciplines/evaluating-omenward-core-ux-and-playtests/SKILL.md`
- Create: `skills/disciplines/governing-omenward-art-animation-and-assets/SKILL.md`

- [x] Define project-specific inputs, procedures, outputs, and failure criteria.
- [x] Keep rules/data, implementation, human UX evidence, and asset contracts separate.

### Task 5: CI and final verification

**Files:**
- Modify: `.github/workflows/validate-skill-system.yml`

- [x] Remove the v3 schema path from active workflow references.
- [x] Add v4 tests to the actual test discovery directory.
- [x] Add Omenward core routing smoke coverage.
- [ ] Confirm GitHub Actions passes on the pull request head.
- [ ] Review the final diff for stale active Skill IDs and stale Base commit references.
