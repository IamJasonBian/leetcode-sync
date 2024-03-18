class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        
        # Add intervals ending before newInterval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        
        # Add the merged interval
        merged.append(newInterval)
        
        # Add intervals starting after newInterval ends
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
