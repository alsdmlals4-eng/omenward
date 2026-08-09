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

function Assert-CleanWorktree([string]$Root, [string]$Label) {
    $dirty = @(& git -C $Root status --porcelain)
    if ($dirty.Count -gt 0) {
        Write-Host "$Label worktree has local changes:" -ForegroundColor Yellow
        $dirty | ForEach-Object { Write-Host "  $_" }
        throw "Refusing to discard or mix existing $Label work. Preserve/isolate it intentionally before rerunning."
    }
}

function Refresh-OperatingContractLfFiles([string]$Root) {
    # .gitattributes pins these raw-byte-hashed operating-contract artifacts to LF.
    # Re-check them out from the clean index so an older CRLF Windows checkout does
    # not poison local RAW_FILE_BYTES_SHA256 validation or generated hashes.
    $pathspecs = @(
        "skills/PROJECT_BASE_ADAPTER.json",
        "skills/PROJECT_SKILL_SNAPSHOT.json",
        "skills/BASE_V9_ADAPTER.json",
        "skills/PROJECT_BASE_SKILL_ADAPTER.json",
        "docs/PROJECT_OPERATING_HEALTH.json",
        "docs/PROJECT_OPERATING_DASHBOARD.html",
        "docs/operations/PROJECT_BASE_ADAPTER_SHEET_SYNC_EVIDENCE_*.json",
        "docs/archive/base-v9-legacy-inputs/*.json",
        ".agents/skills/omenward-workflow-router/SKILL.md"
    )
    foreach ($pathspec in $pathspecs) {
        $files = @(& git -C $Root ls-files -- $pathspec)
        foreach ($file in $files) {
            & git -C $Root checkout -- $file
            if ($LASTEXITCODE -ne 0) {
                throw "Could not refresh LF checkout for operating-contract file: $file"
            }
        }
    }
}

function Get-AdapterProtectedDelta([string]$Root, [string]$OldBaseline, [string]$NewBaseline, [object[]]$ProtectedPaths) {
    $changed = @(& git -C $Root diff --name-only --no-renames $OldBaseline $NewBaseline --)
    if ($LASTEXITCODE -ne 0) {
        throw "Could not compare protected baseline delta: $OldBaseline -> $NewBaseline"
    }

    $violations = New-Object System.Collections.Generic.List[string]
    foreach ($rawPath in $changed) {
        $path = ($rawPath -replace "\\", "/")
        foreach ($rawPattern in $ProtectedPaths) {
            $pattern = ([string]$rawPattern -replace "\\", "/")
            $matches = $false
            if ($pattern.EndsWith("/")) {
                $matches = $path.StartsWith($pattern, [System.StringComparison]::OrdinalIgnoreCase)
            }
            else {
                $matches = [string]::Equals($path, $pattern, [System.StringComparison]::OrdinalIgnoreCase)
            }
            if ($matches) {
                $violations.Add($path)
                break
            }
        }
    }
    return @($violations | Sort-Object -Unique)
}

Assert-Command git
Assert-Command python
Assert-Command gh
Assert-Command codex

if (-not (Test-Path -LiteralPath $ProjectRoot -PathType Container)) {
    throw "Project root does not exist: $ProjectRoot"
}
if (-not (Test-Path -LiteralPath $BaseRoot -PathType Container)) {
    throw "Base root does not exist: $BaseRoot"
}

Push-Location $ProjectRoot
try {
    Assert-CleanWorktree $ProjectRoot "OMENWARD"

    & git fetch origin --prune
    if ($LASTEXITCODE -ne 0) { throw "git fetch origin failed." }

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
    if ($LASTEXITCODE -ne 0) { throw "Could not switch to $ExecutionBranch" }

    & git pull --ff-only origin $ExecutionBranch
    if ($LASTEXITCODE -ne 0) { throw "Could not fast-forward $ExecutionBranch from origin." }
    Assert-CleanWorktree $ProjectRoot "OMENWARD"

    # Fresh Base authority, without rewriting unrelated Base work.
    Assert-CleanWorktree $BaseRoot "Base"
    & git -C $BaseRoot fetch origin --prune
    if ($LASTEXITCODE -ne 0) { throw "Base git fetch origin failed." }
    $baseBranch = (& git -C $BaseRoot branch --show-current).Trim()
    if ($baseBranch -ne "main") {
        throw "Base must be on main for freshness reconciliation; current branch is '$baseBranch'."
    }
    & git -C $BaseRoot pull --ff-only origin main
    if ($LASTEXITCODE -ne 0) { throw "Could not fast-forward Base main." }
    Assert-CleanWorktree $BaseRoot "Base"

    Refresh-OperatingContractLfFiles $ProjectRoot
    Assert-CleanWorktree $ProjectRoot "OMENWARD after LF refresh"

    $mainSha = (& git rev-parse origin/main).Trim()
    $adapterPath = Join-Path $ProjectRoot "skills\PROJECT_BASE_ADAPTER.json"
    $adapter = Get-Content -LiteralPath $adapterPath -Raw | ConvertFrom-Json
    $oldBaseline = [string]$adapter.protected_baseline.commit
    if ([string]::IsNullOrWhiteSpace($oldBaseline)) {
        throw "PROJECT_BASE_ADAPTER protected baseline commit is missing."
    }

    if ($oldBaseline -ne $mainSha) {
        $ancestorProbe = Invoke-ExpectedNativeProbe { & git merge-base --is-ancestor $oldBaseline $mainSha }
        if ($ancestorProbe -ne 0) {
            throw "BLOCKED_UNVERIFIED: adapter baseline $oldBaseline is not an ancestor of current main $mainSha."
        }

        $protectedPaths = @($adapter.protected_paths)
        if ($protectedPaths.Count -eq 0) {
            throw "BLOCKED_UNVERIFIED: adapter protected_paths is empty."
        }
        $protectedDelta = @(Get-AdapterProtectedDelta $ProjectRoot $oldBaseline $mainSha $protectedPaths)
        if ($protectedDelta.Count -gt 0) {
            Write-Host "Protected-path changes exist between adapter baseline and current main:" -ForegroundColor Red
            $protectedDelta | ForEach-Object { Write-Host "  $_" -ForegroundColor Red }
            throw "BLOCKED_UNVERIFIED: protected baseline cannot auto-advance across protected-path changes."
        }

        Write-Host "Bounded adapter freshness recovery: $oldBaseline -> $mainSha (protected delta NONE)" -ForegroundColor Yellow

        $env:OMW_PROJECT_ROOT = $ProjectRoot
        $env:OMW_MAIN_SHA = $mainSha
        $patchPython = @'
import hashlib
import json
import os
import pathlib
import re

root = pathlib.Path(os.environ["OMW_PROJECT_ROOT"])
main_sha = os.environ["OMW_MAIN_SHA"]
adapter_path = root / "skills" / "PROJECT_BASE_ADAPTER.json"
adapter = json.loads(adapter_path.read_text(encoding="utf-8"))
adapter["protected_baseline"]["commit"] = main_sha
adapter_raw = (json.dumps(adapter, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
adapter_path.write_bytes(adapter_raw)
adapter_sha = hashlib.sha256(adapter_raw).hexdigest()

test_path = root / "tests" / "python" / "test_project_base_adapter_freshness.py"
text = test_path.read_text(encoding="utf-8")
text, baseline_count = re.subn(
    r'^CURRENT_PROTECTED_BASELINE = "[0-9a-f]{40}"$',
    f'CURRENT_PROTECTED_BASELINE = "{main_sha}"',
    text,
    flags=re.MULTILINE,
)
text, sha_count = re.subn(
    r'^CURRENT_ADAPTER_SHA = "[0-9a-f]{64}"$',
    f'CURRENT_ADAPTER_SHA = "{adapter_sha}"',
    text,
    flags=re.MULTILINE,
)
if baseline_count != 1 or sha_count != 1:
    raise SystemExit(
        f"freshness-test constant patch mismatch: baseline={baseline_count} adapter_sha={sha_count}"
    )
with test_path.open("w", encoding="utf-8", newline="\n") as handle:
    handle.write(text)
print(f"adapter_sha256={adapter_sha}")
'@
        $patchPython | & python -
        if ($LASTEXITCODE -ne 0) {
            throw "Could not advance adapter baseline and freshness-test expectation."
        }
    }
    else {
        Write-Host "PROJECT_BASE_ADAPTER protected baseline already matches current main: $mainSha" -ForegroundColor Green
    }

    $builder = Join-Path $BaseRoot "tools\build_project_operating_artifacts.py"
    $validator = Join-Path $BaseRoot "tools\check_project_operating_contract.py"

    Write-Host "Regenerating Base project-operating artifacts from canonical adapter..." -ForegroundColor Cyan
    & python $builder --project-root $ProjectRoot --base-repository $BaseRoot --protected-base $mainSha --write
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: Base official artifact generator --write failed."
    }

    Write-Host "Checking generated artifacts..." -ForegroundColor Cyan
    & python $builder --project-root $ProjectRoot --base-repository $BaseRoot --protected-base $mainSha --check
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: Base official artifact generator --check failed."
    }

    Write-Host "Validating project operating contract..." -ForegroundColor Cyan
    & python $validator --project-root $ProjectRoot --base-repository $BaseRoot --protected-base $mainSha --check
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: Base project operating-contract validation still fails after bounded recovery."
    }

    Write-Host "Running focused adapter freshness regression..." -ForegroundColor Cyan
    & python -m unittest tests.python.test_project_base_adapter_freshness -v
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: project adapter freshness regression failed."
    }

    $allowed = @(
        "skills/PROJECT_BASE_ADAPTER.json",
        "skills/PROJECT_SKILL_SNAPSHOT.json",
        "skills/BASE_V9_ADAPTER.json",
        "skills/PROJECT_BASE_SKILL_ADAPTER.json",
        "docs/PROJECT_OPERATING_DASHBOARD.html",
        ".agents/skills/omenward-workflow-router/SKILL.md",
        "tests/python/test_project_base_adapter_freshness.py"
    )
    $allowedSet = @{}
    foreach ($item in $allowed) { $allowedSet[$item.ToLowerInvariant()] = $true }

    $status = @(& git status --porcelain)
    $unexpected = New-Object System.Collections.Generic.List[string]
    foreach ($line in $status) {
        if ($line.Length -lt 4) { continue }
        $path = $line.Substring(3).Trim() -replace "\\", "/"
        if ($path -match " -> ") { $path = ($path -split " -> ")[-1] }
        if (-not $allowedSet.ContainsKey($path.ToLowerInvariant())) {
            $unexpected.Add($path)
        }
    }
    if ($unexpected.Count -gt 0) {
        Write-Host "Unexpected files changed during adapter recovery:" -ForegroundColor Red
        $unexpected | Sort-Object -Unique | ForEach-Object { Write-Host "  $_" -ForegroundColor Red }
        throw "BLOCKED_UNVERIFIED: adapter recovery escaped its operational whitelist."
    }

    if ($status.Count -gt 0) {
        Write-Host "Committing bounded adapter freshness maintenance before runtime authoring..." -ForegroundColor Cyan
        & git add -- $allowed
        if ($LASTEXITCODE -ne 0) { throw "git add for adapter freshness maintenance failed." }
        & git diff --cached --check
        if ($LASTEXITCODE -ne 0) { throw "git diff --cached --check failed." }
        & git commit -m "chore: reconcile Base adapter runtime preflight freshness"
        if ($LASTEXITCODE -ne 0) { throw "Could not commit adapter freshness maintenance." }
        & git push origin "HEAD:$ExecutionBranch"
        if ($LASTEXITCODE -ne 0) { throw "Could not push adapter freshness maintenance to $ExecutionBranch." }
    }

    Assert-CleanWorktree $ProjectRoot "OMENWARD after adapter reconciliation"

    $reconciledHead = (& git rev-parse HEAD).Trim()
    Write-Host "Adapter preflight reconciliation PASS at $reconciledHead" -ForegroundColor Green
    Write-Host "Proceeding to the existing Issue #$IssueNumber runtime executor." -ForegroundColor Cyan

    $executor = Join-Path $ProjectRoot "tools\invoke_barracks_role_output_executor.ps1"
    if (-not (Test-Path -LiteralPath $executor -PathType Leaf)) {
        throw "Runtime executor is missing: $executor"
    }

    if ($NonInteractive) {
        & $executor -ProjectRoot $ProjectRoot -BaseRoot $BaseRoot -Repository $Repository -IssueNumber $IssueNumber -ExecutionBranch $ExecutionBranch -NonInteractive
    }
    else {
        & $executor -ProjectRoot $ProjectRoot -BaseRoot $BaseRoot -Repository $Repository -IssueNumber $IssueNumber -ExecutionBranch $ExecutionBranch
    }
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
