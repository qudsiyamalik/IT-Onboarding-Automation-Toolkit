# Employee Offboarding Runbook

## Purpose

This runbook provides a consistent process for recording IT offboarding tasks when an employee leaves an organisation.

## Step 1: Verify the Offboarding Request

Confirm that the request is authorised and that the employee's identity and departure details have been checked.

## Step 2: Review Assigned Assets

Open Snipe-IT and inspect the employee's assigned assets. Confirm which devices and equipment must be returned.

## Step 3: Recover Equipment

Arrange the return of assigned equipment. Record the asset check-in in Snipe-IT after the equipment has been received and checked.

## Step 4: Review Software Access

Follow the organisation's approved access-removal procedure. Confirm the relevant account and services before making changes.

## Step 5: Review Licence Reclamation

Verify whether the employee has assigned licences. Reclaim a licence only after confirming that the organisation's policy permits the change and that the licence is no longer required.

## Step 6: Generate the Offboarding Checklist

From the project root, run:

```powershell
.\.venv\Scripts\python.exe .\python\offboarding.py
```

Inspect the generated JSON record and identify pending tasks.

## Step 7: Close the Process

Confirm that equipment recovery, access review, licence review and employee record closure have been completed or explicitly assigned for follow-up.

## Important Limitation

The current Python script generates a checklist. It does not independently disable Microsoft 365 accounts, recover physical devices or reclaim licences.