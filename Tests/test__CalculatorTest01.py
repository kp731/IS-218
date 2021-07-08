import unittest
from Calculator.Calculator.Calculator01 import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        self.test_data = CsvReader('/Tests/Data/Unit Test Addition.csv')
        CsvReader.clear_data(self.test_data)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('/Tests/Data/Unit Test Addition.csv').data
        for row in test_data:
            Result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), Result)
            self.assertEqual(self.calculator.result, Result)
            pprint(row)

    def test_subtraction_method_calculator(self):
        test_data = CsvReader('/Tests/Data/Unit Test Subtraction.csv').data
        for row in test_data:
            Result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), Result)
            self.assertEqual(self.calculator.result, Result)
            pprint(row)
        # self.assertEqual(self.calculator.subtract(2, 2), 0)
        # self.assertEqual(self.calculator.result, 0)

    def test_Multiplication_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader('/Tests/Data/Unit Test Multiplication.csv').data
        for row in test_data:
            Result = float(row['Result'])
            self.assertEqual(self.calculator.Multiplication(row['Value 1'], row['Value 2']), Result)
            self.assertEqual(self.calculator.result, Result)
            pprint(row)
        # self.assertEqual(self.calculator.subtract(2, 2), 0)
        # self.assertEqual(self.calculator.result, 0)

    def test_Division_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader('/Tests/Data/Unit Test Division.csv').data
        for row in test_data:
            Result = round(float(row['Result']), 9)
            self.assertEqual(self.calculator.Division(row['Value 1'], row['Value 2']), Result)
            self.assertEqual(self.calculator.result, Result)

            pprint(row)
        # self.assertEqual(self.calculator.subtract(2, 2), 0)
        # self.assertEqual(self.calculator.result, 0)

    def test_Square_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader('/Tests/Data/Unit Test Square.csv').data
        for row in test_data:
            Result = float(row['Result'])
            self.assertEqual(self.calculator.Square(float(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))
            pprint(row)
        # self.assertEqual(self.calculator.subtract(2, 2), 0)
        # self.assertEqual(self.calculator.result, 0)

    def test_SquareRoot_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader('/Tests/Data/Unit Test Square Root.csv').data
        for row in test_data:
            Result = round(float(row['Result']), 8)
            self.assertEqual(self.calculator.SquareRoot(row['Value 1']), Result)
            self.assertEqual(self.calculator.result, Result)
            pprint(row)
        # self.assertEqual(self.calculator.subtract(2, 2), 0)
        # self.assertEqual(self.calculator.result, 0)


'''
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

'''
if __name__ == '__main__':
    unittest.main()
