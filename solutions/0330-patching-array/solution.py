from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1  # The smallest number we can't form
        i = 0
        length = len(nums)
        
        while miss <= n:
            if i < length and nums[i] <= miss:
                # If current number is less than or equal to miss,
                # we can extend our range to miss + nums[i]
                miss += nums[i]
                i += 1
            else:
                # We need to add 'miss' to the array
                miss += miss
                patches += 1
                
        return patches
