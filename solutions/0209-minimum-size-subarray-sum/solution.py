from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        right = 0
        sum = 0
        left = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return 0 if min_length == float('inf') else min_length
