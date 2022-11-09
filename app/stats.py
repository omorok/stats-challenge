
class Stats:

    def __init__(self, numbers_count, lower, length):
        self.numbers_count = numbers_count
        self.lower = lower
        self.length = length
        print(numbers_count)
        print(lower)
        print(length)
    
    def less(self, number):
        
        if self.validate_number(number):
            return self.error_msg
        return self.lower[number]
    
    def greater(self, number):
        
        if self.validate_number(number):
            return self.error_msg
        return self.length - (self.lower[number] + self.numbers_count[number])
    
    def between(self, min, max):
        
        if self.validate_number(min) or self.validate_number(max):
            return self.error_msg
        return self.less(max+1) - self.less(min-1)