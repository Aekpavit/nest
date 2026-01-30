import unittest
from grade_calculator import GradeCalculator

class TestGradeCalculator(unittest.TestCase):
    def test_grade_A(self):
        calculator = GradeCalculator()
        self.assertEqual(calculator.calculate_grade(85), "A")

if __name__ == "__main__":
    unittest.main()
