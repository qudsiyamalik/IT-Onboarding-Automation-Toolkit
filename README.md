# IT Onboarding Automation and Asset Tracking Toolkit

## Project Overview

This project supports IT employee onboarding, offboarding, asset tracking and software licence administration for Ready IT Services.

## Technologies

- Snipe-IT for asset and licence inventory.
- Python for onboarding and offboarding checklist generation.
- Ansible for provisioning demonstrations.
- PowerShell and Microsoft Graph for licence-status verification.
- Docker Compose for running Snipe-IT and its database.
- MkDocs for technician runbooks.
- Git for source-code version control.

## Project Structure

```text
ansible/       Ansible provisioning files
docker/        Docker Compose configuration and local database backup
docs/          Technician runbooks
powershell/    Microsoft 365 verification scripts
python/        Onboarding and offboarding scripts
screenshots/   Practical demonstration evidence
tests/         Test scripts and test evidence
mkdocs.yml     Documentation configuration
README.md      Project overview and setup instructions
```

## Running Snipe-IT

Start Docker Desktop and wait for the engine to become ready.

From the directory containing `docker-compose.yml`, run:

```powershell
docker.exe compose up -d
docker.exe compose ps
```

Open `http://localhost:8000` when the application is running.

## Running Python Checklists

Run onboarding:

```powershell
.\.venv\Scripts\python.exe .\python\onboarding.py
```

Run offboarding:

```powershell
.\.venv\Scripts\python.exe .\python\offboarding.py
```

Review the generated JSON files in the `python` directory.

## Documentation

Install MkDocs:

```powershell
.\.venv\Scripts\python.exe -m pip install mkdocs
```

Build the documentation:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build
```

Serve the documentation on a separate port:

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -a 127.0.0.1:8001
```

## Security

Do not commit passwords, application keys, access tokens or other secrets. Keep local environment files and sensitive database backups out of public repositories.

## Implementation Status

The Snipe-IT asset register and Python checklist scripts have been tested in the development environment. Ansible, Microsoft Graph integration and MkDocs must be marked as complete only after their corresponding tests have been executed successfully.