# IT Onboarding Automation Toolkit
# Microsoft 365 Licence Status Verification

$ErrorActionPreference = "Stop"

try {
    $context = Get-MgContext

    if (-not $context) {
        Write-Host "No Microsoft Graph session found."
        Write-Host "Please connect to Microsoft Graph first."
        exit 1
    }

    $users = Get-MgUser -All `
        -Property DisplayName,UserPrincipalName,AssignedLicenses

    $report = foreach ($user in $users) {
        [PSCustomObject]@{
            DisplayName       = $user.DisplayName
            UserPrincipalName = $user.UserPrincipalName
            LicenceCount      = @($user.AssignedLicenses).Count
        }
    }

    $report | Format-Table -AutoSize

    Write-Host "Licence status report completed."
}
catch {
    Write-Error "Licence report failed: $($_.Exception.Message)"
}