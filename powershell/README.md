# PowerShell Automation

## Purpose

This folder contains PowerShell scripts for Microsoft 365 licence verification and IT offboarding support.

## Licence Status Verification

The `Get-LicenceStatus.ps1` script retrieves Microsoft 365 user information and reports the number of assigned licences.

## Prerequisites

- Windows PowerShell or PowerShell 7
- Microsoft Graph PowerShell modules
- An authorised Microsoft 365 test tenant
- Appropriate Microsoft Graph permissions

## Execution

Install the required modules:

```powershell
Install-Module Microsoft.Graph.Users -Scope CurrentUser
Install-Module Microsoft.Graph.Authentication -Scope CurrentUser
```

Authenticate:

```powershell
Connect-MgGraph -Scopes "User.Read.All"
```

Run the report from the project root:

```powershell
.\powershell\Get-LicenceStatus.ps1
```

## Security

Use an authorised test tenant. Do not store passwords, access tokens or client secrets in source files. The current script performs read-only licence reporting; it does not revoke licences or disable accounts.