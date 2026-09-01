# OMENWARD Base v9.4.4 맞춤형 운영 어댑터 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to execute this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Base v9.4.4의 released reuse-first 운영 계약을 OMENWARD의 repository-only·single-front 제품 구조에 맞게 고정하고, 구형 route·Sheet 표현이 current authority로 재등장하지 않도록 검증한다.

**Architecture:** `skills/PROJECT_BASE_ADAPTER.json`을 유일한 기계 정본으로 유지하고, `PROJECT_SKILL_SNAPSHOT.json`과 legacy compatibility view는 **current validator program + Base v9.4.4 exact released content**으로 재생성한다. `AGENTS.md`는 얇은 router로 축소하고, 사람이 읽는 세부 adaptation은 `docs/BASE_SHARED_SKILL_INTEGRATION.md`가 소유한다.

**Tech Stack:** GitHub, Base v9.4.4 Python validation tools, Python `unittest`, Markdown/JSON, existing Godot repository structure.

**Spec:** `docs/superpowers/specs/2026-09-01-base-v944-tailored-operating-adapter-design.md`

## Global Constraints

- Base v9.4.4 release identity is `210ec78292fa12ed7563ba743b322dd36103ae4a` / `bb61e68dc3028421b60c11b87ba2abd297ee6f78` / `5adc196c0185951f50e49ab5e51586eff8d60886`.
- Base v9.5 current `main` is reference-only until it is released and separately adopted.
- Base current validator reference is allowed only for Git-canonical evidence handling; it does not import a v9.5 policy.
- Do not modify Godot code, scenes, resources, game data, approved asset binaries, save formats, or product decisions.
- Preserve Sheet/Notion evidence as historical compatibility material; do not delete, write, or reactivate it.
- Keep project-local routes authoritative for Omenward-specific gameplay and shared Base skill bodies outside the repository.
- Do not use direct `main` push, force push, ruleset bypass, rebase of unrelated work, or external paid tooling.

---

### Task 1: Lock the new contract in a failing test

**Files:**
- Create: `tests/test_base_v944_reuse_first_adoption.py`
- Modify: `tests/test_base_v9_adoption.py`
- Modify: `tests/test_base_v942_planning_first_adoption.py`
- Modify: `tests/test_base_v943_first_prompt_adoption.py`
- Modify: `tests/python/test_project_base_adapter_freshness.py`

**Interfaces:**
- Consumes: `skills/PROJECT_BASE_ADAPTER.json`
- Produces: regression assertions for v9.4.4 release identity, reuse gates, repository-only migration boundary, and generated-view integrity.

- [x] **Step 1: Write a failing v9.4.4 adoption test**

```python
release = data["base_release"]
self.assertEqual("9.4.4", release["version"])
self.assertEqual("210ec78292fa12ed7563ba743b322dd36103ae4a", release["release_commit"])
self.assertEqual("REUSE_FIRST_PREFLIGHT_REQUIRED", reuse["required_gates"][0])
self.assertEqual("RETIRED_FROM_ACTIVE_FLOW", data["gdd_sheet"]["sync_status"])
```

- [x] **Step 2: Run the focused test and confirm RED**

Run: `python -m unittest tests.test_base_v944_reuse_first_adoption -v`
Expected: failure because the current adapter still declares v9.4.3 and a current Sheet workspace.

- [x] **Step 3: Update old v9.4.x tests to assert retained behavior through v9.4.4**

Keep planning-first and first-prompt gates asserted, but replace exact v9.4.3 identity with the v9.4.4 release identity and the repository-only Sheet state. Do not remove tests merely because an old release was superseded.

- [x] **Step 4: Run the focused Python adapter test group**

Run: `python -m unittest tests.test_base_v9_adoption tests.test_base_v942_planning_first_adoption tests.test_base_v943_first_prompt_adoption tests.test_base_v944_reuse_first_adoption tests.python.test_project_base_adapter_freshness -v`
Expected: passing only after Task 2 regenerates the adapter views and updates the current adapter hash.

### Task 2: Update the canonical adapter and generated views

**Files:**
- Modify: `skills/PROJECT_BASE_ADAPTER.json`
- Modify/generated: `skills/PROJECT_SKILL_SNAPSHOT.json`
- Modify/generated: `skills/BASE_V9_ADAPTER.json`
- Modify/generated: `skills/PROJECT_BASE_SKILL_ADAPTER.json`
- Modify: `.github/workflows/validate-project-base-adapter.yml`

**Interfaces:**
- Consumes: Base v9.4.4 lock, release index, `build_project_operating_artifacts.py`, `check_project_operating_contract.py`.
- Produces: adapter release pin, reuse-first metadata, historical Sheet boundary, and exact generated views.

- [x] **Step 1: Add v9.4.4 and reuse-first fields to the canonical adapter**

Use the exact release triple from the spec. Migrate the adapter to schema v2 with explicit `project_id: omenward`; this is required to represent the existing repository-only Sheet boundary truthfully. Add the existing Base `PROJECT_WORK_REUSE_HANDOFF.json` source, `REUSE_FIRST_PREFLIGHT_REQUIRED`, `REUSE_LEARNING_HANDOFF_REQUIRED`, `actual_project_execution: NOT_RUN`, and a project-only learning default. Convert `gdd_sheet` to a retained historical compatibility record with no current read/write authority.

- [x] **Step 2: Regenerate views with a validator/content split**

Run:

```powershell
python <Base-current-validator>\tools\build_project_operating_artifacts.py `
  --project-root . `
  --base-repository <Base-v9.4.4-worktree> `
  --protected-base <existing-approved-protected-baseline> `
  --write
```

Expected: only the declared compatibility/generated views change alongside the canonical adapter; no game paths are touched. If the active PR already contains approved protected game changes, generate in a clean temporary worktree at that approval baseline and copy only the generator output back after byte-hash comparison.

- [x] **Step 3: Make CI use the same split safely**

CI checks out validator program `19355b7ef065a21d0f2b685c7d9be64a4a3970f8` and exact v9.4.4 release content `5adc196c0185951f50e49ab5e51586eff8d60886` separately. The adapter retains the existing approved protected baseline, so CI always uses the exact approval-manifest checker and fails closed if the detected protected path set differs. A future baseline migration requires separate review.

- [x] **Step 4: Check generated artifacts**

Run the same split generator with `--check`, then run `check_approved_project_operating_contract.py` against the exact released Base content and the existing approval manifest when the active PR contains protected paths.

### Task 3: Rebuild the human operating entrypoints

**Files:**
- Modify: `AGENTS.md`
- Modify: `docs/BASE_SHARED_SKILL_INTEGRATION.md`
- Modify: `skills/README.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/ACTIVE_CONTEXT.md`

**Interfaces:**
- Consumes: the canonical adapter, current decision/context owners, repository-only policy.
- Produces: one short start router, one detailed Base adaptation explanation, and current navigation entries.

- [x] **Step 1: Replace stale product copies in `AGENTS.md` with thin routing**

State the dual Base model (released adapter vs. current remote observation), current single-front owner lookup, repository-only canon, actual-consumer asset gate, evidence ceiling, GitHub safety, and required completion/readback. Refer to decision/GDD owners instead of embedding mutable topology or live status.

- [x] **Step 2: Refresh Base integration and skills entry text**

Document the v9.4.4 pin, current v9.5 candidate boundary, router preflight, reuse-first order, and historical Sheet/Notion state. Retain legacy adapter views as compatibility-only and correct obsolete three-line wording to single-front terminology.

- [x] **Step 3: Register the current adaptation owner and plan**

Add the design/plan and `docs/BASE_SHARED_SKILL_INTEGRATION.md` to the current documentation map and lifecycle registry. Add only the Base adapter status and unchanged product evidence ceiling to `ACTIVE_CONTEXT.md`.

- [x] **Step 4: Run documentation and contract validation**

Run: `python tools/validate_project_core_docs.py` and the focused adapter test group.
Expected: current routers agree on repository-only, one active march front, and v9.4.4 release identity.

### Task 4: Validate freshness, review, and synchronize

**Files:**
- Create: `docs/reviews/ADVERSARIAL_BASE_V944_TAILORED_OPERATING_ADAPTER_REVIEW_2026-09-01.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

**Interfaces:**
- Consumes: final diff, Base/project validators, GitHub PR checks.
- Produces: five-pass adversarial receipt, exact branch/PR evidence, and next human gate.

- [x] **Step 1: Run canonical freshness and full Python regression**

Run the project freshness validator, all Python tests with the existing exact Base recovery fixture, and `git diff --check`. Retain `NOT_RUN` if a check needs an unavailable physical/runtime environment.

- [x] **Step 2: Perform five adversarial passes until clean**

Check in order: authority/pin drift, generated-view integrity, legacy Sheet/Notion reactivation, stale 3-front terminology, and protected product/runtime scope. Record findings, fixes, and no-finding evidence in the review receipt.

- [ ] **Step 3: Commit, push, and inspect exact-head CI**

Fetch before push, commit only scoped files, normal-push the existing task branch, then inspect PR #257's new exact head and required checks. Do not merge without separate user instruction.

- [ ] **Step 4: Read back and report**

Confirm local and remote branch HEAD equality, report Base release/current-candidate separation, tests and CI evidence, unchanged human usability gate, rollback, and any Base promotion candidate.
