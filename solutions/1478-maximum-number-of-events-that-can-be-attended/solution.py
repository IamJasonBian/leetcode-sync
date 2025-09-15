class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        ls = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(ls, events[j][1])
                j += 1
            while ls and ls[0] < i:
                heapq.heappop(ls)
            if ls:
                heapq.heappop(ls)
                ans += 1

        return ans
