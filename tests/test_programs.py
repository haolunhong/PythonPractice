import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestPythonPractice(unittest.TestCase):
    def test_start_program(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "start.py")],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Mac", result.stdout)

    def test_grades(self):
        cases = {
            100: "A",
            90: "A",
            89: "B",
            80: "B",
            79: "C",
            70: "C",
            69: "D",
            60: "D",
            59: "E",
        }
        for score, expected in cases.items():
            with self.subTest(score=score):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "test.py")],
                    input=f"{score}\n",
                    capture_output=True,
                    text=True,
                    check=True,
                )
                self.assertEqual(result.stdout.strip()[-1], expected)


if __name__ == "__main__":
    unittest.main()
