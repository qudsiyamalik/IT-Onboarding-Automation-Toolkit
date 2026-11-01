# Testing and Verification

## Purpose

This document records the tests used to verify the toolkit's components.

## Test 1: Snipe-IT Availability

**Procedure:** Open the local Snipe-IT interface and inspect the asset register.

**Expected result:** The interface opens and previously created asset records are visible.

**Actual result:** Record the result observed during testing.

## Test 2: Python Onboarding Checklist

**Procedure:** Run the onboarding Python script and inspect its JSON output.

**Expected result:** An onboarding checklist record is generated.

**Actual result:** Record the command output and any pending tasks.

## Test 3: Python Offboarding Checklist

**Procedure:** Run the offboarding Python script and inspect its JSON output.

**Expected result:** An offboarding checklist record is generated.

**Actual result:** Record the command output and any pending tasks.

## Test 4: Ansible Provisioning Demonstration

**Procedure:** Run the playbook syntax check, execute the playbook and inspect the generated status file.

**Expected result:** The playbook completes without errors and creates the expected test file.

**Actual result:** Record the observed output.

## Test 5: PowerShell Licence Report

**Procedure:** Authenticate to an authorised Microsoft Graph tenant and execute the licence-status script.

**Expected result:** The script displays user information and assigned licence counts.

**Actual result:** Record the result only after the test has been executed.

## Test 6: MkDocs Build

**Procedure:** Run `mkdocs build` from the project root.

**Expected result:** MkDocs builds the documentation site without errors.

**Actual result:** Record the actual build result.

## Evidence

Store screenshots of successful tests and retain relevant error messages for failed tests. A test must not be marked as passed until its result has been observed.