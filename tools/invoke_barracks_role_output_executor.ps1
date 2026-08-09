[CmdletBinding()]
param(
    [string]$ProjectRoot = "C:\Users\user\Documents\GitHub\Ninza\omenward",
    [string]$Repository = "alsdmlals4-eng/omenward",
    [int]$IssueNumber = 174,
    [string]$ExecutionBranch = "runtime/barracks-role-output-implementation-20260809",
    [switch]$NonInteractive
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Assert-Command([string]$Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

function Invoke-Native([scriptblock]$Command, [string]$FailureMessage) {
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "$FailureMessage (exit=$LASTEXITCODE)"
    }
}

Assert-Command git
Assert-Command gh
Assert-Command codex

if (-not (Test-Path -LiteralPath $ProjectRoot -PathType Container)) {
    throw "Project root does not exist: $ProjectRoot"
}

Push-Location $ProjectRoot
try {
    $inside = (& git rev-parse --is-inside-work-tree 2>$null).Trim()
    if ($inside -ne "true") {
        throw "Not a git worktree: $ProjectRoot"
    }

    $origin = (& git remote get-url origin).Trim()
    if ($origin -notmatch "alsdmlals4-eng[/:]omenward(?:\.git)?$") {
        throw "Unexpected origin remote: $origin"
    }

    & git fetch origin --prune
    if ($LASTEXITCODE -ne 0) {
        throw "git fetch origin failed."
    }

    $dirty = @(& git status --porcelain)
    if ($dirty.Count -gt 0) {
        Write-Host "Working tree has unrelated/local changes:" -ForegroundColor Yellow
        $dirty | ForEach-Object { Write-Host "  $_" }
        throw "Refusing to discard or mix existing local work. Isolate/stash it intentionally, then run again."
    }

    & git show-ref --verify --quiet "refs/remotes/origin/$ExecutionBranch"
    if ($LASTEXITCODE -ne 0) {
        throw "Remote execution branch is missing: origin/$ExecutionBranch"
    }

    & git show-ref --verify --quiet "refs/heads/$ExecutionBranch"
    if ($LASTEXITCODE -eq 0) {
        & git switch $ExecutionBranch
    }
    else {
        & git switch --track -c $ExecutionBranch "origin/$ExecutionBranch"
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Could not switch to $ExecutionBranch"
    }

    & git pull --ff-only origin $ExecutionBranch
    if ($LASTEXITCODE -ne 0) {
        throw "Could not fast-forward $ExecutionBranch from origin."
    }

    # The executor must be based on fresh main. If main moved beyond this branch,
    # stop instead of silently authoring against stale project state.
    & git merge-base --is-ancestor origin/main HEAD
    if ($LASTEXITCODE -ne 0) {
        $mainSha = (& git rev-parse origin/main).Trim()
        $headSha = (& git rev-parse HEAD).Trim()
        throw "STALE_EXECUTION_BRANCH: origin/main=$mainSha is not an ancestor of HEAD=$headSha. Re-enter the OMENWARD Gate before authoring."
    }

    $projectGodot = Join-Path $ProjectRoot "project.godot"
    $projectText = Get-Content -LiteralPath $projectGodot -Raw
    foreach ($plugin in @(
        "res://addons/godot_ai/plugin.cfg",
        "res://addons/gut/plugin.cfg",
        "res://addons/hera_agent_godot/plugin.cfg"
    )) {
        if ($projectText -notmatch [regex]::Escape($plugin)) {
            throw "Required enabled plugin entry not found in project.godot: $plugin"
        }
    }

    # Godot AI exposes MCP on the local HTTP server. The editor/plugin should
    # already be running before this PowerShell entrypoint is used.
    $mcpReachable = Test-NetConnection 127.0.0.1 -Port 8000 -InformationLevel Quiet -WarningAction SilentlyContinue
    if (-not $mcpReachable) {
        throw "Godot AI MCP port 8000 is not reachable. Open OMENWARD in Godot, confirm the Godot AI dock is connected, then run this script again."
    }

    & codex login status | Out-Host
    if ($LASTEXITCODE -ne 0) {
        throw "Codex is not authenticated. Run 'codex login' first."
    }

    # Preserve a working dock-generated configuration. Only add the documented
    # streamable-HTTP fallback when the godot-ai entry does not exist at all.
    & codex mcp get godot-ai --json *> $null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Codex MCP entry 'godot-ai' is missing; adding local HTTP fallback." -ForegroundColor Yellow
        & codex mcp add godot-ai --url "http://127.0.0.1:8000/mcp"
        if ($LASTEXITCODE -ne 0) {
            throw "Could not configure Codex MCP server 'godot-ai'."
        }
    }

    $issueBody = (& gh issue view $IssueNumber --repo $Repository --json body --jq .body)
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace(($issueBody -join "`n"))) {
        throw "Could not read GitHub Issue #$IssueNumber."
    }
    $issueText = $issueBody -join "`n"

    $branchSha = (& git rev-parse HEAD).Trim()
    $mainSha = (& git rev-parse origin/main).Trim()

    $prompt = @"
You are the local OMENWARD runtime executor operating from PowerShell/Codex with the live Godot AI MCP connection.

Execute GitHub Issue #$IssueNumber completely, using the issue body below as the authoritative executor packet.

Fresh local facts at launch:
- repository: $Repository
- project root: $ProjectRoot
- execution branch: $ExecutionBranch
- branch HEAD: $branchSha
- origin/main: $mainSha
- Godot AI MCP localhost:8000 is reachable

Hard boundaries:
1. Persistent Godot/product authoring MUST go through the godot-ai MCP / HiGodot tools. Do not use shell redirection, generic text editors, apply_patch, or direct filesystem writes for scripts/, data/, scenes/, project.godot, addons/, or GDScript GUT test authoring.
2. Use shell commands only for repository inspection/status, approved test execution, evidence capture, and git operations that do not bypass HiGodot authoring.
3. Establish GUT RED first with >0 discovered tests and preserve the intended failing evidence before battle-runtime authoring.
4. Then perform the minimal HiGodot implementation, Godot import/parse, GUT GREEN (>0 tests), existing regressions, deterministic FV evidence, and Hera live QA with tracked-source delta NONE.
5. Hera is QA/observability only and must not persistently mutate source.
6. Never serialize BLOCKED_RUNTIME_OUTPUT as numeric zero. Do not choose a final weighted functional-value index, final parameter vector, or final product numerics.
7. Do not merge locally. If completion evidence is valid, push only the execution branch and report the exact HEAD/evidence. If a prerequisite conflicts with fresh project state, stop with BLOCKED_UNVERIFIED instead of inventing a workaround.
8. Do not discard unrelated work and do not re-add docs/analysis/barracks_simulation/*.csv.import or *.translation sidecars.

GitHub Issue #$IssueNumber body follows:

$issueText
"@

    Write-Host "Launching Codex with Issue #$IssueNumber as the initial instruction..." -ForegroundColor Cyan
    Write-Host "PowerShell -> Codex -> godot-ai MCP -> Godot Editor" -ForegroundColor Cyan

    if ($NonInteractive) {
        # Safe non-interactive mode: no approval bypass and workspace-write only.
        # A command requiring broader privilege will fail rather than silently escalate.
        $prompt | & codex exec -C $ProjectRoot --sandbox workspace-write --ask-for-approval never -
    }
    else {
        # Interactive by default so the operator can review shell/git actions while
        # Godot authoring itself remains delegated to HiGodot MCP.
        & codex -C $ProjectRoot --sandbox workspace-write --ask-for-approval on-request $prompt
    }

    $codexExit = $LASTEXITCODE
    Write-Host "Codex exited with code $codexExit" -ForegroundColor Cyan
    Write-Host "Current branch/status:" -ForegroundColor Cyan
    & git branch --show-current
    & git status --short
    exit $codexExit
}
finally {
    Pop-Location
}
