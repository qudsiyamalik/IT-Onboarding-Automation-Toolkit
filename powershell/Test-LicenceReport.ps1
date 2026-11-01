# IT Onboarding Automation Toolkit
# Demonstration Licence Report

$licences = @(
    [PSCustomObject]@{
        Employee     = "Alex Morgan"
        Software     = "Microsoft 365 Business Standard"
        LicenceSeats = 5
        Status       = "Demo - Not Live"
    },
    [PSCustomObject]@{
        Employee     = "Jamie Wilson"
        Software     = "Microsoft 365 Business Standard"
        LicenceSeats = 5
        Status       = "Demo - Not Live"
    }
)

Write-Host "IT Onboarding Toolkit - Licence Report"
Write-Host "--------------------------------------"

$licences | Format-Table Employee, Software, LicenceSeats, Status -AutoSize

$reportPath = Join-Path $PSScriptRoot "licence_report.csv"

$licences | Export-Csv -Path $reportPath -NoTypeInformation

Write-Host ""
Write-Host "Demonstration report saved to:"
Write-Host $reportPath