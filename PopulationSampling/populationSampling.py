from RandomGenerator.random_generator import random
from Calculator.Calculator import Calculator01
from Statistics.Statistics import Statistics
import random


class PopulationSampling:

    def __init__(self):
        pass

    def choice(self, l, x, seed):
        random.seed(seed)
        return random.choices(l, k=x)

    def simple_random_sampling(self, l, x, y):
        # l = list
        # x = random numbers
        # y = seed
        rand = PopulationSampling()
        sample = rand.choice(l, x, y)
        return sample

    def confidence_interval(self, l):
        stats = Statistics()
        calculator = Calculator01()
        standard_dev = stats.standard_deviation(l)
        x = len(l)
        m = stats.mean(l)
        margin_error = calculator.Multiplication(1.96, (calculator.Division(calculator.SquareRoot(x), standard_dev)))
        confidence_interval = [round(calculator.addition(m, margin_error), 6), round(calculator.subraction(margin_error, m), 6)]
        return confidence_interval

    def margin_error(self, l):
        stats = Statistics()
        calculator = Calculator01()
        standard_dev = stats.standard_deviation(l)
        x = len(l)
        margin_of_error = calculator.Multiplication(1.96, calculator.sqr(calculator.div(calculator.sqr(standard_dev), x)))
        return margin_of_error
