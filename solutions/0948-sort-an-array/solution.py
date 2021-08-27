class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for t in nums :
            heapq.heappush(heap, t)
        to_ret = []
        while len(heap) > 0:
            to_ret.append(heapq.heappop(heap))
        return to_ret
