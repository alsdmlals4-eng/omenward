# [현행 검토] OMENWARD Phase C C0 Local HiGodot Closure — 2026-08-11

```yaml
decision_id: OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1
review_status: C0_LOCAL_HIGODOT_GATE_PASS
product_mutation: NONE
runtime_resume_authority: GRANTED_AFTER_CURRENT_MAIN_REVALIDATION
persistent_authoring_authority: HIGODOT_ONLY
```

## 1. Fresh authority at closure

```text
BASE_MAIN = 23d5b292f619022cdd8ab7a33fb1debc2d294861
BASE_CHANGE = docs: enforce post-change adversarial monitoring loop (#285)
OMENWARD_MAIN = 8301cbb0868890a43d05926a48a65e38e8b3ebc3
PR175 = OPEN_DRAFT
PR175_HEAD = bde85549560fca90f7aa25fc4842bc0a3afb92e7
PR177 = OPEN_DRAFT_REFERENCE_ONLY_DO_NOT_MERGE
PR177_HEAD = 7654beced2cc5580ecc60a3a1d01c5767712c8b9
```

The Google Sheet still described the local gate as `LOCAL_LIVE_SESSION_UNVERIFIED` and routed the diagnostic through shared `WS9500`. That is stale current-facing routing, not historical evidence to rewrite. This Decision supersedes that live routing while preserving the earlier C0 row/audit/history as historical evidence.

## 2. Why project isolation was required

Godot AI 3.1.4 stores its selected HTTP/WS ports in Godot `EditorSettings`. Normal Godot editors sharing the same Windows editor-settings profile therefore changed ports together. A port-number change alone was not sufficient project isolation.

The accepted OMENWARD route is:

```text
Godot executable = dedicated self-contained OMENWARD editor
self-contained marker = _sc_
project = C:/Users/user/Documents/GitHub/Ninza/omenward
Godot AI HTTP = 8002
Godot AI WS = 9502
Codex executable = shared installation
Codex config isolation = project-specific CODEX_HOME
OMENWARD CODEX_HOME = C:/Users/user/.codex-omenward
```

Codex itself is not duplicated. Only its project-local configuration home is isolated so other project MCP endpoints are not overwritten.

Observed global Codex Godot-AI config remained `8001/9501`; the OMENWARD copy was verified as `8002/9502`.

## 3. Exact local transport evidence

The isolated editor settings were observed with:

```text
godot_ai/http_port = 8002
godot_ai/ws_port = 9502
```

A live transport snapshot established:

```text
HTTP 8002 = LISTEN
WS 9502 = LISTEN
GODOT_AI_SERVER_VERSION = 3.1.4
GODOT_AI_WS_PORT = 9502
GODOT_AI_OWNER_TYPE = plugin
GODOT_AI_ATTACH_PROTOCOL_VERSION = 1
GODOT_AI_ACTIVE_LEASE_COUNT = 1
```

Earlier same-session evidence also showed the isolated OMENWARD Godot process directly ESTABLISHED to WS9502. A later diagnostic correctly found no WS session because the editor itself had exited while the dedicated server remained alive; that empty registry was therefore not classified as a handshake defect.

## 4. Exact registered session closure

After the isolated OMENWARD editor was relaunched against the existing dedicated 8002/9502 server, the project-local Codex invoked read-only `session_manage(op="list")` and received exactly one active session:

```text
SESSION_ID_EVIDENCE = omenward@7f90
SESSION_NAME = omenward
PROJECT_PATH = C:/Users/user/Documents/GitHub/Ninza/omenward/
GODOT_VERSION = 4.7.1-stable (official)
PLUGIN_VERSION = 3.1.4
SERVER_VERSION = 3.1.4
PROTOCOL_VERSION = 1
CURRENT_SCENE = res://scenes/main/main.tscn
PLAY_STATE = stopped
READINESS = ready
EDITOR_PID_EVIDENCE = 28564
SERVER_LAUNCH_MODE = uvx
IS_ACTIVE = true
CONNECTED_AT_UTC = 2026-08-11T07:34:22.761963+00:00
LAST_SEEN_UTC = 2026-08-11T07:34:23.668624+00:00
SESSION_COUNT = 1
```

The session ID and PID are ephemeral evidence only. They MUST NOT be guessed or reused as future execution authority. Every new execution block must fresh-resolve the current session registry and exact project path before mutation.

## 5. C0 classification

```text
C0_REPOSITORY_TOOLCHAIN_GATE = PASS
C0_LOCAL_ISOLATED_EDITOR_GATE = PASS
C0_LOCAL_DEDICATED_TRANSPORT_GATE = PASS
C0_LOCAL_SESSION_REGISTRY_GATE = PASS
C0_LOCAL_HIGODOT_GATE = PASS
C0_OVERALL = PASS
PR175_RUNTIME_RESUME = AUTHORIZED_AFTER_CURRENT_MAIN_REBASE_REVALIDATION
PR175_MERGE = STILL_FORBIDDEN_UNTIL_RUNTIME_ACCEPTANCE
ISSUE176_7_GAPS = STILL_OPEN
FINAL_PRODUCT_NUMERICS = NOT_SELECTED
```

This Decision changes execution routing only. It changes no gameplay semantics and grants no direct GitHub mutation authority for persistent Godot/GDScript/GUT product source.

## 6. Operational boundaries

```text
PERSISTENT_GODOT_AUTHORING = HIGODOT_ONLY
GUT = DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY
HERA = LIVE_QA_OBSERVABILITY_ONLY
HERA_TRACKED_SOURCE_DELTA = MUST_REMAIN_NONE
CODEX_INSTALLATION = SHARED
CODEX_PROJECT_CONFIG = ISOLATED_BY_CODEX_HOME
OMENWARD_GODOT_AI_HTTP = 8002
OMENWARD_GODOT_AI_WS = 9502
SHARED_9500_ROUTING = SUPERSEDED_FOR_OMENWARD_CURRENT_EXECUTION
SESSION_ID_REUSE_WITHOUT_FRESH_LIST = FORBIDDEN
```

One lifecycle follow-up remains visible: `godot_ai/keep_server_on_exit = true` was observed during the isolation work. It does not invalidate the exact current session proof, but the OMENWARD isolated editor should use `keep_server_on_exit = false` for clean future execution-block teardown unless a later approved operation explicitly requires persistence.

The auxiliary Codex `agentmemory` MCP failed startup in the observed terminal, but the `godot-ai` MCP initialized and executed `session_manage` successfully. The `agentmemory` warning is therefore non-blocking for this HiGodot C0 gate and is not treated as Godot-AI evidence.

## 7. Required continuation

```text
1. fresh-resolve OMENWARD main and PR175 head
2. rebase/update PR175 against current main
3. re-run exact-head validation; historical Green is not current evidence
4. Issue176 seven gaps: GUT RED first
5. HiGodot-only persistent implementation
6. GUT GREEN + existing regressions
7. Godot parse/import/headless
8. deterministic FV fixtures twice identical raw
9. Hera live QA with tracked-source delta NONE
10. exact-head CI + adversarial review
11. Base post-change adversarial monitoring loop
```

Base `23d5b292...` adds a post-change adversarial monitoring loop, so successful implementation is not complete until that post-change monitoring requirement is satisfied.
