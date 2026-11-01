# Employee Onboarding Runbook

## Purpose

This runbook provides a consistent procedure for preparing IT equipment and tracking tasks for a new employee.

## Step 1: Create the Employee Record

Open the Snipe-IT web interface and verify that the employee record exists. Create a record only when required.

## Step 2: Check Asset Availability

Open the asset register and identify an available laptop or other required equipment. Check the asset tag, serial number and status before assignment.

## Step 3: Assign the Asset

Use the Snipe-IT checkout function to assign the selected asset to the employee. Verify that the correct employee and asset are linked.

## Step 4: Record the Onboarding Checklist

Run the Python onboarding script from the project root:

```powershell
.\.venv\Scripts\python.exe .\python\onboarding.py
```

Inspect the generated onboarding JSON record.

## Step 5: Verify Software Access

Check the employee's required software and access permissions through the authorised administrative process. Do not mark access verification complete until there is evidence that the required access has been checked.

## Step 6: Confirm Completion

Review outstanding checklist tasks. Record incomplete tasks and assign them for follow-up.

## Expected Outcome

The employee has a recorded onboarding checklist, an appropriate asset assignment where applicable, and a clear record of outstanding tasks.

The Python checklist does not automatically create Snipe-IT records or provision Microsoft 365 accounts unless an integration is implemented and tested.