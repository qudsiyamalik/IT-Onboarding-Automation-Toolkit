import json
import subprocess
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT / "python" / "offboarding.py"
OUTPUT = PROJECT / "python" / "offboarding_record.json"

class TestOffboarding(unittest.TestCase):
    def test_offboarding_record(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertIn("Offboarding checklist saved.", result.stdout)
        record = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(record["employee_id"], "EMP001")
        self.assertEqual(record["name"], "Alex Morgan")
        self.assertEqual(record["offboarding_status"], "In Progress")
        self.assertEqual(
            set(record["pending_tasks"]),
            {
                "recover_laptop",
                "revoke_software_access",
                "reclaim_licence",
                "close_employee_record"
            }
        )
        self.assertEqual(len(record["pending_tasks"]), 4)

if __name__ == "__main__":
    unittest.main()
