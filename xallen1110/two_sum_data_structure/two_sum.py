class TwoSum(object):
    
    def __init__(self):
        self.count_dict = {}
    
    def add(self, number):
        """
        number : int
        """
        if number in self.count_dict:
            self.count_dict[number] += 1
        else:
            self.count_dict[number] = 1
    
    def find(self, value):
        """
        value : int
        returns: bool
        """
        for num in self.count_dict:
            if value - num in self.count_dict and \
                (value - num != num or self.count_dict[num] > 1):
                return True
        return False
