class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(target + 1):
            for n in filter(lambda n: i >= n, nums):
                dp[i] += dp[i - n]
        return dp.pop()
