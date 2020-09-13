from xallen1110.two_sum_data_structure.two_sum import TwoSum
from xallen1110.merge_intervals_data_structure.interval_merger import IntervalMerger

def run_two_sum_data_structure():
    two_sum_structure = TwoSum()
    two_sum_structure.add(5)
    print(two_sum_structure.find(18))
    two_sum_structure.add(5)
    two_sum_structure.add(13)
    print(two_sum_structure.find(10))
    print(two_sum_structure.find(18))

def run_interval_merger():
    interval_merger = IntervalMerger([(3,5), (7,8), (11,13), (4,7)])
    print(interval_merger.get_merged_graph())
    print(interval_merger.get_merged_intervals())
    interval_merger.add_new_interval((11,16))
    print(interval_merger.get_merged_graph())
    print(interval_merger.get_merged_intervals())

if __name__ == '__main__':
    run_two_sum_data_structure()
    print("---")
    run_interval_merger()
