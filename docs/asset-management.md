# Asset Management Runbook

## Purpose

This runbook explains how technicians maintain asset records using Snipe-IT.

## Step 1: Open Snipe-IT

Start the required Docker services and open the Snipe-IT web interface at `http://localhost:8000` when running locally.

## Step 2: Search for an Existing Asset

Open the asset register and search by asset tag, serial number or asset name. Check the current status before making changes.

## Step 3: Register a New Asset

When a new asset must be recorded, enter its asset tag, model and serial number where available. Save the record and verify that it appears in the asset register.

## Step 4: Assign an Asset

Use the checkout function to associate the asset with the correct employee. Confirm the assignment after saving.

## Step 5: Record an Asset Return

When an asset is returned, open its record and use the check-in function. Verify that the asset is no longer assigned to the previous employee.

## Step 6: Verify the Record

Check the asset tag, serial number, status and assignment. Report duplicate or inaccurate records for correction.

## Expected Outcome

Snipe-IT maintains a searchable record of IT equipment and its assignment history.