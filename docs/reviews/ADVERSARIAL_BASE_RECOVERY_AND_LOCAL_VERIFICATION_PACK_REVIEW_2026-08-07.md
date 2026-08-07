# Adversarial review — Base recovery map and Actions validation

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`

Review baseline:

```text
Base main = fa69a77a14f923a756064f6ae151d34cadb374f7
OMENWARD main before PR159 completion = c3efdba7c288f391f492fd5313d80ad5b824de3b
active contract = v4.4
```

## Attack → validated findings

### MUST_FIX — Recovery map pinned an obsolete Base/main baseline

The draft still described Base `4f98f968...`, OMENWARD pre-PR161 state, and v4.3 recovery authority. Current Base is `fa69a77...` and current OMENWARD main is `c3efdba7...`.

**Validated:** yes. The old pin would make any `COMPLETE` claim false even if its older unread list were closed.

**Refinement:** re-pin the recovery map and tests to current Base/root tree and v4.4; preserve old SHAs only as history.

### MUST_FIX — “Whole repository recovered” had no machine proof for every tracked path

A top-level/root/subtree map does not prove every tracked file was classified.

**Validated:** yes. Connector response clamping makes a large search/tree response insufficient as sole proof.

**Refinement:** public CI performs a second exact Base checkout, enumerates `git ls-files`, classifies every path into the bounded recovery taxonomy, and requires zero unclassified paths. Full-text reading remains selective and project-relevant.

### MUST_FIX — Generic partial-read blockers were too coarse to close

The prior map left entire `.github`, `docs`, `skills`, `templates`, `tests`, and `tools` trees as `PARTIAL_READ`, even though Base itself forbids blind full loading and requires impact-driven selection.

**Validated:** yes. This made completion structurally unreachable without violating Base cold-start guidance.

**Refinement:** replace subtree-wide partial placeholders with exact whole-tree classification plus named full-text authority/Skill/template/validator/consumer evidence for the OMENWARD route.

### MUST_FIX — Base release adoption and current Base main were conflated

OMENWARD pins the released v9.4.3 adapter line, while Base main has post-release routing/policy changes.

**Validated:** yes. `docs/BASE_RULES_VERSION.md` still identifies v9.4.3 as the latest released compatible line, while current Registry/routing can evolve independently.

**Refinement:** classify the project pin as `VALID_RELEASE_PIN`, record `PRESENT_POST_RELEASE` main delta, and forbid automatic migration.

### MUST_FIX — Adapter delta recovery exposed a separate project freshness defect

OMENWARD `skills/PROJECT_BASE_ADAPTER.json` still reports Sheet conflict/blocked and an old protected baseline although PR161 reconciled the current canon.

**Validated:** yes. This is not evidence that Base recovery itself is incomplete; it is a current project adapter freshness failure.

**Refinement:** record it as `REQUIRED_SEPARATE_FIX` and keep shared-route/project operating integrity fail-closed until repaired.

### REJECTED_CRITIQUE — Base recovery completion should open the product Entry Gate

This would conflate one process blocker with unrelated product/tool/runtime blockers.

**Rejected:** Base recovery completion only removes `BASE_RECOVERY_PR159_DRAFT_INCOMPLETE`. PR154, PR155, HiGodot, Hera, adapter freshness, local Godot/audio, and other v4.4 blockers remain independent.

### PRESERVED — Public Actions and Godot validation path

The prior simplification remains useful: no new local launcher/receipt framework is introduced. Existing public GitHub-hosted Actions remain the execution authority for this recovery contract, with Godot 4.7.1 coverage preserved.

## Regression boundaries

The completion change is process/docs/test/workflow only. It must not change:

- product scripts/data/scenes/resources/assets/addons/project.godot;
- current gameplay canon;
- GUT adoption state;
- HiGodot exact-pin state;
- Hera adoption state;
- local Windows/Godot/audio evidence.

The exact PR-head diff, Actions results, review threads, and merge evidence are recorded in PR/Sheet surfaces rather than embedded here.

## Verdict

```text
BASE_RECOVERY_DESIGN = ACCEPTABLE_IF_EXACT_HEAD_GREEN
BASE_RECOVERY_BLOCKER_TARGET = CLEAR
GLOBAL_ENTRY_GATE = BLOCK
PROJECT_BASE_ADAPTER_FRESHNESS = SEPARATE_MUST_FIX
PRODUCT_IMPLEMENTATION = FORBIDDEN
```

The earlier “Green Actions but recovery incomplete” conclusion is superseded only after the new exact-Base classification and current-authority tests pass. A Green recovery PR does not by itself authorize product work.
