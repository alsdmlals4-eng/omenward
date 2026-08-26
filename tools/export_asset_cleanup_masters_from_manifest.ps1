param(
    [Parameter(Mandatory = $true)]
    [string]$ApprovedSourceManifest,
    [Parameter(Mandatory = $true)]
    [string]$ExportManifest
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing
Add-Type -ReferencedAssemblies System.Drawing -TypeDefinition @'
using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

public static class OmenwardManifestCleanup
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
                        int alphaIndex = row + (x * 4) + 3;
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

$sources = Get-Content -LiteralPath $ApprovedSourceManifest -Raw | ConvertFrom-Json
$results = foreach ($entry in $sources) {
    $source = $entry.ApprovedSource
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        throw "Approved source missing: $source"
    }
    $mastersDirectory = Join-Path (Split-Path -Parent $source) 'masters'
    New-Item -ItemType Directory -Force -Path $mastersDirectory | Out-Null
    $target = Join-Path $mastersDirectory (([IO.Path]::GetFileNameWithoutExtension($source)) + '_CLEANUP_MASTER_V1.png')
    if (Test-Path -LiteralPath $target) {
        throw "Refusing to overwrite cleanup master: $target"
    }
    $temporary = "$target.tmp.png"
    if (Test-Path -LiteralPath $temporary) {
        throw "Temporary cleanup target already exists: $temporary"
    }
    [OmenwardManifestCleanup]::Export($source, $temporary, 63)
    Move-Item -LiteralPath $temporary -Destination $target
    [pscustomobject]@{
        Source = $source
        Master = $target
        SourceSha256 = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
        MasterSha256 = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()
    }
}

$results | ConvertTo-Json -Depth 3 | Out-File -LiteralPath $ExportManifest -Encoding utf8
