from Calculator.Calculator.Addition import addition
from Calculator.Calculator.Subtraction import subraction
from Calculator.Calculator.Mulitiplication import Multiplication
from Calculator.Calculator.Division import Division
from Calculator.Calculator.Squaring import Square
from Calculator.Calculator.SquarerRoot import SquareRoot

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subraction(a, b)
        return self.result

    def Multiplication(self, a, b):
        self.result = Multiplication(a, b)
        return self.result

    def Division(self, a, b):
        self.result = Division(a, b)
        return self.result

    def Square(self, a):
        self.result = Square(a)
        return self.result

    def SquareRoot(self, a):
        self.result = SquareRoot(float(a))
        return self.result
