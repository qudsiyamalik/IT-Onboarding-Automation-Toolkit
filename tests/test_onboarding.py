import json
import subprocess
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT / "python" / "onboarding.py"
OUTPUT = PROJECT / "python" / "onboarding_record.json"

class TestOnboarding(unittest.TestCase):
    def test_onboarding_record(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertIn("Onboarding checklist saved.", result.stdout)
        record = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(record["employee_id"], "EMP001")
        self.assertEqual(record["name"], "Alex Morgan")
        self.assertEqual(record["onboarding_status"], "In Progress")
        self.assertEqual(
            set(record["pending_tasks"]),
            {"assign_software_licence", "verify_access"}
        )

if __name__ == "__main__":
    unittest.main()
