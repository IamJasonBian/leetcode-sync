class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        result = [list(intervals[0])]
        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                if result[-1][1] <= intervals[i][1]:
                    result[-1][1] = intervals[i][1]
            else:
                result.append(list(intervals[i]))                 
        return result
