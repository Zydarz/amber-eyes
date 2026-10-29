param(
  [string]$Sid = 'subw',
  [string]$JsFile = ''
)
$ErrorActionPreference = 'Continue'
$env:BSK_AUTO_START = '0'

Write-Output '=== session list ==='
bsk session list 2>$null | Out-String | Write-Output

Write-Output '=== evaluate --help ==='
bsk evaluate --help 2>$null | Out-String -Width 160 | Write-Output

if ($JsFile -and (Test-Path $JsFile)) {
  $js = [System.IO.File]::ReadAllText($JsFile, [Text.Encoding]::UTF8)
  Write-Output '=== evaluate ==='
  $r = (bsk evaluate --script $JsFile --session $Sid 2>&1 | Out-String)
  Write-Output "RESULT=$r"
} else {
  Write-Output '=== evaluate simple ==='
  $r = (bsk evaluate 'location.href' --session $Sid 2>&1 | Out-String)
  Write-Output "RESULT=$r"
}
