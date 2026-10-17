param([switch]$Execute)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$taskRepo = 'D:\Workspace\agentic_cinema'
$taskArchive = [IO.Path]::GetFullPath('D:\Workspace\agentic_cinema_media_archive\EP01_Nem_Bui_20261017')
$taskManifest = Join-Path $taskArchive 'DANH_MUC_TAT_CA_NGUON_V2.csv'
$taskManifestHash = '07ece0c8bff5a98dd3caae2b09a9ec9e42c62fe41cccd8169697ac46e4d29ead'
$taskSummaryHash = 'e1e6752f3b6025d360554460a2e6730728375172d76ade4ee5bee97c23fa289f'
$taskQc = Join-Path $taskRepo 'he_thong_chatgpt_veo\series_anh_khoai_tay_chi_dao\episodes\ep01_pilot\restart_720p_v1\06_qc\MEDIA_CONSOLIDATION_325'
$taskAllowedRoots = @(
    'D:\Workspace\agentic_cinema\he_thong_chatgpt_veo',
    'D:\Workspace\agentic_cinema\artifacts',
    'C:\Users\PC\Downloads\du_an_nem_bui',
    'C:\Users\PC\.codex\generated_images\01a0eb0e-6ec3-7121-a6a5-ea0ccdb77744'
)
$taskExplicitRoots = @('C:\Users\PC\Downloads','C:\Users\PC\.codex\generated_images','C:\Users\PC\.codex\attachments')
$taskExtensions = @('.png','.jpg','.jpeg','.webp','.gif','.bmp','.tif','.tiff','.svg','.mp4','.mov','.mkv','.webm','.m4v','.avi','.wav','.mp3','.m4a','.aac','.ogg','.flac')

function Test-TaskChild([string]$Path, [string]$Root) {
    return $Path.StartsWith(([IO.Path]::GetFullPath($Root).TrimEnd('\') + '\'), [StringComparison]::OrdinalIgnoreCase)
}

function Get-TaskCheckedFile([string]$Path) {
    $item = Get-Item -LiteralPath $Path -Force
    if ($item.PSIsContainer) { throw "Not a file: $Path" }
    if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Reparse file refused: $Path" }
    return $item
}

function Get-TaskDriveFree {
    $result = @{}
    foreach ($name in @('C','D')) { $result[$name] = (Get-PSDrive -Name $name).Free }
    return $result
}

if ((Get-FileHash -LiteralPath $taskManifest -Algorithm SHA256).Hash.ToLowerInvariant() -ne $taskManifestHash) { throw 'Source manifest changed' }
$taskSummaryPath = Join-Path $taskArchive 'TONG_HOP_324_V2.json'
if ((Get-FileHash -LiteralPath $taskSummaryPath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $taskSummaryHash) { throw 'Archive summary changed' }
$taskRows = @(Import-Csv -LiteralPath $taskManifest)
if ($taskRows.Count -ne 13020) { throw 'Unexpected source count' }
if (Test-Path -LiteralPath $taskQc) { throw 'Receipt folder exists; review prior attempt before any rerun' }
New-Item -ItemType Directory -Path $taskQc | Out-Null

$taskFreeBefore = Get-TaskDriveFree
$taskPlan = [Collections.Generic.List[object]]::new()
$taskSeen = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
$taskArchiveChecks = @{}
$taskParentChecks = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
$taskCounter = 0
foreach ($row in $taskRows) {
    $source = [IO.Path]::GetFullPath($row.source)
    $destination = [IO.Path]::GetFullPath((Join-Path $taskArchive $row.archive_relative))
    if (-not $taskSeen.Add($source)) { throw "Duplicate source path in manifest: $source" }
    if (Test-TaskChild $source $taskArchive) { throw 'Source points into retained archive' }
    if (-not (Test-TaskChild $destination $taskArchive)) { throw 'Archive traversal refused' }
    $allowed = $false
    foreach ($root in $taskAllowedRoots) { if (Test-TaskChild $source $root) { $allowed = $true; break } }
    if (-not $allowed -and $row.origin -eq 'explicit_project_reference') {
        foreach ($root in $taskExplicitRoots) { if (Test-TaskChild $source $root) { $allowed = $true; break } }
    }
    if (-not $allowed) { throw "Source outside exact approved collection scope: $source" }
    if ([IO.Path]::GetExtension($source).ToLowerInvariant() -notin $taskExtensions) { throw "Non-media source refused: $source" }
    $sourceItem = Get-TaskCheckedFile $source
    # Reject junction/symlink ancestors instead of silently leaving the named tree.
    foreach ($path in @($source,$destination)) {
        $parent = [IO.Path]::GetDirectoryName($path)
        while ($parent -and $taskParentChecks.Add($parent)) {
            $parentItem = Get-Item -LiteralPath $parent -Force
            if (($parentItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Reparse ancestor refused: $parent" }
            $parent = [IO.Path]::GetDirectoryName($parent)
        }
    }
    if ($sourceItem.Length -ne [int64]$row.bytes) { throw "Source size changed: $source" }
    if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant() -ne $row.sha256) { throw "Source checksum changed: $source" }
    if (-not $taskArchiveChecks.ContainsKey($destination)) {
        $archiveItem = Get-TaskCheckedFile $destination
        if ($archiveItem.Length -ne [int64]$row.bytes) { throw "Archive size mismatch: $destination" }
        if ((Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLowerInvariant() -ne $row.sha256) { throw "Archive checksum mismatch: $destination" }
        $taskArchiveChecks[$destination] = @{Length=$archiveItem.Length; Ticks=$archiveItem.LastWriteTimeUtc.Ticks; Hash=$row.sha256}
    }
    $check = $taskArchiveChecks[$destination]
    if ($check.Hash -ne $row.sha256) { throw 'Conflicting archive hash' }
    $taskPlan.Add([pscustomobject]@{Source=$source; Archive=$destination; Bytes=$sourceItem.Length; Sha256=$row.sha256; SourceTicks=$sourceItem.LastWriteTimeUtc.Ticks; ArchiveTicks=$check.Ticks})
    $taskCounter++
    if ($taskCounter % 500 -eq 0 -or $taskCounter -eq $taskRows.Count) { Write-Output "PREFLIGHT $taskCounter/$($taskRows.Count): source+archive verified" }
}

$taskBytes = ($taskPlan | Measure-Object -Property Bytes -Sum).Sum
$taskPlan | Export-Csv -LiteralPath (Join-Path $taskQc 'exact_file_plan_325.csv') -NoTypeInformation -Encoding utf8BOM
$preflight = @{Record='REC325'; Date='2026-10-17'; ExecuteRequested=[bool]$Execute; SourceManifestSHA256=$taskManifestHash; Sources=$taskPlan.Count; UniqueArchiveFiles=$taskArchiveChecks.Count; LogicalSourceBytes=$taskBytes; AllSourceAndArchiveHashesReverified=$true; DirectoriesOrDocumentsRemoved=$false; ArchiveRetained=$taskArchive; FreeBefore=$taskFreeBefore}
$preflight | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $taskQc 'preflight_325.json') -Encoding utf8
if (-not $Execute) { Write-Output 'PLAN ONLY: no source removed'; exit 0 }

$taskReceipt = [Collections.Generic.List[object]]::new()
$taskJournal = Join-Path $taskQc 'source_cleanup_journal_325.jsonl'
$taskCounter = 0
try {
    foreach ($item in $taskPlan) {
        $sourceItem = Get-TaskCheckedFile $item.Source
        $archiveItem = Get-TaskCheckedFile $item.Archive
        if ($sourceItem.Length -ne $item.Bytes -or $sourceItem.LastWriteTimeUtc.Ticks -ne $item.SourceTicks) { throw "Source changed after preflight: $($item.Source)" }
        if ($archiveItem.Length -ne $item.Bytes -or $archiveItem.LastWriteTimeUtc.Ticks -ne $item.ArchiveTicks) { throw "Archive changed after preflight: $($item.Archive)" }
        # File-only operation against the validated manifest. Never recurse or remove the archive.
        Remove-Item -LiteralPath $item.Source -Force
        if (Test-Path -LiteralPath $item.Source) { throw "Source still exists after cleanup: $($item.Source)" }
        $receipt = [pscustomobject]@{Source=$item.Source; Archive=$item.Archive; Bytes=$item.Bytes; Sha256=$item.Sha256; Status='ORIGINAL_COPY_REMOVED_VERIFIED_ARCHIVE_RETAINED'}
        $taskReceipt.Add($receipt)
        $receipt | ConvertTo-Json -Compress | Add-Content -LiteralPath $taskJournal -Encoding utf8
        $taskCounter++
        if ($taskCounter % 500 -eq 0 -or $taskCounter -eq $taskPlan.Count) { Write-Output "CONSOLIDATED $taskCounter/$($taskPlan.Count): originals removed, archive retained" }
    }
} finally {
    $taskReceipt | Export-Csv -LiteralPath (Join-Path $taskQc 'source_cleanup_receipt_325.csv') -NoTypeInformation -Encoding utf8BOM
    $taskResult = @{Record='REC325'; Date='2026-10-17'; Status= $(if($taskReceipt.Count -eq $taskPlan.Count){'CONSOLIDATED_INTO_ONE_RETAINED_ARCHIVE'}else{'PARTIAL_STOP_CHECK_JOURNAL'}); SourceCopiesRemoved=$taskReceipt.Count; PlannedSources=$taskPlan.Count; LogicalBytesRemoved=($taskReceipt|Measure-Object Bytes -Sum).Sum; ArchiveFilesRetained=$taskArchiveChecks.Count; Archive=$taskArchive; SourceManifestSHA256=$taskManifestHash; SourceDirectoriesRemoved=0; TextOrCodeFilesRemoved=0; CloudActions=0; ArchiveDeleted=$false; RestorePossibleFromArchiveAndManifest=$true; OldAbsoluteMediaPathsNowUnavailable=$true; FreeBefore=$taskFreeBefore; FreeAfter=(Get-TaskDriveFree)}
    $taskResult | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $taskQc 'result_325.json') -Encoding utf8
    $taskResult | ConvertTo-Json -Depth 6 | Write-Output
}
