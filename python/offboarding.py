
import json
from pathlib import Path

offboarding = {
    "employee_id": "EMP001",
    "name": "Alex Morgan",
    "tasks": {
        "confirm_departure": True,
        "recover_laptop": False,
        "revoke_software_access": False,
        "reclaim_licence": False,
        "close_employee_record": False
    }
}

pending = [
    task for task, completed in offboarding["tasks"].items()
    if not completed
]

result = {
    **offboarding,
    "pending_tasks": pending,
    "offboarding_status": "Complete" if not pending else "In Progress"
}

output = Path(__file__).parent / "offboarding_record.json"
output.write_text(json.dumps(result, indent=4), encoding="utf-8")

print("Offboarding checklist saved.")
print("Status:", result["offboarding_status"])
print("Pending tasks:", len(pending))

for task in pending:
    print("-", task)
