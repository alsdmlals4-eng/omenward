param(
    [string]$ExportManifest = (Join-Path (Resolve-Path (Join-Path $PSScriptRoot "..")) '.asset-vault/p0_cleanup_master_export_2026-08-26-retry.json')
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing
Add-Type -ReferencedAssemblies System.Drawing -TypeDefinition @'
using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

public static class OmenwardPngCleanupVerification
{
    public static string Verify(string sourcePath, string masterPath)
    {
        using (var source = new Bitmap(sourcePath))
        using (var master = new Bitmap(masterPath))
        {
            if (source.Width != master.Width || source.Height != master.Height)
                throw new InvalidOperationException("master dimensions differ from source");

            var rect = new Rectangle(0, 0, source.Width, source.Height);
            var sourceBits = source.LockBits(rect, ImageLockMode.ReadOnly, PixelFormat.Format32bppArgb);
            var masterBits = master.LockBits(rect, ImageLockMode.ReadOnly, PixelFormat.Format32bppArgb);
            try
            {
                var sourceBytes = new byte[Math.Abs(sourceBits.Stride) * source.Height];
                var masterBytes = new byte[Math.Abs(masterBits.Stride) * master.Height];
                Marshal.Copy(sourceBits.Scan0, sourceBytes, 0, sourceBytes.Length);
                Marshal.Copy(masterBits.Scan0, masterBytes, 0, masterBytes.Length);

                int partialAlpha = 0;
                int cornerAlpha = 0;
                for (int y = 0; y < source.Height; y++)
                {
                    int sourceRow = sourceBits.Stride >= 0 ? y * Math.Abs(sourceBits.Stride) : (source.Height - 1 - y) * Math.Abs(sourceBits.Stride);
                    int masterRow = masterBits.Stride >= 0 ? y * Math.Abs(masterBits.Stride) : (master.Height - 1 - y) * Math.Abs(masterBits.Stride);
                    for (int x = 0; x < source.Width; x++)
                    {
                        int sourceIndex = sourceRow + (x * 4);
                        int masterIndex = masterRow + (x * 4);
                        byte sourceAlpha = sourceBytes[sourceIndex + 3];
                        byte masterAlpha = masterBytes[masterIndex + 3];
                        byte expectedAlpha = sourceAlpha <= 63 ? (byte)0 : (byte)255;
                        if (masterAlpha != expectedAlpha)
                            throw new InvalidOperationException("alpha cleanup mismatch at " + x + "," + y);
                        if (masterAlpha != 0 && masterAlpha != 255)
                            partialAlpha++;
                        if (sourceAlpha > 63 && (sourceBytes[sourceIndex] != masterBytes[masterIndex] || sourceBytes[sourceIndex + 1] != masterBytes[masterIndex + 1] || sourceBytes[sourceIndex + 2] != masterBytes[masterIndex + 2]))
                            throw new InvalidOperationException("opaque RGB changed at " + x + "," + y);
                    }
                }

                int[] corners = new int[] { 0, 0, source.Width - 1, 0, 0, source.Height - 1, source.Width - 1, source.Height - 1 };
                for (int i = 0; i < corners.Length; i += 2)
                {
                    int x = corners[i];
                    int y = corners[i + 1];
                    int row = masterBits.Stride >= 0 ? y * Math.Abs(masterBits.Stride) : (master.Height - 1 - y) * Math.Abs(masterBits.Stride);
                    cornerAlpha += masterBytes[row + (x * 4) + 3];
                }
                return "{\"width\":" + source.Width + ",\"height\":" + source.Height + ",\"partial_alpha_pixels\":" + partialAlpha + ",\"corner_alpha_sum\":" + cornerAlpha + "}";
            }
            finally
            {
                source.UnlockBits(sourceBits);
                master.UnlockBits(masterBits);
            }
        }
    }
}
'@

$manifest = Get-Content -LiteralPath $ExportManifest -Raw | ConvertFrom-Json
$results = foreach ($entry in $manifest) {
    $metrics = [OmenwardPngCleanupVerification]::Verify($entry.Source, $entry.Master) | ConvertFrom-Json
    [pscustomobject]@{
        Source = $entry.Source
        Master = $entry.Master
        SourceSha256 = $entry.SourceSha256
        MasterSha256 = $entry.MasterSha256
        Width = $metrics.width
        Height = $metrics.height
        PartialAlphaPixels = $metrics.partial_alpha_pixels
        CornerAlphaSum = $metrics.corner_alpha_sum
    }
}

$results | ConvertTo-Json -Depth 3
