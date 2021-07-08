from Calculator.Calculator.Addition import addition
from Calculator.Calculator.Division import Division


def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return Division(num_values, total)