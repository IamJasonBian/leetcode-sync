class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for num, freq in fmap.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]: 
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
        return [num for _, num in heap]

# in host memory bullshit
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(str(Solution().topKFrequent(nums, next(inputs))).replace(" ", ""), file=f)
exit(0)
