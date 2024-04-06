import heapq

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Trivial: We can add and remove from hashsets
        # Solution with no extra memory
        res = 0
        for n in nums:
            res = n ^ res
        return res


