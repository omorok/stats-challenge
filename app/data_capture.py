from app.stats import Stats

class DataCapture:
    
    #DataCapture object contains a collection of small
    #positive integers. All values will be less than max_value.
    #
    #Attributes:
    #    numbers (list[int]): collection of numbers.
    #    max_value (int): highest value that the collection can contain.
    #    numbers_count (list[int]): list with count of each number.
    

    def __init__(self):
        #
        self.numbers = []
        self.max_value = 1000
        self.numbers_count = [0] * self.max_value

    def add(self, number):
        
        #Add a new value to the collection and increment the count 
        #in the corresponding position of the number in numbers_count.
        #O(1) — Constant time complexity.
        #
        #Args:
        #    number (int): the new value to add.
        #
        self.numbers.append(number)
        self.numbers_count[number] += 1

    def build_stats(self):
        
        #Computes the total of the lowers values of each value by
        #accumulating the sum of the previous values in numbers_count.
        #O(n) — Linear time complexity.
        #
        #Returns:
        #    Stats (Class): object with methods to display statistics.
        
        lowers = [0]*self.max_value
        for i in range(1, len(self.numbers_count)):
            lowers[i] = lowers[i-1] + self.numbers_count[i-1]
        return Stats(self.numbers_count, lowers, len(self.numbers))
