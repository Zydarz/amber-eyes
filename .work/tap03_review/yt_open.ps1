param(
  [string]$Url = 'https://studio.youtube.com/channel/UCloOzyxGK3TGtp6ICJpGRBA/music',
  [string]$Js = "JSON.stringify({url:location.href,title:document.title,ready:document.readyState})"
)
$ErrorActionPreference = 'Continue'
$env:BSK_AUTO_START = '0'

$out = (bsk session start --json --browser 6e12c7c2 2>$null | Out-String)
try { $sid = ($out | ConvertFrom-Json).session_id } catch { $sid = $null }
if (-not $sid) { Write-Output "SESSION_START_FAILED`n$out"; exit 1 }
Write-Output "SESSION=$sid"

bsk navigate $Url --session $sid 2>$null | Out-String | Write-Output
Start-Sleep -Seconds 12

$js = $Js -replace '"', '\"'
$ev = (bsk evaluate $js --session $sid 2>$null | Out-String)
Write-Output "EVAL=$ev"
Write-Output "SESSIONID_KEEP=$sid"
