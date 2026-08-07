# Base whole-repository and Skill recovery map

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`

Current recovery baseline:

```text
Base exact commit = fa69a77a14f923a756064f6ae151d34cadb374f7
Base root tree = 913b69460649fe717294a27246e0b833958e70e4
OMENWARD baseline = c3efdba7c288f391f492fd5313d80ad5b824de3b
RECOVERY_STATUS = COMPLETE
BASE_RECOVERY_BLOCKER_CLEARED = TRUE
GLOBAL_ENTRY_GATE = BLOCK
```

`BASE_RECOVERY_BLOCKER_CLEARED=TRUE` clears only the Base recovery item. It does not authorize product implementation or clear PR154, PR155, HiGodot, Hera, local Godot/audio, adapter-freshness, or other v4.4 blockers.

## Recovery contract

The active integrated contract v4.4 §4.1 and current Base cold-start rules require two distinct recovery layers:

1. every tracked Base path is inventoried and assigned a bounded role classification;
2. only project-relevant text authorities, Skill bodies, references, templates, validators, and consumers are full-text read.

Blindly loading every Base text body is not the contract. Base `START_HERE.md`, `AGENTS.md`, `docs/OPERATING_MODEL.md`, `docs/WORK_MODE_AND_SKILL_ROUTING.md`, and `docs/DOCUMENTATION_MAP.md` require Registry- and impact-map-driven progressive loading.

## Current whole-repository inventory

The exact Base root tree has 29 root paths. Current subtrees were recovered at the same commit, including `.github`, `docs`, `schemas`, `skills`, `templates`, `tests`, and `tools`.

The exact public Base checkout used by CI is pinned to `fa69a77a14f923a756064f6ae151d34cadb374f7`. The recovery contract enumerates `git ls-files` from that checkout and assigns every tracked path one of:

```text
SKILL / ROUTER / WORKFLOW / TEMPLATE / POLICY / TEST / SCRIPT /
REGISTRY / ARCHIVE / GENERATED / BINARY
```

The acceptance condition is `ZERO_UNCLASSIFIED`. The machine-readable record is `docs/operations/BASE_WHOLE_REPOSITORY_AND_SKILL_MAP.v1.json`; `tests/python/test_base_recovery_map.py` performs the live exact-pin classification in public CI.

## Current Skill and workflow recovery

Current routing authority is `skills/SKILL_REGISTRY.json`, not a frozen release snapshot. The generated current view reports 29 active Skills.

Relevant current behaviors recovered from the Base main pin include:

- L1+ work compares latest main, current decisions, same-goal PRs, actual implementation, and configured project Sheets before mutation.
- repository-wide review inventories everything but full-loads only relevant authorities and consumers.
- project adapter execution is fail-closed on stale/mismatched pins, Registry drift, protected-path drift, generated-view drift, or copied shared Skill bodies.
- HiGodot remains the sole persistent Godot authoring authority; adopted GUT is deterministic GDScript test authority; Hera is restricted to `LIVE_QA_AND_OBSERVABILITY_ONLY` with persistent source mutation forbidden.
- installed addons without a real consumption path are `INSTALLED_UNUSED`.
- current Base also contains post-v9.4.3 policy/routing additions such as the Visual Requirement Gate; their presence does not automatically rewrite a project release pin.

The current Base workflow inventory remains nine workflow files and is recorded exactly in the JSON map.

## Project-relevant full-text surfaces

At exact Base main `fa69a77...`, full text was recovered for the cold-start and current OMENWARD operating path, including:

- `START_HERE.md`
- `AGENTS.md`
- `docs/OPERATING_MODEL.md`
- `docs/WORK_MODE_AND_SKILL_ROUTING.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/BASE_RULES_VERSION.md`
- `docs/PROJECT_GDD_GOOGLE_SHEETS_POLICY.md`
- `docs/BASE_SHARED_SKILL_ADAPTER_CONTRACT.md`
- `skills/SKILL_REGISTRY.json`
- `docs/generated/BASE_ACTIVE_SKILLS.md`
- `skills/managing-game-project-operating-system/SKILL.md`
- `skills/managing-game-project-operating-system/references/project-adapter-and-routing-contract.md`
- `skills/reviewing-and-validating-project-changes/SKILL.md`
- `skills/running-adversarial-review-and-refinement/SKILL.md`
- `docs/knowledge/godot/HIGODOT_SINGLE_AUTHORITY_AND_SAFE_OPERATION.md`

The corresponding adapter schema/template/workflow/validator routes were also identified:

- `schemas/project-base-adapter-v1.schema.json`
- `templates/project-operations/PROJECT_BASE_ADAPTER.json`
- `templates/project-operations/github/validate-project-base-adapter.yml`
- `tools/project_operating_contract.py`

This is sufficient to close the former generic `.github/**`, `docs/**`, `skills/**`, `templates/**`, `tests/**`, and `tools/**` partial-read placeholders: they are replaced by exact whole-tree classification plus bounded project-relevant full-text evidence.

## OMENWARD Base adoption delta

OMENWARD's canonical `skills/PROJECT_BASE_ADAPTER.json` is a released Base **v9.4.3 pin**:

```text
release commit = 7dd1a4f80388bc5faca767ff74a3eb32dc9d0ac8
evidence commit = da33a350d61b8adc52df97fccc7001708a933370
release Registry SHA-256 = 693a0dff3f054ecdd653079909e044211473838e73dd9aff07734d1ce5694c59
```

Base `docs/BASE_RULES_VERSION.md` still identifies v9.4.3 as the latest released compatible line. Therefore the project release pin is not invalid merely because current Base `main` has moved forward.

Current Base main has a newer routing view (`docs/generated/BASE_ACTIVE_SKILLS.md` Registry SHA-256 `ba36a0ae...`) and additional post-release policies. The correct disposition is:

```text
PROJECT_RELEASE_PIN = VALID_RELEASE_PIN
CURRENT_BASE_MAIN_DELTA = PRESENT_POST_RELEASE
AUTOMATIC_MIGRATION = FORBIDDEN
```

The delta is recovered and recorded; migration is a separate project-adoption decision.

## Separate adapter freshness finding

Recovery also exposed current OMENWARD adapter fields that are stale relative to PR161/current main:

- `gdd_sheet.declared_sync_status` still says `SHEET_GITHUB_CONFLICT` and `sync_status=BLOCKED` even though PR161 reconciled current canon and Sheet.
- `protected_baseline.commit` remains a historical baseline and must be reconciled under the adapter's protected-path contract before shared-route execution.

These are **project adapter freshness findings**, not evidence that Base recovery is incomplete. They remain fail-closed and must be repaired in a separate bounded adapter change before claiming project operating integrity.

## Existing Actions validation path

No separate Windows/WSL2 local launcher or receipt system is reintroduced. `.github/workflows/validate-omenward-core.yml` remains the validation entrypoint and now performs a second public checkout of exact Base `fa69a77...` into `_base_recovery` for live tracked-file classification.

The existing validation coverage remains:

- PR fast contracts on standard Ubuntu hosted runner;
- full manual/main matrix on Ubuntu and Windows with Python 3.11, 3.12, and 3.13;
- Godot 4.7.1 import, all headless contract tests, and runtime smoke.

Exact PR-head run IDs and merge evidence belong in PR metadata and the Google Sheet rather than this self-referential document.

## Final Base-recovery verdict

```text
WHOLE_TRACKED_FILE_INVENTORY_CLASSIFICATION = CLOSED_BY_EXACT_BASE_CHECKOUT_AND_ZERO_UNCLASSIFIED_TEST
PROJECT_RELEVANT_AUTHORITY_SKILL_CONSUMER_RECOVERY = CLOSED
OMENWARD_BASE_ADOPTION_DELTA = RECORDED
UNREAD_OR_PARTIALLY_READ_SURFACES = 0
BASE_RECOVERY_BLOCKER_CLEARED = TRUE
GLOBAL_ENTRY_GATE = BLOCK
```

Remaining work proceeds as separate gates, starting with the project adapter freshness finding and the already-recorded PR154/PR155/HiGodot/Hera/local blockers. Product implementation remains forbidden until the global Entry Gate is independently re-evaluated to PASS.
