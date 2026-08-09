[CmdletBinding()]
param(
    [string]$ProjectRoot = "C:\Users\user\Documents\GitHub\Ninza\omenward",
    [string]$BaseRoot = "C:\Users\user\Documents\GitHub\Base",
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

function Invoke-ExpectedNativeProbe([scriptblock]$Command) {
    # Windows PowerShell 5.1 can surface native stderr as NativeCommandError when
    # $ErrorActionPreference is Stop. Expected probes are allowed to return
    # nonzero, so temporarily make native stderr non-terminating and return only
    # the exit code to the caller.
    $savedPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        & $Command 1>$null 2>$null
        return $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $savedPreference
    }
}

function Get-ExactRequirement([string]$RequirementsPath, [string]$PackageName) {
    if (-not (Test-Path -LiteralPath $RequirementsPath -PathType Leaf)) {
        throw "Base requirements file is missing: $RequirementsPath"
    }
    $pattern = "^\s*$([regex]::Escape($PackageName))=="
    $line = Get-Content -LiteralPath $RequirementsPath | Where-Object { $_ -match $pattern } | Select-Object -First 1
    if ([string]::IsNullOrWhiteSpace($line)) {
        throw "Base does not declare an exact $PackageName requirement in $RequirementsPath"
    }
    return $line.Trim()
}

function Test-PythonRequirement([string]$Requirement) {
    $parts = $Requirement -split "==", 2
    if ($parts.Count -ne 2) {
        return $false
    }
    $packageName = $parts[0]
    $expectedVersion = $parts[1]

    # find_spec() avoids PackageNotFoundError traceback when the module is absent.
    # The metadata version check is evaluated only when the import is available.
    $probe = "import importlib.util as u, importlib.metadata as m, sys; sys.exit(0 if u.find_spec('$packageName') is not None and m.version('$packageName') == '$expectedVersion' else 1)"
    $exitCode = Invoke-ExpectedNativeProbe { & $script:PythonExecutable -c $probe }
    return ($exitCode -eq 0)
}

function Ensure-BaseValidatorDependency([string]$RequirementsPath) {
    $requirement = Get-ExactRequirement $RequirementsPath "jsonschema"
    if (Test-PythonRequirement $requirement) {
        Write-Host "Base validator dependency OK: $requirement" -ForegroundColor Green
        return
    }

    Write-Host "Recovering Base validator dependency from Base authority: $requirement" -ForegroundColor Yellow

    $pipProbe = Invoke-ExpectedNativeProbe { & $script:PythonExecutable -m pip --version }
    if ($pipProbe -ne 0) {
        Write-Host "pip is unavailable; attempting Python ensurepip recovery." -ForegroundColor Yellow
        & $script:PythonExecutable -m ensurepip --upgrade
        if ($LASTEXITCODE -ne 0) {
            throw "Could not bootstrap pip for Base validator dependency recovery."
        }
    }

    & $script:PythonExecutable -m pip install $requirement
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Environment install failed; retrying user-site install." -ForegroundColor Yellow
        & $script:PythonExecutable -m pip install --user $requirement
        if ($LASTEXITCODE -ne 0) {
            throw "Could not install Base-authoritative dependency $requirement"
        }
    }

    if (-not (Test-PythonRequirement $requirement)) {
        throw "Installed dependency is still not visible to the active Python: $requirement"
    }
    Write-Host "Recovered Base validator dependency: $requirement" -ForegroundColor Green
}

Assert-Command git
Assert-Command gh
Assert-Command codex
Assert-Command python

$pythonCommand = Get-Command python -CommandType Application -ErrorAction Stop | Select-Object -First 1
$script:PythonExecutable = $pythonCommand.Source
if ([string]::IsNullOrWhiteSpace($script:PythonExecutable) -or -not (Test-Path -LiteralPath $script:PythonExecutable -PathType Leaf)) {
    throw "Could not resolve the exact Python executable used for Base validation."
}
$pythonExecutable = $script:PythonExecutable
$pythonDirectory = Split-Path -Parent $script:PythonExecutable
if ([string]::IsNullOrWhiteSpace($pythonDirectory) -or -not (Test-Path -LiteralPath $pythonDirectory -PathType Container)) {
    throw "Could not resolve the Python installation directory used for Base validation."
}

if (-not (Test-Path -LiteralPath $ProjectRoot -PathType Container)) {
    throw "Project root does not exist: $ProjectRoot"
}
if (-not (Test-Path -LiteralPath $BaseRoot -PathType Container)) {
    throw "Base repository does not exist: $BaseRoot"
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

    $remoteBranchProbe = Invoke-ExpectedNativeProbe { & git show-ref --verify --quiet "refs/remotes/origin/$ExecutionBranch" }
    if ($remoteBranchProbe -ne 0) {
        throw "Remote execution branch is missing: origin/$ExecutionBranch"
    }

    $localBranchProbe = Invoke-ExpectedNativeProbe { & git show-ref --verify --quiet "refs/heads/$ExecutionBranch" }
    if ($localBranchProbe -eq 0) {
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
    $ancestorProbe = Invoke-ExpectedNativeProbe { & git merge-base --is-ancestor origin/main HEAD }
    if ($ancestorProbe -ne 0) {
        $mainSha = (& git rev-parse origin/main).Trim()
        $headSha = (& git rev-parse HEAD).Trim()
        throw "STALE_EXECUTION_BRANCH: origin/main=$mainSha is not an ancestor of HEAD=$headSha. Re-enter the OMENWARD Gate before authoring."
    }

    # Freshen the local Base authority without discarding or rewriting unrelated Base work.
    $baseInside = (& git -C $BaseRoot rev-parse --is-inside-work-tree 2>$null).Trim()
    if ($baseInside -ne "true") {
        throw "Base root is not a git worktree: $BaseRoot"
    }
    $baseDirty = @(& git -C $BaseRoot status --porcelain)
    if ($baseDirty.Count -gt 0) {
        Write-Host "Base worktree has local changes:" -ForegroundColor Yellow
        $baseDirty | ForEach-Object { Write-Host "  $_" }
        throw "Refusing to mutate a dirty Base worktree. Isolate Base changes before executor launch."
    }
    & git -C $BaseRoot fetch origin --prune
    if ($LASTEXITCODE -ne 0) {
        throw "Base git fetch origin failed."
    }
    $baseBranch = (& git -C $BaseRoot branch --show-current).Trim()
    if ($baseBranch -ne "main") {
        throw "Base must be on main for executor validation; current branch is '$baseBranch'."
    }
    $baseHead = (& git -C $BaseRoot rev-parse HEAD).Trim()
    $baseRemoteMain = (& git -C $BaseRoot rev-parse origin/main).Trim()
    if ($baseHead -ne $baseRemoteMain) {
        & git -C $BaseRoot pull --ff-only origin main
        if ($LASTEXITCODE -ne 0) {
            throw "Could not fast-forward local Base main to origin/main."
        }
    }

    # The Base operating-contract validator depends on the exact version declared
    # by Base itself. Recover only that declared dependency for the exact Python
    # executable that is also handed to child Codex for router-mandated revalidation.
    $baseRequirements = Join-Path $BaseRoot "requirements-publication.txt"
    Ensure-BaseValidatorDependency $baseRequirements

    $baseValidator = Join-Path $BaseRoot "tools\check_project_operating_contract.py"
    Write-Host "Running Base project operating-contract validation before Codex launch..." -ForegroundColor Cyan
    & $script:PythonExecutable $baseValidator --project-root $ProjectRoot --base-repository $BaseRoot --check
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: Base project operating-contract validation failed after dependency recovery."
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
    $mcpProbe = Invoke-ExpectedNativeProbe { & codex mcp get godot-ai --json }
    if ($mcpProbe -ne 0) {
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
    $baseSha = (& git -C $BaseRoot rev-parse HEAD).Trim()

    $prompt = @"
You are the local OMENWARD runtime executor operating from PowerShell/Codex with the live Godot AI MCP connection.

Execute GitHub Issue #$IssueNumber completely, using the issue body below as the authoritative executor packet.

Fresh local facts at launch:
- repository: $Repository
- project root: $ProjectRoot
- execution branch: $ExecutionBranch
- branch HEAD: $branchSha
- origin/main: $mainSha
- Base root: $BaseRoot
- Base HEAD: $baseSha
- Base validator Python: $pythonExecutable
- Base validator Python directory granted to Codex sandbox: $pythonDirectory
- Base project operating-contract validation: PASS in PowerShell preflight
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
9. The Base operating-contract validator already passed in the PowerShell preflight using the exact executable shown as `Base validator Python`. The generated project workflow router still requires validation before selecting a route. If the project workflow router requires revalidation, use this exact validated Python executable and command:
   & '$pythonExecutable' '$baseValidator' --project-root '$ProjectRoot' --base-repository '$BaseRoot' --check
   The executor grants only the validated Python installation directory to the Codex sandbox via `--add-dir`; keep `workspace-write` and do not broaden to full-access. Do not invoke this executor recursively to recover validator dependencies inside Codex. The parent preflight already verified the Base-declared jsonschema requirement for this exact executable. If this exact revalidation command fails, stop as BLOCKED_UNVERIFIED and report the failure rather than substituting another Python or changing PowerShell ExecutionPolicy.

GitHub Issue #$IssueNumber body follows:

$issueText
"@

    Write-Host "Launching Codex with Issue #$IssueNumber as the initial instruction..." -ForegroundColor Cyan
    Write-Host "PowerShell -> Base preflight -> Codex -> godot-ai MCP -> Godot Editor" -ForegroundColor Cyan

    if ($NonInteractive) {
        # Safe non-interactive mode: no approval bypass and workspace-write only.
        # Grant only the validated Python installation directory needed for router revalidation.
        $prompt | & codex --add-dir $pythonDirectory exec -C $ProjectRoot --sandbox workspace-write -c 'approval_policy="never"' -
    }
    else {
        # Interactive by default so the operator can review shell/git actions while
        # Godot authoring itself remains delegated to HiGodot MCP.
        & codex --add-dir $pythonDirectory -C $ProjectRoot --sandbox workspace-write --ask-for-approval on-request $prompt
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
