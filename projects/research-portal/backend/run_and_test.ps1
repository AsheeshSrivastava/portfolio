# Start backend and test it

Write-Host "`n[1/2] Starting backend..." -ForegroundColor Yellow
$backend = Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; poetry run uvicorn app.main:app --host 127.0.0.1 --port 8000" -PassThru

Start-Sleep -Seconds 12

Write-Host "`n[2/2] Testing API..." -ForegroundColor Yellow

$body = @{
    question = "test"
    provider = "openai"
    history = @()
} | ConvertTo-Json

try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/chat/query" -Method POST -Body $body -ContentType "application/json" -UseBasicParsing -TimeoutSec 10
    Write-Host "[SUCCESS] API works!" -ForegroundColor Green
} catch {
    Write-Host "[FAILED] $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "`nCheck the backend window for error details." -ForegroundColor Yellow
}

Write-Host "`nPress Enter to stop backend..." -ForegroundColor Yellow
Read-Host

Stop-Process -Id $backend.Id -Force



