# Base whole-repository and Skill recovery map

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`
Base exact commit: `4f98f968a377f7b6a11aafa4fc94d11bddbebedc`
Base root tree: `4bc8d45d4bb88649eb5041f16478b862801b3901`
OMENWARD starting main: `93c388ad1c50581671f8ea059357c863d8d8e0f7`
Current status: `INCOMPLETE / ENTRY_GATE_BLOCK`

## Recovery contract correction

The active integrated contract v4.3 §4.1 requires two different things and they must not be collapsed into one rule:

1. Build the whole tracked-file inventory and classify every tracked file as `Skill`, `Router`, `Workflow`, `Template`, `Policy`, `Test`, `Script`, `Registry`, `Archive`, `Generated`, or `Binary`.
2. Read the full text of project-relevant text files and inspect binary metadata, provenance, and consumers when relevant.

It does **not** require blind full-text loading of every Base file. Base's own `START_HERE.md`, `docs/OPERATING_MODEL.md`, `docs/WORK_MODE_AND_SKILL_ROUTING.md`, and `docs/DOCUMENTATION_MAP.md` independently require selective, Registry- and impact-map-driven loading.

The previous map statement that every unread or partially read top-level subtree was automatically blocked until every file was fully read was therefore over-conservative. This revision keeps the gate fail-closed while correcting the blocker to the actual v4.3 requirement.

## Confirmed inventory

The Base root tree contains 29 tracked root paths. The current Base Skill Registry exposes 29 active Skill entrypoints. The GitHub workflow inventory contains nine workflow files.

Exact recursive indexes have been recovered for the known top-level subtrees used by this audit. Connector response clamping still prevents treating one large recursive response as a complete whole-repository file manifest, so the all-file classification requirement remains open.

## Completed recovery surfaces

### Base root authorities

Full text was read at exact Base commit `4f98f968...` for the current root authority and release/toolchain surfaces needed by the cold start:

- `START_HERE.md`
- `AGENTS.md`
- `README.md`
- `SECURITY.md`
- `LICENSE`
- `.gitattributes`
- `.gitignore`
- `.codex-plugin/plugin.json`
- `base.lock.json`
- `base-v9.1.lock.json`
- `base-v9.2.lock.json`
- `base-v9.3.lock.json`
- `base-v9.4.lock.json`
- `base-v9.4.1.lock.json`
- `base-v9.4.2.lock.json`
- `base-v9.4.3.lock.json`
- `package.json`
- `pnpm-workspace.yaml`
- `requirements-publication.txt`

`pnpm-lock.yaml` was inspected as a generated dependency lock but is not a current Base authority whose entire dependency payload must be loaded to satisfy the project-relevant full-text rule.

### Proposal lifecycle surface

`[수정제안서]/**` exact tree `b40748b461c1df90c9404b307d7cf582f0cf7781` was indexed and all 13 blobs were read.

Lifecycle recovery:

- BCP-2026-001 and BCP-2026-002: `SUBMITTED`; not current execution authority.
- BCP-2026-003 through BCP-2026-007: implementation history is recorded, while each proposal's runtime, human, platform, deployment, or production-readiness limits remain preserved.

Proposal or design presence is not promoted into OMENWARD project implementation evidence.

### Skill routing authority

`skills/SKILL_REGISTRY.json` blob `5ca054e70725f396f286c3b4a315e2a922e1cad5` was recovered as the current 29-Skill routing authority.

Key routing contract:

- `load_all_skills=false`
- automatic trigger matching
- user Skill declaration not required
- maximum one primary discipline Skill
- maximum three foundation Skills
- `HOLD`, `BACKUP`, and `REMOVAL_CANDIDATE` excluded from active routing

### Base cold-start authorities

Full text was read for:

- `docs/OPERATING_MODEL.md`
- `docs/WORK_MODE_AND_SKILL_ROUTING.md`
- `docs/DOCUMENTATION_MAP.md`

All three confirm that repository-wide review starts from an inventory and impact map, then loads the minimum relevant current authorities, consumers, tests, templates, and references. They do not authorize claiming a whole-repository audit from search snippets or a top-level list.

### OMENWARD-relevant Base policies

Full text was also recovered for:

- `docs/PROJECT_GDD_GOOGLE_SHEETS_POLICY.md`
- `docs/knowledge/godot/HIGODOT_SINGLE_AUTHORITY_AND_SAFE_OPERATION.md`

Confirmed boundaries:

- Project Google Sheets is a `USER_FACING_GDD_WORKSPACE`; it does not replace GitHub detailed canon or actual implementation evidence.
- HiGodot (`hi-godot/godot-ai`) is the sole Godot authoring/mutation authority when adopted, but project-specific exact version, Godot version, host registration, runtime/regression evidence, and rollback must be recorded before readiness claims.
- A different-role test or platform addon is not automatically forbidden, but requires its own evaluation, version, license, consumer, validation, and removal path.

## TDD evidence for this correction

Test-first contract commit:

`55c0280777895b1534e70057dac09e4adf87bf94`

Public Core run `31179030259` reproduced RED exactly at the Base recovery map contract:

- C1 validator: PASS
- C2 validator: PASS
- C3 validator: PASS
- CI usage validator: PASS
- existing fast contract tests: PASS
- new recovery-scope tests: FAIL because `recovery_contract` and `completed_recovery_surfaces` did not yet exist

This establishes that the correction changes the recovery-map contract rather than hiding an unrelated product or runtime failure.

## Remaining blocking recovery surfaces

The following remain fail-closed:

1. **Whole tracked-file manifest and classification** — every tracked Base file still needs one inventory/classification record even when its body is not project-relevant.
2. **`.github/**` relevant content** — current workflow and policy bodies that govern the project recovery/validation path require bounded review.
3. **`docs/**` relevant authorities** — beyond the recovered cold-start, GDD Sheet, and HiGodot authorities, current OMENWARD-relevant policy consumers still need recovery.
4. **`skills/**` relevant bodies and references** — recovery, validation, adversarial review, Godot/addon evaluation, continuity, and synchronization Skills must be read and their input/output/failure/next-step paths traced.
5. **`templates/**` relevant adoption and evidence templates** — only templates reached by the current OMENWARD path need full-text recovery, but the entire tree still needs inventory/classification.
6. **`tests/**` and `tools/**` relevant validators/consumers** — project-relevant route integrity and fail-closed consumers need bounded recovery.
7. **OMENWARD adoption delta** — the project's Base Adapter/Snapshot/Router must be compared against exact Base `4f98f968...` and current project decisions.

Accordingly:

```text
RECOVERY_STATUS = INCOMPLETE
BASE_RECOVERY_BLOCKER_CLEARED = FALSE
ENTRY_GATE = BLOCK
PR159 = DRAFT / DO_NOT_MERGE
```

This map cannot authorize product implementation, Godot authoring, GUT activation, audio import, Ready transition, or merge.

## Simplified validation path

The separate Windows/WSL2 launcher and JSON-receipt pack remains removed. Validation reuses `.github/workflows/validate-omenward-core.yml` through `workflow_dispatch`.

The Full validation job uses only standard GitHub-hosted labels:

- operating systems: `ubuntu-latest`, `windows-latest`
- Python: `3.11`, `3.12`, `3.13`
- Godot: `4.7.1` headless import, contract tests, and runtime smoke

The later Decision `OMW-DEC-20260807-PROCESS-PUBLIC-REPOSITORY-STANDARD-HOSTED-ACTIONS-V1` superseded only the original visibility-preservation clause. OMENWARD is public and standard hosted runner execution is proven, but that does not clear the Base recovery gate.

## Next required gate

```text
COMPLETE_TRACKED_FILE_INVENTORY_CLASSIFICATION
+ PROJECT_RELEVANT_AUTHORITY_SKILL_CONSUMER_RECOVERY
+ OMENWARD_BASE_ADOPTION_DELTA
→ exact-head validation
→ only then reassess BASE_RECOVERY_BLOCKER_CLEARED
```
