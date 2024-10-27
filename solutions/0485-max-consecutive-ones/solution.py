class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = mc = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                mc = max(mc, c)
                c = 0
        return max(mc, c)
