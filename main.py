from xallen1110.two_sum_data_structure.two_sum import TwoSum

def run_two_sum_data_structure():
    two_sum_structure = TwoSum()
    two_sum_structure.add(5)
    print(two_sum_structure.find(18))
    two_sum_structure.add(5)
    two_sum_structure.add(13)
    print(two_sum_structure.find(10))
    print(two_sum_structure.find(18))

if __name__ == '__main__':
    run_two_sum_data_structure()
