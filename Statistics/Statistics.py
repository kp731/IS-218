from Calculator.Calculator import Calculator01
from Statistics.Mean import mean





class Statistics(Calculator01):

    def mean(self, data):
        self.result = mean(data)
        return self.result

