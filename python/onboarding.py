
import json
from pathlib import Path

employee = {
    "employee_id": "EMP001",
    "name": "Alex Morgan",
    "asset_tag": "00001",
    "software_licence": "Microsoft 365 Business Standard",
    "tasks": {
        "create_employee_record": True,
        "assign_laptop": True,
        "assign_software_licence": False,
        "verify_access": False
    }
}

pending = [
    task for task, completed in employee["tasks"].items()
    if not completed
]

record = {
    **employee,
    "pending_tasks": pending,
    "onboarding_status": "Complete" if not pending else "In Progress"
}

output = Path(__file__).parent / "onboarding_record.json"
output.write_text(json.dumps(record, indent=4), encoding="utf-8")

print("Onboarding checklist saved.")
print("Employee:", employee["name"])
print("Status:", record["onboarding_status"])
print("Pending tasks:", len(pending))

for task in pending:
    print("-", task)
