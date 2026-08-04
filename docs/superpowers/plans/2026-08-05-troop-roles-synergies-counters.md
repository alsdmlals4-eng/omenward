# OMENWARD Troop Roles, Synergies, and Counters Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Canonize the approved 4/10 troop-role baseline, prove its documentation contract through RED→GREEN→REFACTOR, synchronize GitHub and Google Sheet authority, and merge without changing product data or runtime behavior.

**Architecture:** The approved design Spec remains the rationale source. A new current canon document owns the ten-unit baseline, pressure-counter matrix, behavior-based synergy grammar, Barracks weighting contract, roster-resize gate, Tier/roulette asset rules, and implementation boundaries. A dedicated Python documentation contract verifies the canon, adversarial review, central routing, lifecycle treatment of prototype unit data, and Sheet adoption markers; existing product `.tres` files remain untouched.

**Tech Stack:** Markdown authority documents, Python 3.12 `unittest`, GitHub Actions, Google Sheets bounded batch updates, GitHub PR exact-head verification.

## Global Constraints

- Decision ID: `OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1`.
- Planning counter after canonization: `4_OF_10`.
- Baseline roster: 10; roster count is not sacred; no preset minimum or maximum.
- Product code, Scene, Resource, `.tres` unit data, exact numerics, and art assets must not change.
- T1/T2 roulette tokens reuse actual in-game troop images; T3 roulette tokens remain forbidden.
- Every pressure needs at least two troop response paths plus building/tactical alternatives.
- Synergy is observable battlefield behavior, not a hidden collection bonus.
- GitHub mutations require the explicit non-default branch `gpt/omenward-troop-roles-spec-20260805`.
- TDD order is mandatory: RED → GREEN → REFACTOR.
- Google Sheet writes must use bounded ranges and bounded read-back before any sync claim.

---

### Task 1: Add the failing troop-canon documentation contract

**Files:**
- Create: `tests/python/test_troop_role_canon.py`
- Modify: `.github/workflows/validate-project-core-docs.yml`

**Interfaces:**
- Consumes: the reviewed Spec at `docs/superpowers/specs/2026-08-05-troop-roles-synergies-counters-design.md`.
- Produces: a failing contract that names the exact canon, review, central-router, lifecycle, and Sheet requirements later tasks must satisfy.

- [ ] **Step 1: Write the failing test**

Create `tests/python/test_troop_role_canon.py` with these constants and assertions:

```python
from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-05-troop-roles-synergies-counters-design.md"
CANON = ROOT / "docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md"

TROOPS = (
    "방패수호병", "대검병", "창병", "궁수", "마도사",
    "사제", "암살자", "기병", "비행병", "거인",
)
PRESSURES = ("MASS", "ARMORED", "FLYING", "INFILTRATION", "SIEGE")
CENTRAL_FILES = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "docs/PROJECT_CORE.md",
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/DOCUMENTATION_MAP.md",
    ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md",
    ROOT / "docs/DECISIONS_PENDING.md",
    ROOT / "docs/OMENWARD_ROADMAP.md",
)


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class TroopRoleCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (SPEC, CANON, REVIEW):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_roster_baseline_and_resize_gate_are_explicit(self) -> None:
        text = read(CANON)
        self.assertIn(DECISION_ID, text)
        self.assertIn("ROSTER_BASELINE: 10", text)
        self.assertIn("ROSTER_COUNT_IS_NOT_SACRED", text)
        self.assertIn("ROSTER_MIN_MAX: NOT_PRESET", text)
        self.assertIn("ADD_UNIT_ONLY_IF", text)
        self.assertIn("REMOVE_OR_REPLACE_IF", text)
        for troop in TROOPS:
            self.assertIn(troop, text)

    def test_five_pressures_have_multiple_troop_paths(self) -> None:
        text = read(CANON)
        for pressure in PRESSURES:
            self.assertIn(pressure, text)
        self.assertIn("압력별 최소 두 병종 대응 경로", text)
        self.assertIn("단일 하드키 병종 금지", text)

    def test_synergy_and_barracks_rules_preserve_flexible_composition(self) -> None:
        text = read(CANON)
        for marker in (
            "행동 기반 시너지",
            "단순 세트 보너스: FORBIDDEN",
            "전열 병영 가중 계열",
            "기동 병영 가중 계열",
            "공통 지원 계열",
            "반대 계열 영구 삭제: FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_tier_route_layer_and_asset_boundaries_are_explicit(self) -> None:
        text = read(CANON)
        for marker in (
            "T1 병종 토큰 = 실제 T1 인게임 이미지",
            "T2 병종 토큰 = 실제 T2 인게임 이미지",
            "T3 병종 토큰 = FORBIDDEN",
            "FREE_RECALL: FORBIDDEN",
            "FREE_CROSS_LANE_MOVE: FORBIDDEN",
            "EXACT_NUMERICS: PENDING_SIMULATION",
            "PRODUCT_CODE = UNCHANGED",
        ):
            self.assertIn(marker, text)

    def test_central_authority_routes_decision_four_of_ten(self) -> None:
        for path in CENTRAL_FILES:
            text = read(path)
            self.assertIn(DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("4_OF_10", text, str(path.relative_to(ROOT)))

    def test_legacy_prototype_unit_data_is_not_current_product_authority(self) -> None:
        text = read(ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md")
        self.assertIn("data/units/*.tres", text)
        self.assertIn("[증거]", text)
        self.assertIn("LEGACY_PROTOTYPE_UNIT_DATA", text)
        self.assertIn("IMPLEMENTATION_INPUT_FORBIDDEN", text)

    def test_adversarial_review_closes_known_risks_without_authorizing_product(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-420",
            "OMW-AUD-443",
            "ROLE_OVERLAP_RISK",
            "HARD_COUNTER_LOCK_RISK",
            "FORCED_COMPOSITION_RISK",
            "ROSTER_BLOAT_RISK",
            "PRODUCT_CODE = UNCHANGED",
            "IMPLEMENTATION_READINESS = BLOCKED_BY_TACTICAL_AND_NUMERIC_DECISIONS",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Register the test in the documentation workflow**

Add `tests/python/test_troop_role_canon.py` to pull-request and push path filters, the `py_compile` command, and the `unittest` command in `.github/workflows/validate-project-core-docs.yml`.

- [ ] **Step 3: Run RED and verify the expected failure**

Run through GitHub Actions on the PR head. Expected result: `Validate Project Core Documentation` fails because the canon/review files and 4/10 central routing do not yet exist; existing Base and legacy product checks should remain unaffected.

- [ ] **Step 4: Record the RED run in the plan and PR body**

Replace the plan status line for Task 1 with the exact run number and first expected assertion failure after the run completes.

- [ ] **Step 5: Commit**

```bash
git add tests/python/test_troop_role_canon.py .github/workflows/validate-project-core-docs.yml docs/superpowers/plans/2026-08-05-troop-roles-synergies-counters.md
git commit -m "test: define troop role canon contract"
```

### Task 2: Create the troop canon and adversarial review

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- Create: `docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md`

**Interfaces:**
- Consumes: approved Spec and the RED markers from Task 1.
- Produces: current design authority and risk closure used by central documents and Sheet rows.

- [ ] **Step 1: Write the minimal canon needed for GREEN**

The canon must contain:

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
ADD_UNIT_ONLY_IF
REMOVE_OR_REPLACE_IF
압력별 최소 두 병종 대응 경로
단일 하드키 병종 금지
행동 기반 시너지
단순 세트 보너스: FORBIDDEN
반대 계열 영구 삭제: FORBIDDEN
FREE_RECALL: FORBIDDEN
FREE_CROSS_LANE_MOVE: FORBIDDEN
EXACT_NUMERICS: PENDING_SIMULATION
PRODUCT_CODE = UNCHANGED
```

It must reproduce the approved ten-troop role table, five-pressure response matrix, five behavior-synergy examples, Barracks families, Tier/roulette contract, route/layer rules, roster-resize gate, information contract, and explicit non-authority over product data.

- [ ] **Step 2: Write the adversarial review**

Create audit entries `OMW-AUD-420` through `OMW-AUD-443`. Cover at least:

```text
ROLE_OVERLAP_RISK
HARD_COUNTER_LOCK_RISK
FORCED_COMPOSITION_RISK
ROSTER_BLOAT_RISK
ROSTER_SHRINK_ROLE_GAP
ASSASSIN_CAVALRY_FLIER_DUPLICATION
FLYING_COUNTER_SINGLE_POINT_FAILURE
ARMORED_DEBUFF_DOMINANCE
SIEGE_STOP_AND_STRUCTURE_DAMAGE_CONFLATION
SUPPORT_STALL_META
BARRACKS_WEIGHT_HIDDENNESS
T3_TOKEN_REGRESSION
FREE_CROSS_LANE_MOBILITY
LAYER_UI_MISMATCH
LEGACY_TRES_AUTHORITY_LEAK
EARLY_STAGE_FORCED_ANSWER
NUMERIC_PREMATURE_LOCK
```

Close the document with:

```text
CORE_FIT = STRONG
ROLE_READABILITY = COHERENT
COUNTER_COVERAGE = STRUCTURALLY_VIABLE_WITH_TACTICAL_DEPENDENCY
DOCUMENT_PR_MERGE_READINESS = PASS
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_TACTICAL_AND_NUMERIC_DECISIONS
```

- [ ] **Step 3: Run the focused test**

Run: `python -m unittest tests.python.test_troop_role_canon -v`

Expected: authority, roster, pressure, synergy, Tier, and review tests pass; central routing and lifecycle tests still fail until Task 3.

- [ ] **Step 4: Commit**

```bash
git add docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md
git commit -m "docs: define troop role and counter canon"
```

### Task 3: Route 4/10 authority and quarantine prototype unit data

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/PROJECT_CORE.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/OMENWARD_ROADMAP.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/HANDOFF_CURRENT.md`
- Modify: `docs/decisions/OMENWARD_DECISION_LEDGER.md`
- Modify: `docs/handoff/OMENWARD_GPT_TO_CODEX_HANDOFF.md`
- Modify: `docs/spreadsheet/OMENWARD_GDD_WORKBOOK.md`

**Interfaces:**
- Consumes: canon and adversarial review from Task 2.
- Produces: one current Decision ID, counter, next Gate, lifecycle interpretation, and Sheet contract across all entry points.

- [ ] **Step 1: Update central decision metadata**

Set all central documents to:

```yaml
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
next_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
```

Add the troop canon and review paths to authority maps. Preserve dynamic `current_main` resolution and legacy C1/C2/C3 evidence markers.

- [ ] **Step 2: Add the current troop summary**

Central summaries must state:

```text
방패수호병 / 대검병 / 창병 / 궁수 / 마도사 / 사제 / 암살자 / 기병 / 비행병 / 거인
ROSTER_COUNT_IS_NOT_SACRED
다섯 압력별 최소 두 병종 대응 경로
행동 기반 시너지
전열·기동 병영 가중과 공통 지원 계열
T3 병종 룰렛 토큰 금지
정확 수치=PENDING_SIMULATION
```

- [ ] **Step 3: Quarantine prototype data without editing it**

Add this lifecycle entry:

```text
[증거] data/units/*.tres
status = LEGACY_PROTOTYPE_UNIT_DATA
authority = historical runtime/bootstrap evidence only
IMPLEMENTATION_INPUT_FORBIDDEN until Decision 4/10 + Decision 5/10 + numeric simulation + Codex implementation plan
```

Do not change any `.tres`, GDScript, Scene, Resource, or product-data file.

- [ ] **Step 4: Run the documentation contract**

Run: `python -m unittest tests.python.test_troop_role_canon -v`

Expected: all troop-role tests pass locally except any explicit Sheet-adoption workflow that waits for Task 4.

- [ ] **Step 5: Run all existing documentation tests**

Run:

```bash
python tools/validate_project_core_docs.py
python tools/validate_ci_usage_contract.py
python -m unittest tests.python.test_project_core_docs tests.python.test_ci_usage_contract tests.python.test_building_branch_canon tests.python.test_troop_role_canon -v
```

Expected: PASS with no regression to building, Stage, lifecycle, or legacy evidence contracts.

- [ ] **Step 6: Commit**

```bash
git add README.md AGENTS.md docs/
git commit -m "docs: route troop role canon across authorities"
```

### Task 4: Synchronize Google Sheet and verify bounded read-back

**Files:**
- Modify externally: Google Sheet `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`

**Interfaces:**
- Consumes: exact PR head after Task 3 and audit IDs from Task 2.
- Produces: Sheet rows matching Decision ID, exact head, counter 4/10, review status, lifecycle boundary, and next Gate.

- [ ] **Step 1: Read next available bounded rows**

Inspect bounded ranges in:

```text
00_프로젝트_허브
01_작업순서
02_현재_확정결정
03_근거_라이브러리
04_누락_충돌_감사
05_GDD_요약
12_핵심루프
15_조작_게임규칙
40_핵심시스템_메인콘텐츠
50_메인콘텐츠
99_변경이력
```

- [ ] **Step 2: Write 4/10 authority rows**

Record:

```text
Decision ID = OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
counter = 4/10
roster baseline = 10 / count not sacred / no preset min-max
pressure coverage = MASS·ARMORED·FLYING·INFILTRATION·SIEGE, at least two troop paths each
synergy = observable battlefield behavior / no basic set bonus
lifecycle = data/units/*.tres historical prototype evidence, implementation input forbidden
review = OMW-AUD-420~443
next = tactical skills and mana 5/10
product/runtime/assets = unchanged/not run
```

Bind all new rows to the exact PR head SHA.

- [ ] **Step 3: Perform bounded read-back**

Read only the written ranges and verify exact Decision ID, exact head, `4_OF_10`, audit endpoints, lifecycle marker, and next Decision.

- [ ] **Step 4: Record Sheet evidence in PR body and authority docs**

Use `READBACK_PASS` only after Step 3 succeeds.

### Task 5: Refactor, verify, and merge the documentation PR

**Files:**
- Modify: plan status and PR body only as required by evidence.

**Interfaces:**
- Consumes: Green documentation tests and Sheet bounded read-back.
- Produces: an exact-head, preflight-clean, merged 4/10 documentation canon.

- [ ] **Step 1: Refactor without changing behavior**

Remove duplicated role descriptions, repeated exact markers that would invalidate mutation tests, stale `3_OF_10` current-state text, and ambiguous claims that prototype `.tres` values are current authority.

- [ ] **Step 2: Scan for placeholders and scope violations**

Verify:

```text
TODO/TBD placeholders = 0
product code paths = 0
Scene/Resource/data modifications = 0
current authority conflicts = 0
```

- [ ] **Step 3: Run fresh exact-head verification**

Require all applicable workflows Green and record run numbers:

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Omenward Core
Validate Base v9 Adoption
```

Also verify:

```text
behind main = 0
reviews = 0 or addressed
unresolved threads = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
Sheet bounded read-back = PASS
```

- [ ] **Step 4: Update PR #139 body and mark ready**

Include RED evidence, Green/Refactor run numbers, benchmark adoption/non-adoption, audit `420~443`, changed paths, product boundary, exact head, Sheet ranges, and next Gate.

- [ ] **Step 5: Squash merge with expected head SHA**

Merge only when the PR head still equals the verified exact head.

- [ ] **Step 6: Update Sheet to merged main SHA and read back**

Change only the current 4/10 status ranges from PR-head state to merged-main state. Perform a final bounded read-back and record `MAIN_CANONICAL / READBACK_PASS`.
