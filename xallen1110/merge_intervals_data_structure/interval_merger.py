import collections

class IntervalMerger(object):
    '''
    A class used to merge interval(s) to a graph (represented in connection-merged adjacent list)

    A list of initial intervals is needed to build the class and graph. After the setup, intervals 
    can be added to the class/graph one by one.

    TODO: Refactor this class to allow the addition of list of intervals more than one by one
    TODO: Improve implementation details especially for method __build_initial_graph 

    Example:
    Initial intervals 
        [(3,5), (7,8), (11,13), (4,7)]
    Graph will get setup as
        {(3,8): [(3,5), (7,8), (4,7)], 
        (11,13): [(11,13)]}
    If a new interval is added
        (11,16)
    Graph will become
        {(3,8): [(3,5), (7,8), (4,7)], 
        (11,16): [(11,13), (11,16)]}
    '''

    def __init__(self, intervals): 
        self.__graph = collections.defaultdict(list)
        self.__build_initial_graph(intervals) # self.__graph gets setup

    def get_merged_graph(self):
        return self.__graph

    def get_merged_intervals(self):
        return list(self.__graph.keys())

    def add_new_interval(self, interval):
        merged = False
        for graph_key in self.__graph:
            if self.__have_overlap(graph_key, interval):
                if interval[0] < graph_key[0] or interval[1] > graph_key[1]:
                    new_key = min(interval[0], graph_key[0]),  max(interval[1], graph_key[1])
                    self.__graph[new_key] = self.__graph[graph_key]
                    self.__graph[new_key].append(interval)
                    self.__graph.pop(graph_key)
                else:
                    self.__graph[graph_key].append(interval)
                merged = True
                break
        if not merged:
            self.__graph[interval].append(interval)

    def __have_overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # DFS in recursion
    def __merge_connection(self, input_interval, connection, visited, merged_range, merged_set):
        if input_interval in visited:
            return
        
        visited.add(input_interval)
        merged_set.add(input_interval)
        merged_range[0] = min(merged_range[0], input_interval[0])
        merged_range[1] = max(merged_range[1], input_interval[1])
        for interval in connection[input_interval]:
            self.__merge_connection(interval, connection, visited, merged_range, merged_set)
        return

    def __build_initial_graph(self, intervals):
        # connection is represented in adjacent list containing connections among intervals
        connection = collections.defaultdict(list)
        for interval_i in intervals:
            for interval_j in intervals:
                if interval_i != interval_j and self.__have_overlap(interval_i, interval_j):
                    connection[interval_i].append(interval_j)
                    connection[interval_j].append(interval_i)
        
        # Transform the above connection and intervals to self.__graph using DFS
        visited = set()
        for interval in intervals:
            if interval in visited:
                continue

            if interval not in connection:
                self.__graph[interval].append(interval)
            else:
                merged_range = [interval[0], interval[1]]
                merged_set = set()
                self.__merge_connection(interval, connection, visited, merged_range, merged_set)
                self.__graph[tuple(merged_range)].extend(merged_set)
        
        return self.__graph
