from Calculator.Calculator.Addition import addition
from Calculator.Calculator.Division import Division


def sample_mean(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)