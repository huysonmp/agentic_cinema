[CmdletBinding()]
param(
    [switch]$AllowShallow,
    [switch]$AllowGitlinkChanges
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$expectedPaths = @(
    'ext/a2a',
    'ext/adk-python',
    'ext/adk-samples',
    'ext/agent-starter-pack',
    'ext/generative-ai',
    'ext/mcp-toolbox',
    'ext/modelcontextprotocol',
    'ext/python-genai'
)
$failures = [System.Collections.Generic.List[string]]::new()

function Invoke-GitCapture {
    param(
        [Parameter(Mandatory)][string]$WorkingDirectory,
        [Parameter(Mandatory)][string[]]$Arguments
    )

    $result = & git -C $WorkingDirectory @Arguments 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "git -C $WorkingDirectory $($Arguments -join ' ') failed: $result"
    }
    return ($result | Out-String).Trim()
}

$configuredPaths = @(
    & git -C $repositoryRoot config --file .gitmodules --get-regexp '^submodule\..*\.path$' 2>$null |
        ForEach-Object { ($_ -split '\s+', 2)[1].Replace('\', '/') } |
        Sort-Object
)

if ($LASTEXITCODE -ne 0) {
    throw 'Unable to read .gitmodules.'
}

$pathDifference = Compare-Object $expectedPaths $configuredPaths
if ($pathDifference) {
    $failures.Add(".gitmodules does not contain exactly the expected paths: $($pathDifference | Out-String)")
}

foreach ($relativePath in $expectedPaths) {
    $absolutePath = Join-Path $repositoryRoot $relativePath
    if (-not (Test-Path -LiteralPath $absolutePath)) {
        $failures.Add("Missing working tree: $relativePath")
        continue
    }

    try {
        $actualCommit = Invoke-GitCapture $absolutePath @('rev-parse', 'HEAD')
        $indexEntry = Invoke-GitCapture $repositoryRoot @('ls-files', '--stage', '--', $relativePath)
        $expectedCommit = ($indexEntry -split '\s+')[1]

        if ($actualCommit -ne $expectedCommit -and -not $AllowGitlinkChanges) {
            $failures.Add("Commit mismatch for ${relativePath}: index=$expectedCommit checkout=$actualCommit")
        }
        elseif ($actualCommit -ne $expectedCommit) {
            Write-Host "CHANGED  $relativePath  index=$expectedCommit checkout=$actualCommit"
        }

        $dirty = Invoke-GitCapture $absolutePath @('status', '--porcelain')
        if ($dirty) {
            $failures.Add("Dirty submodule: $relativePath")
        }

        $isShallow = Invoke-GitCapture $absolutePath @('rev-parse', '--is-shallow-repository')
        if (-not $AllowShallow -and $isShallow -eq 'true') {
            $failures.Add("Shallow history is not allowed for the default checkout: $relativePath")
        }

        Write-Host "OK  $relativePath  $actualCommit  shallow=$isShallow"
    }
    catch {
        $failures.Add("${relativePath}: $($_.Exception.Message)")
    }
}

$recursiveStatus = @(& git -C $repositoryRoot submodule status --recursive 2>&1)
if ($LASTEXITCODE -ne 0) {
    $failures.Add("Unable to inspect recursive submodule state: $($recursiveStatus | Out-String)")
}
else {
    foreach ($statusLine in $recursiveStatus) {
        if ($statusLine -and $statusLine[0] -in @('-', '+', 'U')) {
            $failures.Add("Invalid recursive submodule state: $statusLine")
        }
    }
}

if ($failures.Count -gt 0) {
    throw ($failures -join [Environment]::NewLine)
}

Write-Host "Verified $($expectedPaths.Count) pinned submodules."
