param(
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing
Add-Type -ReferencedAssemblies System.Drawing -TypeDefinition @'
using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

public static class OmenwardPngCleanup
{
    public static void Export(string sourcePath, string targetPath, int alphaCutoff)
    {
        using (var master = new Bitmap(sourcePath))
        {
            var rect = new Rectangle(0, 0, master.Width, master.Height);
            var bits = master.LockBits(rect, ImageLockMode.ReadWrite, PixelFormat.Format32bppArgb);
            try
            {
                int stride = Math.Abs(bits.Stride);
                var pixels = new byte[stride * master.Height];
                Marshal.Copy(bits.Scan0, pixels, 0, pixels.Length);
                for (int y = 0; y < master.Height; y++)
                {
                    int row = bits.Stride >= 0 ? y * stride : (master.Height - 1 - y) * stride;
                    for (int x = 0; x < master.Width; x++)
                    {
                        int index = row + (x * 4);
                        int alphaIndex = index + 3;
                        pixels[alphaIndex] = pixels[alphaIndex] <= alphaCutoff ? (byte)0 : (byte)255;
                    }
                }
                Marshal.Copy(pixels, 0, bits.Scan0, pixels.Length);
            }
            finally
            {
                master.UnlockBits(bits);
            }

            master.Save(targetPath, ImageFormat.Png);
        }
    }
}
'@

$sources = @(
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_GREATSWORD_WARRIOR_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_SPEAR_GUARD_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_SPEAR_GUARD_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_ASSASSIN_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_ASSASSIN_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_ARCHER_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_ARCHER_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_CAVALRY_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_CAVALRY_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_PRIEST_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_PRIEST_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_MAGE_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_MAGE_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_FLIER_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_FLIER_IDLE_V1.png',
    'characters/allies/OMENWARD_ASSET_UNIT_LUMERN_GIANT_IDLE_V1.png',
    'characters/enemies/OMENWARD_ASSET_UNIT_VEIL_GIANT_IDLE_V1.png',
    'buildings/OMENWARD_ASSET_BUILDING_VAULT_T1.png',
    'buildings/OMENWARD_ASSET_BUILDING_FARM_T1.png',
    'buildings/OMENWARD_ASSET_BUILDING_GENERAL_BARRACKS_T1.png',
    'buildings/OMENWARD_ASSET_BUILDING_SPECIAL_BARRACKS_T1.png',
    'buildings/OMENWARD_ASSET_BUILDING_DEFENSE_TOWER_T1.png',
    'buildings/OMENWARD_ASSET_BUILDING_COMMAND_POST_T1.png',
    'buildings/OMENWARD_ASSET_BUILDING_MANA_TOWER_T1.png'
)

$libraryRoot = Join-Path $RepositoryRoot '.asset-vault/library'
$results = foreach ($relativeSource in $sources) {
    $source = Join-Path $libraryRoot $relativeSource
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        throw "Approved source missing: $relativeSource"
    }
    $sourceDirectory = Split-Path -Parent $source
    $mastersDirectory = Join-Path $sourceDirectory 'masters'
    New-Item -ItemType Directory -Force -Path $mastersDirectory | Out-Null
    $targetName = ([IO.Path]::GetFileNameWithoutExtension($source)) + '_CLEANUP_MASTER_V1.png'
    $target = Join-Path $mastersDirectory $targetName
    if (Test-Path -LiteralPath $target) {
        throw "Refusing to overwrite cleanup master: $target"
    }
    $temporary = "$target.tmp.png"
    if (Test-Path -LiteralPath $temporary) {
        throw "Temporary cleanup target already exists: $temporary"
    }

    [OmenwardPngCleanup]::Export($source, $temporary, 63)
    Move-Item -LiteralPath $temporary -Destination $target
    [pscustomobject]@{
        Source = $source
        Master = $target
        SourceSha256 = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
        MasterSha256 = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()
    }
}

$results | ConvertTo-Json -Depth 3
