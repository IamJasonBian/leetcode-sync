from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Edge case: if there's only one element, return it
        if len(nums) == 1:
            return nums[0]
            
        # Not distinct element
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k-1]
