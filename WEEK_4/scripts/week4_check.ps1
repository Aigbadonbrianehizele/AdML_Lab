cd $PSScriptRoot\..\src
$modules = @('week_04.linalg_foundations','week_04.gradients','week_04.tensor_ops','week_04.loss_landscape')
foreach ($mods in $modules){
    $result = python -m $mods 2>&1
    if ($LASTEXITCODE -eq 0){
        Write-Host "PASS: $mods" -ForegroundColor Green
    }
    else {
        Write-Host "FAIL: $mods" -ForegroundColor Red; Write-Host "$result"
    }
}