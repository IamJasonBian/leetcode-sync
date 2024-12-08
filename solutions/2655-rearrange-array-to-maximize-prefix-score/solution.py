class Solution:
    def maxScore(self, nums: List[int]) -> int:
        negative = []
        posValue = 0
        for num in nums:
            if num < 0:
                negative.append(num)
            if num > 0:
                posValue += num   
        if posValue == 0:
            return 0
        if len(negative) == 0:
            return len(nums)
        ans = len(nums) - len(negative)
        negative.sort(reverse=True)
        for num in negative:
            posValue += num
            if posValue > 0:
                ans += 1
            else: break
        return ans
