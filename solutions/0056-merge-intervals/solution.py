from typing import List
import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        heap = [(s, e) for s, e in intervals]
        heapq.heapify(heap)

        merged = []
        s, e = heapq.heappop(heap)

        while heap:
            ns, ne = heapq.heappop(heap)
            if ns <= e:
                e = max(e, ne)
            else:
                merged.append([s, e])
                s, e = ns, ne

        merged.append([s, e])
        return merged
