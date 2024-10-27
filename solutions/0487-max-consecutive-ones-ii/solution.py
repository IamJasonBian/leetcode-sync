class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ws, wb, r = 0, -1, 0
        for idx, num in enumerate(nums):
            if num == 0:
                if wb >= 0:
                    ws = wb + 1  # Fixed: window starts AFTER previous zero
                wb = idx
            r = max(r, idx - ws + 1)
        
        r = max(r, len(nums) - ws)
        return r
