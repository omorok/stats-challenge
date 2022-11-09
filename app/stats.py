
class Stats:

    def __init__(self, numbers_count, lower, length):
        self.numbers_count = numbers_count
        self.lower = lower
        self.length = length
        print(numbers_count)
        print(lower)
        print(length)
    
    def less(self, number):
        '''
        "less" method help: returns the total of values lower than a number provided. O(1)
        '''
        if self.validate_number(number):
            return self.error_msg
        return self.lower[number]