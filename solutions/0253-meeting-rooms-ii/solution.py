from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        starts = [s for s, _ in intervals]
        ends = [e for _, e in intervals]
        heapq.heapify(starts)
        heapq.heapify(ends)

        rooms = 0
        ongoing = 0
        while starts:
            if starts[0] < ends[0]:
                heapq.heappop(starts)
                ongoing += 1
                rooms = max(rooms, ongoing)
            else:

                heapq.heappop(ends)
                ongoing -= 1

        return rooms
