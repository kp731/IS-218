def addition(a, b):
    return a + b


def subraction(a, b):
    return a - b


def Multiplication(a, b):
    return a * b


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
