import math


def addition(a, b):
    c = int(a) + int(b)
    return c


def subraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def Multiplication(a, b):
    c = float(a) * float(b)
    return c


def Division(a, b):
    c = float(b)/float(a)
    return round(c, 9)


def Square(a):
    return float(a) * float(a)


def SquareRoot(a):
    return round(math.sqrt(float(a)), 8)


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
