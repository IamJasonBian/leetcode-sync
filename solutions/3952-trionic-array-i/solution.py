from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n-2):
            # nums[0..p] strictly increasing
            if not all(nums[i] < nums[i+1] for i in range(p)):
                continue
            for q in range(p+1, n-1):
                # nums[p..q] strictly decreasing
                if not all(nums[i] > nums[i+1] for i in range(p, q)):
                    continue
                # nums[q..n-1] strictly increasing
                if all(nums[i] < nums[i+1] for i in range(q, n-1)):
                    return True
        return False
