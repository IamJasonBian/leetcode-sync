import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return len(min_heap)
