import unittest
from Calculator01 import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_Multiplication_method_calculator(self):
        self.assertEqual(self.calculator.Multiplication(3, 4), 12)
        self.assertEqual(self.calculator.result, 12)

    def test_Division_method_calculator(self):
        self.assertEqual(self.calculator.Division(24, 8), 3)
        self.assertEqual(self.calculator.result, 3)

    def test_Square_method_calculator(self):
        self.assertEqual(self.calculator.Square(8, 2), 64)
        self.assertEqual(self.calculator.result, 64)

    def test_SquareRoot_method_calculator(self):
        self.assertEqual(self.calculator.SquareRoot(36), 6)
        self.assertEqual(self.calculator.result, 6)


if __name__ == '__main__':
    unittest.main()
