import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # push List into priority queue
        # pop out the next two

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        # Pop elements from the heap until we reach the kth largest element
        for _ in range(k - 1):
            heapq.heappop(max_heap)

        # The top of the heap is now the kth largest element
        return -heapq.heappop(max_heap)

        
