def addition(a, b):
    return a + b


def subraction(a, b):
    return a - b


def Multiplication(a, b):
    return a * b


def Division(a, b):
    return a / b


def Square(a, b):
    return a ** b


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

    def Square(self, a, b):
        self.result = Square(a, b)
        return self.result
