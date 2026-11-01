# Troubleshooting Guide

## Docker Engine Does Not Start

Open Docker Desktop and wait for the engine to become ready. In PowerShell, run:

```powershell
docker.exe version
docker.exe compose ps
```

If the Docker server is unavailable, check Docker Desktop status and its diagnostic messages.

## Snipe-IT Does Not Open

Confirm that the application and database containers are running. Review the application logs:

```powershell
docker.exe compose logs --tail=100 app
```

Run Docker Compose commands from the directory containing the Compose configuration.

## Python Script Fails

Run the script using the project's virtual environment:

```powershell
.\.venv\Scripts\python.exe .\python\onboarding.py
```

Read the complete error message and verify the file path and Python dependencies.

## Ansible Is Not Recognised

Confirm that Ansible is installed in the intended Linux environment:

```bash
ansible --version
```

Do not assume that Ansible is installed in Windows merely because WSL is available.

## Microsoft Graph Authentication Fails

Check the installed PowerShell modules, tenant access and required permissions. Do not put access tokens or passwords into source files.

## Documentation Does Not Build

Confirm that `mkdocs.yml` exists in the project root and that the files referenced in its navigation exist inside the `docs` directory.