# Randomly pick a service status
$statuses = @("Healthy", "Warning", "Critical")
$status = Get-Random -InputObject $statuses

# Randomly pick a system service
$services = @("SQL Server", "Web Server", "Authentication Service", "API Gateway")
$service = Get-Random -InputObject $services

# Build the log entry
$log = @{
    type = "SYSTEM"
    message = "$service is reporting status: $status"
    service = $service
} 

# Convert to JSON
$json = $log | ConvertTo-Json

# Send to the backend
Invoke-RestMethod -Uri http://localhost:5000/api/push-log `
  -Method POST `
  -Body $json `
  -ContentType "application/json"

Write-Host "Sent health check log: $($log.message)"
