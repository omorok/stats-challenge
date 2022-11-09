class Stats:
    '''
    Stats object contains methods to display the basic statistics.

    Attributes:
        numbers_count (list[int]): list with count of each value.
        lower (list[int]): list with total of values lower than each value.
        length: count of elements in the collection of the numbers.
    '''
    error_msg = 'Value error: out of range.'

    def __init__(self, numbers_count, lower, length):
        self.numbers_count = numbers_count
        self.lower = lower
        self.length = length

    def less(self, number):
        '''
        Returns total of values lower than number
        O(1) — Constant time complexity.
        '''
        if self.validate_number(number):
            return self.error_msg
        return self.lower[number]

    def greater(self, number):
        '''Returns total of values higher than number
        O(1) — Constant time complexity.
        '''
        if self.validate_number(number):
            return self.error_msg
        return self.length - (self.lower[number] + self.numbers_count[number])

    def between(self, min, max):
        '''Returns total of values between mix and max
        O(1) — Constant time complexity.
        '''
        if self.validate_number(min) or self.validate_number(max):
            return self.error_msg
        return self.less(max+1) - self.less(min-1)

    def validate_number(self, number):
        return(0 > number or number > (len(self.numbers_count)-1))
