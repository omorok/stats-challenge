
class Stats:
    '''
    Stats class makes possible to execute stats methods using Stats object.
    - numbers_count (list[int]): list with count of each value.
    - lower (list[int]): list with total of values lower than each value.
    - length: count of elements in the collection of the numbers.
    '''

    error_msg = 'Input value error: value out of range.'

    def __init__(self, numbers_count, lower, length):
        self.numbers_count = numbers_count
        self.lower = lower
        self.length = length
            
    def less(self, number):
        '''
        "less" method help: returns the total of values lower than a number provided. O(1)
        '''
        if self.validate_number(number):
            return self.error_msg
        return self.lower[number]
    
    def greater(self, number):
        '''
        "greater" method help: returns total of values higher than a number. O(1) 
        '''
        if self.validate_number(number):
            return self.error_msg
        return self.length - (self.lower[number] + self.numbers_count[number])
    
    def between(self, min, max):
        '''
        "between" method help: returns total of values between min and max threshold. O(1)
        '''
        if self.validate_number(min) or self.validate_number(max):
            return self.error_msg
        return self.less(max+1) - self.less(min)
    
    def validate_number(self, number):
        return(0 > number or number > (len(self.numbers_count)-1))