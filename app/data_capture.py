class DataCapture:


    def __init__(self):
        #
        self.numbers = []
        self.max_value = 1000
        self.numbers_count = [0] * self.max_value
    
    def add(self, number):        

        self.numbers.append(number)
        self.numbers_count[number] += 1