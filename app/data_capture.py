class DataCapture:


    def __init__(self):
        #
        self.numbers = []
        self.max_value = 1000
        self.numbers_count = [0] * self.max_value
    
    def add(self, number):        

        self.numbers.append(number)
        self.numbers_count[number] += 1
    
    def build_stats(self):
       
        lowest = [0]*self.max_value
        for i in range(1, len(self.numbers_count)):
            lowest[i] = lowest[i-1] + self.numbers_count[i-1]
        return Stats(self.numbers_count, lowest, len(self.numbers))