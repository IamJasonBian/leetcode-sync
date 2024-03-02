from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add two dummy balloons at the beginning and end to handle the boundary conditions
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Initialize the dp array
        dp = [[0] * n for _ in range(n)]
        
        # Fill the dp array using the state transition formula
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        
        # The maximum coins that can be collected is dp[0][n-1]
        return dp[0][n-1]

