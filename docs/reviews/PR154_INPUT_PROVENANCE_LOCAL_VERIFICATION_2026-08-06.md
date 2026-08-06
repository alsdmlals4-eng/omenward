# PR #154 Input Provenance Local Alternate Verification

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SIMULATION-INPUT-PROVENANCE-AND-ROULETTE-AXIS-CORRECTION-V1
scope: BOUNDED_RECONSTRUCTED_CONTRACT_VERIFICATION
```

## Evidence

```text
RED_COMMIT = c7da0569a8c3b1179789a1fa769335a2008a9145
RED_RESULT = FileNotFoundError / APPROVED_PROVENANCE_AUTHORITY_MISSING
GREEN_HEAD_BEFORE_MAIN_SYNC = a5528e72e5c5a7d5205d61dbc13c82084316062d
COMMAND = python -m unittest tests.python.test_barracks_simulation_input_provenance_manifest -v
RESULT = 9_PASS / 0_FAILURE / 0_ERROR
COMMAND = python -m py_compile tests/python/test_barracks_simulation_input_provenance_manifest.py
RESULT = EXIT_0
JSON_PARSE = PASS
MANIFEST_CANONICAL_SHA256 = 706ec6da767d1102af7c8b2b39a711b981fa9692f8a949b2e473c90dabb5a33b
```

## Boundary

```text
FULL_PRIVATE_REPOSITORY_CHECKOUT = NOT_PERFORMED
FULL_PYTHON_SUITE = NOT_RUN
GITHUB_ACTIONS_GREEN = UNAVAILABLE_BILLING_PRE_START
GODOT_TESTS = NOT_RUN
SIMULATION = BLOCKED_MISSING_INPUTS
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

The local verification reconstructed the files consumed by the focused provenance contract. It does not prove full repository or gameplay correctness.
