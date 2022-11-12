from app.stats import Stats
class DataCapture:
    '''
    DataCapture class makes posible to store the numbers in challenge.
    All positive integer numbers less than max_value.
        
    - numbers (list[int]): collection of numbers.
    - max_value (int): highest value that the collection can contain.
    - numbers_count (list[int]): list with count of each number.
    '''
    
    error_msg = 'Input value error: value out of range or different integer type.'

    def __init__(self) -> None:
        #        
        self.numbers = []
        self.max_value = 1000
        self.numbers_count = [0] * self.max_value
    
    def add(self, number) -> None:        
        '''
        "add" method help: store new values incrementing the count of each one in the respective position in numbers_count.
        
        - number (int): new value.
        '''
        if self.validate_number(number):
            return self.error_msg
        self.numbers.append(number)
        self.numbers_count[number] += 1
    
    def build_stats(self) -> Stats:
        '''
        "build_stat" method help: returns an Stats object after calculate the total of the lowest values  
        accumulating the previous values in numbers_count. O(n)
                
        - Stats (Class): object with methods to display statistics.
        '''
        lowest = [0]*self.max_value
        for i in range(1, len(self.numbers_count)):
            lowest[i] = lowest[i-1] + self.numbers_count[i-1]
        return Stats(self.numbers_count, lowest, len(self.numbers))
    
    def validate_number(self, number) -> bool:
        return (0 > number or number > (len(self.numbers_count)-1) or type(number) != int)