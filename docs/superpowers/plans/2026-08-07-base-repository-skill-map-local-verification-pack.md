# Base recovery map and existing Actions validation simplification

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Decision:** `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`

**Goal:** Maintain one simple public Actions validation path while proving the current Base recovery contract: every tracked Base path is classified, OMENWARD-relevant authority/Skill/consumer text is recovered, and the project adoption delta is explicit.

**Architecture:** `.github/workflows/validate-omenward-core.yml` remains the validation entrypoint. It checks out OMENWARD plus an exact public Base pin into `_base_recovery`. `tests/python/test_base_recovery_map.py` classifies live `git ls-files` from that Base checkout and verifies the current recovery map. No new local Windows/WSL launcher or receipt framework is introduced.

**Current baselines:**

```text
Base main = fa69a77a14f923a756064f6ae151d34cadb374f7
Base root tree = 913b69460649fe717294a27246e0b833958e70e4
OMENWARD starting main = c3efdba7c288f391f492fd5313d80ad5b824de3b
active integrated contract = v4.4
```

## Constraints

- Keep the same Decision ID.
- Keep unique PR scope in the existing eight process/docs/test/validator paths.
- Do not touch product scripts, data, scenes, resources, assets, addons, or `project.godot`.
- Do not automatically migrate OMENWARD from released Base v9.4.3 to current Base main.
- Clearing the Base recovery blocker does not clear the global Entry Gate.
- User Windows checkout, local Godot, audio vault, HiGodot exact pin, GUT formal adoption, and Hera adoption remain separately evidenced.

## Completed historical simplification

The prior PR159 work already:

- removed the dedicated local verification pack;
- reused standard public GitHub-hosted Actions;
- kept the full Ubuntu/Windows × Python 3.11/3.12/3.13 validation matrix;
- kept Godot 4.7.1 import, headless contracts, and runtime smoke;
- proved the older exact-head candidate Green while correctly leaving Base recovery incomplete at that time.

## Current completion package

### 1. Rebase recovery authority

- Pin recovery to current Base `fa69a77...` and root tree `913b6946...`.
- Pin the project comparison baseline to current OMENWARD main `c3efdba7...`.
- Replace v4.3 recovery authority with active v4.4 §4.1.

### 2. Prove whole tracked-file classification

- Add a second public `actions/checkout@v4` for `alsdmlals4-eng/Base` at the exact current Base pin.
- Enumerate `git ls-files` from `_base_recovery`.
- Classify every path into the bounded recovery taxonomy.
- Fail if any tracked path is unclassified or if the checkout HEAD differs from the exact Base pin.

### 3. Close project-relevant full-text recovery

Recover the current cold-start and OMENWARD operating path, including:

- Base START_HERE / AGENTS / Operating Model / Work Mode routing / Documentation Map;
- current Skill Registry and generated active view;
- GDD Google Sheets policy;
- Base shared adapter contract;
- project operating-system Skill and adapter routing reference;
- change-validation and adversarial-review Skills;
- HiGodot/GUT/Hera authority policy;
- adapter schema/template/workflow/validator consumer path.

No blind full-text load of unrelated Base files is required.

### 4. Record the OMENWARD adoption delta

- Confirm project `PROJECT_BASE_ADAPTER.json` remains a valid released v9.4.3 pin.
- Record current Base main as a post-release routing/policy delta.
- Do not auto-migrate the release pin.
- Separate current project adapter freshness defects into a follow-up gate.

### 5. Verify without self-referential evidence

The exact PR HEAD, run IDs, review status, merge SHA, and Sheet readback are intentionally stored in PR/Sheet evidence, not hard-coded into this plan. This avoids changing the document merely to record the SHA that contains the document.

The merge gate is:

```text
current main synchronized into PR branch
+ unique changed paths remain the allowed eight
+ exact-head public workflows Green
+ Base live classification zero unclassified
+ unresolved review threads 0
+ adversarial review has no unresolved P0/P1 within this scope
→ Ready / merge under repository policy
```

After merge, re-read main and Sheet. Remove only the Base recovery blocker from the global blocker list; all independent blockers remain fail-closed.
